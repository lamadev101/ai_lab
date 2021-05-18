hcf(X,Y,H):- X=Y, H = X.
hcf(X,Y,H):- X<Y, Y1 is Y-X,
    hcf(X,Y1, H).
hcf(X,Y,H):-X>Y, hcf(Y,X,H).
