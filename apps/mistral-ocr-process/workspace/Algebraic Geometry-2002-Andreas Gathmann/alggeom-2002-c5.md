5. Schemes

To any commutative ring $R$ with identity we associate a locally ringed space called $\operatorname{Spec}R$, the spectrum of $R$. Its underlying set is the set of prime ideals of $R$, so if $R$ is the coordinate ring of an affine variety $X$ over an algebraically closed field, then $\operatorname{Spec}R$ as a set is the set of non-empty closed irreducible subvarieties of $X$. Moreover, in this case the open subsets of $\operatorname{Spec}R$ are in one-to-one correspondence with the open subsets of $X$, and the structure sheaves of $\operatorname{Spec}R$ and $X$ coincide via this correspondence.

A morphism of locally ringed spaces is a morphism of ringed spaces that respects the maximal ideals of the local rings. Locally ringed spaces of the form $\operatorname{Spec}R$ are called affine schemes; locally ringed spaces that are locally of the form $\operatorname{Spec}R$ are called schemes. Schemes are the fundamental objects of study in algebraic geometry. Prevarieties correspond exactly to those schemes that are reduced, irreducible, and of finite type over an algebraically closed field.

For any two morphisms of schemes $X\to S$ and $Y\to S$ there is a fiber product $X\times_{S}Y$; this is a scheme such that giving morphisms $Z\to X$ and $Z\to Y$ that commute with the given morphisms to $S$ is “the same” as giving a morphism $Z\to X\times_{S}Y$. If $X$ and $Y$ are prevarieties over $k$ and we take $S=\operatorname{Spec}k$, we get back our old notion of the product $X\times Y$ of prevarieties.

For any graded ring $R$ there is a scheme $\operatorname{Proj}R$ whose points are the homogeneous prime ideals of $R$ that do not contain the irrelevant ideal. This construction generalizes our earlier construction of projective varieties; if $R$ is the homogeneous coordinate ring of a projective variety $X$ over an algebraically closed field then $\operatorname{Proj}R$ “is” just the projective variety $X$.

### 5.1. Affine schemes

We now come to the definition of schemes, which are the main objects of study in algebraic geometry. The notion of schemes extends that of prevarieties in a number of ways. We have already met several instances where an extension of the category of prevarieties could be useful:

- We defined a prevariety to be irreducible. Obviously, it makes sense to also consider reducible spaces. In the case of affine and projective varieties we called them algebraic sets, but we did not give them any further structure or defined regular functions and morphisms of them. Now we want to make reducible spaces into full-featured objects of our category.
- At present we have no geometric objects corresponding to non-radical ideals in $k[x_{1},\ldots,x_{n}]$, or in other words to coordinate rings with nilpotent elements. These non-radical ideals pop up naturally however: e. g. we have seen in exercise 1.4.1 that intersections of affine varieties correspond to sums of their ideals, modulo taking the radical. It would seem more natural to define the intersection $X_{1}\cap X_{2}$ of two affine varieties $X_{1},X_{2}\subset\mathbb{A}^{n}$ to be a geometric object associated to the ideal $I(X_{1})+I(X_{2})\subset k[x_{1},\ldots,x_{n}]$. This was especially obvious when we discussed blow-ups: blowing up $X_{1}\cap X_{2}$ in $\mathbb{A}^{n}$ “separates” $X_{1}$ and $X_{2}$ (if none of these two sets is contained in the other), i. e. their strict transforms $\tilde{X}_{1}$ and $\tilde{X}_{2}$ are disjoint in $\tilde{\mathbb{A}}^{n}$, but this is only true if we blow-up at the ideal $I(X_{1})+I(X_{2})$ and not at its radical (see exercise 4.6.10).
- Recall that by lemma 2.3.7 and remark 2.3.14 we have a one-to-one correspondence between affine varieties over $k$ and finitely generated $k$-algebras that are domains, both modulo isomorphism. We have just seen that we should drop the condition on the $k$-algebra to be a domain. We can go even further and also drop the condition that it is finitely generated — then we would expect to arrive at “infinite-dimensional” objects. Moreover, it turns out that we do not even need a $k$-algebra to do geometry; it is sufficient to start with any commutative ring with

---

identity, i. e. we do not have to have a ground field. This can be motivated by noting that most constructions we made with the coordinate ring of a variety — defining the structure sheaf, setting up correspondences between points and maximal ideals, and so on — actually only used the ring structure of the coordinate ring, and not the $k$-algebra structure.

All these generalizations are included in the definition of a scheme. Note that they apply already to affine varieties; so we will start by defining an affine scheme to be “an affine variety generalized as above”. Later we will then say that a scheme is an object that looks locally like an affine scheme, just as we did it in the case of prevarieties.

We are now ready to construct from any ring $R$ (which will always mean a commutative ring with identity) an affine scheme, which will be a ringed space and which will be denoted $\operatorname{Spec}R$, the spectrum of $R$.

###### Definition 5.1.1.

Let $R$ be a ring (commutative with identity, as always). We define $\operatorname{Spec}R$ to be the set of all prime ideals of $R$. (As usual, $R$ itself does not count as a prime ideal, but $(0)$ does if $R$ is a domain.) We call $\operatorname{Spec}R$ the spectrum of $R$, or the affine scheme associated to $R$. For every $\mathfrak{p}\in\operatorname{Spec}R$, i. e. $\mathfrak{p}\subset R$ a prime ideal, let $k(\mathfrak{p})$ be the quotient field of the domain $R/\mathfrak{p}$.

###### Remark 5.1.2.

Let $X=\operatorname{Spec}R$ be an affine scheme. We should think of $X$ as the analogue of an affine variety, and of $R$ as the analogue of its coordinate ring.

###### Remark 5.1.3.

Any element $f\in R$ can be considered to be a “function” on $\operatorname{Spec}R$ in the following sense: for $\mathfrak{p}\in\operatorname{Spec}R$, denote by $f(\mathfrak{p})$ the image of $f$ under the composite map $R\to R/\mathfrak{p}\to k(\mathfrak{p})$. We call $f(\mathfrak{p})$ the value of $f$ at the point $\mathfrak{p}$. Note that these values will in general lie in different fields. If $R=k[x_{1},\ldots,x_{n}]/I(X)$ is the coordinate ring of an affine variety $X$ and $\mathfrak{p}$ is a maximal ideal (i. e. a point in $X$), then $k(\mathfrak{p})=k$ and the value of an element $f\in R$ as defined above is equal to the value of $f$ at the point corresponding to $\mathfrak{p}$ in the classical sense. If $\mathfrak{p}\subset R$ is not maximal and corresponds to some subvariety $Y\subset X$, the value $f(\mathfrak{p})$ lies in the function field $K(Y)$ and can be thought of as the restriction of the function $f$ to $Y$.

###### Example 5.1.4.

1. If $k$ is a field, then $\operatorname{Spec}k$ consists of a single point $(0)$.
2. The space $\operatorname{Spec}\mathbb{C}[x]$ (that will correspond to the affine variety $\mathbb{A}^{1}$ over $\mathbb{C}$) contains a point $(x-a)$ for every $a\in\mathbb{A}^{1}$, together with a point $(0)$ corresponding to the subvariety $\mathbb{A}^{1}$.
3. More generally, if $R=A(X)$ is the coordinate ring of an affine variety $X$ over an algebraically closed field, then the set $\operatorname{Spec}R$ contains a point for every closed subvariety of $X$ (as subvarieties correspond exactly to prime ideals). This affine scheme $\operatorname{Spec}R$ will be the analogue of the affine variety $X$. So an affine scheme has “more points” than the corresponding affine variety: we have enlarged the set by throwing in an additional point for every closed subvariety $Y$ of $X$. This point is usually called the generic point (or general point) of $Y$. In other words, in the scheme corresponding to an affine variety with coordinate ring $R$ we will have a point for every prime ideal in $R$, and not just for every maximal ideal. These additional points are sometimes important, but quite often one can ignore this fact. Many textbooks will even adopt the convention that a point of a scheme is always meant to be a point in the old geometric sense (i. e. a maximal ideal).
4. In contrast to (ii), the affine scheme $\operatorname{Spec}\mathbb{R}[x]$ contains points that are not of the form $(x-a)$ or $(0)$, e. g. $(x^{2}+1)\in\operatorname{Spec}\mathbb{R}[x]$.
5. The affine scheme $\operatorname{Spec}\mathbb{Z}$ contains an element for every prime number, and in addition the generic point $(0)$.

---

.

So far we have defined $\operatorname{Spec}R$ as a set. This is not particularly interesting, so let us move on and make $\operatorname{Spec}R$ into a topological space. This is done in the same way as for affine varieties.

###### Definition 5.1.5.

Let $R$ be a ring. For every subset $S\subset R$, we define the zero locus of $S$ to be the set

$Z(S):=\{\mathfrak{p}\in\operatorname{Spec}R\ ;\ f(\mathfrak{p})=0\ \text{for all}\ f\in S\}\subset\operatorname{Spec}R,$

where $f(\mathfrak{p})$ is the value of $f$ at $\mathfrak{p}$ as in remark 5.1.3. (Obviously, $S$ and $(S)$ define the same zero locus, so we will usually only consider zero loci of ideals.)

###### Remark 5.1.6.

By the definition of the value of an element $f\in R$ at a point $\mathfrak{p}\in\operatorname{Spec}R$, we can also write the definition of the zero locus as

$Z(S)$ $=\{\mathfrak{p}\in\operatorname{Spec}R\ ;\ f\in\mathfrak{p}\ \text{for all}\ f\in S\}$
$=\{\mathfrak{p}\in\operatorname{Spec}R\ ;\ \mathfrak{p}\supset S\}.$

###### Lemma 5.1.7.

Let $R$ be a ring.

1. If $\{I_{i}\}$ is a family of ideals of $R$ then $\bigcap_{i}Z(I_{i})=Z(\sum_{i}I_{i})\subset\operatorname{Spec}R$.
2. If $I_{1},I_{2}\subset R$ then $Z(I_{1})\cup Z(I_{2})=Z(I_{1}I_{2})\subset\operatorname{Spec}R$.
3. If $I_{1},I_{2}\subset R$ then $Z(I_{1})\subset Z(I_{2})$ if and only if $\sqrt{I_{2}}\subset\sqrt{I_{1}}$.

###### Proof.

The proof is literally the same as in the case of affine algebraic sets. ∎

