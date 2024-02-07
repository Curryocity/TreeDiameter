# How to find the diameter in a data-tree?
## What is a diameter in data tree?
The longest distance possible in a data tree.
Or more precisely but less straight-foward: The longest of all the shortest path between two nodes in a data tree.
Just like the diameter in a circle, the shortest distance(straight line) between two oppsite side is the longest straight line possible in a circle.
## I. Antipodal Property
Let's denote $Y\in\lambda(X)$ as "$Y$ is one of the furthest node from $X$"

If node $A,B$ forms a diameter, then $B\in\lambda(A)$ and $A\in\lambda(B)$. If not, they are not the longest distance in the tree.

We say that $A,B$ are antipodal if $B\in\lambda(A)$ and $A\in\lambda(B)$ is true.

Which means $A,B$ forms a diameter implies that $A,B$ are antipodal? 

Well that is obious, but how about in reversed? Does $A,B$'s antipodal implies 
$A,B$ forms a diameter? We are going to find out.

## II. Reverse Property Proof
Let's denote some functions:

$Path(X,Y)$ as a function that output the shortest path(a set of nodes in the path)
 from node $X$ to node $Y$[^1]

$Distance(X,Y)$ as the shortest distance between node $X$ and node $Y$

#### We will try to use proof by contradiction, we had $A,B$ antipodal.
 Assume that a pair $C,D$ that isn't $A,B$ is the diameter, 
 which means the antipodal pair isn't unique in a tree(So is the diameter, I'll explain it later).

Since $A,B,C,D$ were in a data tree. There must be at least a way to connect 
$Path(A,B$) and $Path(C,D)$. In those bridges that connects them.
There exist a path $Path(E_1,E_2)$(Why?), Where $E_1$ is on $Path(A,B)$ and $E_2$ is on $Path(C,D)$.
 Such that $Path(E_1,E_2)$ is included in $Path(A,C)$.

 It gets interesting as the fact that A,B and C,D are antipodal pairs,
  the crossing paths of them cannot be bigger than their antipodals.

 [inserts a diagram here]

 $Path(A,B)\ge Path(A,C)$

 $a+b\ge a+c+e$

 $b\ge c+e$

 It is also larger or equal than Path(B,D), lead to $a\ge d+e$
 with similiar arguments.

 We could also apply the same thing to $Path(C,D)$

which lead to $d\ge a+e$ and $d\ge a+e$

Notice that in order to satisfy all those inequalities, $e$ had to be $0$.
 And $a=d, b=c$. In fact, due to $a,b$ and $c,d$ were chosen without order. 
 $a=c$ and $b=d$ would hold, too.
 That is $a=b=c=d$ and $e=0$.

 And that actually mean $Path(A,B)$ and $Path(C,D)$ intersect($e=0$) with each other in the midpoint
 ($a=b, c=d$). Every combination of two element in $\{A,B,C,D\}$ forms a diameter, the intersection
 of those paths is shared, let's called it "center point".

 What's more, if there is another pair of antipodal $X,Y$ pair, they will share the center point with
 $A,B,C,D$ and every diameter is cut in half by the center point. Every end nodes are exactly
 the same distance as the center point. Just act like a radius. Isn't that amazing? A circle is
  essentially hidden in a tree structure.  

There is no contradiction in our proof, but a tight condition for everything to hold. That alone
yields the conclusion. $X,Y$ being antipodal does garuntee $X,Y$ forming a diameter. 

$Q.E.D$

## III. 
