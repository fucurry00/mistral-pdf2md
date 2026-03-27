4. Dimension

We have already introduced the concept of dimension of a variety. Now we develop some methods that allow to compute the dimension of most varieties rigorously. We show that the dimension of $\mathbb{A}^{n}$ and $\mathbb{P}^{n}$ is $n$. The dimension of a variety equals the dimension of any of its non-empty open subsets. Every irreducible component of the zero locus of a single function on an affine or projective variety $X$ has dimension $\dim X-1$.

Two varieties are called birational if they contain isomorphic open subsets. As a large class of examples of birational varieties we construct the blow-up of an affine variety in a subvariety or an ideal. We study in detail the case of blowing up a single point $P$ in a variety $X$. In this case, the exceptional hypersurface is the tangent cone $C_{X,P}$.

For any point $P$ in a variety $X$, the tangent space $T_{X,P}$ is the linear space dual to $M/M^{2}$, where $M\subset\mathcal{O}_{X,P}$ is the maximal ideal. The point $P$ is called a smooth point of $X$ if $T_{X,P}=C_{X,P}$, i. e. if $X$ “can be approximated linearly” around $P$. Smoothness can easily be checked by the Jacobi criterion.

As an application of the theory developed so far, we show that every smooth cubic surface $X$ has exactly 27 lines on it. We study the configuration of these lines, and show that $X$ is isomorphic to $\mathbb{P}^{2}$ blown up in 6 suitably chosen points.

### 4.1. The dimension of projective varieties

Recall that in section 1.3 we have introduced the notion of dimension for every (Noetherian) topological space, in particular for every variety $X$: the dimension $\dim X$ of $X$ is the largest integer $n$ such that there is a chain of irreducible closed subsets of $X$

$\emptyset\neq X_{0}\subsetneq X_{1}\subsetneq\cdots\subsetneq X_{n}=X.$

For simplicity of notation, in what follows we will call this a *longest chain* in $X$.

While this definition is quite simple to write down, it is very difficult to use in practice. In fact, we have not even been able yet to compute the dimensions of quite simple varieties like $\mathbb{A}^{n}$ or $\mathbb{P}^{n}$ (although it is intuitively clear that these spaces should have dimension $n$). In this section, we will develop techniques that allow us to compute the dimensions of varieties rigorously.

###### Remark 4.1.1.

We will start our dimension computations by considering projective varieties. It should be said clearly that the theory of dimension is in no way special or easier for projective varieties than it is for other varieties — in fact, it should be intuitively clear that the dimension of a variety is essentially a *local* concept that can be computed in the neighborhood of any point. The reason for us to start with projective varieties is simply that we know more about them: the main theorem on projective varieties and its corollaries of section 3.4 are so strong that they allow for quite efficient applications in dimension theory. One could as well start by looking at the dimensions of affine varieties (and most textbooks will do so), but this requires quite some background in (commutative) algebra that we do not have yet.

###### Remark 4.1.2.

The main idea for our dimension computations is to compare the dimensions of varieties that are related by morphisms with various properties. For example, if $f:X\to Y$ is a *surjective* morphism, we would expect that $\dim X\geq\dim Y$. If $f:X\to Y$ is a morphism with finite fibers, i. e. such that $f^{-1}(P)$ is a finite set for all $P\in Y$, we would expect that $\dim X\leq\dim Y$. In particular, if a morphism both is surjective and has finite fibers, we expect that $\dim X=\dim Y$.

###### Example 4.1.3.

The standard case in which we will prove and apply the idea of comparing dimensions is the case of projections from a point. We have already seen such projections in example 3.3.11 and exercise 3.5.2; let us now consider the general case.

---

4. Dimension

Let  $X \subsetneq \mathbb{P}^n$  be a projective variety, and let  $P \in \mathbb{P}^n$  be a point that is not in  $X$ . By a change of coordinates we can assume that  $P = (0 : \dots : 0 : 1)$ . Let  $H \cong \mathbb{P}^{n-1} \subset \mathbb{P}^n$  be a linear subspace of codimension 1 that does not contain  $P$ ; again by a change of coordinates we can assume that  $H = \{x_n = 0\}$ . We define a projection map  $\pi : X \to H$  from  $P$  as follows: for every point  $Q \in X$  let  $\pi(Q)$  be the intersection point of the line  $\overline{PQ}$  with  $H$ . (Note that this is well-defined as  $Q \neq P$  by assumption.)

![img-0.jpeg](images/img-0.jpeg)

This is in fact a morphism: if  $Q = (a_0 : \dots : a_n) \in X$ , the line  $\overline{PQ}$  is given parametrically by

$$
\overline {{P Q}} = \left\{\left(\lambda a _ {0}: \dots : \lambda a _ {n - 1}: \lambda a _ {n} + \mu\right) \in \mathbb {P} ^ {n}; (\lambda : \mu) \in \mathbb {P} ^ {1} \right\}.
$$

The intersection point of this line with  $H$  is obviously the point  $(a_0 : \dots : a_{n-1} : 0)$ , which is well-defined by the assumption that  $Q \neq P$ . Hence the projection  $\pi$  is given in coordinates by

$$
\pi : X \to \mathbb {P} ^ {n - 1}, (a _ {0}: \dots : a _ {n}) \mapsto (a _ {0}: \dots : a _ {n - 1}).
$$

In particular, this is a polynomial map and therefore a morphism.

Note that projections always have finite fibers: by construction, the inverse image  $\pi^{-1}(Q)$  of a point  $Q\in H$  must be contained in the line  $\overline{PQ}\cong \mathbb{P}^1$ , but it must also be an algebraic set and cannot contain the point  $P$ , hence it must be a finite set.

Note also that we can repeat this process if the image of  $X$  is not all of  $\mathbb{P}^{n-1}$ : we can then project  $\pi(X)$  from a point in  $\mathbb{P}^{n-1}$  to  $\mathbb{P}^{n-2}$ , and so on. After a finite number of such projections, we arrive at a surjective morphism  $X \to \mathbb{P}^m$  for some  $m$  that is the composition of projections as above. In particular, as this morphism is surjective and has finite fibers, we expect  $\dim X = m$ . This is the idea that we will use for our dimension computations.

Let us start with some statements about dimensions that are not only intuitively clear but actually also easy to prove.

# Lemma 4.1.4.

(i) If  $\emptyset \neq X_0 \subsetneq \dots \subsetneq X_n = X$  is a longest chain in  $X$  then  $\dim X_i = i$  for all  $i$ .
(ii) If  $Y \subsetneq X$  is a closed subvariety of the variety  $X$  then  $\dim Y &lt; \dim X$ .
(iii) Let  $f: X \to Y$  be a surjective morphism of projective varieties. Then every longest chain  $\emptyset \neq Y_0 \subsetneq \dots \subsetneq Y_n$  in  $Y$  can be lifted to a chain  $\emptyset \neq X_0 \subsetneq \dots \subsetneq X_n$  in  $X$  (i.e. the  $X_i$  are closed and irreducible with  $f(X_i) = Y_i$  for all  $i$ ). In particular,  $\dim X \geq \dim Y$ .

Proof. (i): It is obvious that  $\dim X_i \geq i$ . If we had  $\dim X_i &gt; i$  there would be a longer chain in  $X_i$  than  $\emptyset \neq X_0 \subsetneq \dots \subsetneq X_i$ . This chain could then be extended by the  $X_j$  for  $j &gt; i$  to a chain in  $X$  that is longer than the given one.

(ii): We can extend a longest chain  $\emptyset \neq Y_0 \subsetneq Y_1 \subsetneq \dots \subsetneq Y_n = Y$  in  $Y$  to a chain  $\emptyset \neq Y_0 \subsetneq Y_1 \subsetneq \dots \subsetneq Y_n = Y \subsetneq X$  in  $X$  which is one element longer.
(iii): We prove the statement by induction on  $n = \dim Y$ ; there is nothing to show if  $n = 0$ . Otherwise let  $Z_{1},\ldots ,Z_{r}\subset X$  be the irreducible components of  $f^{-1}(Y_{n - 1})$ , so that  $f(Z_{1})\cup \dots \cup f(Z_{r}) = Y_{n - 1}$ . Note that  $Y_{n - 1}$  is irreducible and the  $f(Z_{i})$  are closed by corollary

---

3.4.7, so one $Z_{i}$ must map surjectively to $Y_{n-1}$. Applying the induction hypothesis to the restriction $f|_{Z_{i}}:Z_{i}\to Y_{n-1}$ we get $\dim Z_{i}\geq\dim Y_{n-1}=n-1$, so there is a chain $\emptyset\neq X_{0}\subsetneq\cdots\subsetneq X_{n-1}=Z_{i}$. Extending this chain by $X$ at the end, we thus obtain a chain in $X$ of length $n$ lying over the given chain in $Y$. ∎

###### Lemma 4.1.5.

Let $X\subseteq\mathbb{P}^{n}$ be a projective variety, and assume without loss of generality that $P=(0:\cdots:0:1)\notin X$.

1. Any homogeneous polynomial $f\in k[x_{0},\ldots,x_{n}]$ satisfies a relation of the form

$f^{D}+a_{1}f^{D-1}+a_{2}f^{D-2}+\cdots+a_{D}=0\quad\text{in }S(X)=k[x_{0},\ldots,x_{n}]/I(X)$

for some $D>0$ and some homogeneous polynomials $a_{i}\in k[x_{0},\ldots,x_{n-1}]$ that do not depend on the last variable $x_{n}$.
2. Let $\pi:X\to\mathbb{P}^{n-1}$ be the projection from $P$ as in example 4.1.3. If $Y\subset X$ is a closed subvariety such that $\pi(Y)=\pi(X)$ then $Y=X$.

###### Remark 4.1.6.

Before we prove this lemma let us give the idea behind these statements. In (i), you should think of $f$ as being a polynomial containing the variable $x_{n}$, while the $a_{i}$ do not. So for given values of $x_{0},\ldots,x_{n-1}$ the relation in (i) is a non-zero polynomial equation in $x_{n}$ that therefore allows only finitely many values for $x_{n}$ on $X$. As the projection from $P$ is just given by dropping the last coordinate $x_{n}$, the statement of (i) is just that this projection map has finite fibers.

We have argued in remark 4.1.1 that we then expect the dimension of $\pi(X)$ to be less than or equal to the dimension of $X$. To show this we will want to take a longest chain in $X$ and project it down to $\pi(X)$. It is obvious that the images of the elements of such a chain in $X$ are again closed subvarieties in $\pi(X)$, but it is not a priori obvious that a strict inclusion $X_{i}\subsetneq X_{i+1}$ translates into a strict inclusion $\pi(X_{i})\subsetneq\pi(X_{i+1})$. This is exactly the statement of (ii).

###### Proof.

(i): Let $d$ be the degree of $f$. Consider the morphism

$\tilde{\pi}:X\to\mathbb{P}^{n},\;(x_{0}:\cdots:x_{n})\mapsto(y_{0}:\cdots:y_{n}):=(x_{0}^{d}:\cdots:x_{n-1}^{d}:f(x_{0},\ldots,x_{n}))$

(which is well-defined since $P\notin X$). The image of $\tilde{\pi}$ is closed by corollary 3.4.7 and is therefore the zero locus of some homogeneous polynomials $F_{1},\ldots,F_{r}\in k[y_{0},\ldots,y_{n}]$. Note that

$Z(y_{0},\ldots,y_{n-1},F_{1},\ldots,F_{r})=\emptyset\subset\mathbb{P}^{n}$

because the $F_{i}$ require the point to be in the image $\tilde{\pi}(X)$, while the $x_{0},\ldots,x_{n-1}$ do not vanish simultaneously on $X$. So by the projective Nullstellensatz of proposition 3.2.5 (iv) it follows that some power of $y_{n}$ is in the ideal generated by $y_{0},\ldots,y_{n-1},F_{1},\ldots,F_{r}$. In other words,

$y_{n}^{D}=\sum_{i=0}^{n-1}g_{i}(y_{0},\ldots,y_{n})\cdot y_{i}\quad\text{in }S(\tilde{\pi}(X))=k[y_{0},\ldots,y_{n}]/(F_{1},\ldots,F_{r})$

for some $D$. Substituting the definition of $\tilde{\pi}$ for the $y_{i}$ thus shows that there is a relation

$f^{D}+a_{1}f^{D-1}+a_{2}f^{D-2}+\cdots+a_{D}=0\quad\text{in }S(X)$

for some homogeneous $a_{i}\in k[x_{0},\ldots,x_{n-1}]$.

(ii): Assume that the statement is false, i. e. that $Y\subsetneq X$. Then we can pick a homogeneous polynomial $f\in I(Y)\backslash I(X)\subset k[x_{0},\ldots,x_{n}]$ of some degree $d$ that vanishes on $Y$ but not on $X$.

Now pick a relation as in (i) for the smallest possible value of $D$. In particular we then have $a_{D}\neq 0$ in $S(X)$, i. e. $a_{D}\notin I(X)$. But we have chosen $f$ such that $f\in I(Y)$, therefore the relation (i) tells us that $a_{D}\in I(Y)$ as well.

---

It follows that $a_{D}\in I(Y)\backslash I(X)$. But note that $a_{D}\in k[x_{0},\ldots,x_{n-1}]$, so $a_{D}$ is a function on $\mathbb{P}^{n-1}$ that vanishes on $\pi(Y)$ but not on $\pi(X)$, in contradiction to the assumption. ∎

###### Corollary 4.1.7.

Let $X\subsetneq\mathbb{P}^{n}$ be a projective variety, and assume without loss of generality that $P=(0:\cdots:0:1)\notin X$. Let $\pi:X\to\mathbb{P}^{n-1}$ be the projection from $P$ as in example 4.1.3. Then $\dim X=\dim\pi(X)$.