Hence we can define a topology on $\operatorname{Spec}R$ by taking the subsets of the form $Z(S)$ as the closed subsets. In particular, this defines the notions of irreducibility and dimension for $\operatorname{Spec}R$, as they are purely topological concepts.

###### Remark 5.1.8.

Note that points $\mathfrak{p}$ in $\operatorname{Spec}R$ are not necessarily closed: in fact,

$\overline{\{\mathfrak{p}\}}=Z(\mathfrak{p})=\{\mathfrak{q}\in\operatorname{Spec}R\ ;\ \mathfrak{q}\supset\mathfrak{p}\}.$

This is equal to $\{\mathfrak{p}\}$ only if $\mathfrak{p}$ is maximal. Hence the closed points of $\operatorname{Spec}R$ correspond to the points of an affine variety in the classical sense. The other points are just generic points of irreducible closed subsets of $\operatorname{Spec}R$, as already mentioned in example 5.1.4.

###### Example 5.1.9.

The motivation for the name “generic point” can be seen from the following example. Let $k$ be an algebraically closed field, and let $R=\operatorname{Spec}k[x_{1},x_{2}]$ be the affine scheme corresponding to $\mathbb{A}^{2}$. Consider $Z(x_{2})\subset\operatorname{Spec}R$, which “is” just the $x_{1}$-axis; so its complement $\operatorname{Spec}R\backslash Z(x_{2})$ should be the set of points that do not lie on the $x_{1}$-axis. But note that the element $\mathfrak{p}=(x_{1})$ is contained in $\operatorname{Spec}R\backslash Z(x_{2})$, although the zero locus of $x_{1}$, namely the $x_{2}$-axis, does intersect the $x_{1}$-axis. So the geometric way to express the fact that $(x_{1})\in\operatorname{Spec}R\backslash Z(x_{2})$ is to say that the *generic point* of the $x_{2}$-axis does not lie on the $x_{1}$-axis.

###### Remark 5.1.10.

Let $R$ be a ring, let $X=\operatorname{Spec}R$, and let $f\in R$. As in the case of affine varieties, we call $X_{f}:=X\backslash Z(f)$ the distinguished open subset associated to $f$. Note that any open subset of $X$ is a (not necessarily finite) union of distinguished open subsets. This is often expressed by saying that the distinguished open subsets form a *base* of the topology of $X$.

Now we come to the definition of the structure sheaf of $\operatorname{Spec}R$. Recall that in the case of an affine variety $X$, we first defined the local ring $\mathcal{O}_{X,P}$ of the functions regular at a point $P\in X$ to be the localization of $A(X)$ at the maximal ideal corresponding to $P$, and then said that an element in $\mathcal{O}_{X}(U)$ for an open subset $U\subset X$ is a function that is regular at every point $P\in U$. We could accomplish that in the case of varieties just by intersecting the local rings $\mathcal{O}_{X,P}$, as they were all contained in the function field $K(X)$. But in the case of a general affine scheme $\operatorname{Spec}R$ the various local rings $R_{\mathfrak{p}}$ for $\mathfrak{p}\in\operatorname{Spec}R$ do not lie inside

---

some big space, so we cannot just take their intersection. The way around this problem is to say that an element in $\mathcal{O}_{X}(U)$ (for $X=\operatorname{Spec}R$ and $U\subset X$ open) is given by a collection of elements in the various local rings $R_{\mathfrak{p}}$ for all $\mathfrak{p}\in U$, and require that these elements can locally be written as quotients of elements of $R$ (recall that we had a similar condition for affine varieties in lemma 2.1.8):

###### Definition 5.1.11.

Let $R$ be a ring, and let $X=\operatorname{Spec}R$. For every open subset $U\subset X$ we define $\mathcal{O}_{X}(U)$ to be

