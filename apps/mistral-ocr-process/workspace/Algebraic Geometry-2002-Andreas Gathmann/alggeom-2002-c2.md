2. Functions, morphisms, and varieties

> If $X\subset\mathbb{A}^{n}$ is an affine variety, we define the function field $K(X)$ of $X$ to be the quotient field of the coordinate ring $A(X)=k[x_{1},\ldots,x_{n}]/I(X)$; this can be thought of as the field of rational functions on $X$. For a point $P\in X$ the local ring $\mathcal{O}_{X,P}$ is the subring of $K(X)$ of all functions that are regular (i. e. well-defined) at $P$, and for $U\subset X$ an open subset we let $\mathcal{O}_{X}(U)$ be the subring of $K(X)$ of all functions that are regular at every $P\in U$. The ring of functions that are regular on all of $X$ is precisely $A(X)$.

Given two ringed spaces $(X,\mathcal{O}_{X})$, $(Y,\mathcal{O}_{Y})$ with the property that their structure sheaves are sheaves of $k$-valued functions, a set-theoretic map $f:X\to Y$ determines a pull-back map $f^{*}$ from $k$-valued functions on $Y$ to $k$-valued functions on $X$ by composition. We say that $f$ is a morphism if $f$ is continuous and $f^{*}\mathcal{O}_{Y}(U)\subset\mathcal{O}_{X}(f^{-1}(U))$ for all open sets $U$ in $Y$. In particular, this defines morphisms between affine varieties and their open subsets. Morphisms $X\to Y$ between affine varieties correspond exactly to $k$-algebra homomorphisms $A(Y)\to A(X)$.

In complete analogy to the theory of manifolds, we then define a prevariety to be a ringed space (whose structure sheaf is a sheaf of $k$-valued functions and) that is locally isomorphic to an affine variety. Correspondingly, there is a general way to construct prevarieties and morphisms between them by taking affine varieties (resp. morphisms between them) and patching them together. Affine varieties and their open subsets are simple examples of prevarieties, but we also get more complicated spaces as e. g. $\mathbb{P}^{1}$ and the affine line with a doubled origin. A prevariety $X$ is called a variety if the diagonal $\Delta(X)\subset X\times X$ is closed, i. e. if $X$ does not contain “doubled points”.

### 2.1. Functions on affine varieties

After having defined affine varieties, our next goal must of course be to say what the maps between them should be. Let us first look at the easiest case: “regular functions”, i. e. maps to the ground field $k=\mathbb{A}^{1}$. They should be thought of as the analogue of continuous functions in topology, or differentiable functions in real analysis, or holomorphic functions in complex analysis. Of course, in the case of algebraic geometry we want to have algebraic functions, i. e. (quotients of) polynomial functions.

###### Definition 2.1.1.

Let $X\subset\mathbb{A}^{n}$ be an affine variety. We call

$\bm{A(X)}:=k[x_{1},\ldots,x_{n}]/I(X)$

the coordinate ring of $X$.

###### Remark 2.1.2.

The coordinate ring of $X$ should be thought of as the ring of polynomial functions on $X$. In fact, for any $P\in X$ an element $f\in A(X)$ determines a polynomial map $X\to k$ (usually also denoted by $f$) given by $f\mapsto f(P)$:

- this is well-defined, because all functions in $I(X)$ vanish on $X$ by definition,
- if the function $f:X\to k$ is identically zero then $f\in I(X)$ by definition, so $f=0$ in $A(X)$.

Note that $I(X)$ is a prime ideal by lemma 1.3.4, so $A(X)$ is an integral domain. Hence we can make the following definition:

###### Definition 2.1.3.

Let $X\subset\mathbb{A}^{n}$ be an affine variety. The quotient field $\bm{K(X)}$ of $A(X)$ is called the field of rational functions on $X$.

###### Remark 2.1.4.

Recall that the quotient field $K$ of an integral domain $R$ is defined to be the set of pairs $(f,g)$ with $f,g\in R$, $g\neq 0$, modulo the equivalence relation

$(f,g)\sim(f^{\prime},g^{\prime})\iff fg^{\prime}-gf^{\prime}=0.$

---

element $(f,g)$ of $K$ is usually written as $\frac{f}{g}$, and we think of it as the formal quotient of two ring elements. Addition of two such formal quotients is defined in the same way as you would expect to add fractions, namely

$\frac{f}{g}+\frac{f^{\prime}}{g^{\prime}}:=\frac{fg^{\prime}+gf^{\prime}}{gg^{\prime}},$

and similarly for subtraction, multiplication, and division. This makes $K(X)$ into a field. In the case where $R=A(X)$ is the coordinate ring of an affine variety, we can therefore think of elements of $K(X)$ as being quotients of polynomial functions. We have to be very careful with this interpretation though, see example 2.1.7 and lemma 2.1.8.

Now let us define what we want to mean by a regular function on an open subset $U$ of an affine variety $X$. This is more or less obvious: a regular function should be a rational function that is well-defined at all points of $U$:

###### Definition 2.1.5.

Let $X\subset\mathbb{A}^{n}$ be an affine variety and let $P\in X$ be a point. We call

$\bm{O_{X,P}}:=\left\{\frac{f}{g}\mbox{ ; }f,g\in A(X)\mbox{ and }g(P)\neq 0\right\}\subset K(X)$

the local ring of $X$ at the point $P$. Obviously, this should be thought of as the rational functions that are regular at $P$. If $U\subset X$ is a non-empty open subset, we set

$\bm{O_{X}(U)}:=\bigcap_{P\in U}\mathcal{O}_{X,P}.$

This is a subring of $K(X)$. We call this the ring of regular functions on $U$.

###### Remark 2.1.6.

The set $\mathfrak{m_{X,P}}:=\{f\in A(X)\mbox{ ; }f(P)=0\}$ of all functions that vanish at $P$ is an ideal in $A(X)$. This is a maximal ideal, as $A(X)/\mathfrak{m}_{X,P}\cong k$, the isomorphism being evaluation of the polynomial at the point $P$. With this definition, $\mathcal{O}_{X,P}$ is just the localization of the ring $A(X)$ at the maximal ideal $\mathfrak{m}_{X,P}$. We will explain in lemma 2.2.10 where the name “local” (resp. “localization”) comes from.

###### Example 2.1.7.

We have just defined regular functions on an open subset of an affine variety $X\subset\mathbb{A}^{n}$ to be rational functions, i. e. elements in the quotient field $K(X)$, with certain properties. This means that every such function can be written as the “quotient” of two elements in $A(X)$. It does *not* mean however that we can always write a regular function as the quotient of two polynomials in $k[x_{1},\ldots,n_{n}]$. Here is an example showing this. Let $X\subset\mathbb{A}^{4}$ be the variety defined by the equation $x_{1}x_{4}=x_{2}x_{3}$, and let $U\subset X$ be the open subset of all points in $X$ where $x_{2}\neq 0$ or $x_{4}\neq 0$. The function $\frac{x_{1}}{x_{2}}$ is defined at all points of $X$ where $x_{2}\neq 0$, and the function $\frac{x_{3}}{x_{4}}$ is defined at points of $X$ where $x_{4}\neq 0$. By the equation of $X$, these two functions coincide where they are both defined; in other words

$\frac{x_{1}}{x_{2}}=\frac{x_{3}}{x_{4}}\in K(X)$

by remark 2.1.4. So this gives rise to a regular function on $U$. But there is no representation of this function as a quotient of two polynomials in $k[x_{1},x_{2},x_{3},x_{4}]$ that works on all of $U$ — we have to use different representations at different points.

As we will usually want to write down regular functions as quotients of polynomials, we should prove a precise statement how regular functions can be patched together from different polynomial representations:

###### Lemma 2.1.8.

The following definition of regular functions is equivalent to the one of definition 2.1.5:

Let $U$ be an open subset of an affine variety $X\subset\mathbb{A}^{n}$. A set-theoretic map $\varphi:U\to k$ is called regular at the point $P\in U$ if there is a neighborhood $V$ of $P$ in $U$ such that there are

---

polynomials $f,g\in k[x_{1},\ldots,x_{n}]$ with $g(Q)\neq 0$ and $\varphi(Q)=\frac{f(Q)}{g(Q)}$ for all $Q\in V$. It is called regular on $U$ if it is regular at every point in $U$.

###### Proof.

It is obvious that an element of the ring of regular functions on $U$ determines a regular function in the sense of the lemma.

Conversely, let $\varphi:U\to\mathbb{A}^{1}$ be a regular function in the sense of the lemma. Let $P\in U$ be any point, then there are polynomials $f,g$ such that $g(Q)\neq 0$ and $\varphi(Q)=\frac{f(Q)}{g(Q)}$ for all points $Q$ in some neighborhood $V$ of $P$. We claim that $\frac{f}{g}\in K(X)$ is the element in the ring of regular functions that we seek.

