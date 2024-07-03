TODO: More details

## Lumi's typesystem, an overview

Lumi is designed around a combination of gradual set-theoretic typing,
based on [prior academic work](https://www.irif.fr/~gc/papers/icfp17.pdf)
and a partial inclusion of support for algebraic effects.
Lumi *may* at some much later date gain support for generalized algebraic effects.


### Subtyping

1. Subtyping follows from the set-theoretic rules. (TODO: longer doucmentation in a non-overview)
2. It is an error to declare nominal subtypes which violate concetps of safe substitution (TODO: define safe substitution)
3. Structural subtyping in Lumi is limited to what is statically provable.

### Denotable types

- All types which can be statically proven should be both expressible and denotable
- Following from this, Structural types may in some cases only be denotable as type bounds
- If there are a large number of cases that suffer ergonomically for this,
  syntax better supporting it should be the answer, not allowing it unsafely or ignoring an ergonomic issue.

### Exceptions

Most academic work here has not treated Exceptions as control flow or as having values.
Lumi has a partial understanding of the different kinds of Exceptions in the CPython runtime, and
differentiates between the effects of a subset of them.

In particular, Lumi encodes a limited amount of type information or control flow information based on
each of the following python Exceptions. (N.B. This may not be an exhaustive list.)

- StopIteration
- KeyError
- IndexError
- GeneratorExit
- asyncio.CancelledError
- KeyboardInterrupt
- OverflowError
- ZeroDivisionError
- LookupError
- ImportError
- NotImplementedError

Despite having typesystem encoded knowledge about exceptions, **Lumi does not, and will not, have checked exceptions**

### Exceptions carry limited type information and are runtime values

While exceptions are not checked and you are not required to catch all possible exceptions, never the less, exceptions are values that when raised trigger alternative code flow.

As such, given an annotation : `T`, Lumi understands this as `T | Never[Error]`

### Why `Never[Error]` exists, and why and how Lumi has multuple understandings of `Never`

Lumi has multiple kinds of "Never" categorized by a partially encoded understanding of
algebraic effects.

These are

- `Never[Logical]`
- `Never[Error]`

Of these, `Never[Error]` is implicitly always possible when targeting the CPython
runtime (Note: currently this is the only target)

`Never[Error]` is not considered to be a subtype of any runtime type,
and is essentially the effect of raising an exception.
While this is always implicitly possible, you
may explicitly mark functions that always raise with this return type.

`Never[Logical]` is the logical abscence of a valid type, usually by exhaustive narrowing
`Never[Logical]` *is not* valid as a return type in Lumi as it is impossible to return a non-existant value.
`Never[Logical]` *is* a subtype of all concrete types.