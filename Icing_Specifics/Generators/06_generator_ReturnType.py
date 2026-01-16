"""
Generator ReturnType (Generator[YieldType, SendType, ReturnType])

• ReturnType = the value produced when the generator *finishes*
  (via `return value` inside the generator)

• When a generator ends:
    - Python raises StopIteration
    - StopIteration.value == ReturnType

• Example meaning:
    Generator[int, None, str]
    - yields int values
    - does NOT accept values via .send()
    - returns a str at the end

• Example:
    def g() -> Generator[int, None, str]:
        yield 1
        yield 2
        return "done"

• Runtime behavior:
    gen = g()
    next(gen)  → 1
    next(gen)  → 2
    next(gen)  → raises StopIteration("done")

• Accessing ReturnType:
    try:
        next(gen)
    except StopIteration as e:
        result = e.value  # "done"

• Common case:
    - Most generators use `return None`
    - ReturnType is often None in type hints
"""
