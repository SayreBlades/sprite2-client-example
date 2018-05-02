from dask import bag as db
from dask.diagnostics import ProgressBar
import sprite2.aws
import sprite2.dask
import math


# primality test
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


# chunk 10 million
d = (db.range(100000000, npartitions=100)
       .filter(is_prime)
       .count())

# compute result
with ProgressBar():
    result = d.compute(get=sprite2.dask.get)
print(result)
