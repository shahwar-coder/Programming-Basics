'''
Example of time calculation
'''

import time
def test_runtime():
    start = time.time()
    sum(range(10**6))
    end = time.time()
    print("Time Taken:", end - start)
