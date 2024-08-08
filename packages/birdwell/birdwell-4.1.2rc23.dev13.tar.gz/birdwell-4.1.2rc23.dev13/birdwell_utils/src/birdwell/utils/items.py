

def fracture(lst: list, size: int | None = 100, with_idx=False) -> list | tuple[list, int]:
    for i in range(0, len(lst), size):
        if with_idx:
            yield lst[i:i + size], i
        else:
            yield lst[i:i + size]
