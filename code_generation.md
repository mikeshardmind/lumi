
## Guiding principles of code generation

1. If it can be safely statically eliminated, do so.
2. Generated python code should remain understandable to those who known python
3. Generated code should behave in an obvious manner.
   Said obviousness is allowed to rely on the reader needing to know what Lumi's purpose is.
4. Methods of code generation should be easy to understand.



Example:

```
type Bitfield = uint64
type TrustRole = Literal["admin", "moderator", "member"]

lumi record User:
    fields:
        id: uint64
        permissions: Bitfield
        role: TrustRole | None
    equality: {id, permissions, role}
    hashable: True
    ordering: False
    frozen: True
    repr: {id}


def filter_users_by_permissions(users: list[User] => [], permissions: Bitfield = Bitfield(0)) -> Iterator[User]:
    for user in users:
        if permissions & user.permissions = permissions:
            yield user
```

Should generate python that looks like:

```py
import reprlib
from typing import Generator, Any, Never

from lumi.types import uint64, MISSING
from lumi.exceptions import FrozenRecordError

type Bitfield = uint64
type TrustRole = Literal["admin", "moderator", "member"]


class User:
    __slots__ = ("id", "permissions", "role")
    id: uint64
    permissions: Bitfield
    role: TrustRole | None

    def __init__(self, id_: uint64, permissions: Bitfield, role: TrustRole | None):
        object.__setattr__(self, "id", id_)
        object.__setattr__(self, "permissions", permissions)
        object.__setattr__(self, "role", role)

    def __setattr__(self, name: str, value: Any) -> Never:
        raise FrozenRecordError("Cannot assign to field {name}")

    def __delattr__(self, name: str) -> Never:
        raise FrozenRecordError("Cannot delete field {name}")

    def __repr__(self) -> str:
        return f"<User Record Type: id = {self.id!r}>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return (self.id, self.permissions, self.role) == (other.id, other.permissions, other.role)

    def __hash__(self) -> int:
        type_hash = hash(f"Lumi Generated {type(self).__module__} {type(self).__qualname__}")
        return hash((type_hash, self.id, self.permissions, self.role))


def filter_users_by_permissions(
    users: list[User] = MISSING, permissions: Bitfield = Bitfield(0)
) -> Generator[User, None, None]:
    if users is MISSING:
        users = []
    for user in users:
        if permissions & user.permissions = permissions:
            yield user
```


A few things to note about this example

1. Currently, this is a handwritten example. Once code generation is going, the example should be replaced with a real generation.
2. The code generation should continue to function in an obvious manner as if it were handwritten
3. Lumi replaces `Iterator[yield_type]` with `Generator[yield_type, None, None]` when implementing generator functions. This produces better results for python's specified typesystem, but this is due to a few unfortunate issues in python's typeshed and how Iterator and Generator are specified.
4. One of the principles should have changed the late bind to list to just return there. While that's intended, I anticipate the
initial generation method to not be that advanced, this also allows the example to show how this feature would function.
5. lumi record type generation are still being worked on for what they will support and how. At a later date, they may end up implemented natively