In fact, all we have to show is that this element does not depend on the choices that we made. So let $P^{\prime}\in U$ be another point (not necessarily distinct from $P$), and suppose that there are polynomials $f^{\prime},g^{\prime}$ such that $\frac{f}{g}=\frac{f^{\prime}}{g^{\prime}}$ on some neighborhood $V^{\prime}$ of $P^{\prime}$. Then $fg^{\prime}=gf^{\prime}$ on $V\cap V^{\prime}$ and hence on $X$ as $V\cap V^{\prime}$ is dense in $X$ by remark 1.3.17. In other words, $fg^{\prime}-gf^{\prime}\in I(X)$, so it is zero in $A(X)$, i. e. $\frac{f}{g}=\frac{f^{\prime}}{g^{\prime}}\in K(X)$. ∎

###### Remark 2.1.9.

An almost trivial but remarkable consequence of our definition of regular functions is the following: let $U\subset V$ be non-empty open subsets of an affine variety $X$. If $\varphi_{1},\varphi_{2}:V\to k$ are two regular functions on $V$ that agree on $U$, then they agree on all of $V$. This is obvious because the ring of regular functions (on any non-empty open subset) is a subring of the function field $K(X)$, so if two such regular functions agree this just means that they are the same element of $K(X)$. Of course, this is not surprising as open subsets are always dense, so if we know a regular function on an open subset it is intuitively clear that we know it almost everywhere anyway.

The interesting remark here is that the very same statement holds in complex analysis for holomorphic functions as well (or more generally, in real analysis for analytic functions): two holomorphic functions on a (connected) open subset $U\subset\mathbb{C}^{n}$ must be the same if they agree on any smaller open subset $V\subset U$. This is called the identity theorem for holomorphic functions — in complex analysis this is a real theorem because there the open subset $V$ can be “very small”, so the statement that the extension to $U$ is unique is a lot more surprising than it is here in algebraic geometry. Still this is an example of a theorem that is true in literally the same way in both algebraic and complex geometry, although these two theories are quite different a priori.

Let us compute the rings $\mathcal{O}_{X}(U)$ explicitly in the cases where $U$ is the complement of the zero locus of just a single polynomial.

###### Proposition 2.1.10.

Let $X\subset\mathbb{A}^{n}$ be an affine variety. Let $f\in A(X)$ and $X_{f}=\{P\in X\ ;\ f(P)\neq 0\}$. (Open subsets of this form are called distinguished open subsets.) Then

$\mathcal{O}_{X}(X_{f})=A(X)_{f}:=\left\{\frac{g}{f^{r}}\ ;\ g\in A(X)\ \text{and}\ r\geq 0\right\}.$

In particular, $\mathcal{O}_{X}(X)=A(X)$, i. e. any regular function on $X$ is polynomial (take $f=1$).

###### Proof.

It is obvious that $A(X)_{f}\subset\mathcal{O}_{X}(X_{f})$, so let us prove the converse. Let $\varphi\in\mathcal{O}_{X}(X_{f})\subset K(X)$. Let $J=\{g\in A(X)\ ;\ g\varphi\in A(X)\}$. This is an ideal in $A(X)$; we want to show that $f^{r}\in J$ for some $r$.

For any $P\in X_{f}$ we know that $\varphi\in\mathcal{O}_{X,P}$, so $\varphi=\frac{h}{g}$ with $g\neq 0$ in a neighborhood of $P$. In particular $g\in J$, so $J$ contains an element not vanishing at $P$. This means that the zero locus of the ideal $I(X)+J\subset k[x_{1},\ldots,x_{n}]$ is contained in the set $\{P\in X\ ;\ f(P)=0\}$, or in other words that $Z(I(X)+J)\subset Z(f)$. By proposition 1.2.9 (i) it follows that $I(Z(f))\subset I(Z(I(X)+J))$. So $f^{\prime}\in I(Z(I(X)+J))$, where $f^{\prime}\in k[x_{1},\ldots,x_{n}]$ is a representative of $f$. Therefore $f^{\prime}{}^{\prime}\in I(X)+J$ for some $r$ by the Nullstellensatz 1.2.9 (iii), and so $f^{r}\in J$. ∎

---

###### Remark 2.1.11.

In the proof of proposition 2.1.10 we had to use the Nullstellensatz again. In fact, the statement is false if the ground field is not algebraically closed, as you can see from the example of the function $\frac{1}{x^{2}+1}$ that is regular on all of $\mathbb{A}^{1}(\mathbb{R})$, but not polynomial.

###### Example 2.1.12.

Probably the easiest case of an open subset of an affine variety $X$ that is not of the form $X_{f}$ as in proposition 2.1.10 is the complement $U=\mathbb{C}^{2}\backslash\{0\}$ of the origin in the affine plane. Let us compute $\mathcal{O}_{\mathbb{C}^{2}}(U)$. By definition 2.1.5 any element $\varphi\in\mathcal{O}_{\mathbb{C}^{2}}(U)\subset\mathbb{C}(x,y)$ is globally the quotient $\varphi=\frac{f}{g}$ of two polynomials $f,g\in\mathbb{C}[x,y]$. The condition that we have to satisfy is that $g(x,y)\neq 0$ for all $(x,y)\neq(0,0)$. We claim that this implies that $g$ is constant. (In fact, this follows intuitively from the fact that a single equation can cut down the dimension of a space by only $1$, so the zero locus of the polynomial $g$ cannot only be the origin in $\mathbb{C}^{2}$. But we have not proved this rigorously yet.)

We know already by the Nullstellensatz that there is no non-constant polynomial that has empty zero locus in $\mathbb{C}^{2}$, so we can assume that $g$ vanishes on $(0,0)$. If we write $g$ as

$g(x,y)=f_{0}(x)+f_{1}(x)\cdot y+f_{2}(x)\cdot y^{2}+\dots+f_{n}(x)\cdot y^{n},$

this means that $f_{0}(0)=0$. We claim that $f_{0}(x)$ must be of the form $x^{m}$ for some $m$. In fact:

- if $f_{0}$ is the zero polynomial, then $g(x,y)$ contains $y$ as a factor and hence the whole $x$-axis in its zero locus,
- if $f_{0}$ contains more than one monomial, $f_{0}$ has a zero $x_{0}\neq 0$, and hence $g(x_{0},0)=0$.

So $g(x,y)$ is of the form

$g(x,y)=x^{m}+f_{1}(x)\cdot y+f_{2}(x)\cdot y^{2}+\dots+f_{n}(x)\cdot y^{n}.$

Now set $y=\varepsilon$ for some small $\varepsilon$. As $g(x,0)=x^{m}$ and all $f_{i}$ are continuous, the restriction $g(x,\varepsilon)$ cannot be the zero or a constant polynomial. Hence $g(x,\varepsilon)$ vanishes for some $x$, which is a contradiction.

So we see that we cannot have any denominators, i. e. $\mathcal{O}_{\mathbb{C}^{2}}(U)=\mathbb{C}[x,y]$. In other words, a regular function on $\mathbb{C}^{2}\backslash\{0\}$ is always regular on all of $\mathbb{C}^{2}$. This is another example of a statement that is known from complex analysis for holomorphic functions, known as the removable singularity theorem.

### 2.2. Sheaves

We have seen in lemma 2.1.8 that regular functions on affine varieties are defined in terms of local properties: they are set-theoretic functions that can locally be written as quotients of polynomials. Local constructions of function-like objects occur in many places in algebraic geometry (and also in many other “topological” fields of mathematics), so we should formalize the idea of such objects. This will also give us an “automatic” definition of morphisms between affine varieties in section 2.3.

###### Definition 2.2.1.

A presheaf $\mathcal{F}$ of rings on a topological space $X$ consists of the data:

- for every open set $U\subset X$ a ring $\mathcal{F}(U)$ (think of this as the ring of functions on $U$),
- for every inclusion $U\subset V$ of open sets in $X$ a ring homomorphism $\rho_{V,U}:\mathcal{F}(V)\to\mathcal{F}(U)$ called the restriction map (think of this as the usual restriction of functions to a subset),

such that

- $\mathcal{F}(\emptyset)=0$,
- $\rho_{U,U}$ is the identity map for all $U$,
- for any inclusion $U\subset V\subset W$ of open sets in $X$ we have $\rho_{V,U}\circ\rho_{W,V}=\rho_{W,U}$.

The elements of $\mathcal{F}(U)$ are usually called the sections of $\mathcal{F}$ over $U$, and the restriction maps $\rho_{V,U}$ are written as $f\mapsto f|_{U}$.

---

A presheaf $\mathcal{F}$ of rings is called a sheaf of rings if it satisfies the following glueing property: if $U\subset X$ is an open set, $\{U_{i}\}$ an open cover of $U$ and $f_{i}\in\mathcal{F}(U_{i})$ sections for all $i$ such that $f_{i}|_{U_{i}\cap U_{j}}=f_{j}|_{U_{i}\cap U_{j}}$ for all $i,j$, then there is a unique $f\in\mathcal{F}(U)$ such that $f|_{U_{i}}=f_{i}$ for all $i$.

###### Remark 2.2.2.

In the same way one can define (pre-)sheaves of Abelian groups / $k$-algebras etc., by requiring that all $\mathcal{F}(U)$ are objects and all $\rho_{V,U}$ are morphisms in the corresponding category.

