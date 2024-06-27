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

### TypeVariable use and constraint solving

TypeVariables do not necessarily need to correspond to another TypeVariable use

TypeVariables generally can have 4 ways of appearing:

- 1 to 1 ie:

`def foo(x: T) -> T: ...`

- many to 1

`def foo(x: T, y: T) -> T: ...`

- 1 to many

`class Foo[T]: ... # multiple uses of T in body`

or

`def foo[T](x: T, y: T): ...`

(or 1 to many to 1):

`def foo[T](x: T, y: T) -> T: ...`

- free standing, no clear relation

`def foo (x: T, y: T) -> None: ...` or even just `def foo(x: T) -> None: ...`

In the 1:1 case, the input type is clearly the output type
In the many to 1 case, the direction of code flow is many inputs, 1 output, so the types are collected into a union.
In the one to many (and by extension, the one to many to one) case the initial subscripted type is used.
In the freestanding case, lumi does not assume a direct association between these types, but does still require that there be a type that satisfies the presented constraints.

This becomes clearer when looking at the following python example:

```py
T = TypeVar("T")

def foo(x: T, y: T) -> T:
    ...

#vs
IntStr = TypeVar("IntStr", int, str)

def bar(x: IntStr, y: IntStr):
    ...

reveal_type(foo(1, "two"))  # Should be int | str or object, depending on inference model
reveal_type(bar(1, "two"))  # should be rejected at call, there is no type which satisfies these constraints
```

Of current (2024-06-27) "mainstream, specification participating typecheckers",

- mypy and pytype each fail at some part of this this.
- pyright fails at other examples in the thread this recently arose in (see link below)
- Pyre gets this correct.


The "Correct" behavior is currently not specified within Cpython.


> Constraint solving can be very costly, so implementations take certain shortcuts and make certain assumptions. These can fail to find certain solutions. I suspect that’s what’s happening in this case for mypy.
> Constraint solving behaviors are not discussed in the typing spec currently, and I think it will be a long time (if ever) before they are. Spec’ing this behavior would be very difficult as it involves many heuristics, edge cases, behaviors that differ between type checkers, and limitations dictated by internal implementation choices. It also relies on other concepts (like value-constrained TypeVars) that are not yet well spec’ed. If you want to pursue standardization in this space, it will take significant time and effort.


See discussion of the topic [here](https://discuss.python.org/t/constraining-generic-argument-types/56809)


Lumi has a specified behavior (TODO: definitions this specification depends on need to be mroe rigorous)


Constraints should be solved by analyzing the directional flow of code to determine if there is a set-theoretic type which satisfies the constraints. If so, that's the type, otherwise the code is invalid.
