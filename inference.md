## Inference in Lumi

### Basic principles

1. The default type for an unannotated type is not `Any` but `auto`
2. Operator based inference errs towards a specific mathematical perspective which is more restrictive.
3. Lumi will prompt for more type information in some cases if `auto` cannot produce a reasonable type.


### Operator resolution

Given the following:

```
def add(a, b) -> int:
    return a + b
```


Lumi will allow use of add such that a + b -> int is valid

Without types specified on either the LHS or RHS, some operators are
restricted based on mathematical assumptions.

This may prevent some types from being accepted, for instance

```
def add(a + b):
    print(a + b)
```

is allowed any commutative addition between a and b.
The default behavior for operators and inferenence
when both LHS and RHS is to consider if the operator
would typically be commutative for numeric use.
(TODO: table)

example  {`+`, `*`} are assumed commutative when LHS and RHS are absent,
but {`-`, `/`} are assumed not

In general, at least one of LHS, RHS, or the resulting type needs to be
determinable if the result of the operator use would impact the return type
of a function.