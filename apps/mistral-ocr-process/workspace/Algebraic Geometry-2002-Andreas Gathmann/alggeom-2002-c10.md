10. Chern classes

For any vector bundle $\pi:F\to X$ of rank $r$ on a scheme $X$ we define an associated projective bundle $p:\mathbb{P}(F)\to X$ whose fibers $p^{-1}(P)$ are just the projectivizations of the affine fibers $\pi^{-1}(P)$. We construct natural line bundles $\mathcal{O}_{\mathbb{P}(F)}(d)$ on $\mathbb{P}(F)$ for all $d\in\mathbb{Z}$ that correspond to the standard line bundles $\mathcal{O}(d)$ on projective spaces. As in the case of vector bundles there are pull-back homomorphisms $A_{*}(X)\to A_{*}(\mathbb{P}(F))$ between the Chow groups.

For a bundle as above we define the $i$-th Segre class $s_{i}(F):A_{*}(X)\to A_{*-i}(X)$ by $s_{i}(F)\cdot\alpha=p_{*}(D_{F}^{r-1+i}\cdot p^{*}\alpha)$, where $D_{F}$ denotes the Cartier divisor associated to the line bundle $\mathcal{O}_{\mathbb{P}(F)}(1)$. The Chern classes $c_{i}(F)$ are defined to be the inverse of the Segre classes. Segre and Chern classes are commutative; they satisfy the projection formula for proper push-forwards and are compatible with pull-backs. They are multiplicative on exact sequences. Moreover, $c_{i}(F)=0$ for $i>r$. The top Chern class $c_{r}(F)$ has the additional geometric interpretation as the zero locus of a section of $F$. Using the technique of Chern roots one can compute the Chern classes of almost any bundle that is constructed from known bundles in some way (e. g. by means of direct sums, tensor products, dualizing, exact sequences, symmetric and exterior products).

The Chern character $\mathrm{ch}(F)$ and Todd class $\mathrm{td}(F)$ are defined to be certain polynomial combinations of the Chern classes of $F$. The Hirzebruch-Riemann-Roch theorem states that $\sum_{i}h^{i}(X,F)=\deg(\mathrm{ch}(F)\cdot\mathrm{td}(T_{X}))$ for any vector bundle $F$ on a smooth projective scheme $X$. We study some examples and applications of this theorem and give a sketch of proof.

### 10.1. Projective bundles

Recall that for any line bundle $\mathcal{L}$ on a variety $X$ there is a Cartier divisor on $X$ corresponding to $\mathcal{L}$ that in turn defines intersection homomorphisms $A_{k}(X)\to A_{k-1}(X)$. These homomorphisms can be thought of as intersecting a $k$-cycle on $X$ with the divisor of any rational section of $\mathcal{L}$. We now want to generalize this idea from line bundles to vector bundles. To do so, we need some preliminaries on projective bundles first.

Roughly speaking, the projective bundle $\mathbb{P}(E)$ associated to a vector bundle $E$ of rank $r$ on a scheme $X$ is simply obtained by replacing the fibers (that are all isomorphic to $\mathbb{A}^{r}$) by the corresponding projective spaces $\mathbb{P}^{r-1}=(\mathbb{A}^{r}\backslash\{0\})/k^{*}$. Let us give the precise definition.

###### Definition 10.1.1.

Let $\pi:F\to X$ be a vector bundle of rank $r$ on a scheme $X$ (see remark 7.3.2). In other words, there is an open covering $\{U_{i}\}$ of $X$ such that

1. there are isomorphisms $\psi_{i}:\pi^{-1}(U_{i})\to U_{i}\times\mathbb{A}^{r}$ over $U_{i}$,
2. on the overlaps $U_{i}\cap U_{j}$ the compositions

$\psi_{i}\circ\psi_{j}^{-1}:(U_{i}\cap U_{j})\times\mathbb{A}^{r}\to(U_{i}\cap U_{j})\times\mathbb{A}^{r}$

are linear in the coordinates of $\mathbb{A}^{r}$, i. e. they are of the form

$(P,x)\mapsto(P,\Psi_{i,j}x)$

where $P\in U$, $x=(x_{1},\ldots,x_{r})\in\mathbb{A}^{r}$, and the $\Psi_{i,j}$ are $r\times r$ matrices with entries in $\mathcal{O}_{X}(U_{i}\cap U_{j})$.

Then the projective bundle $\mathbb{P}(F)$ is defined by glueing the patches $U_{i}\times\mathbb{P}^{r-1}$ along the same transition functions, i. e. by glueing $U_{i}\times\mathbb{P}^{r-1}$ to $U_{j}\times\mathbb{P}^{r-1}$ along the isomorphisms

$(U_{i}\cap U_{j})\times\mathbb{P}^{r-1}\to(U_{i}\cap U_{j})\times\mathbb{P}^{r-1},\quad(P,x)\mapsto(P,\Psi_{i,j}x)$

for all $i,j$, where $P\in U_{i}\cap U_{j}$ and $x=(x_{1}:\cdots:x_{r})\in\mathbb{P}^{r-1}$. We say that $\mathbb{P}(F)$ is a projective bundle of rank $r-1$ on $X$

---

Note that in the same way as for vector bundles there is a natural projection morphism $p:\mathbb{P}(F)\to X$ that sends a point $(P,x)$ to $P$. In contrast to the vector bundle case however the morphism $p$ is *proper* (which follows easily from exercise 9.5.5).

###### Example 10.1.2.

Let $X=\mathbb{P}^{1}$, and let $F$ be the vector bundle (i. e. locally free sheaf) $\mathcal{O}_{X}\oplus\mathcal{O}_{X}(-1)$ on $X$. Then $\mathbb{P}(F)$ is a projective bundle of rank $1$ on $X$, so it is a scheme of dimension $2$. We claim that $\mathbb{P}(F)$ is isomorphic to the blow-up $\tilde{\mathbb{P}}^{2}$ of the projective plane in a point $P$. In fact, this can be checked directly: by definition 10.1.1 $\mathbb{P}(F)$ is obtained by glueing two copies $U_{1},U_{2}$ of $\mathbb{A}^{1}\times\mathbb{P}^{1}$ along the isomorphism

$(\mathbb{A}^{1}\backslash\{0\})\times\mathbb{P}^{1}\to(\mathbb{A}^{1}\backslash\{0\})\times\mathbb{P}^{1},\quad(z,(x_{1}:x_{2}))\mapsto(\frac{1}{z},(x_{1}:zx_{2})).$

On the other hand, $\tilde{\mathbb{P}}^{2}$ is given by

$\tilde{\mathbb{P}}^{2}=\{((x_{0}:x_{1}:x_{2}),(y_{1}:y_{2}))\mbox{ ; }x_{1}y_{2}=x_{2}y_{1}\}\subset\mathbb{P}^{2}\times\mathbb{P}^{1}$

(see example 4.3.4). Now an isomorphism is given by

$U_{1}\cong\mathbb{A}^{1}\times\mathbb{P}^{1}\to\tilde{\mathbb{P}}^{2},\quad(z,(x_{1}:x_{2}))\mapsto((x_{1}:zx_{2}:x_{2}),(z:1)),$
$U_{2}\cong\mathbb{A}^{1}\times\mathbb{P}^{1}\to\tilde{\mathbb{P}}^{2},\quad(z,(x_{1}:x_{2}))\mapsto((x_{1}:x_{2}:zx_{2}),(1:z))$

(note that this is compatible with the glueing isomorphism above).

To see geometrically that $\tilde{\mathbb{P}}^{2}$ is a projective bundle of rank $1$ over $\mathbb{P}^{1}$ let $p:\tilde{\mathbb{P}}^{2}\to E\cong\mathbb{P}^{1}$ be the projection morphism onto the exceptional divisor as of example 9.2.14 (ii). The fibers of this morphism are the strict transforms of lines through $P$, so they are all isomorphic to $\mathbb{P}^{1}$.

###### Remark 10.1.3.

If $F$ is a vector bundle and $L$ a line bundle on $X$ then $\mathbb{P}(F)\cong\mathbb{P}(F\otimes L)$. In fact, tensoring $F$ with $L$ just multiplies the transition matrices $\Psi_{i,j}$ of definition 10.1.1 with a scalar function, which does not affect the morphism as the $x_{i}$ are projective coordinates.

###### Example 10.1.4.

Let $p:\mathbb{P}(F)\to X$ be a projective bundle over a scheme $X$, given by an open cover $\{U_{i}\}$ of $X$ and transition matrices $\Psi_{i,j}$ as in definition 10.1.1. In this example we want to construct line bundles $\mathcal{O}_{\mathbb{P}(F)}(d)$ for all $d\in\mathbb{Z}$ on $\mathbb{P}(F)$ that are relative versions of the ordinary bundles $\mathcal{O}_{\mathbb{P}^{r-1}}(d)$ on projective spaces.

The construction is simple: on the patches $U_{i}\times\mathbb{P}^{r-1}$ of $\mathbb{P}(F)$ we take the line bundles $\mathcal{O}_{\mathbb{P}^{r-1}}(d)$. On the overlaps $U_{i}\cap U_{j}$ these line bundles are glued by $\varphi\mapsto\varphi\circ\Psi_{i,j}$, where $\varphi=\frac{f}{g}$ is (locally) a quotient of homogeneous polynomials $f,g\in k[x_{1},\ldots,x_{r}]$ with $\deg f-\deg g=d$. Note that the $\varphi\circ\Psi_{i,j}$ satisfies the same degree conditions as the $\Psi_{i,j}$ are linear functions.

Summarizing, we can say that sections of the line bundle $\mathcal{O}_{\mathbb{P}(F)}(d)$ are locally given by quotients of two polynomials which are homogeneous in the fiber coordinates and whose degree difference is $d$.

###### Construction 10.1.5.

Again let $p:\mathbb{P}(F)\to X$ be a projective bundle over a scheme $X$, given by an open cover $\{U_{i}\}$ of $X$ and transition matrices $\Psi_{i,j}$. Consider the vector bundle $p^{*}F$ on $\mathbb{P}(F)$. It is given by glueing the patches $U_{i}\times\mathbb{P}^{r-1}\times\mathbb{A}^{r}$ along the isomorphisms

$(U_{i}\cap U_{j})\times\mathbb{P}^{r-1}\times\mathbb{A}^{r}\to(U_{i}\cap U_{j})\times\mathbb{P}^{r-1}\times\mathbb{A}^{r},\quad(P,x,y)\mapsto(P,\Psi_{i,j}x,\Psi_{i,j}y),$

where $x=(x_{1}:\cdots:x_{r})$ are projective coordinates on $\mathbb{P}^{r-1}$, and $y=(y_{1},\ldots,y_{r})$ are affine coordinates on $\mathbb{A}^{r}$. Now consider the subbundle $S$ of $p^{*}F$ given locally by the equations $x_{i}y_{j}=x_{j}y_{i}$ for all $i,j=1,\ldots,r$, i. e. the subbundle of $p^{*}F$ consisting of those $(y_{1},\ldots,y_{r})$ that are scalar multiples of $(x_{1}:\cdots:x_{r})$. Obviously, $S$ is a line bundle on $\mathbb{P}(F)$ contained in $p^{*}F$. Geometrically, the fiber of $S$ over a point $(P,x)\in\mathbb{P}(F)$ is precisely the line in the fiber $F_{P}$ whose projectivization is the point $x$. The line bundle $S\subset p^{*}F$ is called the tautological subbundle on $\mathbb{P}(F)$.

######

---

We can actually identify the subbundle $S$ in the language of example 10.1.4: we claim that $S$ is isomorphic to $\mathcal{O}_{\mathbb{P}(F)}(-1)$. In fact, an isomorphism is given by

$\mathcal{O}_{\mathbb{P}(F)}(-1)\to S,\quad\varphi\mapsto(y_{i}=\varphi\cdot x_{i}),$

where $\varphi$ is (locally) the quotient of two polynomials homogeneous in the $x_{i}$ of degree difference $-1$. It is obvious that the $\varphi\cdot x_{i}$ are then quotients of two polynomials homogeneous in the $x_{i}$ of the same degree, so that the $y_{i}$ are well-defined.

