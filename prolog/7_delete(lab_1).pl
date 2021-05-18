del(X,[X|Tail],Tail).
del(X,[Head|Tail], [Head|NewTail]):-del(X,Tail,NewTail).
