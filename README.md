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
a good thing and that there is just too much depending on this to change it,
but when issues with this are raised, concerns about type safety are often
dismissed as "merely academic" or by dismissing that users want more type safety
than is currently provided or even possible.

One pragmatic answer to this as a user would be to go use a language that
enables users to have what they want from it, but this ignores existing code,
the cost of converting, and a wealth of python libraries.

There is no strong statically checkable type safety to be had through python's
type system. Those who care about it must by neccessity ignore the specification,
and the specification being treated in this way prevents any
"specification-compliant" type checker from fixing the problems.
This goes so deep as to have lies about the basic structure of builtin types specified.

So the answer to why, is that I've found this to be a large enough hole in
what exists in python that does not seem possible to resolve by
cooperation with those involved as members of CPython.


### A measured followup to the above

Many of the issues with python's type system are old, or in some cases even
predate the type system. ABC registration, python's float behavior,
and a few others apply here.

Many further issues with python's type system are deep seated and would have
excessive costs to fix to existing code bases.

Some of them are just really hard problems that even other languages with a
focus on soundness have gotten wrong or partially wrong before (variance especially)

There are tradeoffs that have to be considered when making decisions at the
language level, and right now, the balance on some of these issues has been
to keep certain kinds of unsoundness in favor of stability of existing systems.

I hope this becomes a useful tool that people can rely on, and I think it also
can help assist CPython upstream in having another lens to view some of the
problems in that isn't just academic, but implemented and ready to use.


## Primary Goals

- Typed code is checked for type safety.
- Typed code may be called from untyped code.
- Typed code may call untyped code, with some caveats.
- Replace python's type system with an external one.
- Provide a few additional implemented base types
- For it to be easy to write the correct type.
- Provide additional syntax supporting the ideas that enable people to write type safe code with less effort.

## Long term goals

- Providing type information should allow emitting optimized compiled modules.
- Pure Lumi code should be possible to emit a binary which does not require the python runtime.

## Non-goals

- Making all valid python code possible to type.
- Upstream this (At least at this point in time.)
