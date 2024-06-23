
- Lumi allows operator overloading.
- Operator overloading is only allowed for types where the relationship has been declared
  implementations of operators will be checked against such declarations.


ie. (syntax not final)

```
lumi binop-relation: datetime + timedelta = datetime
```

lumi also allows this to be expressed for broadcasting: (TODO)
