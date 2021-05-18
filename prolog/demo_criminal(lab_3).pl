criminal(X):-american(X), sells_missiles(X, Y), hostile(Y).
enemy_of_america(X) :-hostile(X).
enemy_of_america("Iraq").
hostile(X):-country(X). 
has_missile("Iraq").
sells_missiles("George", "Iraq"). 
american("George"). 
country("Iraq").