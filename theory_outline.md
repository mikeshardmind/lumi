### This is just here for me temporarily, so I don't lose track of anything I need to account for


- Unions and Intersections
- Filtering by constraint
- subtyping (`<:`)
- refinement types (via guard clauses, Literals)
- Negation, limited to negation of sets of runtime types
- Rules defining a relation between sized numeric types in the type system
- Multiply Expressible lower and upper type bounds, constraints
- Variance interaction with type bounds
- Generics

To further explore:

- Higher ranked types (vs fully decidable Unification)
- Dependent types
- TypeConstructors as an explicit concept (ie. type[T] vs Callable[Paramspec.fromcallable[T], T])
  to deal with python's issue with ignoring LSP for construction, and covariant type
- There's probbaly some issues interacting with CPython apis that expect sequences due to variance mismatches...
  need to find a way to mark these in a lumi stub based on how lumi code can safely interact with these
  functions