###### Example 10.1.6.

One place where projective bundles occur naturally is in blow-ups. Recall from construction 4.3.2 that the blow-up $\tilde{X}$ of an affine variety $X\subset\mathbb{A}^{n}$ at a subvariety $Y\subset X$ with ideal $I(Y)=(f_{1},\ldots,f_{r})$ is defined to be the closure of the graph

$\Gamma=\{(P,(f_{1}(P):\cdots:f_{r}(P)))\;;\;P\in X\backslash Y\}\subset X\times\mathbb{P}^{r-1}.$

The exceptional hypersurface of the blow-up must be contained in $Y\times\mathbb{P}^{r-1}$, which has dimension $\dim Y+r-1$. So if $Y$ has dimension $\dim X-r$ (which is the expected dimension as its ideal has $r$ generators) then the exceptional hypersurface must be all of $Y\times\mathbb{P}^{r-1}$ for dimensional reasons.

Let us now sketch how this construction can be generalized to blow-ups of arbitrary (not necessarily affine) varieties $X$ in a subvariety $Y$. For simplicity let us assume that there are $r$ line bundles $\mathcal{L}_{1},\ldots,\mathcal{L}_{r}$ on $X$ together with global sections $s_{i}\in H^{0}(X,\mathcal{L}_{i})$ such that $Y$ is scheme-theoretically the zero locus $s_{1}=\cdots=s_{r}=0$. Then the straightforward generalization of the above construction is to define the blow-up of $X$ in $Y$ to be the closure of the graph

$\Gamma=\{(P,(s_{1}(P):\cdots:s_{r}(P))\;;\;P\in X\backslash Y\}\subset\mathbb{P}(\mathcal{L}_{1}\oplus\cdots\oplus\mathcal{L}_{r}).$

As above, if $Y$ has codimension $r$ in $X$ then the exceptional hypersurface of the blow-up is the projective bundle $\mathbb{P}((\mathcal{L}_{1}\oplus\cdots\oplus\mathcal{L}_{r})|_{Y})$ over $Y$.

Now recall from remark 7.4.17 and example 9.4.3 (ii) that the normal bundle of a smooth codimension-1 hypersurface $Y$ in a smooth variety $X$ that is given as the zero locus of a section of a line bundle $\mathcal{L}$ is just the restriction of this line bundle $\mathcal{L}$ to $Y$. If we iterate this result $r$ times we see that the normal bundle of a smooth codimension-$r$ hypersurface $Y$ in a smooth variety $X$ that is given as the zero locus of sections of $r$ line bundles $\mathcal{L}_{1},\ldots,\mathcal{L}_{r}$ is just $(\mathcal{L}_{1}\oplus\cdots\oplus\mathcal{L}_{r})|_{Y}$. Combining this with what we have said above we conclude that *the exceptional hypersurface of the blow-up of a smooth variety $X$ in a smooth variety $Y$ is just the projectivized normal bundle $\mathbb{P}(N_{Y/X})$ over $Y$*. This is a relative version of our earlier statement that the exceptional hypersurface of the blow-up of a variety in a smooth point is isomorphic to the projectivized tangent space at this point.

In the above argument we have used for simplicity that the codimension-$r$ subvariety $Y$ is globally the zero locus of $r$ sections of line bundles. Actually we do not need this. We only need that $Y$ is *locally* around every point the zero locus of $r$ regular functions, as we can then make the above construction locally and finally glue the local patches together. Using techniques similar to those in theorem 9.3.7 one can show that *every* smooth subvariety $Y$ of codimension $r$ in a smooth variety $X$ is locally around every point the zero locus of $r$ regular functions. So it is actually true in general that the exceptional hypersurface of the blow-up of $X$ in $Y$ is $\mathbb{P}(N_{Y/X})$ if $X$ and $Y$ are smooth.

Finally, in analogy to the case of vector bundles in proposition 9.1.14 let us discuss pull-back homomorphisms for Chow groups induced by projective bundles.

###### Lemma 10.1.7.

Let $F$ be a vector bundle on a scheme $X$ of rank $r+1$, and let $p:\mathbb{P}(F)\to X$ be the associated projective bundle of rank $r$. Then there are pull-back homomorphisms

$p^{*}:A_{k}(X)\to A_{k+r}(\mathbb{P}(F)),\quad[V]\mapsto[p^{-1}(V)]$

for all $k$, satisfying the following compatibilities with our earlier constructions:

---

10. Chern classes

(i) (Compatibility with proper push-forward) Let  $f: X \to Y$  be a proper morphism, and let  $F$  be a vector bundle of rank  $r + 1$  on  $Y$ . Form the fiber diagram

![img-0.jpeg](images/img-0.jpeg)

Then  $p^* f_* = f_*' p'^*$  as homomorphisms  $A_k(X) \to A_{k + r}(\mathbb{P}(F))$ .

(ii) (Compatibility with intersection products) Let  $F$  be a vector bundle of rank  $r + 1$  on  $X$ , and let  $D \in \operatorname{Pic} X$  be a Cartier divisor (class). Then

$$
p ^ {*} (D \cdot \alpha) = (p ^ {*} D) \cdot (p ^ {*} \alpha)
$$

in  $A_{k + r - 1}(\mathbb{P}(F))$  for every  $k$ -cycle  $\alpha \in A_k(X)$ .

Proof. (i): Let  $V \subset X$  be a  $k$ -dimensional subvariety. Then  $p^{-1}(f(V)) = f'(p'^{-1}(V)) \eqqcolon W$ , and both  $p^* f_*[V]$  and  $f'_* p'^*[V]$  are equal to  $d \cdot [W]$ , where  $d$  is the generic number of inverse image points of  $f$  (resp.  $f'$ ) on  $f(V)$  (resp.  $p^{-1}(f(V))$ ).

(ii): Let  $\alpha = [V]$  for a  $k$ -dimensional subvariety  $V \subset X$ . On  $V$  the Cartier divisor  $D$  is given by a line bundle  $\mathcal{L}$ . If  $\varphi$  is any rational section of  $\mathcal{L}$  then the statement follows from the obvious identity  $p^* \mathrm{div}(\varphi) = \mathrm{div}(p^*\varphi)$ .

Remark 10.1.8. We have now constructed pull-back morphisms for Chow groups in three cases:

(i) inclusions of open subsets (example 9.1.11),
(ii) projections from vector bundles (proposition 9.1.14),
(iii) projections from projective bundles (lemma 10.1.7).

These are in fact special cases of a general class of morphisms, called flat morphisms, for which pull-back maps exist. See [F] section 1.7 for more details.

10.2. Segre and Chern classes of vector bundles. Let  $X$  be a scheme, and let  $F$  be a vector bundle of rank  $r$  on  $X$ . Let  $p: \mathbb{P}(F) \to X$  be the projection from the corresponding projective bundle. Note that we have the following constructions associated to  $p$ :

(i) push-forward homomorphisms  $p_*: A_k(\mathbb{P}(F)) \to A_k(X)$  since  $p$  is proper (see corollary 9.2.12),
(ii) pull-back homomorphisms  $p^*: A_k(X) \to A_{k + r - 1}(\mathbb{P}(F))$  by lemma 10.1.7,
(iii) a line bundle  $O_{\mathbb{P}(F)}(1)$  on  $\mathbb{P}(F)$  by example 10.1.4 (the dual of the tautological subbundle).

We can now combine these three operations to get homomorphisms of the Chow groups of  $X$  that depend on the vector bundle  $F$ :

Definition 10.2.1. Let  $X$  be a scheme, and let  $F$  be a vector bundle of rank  $r$  on  $X$ . Let  $p: \mathbb{P}(F) \to X$  be the projection map from the associated projective bundle. Assume for simplicity that  $X$  (and hence  $\mathbb{P}(F)$ ) is irreducible (see below), so that the line bundle  $O_{\mathbb{P}(F)}(1)$  corresponds to a Cartier divisor  $D_F$  on  $\mathbb{P}(F)$ . Now for all  $i \geq -r + 1$  we define Segre class homomorphisms by the formula

$$
s _ {i} (F): A _ {k} (X) \to A _ {k - i} (X), \qquad \alpha \mapsto s _ {i} (F) \cdot \alpha := p _ {*} (D _ {F} ^ {r - 1 + i} \cdot p ^ {*} \alpha).
$$

Remark 10.2.2. We will discuss some geometric interpretations of Segre classes (or rather some combinations of them) later in proposition 10.2.3 (i) and (ii), proposition 10.3.12, and remark 10.3.14. For the moment let us just note that every vector bundle  $F$  gives rise to these homomorphisms  $s_i(F)$  that look like intersections (hence the notation  $s_i(F) \cdot \alpha$ ) with

---

Andreas Gathmann

some object of codimension  $i$  as they decrease the dimension of cycles by  $i$ . (In algebraic topology the Segre class  $s_i(F)$  is an object in the cohomology group  $H^{2i}(X,\mathbb{Z})$ .)

Note also that the condition that  $X$  be irreducible is not really necessary: even if  $\mathcal{O}_{\mathbb{P}(F)}(1)$  does not determine a Cartier divisor on  $\mathbb{P}(F)$  it does so on every subvariety of  $\mathbb{P}(F)$ , and this is all we need for the construction of the intersection product (as we intersect with a cycle in  $\mathbb{P}(F)$  which is by definition a formal linear combination of subvarieties).

Proposition 10.2.3. Let  $X$  and  $Y$  be schemes.

(i) For any vector bundle  $F$  on  $X$  we have

$s_i(F) = 0$  for  $i &lt;   0$
$s_0(F) = \mathrm{id}$

(ii) For any line bundle  $L$  on  $X$  we have  $s_i(L) \cdot \alpha = (-1)^i D^i \cdot \alpha$  for  $i \geq 0$  and all  $\alpha \in A_*(X)$ , where  $D$  is the Cartier divisor class associated to the line bundle  $L$ .

(iii) (Commutativity) If  $F_{1}$  and  $F_{2}$  are vector bundles on  $X$ , then

$$
s _ {i} \left(F _ {1}\right) \cdot s _ {j} \left(F _ {2}\right) = s _ {j} \left(F _ {2}\right) \cdot s _ {i} \left(F _ {1}\right)
$$

as homomorphisms  $A_{k}(X) \to A_{k - i - j}(X)$  for all  $i, j$  (where the dot denotes the composition of the two homomorphisms).

(iv) (Projection formula) If  $f: X \to Y$  is proper,  $F$  is a vector bundle on  $Y$ , and  $\alpha \in A_{*}(X)$ , then

$$
f _ {*} \left(s _ {i} \left(f ^ {*} F\right) \cdot \alpha\right) = s _ {i} (F) \cdot f _ {*} \alpha .
$$

(v) (Compatibility with pull-back) If  $f: X \to Y$  is a morphism for which a pull-back  $f^{*}: A_{*}(Y) \to A_{*}(X)$  exists (see remark 10.1.8),  $F$  is a vector bundle on  $Y$ , and  $\alpha \in A_{*}(Y)$ , then

$$
s _ {i} \left(f ^ {*} F\right) \cdot f ^ {*} \alpha = f ^ {*} \left(s _ {i} (F) \cdot \alpha\right).
$$

Proof. (i): Let  $V \subset X$  be a  $k$ -dimensional subvariety. By construction we can represent  $s_i(F) \cdot [V]$  by a cycle of dimension  $k - i$  supported in  $V$ . As  $Z_{k - i}(V) = 0$  for  $i &lt; 0$  and  $Z_k(V) = [V]$  we conclude that  $s_i(F) = 0$  for  $i &lt; 0$  and  $s_0(F) \cdot [V] = n \cdot [V]$  for some  $n \in \mathbb{Z}$ . The computation of the multiplicity  $n$  is a local calculation, so we can replace  $X$  by an open subset and thus assume that  $F$  is a trivial bundle. In this case  $\mathbb{P}(F) = X \times \mathbb{P}^{r - 1}$  and  $D_F$  is a hyperplane in  $\mathbb{P}^{r - 1}$ . So  $D_F^{r - 1}$  is a point in  $\mathbb{P}^{r - 1}$ , i.e.  $D_F^{r - 1} \cdot p^*[V] = [V \times \{\mathrm{pt}\}]$  and hence  $s_0(F) \cdot [V] = [V]$ .

(ii): If  $L$  is a line bundle then  $\mathbb{P}(L) = X$  and  $p$  is the identity. Hence the statement follows from the identity  $\mathcal{O}_{\mathbb{P}(L)}(-1) = L$ .

The proofs of (iii), (iv), and (v) all follow from the various compatibilities between push-forward, pull-back, and intersection products. As an example we give the proof of (iv), see [F] proposition 3.1 for the other proofs.

For (iv) consider the fiber square

![img-1.jpeg](images/img-1.jpeg)

---

10. Chern classes

and denote the Cartier divisors associated to the line bundles  $\mathcal{O}_{\mathbb{P}(F)}(1)$  and  $\mathcal{O}_{\mathbb{P}(f^* F)}(1)$  by  $D_F$  and  $D_F'$ , respectively. Then

$$
\begin{array}{l} f _ {*} \left(s _ {i} \left(f ^ {*} F\right) \cdot \alpha\right) = f _ {*} p _ {*} ^ {\prime} \left(D _ {F} ^ {\prime} ^ {r - 1 + i} \cdot p ^ {\prime *} \alpha\right) \quad \text {by definition 10.2.1} \\ = p _ {*} f _ {*} ^ {\prime} \left(D _ {F} ^ {\prime} ^ {r - i + 1} \cdot p ^ {\prime *} \alpha\right) \quad \text {by remark 9.2.10} \\ = p _ {*} f _ {*} ^ {\prime} \left(\left(f ^ {\prime *} D _ {F}\right) ^ {r - i + 1} \cdot p ^ {\prime *} \alpha\right) \quad \text {as} D _ {F} ^ {\prime} = f ^ {\prime *} D _ {F} \\ = p _ {*} \left(D _ {F} ^ {r - i + 1} \cdot f _ {*} ^ {\prime} p ^ {\prime *} \alpha\right) \quad \text {by lemma 9.4.10} \\ = p _ {*} \left(D _ {F} ^ {r - i + 1} \cdot p ^ {*} f _ {*} \alpha\right) \quad \text {by lemma 10.1.7 (i)} \\ = s _ {i} (E) \cdot f _ {*} \alpha \quad \text {by definition 10.2.1}. \\ \end{array}
$$

□

Corollary 10.2.4. Let  $F$  be a vector bundle on a scheme  $X$ , and let  $p: \mathbb{P}(F) \to X$  be the projection. Then  $p_*: A_*(\mathbb{P}(F)) \to A_*(X)$  is surjective and  $p^*: A_*(X) \to A_*(\mathbb{P}(F))$  is injective.

Proof. By proposition 10.2.3 (i) we have

$$
\alpha = s _ {0} (F) \cdot \alpha = p _ {*} \left(D _ {F} ^ {r - 1} \cdot p ^ {*} \alpha\right)
$$

for all  $\alpha \in A_{*}(X)$ , so  $p_*$  is surjective. The same formula shows that  $\alpha = 0$  if  $p^*\alpha = 0$ , so  $p^*$  is injective.

By proposition 10.2.3 (iii) any polynomial expression in the Segre classes of some vector bundles acts on the Chow groups of  $X$ . Although the Segre classes are the characteristic classes of vector bundles that are the easiest ones to define, some others that are polynomial combinations of them have nicer properties and better geometric interpretations. Let us now define these combinations.

Definition 10.2.5. Let  $X$  be a scheme, and let  $F$  be a vector bundle of rank  $r$  on  $X$ . The total Segre class of  $F$  is defined to be the formal sum

$$
s (F) = \sum_ {i \geq 0} s _ {i} (F): A _ {*} (X) \to A _ {*} (X).
$$

Note that:

(i) All  $s_i(F)$  can be recovered from the homomorphism  $s(F)$  by considering the graded parts.
(ii) Although the sum over  $i$  in  $s(F)$  is formally infinite, it has of course only finitely many terms as  $A_{k}(X)$  is non-zero only for finitely many  $k$ .
(iii) The homomorphism  $s(F)$  is in fact an isomorphism of vector spaces: by proposition 10.2.3 (i) it is given by a triangular matrix with ones on the diagonal (in the natural grading of  $A_{*}(X)$ ).

By (iii) it makes sense to define the total Chern class of  $F$

$$
c (F) = \sum_ {i \geq 0} c _ {i} (F)
$$

to be the inverse homomorphism of  $s(F)$ . In other words, the Chern classes  $c_{i}(F)$  are the unique homomorphisms  $c_{i}(F): A_{k}(X) \to A_{k - i}(X)$  such that

$$
s (F) \cdot c (F) = (1 + s _ {1} (F) + s _ {2} (F) + \dots) \cdot (c _ {0} (F) + c _ {1} (F) + c _ {2} (F) + \dots) = \mathrm {i d}.
$$

---

Andreas Gathmann

Explicitly, the first few Chern classes are given by

$$
\begin{array}{l}
c_{0}(F) = 1, \\
c_{1}(F) = -s_{1}(F), \\
c_{2}(F) = -s_{2}(F) + s_{1}(F)^{2}, \\
c_{3}(F) = -s_{3}(F) + 2s_{1}(F)s_{2}(F) - s_{1}(F)^{3}.
\end{array}
$$

Proposition 10.2.3 translates directly into corresponding statements about Chern classes:

**Proposition 10.2.6.** Let $X$ and $Y$ be schemes.

(i) For any line bundle $L$ on $X$ with associated Cartier divisor class $D$ we have $c(L) \cdot \alpha = (1 + D) \cdot \alpha$. In other words, $c_{i}(L) = 0$ for $i &gt; 1$, and $c_{1}(L)$ is the homomorphism of intersection with the Cartier divisor class associated to $L$. By abuse of notation, the Cartier divisor class associated to $L$ is often also denoted $c_{1}(L)$.

(ii) (Commutativity) If $F_{1}$ and $F_{2}$ are vector bundles on $X$, then

$$
c_{i}(F_{1}) \cdot c_{j}(F_{2}) = c_{j}(F_{2}) \cdot c_{i}(F_{1})
$$

for all $i,j$.

(iii) (Projection formula) If $f: X \to Y$ is proper, $F$ is a vector bundle on $Y$, and $\alpha \in A_{*}(X)$, then

$$
f_{*}(c_{i}(f^{*}F) \cdot \alpha) = c_{i}(F) \cdot f_{*}\alpha.
$$

(iv) (Pull-back) If $f: X \to Y$ is a morphism for which a pull-back $f^{*}: A_{*}(Y) \to A_{*}(X)$ exists, $F$ is a vector bundle on $Y$, and $\alpha \in A_{*}(Y)$, then

$$
c_{i}(f^{*}F) \cdot f^{*}\alpha = f^{*}(c_{i}(F) \cdot \alpha).
$$

**Proof.** (i): This follows from proposition 10.2.3, since

$$
(1 - D + D^{2} - D^{3} \pm \cdots)(1 + D) = 1.
$$

(ii), (iii), (iv): All these statements follow from the corresponding properties of Segre classes in proposition 10.2.3, taking into account that the Chern classes are just polynomials in the Segre classes.

10.3. **Properties of Chern classes.** In this section we will show how to compute the Chern classes of almost any bundle that is constructed from other known bundles in some way (e.g. by means of direct sums, tensor products, dualizing, exact sequences, symmetric and exterior products). We will also discuss the geometric meaning of Chern classes.

The most important property of Chern classes is that they are multiplicative in exact sequences:

**Proposition 10.3.1.** Let $0 \to F' \to F \to F'' \to 0$ be an exact sequence of vector bundles on a scheme $X$. Then $c(F) = c(F') \cdot c(F'')$.

