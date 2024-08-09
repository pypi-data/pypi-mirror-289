# Expected Value Package

This is a simple package which offers functions to calculate the expected value and the total probability for the outcome data type. 

# Importing

You can import the expected value package by:
``` 
from expected_value import expected_value
```

# Using Expected Value

You can use the Expected Value command using:
```
o1 = outcome.Outcome("win", float(2), probability.Probability(.5))
o2 = outcome.Outcome("tie", float(10), probability.Probability(.1))
o3 = outcome.Outcome("lose", float(-1), probability.Probability(.4))

os = [o1, o2, o3]

print(expected_value(os))
```
which will output 1.6.

You can use the permutations (where order does matter) command using:
```
o1 = outcome.Outcome("win", float(2), probability.Probability(.5))
o2 = outcome.Outcome("tie", float(10), probability.Probability(.1))
o3 = outcome.Outcome("lose", float(-1), probability.Probability(.4))

os = [o1, o2, o3]

print(total_probability(os))
```
which will output 1.0.
