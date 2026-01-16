"""
SendType (Generator[YieldType, SendType, ReturnType]) — concise summary

• SendType = type of value sent *into* a paused generator via .send(value)

• The value passed to .send(x) becomes the result of the `yield` expression

• First resume must be next(gen) or gen.send(None)
  (you cannot send a real value before the first yield)

• Example meaning:
    Generator[int, str, None]
    - yields int values
    - expects str values from .send()
    - returns None when finished

• At runtime:
    value = yield 0
    # `value` receives whatever is passed to .send(...)

• If you call:
    gen.send("hello")
  then:
    value == "hello"

• If SendType is None:
    - generator does not expect any external input
    - you only use next(gen), not .send(x)
"""