###### Proof.

Let $\emptyset\neq X_{0}\subsetneq\cdots\subsetneq X_{r}=X$ be a longest chain in $X$. Then $\emptyset\neq Y_{0}\subsetneq\cdots\subsetneq Y_{r}=Y$ with $Y_{i}=\pi(X_{i})$ is a chain in $\pi(X)$: note that the $Y_{i}$ are closed by corollary 3.4.7, irreducible as they are the images of irreducible sets, and no two of them can coincide by lemma 4.1.5. It follows that $\dim\pi(X)\geq\dim X$. But also $\dim\pi(X)\leq\dim X$ by lemma 4.1.4 (iii), so the statement follows. ∎

###### Corollary 4.1.8.

The dimension of $\mathbb{P}^{n}$ is $n$.

###### Proof.

By lemma 4.1.4 (ii) we know that

$\dim\mathbb{P}^{0}<\dim\mathbb{P}^{1}<\dim\mathbb{P}^{2}<\dim\mathbb{P}^{3}<\cdots.$ ($\ast$)

Moreover, we have seen in example 4.1.3 that every projective variety $X$ can be mapped surjectively to some $\mathbb{P}^{n}$ by a sequence of projections from points; it then follows that $\dim X=\dim\mathbb{P}^{n}$ by corollary 4.1.7. In other words, every dimension that occurs as the dimension of some projective variety must occur already as the dimension of some projective space. But combining ($\ast$) with lemma 4.1.4 (i) we see that every non-negative integer occurs as the dimension of some projective variety — and therefore as the dimension of some projective space. So in ($\ast$) we must have $\dim\mathbb{P}^{n}=n$ for all $n$. ∎

###### Proposition 4.1.9.

Let $X\subset\mathbb{P}^{n}$ be a projective variety, and let $f\in k[x_{0},\ldots,x_{n}]$ be a non-constant homogeneous polynomial that does not vanish identically on $X$. Then $\dim(X\cap Z(f))=\dim X-1$.

###### Remark 4.1.10.

Note that in the statement of this proposition $X\cap Z(f)$ may well be reducible; the statement is then that there is at least one component that has dimension $\dim X-1$ (and that no component has bigger dimension). We will prove a stronger statement, namely a statement about *every* component of $X\cap Z(f)$, in corollary 4.2.5.

###### Proof.

Let $m=\dim X$. After applying a Veronese embedding of degree $\deg f$ as in example 3.4.11 we can assume that $f$ is linear. Now construct linear functions $f_{0},\ldots,f_{m}$ and algebraic sets $X_{0},\ldots,X_{m+1}\subset X$ inductively as follows: Let $X_{0}=X$ and $f_{0}=f$. For $i\geq 0$ let $X_{i+1}=X_{i}\cap Z(f_{i})$, and let $f_{i+1}$ be any linear form such that

1. $f_{i+1}$ does not vanish identically on any component of $X_{i+1}$, and
2. $f_{i+1}$ is linearly independent from the $f_{1},\ldots,f_{i}$.

It is obvious that (i) can always be satisfied. Moreover, (ii) is automatic if $X_{i+1}$ is not empty (as $f_{1},\ldots,f_{i}$ vanish on $X_{i+1}$), and easy to satisfy otherwise (as then (i) is no condition).

Applying lemma 4.1.4 (ii) inductively, we see that no component of $X_{i}$ has dimension bigger than $m-i$. In particular, $X_{m+1}$ must be empty. Hence the linear forms $f_{0},\ldots,f_{m}$ do not vanish simultaneously on $X$; so they define a morphism $\pi:X\to\mathbb{P}^{m}$. As the $f_{i}$ are linear and linearly independent, $\pi$ is up to a change of coordinates the same as $f_{i}=x_{i}$ for $0\leq i\leq m$, so it is just a special case of a continued projection from points as in example 4.1.3. In particular, $\dim\pi(X)=\dim X=m$ by corollary 4.1.7. By lemma 4.1.4 (ii) it then follows that $\pi(X)=\mathbb{P}^{m}$, i. e. $\pi$ is surjective.

Now suppose that every component of $X_{1}=X\cap Z(f)$ has already dimension at most $m-2$, then by the above inductive argument already $X_{m}$ is empty and the forms $f_{0},\ldots,f_{m-1}$ do not vanish simultaneously on $X$. But this means that $(0:\cdots:0:1)\notin\pi(X)$, which contradicts the surjectivity of $\pi$. ∎

##

---

### 4.2. The dimension of varieties

After having exploited the main theorem on projective varieties as far as possible, let us now study the dimension of more general varieties. We have already remarked that the dimension of a variety should be a local concept; in particular the dimension of any open subvariety $U$ of a variety $X$ should be the same as that of $X$. This is what we want to prove first.

###### Proposition 4.2.1.

Let $X$ be a variety, and let $U\subset X$ be a non-empty open subset of $X$. Then $\dim U=\dim X$.

###### Proof.

“$\leq$”: Let $\emptyset\neq U_{0}\subsetneq U_{1}\subsetneq\cdots\subsetneq U_{n}=U$ be a longest chain in $U$. If $X_{i}$ denotes the closure of $U_{i}$ in $X$ for all $i$, then $\emptyset\neq X_{0}\subsetneq\cdots\subsetneq X_{n}=X$ is a chain in $X$.

“$\geq$”: We will prove this in several steps.

Step 1: Let $\emptyset\neq X_{0}\subsetneq\cdots\subsetneq X_{n}=X$ be a longest chain in $X$, and assume that $X_{0}\subset U$. Then set $U_{i}=X_{i}\cap U$ for all $i$; we claim that $\emptyset\neq U_{0}\subsetneq\cdots\subsetneq U_{n}=U$ is a chain in $U$ (from which it then follows that $\dim U\geq\dim X$). In fact, the only statement that is not obvious here is that $U_{i}\neq U_{i+1}$ for all $i$. So assume that $U_{i}=U_{i+1}$ for some $i$. Then

$X_{i+1}$ $=(X_{i+1}\cap U)\cup(X_{i+1}\cap(X\backslash U))$
$=(X_{i}\cap U)\cup(X_{i+1}\cap(X\backslash U))$
$=X_{i}\cup(X_{i+1}\cap(X\backslash U)),$

where the last equality follows from $X_{i}\cap(X\backslash U)\subset X_{i+1}\cap(X\backslash U)$. But this is a contradiction to $X_{i+1}$ being irreducible, as $X_{i}$ is neither empty nor all of $X_{i+1}$. So we have now proven the proposition in the case where the element $X_{0}$ of a longest chain in $X$ lies in $U$.

Step 2: Let $X$ be a projective variety. Then we claim that we can always find a longest chain $\emptyset\neq X_{0}\subsetneq\cdots\subsetneq X_{n}$ (with $n=\dim X$) such that $X_{0}\subset U$. We will construct this chain by descending recursion on $n$, starting by setting $X_{n}=X$. So assume that $X_{i}\subsetneq X_{i+1}\subsetneq\cdots\subsetneq X_{n}=X$ has already been constructed such that $X_{i}\cap U\neq\emptyset$. Pick any non-constant homogeneous polynomial $f$ that does not vanish identically on any irreducible component of $X_{i}\backslash U$. By proposition 4.1.9 there is a component of $X_{i}\cap Z(f)$ of dimension $i-1$; call this $X_{i-1}$. We have to show that $X_{i-1}\cap U\neq\emptyset$. Assume the contrary; then $X_{i-1}$ must be contained in $X_{i}\backslash U$. But by the choice of $f$ we know that $X_{i-1}$ is not a whole component of $X_{i}\backslash U$, so it can only be a proper subset of a component of $X_{i}\backslash U$. But by lemma 4.1.4 (ii) the components of $X_{i}\backslash U$ have dimension at most $i-1$, and therefore proper subsets of them have dimension at most $i-2$. This is a contradiction to $\dim X_{i-1}=i-1$.

Combining steps 1 and 2, we have now proven the proposition if $X$ is a projective variety. Of course the statement then also follows if $X$ is an affine variety: let $\bar{X}$ be the projective closure of $X$ as in exercise 3.5.3, then by applying our result twice we get $\dim U=\dim\bar{X}=\dim X$.

Step 3: Let $X$ be any variety, and let $\emptyset\neq X_{0}\subsetneq\cdots\subsetneq X_{n}=X$ be a longest chain in $X$. Let $V\subset X$ be an affine open neighborhood of the point $X_{0}$; then $\dim V=\dim X$ by step 1. In the same way we can find an affine open subset $W$ of $U$ such that $\dim W=\dim U$. As $V\cap W\neq\emptyset$, it finally follows from steps 1 and 2 that

$\dim X=\dim V=\dim(V\cap W)=\dim W=\dim U.$

∎

In particular, as every variety can be covered by affine varieties, this proposition implies that it is sufficient to study the dimensions of affine varieties. Let us first prove the affine equivalent of proposition 4.1.9.

###### Example 4.2.2.

1. As $\mathbb{A}^{n}$ is an open subset of $\mathbb{P}^{n}$, it follows by corollary 4.1.8 that $\dim\mathbb{A}^{n}=n$.
2.

---

.
2. As $\mathbb{A}^{m+n}$ is an open subset of $\mathbb{P}^{n}\times\mathbb{P}^{m}$, it follows by (i) that $\dim(\mathbb{P}^{n}\times\mathbb{P}^{m})=n+m$.
3. Let $f\in k[x_{1},\ldots,x_{n}]$ be a non-constant polynomial. We claim that $Z(f)\subset\mathbb{A}^{n}$ has dimension $n-1$. In fact, let $\tilde{X}\subset\mathbb{P}^{n}$ be the projective closure of $Z(f)$; by proposition 4.1.9 there is a component $Y$ of $\tilde{X}$ of dimension $n-1$. As the homogenized polynomial $f$ does not contain $x_{0}$ as a factor, $\tilde{X}$ cannot contain the whole “infinity locus” $\mathbb{P}^{n}\backslash\mathbb{A}^{n}\cong\mathbb{P}^{n-1}$. So the part of $\tilde{X}$ in the infinity locus has dimension at most $n-2$; in particular the component $Y$ of $\tilde{X}$ has non-empty intersection with $\mathbb{A}^{n}$. In other words, $Z(f)\subset\mathbb{A}^{n}$ has dimension $n-1$.
4. Let $f\in k[x_{1},\ldots,x_{n}]$ be as in (iii); we claim that in fact the dimension of *every* irreducible component of $Z(f)\subset\mathbb{A}^{n}$ is $n-1$: in fact, as $k[x_{1},\ldots,x_{n}]$ is a unique factorization domain, we can write $f$ as a product $f_{1}\cdots f_{r}$ of irreducible polynomials, so that the decomposition of $Z(f)$ into its irreducible components is $Z(f_{1})\cup\cdots\cup Z(f_{r})$. Now we can apply (iii) to the $f_{i}$ separately to get the desired result.
5. The corresponding statements to (iii) and (iv) are true for the zero locus of a homogeneous polynomial in $\mathbb{P}^{n}$ as well (the proof is the same).

By (iv) and (v), there is a one-to-one correspondence between closed subvarieties of $\mathbb{A}^{n}$ (resp. $\mathbb{P}^{n}$) of dimension $n-1$ and non-constant irreducible polynomials in $k[x_{1},\ldots,x_{n}]$ (resp. non-constant homogeneous polynomials in $k[x_{0},\ldots,x_{n}]$). Varieties that are of this form are called hypersurfaces; if the degree of the polynomial is $1$ they are called hyperplanes.

###### Remark 4.2.3.

Next we want to prove for general affine varieties $X\subset\mathbb{A}^{n}$ that the dimension of (every component of) $X\cap Z(f)$ is $\dim X-1$. Note that this does *not* follow immediately from the projective case as it did for $X=\mathbb{A}^{n}$ in example 4.2.2 (iii) or (iv):

1. As for example 4.2.2 (iii), of course we can still consider the projective closure $\tilde{X}$ of $X$ in $\mathbb{P}^{n}$ and intersect it with the zero locus of the homogenization of $f$; but proposition 4.1.9 only gives us the existence of one component of dimension $\dim X-1$ in $\tilde{X}\cap Z(f)$. It may well be that there is a component of $\tilde{X}\cap Z(f)$ that is contained in the “hyperplane at infinity” $\mathbb{P}^{n}\backslash\mathbb{A}^{n}$, in which case we get no information about the affine zero locus $X\cap Z(f)$. As an example you may consider the projective variety $X=\{x_{0}x_{2}=x_{1}^{2}\}\subset\mathbb{P}^{2}$ and $f=x_{1}$: then $X\cap Z(f)=(1:0:0)\cup(0:0:1)$ contains a point $(0:0:1)$ at infinity as an irreducible component.
2. As for example 4.2.2 (iv), note that a factorization of $f$ as for $\mathbb{A}^{n}$ is simply not possible in general. For example, in the case just considered in (i), $Z(f)$ intersects $X$ in two points, but there is no decomposition of the linear function $f$ into two factors that vanish on only one of the points.

Nevertheless the idea of the proof is still to use projections from points:

###### Proposition 4.2.4.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $f\in k[x_{1},\ldots,x_{n}]$ be a non-constant polynomial that does not vanish identically on $X$. Then $\dim(X\cap Z(f))=\dim X-1$ (unless $X\cap Z(f)=\emptyset$).

###### Proof.

We prove the statement by induction on $n$ (not on $\dim X!$); there is nothing to show for $n=0$. If $X=\mathbb{A}^{n}$ the statement follows from example 4.2.2 (iv), so we can assume that $X\subsetneq\mathbb{A}^{n}$.