###### Example 2.2.3.

If $X\subset\mathbb{A}^{n}$ is an affine variety, then the rings $\mathcal{O}_{X}(U)$ of regular functions on open subsets of $X$ (with the obvious restriction maps $\mathcal{O}_{X}(V)\to\mathcal{O}_{X}(U)$ for $U\subset V$) form a sheaf of rings $\mathcal{O}_{X}$, the sheaf of regular functions or structure sheaf on $X$. In fact, all defining properties of presheaves are obvious, and the glueing property of sheaves is easily seen from the description of regular functions in lemma 2.1.8.

###### Example 2.2.4.

Here are some examples from other fields of mathematics: Let $X=\mathbb{R}^{n}$, and for any open subset $U\subset X$ let $\mathcal{F}(U)$ be the ring of continuous functions on $U$. Together with the obvious restriction maps, these rings $\mathcal{F}(U)$ form a sheaf, the *sheaf of continuous functions*. In the same way we can define the sheaf of $k$ times differentiable functions, analytic functions, holomorphic functions on $\mathbb{C}^{n}$, and so on. The same definitions can be applied if $X$ is a real or complex manifold instead of just $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$.

In all these examples, the sheaves just defined “are” precisely the functions that are considered to be morphisms in the corresponding category (for example, in complex analysis the morphisms are just the holomorphic maps). This is usually expressed in the following way: a pair $(X,\mathcal{F})$ where $X$ is a topological space and $\mathcal{F}$ is a sheaf of rings on $X$ is called a ringed space. The sheaf $\mathcal{F}$ is then called the structure sheaf of this ringed space and usually written $\mathcal{O}_{X}$. Hence we have just given affine varieties the structure of a ringed space. (Although being general, this terminology will usually only be applied if $\mathcal{F}$ actually has an interpretation as the space of functions that are considered to be morphisms in the corresponding category.)

###### Remark 2.2.5.

Intuitively speaking, any “function-like” object forms a presheaf; it is a sheaf if the conditions imposed on the “functions” are local. Here is an example illustrating this fact. Let $X=\mathbb{R}$ be the real line. For $U\subset X$ open and non-empty let $\mathcal{F}(U)$ be the ring of constant (real-valued) functions on $U$, i. e. $\mathcal{F}(U)\cong\mathbb{R}$ for all $U$. Let $\rho_{V,U}$ for $U\subset V$ be the obvious restriction maps. Then $\mathcal{F}$ is obviously a presheaf, but not a sheaf. This is because being constant is *not a local property*; it means that $f(P)=f(Q)$ for all $P$ and $Q$ that are possibly quite far away. For example, let $U=(0,1)\cup(2,3)$. Then $U$ has an open cover $U=U_{1}\cup U_{2}$ with $U_{1}=(0,1)$ and $U_{2}=(2,3)$. Let $f_{1}:U_{1}\to\mathbb{R}$ be the constant function $0$, and let $f_{2}:U_{2}\to\mathbb{R}$ be the constant function $1$. Then $f_{1}$ and $f_{2}$ trivially agree on the overlap $U_{1}\cap U_{2}=\emptyset$, but there is no *constant* function on $U$ that restricts to both $f_{1}$ and $f_{2}$ on $U_{1}$ and $U_{2}$, respectively. There is however a uniquely defined *locally constant* function on $U$ with that property. In fact, it is easy to see that the *locally constant* functions on $X$ do form a sheaf.

###### Remark 2.2.6.

If $\mathcal{F}$ is a sheaf on $X$ and $U\subset X$ is an open subset, then one defines the restriction of $\mathcal{F}$ to $U$, denoted $\mathcal{F}|_{U}$, by $(\mathcal{F}|_{U})(V)=\mathcal{F}(V)$ for all open subsets $V\subset U$. Obviously, this is again a sheaf.

Finally, let us see how the local rings of an affine variety appear in the language of sheaves.

###### Definition 2.2.7.

Let $X$ be a topological space, $P\in X$, and $\mathcal{F}$ a (pre-)sheaf on $X$. Consider pairs $(U,\varphi)$ where $U$ is an open neighborhood of $P$ and $\varphi\in\mathcal{F}(U)$ a section of $\mathcal{F}$ over $U$. We call two such pairs $(U,\varphi)$ and $(U^{\prime},\varphi^{\prime})$ equivalent if there is an open neighborhood $V$ of

---

$P$ with $V\subset U\cap U^{\prime}$ such that $\varphi|_{V}=\varphi^{\prime}|_{V}$. (Note that this is in fact an equivalence relation.) The set of all such pairs modulo this equivalence relation is called the stalk $\mathcal{F}_{P}$ of $\mathcal{F}$ at $P$, its elements are called germs of $\mathcal{F}$.

###### Remark 2.2.8.

If $\mathcal{F}$ is a (pre-)sheaf of rings (or $k$-algebras, Abelian groups, etc.) then the stalks of $\mathcal{F}$ are rings (or $k$-algebras, Abelian groups, etc.).

###### Remark 2.2.9.

The interpretation of the stalk of a sheaf is obviously that its elements are sections of $\mathcal{F}$ that are defined in an (arbitrarily small) neighborhood around $P$. Hence e. g. on the real line the germ of a differentiable function at a point $P$ allows you to compute the derivative of this function at $P$, but none of the actual values of the function at any point besides $P$. On the other hand, we have seen in remark 2.1.9 that holomorphic functions on a (connected) complex manifold are already determined by their values on any open set, so germs of holomorphic functions carry “much more information” than germs of differentiable functions. In algebraic geometry, this is similar: it is already quite obvious that germs of regular functions must carry much information, as the open subsets in the Zariski topology are so big. We will now show that the stalk of $\mathcal{O}_{X}$ at a point $P$ is exactly the local ring $\mathcal{O}_{X,P}$, which finally gives a good motivation for the name “local ring”.

###### Lemma 2.2.10.

Let $X$ be an affine variety and $P\in X$. The stalk of $\mathcal{O}_{X}$ at $P$ is $\mathcal{O}_{X,P}$.

###### Proof.

Recall that $\mathcal{O}_{X}(U)\subset\mathcal{O}_{X,P}\subset K(X)$ for all $P\in U$ by definition.

Therefore, if we are given a pair $(U,\varphi)$ with $P\in U$ and $\varphi\in\mathcal{O}_{X}(U)$, we see that $\varphi\in\mathcal{O}_{X,P}$ determines an element in the local ring. If we have another equivalent pair $(U^{\prime},\varphi^{\prime})$, then $\varphi$ and $\varphi^{\prime}$ agree on some $V$ with $P\in V\subset U\cap U^{\prime}$ by definition, so they determine the same element in $\mathcal{O}_{X}(V)$ and hence in $\mathcal{O}_{X,P}$.

Conversely, if $\varphi\in\mathcal{O}_{X,P}$ is an element in the local ring, we can write it as $\varphi=\frac{f}{g}$ with polynomials $f,g$ such that $g(P)\neq 0$. Then there must be a neighborhood $U$ of $P$ on which $g$ is non-zero, and therefore the $(U,\varphi)$ defines an element in the stalk of $\mathcal{O}_{X}$ at $P$. ∎

### 2.3. Morphisms between affine varieties

Having given the structure of ringed spaces to affine varieties, there is a natural way to define morphisms between them. In this section we will allow ourselves to view morphisms as set-theoretic maps on the underlying topological spaces with additional properties (see lemma 2.1.8).

###### Definition 2.3.1.

Let $(X,\mathcal{O}_{X})$ and $(Y,\mathcal{O}_{Y})$ be ringed spaces whose structure sheaves $\mathcal{O}_{X}$ and $\mathcal{O}_{Y}$ are sheaves of $k$-valued functions (in the case we are considering right now $X$ and $Y$ will be affine varieties or open subsets of affine varieties). Let $f:X\to Y$ be a set-theoretic map.

1. If $\varphi:U\to k$ is a $k$-valued (set-theoretic) function on an open subset $U$ of $Y$, the composition $\varphi\circ f:f^{-1}(U)\to k$ is again a set-theoretic function. It is denoted by $f^{*}\varphi$ and is called the pull-back of $\varphi$.
2. The map $f$ is called a morphism if it is continuous, and if it pulls back regular functions to regular functions, i. e. if $f^{*}\mathcal{O}_{Y}(U)\subset\mathcal{O}_{X}(f^{-1}(U))$ for all open $U\subset Y$.

###### Remark 2.3.2.

Recall that a function $f:X\to Y$ between topological spaces is called continuous if inverse images of open subsets are always open. In the above definition (ii), the requirement that $f$ be continuous is therefore necessary to formulate the second condition, as it ensures that $f^{-1}(U)$ is open, so that $\mathcal{O}_{X}(f^{-1}(U))$ is well-defined.

###### Remark 2.3.3.

In our context of algebraic geometry $\mathcal{O}_{X}$ and $\mathcal{O}_{Y}$ will always be the sheaves of regular maps constructed in definition 2.1.5. But in fact, this definition of morphisms is used in many other categories as well, e. g. one can say that a set-theoretic map between complex manifolds is holomorphic if it pulls back holomorphic functions to holomorphic functions. In fact, it is almost the general definition of morphisms between ringed spaces —