$\mathcal{O}_{X}(U)$ $:=$ $\{\varphi=(\varphi_{\mathfrak{p}})_{\mathfrak{p}\in U}\text{ with }\varphi_{\mathfrak{p}}\in R_{\mathfrak{p}}\text{ for all }\mathfrak{p}\in U$
$\text{ such that }\text{``}\varphi\text{ is locally of the form }\frac{f}{g}\text{ for }f,g\in R"\}$
$=$ $\{\varphi=(\varphi_{\mathfrak{p}})_{\mathfrak{p}\in U}\text{ with }\varphi_{\mathfrak{p}}\in R_{\mathfrak{p}}\text{ for all }\mathfrak{p}\in U$
$\text{ such that for every }\mathfrak{p}\in U\text{ there is a neighborhood }V\text{ in }U\text{ and }f,g\in R$
$\text{ with }g\notin\mathfrak{q}\text{ and }\varphi_{\mathfrak{q}}=\frac{f}{g}\in R_{\mathfrak{q}}\text{ for all }\mathfrak{q}\in V.\}$

As the conditions imposed on the elements of $\mathcal{O}_{X}(U)$ are local, it is easy to verify that this defines a sheaf $\mathcal{O}_{X}$ on $X=\operatorname{Spec}R$. The first thing to do is to check that this sheaf has the properties that we expect from the case of affine varieties (see definition 2.1.5, remark 2.1.6, and proposition 2.1.10).

###### Proposition 5.1.12.

Let $R$ be a ring and $X=\operatorname{Spec}R$.

1. For any $\mathfrak{p}\in X$ the stalk $\mathcal{O}_{X,\mathfrak{p}}$ of the sheaf $\mathcal{O}_{X}$ is isomorphic to the local ring $R_{\mathfrak{p}}$.
2. For any $f\in R$, the ring $\mathcal{O}_{X}(X_{f})$ is isomorphic to the localized ring $R_{f}$. In particular, $\mathcal{O}_{X}(X)=R$.

###### Proof.

(i): There is a well-defined ring homomorphism

$\psi:\mathcal{O}_{X,\mathfrak{p}}\to R_{\mathfrak{p}},\;(U,\varphi)\mapsto\varphi_{\mathfrak{p}}.$

We have to show that $\psi$ is a bijection.

$\psi$ is surjective: Any element of $R_{\mathfrak{p}}$ has the form $\frac{f}{g}$ with $f,g\in R$ and $g\notin\mathfrak{p}$. The function $\frac{f}{g}$ is well-defined on $X_{g}$, so $(X_{g},\frac{f}{g})$ defines an element in $\mathcal{O}_{X,\mathfrak{p}}$ that is mapped by $\psi$ to the given element.

$\psi$ is injective: Let $\varphi_{1},\varphi_{2}\in\mathcal{O}_{X}(U)$ for some neighborhood $U$ of $\mathfrak{p}$, and assume that $(\varphi_{1})_{\mathfrak{p}}=(\varphi_{2})_{\mathfrak{p}}$. We have to show that $\varphi_{1}$ and $\varphi_{2}$ coincide in a neighborhood of $\mathfrak{p}$, so that they define the same element in $\mathcal{O}_{X,\mathfrak{p}}$. By shrinking $U$ if necessary we may assume that $\varphi_{i}=\frac{f_{i}}{g_{i}}$ on $U$ for $i=1,2$, where $f_{i},g_{i}\in R$ and $g_{i}\notin\mathfrak{p}$. As $\varphi_{1}$ and $\varphi_{2}$ have the same image in $R_{\mathfrak{p}}$, it follows that $h(f_{1}g_{2}-f_{2}g_{1})=0$ in $R$ for some $h\notin\mathfrak{p}$. Therefore we also have $\frac{f_{1}}{g_{1}}=\frac{f_{2}}{g_{2}}$ in every local ring $R_{\mathfrak{q}}$ such that $g_{1},g_{2},h\notin\mathfrak{q}$. But the set of such $\mathfrak{q}$ is the open set $X_{g_{1}}\cap X_{g_{2}}\cap X_{h}$, which contains $\mathfrak{p}$. Hence $\varphi_{1}=\varphi_{2}$ on some neighborhood of $\mathfrak{p}$, as required.

(ii): There is a well-defined ring homomorphism

$\psi:R_{f}\to\mathcal{O}_{X}(X_{f}),\;\frac{g}{f^{r}}\mapsto\frac{g}{f^{r}}$

(i. e. we map $\frac{g}{f^{r}}$ to the element of $\mathcal{O}_{X}(X_{f})$ that assigns to any $\mathfrak{p}$ the image of $\frac{g}{f^{r}}$ in $R_{\mathfrak{p}}$).

$\psi$ is injective: Assume that $\psi(\frac{g_{1}}{f^{r_{1}}})=\psi(\frac{g_{2}}{f^{r_{2}}})$, i. e. for every $\mathfrak{p}\in X_{f}$ there is an element $h\notin\mathfrak{p}$ such that $h(g_{1}f^{r_{2}}-g_{2}f^{r_{1}})=0$. Let $I\subset R$ be the annihilator of $g_{1}f^{r_{2}}-g_{2}f^{r_{1}}$, then we have just shown that $I\not\subset\mathfrak{p}$, as $h\in I$ but $h\notin\mathfrak{p}$. This holds for every $\mathfrak{p}\in X_{f}$, so $Z(I)\cap X_{f}=\emptyset$, or in other words $Z(I)\subset Z(f)$. By lemma 5.1.7 (iii) this means that $f^{r}\in I$ for some $r$, so $f^{r}(g_{1}f^{r_{2}}-g_{2}f^{r_{1}})=0$, hence $\frac{g_{1}}{f^{r_{1}}}=\frac{g_{2}}{f^{r_{2}}}$ in $R_{f}$.

$\psi$ is surjective: Let $\varphi\in\mathcal{O}_{X}(X_{f})$. By definition, we can cover $X_{f}$ by open sets $U_{i}$ on which $\varphi$ is represented by a quotient $\frac{g_{i}}{f_{i}}$, with $f_{i}\notin\mathfrak{p}$ for all $\mathfrak{p}\in U_{i}$, i. e. $U_{i}\subset X_{f_{i}}$. As

---

the open subsets of the form $X_{h_{i}}$ form a base for the topology of $X$, we may assume that $U_{i}=X_{h_{i}}$ for some $h_{i}$.

We want to show that we can assume $f_{i}=h_{i}$. In fact, as $X_{h_{i}}\subset X_{f_{i}}$, i. e. by taking complements we get $Z(f_{i})\subset Z(h_{i})$, and therefore $h_{i}\in\sqrt{f_{i}}$ by lemma 5.1.7 (iii). Hence $h_{i}^{r}=cf_{i}$, so $\frac{g_{i}}{f_{i}}=\frac{cg_{i}}{h_{i}^{r}}$. Replacing $h_{i}$ by $h_{i}^{r}$ (as $X_{h_{i}}=X_{h_{i}^{r}}$) and $g_{i}$ by $cg_{i}$ we can assume that $X_{f}$ is covered by open subsets of the form $X_{h_{i}}$, and that $\varphi$ is represented by $\frac{g_{i}}{h_{i}}$ on $X_{h_{i}}$.

Next we prove that $X_{f}$ can actually be covered by finitely many such $X_{h_{i}}$. Indeed, $X_{f}\subset\bigcup_{i}X_{h_{i}}$ if and only if $Z(f)\supset\bigcap_{i}Z(h_{i})=Z(\sum(h_{i}))$. By lemma 5.1.7 (iii) this is equivalent to saying that $f^{r}\in\sum(h_{i})$ for some $r$. But this means that $f^{r}$ can be written as a finite sum $f^{r}=\sum b_{i}h_{i}$. Hence we can assume that we have only finitely many $h_{i}$.

On $X_{h_{i}}\cap X_{h_{j}}=X_{h_{i}h_{j}}$, we have two elements $\frac{g_{i}}{h_{i}}$ and $\frac{g_{j}}{h_{j}}$ representing $\varphi$, so by the injectivity proven above it follows that $\frac{g_{i}}{h_{i}}=\frac{g_{j}}{h_{j}}$ in $R_{h_{i}h_{j}}$, hence $(h_{i}h_{j})^{n}(g_{i}h_{j}-g_{j}h_{i})=0$ for some $n$. As we have only finitely many $h_{i}$, we may pick one $n$ that works for all $i,j$. Now replace $g_{i}$ by $g_{i}h_{i}^{n}$ and $h_{i}$ by $h_{i}^{n+1}$ for all $i$, then we still have $\varphi$ represented by $\frac{g_{i}}{h_{i}}$ on $X_{h_{i}}$, and moreover $g_{i}h_{j}-g_{j}h_{i}=0$ for all $i,j$.

Now write $f^{r}=\sum b_{i}h_{i}$ as above, which is possible since the $X_{h_{i}}$ cover $X_{f}$. Let $g=\sum b_{i}g_{i}$. Then for every $j$ we have

$gh_{j}=\sum_{i}b_{i}g_{i}h_{j}=\sum_{i}b_{i}h_{i}g_{j}=f^{r}g_{j},$

so $\frac{f}{g}=\frac{h_{j}}{g_{j}}$ on $X_{h_{j}}$. Hence $\varphi$ is represented on $X_{f}$ by $\frac{g}{f^{r}}\in R_{f}$, i. e. $\psi$ is surjective. ∎

###### Remark 5.1.13.

Note that a regular function is in general no longer determined by its values on points. For example, let $R=k[x]/(x^{2})$ and $X=\operatorname{Spec}R$. Then $X$ has just one point $(x)$. On this point, the function $x\in R=\mathcal{O}_{X}(X)$ takes the value $0=x\in(k[x]/(x^{2}))/(x)=k$. In particular, the functions $0$ and $x$ have the same values at all points of $X$, but they are not the same regular function.

### 5.2. Morphisms and locally ringed spaces

As in the case of varieties, the next step after defining regular functions on an affine scheme is to define morphisms between them. Of course one is tempted to define a morphism $f:X\to Y$ between affine schemes to be a morphism of ringed spaces as in definition 2.3.1, but recall that for this definition to work we needed a notion of pull-back $f^{*}$ of regular functions. In the case of varieties we got this by requiring that the structure sheaves be sheaves of $k$-valued functions, so that a set-theoretic pull-back exists. But this is not possible for schemes, as we do not have a ground field, and the values $\varphi(\mathfrak{p})$ of a regular function $\varphi$ lie in unrelated rings. Even worse, we have seen already in example 5.1.13 that a regular function is not determined by its values on points.

The way out of this dilemma is to make the pull-back maps $f^{*}:\mathcal{O}_{Y}(U)\to\mathcal{O}_{X}(f^{-1}(U))$ part of the data required to define a morphism. Hence we say that a morphism $f:X\to Y$ between affine schemes is given by a continuous map $f:X\to Y$ between the underlying topological spaces, together with pull-back maps $f^{*}=f^{*}_{U}:\mathcal{O}_{Y}(U)\to\mathcal{O}_{X}(f^{-1}(U))$ for every open subset $U\subset Y$. Of course we need some compatibility conditions among the $f^{*}_{U}$. The most obvious one is compatibility with the restriction maps, i. e. $f^{*}_{V}\circ\rho_{U,V}=\rho_{f^{-1}(U),f^{-1}(V)}\circ f^{*}_{U}$. But we also need some sort of compatibility between the $f^{*}_{U}$ and the continuous map $f$. To explain this condition, note that the maps $f^{*}_{U}$ give rise to a map between the stalks

$f^{*}_{P}:\mathcal{O}_{Y,f(P)}\to\mathcal{O}_{X,P},\;(U,\varphi)\mapsto(f^{-1}(U),f^{*}\varphi)$

for every point $P\in X$ (this is easily seen to be well-defined). These stalks are local rings, call their maximal ideals $\mathfrak{m}_{Y,f(P)}$ and $\mathfrak{m}_{X,P}$, respectively. Now the fact that $f$ maps $P$

---

to $f(P)$ should be reflected on the level of the pull-back maps $f^{*}$ by the condition that $(f_{P}^{*})^{-1}(\mathfrak{m}_{X,P})=\mathfrak{m}_{Y,f(P)}$. This leads to the following definition.

###### Definition 5.2.1.

A locally ringed space is a ringed space $(X,\mathcal{O}_{X})$ such that at each point $P\in X$ the stalk $\mathcal{O}_{X,P}$ is a local ring. The maximal ideal of $\mathcal{O}_{X,P}$ will be denoted by $\mathfrak{m}_{X,P}$, and the residue field $\mathcal{O}_{X,P}/\mathfrak{m}_{X,P}$ will be denoted $k(P)$.

A morphism of locally ringed spaces from $(X,\mathcal{O}_{X})$ to $(Y,\mathcal{O}_{Y})$ is given by the following data:

- a continuous map $f:X\to Y$,
- for every open subset $U\subset Y$ a ring homomorphism $f_{U}^{*}:\mathcal{O}_{Y}(U)\to\mathcal{O}_{X}(f^{-1}(U))$,

such that $f_{V}^{*}\circ\mathfrak{p}_{U,V}=\mathfrak{p}_{f^{-1}(U),f^{-1}(V)}\circ f_{U}^{*}$ for all $V\subset U\subset Y$ (i. e. the $f^{*}$ are compatible with the restriction maps) and $(f_{P}^{*})^{-1}(\mathfrak{m}_{X,P})=\mathfrak{m}_{Y,f(P)}$, where the $f_{P}^{*}:\mathcal{O}_{Y,f(P)}\to\mathcal{O}_{X,P}$ are the maps induced on the stalks, as explained above. We will often omit the index of the various pull-back maps $f^{*}$ if it is clear from the context on which spaces they act.

A morphism of affine schemes is a morphism as locally ringed spaces.

The following proposition is the analogue of lemma 2.3.7. It shows that definition 5.2.1 was “the correct one”, because it gives us finally what we want.

###### Proposition 5.2.2.

Let $R,S$ be rings, and let $X=\operatorname{Spec}R$ and $Y=\operatorname{Spec}S$ the corresponding affine schemes. There is a one-to-one correspondence between morphisms $X\to Y$ and ring homomorphisms $S\to R$.

###### Proof.

If $\psi:S\to R$ is a ring homomorphism, we define a map $f:X\to Y$ by $f(\mathfrak{p})=\psi^{-1}(\mathfrak{p})$. For every ideal $I\subset S$ it follows that $f^{-1}(Z(I))=Z(\psi(I))$, so $f$ is continuous. For each $\mathfrak{p}\in\operatorname{Spec}R$, we can localize $\psi$ to get a homomorphism of local rings $\psi_{\mathfrak{p}}:\mathcal{O}_{Y,f(\mathfrak{p})}=S_{\psi^{-1}(\mathfrak{p})}\to R_{\mathfrak{p}}=\mathcal{O}_{X,\mathfrak{p}}$ satisfying the condition $\psi_{\mathfrak{p}}^{-1}(\mathfrak{m}_{X,\mathfrak{p}})=\mathfrak{m}_{Y,f(\mathfrak{p})}$. By definition of the structure sheaf, this gives homomorphisms of rings $f^{*}:\mathcal{O}_{Y}(U)\to\mathcal{O}_{X}(f^{-1}(U))$, and by construction $f_{\mathfrak{p}}^{*}=\psi_{\mathfrak{p}}$, so we get a morphism of locally ringed spaces.

If $f:X\to Y$ is a morphism, we get a ring homomorphism $f^{*}:S=\mathcal{O}_{Y}(Y)\to\mathcal{O}_{X}(X)=R$ by proposition 5.1.12 (ii). By the above this again determines a morphism $g:X\to Y$. We leave it as an exercise to check that the various compatibility conditions imply that $f=g$. ∎

###### Example 5.2.3.

Let $X=\operatorname{Spec}R$ be an affine scheme. If $I\subset R$ is an ideal, then we can form the affine scheme $Y=\operatorname{Spec}(R/I)$, and the ring homomorphism $R\to R/I$ gives us a morphism $Y\to X$. Note that the prime ideals of $R/I$ are exactly the ideals $\mathfrak{p}\subset R$ with $\mathfrak{p}\supset I$, so the map $Y\to X$ is an inclusion with image $Z(I)$. So we can view $Y$ as an affine “closed subscheme” of $X$. For a precise definition of this concept see example 7.2.10.

Now let $Y_{1}=\operatorname{Spec}(R/I_{1})$ and $Y_{2}=\operatorname{Spec}(R/I_{2})$ be closed subschemes of $X$. We define the intersection scheme $Y_{1}\cap Y_{2}$ in $X$ to be $Y_{1}\cap Y_{2}=\operatorname{Spec}R/(I_{1}+I_{2})$.

For example, let $X=\operatorname{Spec}\mathbb{C}[x_{1},x_{2}]$, $Y_{1}=\operatorname{Spec}\mathbb{C}[x_{1},x_{2}]/(x_{2})$, $Y_{2}=\operatorname{Spec}\mathbb{C}[x_{1},x_{2}]/(x_{2}-x_{1}^{2}+a^{2})$ for some $a\in\mathbb{C}$. Then the intersection scheme $Y_{1}\cap Y_{2}$ is $\operatorname{Spec}\mathbb{C}[x_{1}]/((x_{1}-a)(x_{1}+a))$. For $a\neq 0$ we have $\mathbb{C}[x_{1}]/((x_{1}-a)(x_{1}+a))\cong\mathbb{C}[x_{1}]/(x_{1}-a)\times\mathbb{C}[x_{1}]/(x_{1}+a)\cong\mathbb{C}\times\mathbb{C}$, so $Y_{1}\cap Y_{2}$ is just the disjoint union of the two points $(a,0)$ and $(-a,0)$ in $\mathbb{C}^{2}$. For $a=0$ however we have $Y_{1}\cap Y_{2}=\operatorname{Spec}\mathbb{C}[x_{1}]/(x_{1}^{2})$, which has only one point $(0,0)$. But in all cases the ring $\mathbb{C}[x_{1}]/((x_{1}-a)(x_{1}+a))$ has dimension $2$ as a vector space over $\mathbb{C}$. We say that $Y_{1}\cap Y_{2}$ is a “scheme of length $2$”, which consists either of two distinct points of length $1$ each, or of one point of length (i. e. multiplicity) $2$.

Note also that there is always a unique line in $\mathbb{A}^{2}$ through $Y_{1}\cap Y_{2}$, even in the case $a=0$ where the scheme has only one geometric point. This is because the scheme $Y_{1}\cap Y_{2}=\operatorname{Spec}\mathbb{C}[x_{1},x_{2}]/(x_{2},(x_{1}-a)(x_{1}+a))$ is a subscheme of the line $L=\operatorname{Spec}\mathbb{C}[x_{1},x_{2}]/(c_{1}x_{1}+a)$

---

Andreas Gathmann

$c_{2}x_{2})$  if and only if  $(c_{1}x_{1} + c_{2}x_{2})\subset (x_{2},(x_{1} - a)(x_{1} + a))$ , which is the case only if  $c_{1} = 0$ . In particular, the  $x_{1}$ -axis is the only line in  $\mathbb{A}^2$  that contains  $\operatorname{Spec}\mathbb{C}[x_1,x_2] / (x_2,x_1^2)$ . One can therefore think of this scheme as "the origin together with a tangent direction along the  $x_{1}$ -axis".