Let $\tilde{X}$ be the projective closure in $\mathbb{P}^{n}$; we can assume by an affine change of coordinates that $P=(0:\cdots:0:1)\notin\tilde{X}$. Consider the projection $\tilde{\pi}:\tilde{X}\to\mathbb{P}^{n-1}$ from $P$ as in example 4.1.3. Obviously, we can restrict this projection map to the affine space $\mathbb{A}^{n}\subset\mathbb{P}^{n}$ given by $x_{0}\neq 0$; we thus obtain a morphism $\pi:X\to\pi(X)$ that is given in coordinates by $(a_{1},\ldots,a_{n})\mapsto(a_{1},\ldots,a_{n-1})$. Note that $\pi(X)$ is closed in $\mathbb{A}^{n}$, as $\pi(X)=\tilde{\pi}(\tilde{X})\cap\mathbb{A}^{n}$.

---

By lemma 4.1.5 (i) applied to the function $x_{n}$ we see that there is a relation

$p(x_{n}):=x_{n}^{D}+a_{1}x_{n}^{D-1}+\cdots a_{D}=0\quad\text{in }A(X)$ ($*$)

for some $D>0$ and some $a_{i}\in k[x_{1},\ldots,x_{n-1}]$ that do not depend on $x_{n}$. Let $K$ be the field $k(x_{1},\ldots,x_{n-1})$ of rational functions in $n-1$ variables. Set $V=K[x_{n}]/p(x_{n})$; by $(*)$ this is a $D$-dimensional vector space over $K$ (with basis $1,x_{n},\ldots,x_{n}^{D-1}$). Obviously, every polynomial $g\in k[x_{1},\ldots,x_{n}]$ defines a vector space homomorphism $g:V\to V$ (by polynomial multiplication), so we can talk about its determinant $\det g\in K$. Moreover, it is easy to see that $\det g\in k[x_{1},\ldots,x_{n-1}]$, as the definition of the determinant does not use divisions. Note also that $\det g=g^{D}$ if $g\in k[x_{1},\ldots,x_{n-1}]$.

Now go back to our original problem: describing the zero locus of the given polynomial $f$ on $X$. We claim that

$\pi(X\cap Z(f))=\pi(X)\cap Z((f)\cap k[x_{1},\ldots,x_{n-1}])\supset\pi(X)\cap Z(\det f)$

(in fact there is equality, but we do not need this). The first equality is obvious from the definition of $\pi$. To prove the second inclusion, note that by the Nullstellensatz it suffices to show that $(f)\cap k[x_{1},\ldots,x_{n-1}]\subset\sqrt{(\det f)}$. So let $g\in(f)\cap k[x_{1},\ldots,x_{n-1}]$; in particular $g=f\cdot b$ for some $b\in k[x_{1},\ldots,x_{n}]$. It follows that

$g^{D}=\det g=\det f\cdot\det b\in(\det f),$

i. e. $g\in\sqrt{(\det f)}$, as we have claimed.

The rest is now easy:

$\dim(X\cap Z(f))$ $=\dim\pi(X\cap Z(f))\qquad\text{by
corollary 4.1.7 and proposition 4.2.1}$
$\geq\dim(\pi(X)\cap Z(\det f))\qquad\text{by the inclusion just proven}$
$=\dim\pi(X)-1\qquad\text{by the induction hypothesis}$
$=\dim X-1\qquad\text{by
corollary 4.1.7 and proposition 4.2.1 again.}$

The opposite inequality follows trivially from lemma 4.1.4 (ii). ∎

It is now quite easy to extend this result to a statement about *every* component of $X\cap Z(f)$:

###### Corollary 4.2.5.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $f\in k[x_{1},\ldots,x_{n}]$ be a non-constant polynomial that does not vanish identically on $X$. Then every irreducible component of $X\cap Z(f)$ has dimension $\dim X-1$.

###### Proof.

Let $X\cap Z(f)=Z_{1}\cup\cdots\cup Z_{r}$ be the decomposition into irreducible components; we want to show that $\dim Z_{1}=\dim X-1$. Let $g\in k[x_{1},\ldots,x_{n}]$ be a polynomial that vanishes on $Z_{2},\ldots,Z_{r}$ but not on $Z_{1}$, and let $U=X_{g}=X\backslash Z(g)$. Then $U$ is an affine variety by lemma 2.3.16, and $U\cap Z(f)$ has only one component $Z_{1}\cap U$. So the statement follows from proposition 4.2.4 together with proposition 4.2.1. ∎

###### Remark 4.2.6.

Proposition 4.2.1 and especially corollary 4.2.5 are the main properties of the dimension of varieties. Together they allow to compute the dimension of almost any variety without the need to go back to the cumbersome definition. Here are two examples:

###### Corollary 4.2.7.

Let $f:X\to Y$ be a morphism of varieties, and assume that the dimension of all fibers $n=\dim f^{-1}(P)$ is the same for all $P\in Y$. Then $\dim X=\dim Y+n$.

###### Proof.

We prove the statement by induction on $\dim Y$; there is nothing to show for $n=0$ (i. e. if $Y$ is a point).

---

By proposition 4.2.1 we can assume that $Y\subset\mathbb{A}^{m}$ is an affine variety. Let $f\in k[x_{1},\ldots,x_{m}]$ be any non-zero polynomial in the coordinates of $\mathbb{A}^{m}$ that vanishes somewhere, but not everywhere on $Y$, let $Y^{\prime}\subset Y$ be an irreducible component of $Y\cap Z(f)$, and let $X^{\prime}=f^{-1}(Y^{\prime})$. Then it follows by corollary 4.2.5 and the induction hypothesis that

$\dim X=\dim X^{\prime}+1=\dim Y^{\prime}+n+1=\dim Y+n.$

∎

###### Example 4.2.8.

1. For any varieties $X$, $Y$ we have $\dim(X\times Y)=\dim X+\dim Y$ (apply corollary 4.2.7 to the projection morphism $X\times Y\to X$).
2. Combining corollary 4.2.7 with proposition 4.2.1 again, we see that it is actually sufficient that $f^{-1}(P)$ is non-empty and of the same dimension for all $P$ in a non-empty open subset $U$ of $Y$.

###### Corollary 4.2.9.

Let $X$ and $Y$ be affine varieties in $\mathbb{A}^{n}$. Then every irreducible component of $X\cap Y\subset\mathbb{A}^{n}$ has dimension at least $\dim X+\dim Y-n$.

###### Proof.

Rewrite $X\cap Y$ as the intersection of $X\times Y$ with the diagonal $\Delta(\mathbb{A}^{n})$ in $\mathbb{A}^{n}\times\mathbb{A}^{n}$. The diagonal is given by the zero locus of the $n$ functions $x_{i}-y_{i}$ for $1\leq i\leq n$, where $x_{1},\ldots,x_{n},y_{1},\ldots,y_{n}$ are the coordinates of $\mathbb{A}^{n}\times\mathbb{A}^{n}$. By corollary 4.2.5, every component of the intersection of an affine variety $Z$ with the zero locus of a non-constant function has dimension at least equal to $\dim Z-1$ (it is $\dim Z$ if $f$ vanishes identically on $Z$, and $\dim Z-1$ otherwise). Applying this statement $n$ times to the functions $x_{i}-y_{i}$ on $X\times Y$ in $\mathbb{A}^{n}\times\mathbb{A}^{n}$ we conclude that every component of $X\cap Y$ has dimension at least $\dim(X\times Y)-n=\dim X+\dim Y-n$. ∎

###### Remark 4.2.10.

(For commutative algebra experts) There is another more algebraic way of defining the dimension of varieties that is found in many textbooks: the dimension of a variety $X$ is the transcendence degree over $k$ of the field of rational functions $K(X)$ on $X$. Morally speaking, this definition captures the idea that the dimension of a variety is the number of independent coordinates on $X$. We have not used this definition here as most propositions concerning dimensions would then have required methods of (commutative) algebra that we have not developed yet.

Here are some ideas that can be used to show that this algebraic definition of dimension is equivalent to our geometric one:

- If $U\subset X$ is a non-empty open subset we have $K(U)=K(X)$, so with the algebraic definition of dimension it is actually trivial that $\dim U=\dim X$.
- It is then also obvious that $\dim\mathbb{A}^{n}=\operatorname{tr}\deg k(x_{1},\ldots,x_{n})=n$.
- Let $\pi:X\to\pi(X)$ be a projection map as in the proof of proposition 4.2.4. The relation $(*)$ in the proof can be translated into the fact that $K(X)$ is an algebraic field extension of $K(\pi(X))$ (we add one variable $x_{n}$, but this variable satisfies a polynomial relation). In particular, these two fields have the same transcendence degree, translating into the fact that $\dim\pi(X)=\dim X$.

### 4.3. Blowing up

We have just seen in 4.2.1 that two varieties have the same dimension if they contain an isomorphic (non-empty) open subset. In this section we want to study this relation in greater detail and construct a large and important class of examples of varieties that are not isomorphic but contain an isomorphic open subset. Let us first make some definitions concerning varieties containing isomorphic open subsets. We will probably not use them very much, but they are often found in the literature.

###### Definition 4.3.1.

Let $X$ and $Y$ be varieties. A rational map $f$ from $X$ to $Y$, written $f:X\dashrightarrow Y$, is a morphism $f:U\to Y$ (denoted by the same letter) from a non-empty open

---

subset $U\subset X$ to $Y$. We say that two such rational maps $f:U\to Y$ and $g:V\to Y$ with $U,V\subset X$ are the same if $f=g$ on $U\cap V$.

A rational map $f:X\dashrightarrow Y$ is called dominant if its image is dense in $Y$, i. e. if $f$ is given by a morphism $f:U\to Y$ such that $f(U)$ contains a non-empty open subset of $Y$. If $f:X\dashrightarrow Y$ and $g:Y\dashrightarrow Z$ are rational maps, and if $f$ is dominant, then the composition $g\circ f:X\dashrightarrow Z$ is a well-defined rational map.

A birational map from $X$ to $Y$ is a rational map with an inverse, i. e. it is a (dominant) rational map $f:X\dashrightarrow Y$ such that there is a (dominant) rational map $g:Y\dashrightarrow X$ with $g\circ f=\mathrm{id}_{X}$ and $f\circ g=\mathrm{id}_{Y}$ as rational maps. Two varieties $X$ and $Y$ are called birational if there is a birational map between them. In other words, $X$ and $Y$ are birational if they contain an isomorphic non-empty open subset.

We will now construct the most important examples of birational morphisms (resp. birational varieties), namely blow-ups.

###### Construction 4.3.2.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $f_{0},\ldots,f_{r}\in k[x_{1},\ldots,x_{n}]$ be polynomial functions that do not vanish identically on $X$. Then $U=X\backslash Z(f_{0},\ldots,f_{r})$ is a non-empty open subset of $X$, and there is a well-defined morphism

$f:U\to\mathbb{P}^{r},P\mapsto(f_{0}(P):\cdots:f_{r}(P)).$

Now consider the graph

$\Gamma=\{(P,f(P))\;;\;P\in U\}\subset X\times\mathbb{P}^{r}$

which is isomorphic to $U$ (with inverse morphism $(P,Q)\mapsto P$). Note that $\Gamma$ is in general not closed in $X\times\mathbb{P}^{r}$, because the points in $X\backslash U$ where $(f_{0}:\cdots:f_{r})$ is ill-defined as a point in $\mathbb{P}^{r}$ are “missing”.

The closure of $\Gamma$ in $X\times\mathbb{P}^{r}$ is called the blow-up of $X$ in $(f_{0},\ldots,f_{r})$; we denote it by $\tilde{X}$. It is a closed subset of $X\times\mathbb{P}^{r}$, and it is irreducible as $\Gamma$ is; so it is a closed subvariety of $X\times\mathbb{P}^{r}$. In particular, there are projection morphisms $\pi:\tilde{X}\to X$ and $p:\tilde{X}\to\mathbb{P}^{r}$. Note that $X$ and $\tilde{X}$ both contain $U$ as a dense open subset, so $X$ and the blow-up $\tilde{X}$ have the same dimension.

Let us now investigate the geometric meaning of blow-ups.

###### Example 4.3.3.

If $r=0$ in the above notation, i. e. if there is only one function $f_{0}$, the blow-up $\tilde{X}$ is isomorphic to $X$. In fact, we then have $\tilde{X}\subset X\times\mathbb{P}^{0}\cong X$, so $\tilde{X}$ is the smallest closed subvariety containing $U$.

###### Example 4.3.4.

Let $X=\mathbb{A}^{2}$ with coordinates $x_{0},x_{1}$, and let $f_{0}=x_{0}$, $f_{1}=x_{1}$. Then the blow-up of $X$ in $(f_{0},f_{1})$ is a subvariety of $\mathbb{A}^{2}\times\mathbb{P}^{1}$. The morphism $(x_{0},x_{1})\mapsto(x_{0}:x_{1})$ is well-defined on $U=X\backslash\{(0,0)\}$; so on this open subset the graph is given by

$\Gamma=\{((x_{0},x_{1}),(y_{0}:y_{1}))\;;\;x_{0}y_{1}=x_{1}y_{0}\}\subset U\times\mathbb{P}^{1}.$

The closure of $\Gamma$ is now obviously given by the same equation, considered in $\mathbb{A}^{2}\times\mathbb{P}^{1}$:

$\tilde{X}=\{((x_{0},x_{1}),(y_{0}:y_{1}))\;;\;x_{0}y_{1}=x_{1}y_{0}\}\subset\mathbb{A}^{2}\times\mathbb{P}^{1}.$

The projection morphisms to $X=\mathbb{A}^{2}$ and $\mathbb{P}^{1}$ are obvious.