**Proof.** We prove the statement by induction on the rank of $F''$.

**Step 1:** $\operatorname{rank} F'' = 1$. We have to show that $s(F') \cdot [V] = c(F'') \cdot s(F) \cdot [V]$ for all $k$-dimensional subvarieties $V \subset X$. Consider the diagram

$$
P' = \mathbb{P}(F'|_{V}) \xrightarrow[i]{\text{ } } \mathbb{P}(F|_{V}) = P
$$

![img-2.jpeg](images/img-2.jpeg)

---

10. Chern classes

Then

$$
\begin{array}{l} c \left(F ^ {\prime \prime}\right) \cdot s (F) \cdot [ V ] = c \left(F ^ {\prime \prime}\right) \cdot p _ {*} \left(\left(1 + D _ {F} + D _ {F} ^ {2} + \dots\right) \cdot [ P ]\right) \quad \text {b y} \\ = c \left(F ^ {\prime \prime}\right) \cdot p _ {*} \left(s \left(O _ {P} (- 1)\right) \cdot [ P ]\right) \quad \text {b y} \\ = \left(1 + c _ {1} \left(F ^ {\prime \prime}\right)\right) \cdot p _ {*} \left(s \left(O _ {P} (- 1)\right) \cdot [ P ]\right) \quad \text {b y} \\ = p _ {*} \left(\left(1 + c _ {1} \left(p ^ {*} F ^ {\prime \prime}\right)\right) \cdot s \left(O _ {P} (- 1)\right) \cdot [ P ]\right) \quad \text {b y} \\ \end{array}
$$

On the other hand, we have a bundle map  $\mathcal{O}_P(-1) \hookrightarrow p^*F \to p^*F''$  on  $P$ , which by construction fails to be injective exactly at the points of  $P'$ . In other words,  $P'$  in  $P$  is the (scheme-theoretic) zero locus of a section of the line bundle  $p^*F'' \otimes \mathcal{O}_P(-1)^\vee$ . So we get

$$
\begin{array}{l} s \left(F ^ {\prime}\right) \cdot [ V ] = p _ {*} ^ {\prime} \left(s \left(O _ {P ^ {\prime}} (- 1)\right) \cdot \left[ P ^ {\prime} \right]\right) \\ = p _ {*} i _ {*} \left(s \left(i ^ {*} O _ {P} (- 1)\right) \cdot \left[ P ^ {\prime} \right]\right) \\ = p _ {*} \left(s \left(O _ {P} (- 1)\right) \cdot i _ {*} \left[ P ^ {\prime} \right]\right) \\ = p _ {*} \left(s \left(O _ {P} (- 1)\right) \cdot \left(c _ {1} \left(p ^ {*} F ^ {\prime \prime}\right) - c _ {1} \left(O _ {P} (- 1)\right)\right) \cdot [ P ]\right). \\ \end{array}
$$

Subtracting these two equations from each other, we get

$$
c \left(F ^ {\prime \prime}\right) \cdot s (F) \cdot [ V ] - s \left(F ^ {\prime}\right) \cdot [ V ] = p _ {*} \left(s \left(O _ {P} (- 1)\right) c \left(O _ {P} (- 1)\right) [ P ]\right) = p _ {*} [ P ] = 0
$$

for dimensional reasons.

Step 2:  $\mathrm{rank}F^{\prime \prime} &gt; 1$ . Let  $Q = \mathbb{P}(F^{\prime \prime \vee})$  with projection map  $q:Q\to X$ , and let  $L^{\vee}\subset q^{*}F^{\prime \prime \vee}$  be the universal line bundle. Then we get a commutative diagram of vector bundles on  $Q$  with exact rows and columns

![img-3.jpeg](images/img-3.jpeg)

for some vector bundles  $\tilde{F}$  and  $\tilde{F}''$  on  $Q$  with  $\mathrm{rank}\tilde{F}'' = \mathrm{rank}F'' - 1$ . Recall that we want to prove the statement that for any short exact sequence of vector bundles the Chern polynomial of the bundle in the middle is equal to the product of the Chern polynomials of the other two bundles. In the above diagram we know that this is true for the columns by step 1 and for the top row by the inductive assumption; hence it must be true for the bottom row as well. So we have shown that

$$
c \left(q ^ {*} F\right) = c \left(q ^ {*} F ^ {\prime}\right) \cdot c \left(q ^ {*} F ^ {\prime \prime}\right).
$$

It follows that

$$
q ^ {*} c (F) = q ^ {*} \left(c \left(F ^ {\prime}\right) \cdot c \left(F ^ {\prime \prime}\right)\right)
$$

