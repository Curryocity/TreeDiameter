# How to find the diameter in a data-tree?

## $\emptyset .$ What is a diameter in data tree?

The longest distance possible in a data tree.
Or more precisely but less straight-foward: The longest distance of all the shortest path between two nodes in a data tree.
Just like the diameter in a circle, the shortest path(a.k.a straight line) between two oppsite side is the longest distance possible in a circle.

## $I.$ Antipodal Property

Let's denote $Y\in\lambda(X)$ as " $Y$ is one of the furthest node from $X$"

If node $A,B$ forms a diameter, then $B\in\lambda(A)$ and $A\in\lambda(B)$. If not both, they are not the longest distance in the tree.

We say that $A,B$ are antipodal if $B\in\lambda(A)$ and $A\in\lambda(B)$ are true.

Which means that $A,B$ forms a diameter implies they are antipodal pairs.

Well that is obious, but how about in reversed? Does $A,B$'s antipodal implies
$A,B$ forms a diameter? We are going to find out in the next chapter.

## $II.$ Reverse Property Proof

Let's denote some functions:

$Path(X,Y)$ as a function that output the shortest path(a set of nodes in the path)
 from node $X$ to node $Y$ (Single valued function, because tree)

$Distance(X,Y)$ as the shortest distance between node $X$ and node $Y$

### We will try to use proof by contradiction, given $A,B$ antipodal

 Assume that a pair $C,D$ ( $\{A,B\}\land\{C,D\}=\emptyset$ ) forms a diameter,
  which means the antipodal pair isn't unique in a tree(So is the diameter in a specific case, we'll came back to it).

Since $A,B,C,D$ were in a data tree. There must be at least a way to connect
 $Path(A,B$) and $Path(C,D)$. In those bridges that connects them.
There exist a path $Path(E_1,E_2)$(Why?), Where $E_1\in Path(A,B)$ and $E_2\in Path(C,D)$.
 Such that $Path(E_1,E_2)\subset Path(A,C)$.

 It gets interesting by the fact that $A,B$ and $C,D$ are antipodal pairs. Means that
  the crossing paths of them cannot be bigger than their antipodals. Start by:

![picture1](/CurryDoc/image/Antipodal%20node%20proof_resize.png)

 $Path(A,B)\ge Path(A,C)$

 $a+b\ge a+c+e$

 $b\ge c+e$

 Note that $Path(E_1,E_2)$ and $e$ is different in each node pairing. So we are going to use the weaker argument $b\ge c$ universally. Which the $e=0$ is neccesary for the equality to happen.

 $Path(A,B)$ is also larger or equal than $Path(B,D)$, lead to $a\ge d$
 with similiar arguments.

 We could also apply the same thing to $Path(C,D)$

which lead to $c\ge b$ and $d\ge a$

Notice that in order to satisfy all those inequalities, $e$ had to be $0$.
 And $a=d, b=c$. In fact, due to $a,b$ and $c,d$ were chosen without order.
 $a=c$ and $b=d$ would hold, too.
 That is $a=b=c=d$ and the bridge path is None(local $e==0$ for every bridges).

 And that actually mean $Path(A,B)$ and $Path(C,D)$ intersects($e=0$) with each other in the midpoint
 ($a=b, c=d$). Every combination of two element in $\{A,B,C,D\}$ forms a diameter, the intersection
 of those paths is shared, let's called it "center point".

 What's more, if there is another pair of antipodal $X,Y$ pair. They will share the center point with
 $A,B,C,D$, and every diameter is cut in half by the center point. Every end nodes are exactly
 the same distance as the center point. Just act like a radius. Isn't that amazing? A circle is
  essentially hidden in a tree structure.  

There is no contradiction in our proof, but a tight condition for everything to hold. That alone
yields the conclusion. $X,Y$ being antipodal does guarantee $X,Y$ forming a diameter.

$Q.E.D$

## $III.$ Attempt using $\lambda()$ to find the diameter

### from chapter $II$: "if $X,Y$ is antipodal, then $Path(X,Y)$ is a diameter"

if there is such $X$ that $X\in\lambda(Y)$ where $Y\in\lambda(X)$ , then $Path(X,Y)$ is the diameter.
what if we had a algorithm that starts with a abitrary node, and keep applying $\lambda()$.
 Until there is an X that doing lambda search twice returns X iself, then the diameter is found.
 But is that possible? Does it guarantee to find the "reflection node"(node that $\lambda()$ twice returns to itself)?