Note that the inverse image of a point $P=(x_{0},x_{1})\in X\backslash\{(0,0)\}$ under $\pi$ is just the single point $((x_{0},x_{1}),(x_{0}:x_{1}))$ — we knew this before. The inverse image of $(0,0)\in X$ however is $\mathbb{P}^{1}$, as the equation $x_{0}y_{1}=x_{1}y_{0}$ imposes no conditions on $y_{0}$ and $y_{1}$ if $(x_{0},x_{1})=(0,0)$.

To give a geometric interpretation of the points in $\pi^{-1}(0,0)$ let us first introduce one more piece of notation. Let $Y\subset X$ be a closed subvariety that has non-empty intersection with $U$. As $U$ is also a subset of $\tilde{X}$, we can consider the closure of $Y\cap U$ in $\tilde{X}$. We call this the strict transform of $Y$. Note that by definition the strict transform of $Y$ is just the blow-up of $Y$ at $(f_{0},\ldots,f_{r})$; so we denote it by $\tilde{Y}$.

######

---

4. Dimension

Now let  $C \subset X = \mathbb{A}^2$  be a curve, given by the equation

$$
g (x _ {0}, x _ {1}) = \sum_ {i, j} a _ {i, j} x _ {0} ^ {i} x _ {1} ^ {j} = a _ {0, 0} + a _ {1, 0} x _ {0} + a _ {0, 1} x _ {1} + a _ {1, 1} x _ {0} x _ {1} + \dots .
$$

Assume that  $a_{0,0} = 0$ , i.e. that  $C$  passes through the origin in  $\mathbb{A}^2$ , and that  $(a_{1,0}, a_{0,1}) \neq (0,0)$ , so that  $C$  has a well-defined tangent line at the origin, given by the linearization  $a_{1,0}x_0 + a_{0,1}x_1 = 0$  of  $g$ . Let us compute the strict transform  $\tilde{C}$ . Of course, the points  $((x_0, x_1), (y_0 : y_1))$  of  $\tilde{C}$  satisfy the equation

$$
a _ {1, 0} x _ {0} + a _ {0, 1} x _ {1} + a _ {1, 1} x _ {0} x _ {1} + a _ {2, 0} x _ {0} ^ {2} + a _ {0, 2} x _ {1} ^ {2} + \dots = 0. \tag {*}
$$

But it is not true that  $\tilde{C}$  is just the common zero locus in  $\mathbb{A}^2\times \mathbb{P}^1$  of this equation together with  $x_0y_1 = x_1y_0$ , because this common zero locus contains the whole fiber  $\pi^{-1}(0,0)\cong \mathbb{P}^1$  — but  $\tilde{C}$  has to be irreducible of dimension 1, so it cannot contain this  $\mathbb{P}^1$ . In fact, we have forgotten another relation: on the open set where  $x_0\neq 0$  and  $x_{1}\neq 0$  we can multiply  $(*)$  with  $\frac{y_0}{x_0}$ , using the relation  $\frac{y_0}{x_0} = \frac{y_1}{x_1}$  we get

$$
a _ {1, 0} y _ {0} + a _ {0, 1} y _ {1} + a _ {1, 1} y _ {0} x _ {1} + a _ {2, 0} x _ {0} y _ {0} + a _ {0, 2} x _ {1} y _ {1} + \dots = 0.
$$

This equation must then necessarily hold on the closure  $\tilde{C}$  too. Restricting it to the origin  $(x_0, x_1) = (0, 0)$  we get  $a_{1,0}y_0 + a_{0,1}y_1 = 0$ , which is precisely the equation of the tangent line to  $C$  at  $(0, 0)$ . In other words, the strict transform  $\tilde{C}$  of  $C$  intersects the fiber  $\pi^{-1}(0, 0)$  precisely in the point of  $\mathbb{P}^1$  corresponding to the tangent line of  $C$  in  $(0, 0)$ . In this sense we can say that the points of  $\pi^{-1}(0, 0)$  correspond to tangent directions in  $X$  at  $(0, 0)$ .

The following picture illustrates this: we have two curves  $C_1, C_2$  that intersect at the origin with different tangent directions. The strict transforms  $\tilde{C}_1$  and  $\tilde{C}_2$  are then disjoint on the blow-up  $\tilde{X}$ .

![img-1.jpeg](images/img-1.jpeg)

Let us now generalize the results of this example to general blow-ups. Note that in the example we would intuitively say that we have "blown up the origin", i.e. the zero locus of the functions  $f_0, \ldots, f_r$ . In fact, the blow-up construction depends only on the ideal generated by the  $f_i$ :

Lemma 4.3.5. The blow-up of an affine variety  $X$  at  $(f_0, \ldots, f_r)$  depends only on the ideal  $I \subset A(X)$  generated by  $f_0, \ldots, f_r$ . We will therefore usually call it the blow-up of  $X$  at the ideal  $I$ . If  $I = I(Y)$  for a closed subset  $Y \subset X$ , we will also call it the blow-up of  $X$  in  $Y$ .

Proof. Let  $(f_0, \ldots, f_r)$  and  $(f_0', \ldots, f_s')$  be two sets of generators of the same ideal  $I \subset A(X)$ , and let  $\tilde{X}$  and  $\tilde{X}'$  be the blow-ups of  $X$  at these sets of generators. By assumption we have relations in  $A(X)$

$$
f _ {i} = \sum_ {j} g _ {i, j} f _ {j} ^ {\prime} \quad \text {a n d} \quad f _ {j} ^ {\prime} = \sum_ {k} g _ {j, k} ^ {\prime} f _ {k}.
$$

We want to define a morphism  $\tilde{X} \to \tilde{X}'$  by sending  $(P, (y_0 : \dots : y_r))$  to  $(P, (y_0' : \dots : y_r'))$ , where  $y_j' = \sum_k g_{j,k}'(P)y_k$ . First of all we show that this defines a morphism to  $X \times \mathbb{P}^s$ , i.e. that the  $y_j'$  cannot be simultaneously zero. To do this, note that by construction we have the

---

relation $(y_{0}:\cdots:y_{r})=(f_{0}:\cdots:f_{r})$ on $X\backslash Z(I)\subset\bar{X}\subset X\times\mathbb{P}^{r}$, i. e. these two vectors are linearly dependent (and non-zero) at each point in this set. Hence the linear relations $f_{i}=\sum_{j,k}g_{i,j}g^{\prime}_{j,k}f_{k}$ in $f_{0},\ldots,f_{r}$ imply the corresponding relations $y_{i}=\sum_{j,k}g_{i,j}g^{\prime}_{j,k}y_{k}$ in $y_{0},\ldots,y_{r}$ on this set, and thus also on its closure, which is by definition $\bar{X}$. So if we had $y^{\prime}_{j}=\sum_{k}g^{\prime}_{j,k}y_{k}=0$ for all $j$ then we would also have $y_{i}=\sum_{j}g_{i,j}y^{\prime}_{j}=0$ for all $i$, which is a contradiction.

Hence we have defined a morphism $\bar{X}\to X\times\mathbb{P}^{s}$. By construction it maps the open subset $X\backslash Z(f_{0},\ldots,f_{r})\subset\bar{X}$ to $X\backslash Z(f^{\prime}_{0},\ldots,f^{\prime}_{s})\subset\bar{X}^{\prime}$, so it must map its closure $\bar{X}$ to $\bar{X}^{\prime}$ as well. By the same arguments we get an inverse morphism $\bar{X}^{\prime}\to\bar{X}$, so $\bar{X}$ and $\bar{X}^{\prime}$ are isomorphic. ∎

Let us now study the variety $\bar{X}$ itself, in particular over the locus $Z(f_{0},\ldots,f_{r})$ where $\pi:\bar{X}\to X$ is not an isomorphism.

###### Lemma 4.3.6.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $\bar{X}$ be the blow-up of $X$ at the ideal $I=(f_{0},\ldots,f_{r}).$ Then:

1. The blow-up $\bar{X}$ is contained in the set

$\{(P,(y_{0}:\cdots:y_{r}))\ ;\ y_{i}f_{j}(P)=y_{j}f_{i}(P)\text{ for all }i,j=0,\ldots,r\}\subset X\times\mathbb{P}^{r}.$
2. The inverse image $\pi^{-1}(Z(f_{0},\ldots,f_{r}))$ is of pure dimension $\dim X-1$. It is called the exceptional hypersurface.

###### Proof.

(i): By definition we must have $(y_{0}:\cdots:y_{r})=(f_{0}(P):\cdots:f_{r}(P))$ on the non-empty open subset $X\backslash Z(I)\subset\bar{X}$. So these equations must be true as well on the closure of this open subset, which is $\bar{X}$ by definition.

(ii): It is enough to prove the statement on the open subset where $y_{i}\neq 0$, as these open subsets for all $i$ cover $\bar{X}$. Note that on this open subset the condition $f_{i}(P)=0$ implies $f_{j}(P)=0$ for all $j$ by the equations of (i). So the inverse image $\pi^{-1}(Z(f_{0},\ldots,f_{r}))$ is given by one equation $f_{j}=0$, and is therefore of pure dimension $\dim\bar{X}-1=\dim X-1$ by corollary 4.2.5. ∎

###### Example 4.3.7.

In example 4.3.4, $X=\mathbb{A}^{2}$ has dimension $2$, and the exceptional hypersurface was isomorphic to $\mathbb{P}^{1}$, which has dimension $1$.

###### Remark 4.3.8.

The equations in lemma 4.3.6 (i) are in general not the only ones for $\bar{X}$. Note that they do not impose any conditions over the zero locus $Z(f_{0},\ldots,f_{r})$ at all, so that it would seem from these equations that the exceptional hypersurface is always $\mathbb{P}^{r}$. This must of course be false in general just for dimensional reasons (see lemma 4.3.6 (ii)).

In fact, we can write down explicitly the equations for the exceptional hypersurface. We will do this here only in the case of the blow-up of (the ideal of) a point $P$, which is the most important case. By change of coordinates, we can then assume that $P$ is the origin in $\mathbb{A}^{n}$.

For any $f\in k[x_{1},\ldots,x_{n}]$ we let $f^{in}$ be the “initial polynomial” of $f$, i. e. if $f=\sum_{i}f^{(i)}$ is the splitting of $f$ such that $f^{(i)}$ is homogeneous of degree $i$, then $f^{in}$ is by definition equal to the smallest non-zero $f^{(i)}$. If $I\subset k[x_{1},\ldots,x_{n}]$, we let $I^{in}$ be the ideal generated by the initial polynomials $f^{in}$ for all $f\in I$. Note that $I^{in}$ is by definition a homogeneous ideal. So its affine zero locus $Z_{a}(I^{in})\subset\mathbb{A}^{n}$ is a cone, and there is also a well-defined projective zero locus $Z_{p}(I^{in})$. By exercise 4.6.8, the exceptional hypersurface of the blowup of an affine variety $X\subset\mathbb{A}^{n}$ in the origin is precisely $Z_{p}(I(X)^{in})$. (The proof of this statement is very similar to the computation of $\bar{C}$ in example 4.3.4.)

Let us figure out how this can be interpreted geometrically. By construction, $I(X)^{in}$ is obtained from $I(X)$ by only keeping the terms of lowest degree, so it can be interpreted as an “approximation” of $I(X)$ around zero, just in the same way as the Taylor polynomial

---

4. Dimension

approximates a function around a given point. Note also that  $Z_{a}(I(X)^{in})$  has the same dimension as  $X$  by lemma 4.3.6 (ii). Hence we can regard  $Z_{a}(I(X)^{in}) \subset \mathbb{A}^{n}$  as the cone that approximates  $X$  best around the point  $P$ . It is called the tangent cone of  $X$  in  $P$  and denoted  $C_{X,P}$ . The exceptional locus of the blow-up  $\tilde{X}$  of  $X$  in  $P$  is then the "projectivized tangent cone", i.e. it corresponds to "tangent directions" in  $X$  through  $P$ , just as in example 4.3.4.

Example 4.3.9. Here are some examples of tangent cones.

(i) Let  $X = \{(x,y); y = x(x - 1)\} \subset \mathbb{A}^2$ . The tangent cone of  $X$  in  $P = (0,0)$  is given by keeping only the linear terms of the equation  $y = x(x - 1)$ , i.e.  $C_{X,P} = \{(x,y); y = -x\}$  is the tangent line to  $X$  in  $P$ . Consequently, the exceptional hypersurface of the blow-up of  $X$  in  $P$  contains only one point. In fact,  $\tilde{X}$  is isomorphic to  $X$  in this case: note that on  $X$ , the ideal of  $P$  is just given by the single function  $x$ , as  $(y - x(x - 1),x) = (x,y)$ . So we are blowing up at  $f_0 = x$  only. It follows then by example 4.3.3 that  $\tilde{X} = X$ .
(ii) Let  $X = \{(x,y); y^2 = x^2 + x^3\} \subset \mathbb{A}^2$ . This time there are no linear terms in the equation of  $X$ , so the tangent cone in  $P = (0,0)$  is given by the quadratic terms  $C_{X,P} = \{(x,y); y^2 = x^2\}$ , i.e. it is the union of the two tangent lines  $y = x$  and  $y = -x$  to  $X$  in  $P$  (see the picture below). The exceptional hypersurface of the blow-up of  $X$  in  $P$  therefore contains exactly two points, one for every tangent direction in  $P$ . In other words, the two local branches of  $X$  around  $P$  get separated in the blow-up. Note that we cannot apply the argument of (i) here that  $\tilde{X}$  should be isomorphic to  $X$ : the ideal of  $P$  cannot be generated on  $X$  by one function only. While it is true that the zero locus of  $(x,y^2 - x^2 - x^3)$  is  $P$ , the ideal  $(x,y^2 - x^2 - x^3) = (x,y^2)$  is not equal to  $I(P) = (x,y)$  — and this is the important point. In particular, we see that the blow-up of  $X$  in an ideal  $I$  really does depend on the ideal  $I$  and not just on its zero locus, i.e. on the radical of  $I$ .
(iii) Let  $X = \{(x,y); y^2 = x^3\} \subset \mathbb{A}^2$ . This time the tangent cone is  $C_{X,P} = \{y^2 = 0\}$ , i.e. it is only one line. So for  $\tilde{X}$  the point  $P \in X$  is replaced by only one single point again, as in (i). But in this case  $X$  and  $\tilde{X}$  are not isomorphic, as we will see in 4.4.7.