by proposition 10.2.6 (iv), and finally that

$$
c (F) = c \left(F ^ {\prime}\right) \cdot c \left(F ^ {\prime \prime}\right)
$$

as  $q^{*}$  is injective by corollary 10.2.4.

Remark 10.3.2. Of course proposition 10.3.1 can be split up into graded parts to obtain the equations

$$
c _ {k} (F) = \sum_ {i + j = k} c _ {i} \left(F ^ {\prime}\right) \cdot c _ {j} \left(F ^ {\prime \prime}\right)
$$

---

for all $k\geq 0$ and any exact sequence $0\to F^{\prime}\to F\to F^{\prime\prime}\to 0$ of vector bundles on a scheme $X$.

Note moreover that by definition the same relation $s(F)=s(F^{\prime})\cdot s(F^{\prime\prime})$ then holds for the Segre classes.

###### Example 10.3.3.

In this example we will compute the Chern classes of the tangent bundle $T_{X}$ of $X=\mathbb{P}^{n}$. By lemma 7.4.15 we have an exact sequence of vector bundles on $X$

$0\to\mathcal{O}_{X}\to\mathcal{O}_{X}(1)^{\oplus(n+1)}\to T_{X}\to 0.$

Moreover proposition 10.2.6 (i) implies that $c(\mathcal{O}_{X})=1$ and $c(\mathcal{O}_{X}(1))=1+H$, where $H$ is (the divisor class of) a hyperplane in $X$. So by proposition 10.3.1 it follows that

$c(T_{X})=c(\mathcal{O}_{X}(1))^{n+1}/c(\mathcal{O}_{X})=(1+H)^{n+1},$

i. e. $c_{k}(T_{X})=\binom{n+1}{k}\cdot H^{k}$ (where $H^{k}$ is the class of a linear subspace of $X$ of codimension $k$).

###### Remark 10.3.4.

Note that proposition 10.3.1 allows us to compute the Chern classes of any bundle $F$ of rank $r$ on a scheme $X$ that has a filtration

$0=F_{0}\subset F_{1}\subset\cdots\subset F_{r-1}\subset F_{r}=F$

by vector bundles such that the quotients $L_{i}:=F_{i}/F_{i-1}$ are all line bundles (i. e. $F_{i}$ has rank $i$ for all $i$). In fact, in this case a recursive application of proposition 10.3.1 to the exact sequences

$0\to F_{i-1}\to F_{i}\to L_{i}\to 0$

yields (together with proposition 10.2.6 (i))

$c(F)=\prod_{i=1}^{r}(1+D_{i})$

where $D_{i}=c_{1}(L_{i})$ is the divisor associated to the line bundle $L_{i}$.

Unfortunately, not every vector bundle admits such a filtration. We will see now however that for computations with Chern classes we can essentially pretend that such a filtration always exists.

###### Lemma 10.3.5.

(Splitting construction) Let $F$ be a vector bundle of rank $r$ on a scheme $X$. Then there is a scheme $Y$ and a morphism $f:Y\to X$ such that

1. $f$ admits push-forwards and pull-backs for Chow groups (in fact it will be an iterated projective bundle),
2. the push-forward $f_{*}$ is surjective,
3. the pull-back $f^{*}$ is injective,
4. $f^{*}F$ has a filtration by vector bundles

$0=F_{0}\subset F_{1}\subset\cdots\subset F_{r-1}\subset F_{r}=f^{*}F$

such that the quotients $F_{i}/F_{i-1}$ are line bundles on $Y$.

In other words, “every vector bundle admits a filtration after pulling back to an iterated projective bundle”.

###### Proof.

We construct the morphism $f$ by induction on $\operatorname{rank}F$. There is nothing to do if $\operatorname{rank}F=1$. Otherwise set $Y^{\prime}=\mathbb{P}(F^{\vee})$ and let $f^{\prime}:Y^{\prime}\to X$ be the projection. Let $L^{\vee}\subset f^{\prime}*F^{\vee}$ be the tautological line bundle on $Y^{\prime}$. Then we have an exact sequence of vector bundles $0\to\tilde{F}\to f^{\prime}*F\to L\to 0$ on $Y^{\prime}$, where $\operatorname{rank}\tilde{F}=\operatorname{rank}F-1$. Hence by the inductive assumption there is a morphism $f^{\prime\prime}:Y\to Y^{\prime}$ such that $f^{\prime\prime}*\tilde{F}$ has a filtration $(F_{i})$ with line bundle quotients. If we set $f=f^{\prime}\circ f^{\prime\prime}$ it follows that we have an induced filtration of $f^{*}F$ on $Y$

$0=F_{0}\subset F_{1}\subset\cdots\subset F_{r-1}=f^{\prime\prime}*\tilde{F}\subset f^{*}F$

---

10. Chern classes

with line bundle quotients. Moreover, $f_{*}$ is surjective and $f^{*}$ is injective, as this is true for $f^{\prime \prime}$ by the inductive assumption and for $f^{\prime}$ by corollary 10.2.4. $\square$

###### Construction 10.3.6.

(Splitting construction) Suppose one wants to prove a universal identity among Chern classes of vector bundles on a scheme $X$, e. g. the statement that $c_{i}(F)=0$ whenever $i&gt;\operatorname{rank}F$ (see corollary 10.3.7 below). If the identity is invariant under pull-backs (which it essentially always is because of proposition 10.2.6 (iv)) then one can assume that the vector bundles in question have filtrations with line bundle quotients. More precisely, pick a morphism $f:Y\to X$ as in lemma 10.3.5. We can then show the identity for the pulled-back bundle $f^{*}F$ on $Y$, using the filtration. As the pull-back $f^{*}$ is injective and commutes with the identity we want to show, the identity then follows for $F$ on $X$ as well. (This is the same argument that we used already at the end of the proof of proposition 10.3.1.)

###### Corollary 10.3.7.

Let $F$ be a vector bundle of rank $r$ on a scheme $X$. Then $c_{i}(F)=0$ for all $i&gt;r$.

###### Proof.

By the splitting construction 10.3.6 we can assume that $F$ has a filtration with line bundle quotients $L_{i}$, $i=1,\ldots,r$. But then $c(F)=\prod_{i=1}^{r}(1+c_{1}(L_{i}))$ by remark 10.3.4, which obviously has no parts of degree bigger than $r$. $\square$

###### Remark 10.3.8.

This vanishing of Chern classes beyond the rank of the bundle is a property that is not shared by the Segre classes (see e. g. proposition 10.2.3 (ii)). This is one reason why Chern classes are usually preferred over Segre classes in computations (although they carry the same information).

###### Remark 10.3.9.

The splitting construction is usually formalized as follows. Let $F$ be a vector bundle of rank $r$ on a scheme $X$. We write formally

$c(F)=\prod_{i=1}^{r}(1+\alpha_{i}).$

There are two ways to think of the $\alpha_{1},\ldots,\alpha_{r}$:

- The $\alpha_{i}$ are just formal “variables” such that the $k$-th elementary symmetric polynomial in the $\alpha_{i}$ is exactly $c_{k}(F)$. So any symmetric polynomial in the $\alpha_{i}$ is expressible as a polynomial in the Chern classes of $F$ in a unique way.
- After having applied the splitting construction, the vector bundle $F$ has a filtration with line bundle quotients $L_{i}$. Then we can set $\alpha_{i}=c_{1}(L_{i})$, and the decomposition $c(F)=\prod_{i=1}^{r}(1+\alpha_{i})$ becomes an actual equation (and not just a formal one).

The $\alpha_{i}$ are usually called the Chern roots of $F$. Using the splitting construction and Chern roots, one can compute the Chern classes of almost any bundle that is constructed from other known bundles by standard operations:

###### Proposition 10.3.10.

Let $X$ be a scheme, and let $F$ and $F^{\prime}$ be vector bundles with Chern roots $(\alpha_{i})_{i}$ and $(\alpha_{j}^{\prime})_{j}$, respectively. Then:

1. $F^{\vee}$ has Chern roots $(-\alpha_{i})_{i}$.
2. $F\otimes F^{\prime}$ has Chern roots $(\alpha_{i}+\alpha_{j}^{\prime})_{i,j}$.
3. $S^{k}F$ has Chern roots $(\alpha_{i_{1}}+\cdots+\alpha_{i_{k}})_{i_{1}\leq\cdots\leq i_{k}}$.
4. $\Lambda^{k}F$ has Chern roots $(\alpha_{i_{1}}+\cdots+\alpha_{i_{k}})_{i_{1}&lt;\cdots&lt;i_{k}}$.

###### Proof.

(i): If $F$ has a filtration $0=F_{0}\subset F_{1}\subset\cdots\subset F_{r}=F$ with line bundle quotients $L_{i}=F_{i}/F_{i-1}$, then $F^{\vee}$ has an induced filtration $0=(F/F_{r})^{\vee}\subset(F/F_{r-1})^{\vee}\subset\cdots\subset(F/F_{0})^{\vee}=F^{\vee}$ with line bundle quotients $L_{i}^{\vee}$.

(ii): If $F$ and $F^{\prime}$ have filtrations

$0=F_{0}\subset F_{1}\subset\cdots\subset F_{r}=F\quad\text{and}\quad 0=F_{0}^{\prime}\subset F_{1}^{\prime}\subset\cdots\subset F_{s}^{\prime}=F^{\prime}$

---

Andreas Gathmann

with line bundle quotients $L_{i}:=F_{i}/F_{i-1}$ and $L_{i}^{\prime}:=F_{i}^{\prime}/F_{i-1}^{\prime}$, then $F\otimes F^{\prime}$ has a filtration

$0=F_{0}\otimes F^{\prime}\subset F_{1}\otimes F^{\prime}\subset\cdots\subset F_{r}\otimes F^{\prime}=F\otimes F^{\prime}$

with quotients $L_{i}\otimes F^{\prime}$. But $L_{i}\otimes F^{\prime}$ itself has a filtration

$0=L_{i}\otimes F_{0}^{\prime}\subset L_{i}\otimes F_{1}^{\prime}\subset\cdots\subset L_{i}\otimes F_{s}^{\prime}=L_{i}\otimes F^{\prime}$

with quotients $L_{i}\otimes L_{j}^{\prime}$, so the result follows.

(iii) and (iv) follow in the same way. $\square$

###### Example 10.3.11.

The results of proposition 10.3.10 can be restated using Chern classes instead of Chern roots. For example, (i) just says that $c_{i}(F^{\vee})=(-1)^{i}c_{i}(F)$. It is more difficult to write down closed forms for the Chern classes in the cases (ii) to (iv). For example, if $F^{\prime}=L$ is a line bundle, then

$c(F\otimes L)=\prod_{i}(1+(\alpha_{i}+\alpha^{\prime}))=\sum_{i}(1+c_{1}(L))^{r-i}c_{i}(F)$

where $r=\operatorname{rank}F$. So for $0\leq p\leq r$ we have

$c_{p}(F\otimes L)=\sum_{i=0}^{p}{r-i\choose p-i}c_{i}(F)\,c_{1}(L)^{p-i}.$

Also, from part (iv) it follows immediately that $c_{1}(F)=c_{1}(\Lambda^{r}F)$.

As a more complicated example, assume that $F$ is a rank-2 bundle on a scheme $X$ and let us compute the Chern classes of $S^{3}F$. Say $F$ has Chern roots $\alpha_{1}$ and $\alpha_{2}$, so that $c_{1}(F)=\alpha_{1}+\alpha_{2}$ and $c_{2}(F)=\alpha_{1}\alpha_{2}$. Then by part (iii) a tedious but easy computation shows that

$c(S^{3}F)$ $=(1+3\alpha_{1})(1+2\alpha_{1}+\alpha_{2})(1+\alpha_{1}+2\alpha_{2})(1+3\alpha_{2})$
$=1+6c_{1}(F)+10c_{2}(F)+11c_{1}(F)^{2}+30c_{1}(F)c_{2}(F)$
$\quad+6c_{1}(F)^{3}+9c_{2}(F)^{2}+18c_{1}(F)^{2}c_{2}(F).$

Splitting this up into graded pieces one obtains the individual Chern classes, e. g.

