### overloads

- Lumi does not allow overloads to share an implementation, and requires each type specification to have it's own implementation.
- Lumi will statically skip calling an overload-dispatch system when the types are statically known, generating a direct call to the implementation.
- This results in all overload branches being type safe, while minimizing performance concerns.
- Lumi will generate an efficient underlying dispatch mechanism.