![img-2.jpeg](images/img-2.jpeg)

![img-3.jpeg](images/img-3.jpeg)

![img-4.jpeg](images/img-4.jpeg)

Remark 4.3.10. Let  $X$  be any variety, and let  $Y \subset X$  be a closed subset. For an affine open cover  $\{U_i\}$  of  $X$ , let  $\tilde{U}_i$  be the blow-up of  $U_i$  in  $U_i \cap Y$ . It is then easy to see that the  $\tilde{U}_i$  can be glued together to give a blow-up variety  $\tilde{X}$ .

In what follows, we will only need this in the case of the blow-up of a point, where the construction is even easier as it is local around the blown-up point: let  $X$  be a variety, and let  $P \in X$  be a point. Choose an affine open neighborhood  $U \subset X$  of  $P$ , and let  $\tilde{U}$  be the blow-up of  $U$  in  $P$ . Then we obtain  $\tilde{X}$  by glueing  $X \backslash P$  to  $\tilde{U}$  along the common open subset  $U \backslash P$ . In particular, this defines the tangent cone  $C_{X,P}$  to  $X$  at  $P$  for any variety  $X$ : it is the affine cone over the exceptional hypersurface of the blow-up of  $X$  in  $P$ .

This sort of glueing currently works only for blow-ups at subvarieties, i.e. for blow-ups at radical ideals. For the general construction we would need to patch ideals, which we do not know how to do at the moment.

---

Note however that it is easy to see that for projective varieties, the blow-up at a homogeneous ideal can be defined in essentially the same way as for affine varieties: let $X\subset\mathbb{P}^{n}$ be a projective variety, and let $Y\subset X$ be a closed subset. If $f_{0},\ldots,f_{r}$ are homogeneous generators of $I(Y)$ of the same degree, the blow-up of $X$ in $Y$ is precisely the closure of