$c_{4}(S^{3}F)=9c_{2}(F)^{2}+18c_{1}(F)^{2}c_{2}(F).$

Now that we have shown how to compute Chern classes let us discuss their geometric meaning. By far the most important property of Chern classes is that the “top Chern class” of a vector bundle (i. e. $c_{r}(F)$ if $r=\operatorname{rank}F$) is the class of the zero locus of a section:

###### Proposition 10.3.12.

Let $F$ be a vector bundle of rank $r$ on an $n$-dimensional scheme $X$. Let $s\in\Gamma(F)$ be a global section of $F$, and assume that its scheme-theoretic zero locus $Z(s)$ has dimension $n-r$ (as expected). Then $[Z(s)]=c_{r}(F)\cdot[X]\in A_{n-r}(X)$.

###### Proof.

We will only sketch the proof; for details especially about multiplicities we refer to *[x10]* section 14.1.

We prove the statement by induction on $r$. Applying the splitting principle we may assume that there is an exact sequence

$0\to F^{\prime}\to F\to L\to 0$ ($\ast$)

of vector bundles on $X$, where $L$ is a line bundle and $\operatorname{rank}F^{\prime}=\operatorname{rank}F-1$. Now let $s\in\Gamma(X,F)$ be a global section of $F$ as in the proposition. Then $s$ induces

- a section $l\in\Gamma(X,L)$, and
- a section $s^{\prime}\in\Gamma(Z(l),F^{\prime})$ (i. e. “$s$ is a section of $F^{\prime}$ on the locus where the induced section on $L$ vanishes”).

---

10. Chern classes

Let us assume that $l$ is not identically zero, and denote by $i:Z(l)\hookrightarrow X$ the inclusion morphism. Note that then $i_{*}[Z(s^{\prime})]=c_{r-1}(F)\cdot[Z(l)]$ by the induction hypothesis, and $[Z(l)]=c_{1}(L)\cdot[X]$ as the Weil divisor associated to a line bundle is just the zero locus of a section. Combining these results we get

$[Z(s)]=i_{*}[Z(s^{\prime})]=c_{r-1}(F)\cdot c_{1}(L)\cdot[X].$

But applying proposition 10.3.1 to the exact sequence $(*)$ we get $c_{r}(F)=c_{r-1}(F^{\prime})\cdot c_{1}(L)$, so the result follows. ∎

###### Remark 10.3.13.

Proposition 10.3.12 is the generalization of our old statement that the first Chern class of a line bundle (i. e. the divisor associated to a line bundle) is the zero locus of a (maybe rational) section of that bundle. In contrast to the line bundle case however, it is not clear that a section of the vector bundle exists that vanishes in the right codimension. This is why proposition 10.3.12 cannot be used as a definition for the top Chern class.

###### Remark 10.3.14.

There are analogous interpretations for the intermediate Chern classes $c_{k}(F)$ that we state without proof: let $F$ be a vector bundle of rank $r$ on a scheme $X$. Let $s_{1},\ldots,s_{r+1-k}$ be global sections of $X$, and assume that the (scheme-theoretic) locus $Z\subset X$ *where the sections $s_{1},\ldots,s_{r+1-k}$ are linearly dependent* has codimension $k$ in $X$ (which is the expected codimension). Then $[Z]=c_{k}(F)\cdot[X]\in A_{*}(X)$. (For a proof of this statement see *[x12]* example 14.4.1).

Two special cases of this property are easy to see however:

1. In the case $k=r$ we are reduced to proposition 10.3.12.
2. In the case $k=1$ the locus $Z$ is just the zero locus of a section of $\Lambda^{r}F$, so we have $[Z]=c_{1}(\Lambda^{r}F)=c_{1}(F)$ (the latter equality is easily checked using proposition 10.3.10 (iv)).

###### Example 10.3.15.

As an example of proposition 10.3.12 let us recalculate that there are 27 lines on a cubic surface $X$ in $\mathbb{P}^{3}$ (see section 4.5). To be more precise, we will not reprove here that the number of lines in $X$ is finite; instead we will assume that it is finite and just recalculate the number 27 under this assumption.

Let $G(1,3)$ be the 4-dimensional Grassmannian variety of lines in $\mathbb{P}^{3}$. As in construction 10.1.5 there is a *tautological rank-2 subbundle* $F$ of the trivial bundle $\mathbb{C}^{4}$ whose fiber over a point $[L]\in G(1,3)$ (where $L\subset\mathbb{P}^{3}$ is a line) is precisely the 2-dimensional subspace of $\mathbb{C}^{4}$ whose projectivization is $L$. Dualizing, we get a surjective morphism of vector bundles $(\mathbb{C}^{4})^{\vee}\to F^{\vee}$ that corresponds to restricting a linear function on $\mathbb{C}^{4}$ (or $\mathbb{P}^{3}$) to the line $L$. Taking the $d$-th symmetric power of this morphism we arrive at a surjective morphism $S^{d}(\mathbb{C}^{4})^{\vee}\to S^{d}F^{\vee}$ that corresponds to restricting a homogeneous polynomial of degree $d$ on $\mathbb{P}^{3}$ to $L$.

Now let $X=\{f=0\}$ be a cubic surface. By what we have just said the polynomial $f$ determines a section of $S^{3}F^{\vee}$ whose set of zeros in $G(1,3)$ is precisely the set of lines that lie in $X$ (i. e. the set of lines on which $f$ vanishes). So *assuming that this set is finite* we see by proposition 10.3.12 that the number of lines in the cubic surface $X$ is the degree of the cycle $c_{4}(S^{3}F^{\vee})$ on $G(1,3)$.

To compute this number note that by example 10.3.11 we have

$c_{4}(S^{3}F^{\vee})=9c_{2}(F^{\vee})^{2}+18c_{1}(F^{\vee})^{2}c_{2}(F^{\vee}),$

so that it remains to compute the numbers $c_{2}(F^{\vee})^{2}$ and $c_{1}(F^{\vee})^{2}c_{2}(F^{\vee})$. There are general rules (called “Schubert calculus”) how to compute such intersection products on Grassmannian varieties, but in this case we can also compute the result directly in a way similar to that in example 9.4.9:

1. By exactly the same reasoning as above, $c_{2}(F^{\vee})=c_{2}(S^{1}F^{\vee})$ is the locus of all lines in $\mathbb{P}^{3}$ that are contained in a given plane.

---

1. The class $c_{1}(F^{\vee})=c_{1}(\Lambda^{2}F^{\vee})$ is (by definition of the exterior product, see also remark 10.3.14) the locus of all lines $L\subset\mathbb{P}^{3}$ such that two given linear equations $f_{1},f_{2}$ on $\mathbb{P}^{4}$ become linearly dependent when restricted to the line. This means that $f_{1}|_{L}$ and $f_{2}|_{L}$ must have their zero at the same point of $L$. In other words, $L$ intersects $Z(f_{1},f_{2})$, which is a line. In summary, $c_{1}(F^{\vee})$ is just the class of lines that meet a given line in $\mathbb{P}^{3}$.

Using these descriptions we can now easily compute the required intersection products: $c_{2}(F^{\vee})^{2}$ is the number of lines that are contained in two given planes in $\mathbb{P}^{3}$, so it is 1 (the line must precisely be the intersection line of the two planes). Moreover, $c_{1}(F^{\vee})^{2}c_{2}(F^{\vee})$ is the number of lines intersecting two given lines and lying in a given plane, i. e. the number of lines through two points in a plane, which is 1.

Summarizing, we get that the number of lines on a cubic surface is

$c_{4}(S^{3}F^{\vee})=9c_{2}(F^{\vee})^{2}+18c_{1}(F^{\vee})^{2}c_{2}(F^{\vee})=9\cdot 1+18\cdot 1=27.$

###### Remark 10.3.16.

The preceding example 10.3.15 shows very well how enumerative problems can be attacked in general. By an enumerative problem we mean that we want to count the number of curves in some space with certain conditions (e. g. lines through two points, lines in a cubic surface, plane conics through 5 points, and so on). Namely:

1. Find a complete (resp. compact) “moduli space” $M$ whose points correspond to the curves one wants to study (in the above example: the Grassmannian $G(1,3)$ that parametrizes lines in $\mathbb{P}^{3}$).
2. Every condition that one imposes on the curves (passing through a point, lying in a given subvariety, …) corresponds to some intersection-theoretic cycle on $M$ — a divisor, a combination of Chern classes, or something else.
3. If the expected number of curves satisfying the given conditions is finite then the intersection product of the cycles in (ii) will have dimension 0. As $M$ is complete the degree of this zero-cycle is a well-defined integer. It is called the virtual solution to the enumerative problem. Note that this number is well-defined even if the actual number of curves satisfying the given conditions is not finite.
4. It is now a different (and usually more difficult, in any case not an intersection-theoretic) problem to figure out whether the actual number of curves satisfying the given conditions is finite or not, and if so whether they are counted in the intersection product of (iii) with the scheme-theoretic multiplicity 1. If this is the case then the solution of (iii) is said to be enumerative (and not only virtual). For example, we have shown in section 4.5 that the number 27 computed intersection-theoretically in example 10.3.15 is actually enumerative for any smooth cubic surface $X$.

### 10.4. Statement of the Hirzebruch-Riemann-Roch theorem

As a final application of Chern classes we will now state and sketch a proof of the famous Hirzebruch-Riemann-Roch theorem that is a vast and very useful generalization (yet still not the most general version) of the Riemann-Roch theorem (see section 7.7, in particular remark 7.7.7).

As usual the goal of the Riemann-Roch type theorems is to compute the dimension $h^{0}(X,\mathcal{F})$ of the space of global sections of a sheaf $\mathcal{F}$ on a scheme $X$, in the case at hand of a vector bundle on a smooth projective scheme $X$. As we have already seen in the case where $X$ is a curve and $\mathcal{F}$ a line bundle there is no easy general formula for this number unless you add some “correction term” (that was $-h^{1}(X,\mathcal{F})$ in the case of curves). The same is true in higher dimensions. Here the Riemann-Roch theorem will compute the Euler characteristic of $\mathcal{F}$:

###### Definition 10.4.1.

Let $\mathcal{F}$ be a coherent sheaf on a projective scheme $X$. Then the dimensions $h^{i}(X,\mathcal{F})=\dim H^{i}(X,\mathcal{F})$ are all finite by theorem 8.4.7 (i). We define the Euler

---

characteristic of $\mathcal{F}$ to be the integer

$\chi(X,\mathcal{F}):=\sum_{i\geq 0}(-1)^{i}h^{i}(X,\mathcal{F}).$

(Note that the sum is finite as $h^{i}(X,\mathcal{F})=0$ for $i>\dim X$.)

The “left hand side” of the Hirzebruch-Riemann-Roch theorem will just be $\chi(X,\mathcal{F})$; this is the number that we want to compute. Recall that there were many “vanishing theorems”, e. g. $h^{i}(X,\mathcal{F}\otimes\mathcal{O}_{X}(d))=0$ for $i>0$ and $d\gg 0$ by theorem 8.4.7 (ii). So in the cases when such vanishing theorems apply the theorem will actually compute the desired number $h^{0}(X,\mathcal{F})$.

The “right hand side” of the Hirzebruch-Riemann-Roch theorem is an intersection-theoretic expression that is usually easy to compute. It is a certain combination of the Chern (resp. Segre) classes of the bundle $F$ (corresponding to the locally free sheaf $\mathcal{F}$) and the tangent bundle $T_{X}$ of $X$. These combinations will have rational coefficients, so we have to tensor the Chow groups with $\mathbb{Q}$ (i. e. we consider formal linear combinations of subvarieties with rational coefficients instead of integer ones).

###### Definition 10.4.2.

Let $F$ be a vector bundle of rank $r$ with Chern roots $\alpha_{1},\ldots,\alpha_{r}$ on a scheme $X$. Then we define the Chern character $\mathrm{ch}(F):A_{*}(X)\otimes\mathbb{Q}\to A_{*}(X)\otimes\mathbb{Q}$ to be

$\mathrm{ch}(F)=\sum_{i=1}^{r}\exp(\alpha_{i})$

