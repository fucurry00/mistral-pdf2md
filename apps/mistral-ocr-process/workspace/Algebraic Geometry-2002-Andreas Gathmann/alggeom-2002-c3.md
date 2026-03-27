3. Projective varieties

> Similarly to the affine case, a subset of projective $n$-space $\mathbb{P}^{n}$ over $k$ is called a projective algebraic set if it can be written as the zero locus of a (finite) set of homogeneous polynomials. The Zariski topology on $\mathbb{P}^{n}$ is the topology whose closed sets are the projective algebraic sets. The concepts of irreducibility and dimension are purely topological and extend therefore immediately to subsets of projective space. We prove a projective version of the Nullstellensatz and make projective varieties into ringed spaces that are varieties.
>
> The main property of projective varieties distinguishing them from affine varieties is that (over $\mathbb{C}$ in the classical topology) they are compact. In terms of algebraic geometry this translates into the statement that if $f:X\to Y$ is a morphism between projective varieties then $f(X)$ is closed in $Y$.

### 3.1. Projective spaces and projective varieties

In the last section we have studied varieties, i. e. topological spaces that are locally isomorphic to affine varieties. In particular, the ability to glue affine varieties together allowed us to construct *compact* spaces (over the ground field $\mathbb{C}$) like e. g. $\mathbb{P}^{1}$, whereas affine varieties themselves are never compact unless they are a single point (see exercise 3.5.6). Unfortunately, the description of a variety in terms of its affine patches is often quite inconvenient in practice, as we have seen already in the calculations in the last section. It would be desirable to have a global description of the spaces that does not refer to glueing methods.

Projective varieties form a large class of “compact” varieties that do admit such a unified global description. In fact, the class of projective varieties is so large that it is not easy to construct a variety that is *not* (an open subset of) a projective variety.

To construct projective varieties, we need to define projective spaces first. Projective spaces are “compactifications” of affine spaces. We have seen $\mathbb{P}^{1}$ already as a compactification of $\mathbb{A}^{1}$; general projective spaces are an extension of this construction to higher dimensions.

###### Definition 3.1.1.

We define projective $n$-space over $k$, denoted $\mathbb{P}^{n}$, to be the set of all one-dimensional linear subspaces of the vector space $k^{n+1}$.

###### Remark 3.1.2.

Obviously, a one-dimensional linear subspace of $k^{n+1}$ is uniquely determined by a non-zero vector in $k^{n+1}$. Conversely, two such vectors $a=(a_{0},\ldots,a_{n})$ and $b=(b_{0},\ldots,b_{n})$ in $k^{n+1}$ span the same linear subspace if and only if they differ only by a common scalar, i. e. if $b=\lambda a$ for some non-zero $\lambda\in k$. In other words,

$\mathbb{P}^{n}=\{(a_{0},\ldots,a_{n})\;;\;a_{i}\in k,\;\text{not all}\;a_{i}=0\}/\sim$

with the equivalence relation

$(a_{0},\ldots,a_{n})\sim(b_{0},\ldots,b_{n})\quad\text{if}\quad a_{i}=\lambda b_{i}\text{ for some }\lambda\in k\backslash\{0\}\text{ and all }i.$

This is often written as

$\mathbb{P}^{n}=(k^{n+1}\backslash\{0\})/(k\backslash\{0\}),$

and the point $P$ in $\mathbb{P}^{n}$ determined by $(a_{0},\ldots,a_{n})$ is written as $P=(a_{0}:\cdots:a_{n})$ (the notation $[a_{0},\ldots,a_{n}]$ is also common in the literature). So the notation $(a_{0}:\cdots:a_{n})$ means that the $a_{i}$ are not all zero, and that they are defined only up to a common scalar multiple. The $a_{i}$ are called the homogeneous coordinates of the point $P$ (the motivation for this name will become obvious in the course of this section).

###### Example 3.1.3.

Consider the one-dimensional projective space $\mathbb{P}^{1}$. Let $(a_{0}:a_{1})\in\mathbb{P}^{1}$ be a point. Then we have one of the following cases:

---

1. $a_{0}\neq 0$. Then $P$ can be written as $P=(1:a)$ with $a=\frac{a_{1}}{a_{0}}\in k$. Obviously $(1:a)=(1:b)$ if and only if $a=b$, i. e. the ambiguity in the homogeneous coordinates is gone if we fix one of them to be 1. So the set of these points is just $\mathbb{A}^{1}$. We call $a=\frac{a_{1}}{a_{0}}$ the affine coordinate of the point $P$; it is uniquely determined by $P$ (and not just up to a multiple as for the homogeneous coordinates).
2. $a_{0}=0$, and therefore $a_{1}\neq 0$. There is just one such point that we can write as $(0:1)$.

So $\mathbb{P}^{1}$ is just $\mathbb{A}^{1}$ with one point added. This additional point $(0:1)$ can be thought of as a “point at infinity”, as you can see from the fact that its affine coordinate is formally $\frac{1}{0}$. So we arrive at the same description of $\mathbb{P}^{1}$ as in example 2.4.5 (i).

###### Remark 3.1.4.

There is a completely analogous description of $\mathbb{P}^{n}$ as $\mathbb{A}^{n}$ with some points added “at infinity”: let $P=(a_{0}:\cdots:a_{n})\in\mathbb{P}^{n}$ be a point. Then we have one of the following cases:

1. $a_{0}\neq 0$. Then $P=(1:\alpha_{1}:\cdots:\alpha_{n})$ with $\alpha_{i}=\frac{a_{i}}{a_{0}}$ for all $i$. The $\alpha_{i}$ are the affine coordinates of $P$; they are uniquely determined by $P$ and are obtained by setting $a_{0}=1$. So the set of all $P$ with $a_{0}\neq 0$ is just $\mathbb{A}^{n}$.
2. $a_{0}=0$, i. e. $P=(0:a_{1}:\cdots:a_{n})$, with the $a_{i}$ still defined only up to a common scalar. Obviously, the set of such points is $\mathbb{P}^{n-1}$; the set of all one-dimensional linear subspaces of $\mathbb{A}^{n}$. We think of these points as points at infinity; the new twist compared to $\mathbb{P}^{1}$ is just that we have a point at infinity for every one-dimensional linear subspace of $\mathbb{A}^{n}$, i. e. for every “direction” in $\mathbb{A}^{n}$. So, for example, two lines in $\mathbb{A}^{n}$ will meet at infinity (when compactified in $\mathbb{P}^{n}$) if and only if they are parallel, i. e. point in the same direction. (This is good as it implies that two distinct lines always intersect in exactly one point.)

Usually, it is more helpful to think of the projective space $\mathbb{P}^{n}$ as the affine space $\mathbb{A}^{n}$ compactified by adding some points (parametrized by $\mathbb{P}^{n-1}$) at infinity, rather than as the set of lines in $\mathbb{A}^{n+1}$.

###### Remark 3.1.5.

In the case $k=\mathbb{C}$, we claim that $\mathbb{P}^{n}$ is a compact space (in the classical topology). In fact, let

$S^{2n+1}=\{(a_{0},\ldots,a_{n})\in\mathbb{C}^{n+1}\ ;\ |a_{0}|^{2}+\cdots+|a_{n}|^{2}=1\}$

be the unit sphere in $\mathbb{C}^{n+1}=\mathbb{R}^{2n+2}$. This is a compact space as it is closed and bounded, and there is an obvious surjective map

$S^{2n+1}\to\mathbb{P}^{n},\ (a_{0},\cdots,a_{n})\mapsto(a_{0}:\cdots:a_{n}).$

As images of compact sets under continuous maps are compact, it follows that $\mathbb{P}^{n}$ is also compact.

###### Remark 3.1.6.

