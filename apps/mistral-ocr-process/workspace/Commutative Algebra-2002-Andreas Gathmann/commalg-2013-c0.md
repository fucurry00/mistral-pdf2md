## 0. Introduction

Commutative algebra is the study of commutative rings. In this class we will assume the basics of ring theory that you already know from earlier courses (e. g. ideals, quotient rings, the homomorphism theorem, and unique prime factorization in principal ideal domains such as the integers or polynomial rings in one variable over a field), and move on to more advanced topics, some of which will be sketched in Remark 0.14 below. For references to earlier results I will usually use my German notes for the “Algebraic Structures” and occasionally the “Foundations of Mathematics” and “Introduction to Algebra” classes *[x10, x11, x12]*, but if you prefer English references you will certainly have no problems to find them in almost any textbook on abstract algebra.

You will probably wonder why the single algebraic structure of commutative rings deserves a full one-semester course for its study. The main motivation for this is its many applications in both algebraic geometry and (algebraic) number theory. Especially the connection between commutative algebra and algebraic geometry is very deep — in fact, to a certain extent one can say that these two fields of mathematics are essentially the same thing, just expressed in different languages. Although some algebraic constructions and results in this class may seem a bit abstract, most of them have an easy (and sometimes surprising) translation in terms of geometry, and knowing about this often helps to understand and remember what is going on. For example, we will see that the Chinese Remainder Theorem that you already know *[x10, Proposition 11.22]* (and that we will extend to more general rings than the integers in Proposition 1.14) can be translated into the seemingly obvious geometric statement that “giving a function on a disconnected space is the same as giving a function on each of its connected components” (see Example 1.15 (b)).

However, as this is not a geometry class, we will often only sketch the correspondence between algebra and geometry, and we will never actually use algebraic geometry to prove anything. Although our “Commutative Algebra” and “Algebraic Geometry” classes are deeply linked, they are deliberately designed so that none of them needs the other as a prerequisite. But I will always try to give you enough examples and background to understand the geometric meaning of what we do, in case you have not attended the “Algebraic Geometry” class yet.

So let us explain in this introductory chapter how algebra enters the field of geometry. For this we have to introduce the main objects of study in algebraic geometry: solution sets of polynomial equations over some field, the so-called varieties.

###### Convention 0.1 (Rings and fields).

In our whole course, a ring $R$ is always meant to be a commutative ring with 1 *[x10, Definition 7.1]*. We do not require that this multiplicative unit 1 is distinct from the additive neutral element 0, but if $1=0$ then $R$ must be the zero ring *[x10, Lemma 7.5 (c)]*. Subrings must have the same unit as the ambient ring, and ring homomorphisms are always required to map 1 to 1. Of course, a ring $R\neq\{0\}$ is a field if and only if every non-zero element has a multiplicative inverse.

###### Definition 0.2 (Polynomial rings).

Let $R$ be a ring, and let $n\in\mathbb{N}_{>0}$. A polynomial over $R$ in $n$ variables is a formal expression of the form

$f=\sum_{i_{1},\ldots,i_{n}\in\mathbb{N}}a_{i_{1},\ldots,i_{n}}\,x_{1}^{i_{1}}\cdot\,\cdots\cdot x_{n}^{i_{n}},$

with coefficients $a_{i_{1},\ldots,i_{n}}\in R$ and formal variables $x=(x_{1},\ldots,x_{n})$, such that only finitely many of the coefficients are non-zero (see *[x10, Chapter 9]* how this concept of “formal variables” can be defined in a mathematically rigorous way).

Polynomials can be added and multiplied in the obvious way, and form a ring with these operations. We call it the polynomial ring over $R$ in $n$ variables and denote it by $R[x_{1},\ldots,x_{n}]$.

---

Andreas Gathmann

Definition 0.3 (Varieties). Let  $K$  be a field, and let  $n \in \mathbb{N}$ .

(a) We call

$$
\mathbb {A} _ {K} ^ {n} := \left\{\left(c _ {1}, \dots , c _ {n}\right): c _ {i} \in K \text {f o r} i = 1, \dots , n \right\}
$$

the affine  $n$ -space over  $K$ . If the field  $K$  is clear from the context, we will write  $\mathbb{A}_K^n$  also as  $\mathbb{A}^n$ .