and the Todd class $\mathrm{td}(F):A_{*}(X)\otimes\mathbb{Q}\to A_{*}(X)\otimes\mathbb{Q}$ to be

$\mathrm{td}(F)=\prod_{i=1}^{r}\frac{\alpha_{i}}{1-\exp(-\alpha_{i})},$

where the expressions in the $\alpha_{i}$ are to be understood as formal power series, i. e.

$\exp(\alpha_{i})=1+\alpha_{i}+\frac{1}{2}\alpha_{i}^{2}+\frac{1}{6}\alpha_{i}^{3}+\cdots$

and

$\frac{\alpha_{i}}{1-\exp(-\alpha_{i})}=1+\frac{1}{2}\alpha_{i}+\frac{1}{12}\alpha_{i}^{2}+\cdots.$

###### Remark 10.4.3.

As usual we can expand the definition of $\mathrm{ch}(F)$ and $\mathrm{td}(F)$ to get symmetric polynomials in the Chern roots which can then be written as polynomials (with rational coefficients) in the Chern classes $c_{i}=c_{i}(F)$ of $F$. Explicitly,

$\mathrm{ch}(F)=r+c_{1}+\frac{1}{2}(c_{1}^{2}-2c_{2})+\frac{1}{6}(c_{1}^{3}-3c_{1}c_{2}+3c_{3})+\cdots$
$\text{and}\quad\mathrm{td}(F)=1+\frac{1}{2}c_{1}+\frac{1}{12}(c_{1}^{2}+c_{2})+\frac{1}{24}c_{1}c_{2}+\cdots.$

###### Remark 10.4.4.

If $0\to F^{\prime}\to F\to F^{\prime\prime}\to 0$ is an exact sequence of vector bundles on $X$ then the Chern roots of $F$ are just the union of the Chern roots of $F^{\prime}$ and $F^{\prime\prime}$. So we see that

$\mathrm{ch}(F)=\mathrm{ch}(F^{\prime})+\mathrm{ch}(F^{\prime\prime})$

and

$\mathrm{td}(F)=\mathrm{td}(F^{\prime})\cdot\mathrm{td}(F^{\prime\prime}).$

We can now state the Hirzebruch-Riemann-Roch theorem:

###### Theorem 10.4.5.

(Hirzebruch-Riemann-Roch theorem) Let $F$ be a vector bundle on a smooth projective variety $X$. Then

$\chi(X,F)=\deg(\mathrm{ch}(F)\cdot\mathrm{td}(T_{X}))$

where $\deg(\alpha)$ denotes the degree of the dimension-0 part of the (non-homogeneous) cycle $\alpha$.

---

Before we sketch a proof of this theorem in the next section let us consider some examples.

###### Example 10.4.6.

Let $F=L$ be a line bundle on a smooth projective curve $X$ of genus $g$. Then $\chi(X,L)=h^{0}(X,L)-h^{1}(X,L)$. On the right hand side, the dimension-0 part of $\mathrm{ch}(L)\cdot\mathrm{td}(T_{X})$, i. e. its codimension-1 part, is equal to

$\deg(\mathrm{ch}(L)\cdot\mathrm{td}(T_{X}))$ $=\deg((1+c_{1}(L))(1+\tfrac{1}{2}c_{1}(T_{X})))\qquad\text{ by remark 10.4.3}$
$=\deg(c_{1}(L)-\tfrac{1}{2}c_{1}(\Omega_{X}))$
$=\deg L-\tfrac{1}{2}(2g-2)\qquad$ $\text{ by corollary 7.6.6}$
$=\deg L+1-g,$

so we are recovering our earlier Riemann-Roch theorem of corollary 8.3.3.

###### Example 10.4.7.

If $F$ is a vector bundle of rank $r$ on a smooth projective curve $X$ then we get in the same way

$h^{0}(X,F)-h^{1}(X,F)$ $=\deg(\mathrm{ch}(F)\cdot\mathrm{td}(T_{X}))$
$=\deg((r+c_{1}(F))(1+\frac{1}{2}c_{1}(T_{X})))$
$=\deg c_{1}(F)+r(1-g).$

###### Example 10.4.8.

Let $L=\mathcal{O}_{X}(D)$ be a line bundle on a smooth projective surface $X$ corresponding to a divisor $D$. Now the dimension-0 part of the right hand side has codimension 2, so the Hirzebruch-Riemann-Roch theorem states that

$h^{0}(X,L)$ $-h^{1}(X,L)+h^{2}(X,L)$
$=\deg(\mathrm{ch}(F)\cdot\mathrm{td}(T_{X}))$
$=\deg\left(\left(1+c_{1}(L)+\frac{1}{2}c_{1}(L)^{2}\right)\left(1+\frac{1}{2}c_{1}(T_{X})+\frac{1}{12}(c_{1}(T_{X})^{2}+c_{2}(T_{X}))\right)\right)$
$=\frac{1}{2}D\cdot(D-K_{X})+\frac{K_{X}^{2}+c_{2}(T_{X})}{12}.$

Note that:

1. The number $\chi(X,\mathcal{O}_{X})=\frac{K_{X}^{2}+c_{2}(T_{X})}{12}$ is an invariant of $X$ that does not depend on the line bundle. The Hirzebruch-Riemann-Roch theorem implies that it is always an integer, i. e. that $K_{X}^{2}+c_{2}(T_{X})$ is divisible by 12 (which is not at all obvious from the definitions).
2. If $X$ has degree $d$ and $L=\mathcal{O}_{X}(n)$ for $n\gg 0$ then $h^{1}(X,L)=h^{2}(X,L)=0$ by theorem 8.4.7 (ii). Moreover we then have $D^{2}=dn^{2}$, so we get

$h^{0}(X,\mathcal{O}_{X}(n))=\frac{d}{2}n^{2}+\frac{1}{2}(H\cdot K_{X})\cdot n+\frac{K_{X}^{2}+c_{2}(T_{X})}{12}$

where $H$ denotes the class of a hyperplane (restricted to $X$). In other words, we have just recovered proposition 6.1.5 about the Hilbert function of $X$. Moreover, we have identified the non-leading coefficients of the Hilbert polynomial in terms of intersection-theoretic data.

###### Example 10.4.9.

The computation of example 10.4.8 works for higher-dimensional varieties as well: let $X$ be a smooth projective $N$-dimensional variety of degree $d$ and consider the line bundle $L=\mathcal{O}_{X}(n)$ on $X$ for $n\gg 0$. We see immediately that the codimension-$N$ part of $\mathrm{ch}(\mathcal{O}_{X}(n))\cdot\mathrm{td}(T_{X})$ is a polynomial in $n$ of degree $N$ with leading coefficient

$\frac{1}{N!}c_{1}(L)^{N}=\frac{d}{N!}n^{N},$

---

which reproves proposition 6.1.5 (for smooth $X$). Moreover, we can identify the other coefficients of the Hilbert polynomial in terms of intersection-theoretic expressions involving the characteristic classes of the tangent bundle of $X$.

###### Example 10.4.10.

Let $F=\mathcal{O}_{X}(d)$ be a line bundle on $X=\mathbb{P}^{n}$. Then we can compute both sides of the Hirzebruch-Riemann-Roch theorem explicitly and therefore prove the theorem in this case:

As for the left hand side, proposition 8.4.1 implies that

\[ \chi(X,\mathcal{O}_{X}(d))=\begin{cases}h^{0}(X,\mathcal{O}_{X}(d))=\binom{n+d}{n}&\text{if }d\geq 0,\\
(-1)^{n}h^{n}(X,\mathcal{O}_{X}(d))=(-1)^{n}\binom{-d-1}{n}&\text{if }d\leq-n-1,\\
0&\text{otherwise}.\end{cases} \]

Note that this means in fact in all cases that

$\chi(X,\mathcal{O}_{X}(d))=\binom{n+d}{n}.$

As for the right hand side let us first compute the Todd class of $T_{X}$. By the Euler sequence

$0\to\mathcal{O}_{X}\to\mathcal{O}_{X}(1)^{\oplus(n+1)}\to T_{X}\to 0$

of lemma 7.4.15 together with the multiplicativity of Chern classes (see proposition 10.3.1) we see that the Chern classes (and hence the Todd class) of $T_{X}$ are the same as those of $\mathcal{O}_{X}(1)^{\oplus(n+1)}$. But the Chern roots of the latter bundle are just $n+1$ times the class $H$ of a hyperplane, so it follows that

$\operatorname{td}(T_{X})=\frac{H^{n+1}}{(1-\exp(-H))^{n+1}}.$

As the Chern character of $\mathcal{O}_{X}(d)$ is obviously $\exp(dH)$ we conclude that the right hand side of the Hirzebruch-Riemann-Roch theorem is the $H^{n}$-coefficient of

$\frac{H^{n+1}\exp(dH)}{(1-\exp(-H))^{n+1}}.$

But this is equal to the residue

$\operatorname{res}_{H=0}\frac{\exp(dH)}{(1-\exp(-H))^{n+1}}\,dH,$

which we can compute using the substitution $x=1-\exp(-H)$ (so $\exp(H)=\frac{1}{1-x}$ and $\frac{dH}{dx}=\frac{1}{1-x}$):

$\operatorname{res}_{H=0}\frac{\exp(dH)}{(1-\exp(-H))^{n+1}}\,dH=\operatorname{res}_{x=0}\frac{(1-x)^{-d-1}}{x^{n+1}}\,dx.$

This number is equal to the $x^{n}$-coefficient of $(1-x)^{-d-1}$, which is simply

$(-1)^{n}\binom{-d-1}{n}=\binom{n+d}{n}$

in agreement with what we had found for the left hand side of the Hirzebruch-Riemann-Roch theorem above. So we have just proven the theorem for line bundles on $\mathbb{P}^{n}$.

### 10.5. Proof of the Hirzebruch-Riemann-Roch theorem

Finally we now want to give a very short sketch of proof of the Hirzebruch-Riemann-Roch theorem 10.4.5, skipping several subtleties from commutative algebra. The purpose of this section is just to give an idea of the proof, and in particular to show why the rather strange-looking Todd classes come into play. For a more detailed discussion of the proof or more general versions see *[F]* chapter 15.

---

The proof of the theorem relies heavily on certain constructions being additive (or otherwise well-behaved) on exact sequences of vector bundles. Let us formalize this idea first.

###### Definition 10.5.1.

Let $X$ be a scheme. The Grothendieck group of vector bundles $K^{\circ}(X)$ on $X$ is defined to be the group of formal finite sums $\sum_{i}a_{i}[F_{i}]$ where $a_{i}\in\mathbb{Z}$ and the $F_{i}$ are vector bundles on $X$, modulo the relations $[F]=[F^{\prime}]+[F^{\prime\prime}]$ for every exact sequence $0\to F^{\prime}\to F\to F^{\prime\prime}\to 0$. (Of course we then also have $\sum_{i=1}^{r}(-1)^{i}[F_{i}]=0$ for every exact sequence

$0\to F_{1}\to F_{2}\to\cdots\to F_{r}\to 0.)$

###### Example 10.5.2.

Definition 10.5.1 just says that every construction that is additive on exact sequences passes to the Grothendieck group. For example:

- If $X$ is projective then the Euler characteristic of a vector bundle (see definition 10.4.1) is additive on exact sequences by the long exact cohomology sequence of proposition 8.2.1. Hence the Euler characteristic can be thought of as a homomorphism of Abelian groups

$\chi:K^{\circ}(X)\to\mathbb{Z},\quad\chi([F])=\chi(X,F).$
- The Chern character of a vector bundle is additive on exact sequences remark 10.4.4. So we get a homomorphism

$\operatorname{ch}:K^{\circ}(X)\to A_{*}(X)\otimes\mathbb{Q},\quad\operatorname{ch}([F])=\operatorname{ch}(F).$

(It can in fact be shown that this homomorphism gives rise to an isomorphism $K^{\circ}(X)\otimes\mathbb{Q}\to A_{*}(X)\otimes\mathbb{Q}$ if $X$ is smooth; see *[x10]* example 15.2.16(b). We will not need this however in our proof.)
- Let $X$ be a smooth projective variety. For the same reason as in (ii) the right hand side of the Hirzebruch-Riemann-Roch theorem gives rise to a homomorphism

