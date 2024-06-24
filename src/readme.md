## lumi_runtime

These are used by lumi when generating python code

### builtins.py

This contains all of the type-safe replaced builtin behavior.

### type_forms.py

This contains type forms that do not exist in python's type system.
These are available for tools which wish to introspect Lumi generated code
Where possible, they are defined in such a way that the existing
*specification compliant* type system will understand them,
but this is done on a "best effort" basis. Use of `Any` is prefered
for cases where python's type system cannot understand.
