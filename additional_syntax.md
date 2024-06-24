### Additional syntax

Lumi provides additional syntax for certain things which will result in generating appropriate code,
while retaining the type checking benefits of that code. In cases where CPython's type system cannot
appropriately handle this, they will be typed in the generated module as `Any` rather than lie about this.
Attempts will be made to generate at minimum sensible structural types for python consumers of your module.


Currently planned:

- Efficient Data only structs
- ADTs
- Derived numerical types and refinement types (see numerics.md)
- Differing overload behavior (see overloads.md)
- Guard clauses
- None aware operations (will expand to python code that short circuits on None)
- Late bound function defaults (will still generate a sentinel, but allows ensuring the
  type system checks that you removed the generated sentinel by not having this exist in your code)