$\tau:K^{\circ}(X)\to A_{*}(X)\otimes\mathbb{Q},\quad\tau(F)=\operatorname{ch}(F)\cdot\operatorname{td}(T_{X}).$

In particular, by (i) and (iii) we have checked already that both sides of the Hirzebruch-Riemann-Roch theorem are additive on exact sequences (which is good). So to prove the theorem we only have to check it on a set of generators for $K^{\circ}(X)$. To use this to our advantage however we first have to gather more information about the structure of the Grothendieck groups. We will need the following lemma of which we can only sketch the proof.

###### Lemma 10.5.3.

Let $X$ be a smooth projective scheme. Then for every coherent sheaf $\mathcal{F}$ on $X$ there is an exact sequence

$0\to F_{r}\to F_{r-1}\to\cdots\to F_{0}\to\mathcal{F}\to 0$

where the $F_{i}$ are vector bundles (i. e. locally free sheaves). We say that “every coherent sheaf has a finite locally free resolution”. Moreover, if $X=\mathbb{P}^{n}$ then the $F_{i}$ can all be chosen to be direct sums of line bundles $\mathcal{O}_{X}(d)$ for various $d$.

###### Proof.

By a repeated application of lemma 8.4.6 we know already that there is a (possibly infinite) exact sequence

$\cdots\to F_{r}\to\cdots\to F_{1}\to F_{0}\to\mathcal{F}\to 0.$

Now one can show that for an $n$-dimensional smooth scheme the kernel $K$ of the morphism $F_{r-1}\to F_{r-2}$ is always a vector bundle (see *[x10]* B.8.3). So we get a locally free resolution

$0\to K\to F_{r-1}\to F_{r-2}\to\cdots\to F_{0}\to\mathcal{F}\to 0$

as required.

---

10. Chern classes

If  $X = \mathbb{P}^n$  with homogeneous coordinate ring  $S = k[x_0, \ldots, x_n]$  then one can show that a coherent sheaf  $\mathcal{F}$  on  $X$  is nothing but a graded  $S$ -module  $M$  (in the same way that a coherent sheaf on an affine scheme  $\operatorname{Spec} R$  is given by an  $R$ -module). By the famous Hilbert syzygy theorem (see [EH] theorem III-57) there is a free resolution of  $M$

$$
0 \to \bigoplus_ {i} S _ {n, i} \to \dots \to \bigoplus_ {i} S _ {1, i} \to \bigoplus_ {i} S _ {0, i} \to M \to 0
$$

where each  $S_{j,i}$  is isomorphic to  $S$ , with the grading shifted by some constants  $a_{j,i}$ . This means exactly that we have a locally free resolution

$$
0 \to \bigoplus_ {i} O _ {X} (a _ {n, i}) \to \dots \to \bigoplus_ {i} O _ {X} (a _ {1, i}) \to \bigoplus_ {i} O _ {X} (a _ {0, i}) \to \mathcal {F} \to 0
$$

of  $\mathcal{F}$

Corollary 10.5.4. The Hirzebruch-Riemann-Roch theorem 10.4.5 is true for any vector bundle on  $\mathbb{P}^n$ .

Proof. By lemma 10.5.3 (applied to  $X = \mathbb{P}^n$  and a vector bundle  $\mathcal{F}$ ) the Grothendieck group  $K^{\circ}(\mathbb{P}^{n})$  is generated by the classes of the line bundles  $O_{\mathbb{P}^n}(d)$  for  $d \in \mathbb{Z}$ . As we have already checked the Hirzebruch-Riemann-Roch theorem for these bundles in example 10.4.10 the statement follows by the remark at the end of example 10.5.2.

Remark 10.5.5. To study the Hirzebruch-Riemann-Roch theorem for general smooth projective  $X$  let  $i:X\to \mathbb{P}^n$  be an embedding of  $X$  in projective space and consider the following diagram:

![img-4.jpeg](images/img-4.jpeg)

Let us first discuss the right square. The homomorphisms  $\chi$  and  $\tau$  are explained in example 10.5.2, and deg denotes the degree of the dimension-0 part of a cycle class. The Hirzebruch-Riemann-Roch theorem for  $\mathbb{P}^n$  of corollary 10.5.4 says precisely that this right square is commutative.

Now consider the left square. The homomorphism  $\tau$  is as above, and the  $i_{*}$  in the bottom row is the proper push-forward of cycles of corollary 9.2.12. We have to explain the pushforward  $i_{*}$  in the top row. Of course we would like to define  $i_{*}[F] = [i_{*}F]$  for any vector bundle  $F$  on  $X$ , but we cannot do this directly as  $i_{*}F$  is not a vector bundle but only a coherent sheaf on  $\mathbb{P}^n$ . So instead we let

$$
0 \rightarrow F _ {r} \rightarrow F _ {r - 1} \rightarrow \dots \rightarrow F _ {0} \rightarrow i _ {*} F \rightarrow 0 \tag {*}
$$

be a locally free resolution of the coherent sheaf  $i_{*}F$  on  $\mathbb{P}^n$  and set

$$
i _ {*}: K ^ {\circ} (X) \to K ^ {\circ} (\mathbb {P} ^ {n}), \quad i _ {*} ([ F ]) = \sum_ {k = 0} ^ {r} (- 1) ^ {k} [ F _ {k} ].
$$

One can show that this is indeed a well-defined homomorphism of groups (i.e. that this definition does not depend on the choice of locally free resolution), see [F] section B.8.3. But in fact we do not really need to know this: we do know by the long exact cohomology sequence applied to  $(\ast)$  that

$$
\chi (X, F) = \sum_ {k = 0} ^ {r} (- 1) ^ {k} \chi (\mathbb {P} ^ {n}, F _ {k}),
$$

---

so it is clear that at least the composition $\chi\circ i_{*}$ does not depend on the choice of locally free resolution. The Hirzebruch-Riemann-Roch theorem on $X$ is now precisely the statement that the outer rectangle in the above diagram is commutative.

As we know already that the right square is commutative, it suffices therefore to show that the left square is commutative as well (for any choice of locally free resolution as above), i. e. that

$\sum_{k=0}^{r}(-1)^{k}\operatorname{ch}(F_{k})\cdot\operatorname{td}(T_{\mathbb{P}^{r}})=i_{*}(\operatorname{ch}(F)\cdot\operatorname{td}(T_{X})).$

As the Todd class is multiplicative on exact sequences by remark 10.4.4 we can rewrite this using the projection formula as

$\sum_{k=0}^{r}(-1)^{k}\operatorname{ch}(F_{k})=i_{*}\frac{\operatorname{ch}(F)}{\operatorname{td}(N_{X/\mathbb{P}^{n}})}.$

Summarizing our ideas we see that to prove the general Hirzebruch-Riemann-Roch theorem it suffices to prove the following proposition (for $Y=\mathbb{P}^{n}$):

###### Proposition 10.5.6.

Let $i:X\to Y$ be a closed immersion of smooth projective schemes, and let $F$ be a vector bundle on $X$. Then there is a locally free resolution

$0\to F_{r}\to F_{r-1}\to\dots\to F_{0}\to i_{*}F\to 0$

of the coherent sheaf $i_{*}F$ on $Y$ such that

$\sum_{k=0}^{r}(-1)^{k}\operatorname{ch}(F_{k})=i_{*}\frac{\operatorname{ch}(F)}{\operatorname{td}(N_{X/Y})}$

in $A_{*}(Y)\otimes\mathbb{Q}$.

###### Example 10.5.7.

Before we give the general proof let us consider an example where both sides of the equation can be computed explicitly: let $X$ be a smooth scheme, $E$ a vector bundle of rank $r$ on $X$, and $Y=\mathbb{P}(E\oplus\mathcal{O}_{X})$. The embedding $i:X\to Y$ is given by $X=\mathbb{P}(0\oplus\mathcal{O}_{X})\hookrightarrow\mathbb{P}(E\oplus\mathcal{O}_{X})$. In other words, $X$ is just “the zero section of a projective bundle”. The special features of this particular case that we will need are:

1. There is a projection morphism $p:Y\to X$ such that $p\circ i=\operatorname{id}$.
2. $X$ is the zero locus of a section of a vector bundle on $Y$: consider the exact sequence

$0\to S\to p^{*}(E\oplus\mathcal{O}_{X})\to Q\to 0$ (*)

on $Y$, where $S$ is the tautological subbundle of construction 10.1.5. The vector bundle $Q$ (which has rank $r$) is usually called the *universal quotient bundle*. Note that we have a global section of $p^{*}(E\oplus\mathcal{O}_{X})$ by taking the point $(0,1)$ in every fiber (i. e. $0$ in the fiber of $E$ and $1$ in the fiber of $\mathcal{O}_{X}$). By definition of $S$ the induced section $s\in\Gamma(Q)$ vanishes precisely on $\mathbb{P}(0\oplus\mathcal{O}_{X})=X$.
3. Restricting $(*)$ to $X$ (i. e. pulling the sequence back by $i$) we get the exact sequence

$0\to i^{*}S\to E\oplus\mathcal{O}_{X}\to i^{*}Q\to 0$ (*)

on $X$. Note that the first morphism is given by $\lambda\mapsto(0,\lambda)$ by construction, so we conclude that $i^{*}Q=E$.
4. As $X$ is given in $Y$ as the zero locus of a section of $Q$, we see from example 10.1.6 that the normal bundle of $X$ in $Y$ is just $N_{X/Y}=i^{*}Q=E$.

Let us now check proposition 10.5.6 in this case. Note that *away from the zero locus of $s$* there is an exact sequence

$0\to\mathcal{O}_{Y}\stackrel{{\scriptstyle\cdot t}}{{\to}}Q\stackrel{{\scriptstyle\wedge t}}{{\to}}\Lambda^{2}Q\stackrel{{\scriptstyle\wedge t}}{{\to}}\Lambda^{3}Q\to\dots\to\Lambda^{r-1}Q\stackrel{{\scriptstyle\wedge t}}{{\to}}\Lambda^{r}Q\to 0$

---

of vector bundles (which follows from the corresponding statement for vector spaces). Dualizing and tensoring this sequence with $p^{*}F$ we get the exact sequence

$0\to p^{*}F\otimes\Lambda^{r}Q^{\vee}\to p^{*}F\otimes\Lambda^{r-1}Q^{\vee}\to\cdots\to p^{*}F\otimes Q^{\vee}\to p^{*}F\to 0$

again on $Y\backslash Z(s)=Y\backslash X$. Let us try to extend this exact sequence to all of $Y$. Note that the last morphism $p^{*}F\otimes Q^{\vee}\to p^{*}F$ is just induced by the evaluation morphism $s:Q^{\vee}\to\mathcal{O}_{Y}$, so its cokernel is precisely the sheaf $(p^{*}F)|_{Z(s)}=i_{*}F$. One can show that the other stages of the sequence remain indeed exact (see *[x10]* B.3.4), so we get a locally free resolution

$0\to p^{*}F\otimes\Lambda^{r}Q^{\vee}\to p^{*}F\otimes\Lambda^{r-1}Q^{\vee}\to\cdots\to p^{*}F\otimes Q^{\vee}\to p^{*}F\to i_{*}F\to 0$

on $Y$. (This resolution is called the Koszul complex.) So what we have to check is that

$\sum_{k=0}^{r}(-1)^{k}\operatorname{ch}(p^{*}F\otimes\Lambda^{k}Q^{\vee})=i_{*}\frac{\operatorname{ch}(F)}{\operatorname{td}(i^{*}Q)}.$

But note that

$i_{*}\frac{\operatorname{ch}(F)}{\operatorname{td}(i^{*}Q)}=\frac{\operatorname{ch}(p^{*}F)}{\operatorname{td}(Q)}\cdot i_{*}[X]=\frac{\operatorname{ch}(p^{*}F)c_{r}(Q)}{\operatorname{td}(Q)}$

by the projection formula and proposition 10.3.12. So by the additivity of Chern characters it suffices to prove that

$\sum_{k=0}^{r}(-1)^{k}\operatorname{ch}(\Lambda^{k}Q^{\vee})=\frac{c_{r}(Q)}{\operatorname{td}(Q)}.$