In complete analogy to affine algebraic sets, we now want to define projective algebraic sets to be subsets of $\mathbb{P}^{n}$ that can be described as the zero locus of some polynomials in the homogeneous coordinates. Note however that if $f\in k[x_{0},\ldots,x_{n}]$ is an arbitrary polynomial, it does not make sense to write down a definition like

$Z(f)=\{(a_{0}:\cdots:a_{n})\ ;\ f(a_{0},\ldots,a_{n})=0\},$

because the $a_{i}$ are only defined up to a common scalar. For example, if $f(x_{0},x_{1})=x_{1}^{2}-x_{0}$ then $f(1,1)=0$ but $f(-1,-1)\neq 0$, although $(1:1)$ and $(-1:-1)$ are the same point in $\mathbb{P}^{1}$. To get rid of this problem we have to require that $f$ be homogeneous, i. e. that all of its monomials have the same (total) degree $d$. This is equivalent to the requirement

$f(\lambda x_{0},\ldots,\lambda x_{n})=\lambda^{d}f(x_{0},\ldots,x_{n})\ \text{for all}\ \lambda,$

---

so in particular we see that

$f(\lambda x_{0},\ldots,\lambda x_{n})=0\iff f(x_{0},\ldots,x_{n})=0,$

i. e. the condition that a *homogeneous* polynomial in the homogeneous coordinates vanishes is indeed well-defined.

###### Definition 3.1.7.

For every $f\in k[x_{0},\ldots,x_{n}]$ let $f^{(d)}$ denote the degree-$d$ part of $f$, i. e. $f=\sum f^{(d)}$ with $f^{(d)}$ homogeneous of degree $d$ for all $d$.

###### Lemma 3.1.8.

Let $I\subset k[x_{0},\ldots,x_{n}]$ be an ideal. The following are equivalent:

1. I can be generated by homogeneous polynomials.
2. For every $f\in I$ we have $f^{(d)}\in I$ for all $d$.

An ideal that satisfies these conditions is called homogeneous.

###### Proof.

(i) $\Rightarrow$ (ii): Let $I=(f_{1},\ldots,f_{m})$ with all $f_{i}$ homogeneous. Then every $f\in I$ can be written as $f=\sum_{i}a_{i}f_{i}$ for some $a_{i}\in k[x_{0},\ldots,x_{n}]$ (which need not be homogeneous). Restricting this equation to the degree-$d$ part, we get $f^{(d)}=\sum_{i}(a_{i})^{(d-\deg f_{i})}f_{i}\in I$.

(ii) $\Rightarrow$ (i): Any ideal can be written as $I=(f_{1},\ldots,f_{m})$ with the $f_{i}$ possibly not being homogeneous. But by (ii) we know that all $f_{i}^{(d)}$ are in $I$ too, so it follows that $I$ is generated by the homogeneous polynomials $f_{i}^{(d)}$. ∎

###### Remark 3.1.9.

Note that it is *not* true that every element of a homogeneous ideal $I$ is a homogeneous polynomial: we can always add two polynomials of $I$ to get another element of $I$, even if they do not have the same degree.

With the exception of the homogeneity requirement, the following constructions are now completely analogous to the affine case:

###### Definition 3.1.10.

Let $I\subset k[x_{0},\ldots,x_{n}]$ be a homogeneous ideal (or a set of homogeneous polynomials). The set

$\mathbf{Z(I)}:=\{(a_{0}:\cdots:a_{n})\in\mathbb{P}^{n}\ ;\ f(a_{0},\ldots,a_{n})=0\ \text{for all}\ f\in I\}$

is called the zero locus of $I$; this is well-defined by remark 3.1.6. Subsets of $\mathbb{P}^{n}$ that are of the form $Z(I)$ are called algebraic sets. If $X\subset\mathbb{P}^{n}$ is any subset, we call

$I(X)$ $:=$the ideal generated by

$\{f\in k[x_{0},\ldots,x_{n}]\ \text{homogeneous}\ ;\ f(a_{0},\ldots,a_{n})=0\ \text{for all}\ (a_{0}:\cdots:a_{n})\in X\}$
$\subset k[x_{0},\ldots,x_{n}]$

the ideal of $X$; by definition this is a homogeneous ideal.

If we want to distinguish between the affine zero locus $Z(I)\subset\mathbb{A}^{n+1}$ and the projective zero locus $Z(I)\subset\mathbb{P}^{n}$ of the same (homogeneous) ideal, we denote the former by $Z_{a}(I)$ and the latter by $Z_{p}(I)$.

###### Remark 3.1.11.

A remark that is sometimes useful is that every projective algebraic set can be written as the zero locus of finitely many homogeneous polynomials *of the same degree*. This follows easily from the fact that $Z(f)=Z(x_{0}^{d}f,\ldots,x_{n}^{d}f)$ for all homogeneous polynomials $f$ and every $d\geq 0$.

###### Example 3.1.12.

Let $L\subset\mathbb{A}^{n+1}$ be a linear subspace of dimension $k+1$; it can be given by $n-k$ linear equations in the coordinates of $\mathbb{A}^{n+1}$. The image of $L$ under the quotient map $(\mathbb{A}^{n+1}\backslash\{0\})/(k\backslash\{0\})=\mathbb{P}^{n}$, i. e. the subspace of $\mathbb{P}^{n}$ given by the same $n-k$ equations (now considered as equations in the homogeneous coordinates on $\mathbb{P}^{n}$) is called a linear subspace of $\mathbb{P}^{n}$ of dimension $k$. Once we have given projective varieties the structure of varieties, we will see that a linear subspace of $\mathbb{P}^{n}$ of dimension $k$ is isomorphic to $\mathbb{P}^{k}$. For

---

Andreas Gathmann

example, a line in  $\mathbb{P}^3$  (with homogeneous coordinates  $x_0, x_1, x_2, x_3$ ) is given by two linearly independent equations in the  $x_i$ . One example is the line

$$
\left\{x _ {2} = x _ {3} = 0 \right\} = \left\{\left(a _ {0}: a _ {1}: 0: 0\right); a _ {0}, a _ {1} \in k \right\} \subset \mathbb {P} ^ {3},
$$

which is "obviously isomorphic" to  $\mathbb{P}^1$ .

Example 3.1.13. Consider the conics in  $\mathbb{A}^2$

$$
X _ {1} = \left\{x _ {2} = x _ {1} ^ {2} \right\} \quad \text {and} \quad X _ {2} = \left\{x _ {1} x _ {2} = 1 \right\}
$$

of exercise 2.6.1. We want to "compactify" these conics to projective algebraic sets  $\tilde{X}_1$ ,  $\tilde{X}_2$  in  $\mathbb{P}^2$ . Note that for a projective algebraic set we need the defining polynomials to be homogeneous, which is not yet the case here. On the other hand, we have an additional coordinate  $x_0$  that you can think of as being 1 on the affine space  $\mathbb{A}^2 \subset \mathbb{P}^2$ . So it is obvious that we should make the defining equations homogeneous by adding suitable powers of  $x_0$ : consider

$$
\tilde {X} _ {1} = \left\{x _ {0} x _ {2} = x _ {1} ^ {2} \right\} \quad \text {and} \quad \tilde {X} _ {2} = \left\{x _ {1} x _ {2} = x _ {0} ^ {2} \right\}
$$

in  $\mathbb{P}^2$ . Then the restriction of  $\tilde{X}_i$  to the affine space  $\mathbb{A}^2 \subset \mathbb{P}^2$  is just given by  $X_i$  for  $i = 1, 2$ . We call  $\tilde{X}_i$  the projective completion of  $X_i$ ; it can be done in the same way for all affine varieties (see exercise 3.5.3).

