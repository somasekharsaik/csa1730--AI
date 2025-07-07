% Facts: which teacher teaches which subject
teaches(cg, math).
teaches(gabe, english).
teaches(bob, history).

% Facts: which student takes which subject
takes(alice, math).
takes(bobby, english).
takes(carol, history).

% Predicate to find the subjects taught by a teacher
teaching_subjects(Teacher, Subject) :-
    teaches(Teacher, Subject).

% Predicate to find the students taking a given subject
taking_students(Subject, Student) :-
    takes(Student, Subject).