![img-0.jpeg](images/img-0.jpeg)

![img-1.jpeg](images/img-1.jpeg)

Example 5.2.4. Again let  $Y_{1} = \operatorname{Spec}(R / I_{1})$  and  $Y_{2} = \operatorname{Spec}(R / I_{2})$  be closed subschemes of the affine scheme  $X = \operatorname{Spec} R$ . Note that for affine varieties the ideal of the union of two closed subsets equals the intersection of their ideals (see exercise 1.4.1 (i)). So scheme-theoretically we just define the union  $Y_{1} \cup Y_{2}$  to be  $\operatorname{Spec} R / (I_{1} \cap I_{2})$ .

The following lemma is the scheme-theoretic analogue of lemma 2.3.16.

Lemma 5.2.5. Let  $X = \operatorname{Spec} R$  be an affine scheme, and let  $f \in R$ . Then the distinguished open subset  $X_f$  is the affine scheme  $\operatorname{Spec} R_f$ .

Proof. Note that both  $X_{f}$  and  $\operatorname{Spec} R_{f}$  have the description  $\{\mathfrak{p} \in X; f \notin \mathfrak{p}\}$ . So it only remains to be checked that the structure sheaves on  $X_{f}$  and  $\operatorname{Spec} R_{f}$  agree. Now let  $g \in R$  and consider the distinguished open subset  $X_{fg} = (\operatorname{Spec} R_{f})_{g}$ . By proposition 5.1.12 (ii) we have

$$
\mathcal {O} _ {X _ {f}} \left(X _ {f g}\right) = \mathcal {O} _ {X} \left(X _ {f g}\right) = R _ {f g}
$$

and  $O_{\operatorname{Spec}R_f}((\operatorname{Spec}R_f)_g) = (R_f)_g = R_{fg}.$

So the rings of regular functions are the same for  $X_{f}$  and  $\operatorname{Spec} R_{f}$  on every distinguished open subset. But every open subset is the intersection of such distinguished opens, so the rings of regular functions must be the same on every open subset.

5.3. Schemes and prevarieties. Having defined affine schemes and their morphisms, we can now define schemes as objects that look locally like affine schemes — this is in parallel to the definition 2.4.1 of prevarieties.

Definition 5.3.1. A scheme is a locally ringed space  $(X, \mathcal{O}_X)$  that can be covered by open subsets  $U_i \subset X$  such that  $(U_i, \mathcal{O}_X|_{U_i})$  is isomorphic to an affine scheme  $\operatorname{Spec} R_i$  for all  $i$ . A morphism of schemes is a morphism as locally ringed spaces.

Remark 5.3.2. From the point of view of prevarieties, it would seem more natural to call the objects defined above preschemes, and then say that a scheme is a prescheme having the "Hausdorff" property, i.e. a prescheme with closed diagonal (see definition 2.5.1 and lemma 2.5.3). This is in fact the terminology of [M1], but nowadays everyone seems to adopt the definition that we gave above, and then say that a scheme having the "Hausdorff property" is a separated scheme.

From our definitions we see that prevarieties are in a sense special cases of schemes — if we have an affine variety  $X = Z(I) \subset \mathbb{A}^n$  with  $I \subset k[x_1, \ldots, x_n]$  an ideal, the scheme  $\operatorname{Spec} A(X)$  corresponds to  $X$  (where  $A(X) = k[x_1, \ldots, x_n]$  is the coordinate ring of  $X$ ); and any glueing along isomorphic open subsets that can be done in the category of prevarieties can be done equally well for the corresponding schemes. Hence we would like to say that every prevariety is a scheme. In the strict sense of the word this is not quite true

---

5. Schemes

however, because the topological space of a scheme contains a point for every irreducible closed subset, whereas the topological space of a prevariety consists only of the geometric points in the classical sense (i.e. the closed points). But of course there is a natural way to consider every prevariety as a scheme, by throwing in additional generic points for every irreducible closed subset. We give the precise statement and leave its proof as an exercise:

Proposition 5.3.3. Let  $k$  be an algebraically closed field, and let  $X$  be a prevariety over  $k$ . Let  $X_{sch}$  be the space of all non-empty closed irreducible subsets of  $X$ . Then  $X_{sch}$  is a scheme in a natural way. The open subsets of  $X$  correspond bijectively to the open subsets of  $X_{sch}$ , and for every open subset  $U$  of  $X$  (which can then also be considered as an open subset of  $X_{sch}$ ) we have  $\mathcal{O}_{X_{sch}}(U) = \mathcal{O}_X(U)$ . Every morphism  $X \to Y$  of prevarieties over  $k$  extends to a morphism  $X_{sch} \to Y_{sch}$  of schemes in a natural way.

Let us now investigate the properties of schemes that arise from prevarieties in this way. As we have mentioned already, the glueing of schemes from affine schemes is exactly the same as that of prevarieties from varieties. Hence the special properties of schemes that come from prevarieties can already be seen on the level of affine schemes. We have also seen above that in an affine scheme  $\operatorname{Spec} R$  the ring  $R$  corresponds to what is the coordinate ring  $A(X)$  of an affine variety. Moreover we know by remark 2.3.14 that the coordinate ring of an affine variety is a finitely generated  $k$ -algebra that is a domain. So we have to write down conditions on a scheme that reflect the property that its local patches  $\operatorname{Spec} R$  are not made from arbitrary rings, but rather from finitely generated  $k$ -algebras that are domains.

Definition 5.3.4. Let  $Y$  be a scheme. A scheme over  $Y$  is a scheme  $X$  together with a morphism  $X \to Y$ . A morphism of schemes  $X_{1}, X_{2}$  over  $Y$  is a morphism of schemes  $X_{1} \to X_{2}$  such that

![img-2.jpeg](images/img-2.jpeg)

commutes. If  $R$  is a ring, a scheme over  $R$  is a scheme over  $\operatorname{Spec} R$ .

A scheme  $X$  over  $Y$  is said to be of finite type over  $Y$  if there is a covering of  $Y$  by open affine subsets  $V_{i} = \operatorname{Spec} B_{i}$  such that  $f^{-1}(V_{i})$  can be covered by finitely many open affines  $U_{i,j} = \operatorname{Spec} A_{i,j}$ , where each  $A_{i,j}$  is a finitely generated  $B_{i}$ -algebra. In particular, a scheme  $X$  over a field  $k$  is of finite type over  $k$  if it can be covered by finitely many open affines  $U_{i} = \operatorname{Spec} A_{i}$ , where each  $A_{i}$  is a finitely generated  $k$ -algebra.

A scheme  $X$  is called reduced if the rings  $O_X(U)$  have no nilpotent elements for all open subsets  $U \subset X$ .

Now it is obvious what these conditions mean for an affine scheme  $\operatorname{Spec} R$ :

-  $\operatorname{Spec} R$  is a scheme over  $k$  if and only if we are given a morphism  $k \to R$ , i.e. if  $R$  is a  $k$ -algebra. Moreover, a morphism  $\operatorname{Spec} R \to \operatorname{Spec} S$  is a morphism of schemes over  $k$  if and only if the corresponding ring homomorphism  $S \to R$  is a morphism of  $k$ -algebras.
-  $\operatorname{Spec} R$  is of finite type over  $k$  if and only if  $R$  is a finitely generated  $k$ -algebra.
-  $\operatorname{Spec} R$  is reduced and irreducible if and only if  $f \cdot g = 0$  in  $R$  implies  $f = 0$  or  $g = 0$ , i.e. if and only if  $R$  is a domain. To see this, assume that  $f \cdot g = 0$ , but  $f \neq 0$  and  $g \neq 0$ . If  $f$  and  $g$  are the same up to a power, then  $R$  is not nilpotent-free, so  $\operatorname{Spec} R$  is not reduced. Otherwise, we get a decomposition of  $\operatorname{Spec} R$  into two proper closed subsets  $Z(f)$  and  $Z(g)$ , so  $\operatorname{Spec} R$  is not irreducible.

