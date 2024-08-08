from __future__ import annotations
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Callable, TypeVar, Final, Generator, Concatenate, Self, Iterator, cast, ClassVar

from .items import fracture


def wait_threads(threads: list[threading.Thread], verbose=True):
    while len(threads):
        for idx in range(len(threads)-1, -1, -1):
            if not threads[idx].is_alive():
                threads.pop(idx)
                if verbose:
                    print(f'REMAINING THREADS {len(threads)}')


def thread_wrapped(func, items: list, thread_count=8, per_call=1,
                   output_mode=None, verbose=False, respawns=-1):
    """

    Parameters
    ----------
    func : function called with item chunks passed as only arg
    items : full list of items to process with func
    thread_count : number of threads to perform work with
    per_call : number of items to pass to func per call
    output_mode: func output handling
    verbose: print cycle / remaining / current on func call
    respawns: define max exception count; int used as a direct limit,
        float value used to calculate limit using the formula: respawns = int(len(items) // per_call * respawns)

    """

    if not isinstance(per_call, int) or per_call <= 0:
        raise ValueError('Items per call must be positive int')

    running = True  # used to stop threads via main
    threads = []
    packs = items[::] if per_call == 1 else list(fracture(items, per_call))
    cycles, revives = 0, 0

    # calculate scaling respawns
    if isinstance(respawns, float):
        respawns = int(len(items) // per_call * respawns)

    # func is wrapped to give calling thread access to context
    def wrapped_func():
        # thread will continue running until work is complete or interrupted
        while packs and running:
            item = packs.pop()
            nonlocal cycles
            cycles += 1
            if verbose:
                print(f'CYCLE: {cycles:_}, REMAIN: {len(packs):_} CURRENT: {item}')

            res = func(item)
            if output_mode == 'append' and res:
                packs.extend(res)

    # initial thread population
    for i in range(thread_count):
        tr = threading.Thread(target=wrapped_func, daemon=True)
        threads.append(tr)
        tr.start()

    # try/except used for shutdown control
    try:
        # monitor thread progress and block main
        # note: could also make this a threaded operation to not block
        while threads:
            # reversed index used to enable popping
            for idx in range(len(threads)-1, -1, -1):
                # remove as completed/errored
                if not threads[idx].is_alive():
                    threads.pop(idx)

            # ensure threadpool runs at full capacity while items are available
            if respawns is not None and running and (len(threads) < thread_count < len(packs)):
                if respawns == -1 or respawns - revives >= 0:

                    etc = '' if not verbose else (
                        f'REVIVE_COUNT=[{revives + 1}] '
                        f'REMAINING_RESPAWNS=[{'UNLIMITED' if respawns == -1 else respawns - revives}] '
                        f'SPAWNING REPLACEMENT.')

                    print(f'EARLY THREAD TERMINATION DETECTED. {etc}')
                    # replace dead threads
                    tr = threading.Thread(target=wrapped_func, daemon=True)
                    threads.append(tr)
                    tr.start()
                    revives += 1

    # propagate stop/interrupt to inner threads
    except KeyboardInterrupt as e:
        running = False
        raise e


@dataclass
class BackgroundCall[_R]:
    result: _R | None
    thread: threading.Thread | None


class BackgroundThread[**_P, _R]:
    def __init__(self, func: Callable[_P, _R], raise_exceptions=False, timeout=None):
        self.func: Callable[_P, _R] = func
        self.data: BackgroundCall[_R] = BackgroundCall(result=None, thread=None)
        # self.result: _R = None
        # self.thread: threading.Thread | None = None
        self.raise_exceptions = raise_exceptions
        self.timeout = timeout
    #
    # def wrapped(self, *args: _P.args, **kwargs: _P.kwargs) -> None:
    #     try:
    #         self.data.result = self.func(*args, **kwargs)
    #     except Exception as e:
    #         self.data.result = e

    @contextmanager
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> Generator[BackgroundCall[_R], None, None]:
        def inner_call():
            try:
                self.data.result = self.func(*args, **kwargs)
            except Exception as e:
                self.data.result = e

        self.data.thread = threading.Thread(target=inner_call, daemon=True)
        self.data.thread.start()
        try:
            yield self.data
        finally:
            self.data.thread.join(timeout=self.timeout)
            if self.raise_exceptions and isinstance(self.data.result, Exception):
                raise self.data.result


@contextmanager
def background_thread[**_P, _R](func: Callable[[_P], _R], *args: _P.args, **kwargs: _P.kwargs):
    result: _R = None
    res: BackgroundCall = BackgroundCall(result=result, thread=None)

    def wrapped():
        try:
            res.result = func(*args, **kwargs)
        except Exception as e:
            res.result = e

    res.thread = threading.Thread(target=wrapped, daemon=True)
    res.thread.start()
    try:
        yield res
    finally:
        res.thread.join()
