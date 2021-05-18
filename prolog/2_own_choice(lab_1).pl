eat(tiger, deer).
eat(deer, grass).
%eat(carnivores, herbivores).
herbivores(deer).

carnivores(X):- eat(X, Y), herbivores(Y).
