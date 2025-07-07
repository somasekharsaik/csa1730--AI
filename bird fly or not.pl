% Facts: bird(name). and cannot_fly(name).
bird(sparrow).
bird(penguin).
bird(ostrich).
bird(eagle).
bird(duck).

cannot_fly(penguin).
cannot_fly(ostrich).

% Rule: A bird can fly if it is a bird and it is not in the cannot_fly list.
can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).

% Rule: A bird cannot fly if it is in the cannot_fly list.
cannot_fly_bird(Bird) :-
    bird(Bird),
    cannot_fly(Bird).