---

the only additional twist in the general case is that if $f:X\to Y$ is a continuous map between arbitrary ringed spaces $(X,\mathcal{O}_{X})$ and $(Y,\mathcal{O}_{Y})$, there is no a priori definition of the pull-back map $\mathcal{O}_{Y}(U)\to\mathcal{O}_{X}(f^{-1}(U))$. In the case above we solved this problem by applying the set-theoretic viewpoint that gave us a notion of pull-back in our special case. In more general cases (e. g. for schemes that we will discuss later in section 5) one will have to include these pull-back maps in the data needed to define a morphism.

We now want to show that for affine varieties the situation is a lot easier: we actually do not have to deal with open subsets, but it suffices to check the pull-back property on *global* functions only:

###### Lemma 2.3.4.

Let $f:X\to Y$ be a continuous map between affine varieties. Then the following are equivalent:

1. $f$ is a morphism (i. e. $f$ pulls back regular functions on open subsets to regular functions on open subsets).
2. For every $\varphi\in\mathcal{O}_{Y}(Y)$ we have $f^{*}\varphi\in\mathcal{O}_{X}(X)$, i. e. $f$ pulls back *global* regular functions to *global* regular functions.
3. For every $P\in X$ and every $\varphi\in\mathcal{O}_{Y,f(P)}$ we have $f^{*}\varphi\in\mathcal{O}_{X,P}$, i. e. $f$ pulls back *germs* of regular functions to *germs* of regular functions.

###### Proof.

(i) $\Rightarrow$ (ii) is trivial, and (iii) $\Rightarrow$ (i) follows immediately from the definition of $\mathcal{O}_{Y}(U)$ and $\mathcal{O}_{X}(f^{-1}(U))$ as intersections of local rings. To prove (ii) $\Rightarrow$ (iii) let $\varphi\in\mathcal{O}_{Y,f(P)}$ be the germ of a regular function on $Y$. We write $\varphi=\frac{g}{h}$ with $g,h\in A(Y)=\mathcal{O}_{Y}(Y)$ and $h(f(P))\neq 0$. By (ii), $f^{*}g$ and $f^{*}h$ are global regular functions in $A(X)=\mathcal{O}_{X}(X)$, hence $f^{*}\varphi=\frac{f^{*}g}{f^{*}h}\in\mathcal{O}_{X,P}$, since we have $h(f(P))\neq 0$. ∎

###### Example 2.3.5.

Let $X=\mathbb{A}^{1}$ be the affine line with coordinate $x$, and let $Y=\mathbb{A}^{1}$ be the affine line with coordinate $y$. Consider the set-theoretic map

$f:X\to Y,\quad x\mapsto y=x^{2}.$

We claim that this is a morphism. In fact, by lemma 2.3.4 (ii) we just have to show that $f$ pulls back polynomials in $k[y]$ to polynomials in $k[x]$. But this is obvious, as the pull-back of a polynomial $\varphi(y)\in k[y]$ is just $\varphi(x^{2})$ (i. e. we substitute $x^{2}$ for $y$ in $\varphi$). This is still a polynomial, so it is in $k[x]$.

###### Example 2.3.6.

For the very same reason, every polynomial map is a morphism. More precisely, let $X\subset\mathbb{A}^{m}$ and $Y\subset\mathbb{A}^{n}$ be affine varieties, and let $f:X\to Y$ be a polynomial map, i. e. a map that can be written as $f(P)=(f_{1}(P),\ldots,f_{n}(P))$ with $f_{i}\in k[x_{1},\ldots,x_{m}]$. As $f$ then pulls back polynomials to polynomials, we conclude first of all that $f$ is continuous. Moreover, it then follows from lemma 2.3.4 (ii) that $f$ is a morphism. In fact, we will show now that all morphisms between affine varieties are of this form.

###### Lemma 2.3.7.

Let $X\subset\mathbb{A}^{n}$ and $Y\subset\mathbb{A}^{m}$ be affine varieties. There is a one-to-one correspondence between morphisms $f:X\to Y$ and $k$-algebra homomorphisms $f^{*}:A(Y)\to A(X)$.

###### Proof.

Any morphism $f:X\to Y$ determines a $k$-algebra homomorphism $f^{*}:\mathcal{O}_{Y}(Y)=A(Y)\to\mathcal{O}_{X}(X)=A(X)$ by definition. Conversely, if

$g:k[y_{1},\ldots,y_{m}]/I(Y)\to k[x_{1},\ldots,x_{n}]/I(X)$

is any $k$-algebra homomorphism then it determines a polynomial map $f=(f_{1},\ldots,f_{m}):X\to Y$ as in example 2.3.6 by $f_{i}=g(y_{i})$, and hence a morphism. ∎

######

---

2. Functions, morphisms, and varieties

Example 2.3.8. Of course, an isomorphism is defined to be a morphism  $f: X \to Y$  that has an inverse (i.e., a morphism such that there is a morphism  $g: Y \to X$  with  $g \circ f = \mathrm{id}_X$  and  $f \circ g = \mathrm{id}_Y$ ). A warning is in place here that an isomorphism of affine varieties is not the same as a bijective morphism (in contrast e.g. to the case of vector spaces). For example, let  $X \subset \mathbb{A}^2$  be the curve given by the equation  $x^2 = y^3$ , and consider the map

![img-0.jpeg](images/img-0.jpeg)

This is a morphism as it is given by polynomials, and it is bijective as the inverse is given by

$$
f ^ {- 1}: X \to \mathbb {A} ^ {1}, \quad (x, y) \mapsto \left\{ \begin{array}{l l} \frac {x}{y} &amp; \text {i f} (x, y) \neq (0, 0), \\ 0 &amp; \text {i f} (x, y) = (0, 0). \end{array} \right.
$$

But if  $f$  was an isomorphism, the corresponding  $k$ -algebra homomorphism

$$
k [ x, y ] / (x ^ {2} - y ^ {3}) \to k [ t ], \quad x \mapsto t ^ {3} \text {a n d} y \mapsto t ^ {2}
$$

would have to be an isomorphism by lemma 2.3.7. This is obviously not the case, as the image of this algebra homomorphism contains no linear polynomials.

Example 2.3.9. As an application of morphisms, let us consider products of affine varieties. Let  $X \subset \mathbb{A}^n$  and  $Y \subset \mathbb{A}^m$  be affine varieties with ideals  $I(X) \subset k[x_1, \ldots, x_n]$  and  $I(Y) \subset k[y_1, \ldots, y_m]$ . As usual, we define the product  $X \times Y$  of  $X$  and  $Y$  to be the set

$$
X \times Y = \left\{\left(P, Q\right) \in \mathbb {A} ^ {n} \times \mathbb {A} ^ {m}; P \in X \text {a n d} Q \in Y \right\} \subset \mathbb {A} ^ {n} \times \mathbb {A} ^ {m} = \mathbb {A} ^ {n + m}.
$$

Obviously, this is an algebraic set in  $\mathbb{A}^{n + m}$  with ideal

$$
I (X \times Y) = I (X) + I (Y) \subset k [ x _ {1}, \dots , x _ {n}, y _ {1}, \dots , y _ {m} ]
$$

where we consider  $k[x_1, \ldots, x_n]$  and  $k[y_1, \ldots, y_m]$  as subalgebras of  $k[x_1, \ldots, x_n, y_1, \ldots, y_m]$  in the obvious way. Let us show that it is in fact a variety, i.e. irreducible:

Proposition 2.3.10. If  $X$  and  $Y$  are affine varieties, then so is  $X \times Y$ .

Proof. For simplicity, let us just write  $x$  for the collection of the  $x_{i}$ , and  $y$  for the collection of the  $y_{i}$ . By the above discussion it only remains to show that  $I(X \times Y)$  is prime. So let  $f, g \in k[x,y]$  be polynomial functions such that  $fg \in I(X \times Y)$ ; we have to show that either  $f$  or  $g$  vanishes on all of  $X \times Y$ , i.e. that  $X \times Y \subset Z(f)$  or  $X \times Y \subset Z(g)$ .

So let us assume that  $X \times Y \not\subset Z(f)$ , i.e. there is a point  $(P, Q) \in X \times Y \backslash Z(f)$  (where  $P \in X$  and  $Q \in Y$ ). Denote by  $f(\cdot, Q) \in k[x]$  the polynomial obtained from  $f \in k[x, y]$  by plugging in the coordinates of  $Q$  for  $y$ . For all  $P' \in X \backslash Z(f(\cdot, Q))$  (e.g. for  $P' = P$ ) we must have

$$
Y \subset Z (f (P ^ {\prime}, \cdot) \cdot g (P ^ {\prime}, \cdot)) = Z (f (P ^ {\prime}, \cdot)) \cup Z (g (P ^ {\prime}, \cdot)).
$$

