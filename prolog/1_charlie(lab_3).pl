parent("Bluebeard”, “Charlie").
horse("Bluebeard").

offspring(X, Y):- parent(Y, X).
mammals(X):- parent(Y, X), offspring(X, Y).
horse(X):- mammals(X), offspring(X, Y), horse(Y).
