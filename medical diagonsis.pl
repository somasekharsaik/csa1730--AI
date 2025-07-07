% ---------- Disease rules based on symptoms ----------

diagnose(flu, Symptoms) :-
    member(fever, Symptoms),
    member(cough, Symptoms),
    member(body_pain, Symptoms).

diagnose(cold, Symptoms) :-
    member(sneezing, Symptoms),
    member(runny_nose, Symptoms),
    member(sore_throat, Symptoms).

diagnose(malaria, Symptoms) :-
    member(fever, Symptoms),
    member(chills, Symptoms),
    member(sweating, Symptoms).

% ---------- Start Diagnosis ----------

start :-
    write('Enter your symptoms as a list (e.g., [fever, cough, body_pain].): '),
    read(Symptoms),
    diagnose(Disease, Symptoms),
    format('You may have ~w.~n', [Disease]), !.

start :-
    write('No matching diagnosis found based on the given symptoms.'), nl.