As  $Y$  is irreducible and  $Y \not\subset Z(f(P', \cdot))$  by the choice of  $P'$ , it follows that  $Y \subset Z(g(P', \cdot))$ .

This is true for all  $P' \in X \backslash Z(f(\cdot, Q))$ , so we conclude that  $(X \backslash Z(f(\cdot, Q)) \times Y \subset Z(g)$ . But as  $Z(g)$  is closed, it must in fact contain the closure of  $(X \backslash Z(f(\cdot, Q)) \times Y$  as well, which is just  $X \times Y$  as  $X$  is irreducible and  $X \backslash Z(f(\cdot, Q))$  a non-empty open subset of  $X$  (see remark 1.3.17).

The obvious projection maps

$$
\pi_ {X}: X \times Y \to X, (P, Q) \mapsto P \quad \text {a n d} \quad \pi_ {Y}: X \times Y \to Y, (P, Q) \mapsto Q
$$

are given by (trivial) polynomial maps and are therefore morphisms. The important main property of the product  $X \times Y$  is the following:

---

Andreas Gathmann

Lemma 2.3.11. Let  $X$  and  $Y$  be affine varieties. Then the product  $X \times Y$  satisfies the following universal property: for every affine variety  $Z$  and morphisms  $f: Z \to X$  and  $g: Z \to Y$ , there is a unique morphism  $h: Z \to X \times Y$  such that  $f = \pi_X \circ h$  and  $g = \pi_Y \circ h$ , i.e., such that the following diagram commutes:

![img-1.jpeg](images/img-1.jpeg)

In other words, giving a morphism  $Z \to X \times Y$  "is the same" as giving two morphisms  $Z \to X$  and  $Z \to Y$ .

Proof. Let  $A$  be the coordinate ring of  $Z$ . Then by lemma 2.3.7 the morphism  $f: Z \to X$  is given by a  $k$ -algebra homomorphism  $\tilde{f}: k[x_1, \ldots, x_n] / I(X) \to A$ . This in turn is determined by giving the images  $\tilde{f}_i := \tilde{f}(x_i) \in A$  of the generators  $x_i$ , satisfying the relations of  $I$  (i.e.  $F(\tilde{f}_1, \ldots, \tilde{f}_n) = 0$  for all  $F(x_1, \ldots, x_n) \in I(X)$ ). The same is true for  $g$ , which is determined by the images  $\tilde{g}_i := \tilde{g}(y_i) \in A$ .

Now it is obvious that the elements  $\tilde{f}_i$  and  $\tilde{g}_i$  determine a  $k$ -algebra homomorphism

$$
k \left[ x _ {1}, \dots , x _ {n}, y _ {1}, \dots , y _ {m} \right] / \left(I (X) + I (Y)\right)\rightarrow A,
$$

which determines a morphism  $h: Z \to X \times Y$  by lemma 2.3.7.

To show uniqueness, just note that the relations  $f = \pi_X \circ h$  and  $g = \pi_Y \circ h$  imply immediately that  $h$  must be given set-theoretically by  $h(P) = (f(P), g(P))$  for all  $P \in Z$ .

Remark 2.3.12. It is easy to see that the property of lemma 2.3.11 determines the product  $X \times Y$  uniquely up to isomorphism. It is therefore often taken to be the defining property for products.

Remark 2.3.13. If you have heard about tensor products before, you will have noticed that the coordinate ring of  $X \times Y$  is just the tensor product  $A(X) \otimes A(Y)$  of the coordinate rings of the factors (where the tensor product is taken as  $k$ -algebras). See also section 5.4 for more details.

Remark 2.3.14. Lemma 2.3.7 allows us to associate an affine variety up to isomorphism to any finitely generated  $k$ -algebra that is a domain: if  $A$  is such an algebra, let  $x_{1},\ldots ,x_{n}$  be generators of  $A$ , so that  $A = k[x_1,\dots,x_n] / I$  for some ideal  $I$ . Let  $X$  be the affine variety in  $\mathbb{A}^n$  defined by the ideal  $I$ ; by the lemma it is defined up to isomorphism. Therefore we should make a (very minor) redefinition of the term "affine variety" to allow for objects that are isomorphic to an affine variety in the old sense, but that do not come with an intrinsic description as the zero locus of some polynomials in affine space:

Definition 2.3.15. A ringed space  $(X,O_X)$  is called an affine variety over  $k$  if

(i)  $X$  is irreducible,
(ii)  $O_X$  is a sheaf of  $k$ -valued functions,
(iii)  $X$  is isomorphic to an affine variety in the sense of definition 1.3.1.

Here is an example of an affine variety in this new sense although it is not a priori given as the zero locus of some polynomials in affine space:

Lemma 2.3.16. Let  $X$  be an affine variety and  $f \in A(X)$ , and let  $X_f = X \backslash Z(f)$  be a distinguished open subset as in proposition 2.1.10. Then the ringed space  $(X_f, O_X|_{X_f})$  is isomorphic to an affine variety with coordinate ring  $A(X)_f$ .

---

###### Proof.

Let $X\subset\mathbb{A}^{n}$ be an affine variety, and let $f^{\prime}\in k[x_{1},\ldots,x_{n}]$ be a representative of $f$. Let $J\subset k[x_{1},\ldots,x_{n},t]$ be the ideal generated by $I(X)$ and the function $1-tf^{\prime}$. We claim that the ringed space $(X_{f},\mathcal{O}_{X}|_{X_{f}})$ is isomorphic to the affine variety

$Z(J)=\{(P,\lambda)\;;\;P\in X\text{ and }\lambda=\tfrac{1}{f^{\prime}(P)}\}\subset\mathbb{A}^{n+1}.$

Consider the projection map $\pi:Z(J)\to X$ given by $\pi(P,\lambda)=P$. This is a morphism with image $X_{f}$ and inverse morphism $\pi^{-1}(P)=(P,\tfrac{1}{f^{\prime}(P)})$, hence $\pi$ is an isomorphism. It is obvious that $A(Z(J))=A(X)_{f}$. ∎

###### Remark 2.3.17.

So we have just shown that even open subsets of affine varieties are themselves affine varieties, provided that the open subset is the complement of the zero locus of a single polynomial equation.

Example 2.1.12 shows however that not all open subsets of affine varieties are themselves isomorphic to affine varieties: if $U\subset\mathbb{C}^{2}\backslash\{0\}$ we have seen that $\mathcal{O}_{U}(U)=k[x,y]$. So if $U$ was an affine variety, its coordinate ring must be $k[x,y]$, which is the same as the coordinate ring of $\mathbb{C}^{2}$. By lemma 2.3.7 this means that $U$ and $\mathbb{C}^{2}$ would have to be isomorphic, with the isomorphism given by the identity map. Obviously, this is not true. Hence $U$ is not an affine variety. It can however be covered by two open subsets $\{x\neq 0\}$ and $\{y\neq 0\}$ which are both affine by lemma 2.3.16. This leads us to the idea of *patching* affine varieties together, which we will do in the next section.

### 2.4. Prevarieties

Now we want to extend our category of objects to more general things than just affine varieties. Remark 2.3.17 showed us that not all open subsets of affine varieties are themselves isomorphic to affine varieties. But note that every open subset of an affine variety can be written as a finite union of distinguished open subsets (as this is equivalent to the statement that every closed subset of an affine variety is the zero locus of finitely many polynomials). Hence any such open subset can be *covered* by affine varieties. This leads us to the idea that we should study objects that are not affine varieties themselves, but rather can be covered by (finitely many) affine varieties. Note that the following definition is completely parallel to the definition 2.3.15 of affine varieties (in the new sense).

###### Definition 2.4.1.

A *prevariety* is a ringed space $(X,\mathcal{O}_{X})$ such that

1. $X$ is irreducible,
2. $\mathcal{O}_{X}$ is a sheaf of $k$-valued functions,
3. there is a finite open cover $\{U_{i}\}$ of $X$ such that $(U_{i},\mathcal{O}_{X}|_{U_{i}})$ is an affine variety for all $i$.

As before, a morphism of prevarieties is just a morphism as ringed spaces (see definition 2.3.1).

An open subset $U\subset X$ of a prevariety such that $(U,\mathcal{O}_{X}|_{U})$ is isomorphic to an affine variety is called an affine open set.

###### Example 2.4.2.

Affine varieties and open subsets of affine varieties are prevarieties (the irreducibility of open subsets follows from exercise 1.4.6).

###### Remark 2.4.3.

The above definition is completely analogous to the definition of manifolds. Recall how manifolds are defined: first you look at open subsets of $\mathbb{R}^{n}$ that are supposed to form the patches of your space, and then you define a manifold to be a topological space that looks locally like these patches. In the algebraic case now we can say that the affine varieties form the basic patches of the spaces that we want to consider, and that e. g. open subsets of affine varieties are spaces that look locally like affine varieties.

---

Andreas Gathmann

As we defined a prevariety to be a space that can be covered by affine opens, the most general way to construct prevarieties is of course to take some affine varieties (or prevarieties that we have already constructed) and patch them together:

Example 2.4.4. Let  $X_{1}, X_{2}$  be prevarieties, let  $U_{1} \subset X_{1}$  and  $U_{2} \subset X_{2}$  be non-empty open subsets, and let  $f: (U_{1}, \mathcal{O}_{X_{1}}|_{U_{1}}) \to (U_{2}, \mathcal{O}_{X_{2}}|_{U_{2}})$  be an isomorphism. Then we can define a prevariety  $X$ , obtained by glueing  $X_{1}$  and  $X_{2}$  along  $U_{1}$  and  $U_{2}$  via the isomorphism  $f$ :

- As a set, the space  $X$  is just the disjoint union  $X_{1} \cup X_{2}$  modulo the equivalence relation  $P \sim f(P)$  for all  $P \in U_{1}$ .
- As a topological space, we endow  $X$  with the so-called quotient topology induced by the above equivalence relation, i.e. we say that a subset  $U \subset X$  is open if and only if  $i_1^{-1}(U) \subset X_1$  and  $i_2^{-1}(U) \subset X_2$  are both open, with  $i_1: X_1 \to X$  and  $i_2: X_2 \to X$  being the obvious inclusion maps.
- As a ringed space, we define the structure sheaf  $O_X$  by

$\mathcal{O}_X(U) = \{(\varphi_1,\varphi_2);\varphi_1\in \mathcal{O}_{X_1}(i_1^{-1}(U)),\varphi_2\in \mathcal{O}_{X_2}(i_2^{-1}(U)),$

$\varphi_{1} = \varphi_{2}$  on the overlap (i.e.  $f^{*}(\varphi_{2}|_{i_{2}^{-1}(U)\cap U_{2}}) = \varphi_{1}|_{i_{1}^{-1}(U)\cap U_{1}})\}$

It is easy to check that this defines a sheaf of  $k$ -valued functions on  $X$  and that  $X$  is irreducible. Of course, every point of  $X$  has an affine neighborhood, so  $X$  is in fact a prevariety.

Example 2.4.5. As an example of the above glueing construction, let  $X_{1} = X_{2} = \mathbb{A}^{1}$ ,  $U_{1} = U_{2} = \mathbb{A}^{1} \backslash \{0\}$ .

- Let  $f: U_1 \to U_2$  be the isomorphism  $x \mapsto \frac{1}{x}$ . The space  $X$  can be thought of as  $\mathbb{A}^1 \cup \{\infty\}$ : of course the affine line  $X_1 = \mathbb{A}^1 \subset X$  sits in  $X$ . The complement  $X \backslash X_1$  is a single point that corresponds to the zero point in  $X_2 \cong \mathbb{A}^1$  and hence to “ $\infty = \frac{1}{0}$ ” in the coordinate of  $X_1$ . In the case  $k = \mathbb{C}$ , the space  $X$  is just the Riemann sphere  $\mathbb{C}_{\infty}$ .

![img-2.jpeg](images/img-2.jpeg)

We denote this space by  $\mathbb{P}^1$ . (This is a special case of a projective space; see section 3.1 and remark 3.3.7 for more details.)

- Let  $f: U_1 \to U_2$  be the identity map. Then the space  $X$  obtained by glueing along  $f$  is "the affine line with the zero point doubled":

![img-3.jpeg](images/img-3.jpeg)

Obviously this is a somewhat weird space. Speaking in classical terms (and thinking of the complex numbers), if we have a sequence of points tending to the zero, this sequence would have two possible limits, namely the two zero points. Usually we want to exclude such spaces from the objects we consider. In the theory of manifolds, this is simply done by requiring that a manifold satisfies the so-called Hausdorff property, i.e. that every two distinct points have disjoint open neighborhoods. This is obviously not satisfied for our space  $X$ . But the analogous definition does not make sense in the Zariski topology, as non-empty open subsets

---

are never disjoint. Hence we need a different characterization of the geometric concept of “doubled points”. We will do this in section 2.5.

###### Example 2.4.6.

Let $X$ be the complex affine curve

$X=\{(x,y)\in\mathbb{C}^{2}\ ;\,y^{2}=(x-1)(x-2)\cdots(x-2n)\}.$

We have already seen in example 0.1.1 that $X$ can (and should) be “compactified” by adding two points at infinity, corresponding to the limit $x\to\infty$ and the two possible values for $y$. Let us now construct this compactified space rigorously as a prevariety.

To be able to add a limit point “$x=\infty$” to our space, let us make a coordinate change $\tilde{x}=\frac{1}{x}$, so that the equation of the curve becomes

$y^{2}\tilde{x}^{2n}=(1-\tilde{x})(1-2\tilde{x})\cdots(1-2n\tilde{x}).$

If we make an additional coordinate change $\tilde{y}=\frac{y}{x^{n}}$, this becomes

$\tilde{y}^{2}=(1-\tilde{x})(1-2\tilde{x})\cdots(1-2n\tilde{x}).$

In these coordinates we can add our two points at infinity, as they now correspond to $\tilde{x}=0$ (and therefore $\tilde{y}=\pm 1$).

Summarizing, our “compactified curve” of example 0.1.1 is just the prevariety obtained by glueing the two affine varieties

$X$ $=\{(x,y)\in\mathbb{C}^{2}\ ;\,y^{2}=(x-1)(x-2)\cdots(x-2n)\}$
$\text{and}\quad\tilde{X}$ $=\{(\tilde{x},\tilde{y})\in\mathbb{C}^{2}\ ;\,\tilde{y}^{2}=(1-\tilde{x})(1-2\tilde{x})\cdots(1-2n\tilde{x})\}$

along the isomorphism

$f:U$ $\to\tilde{U},\quad(x,y)\mapsto(\tilde{x},\tilde{y})=\left(\frac{1}{x},\frac{y}{x^{n}}\right),$
$f^{-1}:\tilde{U}$ $\to U,\quad(\tilde{x},\tilde{y})\mapsto(x,y)=\left(\frac{1}{\tilde{x}},\frac{\tilde{y}}{\tilde{x}^{n}}\right),$

where $U=\{x\neq 0\}\subset X$ and $\tilde{U}=\{\tilde{x}\neq 0\}\subset\tilde{X}$.

Of course one can also glue together more than two prevarieties. As the construction is the same as in the case above, we will just give the statement and leave its proof as an exercise:

###### Lemma 2.4.7.

Let $X_{1},\ldots,X_{r}$ be prevarieties, and let $U_{i,j}\subset X_{i}$ be non-empty open subsets for $i,j=1,\ldots,r$. Let $f_{i,j}:U_{i,j}\to U_{j,i}$ be isomorphisms such that

1. $f_{i,j}=f_{j,i}^{-1}$,
2. $f_{i,k}=f_{j,k}\circ f_{i,j}$ where defined.

Then there is a prevariety $X$, obtained by glueing the $X_{i}$ along the morphisms $f_{i,j}$ as in example 2.4.4 (see below).

###### Remark 2.4.8.

The prevariety $X$ in the lemma 2.4.7 can be described as follows:

- As a set, $X$ is the disjoint union of the $X_{i}$, modulo the equivalence relation $P\sim f_{i,j}(P)$ for all $P\in U_{i,j}$.
- To define $X$ as a topological space, we say that a subset $Y\subset X$ is closed if and only if all restrictions $Y\cap X_{i}$ are closed.
- A regular function on an open set $U\subset X$ is a collection of regular functions $\varphi_{i}\in\mathcal{O}_{X_{i}}(X_{i}\cap U)$ that agree on the overlaps.

---

Andreas Gathmann

Condition (ii) of the lemma gives a compatibility condition for triple overlaps: consider three patches  $X_{i}, X_{j}, X_{k}$  that have a common intersection. Then we want to identify every point  $P \in U_{i,j}$  with  $f_{i,j}(P) \in U_{j,k}$ , and the point  $f_{i,j}(P)$  with  $f_{j,k}(f_{i,j}(P))$  (if it lies in  $U_{j,k}$ ). So the glueing map  $f_{i,k}$  must map  $P$  to the same point  $f_{j,k}(f_{i,j}(P))$  to get a consistent glueing. This is illustrated in the following picture:

![img-4.jpeg](images/img-4.jpeg)

Let us now consider some examples of morphisms between prevarieties.

Example 2.4.9. Let  $f: \mathbb{P}^1 \to \mathbb{A}^1$  be a morphism. We claim that  $f$  must be constant.

In fact, consider the restriction  $f|_{\mathbb{A}^1}$  of  $f$  to the open affine subset  $\mathbb{A}^1 \subset \mathbb{P}^1$ . By definition the restriction of a morphism is again a morphism, so  $f|_{\mathbb{A}^1}$  must be of the form  $x \mapsto y = p(x)$  for some polynomial  $p \in k[x]$ . Now consider the second patch of  $\mathbb{P}^1$  with coordinate  $\tilde{x} = \frac{1}{x}$ . Applying this coordinate change, we see that  $f|_{\mathbb{P}^1 \setminus \{0\}}$  is given by  $\tilde{x} \mapsto p\left(\frac{1}{\tilde{x}}\right)$ . But this must be a morphism too, i.e.  $p\left(\frac{1}{\tilde{x}}\right)$  must be a polynomial in  $\tilde{x}$ . This is only true if  $p$  is a constant.

In the same way as prevarieties can be glued, we can patch together morphisms too. Of course, the statement is essentially that we can check the property of being a morphism on affine open covers:

Lemma 2.4.10. Let  $X, Y$  be prevarieties and let  $f: X \to Y$  be a set-theoretic map. Let  $\{U_1, \ldots, U_r\}$  be an open cover of  $X$  and  $\{V_1, \ldots, V_r\}$  an affine open cover of  $Y$  such that  $f(U_i) \subset V_i$  and  $(f|_{U_i})^* O_Y(V_i) \subset O_X(U_i)$ . Then  $f$  is a morphism.

Proof. We may assume that the  $U_{i}$  are affine, as otherwise we can replace the  $U_{i}$  by a set of affines that cover  $U_{i}$ . Consider the restrictions  $f_{i}: U_{i} \to V_{i}$ . The homomorphism  $f_{i}^{*}: O_{Y}(V_{i}) = A(V_{i}) \to O_{X}(U_{i}) = A(U_{i})$  is induced by some morphism  $U_{i} \to V_{i}$  by lemma 2.3.7 which is easily seen to coincide with  $f_{i}$ . In particular, the  $f_{i}$  are continuous, and therefore so is  $f$ . It remains to show that  $f^{*}$  takes sections of  $O_{Y}$  to sections of  $O_{X}$ . But if  $V \subset Y$  is open and  $\varphi \in O_{Y}(V)$ , then  $f^{*}\varphi$  is at least a section of  $O_{X}$  on the sets  $f^{-1}(V) \cap U_{i}$ . Since  $O_{X}$  is a sheaf and the  $U_{i}$  cover  $X$ , these sections glue to give a section in  $O_{X}(f^{-1}(V))$ .

Example 2.4.11. Let  $f: \mathbb{A}^1 \to \mathbb{A}^1, x \mapsto y = f(x)$  be a morphism given by a polynomial  $f \in k[x]$ . We claim that there is a unique extension morphism  $\tilde{f}: \mathbb{P}^1 \to \mathbb{P}^1$  such that  $\tilde{f}|_{\mathbb{A}^1} = f$ . We can assume that  $f = \sum_{i=1}^{n} a_i x^i$  is not constant, as otherwise the result is trivial. It is then obvious that the extension should be given by  $\tilde{f}(\infty) = \infty$ . Let us check that this defines in fact a morphism.

We want to apply lemma 2.4.10. Consider the standard open affine cover of the domain  $\mathbb{P}^1$  by the two affine lines  $V_{1} = \mathbb{P}^{1}\backslash \{\infty \}$  and  $V_{2} = \mathbb{P}^{1}\backslash \{0\}$ . Then  $U_{1}\coloneqq \tilde{f}^{-1}(V_{1}) = \mathbb{A}^{1}$ , and  $\tilde{f} |_{\mathbb{A}^1} = f$  is a morphism. On the other hand, let  $U_{2}\coloneqq \tilde{f}^{-1}(V_{2})\backslash \{0\}$ . Consider the coordinates  $\tilde{x} = \frac{1}{x}$  and  $\tilde{y} = \frac{1}{y}$  on  $U_{2}$  and  $V_{2}$ , respectively. In these coordinates, the map  $\tilde{f}$  is given by

$$
\tilde {y} = \frac {\tilde {x} ^ {n}}{\sum_ {i = 1} ^ {n} a _ {i} \tilde {x} ^ {n - i}};
$$

---

in particular $\tilde{x}=0$ maps to $\tilde{y}=0$. So by defining $\tilde{f}(\infty)=\infty$, we get a morphism $\tilde{f}:\mathbb{P}^{1}\to\mathbb{P}^{1}$ that extends $f$ by lemma 2.4.10.

### 2.5. Varieties

Recall example 2.4.5 (ii) where we constructed a prevariety that was “not Hausdorff” in the classical sense: take two copies of the affine line $\mathbb{A}^{1}$ and glue them together on the open set $\mathbb{A}^{1}\backslash\{0\}$ along the identity map. The prevariety $X$ thus obtained is the “affine line with the origin doubled”; its strange property is that even in the classical topology (for $k=\mathbb{C}$) the two origins do not have disjoint neighborhoods. We will now define an algebro-geometric analogue of the Hausdorff property and say that a prevariety is a variety if it has this property.

###### Definition 2.5.1.

Let $X$ be a prevariety. We say that $X$ is a variety if for every prevariety $Y$ and every two morphisms $f_{1},f_{2}:Y\to X$, the set $\{P\in Y\ ;\ f_{1}(P)=f_{2}(P)\}$ is closed in $Y$.

###### Remark 2.5.2.

Let $X$ be the affine line with the origin doubled. Then $X$ is not a variety — if we take $Y=\mathbb{A}^{1}$ and let $f_{1},f_{2}:Y\to X$ be the two obvious inclusions that map the origin in $Y$ to the two different origins in $X$, then $f_{1}$ and $f_{2}$ agree on $\mathbb{A}^{1}\backslash\{0\}$, which is not closed in $\mathbb{A}^{1}$.

On the other hand, if $X$ has the Hausdorff property that we want to characterize, then two morphisms $Y\to X$ that agree on an open subset of $Y$ should also agree on $Y$.

One can make this definition somewhat easier and eliminate the need for an arbitrary second prevariety $Y$. To do so note that we can define products of prevarieties in the same way as we have defined products of affine varieties (see example 2.3.9 and exercise 2.6.13). For any prevariety $X$, consider the diagonal morphism

$\Delta:X\to X\times X,\quad P\mapsto(P,P).$

The image $\Delta(X)\subset X\times X$ is called the diagonal of $X$. Of course, the morphism $\Delta:X\to\Delta(X)$ is an isomorphism onto its image (with inverse morphism being given by $(P,Q)\mapsto P$). So the space $\Delta(X)$ is not really interesting as a new prevariety; instead the main question is how $\Delta(X)$ is embedded in $X\times X$:

###### Lemma 2.5.3.

A prevariety $X$ is a variety if and only if the diagonal $\Delta(X)$ is closed in $X\times X$.

###### Proof.

It is obvious that a variety has this property (take $Y=X\times X$ and $f_{1},f_{2}$ the two projections to $X$). Conversely, if the diagonal $\Delta(X)$ is closed and $f_{1},f_{2}:Y\to X$ are two morphisms, then they induce a morphism $(f_{1},f_{2}):Y\to X\times X$ by the universal property of exercise 2.6.13, and

$\{P\in Y\,|\,f_{1}(P)=f_{2}(P)\}=(f_{1},f_{2})^{-1}(\Delta(X))$

is closed. ∎

###### Lemma 2.5.4.

Every affine variety is a variety. Any open or closed subprevariety of a variety is a variety.

###### Proof.

If $X\subset\mathbb{A}^{n}$ is an affine variety with ideal $I(X)=(f_{1},\ldots,f_{r})$, the diagonal $\Delta(X)\subset\mathbb{A}^{2n}$ is an affine variety given by the equations $f_{i}(x_{1},\ldots,x_{n})=0$ for $i=1,\ldots,r$ and $x_{i}=y_{i}$ for $i=1,\ldots,n$, where $x_{1},\ldots,x_{n},y_{1},\ldots,y_{n}$ are the coordinates on $\mathbb{A}^{2n}$. This is obviously closed, so $X$ is a variety by lemma 2.5.3.

If $Y\subset X$ is open or closed, then $\Delta(Y)=\Delta(X)\cap(Y\times Y)$; i. e. if $\Delta(X)$ is closed in $X\times X$ then so is $\Delta(Y)$ in $Y\times Y$. ∎

###### Example 2.5.5.

Let us illustrate lemma 2.5.3 in the case of the affine line with a doubled origin. So let $X_{1}=X_{2}=\mathbb{A}^{1}$, and let $X$ be the prevariety obtained by glueing $X_{1}$ to $X_{2}$ along the identity on $\mathbb{A}\backslash\{0\}$. Then $X\times X$ is covered by the four affine varieties $X_{1}\times X_{1}$, $X_{1}\times X_{2}$,

---

Andreas Gathmann

$X_{2} \times X_{1}$ , and  $X_{2} \times X_{2}$  by exercise 2.6.13. As we glue along  $\mathbb{A}^1 \setminus \{0\}$  to obtain  $X$ , it follows that the space  $X \times X$  contains the point  $(P, Q) \in \mathbb{A}^1 \times \mathbb{A}^1$

- once if  $P \neq 0$  and  $Q \neq 0$ ,
- twice if  $P = 0$  and  $Q \neq 0$ , or if  $P \neq 0$  and  $Q = 0$ ,
- four times if  $P = 0$  and  $Q = 0$ .

![img-5.jpeg](images/img-5.jpeg)

In particular,  $X \times X$  contains four origins now. But the diagonal  $\Delta(X)$  contains only two of them (by definition of the diagonal we have to take the same origin in both factors). So on the patch  $X_1 \times X_2$ , the diagonal is given by  $\{(P, P); P \neq 0\} \subset X_1 \times X_2 = \mathbb{A}^1 \times \mathbb{A}^1$ , which is not closed. So we see again that  $X$  is not a variety.

# 2.6. Exercises.

Exercise 2.6.1. An algebraic set  $X \subset \mathbb{A}^2$  defined by a polynomial of degree 2 is called a conic. Show that any irreducible conic is isomorphic either to  $Z(y - x^2)$  or to  $Z(xy - 1)$ .

Exercise 2.6.2. Let  $X, Y \subset \mathbb{A}^2$  be irreducible conics as in exercise 2.6.1, and assume that  $X \neq Y$ . Show that  $X$  and  $Y$  intersect in at most 4 points. For all  $n \in \{0, 1, 2, 3, 4\}$ , find an example of two conics that intersect in exactly  $n$  points. (For a generalization see theorem 6.2.1.)

Exercise 2.6.3. Which of the following algebraic sets are isomorphic over the complex numbers?

(a)  $\mathbb{A}^1$

(b)  $Z(xy)\subset \mathbb{A}^2$

(c)  $Z(x^{2} + y^{2})\subset \mathbb{A}^{2}$

(d)  $Z(y^{2} - x^{3} - x^{2})\subset \mathbb{A}^{2}$

(e)  $Z(x^{2} - y^{3})\subset \mathbb{A}^{2}$

(f)  $Z(y - x^{2},z - x^{3})\subset \mathbb{A}^{3}$

Exercise 2.6.4. Let  $X$  be an affine variety, and let  $G$  be a finite group. Assume that  $G$  acts on  $X$ , i.e., that for every  $g \in G$  we are given a morphism  $g: X \to X$  (denoted by the same letter for simplicity of notation), such that  $(g \circ h)(P) = g(h(P))$  for all  $g, h \in G$  and  $P \in X$ .

(i) Let  $A(X)^G$  be the subalgebra of  $A(X)$  consisting of all  $G$ -invariant functions on  $X$ , i.e. of all  $f: X \to k$  such that  $f(g(P)) = f(P)$  for all  $P \in X$ . Show that  $A(X)^G$  is a finitely generated  $k$ -algebra.
(ii) By (i), there is an affine variety  $Y$  with coordinate ring  $A(X)^G$ , together with a morphism  $\pi : X \to Y$  determined by the inclusion  $A(X)^G \subset A(X)$ . Show that  $Y$  can be considered as the quotient of  $X$  by  $G$ , denoted  $X / G$ , in the following sense:

(a)  $\pi$  is surjective.
(b) If  $P, Q \in X$  then  $\pi(P) = \pi(Q)$  if and only if there is a  $g \in G$  such that  $g(P) = Q$ .

(iii) For a given group action, is an affine variety with the properties (ii)(a) and (ii)(b) uniquely determined?
(iv) Let  $\mathbb{Z}_n = \{\exp \left(\frac{2\pi ik}{n}\right); k \in \mathbb{Z}\} \subset \mathbb{C}$  be the group of  $n$ -th roots of unity. Let  $\mathbb{Z}_n$  act on  $\mathbb{C}^m$  by multiplication in each coordinate. Show that  $\mathbb{C} / \mathbb{Z}_n$  is isomorphic to  $\mathbb{C}$  for all  $n$ , but that  $\mathbb{C}^2 / \mathbb{Z}_n$  is not isomorphic to  $\mathbb{C}^2$  for  $n \geq 2$ .

Exercise 2.6.5. Are the following statements true or false: if  $f: \mathbb{A}^n \to \mathbb{A}^m$  is a polynomial map (i.e.  $f(P) = (f_1(P), \ldots, f_m(P))$  with  $f_i \in k[x_1, \ldots, x_n]$ ), and...

---

1. $X\subset\mathbb{A}^{n}$ is an algebraic set, then the image $f(X)\subset\mathbb{A}^{m}$ is an algebraic set.
2. $X\subset\mathbb{A}^{m}$ is an algebraic set, then the inverse image $f^{-1}(X)\subset\mathbb{A}^{n}$ is an algebraic set.
3. $X\subset\mathbb{A}^{n}$ is an algebraic set, then the graph $\Gamma=\{(x,f(x))\,|\,x\in X\}\subset\mathbb{A}^{n+m}$ is an algebraic set.

###### Exercise 2.6.6.

Let $f:X\to Y$ be a morphism between affine varieties, and let $f^{*}:A(Y)\to A(X)$ be the corresponding map of $k$-algebras. Which of the following statements are true?

1. If $P\in X$ and $Q\in Y$, then $f(P)=Q$ if and only if $(f^{*})^{-1}(I(P))=I(Q)$.
2. $f^{*}$ is injective if and only if $f$ is surjective.
3. $f^{*}$ is surjective if and only if $f$ is injective.
4. $f$ is an isomorphism if and only if $f^{*}$ is an isomorphism.

If a statement is false, is there maybe a weaker form of it which is true?

###### Exercise 2.6.7.

Let $X$ be a prevariety. Show that:

1. $X$ is a Noetherian topological space,
2. any open subset of $X$ is a prevariety.

###### Exercise 2.6.8.

Let $(X,\mathcal{O}_{X})$ be a prevariety, and let $Y\subset X$ be an irreducible closed subset. For every open subset $U\subset Y$ define $\mathcal{O}_{Y}(U)$ to be the ring of $k$-valued functions $f$ on $U$ with the following property: for every point $P\in Y$ there is a neighborhood $V$ of $P$ in $X$ and a section $F\in\mathcal{O}_{X}(V)$ such that $f$ coincides with $F$ on $U$.

1. Show that the rings $\mathcal{O}_{Y}(U)$ together with the obvious restriction maps define a sheaf $\mathcal{O}_{Y}$ on $Y$.
2. Show that $(Y,\mathcal{O}_{Y})$ is a prevariety.

###### Exercise 2.6.9.

Let $X$ be a prevariety. Consider pairs $(U,f)$ where $U$ is an open subset of $X$ and $f\in\mathcal{O}_{X}(U)$ a regular function on $U$. We call two such pairs $(U,f)$ and $(U^{\prime},f^{\prime})$ equivalent if there is an open subset $V$ in $X$ with $V\subset U\cap U^{\prime}$ such that $f|_{U}=f|_{U^{\prime}}$.

1. Show that this defines an equivalence relation.
2. Show that the set of all such pairs modulo this equivalence relation is a field. It is called the field of rational functions on $X$ and denoted $K(X)$.
3. If $X$ is an affine variety, show that $K(X)$ is just the field of rational functions as defined in definition 2.1.3.
4. If $U\subset X$ is any non-empty open subset, show that $K(U)=K(X)$.

###### Exercise 2.6.10.

If $U$ is an open subset of a prevariety $X$ and $f:U\to\mathbb{P}^{1}$ a morphism, is it always true that $f$ can be extended to a morphism $\tilde{f}:X\to\mathbb{P}^{1}$ ?

###### Exercise 2.6.11.

Show that the prevariety $\mathbb{P}^{1}$ is a variety.

###### Exercise 2.6.12.

1. Show that every isomorphism $f:\mathbb{A}^{1}\to\mathbb{A}^{1}$ is of the form $f(x)=ax+b$ for some $a,b\in k$, where $x$ is the coordinate on $\mathbb{A}^{1}$.
2. Show that every isomorphism $f:\mathbb{P}^{1}\to\mathbb{P}^{1}$ is of the form $f(x)=\frac{ax+b}{cx+d}$ for some $a,b,c,d\in k$, where $x$ is an affine coordinate on $\mathbb{A}^{1}\subset\mathbb{P}^{1}$. (For a generalization see corollary 6.2.10.)
3. Given three distinct points $P_{1},P_{2},P_{3}\in\mathbb{P}^{1}$ and three distinct points $Q_{1},Q_{2},Q_{3}\in\mathbb{P}^{1}$, show that there is a unique isomorphism $f:\mathbb{P}^{1}\to\mathbb{P}^{1}$ such that $f(P_{i})=Q_{i}$ for $i=1,2,3$.

*(Remark: If the ground field is $\mathbb{C}$, the very same statements are true in the complex analytic category as well, i. e. if “morphisms” are understood as “holomorphic maps” (and $\mathbb{P}^{1}$ is the Riemann sphere $\mathbb{C}_{\infty}$). If you know some complex analysis and have some time to kill, you may try to prove this too.)*

---

Andreas Gathmann

Exercise 2.6.13.

Let $X$ and $Y$ be prevarieties with affine open covers $\{U_{i}\}$ and $\{V_{j}\}$, respectively. Construct the product prevariety $X\times Y$ by glueing the affine varieties $U_{i}\times V_{j}$ together. Moreover, show that there are projection morphisms $\pi_{X}:X\times Y\to X$ and $\pi_{Y}:X\times Y\to Y$ satisfying the “usual” universal property for products: given morphisms $f:Z\to X$ and $g:Z\to Y$ from any prevariety $Z$, there is a unique morphism $h:Z\to X\times Y$ such that $f=\pi_{X}\circ h$ and $g=\pi_{Y}\circ h$.