$\Gamma=\{(P,(f_{0}(P):\cdots:f_{r}(P))\;;\;P\in U\}\subset X\times\mathbb{P}^{r}$

in $X\times\mathbb{P}^{r}$ (this is easily checked on the affine patches $f_{i}\neq 0$).

###### Example 4.3.11.

The following property of blow-ups follows trivially from the definitions, yet it is one of their most important properties.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $f_{0},\ldots,f_{r}$ be polynomials that do not vanish identically on $X$. Note that the morphism $f:P\mapsto(f_{0}(P):\cdots:f_{r}(P))$ to $\mathbb{P}^{r}$ is only well-defined on the open subset $U=X\backslash Z(f_{0},\ldots,f_{r})$ of $X$. In general, we can not expect that this morphism can be extended to a morphism on all of $X$. But we can always extend it “after blowing up the ideal $(f_{0},\ldots,f_{r})$ of the indeterminacy locus”, i. e. there is an extension $\tilde{f}:\tilde{X}\to\mathbb{P}^{r}$ (that agrees with $f$ on the open subset $U$), namely just the projection from $\tilde{X}\subset X\times\mathbb{P}^{r}\to\mathbb{P}^{r}$. So blowing up is a way to extend morphisms to bigger sets on which they would otherwise be ill-defined. The same is true for projective varieties and the construction at the end of remark 4.3.10. Let us consider a concrete example of this idea in the next lemma and the following remark:

###### Lemma 4.3.12.

$\mathbb{P}^{1}\times\mathbb{P}^{1}$ blown up in one point is isomorphic to $\mathbb{P}^{2}$ blown up in two points.

###### Proof.

We know from example 3.3.14 that $\mathbb{P}^{1}\times\mathbb{P}^{1}$ is isomorphic to the quadric surface

$Q=\{(x_{0}:x_{1}:x_{2}:x_{3})\;;\;x_{0}x_{3}=x_{1}x_{2}\}\subset\mathbb{P}^{3}.$

Let $P=(0:0:0:1)\in Q$, and let $\tilde{Q}\subset\mathbb{P}^{3}\times\mathbb{P}^{2}$ be the blow-up of $Q$ in the ideal $I(P)=(x_{0},x_{1},x_{2})$.

On the other hand, let $R_{1}=(0:1:0),R_{2}=(0:0:1)\in\mathbb{P}^{2}$, and let $\tilde{\mathbb{P}}^{2}\subset\mathbb{P}^{2}\times\mathbb{P}^{3}$ be the blow-up of $\mathbb{P}^{2}$ in the ideal $I=(y_{0}^{2},y_{0}y_{1},y_{0}y_{2},y_{1}y_{2})$. Note that this is not quite the ideal $I(R_{1}\cup R_{2})=(y_{0},y_{1}y_{2})$, but this does not matter: the blow-up is a local construction, so let us check that we are doing the right thing around $R_{1}$. There is an open affine neighborhood around $R_{1}$ given by $y_{1}\neq 0$, and on this neighborhood the ideal $I$ is just $(y_{0}^{2},y_{0},y_{0}y_{2},y_{2})=(y_{0},y_{2})$, which is precisely the ideal of $R_{1}$. The same is true for $R_{2}$, so the blow-up of $\mathbb{P}^{2}$ in $I$ is actually the blow-up of $\mathbb{P}^{2}$ in the two points $R_{1}$ and $R_{2}$.

Now we claim that an isomorphism is given by

$f:\tilde{Q}\mapsto\tilde{\mathbb{P}}^{2},\;((x_{0}:x_{1}:x_{2}:x_{3}),(y_{0}:y_{1}:y_{2}))\mapsto((y_{0}:y_{1}:y_{2}),(x_{0}:x_{1}:x_{2}:x_{3})).$

In fact, this is easy to check: obviously, $f$ is an isomorphism $\mathbb{P}^{2}\times\mathbb{P}^{3}\to\mathbb{P}^{3}\times\mathbb{P}^{2}$, so we only have to check that $f$ maps $\tilde{Q}$ to $\tilde{\mathbb{P}}^{2}$, and that $f^{-1}$ maps $\tilde{\mathbb{P}}^{2}$ to $\tilde{Q}$. Note that it suffices to check this away from the blown-up points: $f^{-1}(\tilde{\mathbb{P}}^{2})$ is a closed subset of $\mathbb{P}^{3}\times\mathbb{P}^{2}$, so if it contains a non-empty open subset $U\subset Q$ (e. g. $\tilde{Q}$ minus the exceptional hypersurface), it must contain all of $Q$.

But this is now easy to check: on $\tilde{Q}$ we have $x_{0}x_{3}=x_{1}x_{2}$ and $(y_{0}:y_{1}:y_{2})=(x_{0}:x_{1}:x_{2})$ (where this is well-defined), so in the image of $f$ we get the correct equations

$(x_{0}:x_{1}:x_{2}:x_{3})=(x_{0}^{2}:x_{0}x_{1}:x_{0}x_{2}:x_{0}x_{3})=(x_{0}^{2}:x_{0}x_{1}:x_{0}x_{2}:x_{1}x_{2})=(y_{0}^{2}:y_{0}y_{1}:y_{0}y_{2}:y_{1}y_{2})$

for the image point to lie in $\tilde{\mathbb{P}}^{2}$. Conversely, on $\tilde{\mathbb{P}}^{2}$ we have $(x_{0}:x_{1}:x_{2}:x_{3})=(y_{0}^{2}:y_{0}y_{1}:y_{0}y_{2}:y_{1}y_{2})$ where defined, so we conclude $x_{0}x_{3}=x_{1}x_{2}$ and $(y_{0}:y_{1}:y_{2})=(x_{0}:x_{1}:x_{2})$. ∎

###### Remark 4.3.13.

The proof of lemma 4.3.12 is short and elegant, but not very insightful. Let us try to understand geometrically what is going on.

As in the proof, we think of $\mathbb{P}^{1}\times\mathbb{P}^{1}$ as the quadric

$Q=\{(x_{0}:x_{1}:x_{2}:x_{3})\;;\;x_{0}x_{3}=x_{1}x_{2}\}\subset\mathbb{P}^{3}.$

---

4. Dimension

Consider the projection  $\pi$  from  $P$  to  $\mathbb{P}^2$ , given in coordinates by  $\pi(x_0 : x_1 : x_2 : x_3) = (x_0 : x_1 : x_2)$ . We have considered projections from points before, but so far the projection point  $P$  was always assumed not to lie on the given variety  $Q$ . This is not the case here, and consequently  $\pi$  is only well-defined on  $Q \setminus P$ . To construct  $\pi(P)$  we would have to take "the line through  $P$  and  $P$ " and intersect it with a given  $\mathbb{P}^2 \subset \mathbb{P}^3$  that does not contain  $P$ . Of course this is ill-defined. But there is a well-defined line through  $P$  and any point  $P'$  near  $P$  which we can intersect with  $\mathbb{P}^2$ . It is obvious that  $\pi(P)$  should be the limit of these projection points when  $P'$  tends to  $P$ . The line  $\overleftrightarrow{P'P}$  will then become a tangent line to  $Q$ . But  $Q$ , being two-dimensional, has a one-parameter family of tangent lines. This is why  $\pi(P)$  is ill-defined. But we also see from this discussion that blowing up  $P$  on  $Q$ , i.e. replacing it by the set of tangent lines through  $P$ , will exactly resolve the indeterminacy.

We have thus constructed a morphism  $\widetilde{Q} = \overleftrightarrow{\mathbb{P}^1\times\mathbb{P}^1}\to \mathbb{P}^2$  by projection from  $P$ . If there is an inverse morphism, it is easy to see what it would have to look like: pick a point  $R\in \mathbb{P}^2\subset \mathbb{P}^3$ . The points mapped to  $R$  by  $\pi$  are exactly those on the line  $\overline{PR}$  not equal to  $P$ . In general, this line intersects the quadric  $Q$  in two points, one of which is  $P$ . So there is exactly one point on  $Q$  which maps to  $R$ . This reasoning is false however if the whole line  $\overline{PR} = \mathbb{P}^1$  lies in  $Q$ . This whole line would then be mapped to  $R$ , so that we cannot have an isomorphism. But of course we expect again that this problem can be taken care of by blowing up  $R$  in  $\mathbb{P}^2$ , so that it is replaced by a  $\mathbb{P}^1$  that can then be mapped one-to-one to  $\overline{PR}$ .

There are obviously two such lines  $\overline{PR_1}$  and  $\overline{PR_2}$ , given by  $R_{1} = (0:1:0)$  and  $R_{2} = (0:0:1)$ . If you think of  $Q$  as  $\mathbb{P}^1\times \mathbb{P}^1$  again, these lines are precisely the "horizontal" and "vertical" lines  $\mathbb{P}^1\times \{\mathrm{point}\}$  and  $\{\mathrm{point}\} \times \mathbb{P}^1$  passing through  $P$ . So we would expect that  $\tilde{\pi}$  can be made into an isomorphism after blowing up  $R_{1}$  and  $R_{2}$ , which is what we have shown in lemma 4.3.12.

![img-5.jpeg](images/img-5.jpeg)

4.4. Smooth varieties. Let  $X \subset \mathbb{A}^n$  be an affine variety, and let  $P \in X$  be a point. By a change of coordinates let us assume that  $P = (0, \ldots, 0)$  is the origin. In remark 4.3.8 we have defined the tangent cone of  $X$  in  $P$  to be the closed subset of  $\mathbb{A}^n$  given by the initial ideal of  $X$ , i.e. the "local approximation" of  $X$  around  $P$  given by keeping only the terms of the defining equations of  $X$  of minimal degree. Let us now make a similar definition, but where we only keep the linear terms of the defining equations.

Definition 4.4.1. For any polynomial  $f \in k[x_1, \ldots, x_n]$  denote by  $f^{(1)}$  the linear part of  $f$ . For an ideal  $I \subset k[x_1, \ldots, x_n]$  denote by  $I^{(1)} = \{f^{(1)}; f \in I\}$  the vector space of all linear parts of the elements of  $I$ ; this is by definition a vector subspace of the  $n$ -dimensional space  $k[x_1, \ldots, x_n]^{(1)}$  of all linear forms

$$
\left\{a _ {1} x _ {1} + \dots + a _ {n} x _ {n}; a _ {i} \in k \right\}.
$$

---

The zero locus $Z(I^{(1)})$ is then a linear subspace of $\mathbb{A}^{n}$. It is canonically dual (as a vector space) to $k[x_{1},\ldots,x_{n}]^{(1)}/I^{(1)}$, since the pairing

$k[x_{1},\ldots,x_{n}]^{(1)}/I^{(1)}\times Z(I^{(1)})\to k,\qquad(f,P)\mapsto f(P)$

is obviously non-degenerate.

Now let $X\subset\mathbb{A}^{n}$ be a variety. By a linear change of coordinates, assume that $P=(0,\ldots,0)\in X$. Then the linear space $Z(I(X)^{(1)})$ is called the tangent space to $X$ at $P$ and denoted $T_{X,P}$.

###### Remark 4.4.2.

Let us make explicit the linear change of coordinates mentioned in the definition. If $P=(a_{1},\ldots,a_{n})\in X$, we need to change coordinates from the $x_{i}$ to $y_{i}=x_{i}-a_{i}$. By a (purely formal) Taylor expansion we can rewrite any polynomial $f\in k[x_{1},\ldots,x_{n}]$ as

$f(x_{1},\ldots,x_{n})=f(P)+\sum_{i}\frac{\partial f}{\partial x_{i}}(P)\cdot y_{i}+\text{(terms at least quadratic in the $y_{i}$)},$

so we see that the tangent space $T_{X,P}$ to any point $P=(a_{1},\ldots,a_{n})\in X$ is given by the equations

$\sum_{i}\frac{\partial f}{\partial x_{i}}(P)\cdot(x_{i}-a_{i})=0$

for all $f\in I(X)$.

Here is an alternative description of the tangent space. For simplicity, we will assume again that the coordinates have been chosen such that $P=(0,\ldots,0)$.

###### Lemma 4.4.3.

Let $X\subset\mathbb{A}^{n}$ be a variety, and assume that $P=(0,\ldots,0)\in X$. Then

$k[x_{1},\ldots,x_{n}]^{(1)}/I(X)^{(1)}=M/M^{2},$

where $M=\{\varphi\ ;\ \varphi(P)=0\}\subset\mathcal{O}_{X,P}$ is the maximal ideal in the local ring of $X$ at $P$.

###### Proof.

Recall that

$\mathcal{O}_{X,P}=\Big{\{}\frac{f}{g}\ ;\ f,g\in A(X),g(P)\neq 0\Big{\}},$

and therefore

$M=\Big{\{}\frac{f}{g}\ ;\ f,g\in A(X),f(P)=0,g(P)\neq 0\Big{\}}.$

There is an obvious homomorphism $k[x_{1},\ldots,x_{n}]^{(1)}/I(X)^{(1)}\to M/M^{2}$ of $k$-vector spaces. We will show that it is bijective.

Injectivity: Let $f\in k[x_{1},\ldots,x_{n}]^{(1)}$ be a linear function. Then $\frac{f}{1}$ is zero in $\mathcal{O}_{X,P}$ if and only if it is zero in $A(X)$, i. e. if and only if $f\in I(X)$.

Surjectivity: Let $\varphi=\frac{f}{g}\in M$. Without loss of generality we can assume that $g(P)=1$. Set

$\varphi^{\prime}=\sum_{i}\frac{\partial\varphi}{\partial x_{i}}(P)\cdot x_{i},$

---

which is obviously an element of $k[x_{1},\ldots,x_{n}]^{(1)}$. We claim that $\varphi-\varphi^{\prime}\in M^{2}$. In fact,

$g(\varphi-\varphi^{\prime})$ $=f-g\sum_{i}\frac{\frac{\partial f}{\partial x_{i}}(P)g(P)-\frac{\partial g}{\partial x_{i}}(P)f(P)}{g(P)^{2}}\ x_{i}$
$=f-g\sum_{i}\frac{\partial f}{\partial x_{i}}(P)\ x_{i}$
$\equiv f-g(P)\sum_{i}\frac{\partial f}{\partial x_{i}}(P)\ x_{i}\qquad\pmod{M^{2}}\qquad\text{(as $g-g(P)$ and $x_{i}$ are in $M$)}$
$=f-\sum_{i}\frac{\partial f}{\partial x_{i}}(P)\ x_{i}$
$\equiv 0\qquad\pmod{M^{2}}\qquad\text{(as this is the linear Taylor expression for $f$)}.$

So $\varphi=\varphi^{\prime}$ in $M/M^{2}$. ∎

###### Remark 4.4.4.

In particular, this lemma gives us a more intrinsic definition of the tangent space $T_{X,P}$: we can say that $T_{X,P}$ is the dual of the $k$-vector space $M/M^{2}$, where $M$ is the maximal ideal in the local ring $\mathcal{O}_{X,P}$. This alternative definition shows that the tangent space $T_{X,P}$ (as an abstract vector space) is independent of the chosen embedding of $X$ in affine space. It also allows us to define the tangent space $T_{X,P}$ for any variety $X$ (that is not necessarily affine).

Let us now compare tangent spaces to tangent cones.

###### Remark 4.4.5.

Let $X$ be an affine variety, and assume for simplicity that $P=(0,\ldots,0)\in X$. For all polynomials $f\in k[x_{1},\ldots,x_{n}]$ vanishing at $P$, linear terms are always initial. Hence the ideal generated by $I(X)^{(1)}$ is contained in the ideal $I(X)^{in}$ defining the tangent cone (see remark 4.3.8). So the tangent cone $C_{X,P}\subset\mathbb{A}^{n}$ is contained in the tangent space $T_{X,P}\subset\mathbb{A}^{n}$. In particular, we always have $\dim T_{X,P}\geq\dim C_{X,P}=\dim X$. Summarizing, we can say that, in studying the local properties of $X$ around $P$, the tangent cone has the advantage that it always has the “correct” dimension $\dim X$, whereas the tangent space has the advantage that it is always a linear space. We should give special attention to those cases when both notions agree, i. e. when $X$ “can be approximated linearly” around $P$.

###### Definition 4.4.6.

A variety $X$ is called smooth at the point $P\in X$ if $T_{X,P}=C_{X,P}$, or equivalently, if the tangent space $T_{X,P}$ to $X$ at $P$ has dimension (at most) $\dim X$. It is called singular at $P$ otherwise. We say that $X$ is smooth if it is smooth at all points $P\in X$; otherwise $X$ is singular.

###### Example 4.4.7.

Consider again the curves of example 4.3.9:

1. $X=\{y=x(x-1)\}\subset\mathbb{A}^{2}$,
2. $X=\{y^{2}=x^{2}+x^{3}\}\subset\mathbb{A}^{2}$,
3. $X=\{y^{2}=x^{3}\}\subset\mathbb{A}^{2}$.

In case (i), the tangent space is $\{y=-x\}\subset\mathbb{A}^{2}$ and coincides with the tangent cone: $X$ is smooth at $P=(0,0)$. In the cases (ii) and (iii), there are no linear terms in the defining equations of $X$. So the tangent space of $X$ at $P$ is all of $\mathbb{A}^{2}$, whereas the tangent cone is one-dimensional. Hence in these cases $X$ is singular at $P$.

In case (iii) let us now consider the blow-up of $X$ in $P=(0,0)$. Let us first blow up the ambient space $\mathbb{A}^{2}$ in $P$; we know already that this is given by

$\tilde{\mathbb{A}}^{2}=\{((x,y),(x^{\prime}:y^{\prime}))\hskip 2.84544pt;\hskip 2.84544pty^{\prime}=x^{\prime}y\}\subset\mathbb{A}^{2}\times\mathbb{P}^{1}.$

So local affine coordinates of $\tilde{\mathbb{A}}^{2}$ around the point $((0,0),(1:0))$ are $(u,v)\in\mathbb{A}^{2}$, where

$u=\frac{y^{\prime}}{x^{\prime}}\quad\text{and}\quad v=x$

---

Andreas Gathmann

so that  $((x,y),(x':y')) = ((\nu ,uv),(1:u))$ . In these local coordinates, the equation  $y^{2} = x^{3}$  of the curve  $X$  is given by  $(uv)^{2} = \nu^{3}$ . The exceptional hypersurface has the local equation  $\nu = 0$ , so away from this hypersurface the curve  $X$  is given by the equation  $\nu = u^{2}$ . By definition, this is then also the equation of the blow-up  $\tilde{X}$ .

So we conclude first of all that the blow-up  $\tilde{X}$  is smooth, although  $X$  was not. We say that the singularity  $P \in X$  got "resolved" by blowing up. We can also see that the blow-up of the curve (with local equation  $\nu = u^2$ ) is tangent to the exceptional hypersurface (with local equation  $\nu = 0$ ). All this is illustrated in the following picture (the blow-up of  $\mathbb{A}^2$  is the same as in example 4.3.4):

![img-6.jpeg](images/img-6.jpeg)

It can in fact be shown that every singularity can be "resolved" in a similar way by successively blowing up the singular locus.

The good thing about smoothness is that is very easy to check:

# Proposition 4.4.8.

(i) (Affine Jacobi criterion) Let  $X \subset \mathbb{A}^n$  be an affine variety with ideal  $I(X) = (f_1, \ldots, f_r)$ , and let  $P \in X$  be a point on  $X$ . Then  $X$  is smooth at  $P$  if and only if the rank of the  $r \times n$  "Jacobi matrix"  $\left( \frac{\partial f_i}{\partial x_j}(P) \right)$  is (at least)  $n - \dim X$ .
(ii) (Projective Jacobi criterion) Let  $X \subset \mathbb{P}^n$  be a projective variety with ideal  $I(X) = (f_1, \ldots, f_r)$ , and let  $P \in X$  be a point on  $X$ . Then  $X$  is smooth at  $P$  if and only if the rank of the  $r \times n$  Jacobi matrix  $\left( \frac{\partial f_i}{\partial x_j}(P) \right)$  is (at least)  $n - \dim X$ .

In particular, if the rank is  $r$  (the number of functions) then  $X$  is smooth of dimension  $n - r$ .

Proof. (i): By remark 4.4.2, the linearization of the functions  $f_{i}$  around the point  $P = (a_{1},\ldots ,a_{n})$  is given by  $\sum_{j}\frac{\partial f_{i}}{\partial x_{j}}(P)\cdot (x_{i} - a_{i})$ . By definition,  $X$  is smooth at  $P$  if these functions define a linear subspace of  $\mathbb{A}^n$  of dimension (at most)  $\dim X$ , i.e. if and only if the linear subspace of  $k[x_1,\dots,x_n]^{(1)}$  spanned by the above linearizations has dimension (at least)  $n - \dim X$ . But the dimension of this linear space is exactly the rank of the matrix whose entries are the coefficients of the various linear function.

(ii): This follows easily by covering the projective space  $\mathbb{P}^n$  by the  $n + 1$  affine spaces  $\{x_i \neq 0\} \cong \mathbb{A}^n$ , and applying the criterion of (i) to these  $n + 1$  patches.

Remark 4.4.9. Note that a matrix has rank less than  $k$  if and only if all  $k \times k$  minors are zero. These minors are all polynomials in the entries of the matrix. In particular, the locus of singular points, i.e. where the Jacobi matrix has rank less than  $n - \dim X$  as in the proposition, is closed.

It follows that the set

\{P\in X;X
 is singular at
P\} \subset X

---

is closed. In other words, the set of smooth points of a variety is always open. One can show that the set of smooth points is also non-empty for every variety (see e. g. *[x10]* theorem I.5.3). Hence the set of smooth points is always dense.

###### Example 4.4.10.

1. For given $n$ and $d$, let $X$ be the so-called *Fermat hypersurface*

$X=\{(x_{0}:\cdots:x_{n})~{};~{}x_{0}^{d}+\cdots+x_{n}^{d}=0\}.$

Then the Jacobi matrix has only one row, and the entries of this row are $d~{}x_{i}^{d-1}$ for $i=0,\ldots,n$. Assuming that the characteristic of the ground field is zero (or at least not a divisor of $d$), it follows that at least one of the entries of this matrix is non-zero at every point. In other words, the rank of the Jacobi matrix is always 1. Therefore $X$ is smooth by proposition 4.4.8.
2. Let $X$ be the “twisted cubic curve” of exercise 3.5.2

$X=\{(s^{3}:s^{2}t:st^{2}:t^{3})~{};~{}(s:t)\in\mathbb{P}^{1}\}.$

We have seen earlier that $X$ can be given by the equations

$X=\{(x_{0}:x_{1}:x_{2}:x_{3})~{};~{}x_{1}^{2}-x_{0}x_{2}=x_{2}^{2}-x_{1}x_{3}=x_{0}x_{3}-x_{1}x_{2}=0\}.$

So the Jacobi matrix is given by

\[ \left(\begin{array}[]{cccc}-x_{2}&2x_{1}&-x_{0}&0\\
0&-x_{3}&2x_{2}&-x_{1}\\
x_{3}&-x_{2}&-x_{1}&x_{0}\end{array}\right). \]

By proposition 4.4.8, $X$ is smooth if and only if the rank of this matrix is 2. (We know already that the rank cannot be bigger than 2, which is also easily checked directly).

The $2\times 2$ minor given by the last two rows and the first two columns is $x_{3}^{2}$. The $2\times 2$ minor given by last two rows and the first and last column is $x_{1}x_{3}=x_{2}^{2}$. Similarly we find $2\times 2$ minors that are $x_{1}^{2}$ and $x_{0}^{2}$. These cannot all be simultaneously zero; hence $X$ is smooth. (Of course we have known this before, since $X$ is just the degree-3 Veronese embedding of $\mathbb{P}^{1}$ (see example 3.4.11. In particular, $X$ is isomorphic to $\mathbb{P}^{1}$ and therefore smooth.)

###### Remark 4.4.11.

The Jacobi criterion of proposition 4.4.8 gives us a direct connection to complex analysis. Assume that we are given $r$ holomorphic functions on $\mathbb{C}^{n}$ (e. g. polynomials), and that the matrix of the derivatives of the $f_{i}$ has rank $n-\dim X$ at a point $P$, where $X$ is the zero locus of the $f_{i}$. Assume for simplicity that the square matrix $\left(\frac{\partial f_{i}}{\partial x_{j}}(P)\right)_{1\leq i\leq n-\dim X,\dim X<j\leq n}$ of size $n-\dim X$ is invertible. Then the inverse function theorem states that the coordinates $x_{\dim X+1},\ldots,x_{n}$ are locally around $P$ determined by the other coordinates $x_{1},\ldots,x_{\dim X}$. Thus there is a neighborhood $U$ of $P$ in $\mathbb{C}^{n}$ (in the classical topology!) and holomorphic functions $g_{\dim X+1},\ldots,g_{n}$ of $x_{1},\ldots,x_{\dim X}$ such that for every $P=(x_{1},\ldots,x_{\dim X})\in U$ the functions $f_{i}$ vanish at $P$ if and only if $x_{i}=g_{i}(x_{1},\ldots,x_{\dim X})$ for $i=\dim X+1,\ldots,n$.

So the zero locus of the $f_{i}$ is “locally the graph of a holomorphic map” given by the $g_{i}$. In other words, smoothness in algebraic geometry means in a sense the same thing as differentiability in analysis: the geometric object has “no edges”.

Note however that the inverse function theorem is not true in the Zariski topology, because the open sets are too big. For example, consider the curve $X=\{(x,y)~{};~{}f(x,y)=y-x^{2}=0\}\subset\mathbb{C}^{2}$. Then $\frac{\partial f}{\partial x}\neq 0$ say at the point $P=(1,1)\in X$. Consequently, in complex analysis $x$ can be expressed locally in terms of $y$ around $P$: it is just the square root of $y$. But any non-empty Zariski open subset of $X$ will contain pairs of points $(x,x^{2})$ and $(-x,x^{2})$ for some $x$, so the inverse function theorem cannot hold here in algebraic geometry.

---

### 4.5. The 27 lines on a smooth cubic surface

As an application of the theory that we have developed so far, we now want to study lines on cubic surfaces in $\mathbb{P}^{3}$. We have already mentioned in example 0.1.7 that every smooth cubic surface has exactly 27 lines on it. We now want to show this. We also want to study the configuration of these lines, and show that every smooth cubic surface is birational to $\mathbb{P}^{2}$.

The results of this section will not be needed later on. Therefore we will not give all the proofs in every detail here. The goal of this section is rather to give an idea of what can be done with our current methods.

First let us recall some notation from exercise 3.5.4. Let $G=G(1,3)$ be the Grassmannian variety of lines in $\mathbb{P}^{3}$. This is a 4-dimensional projective variety. In this section we will use local affine coordinates on $G$: if $L_{0}\in G$ is the line in $\mathbb{P}^{3}$ (with coordinates $x_{0},\ldots,x_{3}$) given by the equations $x_{2}=x_{3}=0$ (of course every line is of this form after a linear change of coordinates), then there is an open neighborhood $\mathbb{A}^{4}\subset G$ of $L_{0}$ in $G$ given by sending a point $(a,b):=(a_{2},b_{2},a_{3},b_{3})\in\mathbb{A}^{4}$ to the line through the points $(1,0,a_{2},a_{3})$ and $(0,1,b_{2},b_{3})$.

The cubic surfaces in $\mathbb{P}^{3}$ are parametrized by homogeneous polynomials of degree 3 in $x_{0},x_{1},x_{2},x_{3}$ up to scalars, which is a 19-dimensional projective space $\mathbb{P}^{19}$. A cubic surface given by the equation $f_{c}:=\sum_{\alpha}c_{\alpha}s^{\alpha}=0$ (in multi-index notation, so $\alpha$ runs over all quadruples of indices $(\alpha_{0},\alpha_{1},\alpha_{2},\alpha_{3})$ with $\alpha_{i}\geq 0$ and $\sum_{i}\alpha_{i}=3$) corresponds to the point in $\mathbb{P}^{19}$ with homogeneous coordinates $c=(c_{\alpha})$. We denote the corresponding cubic surface by $X_{c}=\{f_{c}=0\}$.

To study lines in cubic surfaces, we consider the so-called incidence correspondence

$M:=\{(L,X)\;;\;L\subset X\}\subset G\times\mathbb{P}^{19}$

consisting of all pairs of a line and a cubic such that the line lies in the cubic. Let us start by proving some facts about this incidence correspondence.

###### Lemma 4.5.1.

With the above notation, the incidence correspondence $M$ has an open cover by affine spaces $\mathbb{A}^{19}$. In particular, $M$ is a smooth 19-dimensional variety.

###### Proof.

In the coordinates $(a,b,c)=(a_{2},a_{3},b_{2},b_{3},c_{\alpha})$ as above, the incidence correspondence $M$ is given by the equations

$(a,b,c)\in M$ $\iff s\left(1,0,a_{2},a_{3}\right)+t\left(0,1,b_{2},b_{3}\right)\in X_{c}\text{ for all }s,t$
$\iff\sum_{\alpha}c_{\alpha}s^{\alpha_{0}}t^{\alpha_{1}}(s\,a_{2}+t\,b_{2})^{\alpha_{2}}(s\,a_{3}+t\,b_{3})^{\alpha_{3}}=0\text{ for all }s,t$
$\iff:\sum_{i}s^{i}t^{3-i}F_{i}(a,b,c)=0\text{ for all }s,t$
$\iff F_{i}(a,b,c)=0\text{ for }0\leq i\leq 3.$

Note that the $F_{i}$ are linear in the $c_{\alpha}$. Moreover, $c_{i,3-i,0,0}$ occurs only in $F_{i}$ for $i=0,\ldots,3$, and it occurs there with coefficient 1. So these equations can be written as $c_{i,3-i,0,0}=G_{i}(a,b,c)$ for $i=0,\ldots,3$, where the $G_{i}$ depend only on those $c_{\alpha}$ where $\alpha_{2}>0$ or $\alpha_{3}>0$. Therefore the variety $\mathbb{A}^{4}\times\mathbb{P}^{15}$ (with coordinates $a_{2},a_{3},b_{2},b_{3},$ and all $c_{\alpha}$ with $\alpha_{2}>0$ or $\alpha_{3}>0$) is isomorphic to an open subvariety of $M$, with the isomorphism given by the equations $c_{i,3-i,0,0}=G(a,b,c)$. It follows that $M$ has an open cover by affine spaces $\mathbb{A}^{4}\times\mathbb{A}^{15}=\mathbb{A}^{19}$. ∎

###### Lemma 4.5.2.

Again with notations as above, let $(a,b,c)\in M$ be a point such that the corresponding cubic surface $X_{c}$ is smooth. Then the $4\times 4$ matrix $\frac{\partial(F_{0},F_{1},F_{2},F_{3})}{\partial(a_{2},a_{3},b_{2},b_{3})}$ is invertible.

---

4. Dimension

Proof. After a change of coordinates we can assume for simplicity that  $a = b = 0$ . Then

$$
\begin{array}{l} \frac {\partial}{\partial a _ {2}} \left(\sum_ {i} s ^ {i} t ^ {3 - i} F _ {i}\right) | _ {(0, 0, c)} = \frac {\partial}{\partial a _ {2}} f _ {c} (s, t, s a _ {2} + t b _ {2}, s a _ {3} + t b _ {3}) | _ {(0, 0, c)} \\ = s \frac {\partial f _ {c}}{\partial x _ {2}} (s, t, 0, 0). \\ \end{array}
$$

The  $(s,t)$ -coefficients of this polynomial are the first row in the matrix  $\frac{\partial F_i}{\partial(a,b)}(0,0,c)$ . The other rows are obviously  $s\frac{\partial f_c}{\partial x_3}(s,t,0,0)$ ,  $t\frac{\partial f_c}{\partial x_2}(s,t,0,0)$ , and  $t\frac{\partial f_c}{\partial x_3}(s,t,0,0)$ . So if the matrix  $\frac{\partial F_i}{\partial(a,b)}(0,0,c)$  were not invertible, there would be a relation

$$
\left(\lambda_ {2} s + \mu_ {2} t\right) \frac {\partial f _ {c}}{\partial x _ {2}} (s, t, 0, 0) + \left(\lambda_ {3} s + \mu_ {3} t\right) \frac {\partial f _ {c}}{\partial x _ {3}} (s, t, 0, 0) = 0
$$

identically in  $s, t$ , with  $(\lambda_2, \mu_2, \lambda_3, \mu_3) \neq (0, 0, 0, 0)$ . But this means that  $\frac{\partial f_c}{\partial x_2}(s, t, 0, 0)$  and  $\frac{\partial f_c}{\partial x_3}(s, t, 0, 0)$  have a common linear factor, i.e. there is a point  $P = (x_0, x_1, 0, 0) \in \mathbb{P}^3$  such that  $\frac{\partial f_c}{\partial x_2}(P) = \frac{\partial f_c}{\partial x_3}(P) = 0$ . But as the line  $L_0$  lies in the cubic  $f_c$ , we must have  $f_c = x_2 \cdot g_2(x_0, x_1, x_2, x_3) + x_3 \cdot g_3(x_0, x_1, x_2, x_3)$  for some  $g_2, g_3$ . Hence  $\frac{\partial f_c}{\partial x_0}(P) = \frac{\partial f_c}{\partial x_3}(P) = 0$  also, which means that  $P$  is a singular point of the cubic  $X_c$ . This is a contradiction to our assumptions.

Remark 4.5.3. By remark 4.4.11, lemma 4.5.2 means that locally (in the classical topology) around any point  $(a,b,c)\in M$  such that  $X_{c}$  is smooth, the coordinates  $a_2,a_3,b_2,b_3$  are determined uniquely in  $M$  by the  $c_{tt}$ . In other words, the projection map  $\pi :M\to \mathbb{P}^{19}$  is a local isomorphism (again in the classical topology!) around such a point  $(a,b,c)\in M$ . So the local picture looks as follows:

![img-7.jpeg](images/img-7.jpeg)

As the number of lines in a given cubic  $X_{c}$  is just the number of inverse image points of  $c \in \mathbb{P}^{19}$  under this projection map, it follows that the number of lines on a smooth cubic surface is independent of the particular cubic chosen.

Theorem 4.5.4. Every smooth cubic surface  $X\subset \mathbb{P}^3$  contains exactly 27 lines.

Proof. We have just argued that the number of lines on a smooth cubic surface does not depend on the surface, so we can pick a special one. We take the surface  $X$  given by the equation  $f = x_0^3 + x_1^3 + x_2^3 + x_3^3 = 0$  (which is smooth in characteristic not equal to 3). Up to a permutation of coordinates, every line in  $\mathbb{P}^3$  can be written  $x_0 = a_2x_2 + a_3x_3$ ,

---

$x_{1}=b_{2}x_{2}+b_{3}x_{3}$. Substituting this in the equation $f$ yields the conditions

$a_{2}^{3}+b_{2}^{3}=-1,$ (1)
$a_{3}^{3}+b_{3}^{3}=-1,$ (2)
$a_{2}^{2}a_{3}=-b_{2}^{2}b_{3},$ (3)
$a_{2}a_{3}^{2}=-b_{2}b_{3}^{2}.$ (4)

Assume that $a_{2},a_{3},b_{2},b_{3}$ are all non-zero. Then $(3)^{2}/(4)$ gives $a_{2}^{3}=-b_{2}^{3}$, while $(4)^{2}/(3)$ yields $a_{3}^{3}=-b_{3}^{3}$. This is obviously a contradiction to (1) and (2). Hence at least one of the $a_{2},a_{3},b_{2},b_{3}$ must be zero. Assume without loss of generality that $a_{2}=0$. Then $b_{3}=0$ and $a_{3}^{3}=b_{2}^{3}=-1$. This gives 9 lines by setting $a_{3}=-\omega^{i}$ and $b_{2}=-\omega^{j}$ for $0\leq i,j\leq 2$ and $\omega$ a third root of unity. So by allowing permutations of the coordinates we find that there are exactly the following 27 lines on $X$:

$x_{0}+x_{1}\omega^{i}=x_{2}+x_{3}\omega^{j}=0,\quad 0\leq i,j\leq 2,$
$x_{0}+x_{2}\omega^{i}=x_{1}+x_{3}\omega^{j}=0,\quad 0\leq i,j\leq 2,$
$x_{0}+x_{3}\omega^{i}=x_{1}+x_{2}\omega^{j}=0,\quad 0\leq i,j\leq 2.$

∎

###### Remark 4.5.5.

We will now study to a certain extent the *configuration* of the 27 lines on a cubic surface, i. e. determine which of the lines intersect. Consider the special cubic $X$ of the proof of theorem 4.5.4, and let $L$ be the line

$L=\{x_{0}+x_{1}=x_{2}+x_{3}=0\}$

in $X$. Then we can easily check that $L$ meets exactly 10 of the other lines in $X$, namely

$x_{0}+x_{1}\omega^{i}=x_{2}+x_{3}\omega^{j}=0,\quad(i,j)\neq(0,0)$
$x_{0}+x_{2}=x_{1}+x_{3}=0,$
$x_{0}+x_{3}=x_{1}+x_{2}=0.$

The same is true for every other line in $X$. In fact, the statement is also true for every smooth cubic surface, and not just for the special one that we have just considered. The proof of this is very similar to the proof above that the number of lines on a smooth cubic surface does not depend on the particular cubic chosen.

Now let $L_{1}$ and $L_{2}$ be two disjoint lines on a smooth cubic surface $X$. We claim that there are exactly 5 lines on $X$ that intersect both $L_{1}$ and $L_{2}$. To show this, one can proceed in the same way as above: check the statement directly on a special cubic surface, and then show that it must then be true for all other smooth cubic surfaces as well.

###### Proposition 4.5.6.

Any smooth cubic surface in $\mathbb{P}^{3}$ is birational to $\mathbb{P}^{2}$.

###### Proof.

By remark 4.5.5 there are two disjoint lines $L_{1},L_{2}\subset X$. The following mutually inverse rational maps $X\dashrightarrow L_{1}\times L_{2}$ and $L_{1}\times L_{2}\dashrightarrow X$ show that $X$ is birational to $\mathbb{P}^{1}\times\mathbb{P}^{1}$ and hence to $\mathbb{P}^{2}$:

“$X\dashrightarrow L_{1}\times L_{2}$”: By exercise 3.5.1, for every point $P$ not on $L_{1}$ or $L_{2}$ there is a unique line $L(P)$ in $\mathbb{P}^{3}$ through $L_{1}$, $L_{2}$ and $P$. Take the rational map $P\mapsto(L_{1}\cap L(P),L_{2}\cap L(P))$ that is obviously well-defined away from $L_{1}\cup L_{2}$.

“$L_{1}\times L_{2}\dashrightarrow X$”: Map any pair of points $(P,Q)\in L_{1}\times L_{2}$ to the third intersection point of $X$ with the line $\overline{PQ}$. This is well-defined whenever $\overline{PQ}$ is not contained in $X$. ∎

###### Proposition 4.5.7.

Any smooth cubic surface in $\mathbb{P}^{3}$ is isomorphic to $\mathbb{P}^{1}\times\mathbb{P}^{1}$ blown up in 5 (suitably chosen) points, or equivalently, to $\mathbb{P}^{2}$ blown up in 6 (suitably chosen) points.

---

Proof.

We will only sketch the proof. Let $X$ be a smooth cubic surface, and let $f:X\dashrightarrow L_{1}\times L_{2}\cong\mathbb{P}^{1}\times\mathbb{P}^{1}$ be the rational map as in the proof of proposition 4.5.6.

First of all we claim that $f$ is actually a morphism. To see this, note that there is a different description for $f$: if $P\in X\backslash L_{1}$, let $H$ be the unique plane in $\mathbb{P}^{3}$ that contains $L_{1}$ and $P$, and let $f_{2}(P)=H\cap L_{2}$. If one defines $f_{1}(P)$ similarly, then $f(P)=(f_{1}(P),f_{2}(P))$. Now if the point $P$ lies on $L_{1}$, let $H$ be the tangent plane to $X$ at $P$, and again let $f_{2}(P)=H\cap L_{2}$. Extending $f_{1}$ similarly, one can show that this extends $f=(f_{1},f_{2})$ to a well-defined morphism $X\to\mathbb{P}^{1}\times\mathbb{P}^{1}$ on all of $X$.

Now let us investigate where the inverse map $\mathbb{P}^{1}\times\mathbb{P}^{1}\dashrightarrow X$ is not well-defined. As already mentioned in the proof of proposition 4.5.6, this is the case if the point $(P,Q)\in L_{1}\times L_{2}$ is such that $\overline{PQ}\subset X$. In this case, the whole line $\overline{PQ}\cong\mathbb{P}^{1}$ will be mapped to $(P,Q)$ by $f$, and it can be checked that $f$ is actually locally the blow-up of this point. By remark 4.5.5 there are exactly 5 such lines $\overline{PQ}$ on $X$. Hence $f$ is the blow-up of $\mathbb{P}^{1}\times\mathbb{P}^{1}$ at 5 points.

By lemma 4.3.12 it then follows that $f$ is also the blow-up of $\mathbb{P}^{2}$ in 6 suitably chosen points. ∎

###### Remark 4.5.8.

It is interesting to see the 27 lines on a cubic surface $X$ in the picture where one thinks of $X$ as a blow-up of $\mathbb{P}^{2}$ in 6 points. It turns out that the 27 lines correspond to the following curves that we all already know (and that are all isomorphic to $\mathbb{P}^{1}$):

- the 6 exceptional hypersurfaces,
- the strict transforms of the $\binom{6}{2}=15$ lines through two of the blown-up points,
- the strict transforms of the $\binom{6}{5}=6$ conics through five of the blown-up points (see exercise 3.5.8).

In fact, it is easy to see by the above explicit description of the isomorphism of $X$ with the blow-up of $\mathbb{P}^{2}$ that these curves on the blow-up actually correspond to lines on the cubic surface.

It is also interesting to see again in this picture that every such “line” meets 10 of the other “lines”, as mentioned in remark 4.5.5:

- Every exceptional hypersurface intersects the 5 lines and the 5 conics that pass through this blown-up point.
- Every line through two of the blown-up points meets

- the 2 exceptional hypersurfaces of the blown-up points,
- the $\binom{4}{2}=6$ lines through two of the four remaining points,
- the 2 conics through the four remaining points and one of the blown-up points.
- Every conic through five of the blown-up points meets the 5 exceptional hypersurfaces at these points, as well as the 5 lines through one of these five points and the remaining point.

### 4.6. Exercises

###### Exercise 4.6.1.

Let $X,Y\subset\mathbb{P}^{n}$ be projective varieties. Show that $X\cap Y$ is not empty if $\dim X+\dim Y\geq n$.

On the other hand, give an example of a projective variety $Z$ and closed subsets $X,Y\subset Z$ with $\dim X+\dim Y\geq\dim Z$ and $X\cap Y=\emptyset$.

(Hint: Let $H_{1},H_{2}$ be two disjoint linear subspaces of dimension $n$ in $\mathbb{P}^{2n+1}$, and consider $X\subset\mathbb{P}^{n}\cong H_{1}\subset\mathbb{P}^{2n+1}$ and $Y\subset\mathbb{P}^{n}\cong H_{2}\subset\mathbb{P}^{2n+1}$ as subvarieties of $\mathbb{P}^{2n+1}$. Show that the join $J(X,Y)\subset\mathbb{P}^{2n+1}$ of exercise 3.5.7 has dimension $\dim X+\dim Y+1$. Then construct $X\cap Y$ as a suitable intersection of $J(X,Y)$ with $n+1$ hyperplanes.)

---

###### Exercise 4.6.2.

(This is a generalization of corollary 4.2.7). Let $f:X\to Y$ be a morphism of varieties. Show that there is a non-empty open subset $U$ of $Y$ such that every component of the fiber $f^{-1}(P)$ has dimension $\dim X-\dim Y$ for all $P\in U$.

(Hint: You can assume $X\subset\mathbb{A}^{n}$ and $Y\subset\mathbb{A}^{m}$ to be affine. By considering the graph $(P,f(P))\in\mathbb{A}^{n+m}$, reduce to the case where $f:\mathbb{A}^{n+1}\to\mathbb{A}^{n}$ is the projection map.)

###### Exercise 4.6.3.

Let $f:X\to Y$ be a morphism of varieties, and let $Z\subset X$ be a closed subset. Assume that $f^{-1}(P)\cap Z$ is irreducible and of the same dimension for all $P\in Y$. Use exercise 4.6.2 to prove that then $Z$ is irreducible too. (This is a quite useful criterion to check the irreducibility of closed subsets.)

Show by example that the conclusion is in general false if the $f^{-1}(P)\cap Z$ are irreducible but not all of the same dimension.

###### Exercise 4.6.4.

Let $X$ be a variety, and let $Y\subset X$ a closed subset. For every element in an open affine cover $\{U_{i}\}$ of $X$, let $V_{i}=U_{i}\cap Y$, and let $\tilde{U_{i}}$ be the blow-up of $U_{i}$ at $V_{i}$. Show that the spaces $\tilde{U_{i}}$ can be glued together to give a variety $\tilde{X}$. (This variety is then called the blow-up of $X$ at $Y$.)

###### Exercise 4.6.5.

A quadric in $\mathbb{P}^{n}$ is a projective variety in $\mathbb{P}^{n}$ that can be given as the zero locus of a quadratic polynomial. Show that every quadric in $\mathbb{P}^{n}$ is birational to $\mathbb{P}^{n-1}$.

###### Exercise 4.6.6.

Show that for four *general* lines $L_{1},\ldots,L_{4}\subset\mathbb{P}^{3}$, there are exactly two lines in $\mathbb{P}^{3}$ intersecting all the $L_{i}$. (This means: the subset of $G(1,3)^{4}$ of all $(L_{1},\ldots,L_{4})$ such that there are exactly two lines in $\mathbb{P}^{3}$ intersecting $L_{1},\ldots,L_{4}$ is dense. You may want to use the result of exercise 3.5.4 (iii) that $G(1,3)$ is a quadric in $\mathbb{P}^{5}$.)

###### Exercise 4.6.7.

Let $P_{1}=(1:0:0),P_{2}=(0:1:0),P_{3}=(0:0:1)\in\mathbb{P}^{2}$, and let $U=\mathbb{P}^{2}\backslash\{P_{1},P_{2},P_{3}\}$. Consider the morphism

$f:U\mapsto\mathbb{P}^{2},(a_{0}:a_{1}:a_{2})\mapsto(a_{1}a_{2}:a_{0}a_{2}:a_{0}a_{1}).$
1. Show that there is no morphism $F:\mathbb{P}^{2}\to\mathbb{P}^{2}$ extending $f$.
2. Let $\tilde{\mathbb{P}}^{2}$ be the blow-up of $\mathbb{P}^{2}$ in the three points $P_{1},P_{2},P_{3}$. Show that there is an *isomorphism* $\tilde{f}:\tilde{\mathbb{P}}^{2}\to\tilde{\mathbb{P}}^{2}$ extending $f$. This is called the Cremona transformation.

###### Exercise 4.6.8.

Let $X\subset\mathbb{A}^{n}$ be an affine variety. For every $f\in k[x_{0},\ldots,x_{n}]$ denote by $f^{in}$ the *initial terms* of $f$, i. e. the terms of $f$ of the lowest occurring degree (e. g. if $f=x_{2}^{2}+3x_{1}x_{3}-x_{2}x_{3}^{2}$ then the lowest occurring degree in $f$ is $2$, so the initial terms are the terms of degree $2$, namely $f^{in}=x_{2}^{2}+3x_{1}x_{3}$). Let $I(X)^{in}=\{f^{in}\mbox{ ; }f\in I(X)\}$ be the ideal of the initial terms in $I(X)$.

Now let $\pi:\tilde{X}\to X$ be the blow-up of $X$ in the origin $\{0\}=Z(x_{1},\ldots,x_{n})$. Show that the exceptional hypersurface $\pi^{-1}(0)\subset\mathbb{P}^{n}$ is precisely the projective zero locus of the homogeneous ideal $I(X)^{in}$.

###### Exercise 4.6.9.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $P\in X$ be a point. Show that the coordinate ring $A(C_{X,P})$ of the tangent cone to $X$ at $P$ is equal to $\oplus_{k\geq 0}I(P)^{k}/I(P)^{k+1}$, where $I(P)$ is the ideal of $P$ in $A(X)$.

###### Exercise 4.6.10.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $Y_{1},Y_{2}\subsetneq X$ be irreducible, closed subsets, no-one contained in the other. Let $\tilde{X}$ be the blow-up of $X$ at the (possibly non-radical, see exercise 1.4.1) ideal $I(Y_{1})+I(Y_{2})$. Then the strict transforms of $Y_{1}$ and $Y_{2}$ on $\tilde{X}$ are disjoint.

###### Exercise 4.6.11.

Let $C\subset\mathbb{P}^{2}$ be a smooth curve, given as the zero locus of a homogeneous polynomial $f\in k[x_{0},x_{1},x_{2}]$. Consider the morphism

$\varphi_{C}:C\to\mathbb{P}^{2},\>P\mapsto\Big{(}\frac{\partial f}{\partial x_{0}}\,(P):\frac{\partial f}{\partial x_{1}}\,(P):\frac{\partial f}{\partial x_{2}}\,(P)\Big{)}.$

---

4. Dimension

The image  $\varphi_C(C) \subset \mathbb{P}^2$  is called the dual curve to  $C$ .

(i) Find a geometric description of  $\varphi$ . What does it mean geometrically if  $\varphi(P) = \varphi(Q)$  for two distinct points  $P, Q \in C$ ?
(ii) If  $C$  is a conic, prove that its dual  $\varphi(C)$  is also a conic.
(iii) For any five lines in  $\mathbb{P}^2$  in general position (what does this mean?) show that there is a unique conic in  $\mathbb{P}^2$  that is tangent to these five lines. (Hint: Use exercise 3.5.8.)

Exercise 4.6.12. Resolve the singularities of the following curves by subsequent blow-ups of the singular points. This means: starting with the given curve  $C$ , blow up all singular points of  $C$ , and replace  $C$  by its strict transform. Continue this process until the resulting curve is smooth.

Also, describe the singularities that occur in the intermediate steps of the resolution process.

(i)  $C = \{(x,y);x^2 -x^4 -y^4 = 0\} \subset \mathbb{A}^2,$
(ii)  $C = \{(x,y);y^3 -x^5 = 0\} \subset \mathbb{A}^2,$
(iii)  $C = \{(x,y);y^2 -x^k = 0\} \subset \mathbb{A}^2,k\in \mathbb{N}.$

Exercise 4.6.13. Show that "a general hypersurface in  $\mathbb{P}^n$  is smooth". In other words, for any given  $d$  we can consider  $\mathbb{P}^{\binom{n+d}{d}-1}$  as the "space of all hypersurfaces of degree  $d$  in  $\mathbb{P}^n$ ", by associating to any hypersurface  $\{f(x_0,\ldots,x_n)=0\} \subset \mathbb{P}^n$  with  $f$  homogeneous of degree  $d$  the projective vector of all  $\binom{n+d}{d}$  coefficients of  $f$ . Then show that the subset of  $\mathbb{P}^{\binom{n+d}{d}-1}$  corresponding to smooth hypersurfaces is non-empty and open.

Exercise 4.6.14. (This is a generalization of exercises 3.5.8 and 4.6.11 (iii).) For  $i = 0, \ldots, 5$ , determine how many conics there are in  $\mathbb{P}^2$  that are tangent to  $i$  given lines and in addition pass through  $5 - i$  given points.