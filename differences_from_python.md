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

### Never

- Lumi has multiple concepts of Never. While Never should always indicate a lack of a return, Lumi differentiates between reasons for that. This allows Lumi to determine when functions are suitable replacements in subclasses.

Never is not generic over specific exceptions.

Generated Python code will re-reduce all special kinds of Never to just `Never`, as this is not a concept python's type system supports.

The pathological case this prevents is below, see the section on Never in the theory overview for more details.

```py
class A:
    def foo(self) -> Literal[1]:
      return 1

class B:
  def foo(self) -> Literal["this"]:
    return "this"


class C(A, B):
  def foo(self) -> Never:
    raise RuntimeError()
```

A strict interpretation of subtyping without accounting for the concept that
subtypes should remain compatible from the perspective of intent to use the method would allow
C to have a foo that isn't a suitable replacement for either A or B, let alone both.


### Structural types

- Lumi does not allow structural types as return types
- Lumi does allow type variables bound to structural types as return types
- Structural types do not have their own variance.
  Variance is checked as if the static type qualifying
  as having that structure would have appropriate variance.

### ABCs, and other means of lying about subtyping

- Lumi does not support python ABCs or the ABC.register method from Lumi code.
  Lumi *will* emit use of some collections.abc.register methods to allow interoperability
  with existing python code.
- Lumi does not allow implementing `__instancecheck__` or `__subclasscheck__`


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


## Copied from discord, needs formatting and explanations (TODO)

builtins:

Pure logic
-----------
abs()
all()
any()
bin()
bool()
chr()
divmod()
enumerate()
filter()
format()
hex()
len()
map()
max()
min()
oct()
ord()
pow()
reversed()
round()
sum()
zip()


Should be fine
---------------
aiter()
anext()
ascii()
classmethod()
dir()
globals()
hash()
id()
input()
iter()
locals()
next()
print()
property()
range()
repr()
slice()
sorted()
staticmethod()
str()
vars()

Unchanged (for now) Data types
--------------------
bytearray()
bytes()
callable()
dict()
frozenset()
int()
list()
memoryview()
object()
set()
tuple()
complex()

Modified builtins
-----------------------


float()  -> numpy.float64 (for now, temp hack), float literals replaced with numpy.float64("literal")
isinstance()
issubclass()

type()  (single parameter only)
open()  (mode parameter changes, not yet implemented)

Removed builtins
----------------
compile()
delattr()
eval()
exec()
help()

Temp(?) removed builtins
---------------------
breakpoint()
super()
__import__()
getattr()
setattr()
hasattr()