## Base definitions

TODO: figure out which definitions can be lifted directly from academic work,
and which ones require additional wording and reasoning for.

specific TODO after discussion with carljm:
concept of "suitable replacement" needs to be well defined,
otherwise differentiating `Never` and subtyping behavior of `Never` will
end up inconsistent. Also good for this to be well-defined in general.
See also, discussion with DiscordLiz re: Removal of `Never[InfiniteLoop]`
and keeping kinds of `Never` disjoint unless generalized algebraic effects.