Note that  $\mathbb{A}_K^n$  is just  $K^n$  as a set. It is customary to use two different notations here since  $K^n$  is also a  $K$ -vector space and a ring. We will usually use the notation  $\mathbb{A}_K^n$  if we want to ignore these additional structures: for example, addition and scalar multiplication are defined on  $K^n$ , but not on  $\mathbb{A}_K^n$ . The affine space  $\mathbb{A}_K^n$  will be the ambient space for our zero loci of polynomials below.

(b) For a polynomial  $f \in K[x_1, \ldots, x_n]$  as above and a point  $c = (c_1, \ldots, c_n) \in \mathbb{A}_K^n$  we define the value of  $f$  at  $c$  to be

$$
f (c) = \sum_ {i _ {1}, \dots , i _ {n} \in \mathbb {N}} a _ {i _ {1}, \dots , i _ {n}} c _ {1} ^ {i _ {1}} \cdot \dots \cdot c _ {n} ^ {i _ {n}} \quad \in K.
$$

If there is no risk of confusion we will sometimes denote a point in  $\mathbb{A}_K^n$  by the same letter  $x$  as we used for the formal variables, writing  $f\in K[x_1,\ldots ,x_n]$  for the polynomial and  $f(x)$  for its value at a point  $x\in \mathbb{A}_K^n$ .

(c) Let  $S \subset K[x_1, \ldots, x_n]$  be a set of polynomials. Then

$$
V (S) := \left\{x \in \mathbb {A} _ {K} ^ {n}: f (x) = 0 \text {f o r a l l} f \in S \right\} \subset \mathbb {A} _ {K} ^ {n}
$$

is called the zero locus of  $S$ . Subsets of  $\mathbb{A}_K^n$  of this form are called (affine) varieties. If  $S = (f_1, \ldots, f_k)$  is a finite set, we will write  $V(S) = V(\{f_1, \ldots, f_k\})$  also as  $V(f_1, \ldots, f_k)$ .

Example 0.4. Varieties, say over the field  $\mathbb{R}$  of real numbers, can have many different "shapes". The following picture shows a few examples in  $\mathbb{A}_{\mathbb{R}}^{2}$  and  $\mathbb{A}_{\mathbb{R}}^{3}$ .

![img-0.jpeg](images/img-0.jpeg)
(a)  $V(x_{1}^{2} + x_{2}^{2} - 1)\subset \mathbb{A}^{2}$

![img-1.jpeg](images/img-1.jpeg)
(b)  $V(x_{2}^{2} - x_{1}^{3})\subset \mathbb{A}^{2}$

![img-2.jpeg](images/img-2.jpeg)
(c)  $V(x_{1}^{3} - x_{1})\subset \mathbb{A}^{2}$

![img-3.jpeg](images/img-3.jpeg)
(d)  $V(x_{1}^{6} + x_{2}^{6} + x_{3}^{6} - 1)\subset \mathbb{A}^{3}$

![img-4.jpeg](images/img-4.jpeg)
(e)  $V(x_{1}x_{3},x_{2}x_{3})\subset \mathbb{A}^{3}$

![img-5.jpeg](images/img-5.jpeg)
(f)  $V(x_{2}^{2} + x_{3}^{3} - x_{3}^{4} - x_{1}^{2}x_{3}^{2})\subset \mathbb{A}^{3}$

Of course, the empty set  $\emptyset$  and all of  $\mathbb{A}^n$  are also varieties in  $\mathbb{A}^n$ , since  $\emptyset = V(1)$  and  $\mathbb{A}^n = V(0)$ .

It is the goal of algebraic geometry to find out the geometric properties of varieties by looking at the corresponding polynomials from an algebraic point of view (as opposed to an analytical or numerical approach). However, it turns out that it is not a very good idea to just look at the defining polynomials given initially — simply because they are not unique. For example, the variety (a) above was given as the zero locus of the polynomial  $x_1^2 + x_2^2 - 1$ , but it is equally well the zero locus of  $(x_1^2 + x_2^2 - 1)^2$ , or of the two polynomials  $(x_1 - 1)(x_1^2 + x_2^2 - 1)$  and  $x_2(x_1^2 + x_2^2 - 1)$ . In order to

---

remove this ambiguity, it is therefore useful to consider all polynomials vanishing on $X$ at once. Let us introduce this concept now.

###### Construction 0.5 (Rings and ideals associated to varieties).