---

As glueing affine patches is allowed for varieties in the same way as for schemes, we get the following result:

###### Proposition 5.3.5.

Let $k$ be an algebraically closed field. There is a one-to-one correspondence between prevarieties over $k$ (and their morphisms) and reduced, irreducible schemes of finite type over $k$ (and their morphisms).

Hence, from now on a prevariety over $k$ will mean a reduced and irreducible scheme of finite type over $k$.

###### Remark 5.3.6.

As in the case of prevarieties, schemes and morphisms of schemes can (almost by definition) be glued together. As for glueing schemes lemma 2.4.7 holds in the same way (except that one may now also glue infinitely many patches $X_{i}$, and the isomorphic open subsets $U_{i,j}\subset X_{i}$ and $U_{j,i}\subset X_{j}$ can be empty, which might give rise to disconnected schemes). A morphism from the glued scheme $X$ to some scheme $Y$ can then be given by giving morphisms $X_{i}\to Y$ that are compatible on the overlaps in the obvious sense.

The following generalization of proposition 5.2.2 is an application of these glueing techniques.

###### Proposition 5.3.7.

Let $X$ be any scheme, and let $Y=\operatorname{Spec}R$ be an affine scheme. Then there is a one-to-one correspondence between morphisms $X\to Y$ and ring homomorphisms $R=\mathcal{O}_{Y}(Y)\to\mathcal{O}_{X}(X)$.

###### Proof.

Let $\{U_{i}\}$ be an open affine cover of $X$, and let $\{U_{i,j,k}\}$ be an open affine cover of $U_{i}\cap U_{j}$. Then by remark 5.3.6 giving a morphism $f:X\to Y$ is the same as giving morphisms $f_{i}:U_{i}\to Y$ such that $f_{i}$ and $f_{j}$ agree on $U_{i}\cap U_{j}$, i. e. such that $f_{i}|_{U_{i,j,k}}=f_{j}|_{U_{i,j,k}}$ for all $i,j,k$. But as the $U_{i}$ and $U_{i,j,k}$ are affine, by proposition 5.2.2 the morphisms $f_{i}$ and $f_{i}|_{U_{i,j,k}}$ correspond exactly to ring homomorphisms $\mathcal{O}_{Y}(Y)\to\mathcal{O}_{U_{i}}(U_{i})=\mathcal{O}_{X}(U_{i})$ and $\mathcal{O}_{Y}(Y)\to\mathcal{O}_{U_{i,j,k}}(U_{i,j,k})=\mathcal{O}_{X}(U_{i,j,k})$, respectively. Hence a morphism $f:X\to Y$ is the same as a collection of ring homomorphisms $f_{i}^{*}:\mathcal{O}_{Y}(Y)\to\mathcal{O}_{X}(U_{i})$ such that the compositions $\rho_{U_{i},U_{i,j,k}}\circ f_{i}^{*}:\mathcal{O}_{Y}(Y)\to\mathcal{O}_{X}(U_{i,j,k})$ and $\rho_{U_{j},U_{i,j,k}}\circ f_{j}^{*}:\mathcal{O}_{Y}(Y)\to\mathcal{O}_{X}(U_{i,j,k})$ agree for all $i,j,k$. But by the sheaf axiom for $\mathcal{O}_{X}$, this is exactly the data of a ring homomorphism $\mathcal{O}_{Y}(Y)\to\mathcal{O}_{X}(X)$. ∎

###### Remark 5.3.8.

By the above proposition, every scheme $X$ admits a unique morphism to $\operatorname{Spec}\mathbb{Z}$, determined by the natural map $\mathbb{Z}\to\mathcal{O}_{X}(X)$. More explicitly, on points this map is given by associating to every point $P\in X$ the characteristic of its residue field $k(P)$. In particular, if $X$ is a scheme over $\mathbb{C}$ (or any ground field of characteristic $0$ for that matter) then the morphism $X\to\operatorname{Spec}\mathbb{Z}$ maps every point to the zero ideal $(0)$.

### 5.4. Fiber products

In example 2.3.9 and exercise 2.6.13 we defined the product $X\times Y$ for two given prevarieties $X$ and $Y$ by giving the product set $X\times Y$ a suitable structure of a ringed space. The idea of this construction was that the coordinate ring $A(X\times Y)$ should be $A(X)\otimes A(Y)$ if $X$ and $Y$ are affine (see remark 2.3.13), and then to globalize this construction by glueing techniques. The characteristic property of the product $X\times Y$ was that giving a morphism to it is equivalent to giving a morphism to $X$ and a morphism to $Y$ (see lemma 2.3.11 and exercise 2.6.13).

Now we want to do the same thing for schemes. More generally, if $X$ and $Y$ are two schemes *over a third scheme* $S$ (i. e. if morphisms $f:X\to S$ and $g:Y\to S$ are given) we want to construct the so-called fiber product $X\times_{S}Y$, that should naïvely correspond to the points $(x,y)\in X\times Y$ such that $f(x)=g(y)$. As in the case of prevarieties this will be done by first constructing this product in the affine case, and then glueing these products together to obtain the fiber product of general schemes. We start by defining fiber products using the characteristic property mentioned above.

---

5. Schemes

Definition 5.4.1. Let  $f: X \to S$  and  $g: Y \to S$  be morphisms of schemes. We define the fiber product  $X \times_S Y$  to be a scheme together with "projection" morphisms  $\pi_X: X \times_S Y \to X$  and  $\pi_Y: X \times_S Y \to Y$  such that the square in the following diagram commutes, and such that for any scheme  $Z$  and morphisms  $Z \to X$  and  $Z \to Y$  making a commutative diagram with  $f$  and  $g$  there is a unique morphism  $Z \to X \times_S Y$  making the whole diagram commutative:

![img-3.jpeg](images/img-3.jpeg)

Let us first show that the fiber product is uniquely determined by this property:

Lemma 5.4.2. The fiber product  $X \times_S Y$  is unique if it exists. (In other words, if  $F_1$  and  $F_2$  are two fiber products satisfying the above characteristic property, then  $F_1$  and  $F_2$  are canonically isomorphic.)

Proof. Let  $F_{1}$  and  $F_{2}$  be two fiber products satisfying the characteristic property of the definition. In particular,  $F_{2}$  comes together with morphisms to  $X$  and  $Y$ . As  $F_{1}$  is a fiber product, we get a morphism  $\varphi : F_{2} \to F_{1}$

![img-4.jpeg](images/img-4.jpeg)

so that this diagram commutes. By symmetry, we get a morphism  $\psi : F_1 \to F_2$  as well. The diagram

![img-5.jpeg](images/img-5.jpeg)

is then commutative by construction. But the same diagram is commutative too if we replace  $\varphi \circ \psi$  by the identity morphism. So by the uniqueness part of the definition of a fiber product it follows that  $\varphi \circ \psi$  is the identity. Of course  $\psi \circ \varphi$  is then also the identity by symmetry. So  $F_{1}$  and  $F_{2}$  are canonically isomorphic.

Remark 5.4.3. The following two properties of fiber products are easily seen from the definition:

---

1. If $S\subset U$ is an open subset, then $X\times_{S}Y=X\times_{U}Y$ (morphisms from any $Z$ to $X$ and $Y$ commuting with $f$ and $g$ are then the same regardless of whether the base scheme is $S$ or $U$).
2. If $U\subset X$ and $V\subset Y$ are open subsets, then the fiber product

$U\times_{S}V=\pi_{X}^{-1}(U)\cap\pi_{Y}^{-1}(V)\subset X\times_{S}Y$

is an open subset of the total fiber product $X\times_{S}Y$.

Now we want to show that fiber products always exist. We have already mentioned that in the affine case, fiber products should correspond to tensor products in commutative algebra. So let us define the corresponding tensor products first.

###### Definition 5.4.4.

Let $R$ be a ring, and let $M$ and $N$ be $R$-modules. For every $m\in M$ and $n\in N$ let $m\otimes n$ be a formal symbol. We let $F$ be the “free $R$-module generated by the symbols $m\otimes n$”, i. e. $F$ is the $R$-module of formal *finite* linear combinations

$F=\big{\{}\sum_{i}r_{i}(m_{i}\otimes n_{i})\;;\;r_{i}\in R,m_{i}\in M,n_{i}\in N\big{\}}.$

Now we define the tensor product $M\otimes_{R}N$ of $M$ and $N$ over $R$ to be the $R$-module $F$ modulo the relations

$(m_{1}+m_{2})\otimes n=m_{1}\otimes n+m_{2}\otimes n,$
$m\otimes(n_{1}+n_{2})=m\otimes n_{1}+m\otimes n_{2},$
$r(m\otimes n)=(rm)\otimes n=m\otimes(rn)$

for all $m,m_{i}\in M$, $n,n_{i}\in N$, and $r\in R$. Obviously, $M\otimes_{R}N$ is an $R$-module as well.

###### Example 5.4.5.

1. Let $k$ be a field. Then $k[x]\otimes_{k}k[y]=k[x,y]$, where the isomorphism is given by

$k[x]\otimes_{k}k[y]\to k[x,y],\;f(x)\otimes g(y)\mapsto f(x)\cdot g(y)$

and

$k[x,y]\to k[x]\otimes_{k}k[y],\;\sum_{i,j}a_{i,j}x^{i}y^{j}\mapsto\sum_{i,j}a_{i,j}(x^{i}\otimes y^{j}).$
2. Let $R$ be a ring, and let $I_{1}$ and $I_{2}$ be ideals. Then $R/I_{1}$ and $R/I_{2}$ are $R$-modules, and we have $R/I_{1}\otimes_{R}R/I_{2}=R/(I_{1}+I_{2})$. In fact, the isomorphism is given by

$R/I_{1}\otimes_{R}R/I_{2}\to R/(I_{1}+I_{2}),\;r_{1}\otimes r_{2}\mapsto r_{1}\cdot r_{2}$

and

$R/(I_{1}+I_{2})\to R/I_{1}\otimes_{R}R/I_{2},\;r\mapsto r(1\otimes 1)=(r\otimes 1)=(1\otimes r).$
3. If $M$ is any $R$-module, then $M\otimes_{R}R=R\otimes_{R}M=M$.

###### Remark 5.4.6.

It is easy to see that the tensor product of modules satisfies the following characteristic property (which is exactly the same as that of definition 5.4.1, just with all the arrows reversed):

