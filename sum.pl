% Base case: sum from 1 to 0 is 0
sum_to_n(0, 0).

% Recursive case
sum_to_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_to_n(N1, Sum1),
    Sum is Sum1 + N.