For a variety $X\subset\mathbb{A}^{n}_{K}$ (and in fact also for any subset $X$ of $\mathbb{A}^{n}_{K}$) we consider the set

$I(X):=\{f\in K[x_{1},\ldots,x_{n}]:f(x)=0\text{ for all }x\in X\}$

of all polynomials vanishing on $X$. Note that this is an ideal of $K[x_{1},\ldots,x_{n}]$ (which we write as $I(X)\trianglelefteq K[x_{1},\ldots,x_{n}]$): it is clear that $0\in I(X)$, and if two polynomials $f$ and $g$ vanish on $X$, then so do $f+g$ and $f\cdot h$ for any polynomial $h$. We call $I(X)$ the ideal of $X$.

With this ideal we can construct the quotient ring

$A(X):=K[x_{1},\ldots,x_{n}]/I(X)$

in which we identify two polynomials $f,g\in K[x_{1},\ldots,x_{n}]$ if and only if $f-g$ is the zero function on $X$, i. e. if $f$ and $g$ have the same value at every point $x\in X$. So one may think of an element $\overline{f}\in A(X)$ as being the same as a function

$X\to K,\enspace x\mapsto f(x)$

that can be given by a polynomial. We therefore call $A(X)$ the ring of polynomial functions or coordinate ring of $X$. Often we will simply say that $A(X)$ is the ring of functions on $X$ since functions in algebra are always given by polynomials. Moreover, the class of a polynomial $f\in K[x_{1},\ldots,x_{n}]$ in such a ring will usually also be written as $f\in A(X)$, dropping the explicit notation for equivalence classes if it is clear from the context that we are talking about elements in the quotient ring.

###### Remark 0.6 (Polynomials and polynomial functions).

You probably know that over some fields there is a subtle difference between polynomials and polynomial functions: e. g. over the field $K=\mathbb{Z}_{2}$ the polynomial $f=x^{2}+x\in K[x]$ is certainly non-zero, but it defines the zero function on $\mathbb{A}^{1}_{K}$ *[x11, Remark 9.16 (b)]*. In our current notation this means that the ideal $I(\mathbb{A}^{1}_{K})$ of functions vanishing at every point of $\mathbb{A}^{1}_{K}$ is non-trivial, in fact that $I(\mathbb{A}^{1}_{K})=(x^{2}+x)$, and that consequently the ring $A(\mathbb{A}^{1}_{K})=K[x]/(x^{2}+x)$ of polynomial functions on $\mathbb{A}^{1}_{K}$ is not the same as the polynomial ring $K[x]$.

In this class we will skip over this problem entirely, since our main geometric intuition comes from the fields of real or complex numbers where there is no difference between polynomials and polynomial functions. We will therefore usually assume silently that there is no polynomial $f\in K[x_{1},\ldots,x_{n}]$ vanishing on all of $\mathbb{A}^{n}_{K}$, i. e. that $I(\mathbb{A}^{n}_{K})=(0)$ and thus $A(\mathbb{A}^{n}_{K})=K[x_{1},\ldots,x_{n}]$.

###### Example 0.7 (Ideal of a point).

Let $a=(a_{1},\ldots,a_{n})\in\mathbb{A}^{n}_{K}$ be a point. We claim that its ideal $I(a):=I(\{a\})\trianglelefteq K[x_{1},\ldots,x_{n}]$ is

$I(a)=(x_{1}-a_{1},\ldots,x_{n}-a_{n}).$

In fact, this is easy to see:

- If $f\in I(a)$ then $f(a)=0$. This means that replacing each $x_{i}$ by $a_{i}$ in $f$ gives zero, i. e. that $f$ is zero modulo $(x_{1}-a_{1},\ldots,x_{n}-a_{n})$. Hence $f\in(x_{1}-a_{1},\ldots,x_{n}-a_{n})$.
- If $f\in(x_{1}-a_{1},\ldots,x_{n}-a_{n})$ then $f=\sum_{i=1}^{n}(x_{i}-a_{i})\,f_{i}$ for some $f_{1},\ldots,f_{n}\in K[x_{1},\ldots,x_{n}]$, and so certainly $f(a)=0$, i. e. $f\in I(a)$.

###### Construction 0.8 (Subvarieties).