Let us consider  $\tilde{X}_1$  first. The points that we add at infinity correspond to those where  $x_0 = 0$ . It follows from the defining equation that  $x_1 = 0$  as well; and then we must necessarily have  $x_2 \neq 0$  as the coordinates cannot be simultaneously zero. So there is only one point added at infinity, namely  $(0:0:1)$ . It corresponds to the "vertical direction" in  $\mathbb{A}^2$ , which is the direction in which the parabola  $x_2 = x_1^2$  goes off to infinity (at both ends actually).

For  $\tilde{X}_2$ , the added points have again  $x_0 = 0$ . This means that  $x_{1}x_{2} = 0$ , which yields the two points  $(0:1:0)$  and  $(0:0:1)$  in  $\mathbb{P}^2$ : we added two points at infinity, one corresponding to the "horizontal" and one to the "vertical" direction in  $\mathbb{A}^2$ . This is clear from the picture below as the hyperbola  $x_{1}x_{2} = 1$  extends to infinity both along the  $x_{1}$  and the  $x_{2}$  axis.

![img-0.jpeg](images/img-0.jpeg)

![img-1.jpeg](images/img-1.jpeg)

Note that the equations of  $\tilde{X}_1$  and  $\tilde{X}_2$  are exactly the same, up to a permutation of the coordinates. Even if we have not given projective varieties the structure of varieties yet, it should be obvious that  $\tilde{X}_1$  and  $\tilde{X}_2$  will be isomorphic varieties, with the isomorphism being given by exchanging  $x_0$  and  $x_1$ . Hence we see that the two distinct types of conics in  $\mathbb{A}^2$  become the same in projective space: there is only one projective conic in  $\mathbb{P}^2$  up to isomorphism. The difference in the affine case comes from the fact that some conics "meet infinity" in one point (like  $X_1$ ), and some in two (like  $X_2$ ).

# Proposition 3.1.14.

(i) If  $I_1 \subset I_2$  are homogeneous ideals in  $k[x_0, \ldots, x_n]$  then  $Z(I_2) \subset Z(I_1)$ .
(ii) If  $\{I_i\}$  is a family of homogeneous ideals in  $k[x_0, \ldots, x_n]$  then  $\bigcap_{i} Z(I_i) = Z(\bigcup_{i} I_i) \subset \mathbb{P}^n$ .
(iii) If  $I_1, I_2 \subset k[x_0, \ldots, x_n]$  are homogeneous ideals then  $Z(I_1) \cup Z(I_2) = Z(I_1I_2) \subset \mathbb{P}^n$ .

---

3. Projective varieties

In particular, arbitrary intersections and finite unions of algebraic sets are again algebraic sets.

Proof. The proof is the same as in the affine case (proposition 1.1.6).

Definition 3.1.15. We define the Zariski topology on  $\mathbb{P}^n$  to be the topology whose closed sets are the algebraic sets (proposition 3.1.14 tells us that this gives in fact a topology). Moreover, any subset  $X$  of  $\mathbb{P}^n$  (in particular any algebraic set) will be equipped with the topology induced by the Zariski topology on  $\mathbb{P}^n$ . This will be called the Zariski topology on  $X$ .

Remark 3.1.16. The concepts of irreducibility and dimension introduced in section 1.3 are purely topological ones, so they apply to projective algebraic sets (or more generally to any subset of  $\mathbb{P}^n$ ) as well. They have the same geometric interpretation as in the affine case. Irreducible algebraic sets in  $\mathbb{P}^n$  are called projective varieties. As in the affine case (see lemma 1.3.4) a projective algebraic set  $X$  is irreducible if and only if its ideal  $I(X)$  is a prime ideal. In particular,  $\mathbb{P}^n$  itself is irreducible.

3.2. Cones and the projective Nullstellensatz. We will now establish a correspondence between algebraic sets in  $\mathbb{P}^n$  and homogeneous radical ideals in  $k[x_0, \ldots, x_n]$ , similar to the affine case. This is quite straightforward; the only twist is that there is no zero point  $(0: \dots: 0)$  in  $\mathbb{P}^n$ , and so the zero locus of the radical homogeneous ideal  $(x_0, \ldots, x_n)$  is empty although the ideal is not equal to (1). So we will have to exclude this ideal from our correspondence, which is why it is sometimes called the irrelevant ideal.

As we want to use the results of the affine case for the proof of this statement, let us first establish a connection between projective algebraic sets in  $\mathbb{P}^n$  and certain affine algebraic sets in  $\mathbb{A}^{n + 1}$ .

Definition 3.2.1. An affine algebraic set  $X \subset \mathbb{A}^{n+1}$  is called a cone if it is not empty, and if we have for all  $\lambda \in k$

$$
\left(x _ {0}, \dots , x _ {n}\right) \in X \quad \Rightarrow \quad \left(\lambda x _ {0}, \dots , \lambda x _ {n}\right) \in X.
$$

If  $X\subset \mathbb{P}^n$  is a projective algebraic set, then

$$
\boldsymbol {C} (\boldsymbol {X}) := \left\{\left(x _ {0}, \dots , x _ {n}\right) \mid \left(x _ {0}: \dots : x _ {n}\right) \in X \right\} \cup \{0 \}
$$

is called the cone over  $X$  (obviously this is a cone).

Remark 3.2.2. In other words, a cone is an algebraic set in  $\mathbb{A}^{n + 1}$  that can be written as a (usually infinite) union of lines through the origin. The cone over a projective algebraic set  $X\subset \mathbb{P}^n$  is the inverse image of  $X$  under the projection map  $\mathbb{A}^{n + 1}\backslash \{0\} \to (\mathbb{A}^{n + 1}\backslash \{0\}) / (k\backslash \{0\}) = \mathbb{P}^n$ , together with the origin.

Example 3.2.3. The following picture shows an example of a (two-dimensional) cone  $C(X)$  in  $\mathbb{A}^3$  over the (one-dimensional) projective variety  $X$  in  $H = \mathbb{P}^2$ :

![img-2.jpeg](images/img-2.jpeg)

---

$(C(X)$ consists only of the “boundary” of the cone, not of the “interior”.) Note that $C(X)$ contains the two lines $L_{1}$ and $L_{2}$, which correspond to “points at infinity” of the projective space $\mathbb{P}^{2}$.

###### Lemma 3.2.4.

1. Let $I\subsetneq k[x_{0},\ldots,x_{n}]$ be a homogeneous ideal. If $X=Z_{p}(I)\subset\mathbb{P}^{n}$, then $C(X)=Z_{a}(I)\subset\mathbb{A}^{n+1}$.
2. Conversely, if $X\subset\mathbb{P}^{n}$ is a projective algebraic set and $I(X)\subset k[x_{0},\ldots,x_{n}]$ is its homogeneous ideal, then $I(C(X))=I(X)$.

In other words, there is a one-to-one correspondence between projective algebraic sets in $\mathbb{P}^{n}$ and affine cones in $\mathbb{A}^{n+1}$, given by taking the zero locus of the same homogeneous ideal (not equal to $(1)$) either in $\mathbb{P}^{n}$ or in $\mathbb{A}^{n+1}$.

###### Proof.

This is obvious from the definitions. ∎

Using this lemma, it is now very simple to derive a projective version of the Nullstellensatz:

###### Proposition 3.2.5.

(“The projective Nullstellensatz”)

1. If $X_{1}\subset X_{2}$ are algebraic sets in $\mathbb{P}^{n}$ then $I(X_{2})\subset I(X_{1})$.
2. For any algebraic set $X\subset\mathbb{P}^{n}$ we have $Z_{p}(I(X))=X$.
3. For any homogeneous ideal $I\subset k[x_{0},\ldots,x_{n}]$ such that $Z_{p}(I)$ is not empty we have $I(Z_{p}(I))=\sqrt{I}$.
4. For any homogeneous ideal $I\subset k[x_{0},\ldots,x_{n}]$ such that $Z_{p}(I)$ is empty we have either $I=(1)$ or $\sqrt{I}=(x_{0},\ldots,x_{n})$. In other words, $Z_{p}(I)$ is empty if and only if $(x_{0},\ldots,x_{n})^{r}\subset I$ for some $r$.