But this is easily done: if $\alpha_{1},\ldots,\alpha_{r}$ are the Chern roots of $Q$ then the left hand side is

$\sum_{k=0}^{r}(-1)^{k}\sum_{i_{1}<\cdots<i_{k}}\exp(-\alpha_{i_{1}}-\cdots-\alpha_{i_{k}})=\prod_{i=1}^{r}(1-\exp(-\alpha_{i}))=\alpha_{1}\cdots\alpha_{r}\cdot\prod_{i=1}^{r}\frac{1-\exp(-\alpha_{i})}{\alpha_{i}},$

which equals the right hand side. It is in fact this formal identity that explains the appearance of Todd classes in the Hirzebruch-Riemann-Roch theorem.

Using the computation of this special example we can now give the general proof of the Hirzebruch-Riemann-Roch theorem.

###### Proof.

(of proposition 10.5.6) We want to reduce the proof to the special case considered in example 10.5.7.

Let $i:X\to Y$ be any inclusion morphism of smooth projective varieties. We denote by $M$ be the blow-up of $Y\times\mathbb{P}^{1}$ in $X\times\{0\}$. The smooth projective scheme $M$ comes together with a projection morphism $q:M\to\mathbb{P}^{1}$. Its fibers $q^{-1}(P)$ for $P\neq 0$ are all isomorphic to $Y$. The fiber $q^{-1}(0)$ however is reducible with two smooth components: one of them (the exceptional hypersurface of the blow-up) is the projectivized normal bundle of $X\times\{0\}$ in $Y\times\mathbb{P}^{1}$ by example 10.1.6, and the other one is simply the blow-up $\bar{Y}$ of $Y$ in $X$. We are particularly interested in the first component. As the normal bundle of $X\times\{0\}$ in $Y\times\mathbb{P}^{1}$ is $N_{X/Y}\oplus\mathcal{O}_{X}$ this component is just the projective bundle $P:=\mathbb{P}(N_{X/Y}\oplus\mathcal{O}_{X})$ on $X$. Note that there is an inclusion of the space $X\times\mathbb{P}^{1}$ in $M$ that corresponds to the given inclusion $X\subset Y$ in the fibers $q^{-1}(P)$ for $P\neq 0$, and to the “zero section inclusion” $X\subset\mathbb{P}(N_{X/Y}\oplus\mathcal{O}_{X})=P$ as in example 10.5.7 in the fiber $q^{-1}(0)$. The following picture illustrates the geometric situation.

---

Andreas Gathmann

![img-5.jpeg](images/img-5.jpeg)

The idea of the proof is now simply the following: we have to prove an equality in the Chow groups, i.e. modulo rational equivalence. The fibers  $q^{-1}(0)$  and  $q^{-1}(\infty)$  are rationally equivalent as they are the zero resp. pole locus of a rational function on the base  $\mathbb{P}^1$ , so they are effectively "the same" for intersection-theoretic purposes. But example 10.5.7 shows that the proposition is true in the fiber  $q^{-1}(0)$ , so it should be true in the fiber  $q^{-1}(\infty)$  as well.

To be more precise, let  $F$  be a sheaf on  $X$  as in the proposition. Denote by  $p_X: X \times \mathbb{P}^1 \to X$  the projection, and by  $i_X: X \times \mathbb{P}^1 \to M$  the inclusion discussed above. Then  $i_{X*}p_X^*F$  is a coherent sheaf on  $M$  that can be thought of as "the sheaf  $F$  on  $X$  in every fiber of  $q$ ". By lemma 10.5.3 we can choose a locally free resolution

$$
0 \rightarrow F _ {r} \rightarrow F _ {r - 1} \rightarrow \dots \rightarrow F _ {0} \rightarrow i _ {X *} p _ {X} ^ {*} F \rightarrow 0 \tag {1}
$$

on  $M$

Note that the divisor  $[0] - [\infty]$  on  $\mathbb{P}^1$  is equivalent to zero by example 9.1.9. So it follows that

$$
\sum_ {k = 0} ^ {r} (- 1) ^ {k} \operatorname {c h} (F _ {i}) \cdot q ^ {*} ([ 0 ] - [ \infty ]) = 0
$$

in  $A_{*}(M)\otimes \mathbb{Q}$ . Now by definition of the pull-back we have  $q^{*}[0] = [\tilde{Y}] + [P]$  and  $q^{*}[\infty ] = [Y]$ , so we get the equality

$$
\sum_ {k = 0} ^ {r} (- 1) ^ {k} \operatorname {c h} \left(F _ {i} | _ {\tilde {Y}}\right) \cdot [ \tilde {Y} ] + \sum_ {k = 0} ^ {r} (- 1) ^ {k} \operatorname {c h} \left(F _ {i} | _ {P}\right) \cdot [ P ] = \sum_ {k = 0} ^ {r} (- 1) ^ {k} \operatorname {c h} \left(F _ {i} | _ {Y}\right) \cdot [ Y ] \tag {2}
$$

in  $A_{*}(M)\otimes \mathbb{Q}$ . But note that the restriction to  $\tilde{Y}$  of the sheaf  $i_{X*}p_X^* F$  in (1) is the zero sheaf as  $X\times \mathbb{P}^{1}\cap \tilde{Y} = \emptyset$  in  $M$ . So the sequence

$$
0 \to F _ {r} | _ {\tilde {Y}} \to \dots \to F _ {1} | _ {\tilde {Y}} \to F _ {0} | _ {\tilde {Y}} \to 0
$$

is exact, which means that the first sum in (2) vanishes. The second sum in (2) is precisely  $\frac{\operatorname{ch}(F)}{\operatorname{td}(N_{X/Y})} \cdot [X]$  by example 10.5.7. So we conclude that

$$
\sum_ {k = 0} ^ {r} (- 1) ^ {k} \operatorname {c h} (F _ {i} | _ {Y}) \cdot [ Y ] = \frac {\operatorname {c h} (F)}{\operatorname {t d} (N _ {X / Y})} \cdot [ X ]
$$

in  $A_{*}(M)\otimes \mathbb{Q}$ . Pushing this relation forward by the (proper) projection morphism from  $M$  to  $Y$  then gives the desired equation.

This completes the proof of the Hirzebruch-Riemann-Roch theorem 10.4.5.

---

###### Remark 10.5.8.

Combining proposition 10.5.6 with remark 10.5.5 we see that we have just proven the following statement: let $f:X\to Y$ be a closed immersion of smooth projective schemes, and let $F$ be a coherent sheaf on $X$. Then there is a locally free resolution

$0\to F_{r}\to F_{r-1}\to\cdots\to F_{0}\to f_{*}F\to 0$

of the coherent sheaf $f_{*}F$ on $Y$ such that

$\sum_{k=0}^{r}(-1)^{k}\operatorname{ch}(F_{k})\cdot\operatorname{td}(T_{Y})=f_{*}(\operatorname{ch}(F)\cdot\operatorname{td}(T_{X}))\in A_{*}(Y)\otimes\mathbb{Q}.$

This is often written as

$\operatorname{ch}(f_{*}F)\cdot\operatorname{td}(T_{Y})=f_{*}(\operatorname{ch}(F)\cdot\operatorname{td}(T_{X})).$

In other words, “the push-forward $f_{*}$ commutes with the operator $\tau$ of example 10.5.2 (iii)”.

It is the statement of the Grothendieck-Riemann-Roch theorem that this relation is actually true for *any proper* morphism $f$ of smooth projective schemes (and not just for closed immersions). See *[x10]* section 15 for details on how to prove this.

The Grothendieck-Riemann-Roch theorem is probably one of the most general Riemann-Roch type theorems that one can prove. The only further generalization one could think of is to singular schemes. There are some such generalizations to mildly singular schemes; see *[x10]* section 18 for details.

### 10.6. Exercises

###### Exercise 10.6.1.

Let $X=\mathbb{P}^{1}$, and for $n\in\mathbb{Z}$ let $F_{n}$ be the projective bundle $F_{n}=\mathbb{P}(\mathcal{O}_{X}\oplus\mathcal{O}_{X}(n))$. Let $p:F_{n}\to X$ be the projection morphism. The surfaces $F_{n}$ are called Hirzebruch surfaces.

1. Show that $F_{0}\cong\mathbb{P}^{1}\times\mathbb{P}^{1}$, and $F_{n}\cong F_{-n}$ for all $n$.
2. Show that all fibers $p^{-1}(P)\subset F_{n}$ for $P\in X$ are rationally equivalent as $1$-cycles on $F_{n}$. Denote this cycle by $D\in A_{1}(F_{n})$.
3. Now let $n\geq 0$. Show that the global section $(1,x_{0}^{n})$ of $\mathcal{O}_{X}\oplus\mathcal{O}_{X}(n)$ (where $x_{0}$, $x_{1}$ are the homogeneous coordinates of $X$) determines a morphism $s:X\to F_{n}$. Denote by $C\in A_{1}(F_{n})$ the class of the image curve $s(X)$.
4. Again for $n\geq 0$, show that $A_{0}(F_{n})\cong\mathbb{Z}$ and $A_{1}(F_{n})=\mathbb{Z}\cdot[C]\oplus\mathbb{Z}\cdot[D]$. Compute the intersection products $C^{2}$, $D^{2}$, and $C\cdot D$, arriving at a Bézout style theorem for the surfaces $F_{n}$.

###### Exercise 10.6.2.

Let $F$ and $F^{\prime}$ be two rank-$2$ vector bundles on a scheme $X$. Compute the Chern classes of $F\otimes F^{\prime}$ in terms of the Chern classes of $F$ and $F^{\prime}$.

###### Exercise 10.6.3.

Let $F$ be a vector bundle of rank $r$ on a scheme $X$, and let $p:\mathbb{P}(F)\to X$ be the projection. Prove that

$D_{F}^{r}+D_{F}^{r-1}\cdot p^{*}c_{1}(F)+\cdots+p^{*}c_{r}(F)=0,$

where $D_{F}$ is the Cartier divisor associated to the line bundle $\mathcal{O}_{\mathbb{P}(F)}(1)$.

###### Exercise 10.6.4.

Let $X\subset\mathbb{P}^{4}$ be the intersection of two general quadric hypersurfaces.

1. Show that one expects a finite number of lines in $X$.
2. If there is a finite number of lines in $X$, show that this number is $16$ (as usual counted with multiplicities (which one expects to be $1$ for general $X$)).

###### Exercise 10.6.5.

A circle in the plane $\mathbb{P}^{2}_{\mathbb{C}}$ is defined to be a conic passing through the two points $(1:\pm i:0)$.

Why is this called a circle?

How many circles are there in the plane that are tangent to

---

1. three circles
2. two circles and a line
3. one circle and two lines
4. three lines

in general position? (Watch out for possible non-enumerative contributions in the intersection products you consider.)

If you are interested, try to find out the answer to the above questions over $\mathbb{R}$ (and the “usual” definition of a circle).

###### Exercise 10.6.6.

Let $X\subset\mathbb{P}^{4}$ be a smooth quintic hypersurface, i. e. the zero locus of a homogeneous polynomial of degree 5.

1. Show that one expects a finite number of lines in $X$, and that this expected number is then 2875.
2. Show that the number of lines on the special quintic $X=\{x_{0}^{5}+\cdots+x_{4}^{5}=0\}$ is *not* finite. This illustrates the fact that the intersection-theoretic computations will only yield virtual numbers in general. (In fact one can show that the number of lines on a *general* quintic hypersurface in $\mathbb{P}^{4}$ is finite and that the computation of (i) then yields the correct answer.)

###### Exercise 10.6.7.

Let $X=\mathbb{P}^{1}\times\mathbb{P}^{1}$. Compute the number $K_{X}^{2}+c_{2}(T_{X})$ directly and check that it is divisible by 12 (see example 10.4.8).

###### Exercise 10.6.8.

Let $X$ and $Y$ be isomorphic smooth projective varieties. Use the Hirzebruch-Riemann-Roch theorem 10.4.5 to prove that the constant coefficients of the Hilbert polynomials of $X$ and $Y$ agree, whereas the non-constant coefficients will in general be different.