The ideals of varieties defined in Construction 0.5 all lie in the polynomial ring $K[x_{1},\ldots,x_{n}]$. In order to get a geometric interpretation of ideals in more general rings it is useful to consider a relative situation: let $X\subset\mathbb{A}^{n}_{K}$ be a fixed variety. Then for any subset $S\subset A(X)$ of polynomial functions on $X$ we can consider its zero locus

$V_{X}(S)=\{x\in X:f(x)=0\text{ for all }f\in S\}\quad\subset X$

just as in Definition 0.3 (c), and for any subset $Y\subset X$ as in Construction 0.5 the ideal

$I_{X}(Y)=\{f\in A(X):f(x)=0\text{ for all }x\in Y\}\quad\trianglelefteq A(X)$

of all functions on $X$ that vanish on $Y$. It is clear that the sets of the form $V_{X}(S)$ are exactly the varieties in $\mathbb{A}^{n}_{K}$ contained in $X$, the so-called subvarieties of $X$.

##

---

If there is no risk of confusion we will simply write $V(S)$ and $I(Y)$ again instead of $V_{X}(S)$ and $I_{X}(Y)$. So in this notation we have now assigned to every variety $X$ a ring $A(X)$ of polynomial functions on $X$, and to every subvariety $Y\subset X$ an ideal $I(Y)\unlhd A(X)$ of the functions that vanish on $Y$. This assignment of an ideal to a subvariety has some nice features:

###### Lemma 0.9.

Let $X$ be a variety with coordinate ring $A(X)$. Moreover, let $Y$ and $Y^{\prime}$ be subsets of $X$, and let $S$ and $S^{\prime}$ be subsets of $A(X)$.

1. If $Y\subset Y^{\prime}$ then $I(Y^{\prime})\subset I(Y)$ in $A(X)$; if $S\subset S^{\prime}$ then $V(S^{\prime})\subset V(S)$ in $X$.
2. $Y\subset V(I(Y))$ and $S\subset I(V(S))$.
3. If $Y$ is a subvariety of $X$ then $Y=V(I(Y))$.
4. If $Y$ is a subvariety of $X$ then $A(X)/I(Y)\cong A(Y)$.

###### Proof.

1. Assume that $Y\subset Y^{\prime}$. If $f\in I(Y^{\prime})$ then $f$ vanishes on $Y^{\prime}$, hence also on $Y$, which means that $f\in I(Y)$. The second statement follows in a similar way.
2. Let $x\in Y$. Then $f(x)=0$ for every $f\in I(Y)$ by definition of $I(Y)$. But this implies that $x\in V(I(Y))$. Again, the second statement follows analogously.
3. By (b) it suffices to prove “$\supset$”. As $Y$ is a subvariety of $X$ we can write $Y=V(S)$ for some $S\subset A(X)$. Then $S\subset I(V(S))$ by (b), and thus $V(S)\supset V(I(V(S)))$ by (a). Replacing $V(S)$ by $Y$ now gives the required inclusion.
4. The ring homomorphism $A(X)\to A(Y)$ that restricts a polynomial function on $X$ to a function $Y$ is surjective and has kernel $I(Y)$ by definition. So the result follows from the homomorphism theorem *[x11, Proposition 8.12]*. ∎

###### Remark 0.10 (Reconstruction of geometry from algebra).

Let $Y$ be a subvariety of $X$. Then Lemma 0.9 (c) says that $I(Y)$ determines $Y$ uniquely. Similarly, knowing the rings $A(X)$ and $A(Y)$, together with the ring homomorphism $A(X)\to A(Y)$ that describes the restriction of functions on $X$ to functions on $Y$, is enough to recover $I(Y)$ as the kernel of this map, and thus $Y$ as a subvariety of $X$ by the above. In other words, we do not lose any information if we pass from geometry to algebra and describe varieties and their subvarieties by their coordinate rings and ideals.

This map $A(X)\to A(Y)$ corresponding to the restriction of functions to a subvariety is already a first special case of a ring homomorphism associated to a “morphism of varieties”. Let us now introduce this notion.

###### Construction 0.11 (Morphisms of varieties).

Let $X\subset\mathbb{A}_{K}^{n}$ and $Y\subset\mathbb{A}_{K}^{m}$ be two varieties over the same ground field. Then a morphism from $X$ to $Y$ is just a set-theoretic map $f:X\to Y$ that can be given by polynomials, i. e. such that there are polynomials $f_{1},\ldots,f_{m}\in K[x_{1},\ldots,x_{n}]$ with $f(x)=(f_{1}(x),\ldots,f_{m}(x))\in Y$ for all $x\in X$. To such a morphism we can assign a ring homomorphism