###### Proof.

The proofs of (i) and (ii) are literally the same as in the affine case, see proposition 1.2.9.

1. Let $X=Z_{p}(I)$. Then

$I(Z_{p}(I))=I(X)=I(C(X))=I(Z_{a}(I))=\sqrt{I}$

by lemma 3.2.4 and the affine Nullstellensatz of proposition 1.2.9 (iii).

1. If $Z_{p}(I)$ is empty, then $Z_{a}(I)$ is either empty or just the origin. So corollary 1.2.10 tells us that $I=(1)$ or $\sqrt{I}=(x_{0},\ldots,x_{n})$. In any case, this means that $x_{i}^{k_{i}}\in I$ for some $k_{i}$, so $(x_{0},\ldots,x_{n})^{k_{0}+\cdots+k_{n}}\subset I$. ∎

###### Theorem 3.2.6.

There is a one-to-one inclusion-reversing correspondence between algebraic sets in $\mathbb{P}^{n}$ and homogeneous radical ideals in $k[x_{0},\ldots,x_{n}]$ not equal to $(x_{0},\ldots,x_{n})$, given by the operations $Z(\cdot)$ and $I(\cdot)$.

###### Proof.

Immediately from proposition 3.2.5. ∎

### 3.3. Projective varieties as ringed spaces

So far we have defined projective varieties as topological spaces. Of course we want to make them into ringed spaces and finally show that they are varieties in the sense of definitions 2.4.1 and 2.5.1. So let $X\subset\mathbb{P}^{n}$ be a projective variety. First of all we have to make $X$ into a ringed space whose structure sheaf is a sheaf of $k$-valued functions. The construction is completely analogous to the affine case discussed in section 2.1.

###### Definition 3.3.1.

The ring

$\boldsymbol{S(X)}:=k[x_{0},\ldots,x_{n}]/I(X)$

is called the homogeneous coordinate ring of $X$

---

###### Remark 3.3.2.

In contrast to the affine case, the elements of $S(X)$ do *not* define functions on $X$, because the homogeneous coordinates are only determined up to a common scalar. Rather, to get well-defined functions, we have to take quotients of two homogeneous polynomials *of the same degree* $d$, because then a rescaling of the homogeneous coordinates by a factor $\lambda\in k\backslash\{0\}$ gives a factor of $\lambda^{d}$ in both the numerator and denominator, so that it cancels out:

###### Definition 3.3.3.

Let

$S(X)^{(d)}:=\left\{f^{(d)}\ ;\ f\in S(X)\right\}$

be the degree-$d$ part of $S(X)$. Note that this is well-defined: if $f\in I(X)$ then $f^{(d)}=0$ by lemma 3.1.8. We define the field of rational functions to be

$\bm{K(X)}:=\left\{\frac{f}{g}\ ;\ f,g\in S(X)^{(d)}\ \text{and}\ g\neq 0\right\}.$

By remark 3.3.2, the elements of $K(X)$ give set-theoretic functions to the ground field $k$ wherever the denominator is non-zero. Now as in the affine case set

$\mathcal{O}_{X,P}:=\left\{\frac{f}{g}\in K(X)\ ;\ g(P)\neq 0\right\}\quad\text{and}\quad\mathcal{O}_{X}(U):=\bigcap_{P\in U}\mathcal{O}_{X,P}$

for $P\in X$ and $U\subset X$ open. It is easily seen that this is a sheaf of $k$-valued functions.

###### Remark 3.3.4.

In the same way as for affine varieties (see exercise 2.6.9) one can show that the function field $K(X)$ defined above agrees with the definition for general varieties.

###### Remark 3.3.5.

Note that $\mathcal{O}_{X}(X)=k$, i. e. *every regular function on all of $X$ is constant*. This follows trivially from the description of $K(X)$: if the function is to be defined everywhere $g$ must be a constant. But then $f$ has to be a constant too as it must have the same degree as $g$. A (slight) generalization of this will be proved in corollary 3.4.10.

###### Proposition 3.3.6.

Let $X$ be a projective variety. Then $(X,\mathcal{O}_{X})$ is a prevariety.

###### Proof.

We need to find an open affine cover of $X$. Consider the open subset

$X_{0}=\{(a_{0}:\cdots:a_{n})\in X\ ;\ a_{0}\neq 0\}=X\cap\mathbb{A}^{n}$

(where $\mathbb{A}^{n}\subset\mathbb{P}^{n}$ as in remark 3.1.4). If $X=Z(f_{1},\ldots,f_{r})$ with $f_{i}\in k[x_{0},\ldots,x_{n}]$ homogeneous, set $g_{i}(x_{1},\ldots,x_{n})=f_{i}(1,x_{1},\ldots,x_{n})\in k[x_{1},\ldots,x_{n}]$ and define $Y=Z(g_{1},\ldots,g_{r})\subset\mathbb{A}^{n}$. We claim that there is an isomorphism

$F:X\cap\mathbb{A}^{n}\to Y,\ (a_{0}:\cdots:a_{n})\mapsto\left(\frac{a_{1}}{a_{0}},\ldots,\frac{a_{n}}{a_{0}}\right).$

In fact, it is obvious that a set-theoretic inverse is given by

$F^{-1}:Y\to X\cap\mathbb{A}^{n},\ (a_{1},\ldots,a_{n})\mapsto(1:a_{1}:\cdots:a_{n}).$

Moreover, $F$ is a morphism because it pulls back a regular function on (an open subset of) $Y$ of the form

$\frac{p(a_{1},\ldots,a_{n})}{q(a_{1},\ldots,a_{n})}\quad\text{to}\quad\frac{p(\frac{a_{1}}{a_{0}},\ldots,\frac{a_{n}}{a_{0}})}{q(\frac{a_{1}}{a_{0}},\ldots,\frac{a_{n}}{a_{0}})},$

which is a regular function on $X\cap\mathbb{A}^{n}$ as it can be rewritten as a quotient of two homogeneous polynomials of the same degree (by canceling the fractions in the numerator and denominator). In the same way, $F^{-1}$ pulls back a regular function on (an open subset of) $X\cap\mathbb{A}^{n}$

$\frac{p(a_{0},\ldots,a_{n})}{q(a_{0},\ldots,a_{n})}\quad\text{to}\quad\frac{p(1,a_{1},\ldots,a_{n})}{q(1,a_{1},\ldots,a_{n})},$

which is a regular function on $Y$. So $F$ is an isomorphism.

######

---

In the same way we can do this for the open sets $X_{i}=\{(x_{0}:\cdots:x_{n})\in X~{};~{}x_{i}\neq 0\}$ for $i=0,\ldots,n$. As the $x_{i}$ cannot be simultaneously zero, it follows that the $X_{i}$ form an affine cover of $X$. So $X$ is a prevariety. ∎

###### Remark 3.3.7.

Following the proof of proposition 3.3.6, it is easy to see that our “new” definition of $\mathbb{P}^{1}$ agrees with the “old” definition of example 2.4.5 (i) by glueing two affine lines $\mathbb{A}^{1}$.

###### Remark 3.3.8.

Proposition 3.3.6 implies that all our constructions and results for prevarieties apply to projective varieties as well. For example, we know what morphisms are, and have defined products of projective varieties. We have also defined the field of rational functions for prevarieties in exercise 2.6.9; it is easy to check that this definition agrees with the one in definition 3.3.3.

