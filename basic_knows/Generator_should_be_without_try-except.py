'''
GENERATOR ERROR HANDLING — SUMMARY

1. A generator’s responsibility:
   - Yield values lazily
   - Preserve execution state between yields
   - NOT decide how errors should be handled

2. Why generators usually SHOULD NOT use try/except:
   - Catching exceptions hides data problems
   - Caller loses visibility into failures
   - Silent skips can cause data corruption
   - Debugging becomes difficult

3. Correct design principle:
   - Let exceptions propagate naturally
   - Handle errors at the consumption boundary (caller side)

4. Where try/except BELONGS:
   - Around next(generator)
   - Around the loop consuming the generator
   - At system boundaries (API, file, DB, user input)

5. Rule of thumb:
   - If the generator cannot recover meaningfully,
     it should NOT catch the exception.

MENTAL MODEL:
Generator = data producer
Caller     = error policy owner
'''