$\varphi:A(Y)\to A(X),\;\;g\mapsto g\circ f=g(f_{1},\ldots,f_{m})$

given by composing a polynomial function on $Y$ with $f$ to obtain a polynomial function on $X$. Note that this ring homomorphism $\varphi$ …

1. reverses the roles of source and target compared to the original map $f:X\to Y$; and
2. is enough to recover $f$, since $f_{i}=\varphi(y_{i})\in A(X)$ if $y_{1},\ldots,y_{m}$ denote the coordinates of $\mathbb{A}_{K}^{m}$.

###### Example 0.12.

Let $X=\mathbb{A}_{\mathbb{R}}^{1}$ (with coordinate $x$) and $Y=\mathbb{A}_{\mathbb{R}}^{2}$ (with coordinates $y_{1}$ and $y_{2}$), so that $A(X)=\mathbb{R}[x]$ and $A(Y)=\mathbb{R}[y_{1},y_{2}]$ by Remark 0.6. Consider the morphism of varieties

$f:X\to Y,\;\;x\mapsto(y_{1},y_{2}):=(x,x^{2})$

---

0. Introduction

whose image is obviously the standard parabola  $Z = V(y_{2} - y_{1}^{2})$  shown in the picture on the right. Then the associated ring homomorphism  $A(Y) = \mathbb{R}[y_1,y_2]\to \mathbb{R}[x] = A(X)$  of Construction 0.11 is given by composing a polynomial function in  $y_{1}$  and  $y_{2}$  with  $f$ , i.e. by plugging in  $x$  and  $x^2$  for  $y_{1}$  and  $y_{2}$ , respectively:

![img-6.jpeg](images/img-6.jpeg)

$$
\mathbb {R} \left[ y _ {1}, y _ {2} \right] \rightarrow \mathbb {R} [ x ], g \mapsto g (x, x ^ {2}).
$$

Note that with the images of  $g = y_{1}$  and  $g = y_{2}$  under this homomorphism we just recover the polynomials  $x$  and  $x^{2}$  defining the map  $f$ .

If we had considered  $f$  as a morphism from  $X$  to  $Z$  (i.e. restricted the target space to the actual image of  $f$ ) we would have obtained  $A(Z) = K[y_1, y_2] / (y_2 - y_1^2)$  and thus the ring homomorphism

$$
\mathbb {R} \left[ y _ {1}, y _ {2} \right] / \left(y _ {2} - y _ {1} ^ {2}\right)\rightarrow \mathbb {R} [ x ], g \mapsto g (x, x ^ {2})
$$

instead (which is obviously well-defined).

Remark 0.13 (Correspondence between geometry and algebra). Summarizing what we have seen so far, we get the following first version of a dictionary between geometry and algebra:

|  GEOMETRY | → | ALGEBRA  |
| --- | --- | --- |
|  variety X |  | ring A(X) of (polynomial) functions on X  |
|  subvariety Y of X |  | ideal I(Y) ≤ A(X) of functions on X vanishing on Y  |
|  morphism f: X → Y of varieties |  | ring homomorphism A(Y) → A(X), g ↦ g○f  |

Moreover, passing from ideals to subvarieties reverses inclusions as in Lemma 0.9 (a), and we have  $A(X) / I(Y) \cong A(Y)$  for any subvariety  $Y$  of  $X$  by Lemma 0.9 (d) (with the isomorphism given by restricting functions from  $X$  to  $Y$ ).

We have also seen already that this assignment of algebraic to geometric objects is injective in the sense of Remark 0.10 and Construction 0.11 (b). However, not all rings, ideals, and ring homomorphisms arise from this correspondence with geometry, as we will see in Remark 1.10, Example 1.25 (b), and Remark 1.31. So although the geometric picture is very useful to visualize algebraic statements, it can usually not be used to actually prove them in the case of general rings.

Remark 0.14 (Outline of this class). In order to get an idea of the sort of problems considered in commutative algebra, let us quickly list some of the main topics that we will discuss in this class.