Although this gives us the definition of morphisms and products, we would still have to apply our glueing techniques to write down a morphism or a product. So we should find a better description for morphisms and products involving projective varieties:

###### Lemma 3.3.9.

Let $X\subset\mathbb{P}^{n}$ be a projective variety (or an open subset of a projective variety). Let $f_{1},\ldots,f_{m}\in k[x_{0},\ldots,x_{n}]$ be homogeneous polynomials of the same degree in the homogeneous coordinates of $\mathbb{P}^{n}$, and assume that for every $P\in X$ at least one of the $f_{i}$ does not vanish at $P$. Then the $f_{i}$ define a morphism

$f:X\to\mathbb{P}^{m},~{}P\in X\mapsto(f_{0}(P):\cdots:f_{m}(P)).$

###### Proof.

First of all note that $f$ is well-defined set-theoretically: we have assumed that the image point can never be $(0:\cdots:0)$; and if we rescale the homogeneous coordinates $x_{i}$ we get

$(f_{0}(\lambda x_{0}:\cdots:\lambda x_{n}):\cdots:f_{m}(\lambda x_{0}:\cdots:\lambda x_{n}))$
$~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}

---

3. Projective varieties

Note that at least one of the two points  $(x:y)$  and  $(y:z)$  is always well-defined; and if they are both defined they agree because of the equation  $xz = y^2$ . By lemma 3.3.9 both equations determine a morphism where they are well-defined; so by lemma 2.4.10 they glue to give an inverse morphism  $f^{-1}$ . Note that  $f^{-1}$  is a (quite simple) morphism between projective varieties that cannot be written globally in the form of lemma 3.3.9.

Summarizing, we have shown that  $f$  is an isomorphism: the curve  $\{xz = y^2\} \subset \mathbb{P}^2$  is isomorphic to  $\mathbb{P}^1$ . This example should be compared to exercise 2.6.1 and example 3.1.13. It is a special case of the Veronese embedding of 3.4.11.

Finally, let us analyze the isomorphism  $f$  geometrically. Let  $Q = (1:0:0) \in X$ , and let  $L \subset \mathbb{P}^2$  be the line  $\{x = 0\}$ . For any point  $P = (a:b:c) \neq Q$  there is a unique line  $\overline{PQ}$  through  $P$  and  $Q$  with equation  $yc = zb$ . This line has a unique intersection point  $\overline{PQ} \cap L$  with the line  $L$ , namely  $(0:b:c)$ . If we identify  $L$  with  $\mathbb{P}^1$  in the obvious way, we see that the above geometric construction gives us exactly  $f^{-1}(P) = \overline{PQ} \cap L$ . We say that  $f^{-1}$  is the projection from  $Q$  to  $L$ .

![img-3.jpeg](images/img-3.jpeg)

Example 3.3.12. Consider  $\mathbb{P}^n$  with homogeneous coordinates  $x_0, \ldots, x_n$ , and  $\mathbb{P}^m$  with homogeneous coordinates  $y_0, \ldots, y_m$ . We want to find an easy description of the product  $\mathbb{P}^n \times \mathbb{P}^m$ .

Let  $\mathbb{P}^N = \mathbb{P}^{(n + 1)(m + 1) - 1}$  be projective space with homogeneous coordinates  $z_{i,j},0\leq i\leq n,0\leq j\leq m$ . There is an obviously well-defined set-theoretic map  $f:\mathbb{P}^n\times \mathbb{P}^m\to \mathbb{P}^N$  given by  $z_{i,j} = x_iy_j$ .

Lemma 3.3.13. Let  $f: \mathbb{P}^n \times \mathbb{P}^m \to \mathbb{P}^N$  be the set-theoretic map as above. Then:

(i) The image  $X = f(\mathbb{P}^n \times \mathbb{P}^m)$  is a projective variety in  $\mathbb{P}^N$ , with ideal generated by the homogeneous polynomials  $z_{i,j}z_{i',j'} - z_{i,j'}z_{i',j}$  for all  $0 \leq i, i' \leq n$  and  $0 \leq j, j' \leq m$ .
(ii) The map  $f: \mathbb{P}^n \times \mathbb{P}^m \to X$  is an isomorphism. In particular,  $\mathbb{P}^n \times \mathbb{P}^m$  is a projective variety.
(iii) The closed subsets of  $\mathbb{P}^n\times \mathbb{P}^m$  are exactly those subsets that can be written as the zero locus of polynomials in  $k[x_0,\ldots ,x_n,y_0,\ldots ,y_m]$  that are bihomogeneous in the  $x_{i}$  and  $y_{i}$ .

The map  $f$  is called the Segre embedding.

Proof. (i): It is obvious that the points of  $f(\mathbb{P}^n \times \mathbb{P}^m)$  satisfy the given equations. Conversely, let  $P$  be a point in  $\mathbb{P}^N$  with coordinates  $z_{i,j}$  that satisfy the given equations. At least one of these coordinates must be non-zero; we can assume without loss of generality that it is  $z_{0,0}$ . Let us pass to affine coordinates by setting  $z_{0,0} = 1$ . Then we have  $z_{i,j} = z_{i,0}z_{0,j}$ ; so by setting  $x_i = z_{i,0}$  and  $y_j = z_{0,j}$  we obtain a point of  $\mathbb{P}^n \times \mathbb{P}^m$  that is mapped to  $P$  by  $f$ .

(ii): Continuing the above notation, let  $P \in f(\mathbb{P}^n \times \mathbb{P}^m)$  be a point with  $z_{0,0} = 1$ . If  $f(x_i, y_j) = P$ , it follows that  $x_0 \neq 0$  and  $y_0 \neq 0$ , so we can assume  $x_0 = 1$  and  $y_0 = 1$  as the  $x_i$  and  $y_j$  are only determined up to a common scalar. But then it follows that  $x_i = z_{i,0}$  and  $y_j = z_{0,j}$ ; i.e.  $f$  is bijective.

---

Andreas Gathmann

The same calculation shows that  $f$  and  $f^{-1}$  are given (locally in affine coordinates) by polynomial maps; so  $f$  is an isomorphism.

(iii): It follows by the isomorphism of (ii) that any closed subset of  $\mathbb{P}^n\times \mathbb{P}^m$  is the zero locus of homogeneous polynomials in the  $z_{i,j}$ , i.e. of bihomogeneous polynomials in the  $x_{i}$  and  $y_{j}$  (of the same degree). Conversely, a zero locus of bihomogeneous polynomials can always be rewritten as a zero locus of bihomogeneous polynomials of the same degree in the  $x_{i}$  and  $y_{i}$  by remark 3.1.11. But such a polynomial is obviously a polynomial in the  $z_{i,j}$ , so it determines an algebraic set in  $X\cong \mathbb{P}^n\times \mathbb{P}^m$ .

Example 3.3.14. By lemma 3.3.13,  $\mathbb{P}^1\times \mathbb{P}^1$  is (isomorphic to) the quadric surface

$$
X = \left\{\left(z _ {0, 0}: z _ {0, 1}: z _ {1, 0}: z _ {1, 1}\right); z _ {0, 0} z _ {1, 1} = z _ {1, 0} z _ {0, 1} \right\} \subset \mathbb {P} ^ {3}.
$$

by the isomorphism

$$
\mathbb {P} ^ {1} \times \mathbb {P} ^ {1} \rightarrow X, ((x _ {0}: x _ {1}), (y _ {0}: y _ {1})) \mapsto (x _ {0} y _ {0}: x _ {0} y _ {1}: x _ {1} y _ {0}: x _ {1} y _ {1}).
$$

