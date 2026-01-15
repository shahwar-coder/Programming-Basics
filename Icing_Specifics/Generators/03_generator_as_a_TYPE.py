from typing import Generator

"""
Generator[a, b, c]  ->  Generator[YieldType, SendType, ReturnType]

Mental model:
Generator[OUT, IN, END]

OUT  : values produced using `yield`
IN   : values received via `.send()`
END  : final value returned when generator finishes
"""

# Example using all three parameters
def item_processor() -> Generator[int, str, int]:
    total = 0

    while True:
        item = yield total        # OUT (YieldType = int)

        if item == "STOP":
            return total          # END (ReturnType = int)

        total += len(item)        # IN (SendType = str)


# ---- How it behaves ----
gen = item_processor()

next(gen)             # yields int
gen.send("apple")     # sends str, yields int
gen.send("banana")    # sends str, yields int

"""
gen.send("STOP") raises StopIteration
StopIteration.value contains the return value (END)
"""

# Most common backend-style usage:
# Generator[int, None, None]
# - yields int
# - no .send()
# - no meaningful return
