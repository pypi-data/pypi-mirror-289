"A library for playing with strings."

__all__: tuple = (
    "height", "width", "size", "padding", "mirror", "box"
)

def height(__s: str, /) -> int:
    "Returns the height of the string."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    return len(__s.splitlines())

def width(__s: str, /) -> int:
    "Returns the width of the string."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if not __s: return 0
    return len(max(__s.splitlines()))

def size(__s: str, /) -> int:
    "Returns the total (square) size of a string."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if not __s: return 0
    return height(__s) * width(__s)

def padding(__s: str, /) -> str:
    "Returns the given string with padding."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if (__s == "") or (height(__s) == 1): return __s
    
    return "\n".join(f"{line:<{width(__s)}}" for line in __s.splitlines())

def mirror(__s: str, /) -> str:
    "Returns the given string but with each line reversed (the order of the lines is not reversed)."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if __s == "": return ""
    
    return "\n".join(line[::-1] for line in padding(__s).splitlines())

def box(__s: str, /) -> str:
    "Returns a 'box' with the given string as its content."
    if not isinstance(__s, str):
        raise TypeError(f"expected 'str' but got {type(__s).__name__!r}")
    
    if __s == "": return "┌┐\n└┘"
    result: list = [f"┌{'─' * width(__s)}┐"]
    
    for line in __s.splitlines():
        result.append(f"│{line + ' ' * (width(__s) - len(line))}│")
    
    result.append(f"└{'─' * width(__s)}┘")
    
    return "\n".join(result)