In particular, the "lines"  $\mathbb{P}^1\times P$  and  $P\times \mathbb{P}^1$  in  $\mathbb{P}^1\times \mathbb{P}^1$  where the first or second factor is constant are mapped to lines in  $X\subset \mathbb{P}^3$ . We can see these two families of lines on the quadric surface  $X$ :

![img-4.jpeg](images/img-4.jpeg)

Corollary 3.3.15. Every projective variety is a variety.

Proof. We have already seen in proposition 3.3.6 that every projective variety is a prevariety, so by lemma 2.5.3 and lemma 2.5.4 it only remains to be shown that the diagonal  $\Delta(\mathbb{P}^n) \subset \mathbb{P}^n \times \mathbb{P}^n$  is closed. We can describe this diagonal as

$$
\Delta (\mathbb {P} ^ {n}) = \left\{\left(\left(x _ {0}: \dots : x _ {n}\right), \left(y _ {0}: \dots : y _ {n}\right)\right); x _ {i} y _ {j} - x _ {j} y _ {i} = 0 \text {f o r a l l} i, j \right\},
$$

because these equations mean exactly that the matrix

$$
\left( \begin{array}{c c c c} x _ {0} &amp; x _ {1} &amp; \dots &amp; x _ {n} \\ y _ {0} &amp; y _ {1} &amp; \dots &amp; y _ {n} \end{array} \right)
$$

has rank (at most 1), i.e. that  $(x_0:\dots :x_n) = (y_0:\dots :y_n)$

In particular, it follows by lemma 3.3.13 (iii) that  $\Delta (\mathbb{P}^n)\subset \mathbb{P}^n\times \mathbb{P}^n$  is closed.

3.4. The main theorem on projective varieties. The most important property of projective varieties is that they are compact in the classical topology (if the ground field is  $k = \mathbb{C}$ ). We have seen this already for projective spaces in remark 3.1.5, and it then follows for projective algebraic sets as well as they are closed subsets (even in the classical topology) of the compact projective spaces. Unfortunately, the standard definition of compactness does not make sense at all in the Zariski topology, so we need to find an alternative description.

One property of compact sets is that they are mapped to compact sets under continuous maps. In our language, this would mean that images of projective varieties under a morphism should be closed. This is what we want to prove.

---

3. Projective varieties

Remark 3.4.1. Note first that this property definitely does not hold for affine varieties: consider e.g. the affine variety  $X = \{(x,y); xy = 1\} \subset \mathbb{A}^2$  and the projection morphism  $f: X \to \mathbb{A}^1$ ,  $(x,y) \mapsto x$ . The image of  $f$  is  $\mathbb{A}^1 \backslash \{0\}$ , which is not closed in  $\mathbb{A}^1$ . In fact, we can see from example 3.1.13 why it is not closed: the "vertical point at infinity", which would map to  $x = 0 \in \mathbb{A}^1$  and make the image closed, is missing in the affine variety  $X$ .

![img-5.jpeg](images/img-5.jpeg)

To prove the above mentioned statement we start with a special case (from which the general one will follow easily).

Theorem 3.4.2. The projection map  $\pi : \mathbb{P}^n \times \mathbb{P}^m \to \mathbb{P}^n$  is closed, i.e. if  $X \subset \mathbb{P}^n \times \mathbb{P}^m$  is closed then so is  $\pi(X)$ .

Proof. Let  $X \subset \mathbb{P}^n \times \mathbb{P}^m$  be an algebraic set. By lemma 3.3.13 (iii) we can write  $X$  as the zero locus of polynomials  $f_1(x,y), \ldots, f_r(x,y)$  bihomogeneous in the coordinates  $x_i$  of  $\mathbb{P}^n$  and  $y_i$  of  $\mathbb{P}^m$  (where we use the short-hand notation  $f_i(x,y)$  for  $f_i(x_0, \ldots, x_n, y_0, \ldots, y_m)$ ). By remark 3.1.11 we may assume that all  $f_i$  have the same degree  $d$  in the  $y_i$ .

Let  $P \in \mathbb{P}^n$  be a fixed point. Then  $P \in \pi(X)$  if and only if the common zero locus of the polynomials  $f_i(P, y)$  in  $y$  is non-empty in  $\mathbb{P}^m$ , which by proposition 3.2.5 is the case if and only if

$$
\left(y _ {0}, \dots , y _ {m}\right) ^ {s} \notin \left(f _ {1} (P, y), \dots , f _ {r} (P, y)\right) \tag {*}
$$

for all  $s \geq 0$ . As  $(*)$  is obvious for  $s &lt; d$ , it suffices to show that for any  $s \geq d$ , the set of all  $P \in \mathbb{P}^n$  satisfying  $(*)$  is closed, as  $\pi(X)$  will then be the intersection of all these sets and therefore closed as well.

Note that the ideal  $(y_0, \ldots, y_m)^s$  is generated by the  $\binom{m+s}{m}$  monomials of degree  $s$  in the  $y_i$ , which we denote by  $M_i(y)$  (in any order). Hence  $(*)$  is not satisfied if and only if there are polynomials  $g_{i,j}(y)$  such that  $M_i(y) = \sum_j g_{i,j}(y)f_j(P,y)$  for all  $i$ . As the  $M_i$  and  $f_j$  are homogeneous of degree  $s$  and  $d$ , respectively, this is the same as saying that such relations exist with the  $g_{i,j}$  homogeneous of degree  $s - d$ . But if we let  $N_i(y)$  be the collection of all monomials in the  $y_i$  of degree  $s - d$ , this is in turn equivalent to saying that the collection of polynomials  $\{N_i(y)f_j(P,y); 1 \leq i \leq \binom{m+s-d}{m}, 1 \leq j \leq r\}$  generates the whole vector space of polynomials of degree  $s$ . Writing the coefficients of these polynomials in a matrix  $A = A_s(P)$ , this amounts to saying that  $A$  has rank (at least)  $\binom{m+s}{m}$ . Hence  $(*)$  is satisfied if and only if all minors of  $A$  of size  $\binom{m+s}{m}$  vanish. But as the entries of the matrix  $A$  are homogeneous polynomials in the coefficients of  $P$ , it follows that the set of all  $P$  satisfying  $(*)$  is closed.

Remark 3.4.3. Let us look at theorem 3.4.2 from an algebraic viewpoint. We start with some equations  $f_{i}(x,y)$  and ask for the image of the projection map  $(x,y)\mapsto x$ , which can be written as

$\{x$  ; there is a  $y$  such that  $f_{i}(x,y) = 0$  for all  $i\}$

---

n other words, we are trying to *eliminate* the variables $y$ from the system of equations $f_{i}(x,y)=0$. The statement of the theorem is that the set of all such $x$ can itself be written as the solution set of some polynomial equations. This is sometimes called the *main theorem of elimination theory*.

###### Corollary 3.4.4.

The projection map $\pi:\mathbb{P}^{n}\times Y\to Y$ is closed for any variety $Y$.

###### Proof.

Let us first show the statement for $Y\subset\mathbb{A}^{m}$ being an affine variety. Then we can regard $Y$ as a subspace of $\mathbb{P}^{m}$ via the embedding $\mathbb{A}^{m}\subset\mathbb{P}^{m}$ ($Y$ is neither open nor closed in $\mathbb{P}^{m}$, but that does not matter). Now if $Z\subset\mathbb{P}^{n}\times Y$ is closed, let $\bar{Z}\subset\mathbb{P}^{n}\times\mathbb{P}^{m}$ be the projective closure. By theorem 3.4.2, $\pi(\bar{Z})$ is closed in $\mathbb{P}^{m}$, where $\pi$ is the projection morphism. Therefore

$\pi(Z)=\pi(\bar{Z}\cap(\mathbb{P}^{n}\times Y))=\pi(\bar{Z})\cap Y$

is closed in $Y$.