Let's find it out! Start with intial node $A$ and work our way to $B,C,D$, etc... .
From now on we will treat $\lambda()$ like a single value function just to keep everything simple. But we are actually just picking one of
it's element. In reality, we'll iterate through all the element in $\lambda()$'s output.

Firstly, $B=\lambda(A)$ . Then $C=\lambda(B)$ . We know that $C$ doesn't always equal to $A$. As $A$
 is arbitary chosen, $C$ always equal to $A$ means that every node is a endpoint of diameter. And we know
it is impossible. So let's consider the worst case $A \ne C$ and move on, we had $D=\lambda(C)$ , is $D$ a new point?

![picture2](/CurryDoc/image/λ%20iteration%201_resize.png)

$B$ is an endpoint, so the picture below would be more accurate for our use. $E$ is a fork on $A$ to $B,C$
where $Path(A,B)$ and $Path(B,C)$ both passes it. We define $a=Distance(A,E)$ , $b=Distance(B,E)$ , and so on...

Where should $D$ connect to the tree though? Let's called the connected part "$F$".
 There are 4 types of $F$(Pink points) here in the simpified tree.

![picture3](/CurryDoc/image/Possibility%20of%20F_resize.png)

Let's listed out all the possiblities for the case that $D$ is an unique node, as well as the statement derive from $\lambda$ relations:

(note: $f$ is not the same in each cases, $f$ below are local variables, $f=Distance(E,F)\ge 0$)

1. $F\in Path(A,E)$:

      $Path(C,D) > Path(C,B)$, implies $d > b+ f$.

      $Path(A,D) < Path(A,B)$, implies $d < b + f$.

      Contradiction!

2. $F\in Path(B,E)$:

      $Path(C,D) > Path(C,B)$, implies $d > b- f$.

      $Path(A,D) < Path(A,B)$, implies $d < b - f$.

      Contradiction!

3. $F\in Path(C,E)$:

      $Path(C,D) > Path(C,B)$, implies $d > b + f$.

      $Path(A,D) < Path(A,B)$, implies $d < b -f $.

      Contradiction!

4. $F=E$  (so $f=0$):

      This is an overlap of case 1,2,3.
       Would cause: Contradiction!

### Which meant the assumption of " $D$ is an unique node" is false. $D$ must be one of $A,B,C$. (Very good news for the time complexity of our algorithm!)

If $D=C$, which makes $\lambda(C)=D=C$. Then the tree is made out by single node. In that case, $A=B=C=D$, a trival case. We don't consider that
 becauase remember the reason that we move on to D is to consider the worst case where $B\ne C$ (scroll up if you don't know what i am saying).

If D=A, it also wouldn't be possible unless $B=C$, because:

$Path(A,B) > Path(B,C)$, implies $b>c$

$Path(B,C) > Path(B,A)$, implies $c>a$

The two lines above implies $b>a$

$Path(C,D) > Path(C,B)$, which is equivalent to $Path(C,A) > Path(C,B)$ , implies $a>b$

Contradiction!

### Thus, $D=B$

Checking logic consistency with above method:

$Path(C,D) > Path(C,A)$, which is equivalent to $Path(B,A) > Path(C,A)$ , implies $b>c$.

Logic stays consistent.

### An reflection node is guarantee to be found within 3 $\lambda$ iterations

## $IV.$ The Algorithm

1. Pick an Abitrary node $A$. ---- Time complexity: $O(1)$

2. find $B=\lambda(A)$. ---- Time complexity: $O(n)$

3. find $C=\lambda(B)$. ---- Time complexity: $O(n)$

4. return $Path(B,C)$ as diameter. ---- Time complexity: $O(1)$

Total time complexity: $O(n)$

This algorithm works for general web data struction (not only tree).

## $V.$ Outro

Algorithm from an answer of stack overflow without concrete proof(might not be the original source), all proofs are come up by me.

Some technical terms(hope it is not weird) are suggested by ChatGPT

Using local variables and single-valuing a multi-value funciton isn't that formal but easier to understand

### Author: Curryocity

### Thanks Anonnoob and HammSamichz for helping

### GG
