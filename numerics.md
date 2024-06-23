### Lumi's numeric system

TODO: further details, links to theory

- Lumi comes with support for arbitrary sized and machine sized numerics out of the box
- Lumi's numeric types do not automatically convert between domains, but allow resizing. Resizing behavior is based on the defined behavior of the numeric for overflow and underflow. Converting between types with differing precisions rather than differing bounds requires an explicit conversion.
- Long term: Unit aware numerics
- Operator overloading on numerics is limited, but expressive.
- Types define the behavior for saturation, error, or wrapping

User defined types may register which operations are defined

User derived numerics using the default implementation is possible (pseudo syntax, syntax still under development)
This is the encouraged manner to interact with numerics in lumi as safe code will be generated

```
lumi Derived Numeric:
  name: Int64
  derives: SizedInt
  maxsize: 9,223,372,036,854,775,807
  minsize: -9,223,372,036,854,775,808
  overflow: error
  underflow: error
  division: truncate
```
(Note: several common machine sized types come pre-defined)
