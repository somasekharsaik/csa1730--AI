% Facts about teacher, teacher's subject, and student
teacher(bob, math).
teacher(raj, physics).
teacher(jane, english).

% Facts which student learns which subject
learns(alex, math).
learns(boby, english).
learns(cano, physics).

% Predicate to find the subjects taught by a teacher
teaches(Teacher, Subject) :-
    teacher(Teacher, Subject).

% Predicate to find the subjects being taken by a given student
taking(Student, Subject) :-
    learns(Student, Subject).
