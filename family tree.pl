% Facts
male(john).
female(mary).
male(paul).

parent(john, paul).
parent(mary, paul).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
