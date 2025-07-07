% ---------- Pattern matching for simple structures ----------

% Match identical atoms
match(X, X) :-
    format('Matched atom: ~w~n', [X]).

% Match lists: [Head|Tail] structure
match([H|T], Pattern) :-
    format('Checking list head: ~w~n', [H]),
    match(H, Pattern);
    match(T, Pattern).

% Match compound terms
match(Term, Pattern) :-
    compound(Term),
    compound(Pattern),
    Term =.. [F|Args1],
    Pattern =.. [F|Args2],
    match_args(Args1, Args2).

% Match list of arguments
match_args([], []).
match_args([H1|T1], [H2|T2]) :-
    match(H1, H2),
    match_args(T1, T2).
