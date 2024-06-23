## major TODOs

There's a lot here that if you find alarming may just be that not everything here important is laid out yet.
feel free to open a discussion asking about it if so.

### isinstance

lumi replaces isinstance with a type-safe implementation that tracks certain things.

### composition vs inheritence

- Lumi encourages composition over inheritence and functional patterns where applicable.
- Lumi will by default disallow unsafe override of behavior.
- Lumi will allow a directive that says "I want the behavior of this, but am okay with losing it as a supertype" This must be explicitly stated. This results in Lumi generating a new type.

### Use of super

- (Undecided, requires exploration) Lumi will wither reject all uses or reject unsafe uses of super

### Gradual typing

- While Lumi allows *accepting* a a gradual type, a function defined in Lumi may not return a gradual type.
- Lumi has directives for allowing safe, checked use to be generated when partially applying functions recieved from python

### builtins

- Some python builtins will be replaced by default in Lumi.
  You may access the original python builtin via the Python.builtins namespace,
  but these recieve additional scrutiny around narrowing behaviors.

### typing features

- Unsafe coercions are not supported by Lumi
- A few additional tools will exist in lumi to support describing certain kinds of APIs that already exist,
  but cover cases where it may not strictly desirable to support continued development of new code like it.

Examples: `VarArgsReturnList` and `ReturnedHeterogenousList` (planned)

- This is only allowed in Lumi in cases that do not retain a reference to the returned list
- CPython code described with this must not mutate the list once it is returned.
- You are allowed to access each element of it or destructure it on an individual basis, or treat it as a normal list, but not both.
- If Lumi sees this passed to a non-Lumi function or sees you mutate it, it is not allowed to be treated more similarly to a tuple with known individual elements.
- Lumi's error messages will reflect where this occured.
- Lumi allows describing Lumi code with `VarArgsReturnList` but not with `ReturnedHeterogenousList`, the latter exists only for describing existing CPython code. The former must be a "what went in went back out"

This is a common occurance in various Cpython apis and libraries. The best example of this is `asyncio.gather`