Let $R$, $M$, and $N$ be rings, and assume that we are given ring homomorphisms $f:R\to M$ and $g:R\to N$ (that make $M$ and $N$ into $R$-modules). Then for every ring $A$ and homomorphisms $M\to A$ and $N\to A$ making a commutative diagram with $f$ and $g$ there is a unique

---

5. Schemes

ring homomorphism  $M \otimes_R N \to A$  making the whole diagram commutative:

![img-6.jpeg](images/img-6.jpeg)

where  $M \to M \otimes_R N$  and  $N \to M \otimes_R N$  are the obvious maps  $m \mapsto m \otimes 1$  and  $n \mapsto 1 \otimes n$ . In fact, if  $a: M \to A$  and  $b: N \to A$  are the two ring homomorphisms, then  $M \otimes_R N \to A$  is given by  $m \otimes n \mapsto a(m) \cdot b(n)$ .

Using the tensor product of modules, we can now construct the fiber product of schemes.

Lemma 5.4.7. Let  $f: X \to S$  and  $g: Y \to S$  be morphisms of schemes. Then there is a fiber product  $X \times_S Y$ .

Proof. First assume that  $X, Y$ , and  $S$  are affine schemes, so  $X = \operatorname{Spec} M$ ,  $Y = \operatorname{Spec} N$ , and  $S = \operatorname{Spec} R$ . The morphisms  $X \to S$  and  $Y \to S$  make  $M$  and  $N$  into  $R$ -modules by proposition 5.2.2. We claim that  $\operatorname{Spec}(M \otimes_R N)$  is the fiber product  $X \times_S Y$ . Indeed, giving a morphism  $Z \to \operatorname{Spec}(M \otimes_R N)$  is the same as giving a homomorphism  $M \otimes_R N \to O_Z(Z)$  by proposition 5.3.7. By remark 5.4.6, this is the same as giving homomorphisms  $M \to O_Z(Z)$  and  $N \to O_Z(Z)$  that induce the same homomorphism on  $R$ , which again by proposition 5.3.7 is the same as giving morphisms  $Z \to X$  and  $Z \to Y$  that give rise to the same morphism from  $Z \to S$ . Hence  $\operatorname{Spec}(M \otimes_R N)$  is the desired product.

Now let  $X, Y$  and  $S$  be general schemes. Cover  $S$  by open affines  $S_{i}$ , then cover  $f^{-1}(S_{i})$  and  $g^{-1}(S_{i})$  by open affines  $X_{i,j}$  and  $Y_{i,k}$ , respectively. Consider the fiber products  $X_{i,j} \times_{S_i} Y_{i,k}$  that exist by the above tensor product construction. Note that by remark 5.4.3 (i) these will then be fiber products over  $S$  as well. Now if we have another such product  $X_{i',j'} \times_S Y_{i',k'}$ , both of them will contain the (unique) fiber product  $(X_{i,j} \cap X_{i',j'}) \times_S (Y_{i,k} \cap Y_{i',k'})$  as an open subset by remark 5.4.3 (ii), hence they can be glued along these isomorphic open subsets. It is obvious that the final scheme  $X \times_S Y$  obtained by glueing the patches satisfies the defining property of a fiber product.

Example 5.4.8. Let  $X$  and  $Y$  be prevarieties over a field  $k$ . Then the scheme-theoretic fiber product  $X \times_{\operatorname{Spec}k} Y$  is just the product prevariety  $X \times Y$  considered earlier. In fact, this follows from remark 2.3.13 in the affine case, and the glueing is done in the same way for prevarieties and schemes.

Consequently, we will still use the notation  $X \times Y$  to denote the fiber product  $X \times_{\operatorname{Spec}k} Y$  over  $\operatorname{Spec} k$ . Note however that for general schemes  $X$  and  $Y$  one also often defines  $X \times Y$  to be  $X \times_{\operatorname{Spec}\mathbb{Z}} Y$  (see remark 5.3.8). For schemes over  $k$ ,  $X \times_{\operatorname{Spec}k} Y$  and  $X \times_{\operatorname{Spec}\mathbb{Z}} Y$  will in general be different (see exercise 5.6.10), so one has to make clear what is meant by the notation  $X \times Y$ .

Example 5.4.9. Let  $Y_{1} \to X$  and  $Y_{2} \to X$  be morphisms of schemes that are "inclusion morphisms", i.e. the  $Y_{i}$  might be open subsets of  $X$ , or closed subschemes as in example 5.2.3. Then Then  $Y_{1} \times_{X} Y_{2}$  is defined to be the intersection scheme of  $Y_{1}$  and  $Y_{2}$  in  $X$  and is usually written  $Y_{1} \cap Y_{2}$ . For example, if  $X = \operatorname{Spec} R$ ,  $Y_{1} = \operatorname{Spec} R / I_{1}$ , and  $Y_{2} = \operatorname{Spec} R / I_{2}$  as in example 5.2.3, then  $Y_{1} \cap Y_{2}$  is  $\operatorname{Spec} R / (I_{1} + I_{2})$ , which is consistent with example 5.4.5 (ii).

---

Andreas Gathmann

Example 5.4.10. Let  $Y$  be a scheme, and let  $P \in Y$  be a point. Let  $k = k(P)$  be the residue field of  $P$ . Then there is a natural morphism  $\operatorname{Spec} k \to Y$  that maps the unique point of  $\operatorname{Spec} k$  to  $P$  and pulls back a section  $\varphi \in O_Y(U)$  (with  $P \in U$ ) to the element in  $k(P)$  determined by the composition of maps  $O_Y(U) \to O_{Y,P} \to k(P)$ .

Now let  $X \to Y$  be a morphism. Then the fiber product  $X \times_Y \operatorname{Spec} k$  (with the morphism  $\operatorname{Spec} k \to Y$  constructed above) is called the inverse image or fiber of  $X \to Y$  over the point  $P \in Y$  (hence the name "fiber product").

As an example, consider the morphism  $X = \mathbb{A}_{\mathbb{C}}^{1} \to Y = \mathbb{A}_{\mathbb{C}}^{1}$  given by  $x \mapsto y = x^2$ . Over the point  $0 \in Y$  the fiber is then  $\operatorname{Spec}(\mathbb{C}[x] \otimes_{\mathbb{C}[y]} \mathbb{C})$ , where the maps are given by  $y \in \mathbb{C}[y] \mapsto x^2 \in \mathbb{C}[x]$  and  $y \in \mathbb{C}[y] \mapsto 0 \in \mathbb{C}$ . This tensor product is equal to  $\mathbb{C}[x] / (x^2)$ , so the fiber over  $0$  is the double point  $\operatorname{Spec} \mathbb{C}[x] / (x^2)$ ; it is a non-reduced scheme and therefore different from the set-theoretic inverse image of  $0$  as defined earlier for prevarieties.

![img-7.jpeg](images/img-7.jpeg)

Example 5.4.11. Continuing the above example, one might want to think of a morphism  $X \to Y$  as some sort of fibered object, giving a scheme  $X \times_Y \operatorname{Spec} k(P)$  for every point  $P \in Y$ . (This is analogous to fibered objects in topology.) Now let  $f: Y' \to Y$  be any morphism. Then the fiber product  $X' = X \times_Y Y'$  has a natural projection morphism to  $Y'$ , and its fiber over a point  $P \in Y'$  is equal to the fiber of  $X \to Y$  over the point  $P \in Y$ . This is usually called a base extension of the morphism  $X \to Y$ . (It corresponds to e.g. the pull-back of a vector bundle in topology.)

![img-8.jpeg](images/img-8.jpeg)

5.5. Projective schemes. We know that projective varieties are a special important class of varieties that are not affine, but still can be described globally without using glueing techniques. They arise from looking at homogeneous ideals, i.e. graded coordinate rings. A completely analogous construction exists in the category of schemes, starting with a graded ring and looking at homogeneous ideals in it.

Definition 5.5.1. Let  $R$  be a graded ring (think of the homogeneous coordinate ring  $S(X)$  of a projective variety  $X$ ), i.e., a ring together with a decomposition  $R = \bigoplus_{d \geq 0} R^{(d)}$  into abelian groups such that  $R^{(d)} \cdot R^{(e)} \subset R^{(d + e)}$ . An element of  $R^{(d)}$  is called homogeneous of degree  $d$ . An ideal  $I \subset R$  is called homogeneous if it can be generated by homogeneous elements. Let  $R_{+}$  be the ideal  $\bigoplus_{d &gt; 0} R^{(d)}$ .

We define the set  $\operatorname{Proj} R$  to be the set of all homogeneous prime ideals  $\mathfrak{p} \subset R$  with  $R_{+} \not\subset \mathfrak{p}$  (compare this to theorem 3.2.6;  $R_{+}$  corresponds to the "irrelevant ideal"  $(x_0, \ldots, x_n) \subset k[x_0, \ldots, x_n]$ ). If  $I \subset R$  is a homogeneous ideal, we define  $Z(I) = \{\mathfrak{p} \in \operatorname{Proj} R; \mathfrak{p} \supset I\}$  to be the zero locus of  $I$ .

---

5. Schemes

The proof of the following lemma is the same as in the case of affine or projective varieties:

**Lemma 5.5.2.** Let $R$ be a graded ring.

(i) If $\{I_i\}$ is a family of homogeneous ideals of $R$ then $\bigcap_{i} Z(I_i) = Z(\sum_{i} I_i) \subset \operatorname{Proj} R$.

(ii) If $I_1, I_2 \subset R$ are homogeneous ideals then $Z(I_1) \cup Z(I_2) = Z(I_1I_2) \subset \operatorname{Proj} R$.

In particular, we can define a topology on $\operatorname{Proj} R$ by taking the subsets of the form $Z(I)$ for some $I$ to be the closed sets. Of course, the next thing to do is to define a structure of (locally) ringed space on $\operatorname{Proj} R$. This is in complete analogy to the affine case.

Next we have to define the rings of regular functions on $\operatorname{Proj} R$. This is a mixture of the case of affine schemes and projective varieties. We will more or less copy definition 5.1.11 for affine schemes, keeping in mind that in the projective (i.e. homogeneous) case our functions should locally be quotients of homogeneous elements of $R$ of the same degree.

**Definition 5.5.3.** Let $R$ be a graded ring, and let $X = \operatorname{Proj} R$. For every $\mathfrak{p} \in \operatorname{Proj} R$, let

