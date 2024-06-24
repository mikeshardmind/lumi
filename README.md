# lumi
A replacement for python's type system.

## What?

Write code that looks and feels like python in a type safe manner,
leverage existing python code, get a python module that is type checked.
Have best effort type annotations for the existing type system as well.


## Why?

All projects worth pursuing need to first answer "is this needed?"

Python's type system is built on a foundation of "pragmatic lies".
The current leadership surrounding typing decisions for python sees this as
virtuous and good that it is pragmatic, but when issues with this are raised,
concerns about type safety are dismissed as "merely academic" or by dismissing
that users want more type safety than is currently provided.

A pragmatic answer would be to go use a language that enables users to have
what they want from it, but this ignores existing code, the cost of converting,
and a wealth of python libraries.

There is no type safety to be had through python's type system.
Those who care about it must by neccessity ignore the specification,
and the specification being treated in this way prevents any
"compliant" type checker from fixing the problems. This goes so deep as to have
lies about the basic structure of builtin types specified.

So the answer to why, is that I've found this to be a large enough hole in
what exists in python that does not seem possible to resolve by
cooperation with those involved as members of CPython.


## Primary Goals

- Typed code is checked for type safety.
- Typed code may be called from untyped code.
- Typed code may call untyped code, with some caveats.
- Replace python's type system with an external one.
- Provide a few additional implemented base types
- For it to be easy to write the correct type.

## Secondary Goals

- Providing type information should allow emitting optimized compiled modules.
- Provide additional syntax supporting the ideas that enable people to write type safe code with less effort.

## Non-goals

- Making all valid python code possible to type.
- Upstream this (At least at this point in time.)
