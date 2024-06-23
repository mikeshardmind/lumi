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