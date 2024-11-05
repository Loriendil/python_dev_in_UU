from fake_math import divide as fake_div
from true_math import divide as true_div

_result1 = fake_div(15, 12)
_result2 = true_div(2, 3)
_result3 = fake_div(3,0)
_result4 = true_div(-1, 0)

print(_result1)
print(_result2)
print(_result3)
print(_result4)