If $Y$ is any variety we can cover it by affine open subsets. As the condition that a subset is closed can be checked by restricting it to the elements of an open cover, the statement follows from the corresponding one for the affine open patches that we have just shown. ∎

###### Remark 3.4.5.

Corollary 3.4.4 is in fact the property of $\mathbb{P}^{n}$ that captures the idea of compactness (as we will see in corollary 3.4.7). Let us therefore give it a name: we say that a variety $X$ is complete if the projection map $\pi:X\times Y\to Y$ is closed for every variety $Y$. (You can think of the name “complete” as coming from the geometric idea that it contains all the “points at infinity” that were missing in affine varieties.) So corollary 3.4.4 says that $\mathbb{P}^{n}$ is complete. Moreover, any projective variety $Z\subset\mathbb{P}^{n}$ is complete, because any closed set in $Z\times Y$ is also closed in $\mathbb{P}^{n}\times Y$, so its image under the projection morphism to $Y$ will be closed as well.

###### Remark 3.4.6.

We have just seen that every projective variety is complete. In fact, whereas the converse of this statement is not true, it is quite hard to write down an example of a complete variety that is not projective. We will certainly not meet such an example in the near future. So for practical purposes you can usually assume that the terms “projective variety” and “complete variety” are synonymous.

###### Corollary 3.4.7.

Let $f:X\to Y$ be a morphism of varieties, and assume that $X$ is complete. Then the image $f(X)\subset Y$ is closed.

###### Proof.

We factor $f$ as $f:X\xrightarrow{\Gamma}X\times Y\xrightarrow{\pi}Y$, where $\Gamma=(\mathrm{id}_{X},f)$ (the so-called *graph morphism*), and $\pi$ is the projection to $Y$.

We claim that $\Gamma(X)=\{(P,f(P))~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}\text{;}~{}~{}~{}~{}P\in X\}\subset X\times Y$ is closed. To see this, note first that the diagonal $\Delta(Y)\subset Y\times Y$ is closed as $Y$ is a variety. Now $\Gamma(X)$ is just the inverse image of $\Delta(Y)$ under the morphism $(f,\mathrm{id}_{Y}):X\times Y\to Y\times Y$, and is therefore also closed.

As $X$ is complete, it follows that $f(X)=\pi(\Gamma(X))$ is closed. ∎

###### Corollary 3.4.8.

Let $X\subset\mathbb{P}^{n}$ be a projective variety that contains more than one point, and let $f\in k[x_{0},\ldots,x_{n}]$ be a non-constant homogeneous polynomial. Then $X\cap Z(f)\neq\emptyset$.

###### Proof.

Assume that the statement is false, i. e. that $f$ is non-zero on all of $X$. Let $P,Q\in X$ be two distinct points of $X$ and choose a homogeneous polynomial $g\in k[x_{0},\ldots,x_{n}]$ of the same degree as $f$ such that $g(P)=0$ and $g(Q)\neq 0$. Let $F:X\to\mathbb{P}^{1}$ be the morphism defined by $R\mapsto(f(R):g(R))$; this is well-defined as $f$ is non-zero on $X$ by assumption.

By corollary 3.4.7 the image $F(X)$ is closed in $\mathbb{P}^{1}$. Moreover, $F(X)$ is irreducible as $X$ is. Therefore, $F(X)$ is either a point or all of $\mathbb{P}^{1}$. But by assumption $(0:1)\notin F(X)$, so $F(X)$ must be a single point. But this is a contradiction, as $F(P)=(f(P):g(P))=(1:0)$ and $F(Q)=(f(Q):g(Q))\neq(1:0)$ by the choice of $g$. ∎

---

Remark 3.4.9.

Again this statement is false for affine varieties: consider e. g. $X=\{x=0\}\subset\mathbb{A}^{2}$ and $f=x-1$, then $X\cap Z(f)=\emptyset$ although $X$ is a line (and therefore contains more than one point). This example worked because in $\mathbb{A}^{2}$ we can have parallel lines. In $\mathbb{P}^{2}$ such lines would meet at infinity, so the intersection would be non-empty then.

###### Corollary 3.4.10.

Every regular function on a complete variety is constant.

###### Proof.

Let $f:X\to\mathbb{A}^{1}$ be a regular function on a complete variety $X$. Consider $f$ as a morphism to $\mathbb{P}^{1}$ that does not assume the value $\infty$. In particular, $f(X)\subsetneq\mathbb{P}^{1}$, hence it is a single point by corollary 3.4.7. ∎

###### Example 3.4.11.

(This is a generalization of example 3.3.11 and exercise 3.5.2.) Let $f_{i}(x_{0},\ldots,x_{n}),0\leq i\leq N=\binom{n+d}{n}-1$ be the set of all monomials in $k[x_{0},\ldots,x_{n}]$ of degree $d$, i. e. of the monomials of the form $x_{0}^{i_{0}}\cdots x_{n}^{i_{n}}$ with $i_{0}+\cdots+i_{n}=d$. Consider the map

$F:\mathbb{P}^{n}\to\mathbb{P}^{N},\;(x_{0}:\cdots:x_{n})\mapsto(f_{0}:\cdots:f_{N}).$

By lemma 3.3.9 this is a morphism (note that the monomials $x_{0}^{d},\ldots,x_{n}^{d}$, which cannot be simultaneously zero, are among the $f_{i}$). So by corollary 3.4.7 the image $X=F(\mathbb{P}^{n})$ is a projective variety.

We claim that $F:X\to F(X)$ is an isomorphism. All we have to do to prove this is to find an inverse morphism. This is not hard: we can do this on an affine open cover, so let us consider the open subset where $x_{0}\neq 0$ (and therefore $x_{0}^{d}\neq 0$). We can then pass to affine coordinates and set $x_{0}=1$. The inverse morphism is then given by $x_{i}=\frac{x_{i}x_{0}^{d-1}}{x_{0}^{d}}$ for $1\leq 1\leq n$.

The morphism $F$ is therefore an isomorphism and thus realizes $\mathbb{P}^{n}$ as a subvariety of $\mathbb{P}^{N}$. This is usually called the degree-$d$ Veronese embedding. Its importance lies in the fact that degree-$d$ polynomials in the coordinates of $\mathbb{P}^{n}$ are translated into *linear* polynomials when viewing $\mathbb{P}^{n}$ as a subvariety of $\mathbb{P}^{N}$. An example of this application will be given in corollary 3.4.12.

The easiest examples are the degree-$d$ embeddings of $\mathbb{P}^{1}$, given by

$\mathbb{P}^{1}\to\mathbb{P}^{d},\;(s:t)\mapsto(s^{d}:s^{d-1}t:s^{d-2}t^{2}:\cdots:t^{d}).$

The special cases $d=2$ and $d=3$ are considered in example 3.3.11 and exercise 3.5.2.

Note that by applying corollary 3.4.7 we could conclude that $F(X)$ is a projective variety without writing down its equations. Of course, in theory we could also write down the equations, but this is quite messy in this case.

###### Corollary 3.4.12.

Let $X\subset\mathbb{P}^{n}$ be a projective variety, and let $f\in k[x_{0},\ldots,x_{n}]$ be a non-constant homogeneous polynomial. Then $X\backslash Z(f)$ is an affine variety.

###### Proof.

We know this already if $f$ is a linear polynomial (see the proof of proposition 3.3.6). But by applying a Veronese embedding of degree $d$, we can always assume this. ∎

### 3.5. Exercises

###### Exercise 3.5.1.

Let $L_{1}$ and $L_{2}$ be two disjoint lines in $\mathbb{P}^{3}$, and let $P\in\mathbb{P}^{3}\backslash(L_{1}\cup L_{2})$ be a point. Show that there is a unique line $L\subset\mathbb{P}^{3}$ meeting $L_{1}$, $L_{2}$, and $P$ (i. e. such that $P\in L$ and $L\cap L_{i}\neq\emptyset$ for $i=1,2$).

