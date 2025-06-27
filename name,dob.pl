% Define some facts about people and their DOB
dob(john, date(1990, 5, 17)).
dob(rame, date(1985, 12, 10)).
dob(sure, date(1985, 8, 15)).

% Define predicate to lookup a person's DOB by name
lookup(Name, DOB) :-
    dob(Name, DOB).