$$
R_{\langle \mathfrak{p} \rangle} = \left\{ \frac{f}{g} ; g \notin \mathfrak{p} \text{ and } f, g \in R^{(d)} \text{ for some } d \right\}
$$

be the ring of degree zero elements of the localization of $R$ with respect to the multiplicative system of all homogeneous elements of $R$ that are not in $\mathfrak{p}$. (Of course, this will correspond to the local ring at the point $\mathfrak{p}$, see proposition 5.5.4 below.)

Now for every open subset $U \subset X$ we define $\mathcal{O}_X(U)$ to be

$$
\begin{array}{l}
\mathcal{O}_X(U) := \left\{ \varphi = (\varphi_{\mathfrak{p}})_{\mathfrak{p} \in U} \text{ with } \varphi_{\mathfrak{p}} \in R_{\langle \mathfrak{p} \rangle} \text{ for all } \mathfrak{p} \in U \right. \\
\quad \text{ such that } \varphi \text{ is locally of the form } \frac{f}{g} \text{ for } f, g \in R^{(d)} \text{ for some } d \text{ } \\
= \left\{ \varphi = (\varphi_{\mathfrak{p}})_{\mathfrak{p} \in U} \text{ with } \varphi_{\mathfrak{p}} \in R_{\langle \mathfrak{p} \rangle} \text{ for all } \mathfrak{p} \in U \right. \\
\quad \text{ such that for every } \mathfrak{p} \in U \text{ there is a neighborhood } V \text{ in } U \text{ and } f, g \in R^{(d)} \\
\text{ for some } d \text{ with } g \notin \mathfrak{q} \text{ and } \varphi_{\mathfrak{q}} = \frac{f}{g} \in R_{\langle \mathfrak{q} \rangle} \text{ for all } \mathfrak{q} \in V.
\end{array}
$$

It is clear from the local nature of the definition of $\mathcal{O}_X(U)$ that $\mathcal{O}_X$ is a sheaf.

**Proposition 5.5.4.** Let $R$ be a graded ring.

(i) For every $\mathfrak{p} \in \operatorname{Proj} R$ the stalk $\mathcal{O}_{X,\mathfrak{p}}$ is isomorphic to the local ring $R_{\langle \mathfrak{p} \rangle}$.

(ii) For every homogeneous $f \in R_+$, let $X_f \subset X$ be the distinguished open subset

$$
X_f := X \setminus Z(f) = \{ \mathfrak{p} \in \operatorname{Proj} R ; f \notin \mathfrak{p} \}.
$$

These open sets cover $X$, and for each such open set we have an isomorphism of locally ringed spaces $(X_f, \mathcal{O}_X|_{X_f}) \cong \operatorname{Spec} R_{\langle f \rangle}$, where

$$
R_{\langle f \rangle} = \left\{ \frac{g}{f^r} ; g \in R^{(r \cdot \deg f)} \right\}
$$

is the ring of elements of degree zero in the localized ring $R_f$.

In particular, $\operatorname{Proj} R$ is a scheme.

**Proof.** (i): There is a well-defined homomorphism

$$
\mathcal{O}_{X, \mathfrak{p}} \to R_{\langle \mathfrak{p} \rangle}, \quad (U, \varphi) \mapsto \varphi(\mathfrak{p}).
$$

The proof that this is an isomorphism is the same as in the affine case (see proposition 5.1.12 (i)).

(ii): Let $\mathfrak{p} \in X$ be a point. By definition, $R_+ \not\subset \mathfrak{p}$, so there is a $f \in R_+$ with $f \notin \mathfrak{p}$. But then $\mathfrak{p} \in X_f$; hence the open subsets of the form $X_f$ cover $X$.

---

Now fix $f\in R_{+}$; we will define an isomorphism $\psi:X_{f}\to\operatorname{Spec}R_{(f)}$. For any homogeneous ideal $I\subset R$, set $\psi(I):=(I\,R_{f})\cap R_{(f)}$. In particular, restricting this to prime ideals gives a map of sets $X_{f}\to\operatorname{Spec}R_{(f)}$, which is easily seen to be a bijection. Moreover, if $I\subset R$ is any ideal then $\psi(\mathfrak{p})\supset\psi(I)$ if and only if $\mathfrak{p}\supset I$, so $\psi:X_{f}\to\operatorname{Spec}R_{(f)}$ is a homeomorphism. Note also that for $\mathfrak{p}\in X_{f}$ the local rings

$\mathcal{O}_{\operatorname{Proj}R,\mathfrak{p}}=R_{(\mathfrak{p})}=\left\{\frac{g}{h}\text{ ; }g\text{ and }h\text{ homogeneous of the same degree, }h\notin\mathfrak{p}\right\}$

and

$\mathcal{O}_{\operatorname{Spec}R_{(f)},\psi(\mathfrak{p})}=(R_{(f)})_{\psi(\mathfrak{p})}$
$\qquad=\left\{\frac{g/f^{s}}{h/f^{s}}\text{ ; }g\text{ and }h\text{ homogeneous of degrees }r\cdot\deg f\text{ and }s\cdot\deg f,h\notin\mathfrak{p}\right\}$

are isomorphic for $f\notin\mathfrak{p}$. This gives rise to isomorphisms between the rings of regular functions $\mathcal{O}_{X_{f}}(U)$ and $\mathcal{O}_{\operatorname{Spec}R_{(f)}}(U)$ (as they are by definition made up of the local rings). ∎

###### Example 5.5.5.

If $k$ is an algebraically closed field, then by construction $\operatorname{Proj}k[x_{0},\ldots,x_{n}]$ is the scheme that corresponds to projective $n$-space $\mathbb{P}_{k}^{n}$ over $k$. More generally, the scheme associated to a projective variety $X$ is just $\operatorname{Proj}S(X)$, where $S(X)=k[x_{0},\ldots,x_{n}]/I(X)$ is the homogeneous coordinate ring of $X$.

Of course, scheme-theoretically we can now also consider schemes that are of the form $\operatorname{Proj}k[x_{0},\ldots,x_{n}]/I$ where $I$ is any homogeneous ideal of the polynomial ring. This allows projective “subschemes of $\mathbb{P}^{n}$” that are not necessarily irreducible or reduced. Let us turn this into a definition.

###### Definition 5.5.6.

Let $k$ be an algebraically closed field. A projective subscheme of $\mathbb{P}_{k}^{n}$ is a scheme of the form $\operatorname{Proj}k[x_{0},\ldots,x_{n}]/I$ for some homogeneous ideal $I$.

As mentioned above, every projective variety is a projective subscheme of $\mathbb{P}^{n}$. However, the category of projective subschemes of $\mathbb{P}^{n}$ is bigger because it contains schemes that are reducible (e. g. the union of the coordinate axes in the plane $\operatorname{Proj}k[x_{0},x_{1},x_{2}]/(x_{1}x_{2})$) or non-reduced (e. g. the double point $\operatorname{Proj}k[x_{0},x_{1}]/(x_{1}^{2})$).

As in the case of projective varieties, we now want to make precise the relation between projective subschemes of $\mathbb{P}^{n}$ and homogeneous ideals in $k[x_{0},\ldots,x_{n}]$. Note that the existence of the irrelevant ideal $(x_{0},\ldots,x_{n})$ implies that this correspondence is not one-to-one: the example $\operatorname{Proj}k[x_{0},\ldots,x_{n}]/(f)=\operatorname{Proj}k[x_{0},\ldots,x_{n}]/(fx_{0},\ldots,fx_{n})$ of remark 3.1.11 works for schemes as well.

###### Definition 5.5.7.

Let $I\subset S=k[x_{0},\ldots,x_{n}]$ be a homogeneous ideal. The saturation $\bar{I}$ of $I$ is defined to be

$\bar{I}=\{s\in S\text{ ; }x_{i}^{m}\cdot s\in I\text{ for some }m\text{ and all }i\}.$

###### Example 5.5.8.

If $I=(fx_{0},\ldots,fx_{n})$ then $\bar{I}=(f)$. So in this case the saturation removes the ambiguity of the ideal associated to a projective subscheme of $\mathbb{P}^{n}$. We will now show that this is true in general:

###### Lemma 5.5.9.

Let $I,J\subset S=k[x_{0},\ldots,x_{n}]$ be homogeneous ideals. Then

1. $\bar{I}$ is a homogeneous ideal.
2. $\operatorname{Proj}S/I=\operatorname{Proj}S/\bar{I}$.
3. $\operatorname{Proj}S/\bar{I}=\operatorname{Proj}S/\bar{J}$ if and only if $\bar{I}=\bar{J}$.
4. $I^{(d)}=\bar{I}^{(d)}$ for $d\gg 0$. Here and in the following we say that a statement holds for $d\gg 0$ if and only if it holds for large enough $d$, i. e. if and only if there is a number $D\geq 0$ such that the statement holds for all $d\geq D$

---

5. Schemes

Proof. (i): Let $s \in \bar{I}$ any (possibly non-homogeneous) element. Then by definition $x_{i}^{m} \cdot s \in I$ for some $m$ and all $i$. As $I$ is homogeneous, it follows that the graded pieces $x_{i}^{m} \cdot s^{(d)}$ are in $I$ as well for all $d$. Therefore, by definition, it follows that $s^{(d)} \in \bar{I}$ for all $i$. Hence $\bar{I}$ is homogeneous.

(ii): As the open affines $U_{i} \coloneqq \{x_{i} \neq 0\} \subset \mathbb{P}^{n}$ cover $\mathbb{P}^n$, it suffices to show that $U_{i} \cap \operatorname{Proj} S / I = U_{i} \cap \operatorname{Proj} S / \bar{I}$. But this is obvious as $I|_{x_i = 1} = \bar{I}_{x_i = 1}$.

(iii): The direction “$\Rightarrow$” is trivial. For “$\Leftarrow$” it suffices to show that the saturated ideal $\bar{I}$ can be recovered from the projective scheme $X = \operatorname{Proj} S / \bar{I}$ alone. Thinking of projective varieties, $\bar{I}$ should just be “the ideal $I(X)$ of $X$”, i.e. the ideal of functions vanishing on $X$. Now the elements of $S$ do not define functions on $X$, but after setting one $x_{i}$ equal to 1 they do define functions on $X \cap U_{i}$. Hence we can recover $\bar{I}$ from $X$ as

$$
\bar {I} = \left\{s \in S; s | _ {x _ {i} = 1} = 0 \text{ on } X \cap U _ {i} \text{ for all } i \right\}
$$

(note that the right hand side depends only on the scheme $X$ and not on its representation as $\operatorname{Proj} S / I$ for a certain $I$).

(iv): The inclusion $I^{(d)} \subset \bar{I}^{(d)}$ is obvious (for all $d$) as $I \subset \bar{I}$. So we only have to show that $\bar{I}^{(d)} \subset I^{(d)}$ for $d \gg 0$.

First of all note that $\bar{I}$ is finitely generated; let $f_{1},\ldots ,f_{m}$ be (homogeneous) generators. Let $D_{1}$ be the maximum degree of the $f_{i}$. Next, by definition of $\bar{I}$ there is a number $D_{2}$ such that $x_{j}^{d}\cdot f_{i}\in I$ for all $0\leq j\leq n$, $1\leq i\leq m$, and $d\geq D_2$. Set $D = D_{1} + (n + 1)D_{2}$.

Now let $f \in \bar{I}^{(d)}$ be any homogeneous element in the saturation of degree $d \geq D$. We can write $f$ as $\sum_{i} a_{i} f_{i}$, with the $a_{i}$ homogeneous of degree at least $(n + 1)D_{2}$. This degree bound implies that every monomial of $a_{i}$ contains at least one $x_{j}$ with a power of at least $D_{2}$. But then this power multiplied with $f_{i}$ lies in $I$ by construction. So it follows that $a_{i} f_{i} \in I$ for all $i$, and therefore $f \in I^{(d)}$.

Definition 5.5.10. If $X$ is a projective subscheme of $\mathbb{P}^n$, we let $I(X)$ be the saturation of any ideal $I \subset k[x_0, \ldots, x_n]$ such that $X = \operatorname{Proj} k[x_0, \ldots, x_n] / I$. (This is well-defined by lemma 5.5.9 (iii) and generalizes the notion of the ideal of a projective variety to projective subschemes of $\mathbb{P}^n$.) We define $S(X)$ to be $k[x_0, \ldots, x_n] / I(X)$. As usual, we call $I(X)$ the ideal of $X$ and $S(X)$ the homogeneous coordinate ring of $X$.

Corollary 5.5.11. There is a one-to-one correspondence between projective subschemes of $\mathbb{P}_k^n$ and saturated homogeneous ideals in $k[x_0,\ldots ,x_n]$, given by $X\mapsto I(X)$ and $I\mapsto \operatorname{Proj}k[x_0,\ldots ,x_n] / I$.

## 5.6. Exercises.

Exercise 5.6.1. Find all closed points of the real affine plane $\mathbb{A}_{\mathbb{R}}^2$. What are their residue fields?

Exercise 5.6.2. Let $f(x,y) = y^{2} - x^{2} - x^{3}$. Describe the affine scheme $X = \operatorname{Spec} R / (f)$ set-theoretically for the following rings $R$:

(i) $R = \mathbb{C}[x,y]$ (the standard polynomial ring),
(ii) $R = \mathbb{C}[x,y]_{(x,y)}$ (the localization of the polynomial ring at the origin),
(iii) $R = \mathbb{C}[[x,y]]$ (the ring of formal power series).

Interpret the results geometrically. In which of the three cases is $X$ irreducible?

Exercise 5.6.3. For each of these cases below give an example of an affine scheme $X$ with that property, or prove that such an $X$ does not exist:

(i) $X$ has infinitely many points, and $\dim X = 0$
(ii) $X$ has exactly one point, and $\dim X = 1$
(iii) $X$ has exactly two points, and $\dim X = 1$

---

Andreas Gathmann

$(x,y,z)$
- $X=\operatorname{Spec}R$ with $R\subset\mathbb{C}[x]$, and $\dim X=2$.

###### Exercise 5.6.4.

Let $X$ be a scheme, and let $Y$ be an irreducible closed subset of $X$. If $\eta_{Y}$ is the generic point of $Y$, we write $\mathcal{O}_{X,Y}$ for the stalk $\mathcal{O}_{X,\eta_{Y}}$. Show that $\mathcal{O}_{X,Y}$ is “the ring of rational functions on $X$ that are regular at a general point of $Y$”, i. e. it is isomorphic to the ring of equivalence classes of pairs $(U,\varphi)$, where $U\subset X$ is open with $U\cap Y\neq\emptyset$ and $\varphi\in\mathcal{O}_{X}(U)$, and where two such pairs $(U,\varphi)$ and $(U^{\prime},\varphi^{\prime})$ are called equivalent if there is an open subset $V\subset U\cap U^{\prime}$ with $V\cap Y\neq\emptyset$ such that $\varphi|_{V}=\varphi|_{V^{\prime}}$.

(In particular, if $X$ is a scheme that is a variety, then $\mathcal{O}_{X,\eta_{X}}$ is the function field of $X$ as defined earlier. Hence the stalks of the structure sheaf of a scheme generalize both the concepts of the local rings and the function field of a variety.)

###### Exercise 5.6.5.

Let $X$ be a scheme of finite type over an algebraically closed field $k$. Show that the closed points of $X$ are dense in every closed subset of $X$. Conversely, give an example of a scheme $X$ such that the closed points of $X$ are not dense in $X$.

###### Exercise 5.6.6.

Let $X=\{(x,y,z)\in\mathbb{C}^{3}\ ;\ xy=xz=yz=0\}$ be the union of the three coordinate lines in $\mathbb{C}^{3}$. Let $Y=\{(x,y)\in\mathbb{C}^{2}\ ;\ xy(x-y)=0\}$ be the union of three concurrent lines in $\mathbb{C}^{2}$.

Are $X$ and $Y$ isomorphic as schemes? (Hint: Define and compute the tangent spaces of $X$ and $Y$ at the origin.)

###### Exercise 5.6.7.

Let $X\subset\mathbb{P}^{3}$ the complex cubic surface

$X=\{(x_{0}:x_{1}:x_{2}:x_{3})\ ;\ x_{0}^{3}=x_{1}x_{2}x_{3}\}.$

1. Show that $X$ is singular.
2. Let $M\subset G(1,3)$ be the subset of the Grassmannian of lines in $\mathbb{P}^{3}$ that corresponds to all lines in $\mathbb{P}^{3}$ that lie in $X$. By writing down explicit equations for $M$, show that $M$ has the structure of a scheme in a natural way.
3. Show that the scheme $M$ contains exactly 3 points, but that it has length 27 over $\mathbb{C}$, i. e. it is of the form $M=\operatorname{Spec}R$ with $R$ a 27-dimensional $\mathbb{C}$-algebra. Hence in a certain sense we can say that even the singular cubic surface $X$ contains exactly 27 lines, if we count the lines with their correct multiplicities.

###### Exercise 5.6.8.

Let $k$ be an algebraically closed field. An $n$-fold point (over $k$) is a scheme of the form $X=\operatorname{Spec}R$ such that $X$ has only one point and $R$ is a $k$-algebra of vector space dimension $n$ over $k$ (i. e. $X$ has length $n$). Show that every double point is isomorphic to $\operatorname{Spec}k[x]/(x^{2})$. On the other hand, find two non-isomorphic triple points over $k$, and describe them geometrically.

###### Exercise 5.6.9.

Show that for a scheme $X$ the following are equivalent:

1. $X$ is reduced, i. e. for every open subset $U\subset X$ the ring $\mathcal{O}_{X}(U)$ has no nilpotent elements.
2. For any open subset $U_{i}$ of an open affine cover $\{U_{i}\}$ of $X$, the ring $\mathcal{O}_{X}(U_{i})$ has no nilpotent elements.
3. For every point $P\in X$ the local ring $\mathcal{O}_{X,P}$ has no nilpotent elements.

###### Exercise 5.6.10.

Show that $\mathbb{A}_{\mathbb{C}}^{2}\not\cong\mathbb{A}_{\mathbb{C}}^{1}\times_{\operatorname{Spec}\mathbb{Z}}\mathbb{A}_{\mathbb{C}}^{1}$.

###### Exercise 5.6.11.

Let $X=Z(x_{1}^{2}x_{2}+x_{1}x_{2}^{2}x_{3})\subset\mathbb{A}_{\mathbb{C}}^{3}$, and denote by $\pi_{i}$ the projection to the $i$-th coordinate. Compute the scheme-theoretic fibers $X_{x_{i}=a}=\pi_{i}^{-1}(a)$ for all $a\in\mathbb{C}$, and determine the set of isomorphism classes of these schemes.

###### Exercise 5.6.12.

Let $X$ be a prevariety over an algebraically closed field $k$, and let $P\in X$ be a (closed) point of $X$. Let $D=\operatorname{Spec}k[x]/(x^{2})$ be the “double point”. Show that the tangent space $T_{X,P}$ to $X$ at $P$ can be canonically identified with the set of morphisms $D\to X$ that map the unique point of $D$ to $P$.

###### Ex

---

(In particular, this gives the set of morphisms $D\to X$ with fixed image point $P\in X$ the structure of a vector space over $k$. Can you see directly how to add two such morphisms, and how to multiply them with a scalar in $k$ ?)

###### Exercise 5.6.13.

Let $X$ be an affine variety, let $Y$ be a closed subscheme of $X$ defined by the ideal $I\subset A(X)$, and let $\tilde{X}$ be the blow-up of $X$ at $I$. Show that:

1. $\tilde{X}=\mathrm{Proj}(\bigoplus_{d\geq 0}I^{d})$, where we set $I^{0}:=A(X)$.
2. The projection map $\tilde{X}\to X$ is the morphism induced by the ring homomorphism $I^{0}\to\bigoplus_{d\geq 0}I^{d}$.
3. The exceptional divisor of the blow-up, i. e. the fiber $Y\times_{X}\tilde{X}$ of the blow-up $\tilde{X}\to X$ over $Y$, is isomorphic to $\mathrm{Proj}(\bigoplus_{d\geq 0}I^{d}/I^{d+1})$.

###### Exercise 5.6.14.

Let $X=\mathrm{Spec}\,R$ and $Y=\mathrm{Spec}\,S$ be affine schemes. Show that the disjoint union $X\sqcup Y$ is an affine scheme with

$X\sqcup Y=\mathrm{Spec}(R\times S),$

where as usual $R\times S=\{(r,s)\;;\;r\in R,s\in S\}$ (with addition and multiplication defined componentwise).