###### Exercise 3.5.2.

Let $C\subset\mathbb{P}^{3}$ be the “twisted cubic curve” given by the parametrization

$\mathbb{P}^{1}\to\mathbb{P}^{3}\quad(s:t)\mapsto(x:y:z:w)=(s^{3}:s^{2}t:st^{2}:t^{3}).$

Let $P=(0:0:1:0)\in\mathbb{P}^{3}$, and let $H$ be the hyperplane defined by $z=0$. Let $\varphi$ be the projection from $P$ to $H$, i. e. the map associating to a point $Q$ of $C$ the intersection point of the unique line through $P$ and $Q$ with $H$

---

1. Show that $\varphi$ is a morphism.
2. Determine the equation of the curve $\varphi(C)$ in $H\cong\mathbb{P}^{2}$.
3. Is $\varphi:C\to\varphi(C)$ an isomorphism onto its image?

###### Exercise 3.5.3.

Let $I\subset k[x_{1},\dots,x_{n}]$ be an ideal. Define $I^{h}$ to be the ideal generated by $\{f^{h}\mbox{ ; }f\in I\}\subset k[x_{0},\dots,x_{n}]$, where

$f^{h}(x_{0},\dots,x_{n}):=x_{0}^{\deg(f)}\cdot f\left(\frac{x_{1}}{x_{0}},\dots,\frac{x_{n}}{x_{0}}\right)$

denotes the homogenization of $f$ with respect to $x_{0}$. Show that:

1. $I^{h}$ is a homogeneous ideal.
2. $Z(I^{h})\subset\mathbb{P}^{n}$ is the closure of $Z(I)\subset\mathbb{A}^{n}$ in $\mathbb{P}^{n}$. We call $Z(I^{h})$ the projective closure of $Z(I)$.
3. Let $I=(f_{1},\dots,f_{k})$. Show by an example that $I^{h}\neq(f_{1}^{h},\dots,f_{k}^{h})$ in general. (Hint: You may consider (again) the twisted cubic curve of exercise 3.5.2.)

###### Exercise 3.5.4.

In this exercise we will make the space of all lines in $\mathbb{P}^{n}$ into a projective variety.

Fix $n\geq 1$. We define a set-theoretic map

$\varphi:\{\mbox{lines in $\mathbb{P}^{n}$}\}\to\mathbb{P}^{N}$

with $N={n+1\choose 2}-1$ as follows. For every line $L\subset\mathbb{P}^{n}$ choose two distinct points $P=(a_{0}:\cdots:a_{n})$ and $Q=(b_{0}:\cdots:b_{n})$ on $L$ and define $\varphi(L)$ to be the point in $\mathbb{P}^{N}$ whose homogeneous coordinates are the ${n+1\choose 2}$ maximal minors of the matrix

\[ \left(\begin{array}[]{ccc}a_{0}&\cdots&a_{n}\\
b_{0}&\cdots&b_{n}\end{array}\right), \]

in any fixed order. Show that:

1. The map $\varphi$ is well-defined and injective.
2. The image of $\varphi$ is a projective variety that has a finite cover by affine spaces $\mathbb{A}^{2(n-1)}$ (in particular, its dimension is $2(n-1)$). It is called the Grassmannian $G(1,n)$. Hint: recall that by the Gaussian algorithm most matrices (what does this mean?) are equivalent to one of the form

\[ \left(\begin{array}[]{cccc}1&0&a_{2}^{\prime}&\cdots&a_{n}^{\prime}\\
0&1&b_{2}^{\prime}&\cdots&b_{n}^{\prime}\end{array}\right) \]

for some $a_{i}^{\prime},b_{i}^{\prime}$.
3. $G(1,1)$ is a point, $G(1,2)\cong\mathbb{P}^{2}$, and $G(1,3)$ is the zero locus of a quadratic equation in $\mathbb{P}^{5}$.

###### Exercise 3.5.5.

Let $V$ be the vector space over $k$ of homogeneous degree-$2$ polynomials in three variables $x_{0},x_{1},x_{2}$, and let $\mathbb{P}(V)\cong\mathbb{P}^{5}$ be its projectivization.

1. Show that the space of conics in $\mathbb{P}^{2}$ can be identified with an open subset $U$ of $\mathbb{P}^{5}$. (One says that $U$ is a “moduli space” for conics in $\mathbb{P}^{2}$ and that $\mathbb{P}^{5}$ is a “compactified moduli space”.) What geometric objects can be associated to the points in $\mathbb{P}^{5}\backslash U$?
2. Show that it is a linear condition in $\mathbb{P}^{5}$ for the conics to pass through a given point in $\mathbb{P}^{2}$. More precisely, if $P\in\mathbb{P}^{2}$ is a point, show that there is a linear subspace $L\subset\mathbb{P}^{5}$ such that the conics passing through $P$ are exactly those in $U\cap L$. What happens in $\mathbb{P}^{5}\backslash U$, i. e. what do the points in $(\mathbb{P}^{5}\backslash U)\cap L$ correspond to?
3. Prove that there is a unique conic through any five given points in $\mathbb{P}^{2}$, as long as no three of them lie on a line. What happens if three of them do lie on a line?

---

3. Projective varieties

Exercise 3.5.6. Show that an affine variety over $\mathbb{C}$ is never compact in the classical topology unless it is a single point. (Hint: Given an affine variety $X \subset \mathbb{A}^n$, show that the image of $X$ under the projection map $\mathbb{A}^n \to \mathbb{A}^1$ onto the first coordinate is either a point or an open subset (in the Zariski topology) of $\mathbb{A}^1$. Conclude that an affine variety with more than one point is never bounded, i.e., is never contained in a ball $\{(z_1, \ldots, z_n) ; |z_1|^2 + \cdots + |z_n|^2 \leq R^2\} \subset \mathbb{C}^n$, and therefore not compact.)

Exercise 3.5.7. Let $G(1, n)$ be the Grassmannian of lines in $\mathbb{P}^n$ as in exercise 3.5.4. Show that:

(i) The set $\{(L, P); P \in L\} \subset G(1, n) \times \mathbb{P}^n$ is closed.

(ii) If $Z \subset G(1, n)$ is any closed subset then the union of all lines $L \subset \mathbb{P}^n$ such that $L \in Z$ is closed in $\mathbb{P}^n$.

(iii) Let $X, Y \subset \mathbb{P}^n$ be disjoint projective varieties. Then the union of all lines in $\mathbb{P}^n$ intersecting $X$ and $Y$ is a closed subset of $\mathbb{P}^n$. It is called the join $J(X, Y)$ of $X$ and $Y$.

Exercise 3.5.8. Recall that a conic is a curve in $\mathbb{P}^2$ that can be given as the zero locus of an irreducible homogeneous polynomial $f \in k[x_0, x_1, x_2]$ of degree 2. Show that for any 5 given points $P_1, \ldots, P_5 \in \mathbb{P}^2$ in general position, there is a unique conic passing through all the $P_i$. This means: there is a non-empty open subset $U \subset \mathbb{P}^2 \times \cdots \times \mathbb{P}^2$ such that there is a unique conic through the $P_i$ whenever $(P_1, \ldots, P_5) \in U$. (Hint: By mapping a conic $\{a_0x_0^2 + a_1x_1^2 + a_2x_2^2 + a_3x_0x_1 + a_4x_0x_2 + a_5x_1x_2 = 0\}$ to the point $(a_0 : \cdots : a_5) \in \mathbb{P}^5$, you can think of "the space of all conics" as an open subset of $\mathbb{P}^5$.)