- Modules. From linear algebra you know that one of the most important structures related to a field  $K$  is that of a vector space over  $K$ . If we write down the same axioms as for a vector space but relax the condition on  $K$  to allow an arbitrary ring, we obtain the algebraic structure of a module, which is equally important in commutative algebra as that of a vector space in linear algebra. We will study this in Chapter 3.
- Localization. If we have a ring  $R$  that is not a field, an important construction discussed in Chapter 6 is to make more elements invertible by allowing "fractions" — in the same way as one can construct the rational numbers  $\mathbb{Q}$  from the integers  $\mathbb{Z}$ . Geometrically, we will see that this process corresponds to studying a variety locally around a point, which is why it is called "localization".
- Decomposition into primes. In a principal ideal domain  $R$  like the integers or a polynomial ring in one variable over a field, an important algebraic tool is the unique prime factorization of elements of  $R$  [G1, Proposition 11.9]. We will extend this concept in Chapter 8 to more general rings, and also to a "decomposition of ideals into primes". In terms of geometry, this corresponds to a decomposition of a variety into pieces that cannot be subdivided any further — e.g. writing the variety in Example 0.4 (e) as a union of a line and a plane.

---

- Dimension. Looking at Example 0.4 again it seems obvious that we should be able to assign a dimension to each variety $X$. We will do this by assigning a dimension to each commutative ring so that the dimension of the coordinate ring $A(X)$ can be interpreted as the geometric dimension of $X$ (see Chapter 11). With this definition of dimension we can then prove its expected properties, e. g. that cutting down a variety by $n$ more equations reduces its dimension by at most $n$ (Remark 11.18).
- Orders of vanishing. For a polynomial $f\in K[x]$ in one variable you all know what it means that it has a zero of a certain order at a point. If we now have a different variety, say still locally diffeomorphic to a line such as e. g. the circle $X=V(x_{1}^{2}+x_{2}^{2}-1)\subset\mathbb{A}^{2}_{\mathbb{R}}$ in Example 0.4 (a), it seems geometrically reasonable that we should still be able to define such vanishing orders of functions on $X$ at a given point. This is in fact possible, but algebraically more complicated — we will do this in Chapter 12 and study the consequences in Chapter 13.

But before we can discuss these main topics of the class we have to start now by developing more tools to work with ideals than what you know from earlier classes.

###### Exercise 0.15.

Show that the following subsets $X$ of $\mathbb{A}^{n}_{K}$ are not varieties over $K$:

1. $X=\mathbb{Z}\subset\mathbb{A}^{1}_{\mathbb{R}}$;
2. $X=\mathbb{A}^{1}_{\mathbb{R}}\backslash\{0\}\subset\mathbb{A}^{1}_{\mathbb{R}}$;
3. $X=\{(x_{1},x_{2})\in\mathbb{A}^{2}_{\mathbb{R}}:x_{2}=\sin(x_{1})\}\subset\mathbb{A}^{2}_{\mathbb{R}}$;
4. $X=\{x\in\mathbb{A}^{1}_{\mathbb{C}}:|x|=1\}\subset\mathbb{A}^{1}_{\mathbb{C}}$;
5. $X=f(Y)\subset\mathbb{A}^{n}_{\mathbb{R}}$ for an arbitrary variety $Y$ and a morphism of varieties $f:Y\to X$ over $\mathbb{R}$.

###### Exercise 0.16 (Degree of polynomials).

Let $R$ be a ring. Recall that an element $a\in R$ is called a zero-divisor if there exists an element $b\neq 0$ with $ab=0$ *[x10, Definition 7.6 (c)]*, and that $R$ is called an (integral) domain if no non-zero element is a zero-divisor, i. e. if $ab=0$ for $a,b\in R$ implies $a=0$ or $b=0$ *[x10, Definition 7.6 (d)]*.

We define the degree of a non-zero polynomial $f=\sum_{i_{1},\ldots,i_{n}}a_{i_{1},\ldots,i_{n}}x_{1}^{i_{1}}\cdot\cdots\cdot x_{n}^{i_{n}}\in R[x_{1},\ldots,x_{n}]$ to be

$\deg f:=\max\{i_{1}+\cdots+i_{n}:a_{i_{1},\ldots,i_{n}}\neq 0\}.$

Moreover, the degree of the zero polynomial is formally set to $-\infty$. Show that:

1. $\deg(f\cdot g)\leq\deg f+\deg g$ for all $f,g\in R[x_{1},\ldots,x_{n}]$.
2. Equality holds in (a) for all polynomials $f$ and $g$ if and only if $R$ is an integral domain.

##