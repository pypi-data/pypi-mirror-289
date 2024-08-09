# Outcome Package

This is a simple package for the outcome data type which includes the outcomes name, its value, and its probability which can be found in probability-tb. 

# Importing

You can import the outcome package by:
``` 
from outcome_tb import outcome
```

# Using Outcome

You can use the outcome type using:
```
from probability import probability

o = Outcome("outcome1", float(5), probability.Probability(.5))

print(o.outcome_name, o.outcome_value, o.outcome_probability.value)
```
which will have the values o.outcome_name => "outcome1", o.outcome_value => 5.0, outcome.outcome_probabilty.value => .5.
