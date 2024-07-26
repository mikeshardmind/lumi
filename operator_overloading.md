
- Lumi allows operator overloading.
- Operator overloading is only allowed for types where the relationship has been declared
  implementations of operators will be checked against such declarations.


ie. (syntax not final)

```
lumi binop-relation: datetime + timedelta = datetime
```

This avoids a few issues that exist in python.

In python, given an expression, knowing the types of {z,x} or {z, y} does not
give you knowledgeof the unknown of x or y

x + y = z

The reasons for this are a combination of both LHS and RHS being able to implement
most binops (some exceptions like `__matmul__`, don't have a corresponding RHS version `__rmatmul__`)
for the other operand noncooperatively, and that the [RHS steals priority from the LHS
when the RHS is a subclass of the LHS](<https://github.com/python/cpython/commit/2ed6bf87c9ce5d2e8a0eb33f7aa6503196205a0c#diff-ba56d44ce0dd731d979970b966fde9d8dd15d12a82f727a052a8ad48d4a49363>).

Given the priority placed on inference doing most of the work, asking people who are participating in
operator overloading to just list out the participating overloads their types define
prevents that lack of knowledge. In the future, this may result in special syntax for implementing this
instead, with Lumi generating the correct dunder methods for the generated python code.