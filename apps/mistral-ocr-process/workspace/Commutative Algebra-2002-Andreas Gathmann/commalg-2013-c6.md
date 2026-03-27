6. Localization

Localization is a very powerful technique in commutative algebra that often allows to reduce questions on rings and modules to a union of smaller “local” problems. It can easily be motivated both from an algebraic and a geometric point of view, so let us start by explaining the idea behind it in these two settings.

###### Remark 6.1 (Motivation for localization).

1. Algebraic motivation: Let $R$ be a ring which is not a field, i. e. in which not all non-zero elements are units. The algebraic idea of localization is then to make more (or even all) non-zero elements invertible by introducing fractions, in the same way as one passes from the integers $\mathbb{Z}$ to the rational numbers $\mathbb{Q}$.

Let us have a more precise look at this particular example: in order to construct the rational numbers from the integers we start with $R=\mathbb{Z}$, and let $S=\mathbb{Z}\backslash\{0\}$ be the subset of the elements of $R$ that we would like to become invertible. On the set $R\times S$ we then consider the equivalence relation

$(a,s)\sim(a^{\prime},s^{\prime})\quad\Leftrightarrow\quad as^{\prime}-a^{\prime}s=0$

and denote the equivalence class of a pair $(a,s)$ by $\frac{a}{s}$. The set of these “fractions” is then obviously $\mathbb{Q}$, and we can define addition and multiplication on it in the expected way by $\frac{a}{s}+\frac{a^{\prime}}{s^{\prime}}:=\frac{as^{\prime}+a^{\prime}s}{ss^{\prime}}$ and $\frac{a}{s}\cdot\frac{a^{\prime}}{s^{\prime}}:=\frac{aa^{\prime}}{ss^{\prime}}$.
2. Geometric motivation: Now let $R=A(X)$ be the ring of polynomial functions on a variety $X$. In the same way as in (a) we can ask if it makes sense to consider fractions of such polynomials, i. e. rational functions

$X\to K,\>x\mapsto\frac{f(x)}{g(x)}$

for $f,g\in R$. Of course, for global functions on all of $X$ this does not work, since $g$ will in general have zeroes somewhere, so that the value of the rational function is ill-defined at these points. But if we consider functions on subsets of $X$ we can allow such fractions. The most important example from the point of view of localization is the following: for a fixed point $a\in X$ let $S=\{f\in A(X):f(a)\neq 0\}$ be the set of all polynomial functions that do not vanish at $a$. Then the fractions $\frac{f}{g}$ for $f\in R$ and $g\in S$ can be thought of as rational functions that are well-defined at $a$.

In fact, the best way to interpret the fractions $\frac{f}{g}$ with $f\in R$ and $g\in S$ is as “functions on an arbitrarily small neighborhood of $a$”, assuming that we have a suitable topology on $X$: although the only point at which these functions are guaranteed to be well-defined is $a$, for every such function there is a neighborhood on which it is defined as well, and to a certain extent the polynomials $f$ and $g$ can be recovered from the values of the function on such a neighborhood. In this sense we will refer to functions of the form $\frac{f}{g}$ with $f\in R$ and $g\in S$ as “local functions” at $a$. In fact, this geometric interpretation is the origin of the name “localization” for the process of constructing fractions described in this chapter.

Let us now introduce such fractions in a rigorous way. As above, $R$ will always denote the original ring, and $S\subset R$ the set of elements that we would like to become invertible. Note that this subset $S$ of denominators for our fractions has to be closed under multiplication, for otherwise the formulas $\frac{a}{s}+\frac{a^{\prime}}{s^{\prime}}:=\frac{as^{\prime}+a^{\prime}s}{ss^{\prime}}$ and $\frac{a}{s}\cdot\frac{a^{\prime}}{s^{\prime}}:=\frac{aa^{\prime}}{ss^{\prime}}$ for addition and multiplication of fractions would not make sense. Moreover, the equivalence relation on $R\times S$ to obtain fractions will be slightly different from the one in Remark 6.1 (a) — we will explain the reason for this later in Remark 6.3.

---

Andreas Gathmann

Lemma and Definition 6.2 (Localization of rings). Let  $R$  be a ring.

(a) A subset  $S \subset R$  is called multiplicatively closed if  $1 \in S$ , and  $ab \in S$  for all  $a, b \in S$ .
(b) Let  $S \subset R$  be a multiplicatively closed set. Then

$(a,s)\sim (a^{\prime},s^{\prime})\quad \Leftrightarrow \quad$  there is an element  $u\in S$  such that  $u(as^{\prime} - a^{\prime}s) = 0$

is an equivalence relation on  $R \times S$ . We denote the equivalence class of a pair  $(a, s) \in R \times S$  by  $\frac{a}{s}$ . The set of all equivalence classes

$S^{-1}R\coloneqq \left\{\frac{a}{s}:a\in R,s\in S\right\}$

is called the localization of  $R$  at the multiplicatively closed set  $S$ . It is a ring together with the addition and multiplication

$\frac{a}{s} + \frac{a'}{s'} := \frac{as' + a's}{ss'} \quad \text{and} \quad \frac{a}{s} \cdot \frac{a'}{s'} := \frac{aa'}{ss'}.$

Proof. The relation  $\sim$  is clearly reflexive and symmetric. It is also transitive: if  $(a,s)\sim (a^{\prime},s^{\prime})$  and  $(a^{\prime},s^{\prime})\sim (a^{\prime \prime},s^{\prime \prime})$  there are  $u,v\in S$  with  $u(as^{\prime} - a^{\prime}s) = v(a^{\prime}s^{\prime \prime} - a^{\prime \prime}s^{\prime}) = 0$ , and thus

$s^{\prime}uv(as^{\prime \prime} - a^{\prime \prime}s) = vs^{\prime \prime}\cdot u(as^{\prime} - a^{\prime}s) + us\cdot v(a^{\prime}s^{\prime \prime} - a^{\prime \prime}s^{\prime}) = 0.$  (*)

But this means that  $(a,s)\sim (a^{\prime \prime},s^{\prime \prime})$ , since  $S$  is multiplicatively closed and therefore  $s^{\prime}uv\in S$ .

In a similar way we can check that the addition and multiplication in  $S^{-1}R$  are well-defined: if  $(a,s)\sim (a^{\prime \prime},s^{\prime \prime})$ , i.e.  $u(as^{\prime \prime} - a^{\prime \prime}s) = 0$  for some  $u\in S$ , then

$u\left((as^{\prime} + a^{\prime}s)(s^{\prime \prime}s^{\prime}) - (a^{\prime \prime}s^{\prime} + a^{\prime}s^{\prime \prime})(ss^{\prime})\right) = (s^{\prime})^{2}\cdot u(as^{\prime \prime} - a^{\prime \prime}s) = 0$

and  $u\left((aa^{\prime})(s^{\prime \prime}s^{\prime}) - (a^{\prime \prime}a^{\prime})(ss^{\prime})\right) = a^{\prime}s^{\prime}\cdot u(as^{\prime \prime} - a^{\prime \prime}s) = 0,$

and so  $\frac{as' + a's}{ss'} = \frac{a''s' + a's''}{s''s'}$  and  $\frac{aa'}{ss'} = \frac{a''a'}{s''s'}$ .

It is now verified immediately that these two operations satisfy the ring axioms — in fact, the required computations to show this are exactly the same as for ordinary fractions in  $\mathbb{Q}$ .

Remark 6.3 (Explanation for the equivalence relation in Definition 6.2 (b)). Compared to Remark 6.1 (a) it might be surprising that the equivalence relation  $(a,s)\sim (a^{\prime},s^{\prime})$  for  $S^{-1}R$  is not just given by  $as^{\prime} - a^{\prime}s = 0$ , but by  $u(as^{\prime} - a^{\prime}s) = 0$  for some  $u\in S$ . Again, there is both an algebraic and a geometric reason for this:

(a) Algebraic reason: Without the additional element  $u \in S$  the relation  $\sim$  would not be transitive. In fact, if we set  $u = v = 1$  in the proof of transitivity in Lemma 6.2, we could only show that  $s'(as'' - a''s) = 0$  in (*) . Of course, this does not imply  $as'' - a''s = 0$  if  $S$  contains zero-divisors. (On the other hand, if  $S$  does not contain any zero-divisors, the condition  $u(as' - a's) = 0$  for some  $u \in S$  can obviously be simplified to  $as' - a's = 0$ .)
(b) Geometric reason, continuing Remark 6.1 (b): Let  $X = V(xy)$  in  $\mathbb{A}_{\mathbb{R}}^{2}$  be the union of the two coordinate axes as in the picture on the right, so that  $A(X) = \mathbb{R}[x,y] / (xy)$ . Then the functions  $y$  and  $0$  on  $X$  agree in a neighborhood of the point  $a = (1,0)$ , and so  $\frac{\tau}{1}$  and  $\frac{0}{1}$  should be the same local function at  $a$ , i.e. the same element in  $S^{-1}R$  with  $S = \{f \in A(X) : f(a) \neq 0\}$ . But without the additional element  $u \in S$  in Definition 6.2 (b) this would be false, since  $y \cdot 1 - 0 \cdot 1 \neq 0 \in A(X)$ . However, if we can set  $u = x \in S$ , then  $x(y \cdot 1 - 0 \cdot 1) = xy = 0 \in A(X)$ , and hence  $\frac{\tau}{1} = \frac{0}{1} \in S^{-1}R$  as desired.

![img-0.jpeg](images/img-0.jpeg)

Remark 6.4. Let  $S$  be a multiplicatively closed subset of a ring  $R$ .

---

1. There is an obvious ring homomorphism $\varphi:R\to S^{-1}R$, $a\mapsto\frac{a}{1}$ that makes $S^{-1}R$ into an $R$-algebra. However, $\varphi$ is only injective if $S$ does not contain zero-divisors, as $\frac{a}{1}=\frac{0}{1}$ by definition only implies the existence of an element $u\in S$ with $u(a\cdot 1-0\cdot 1)=ua=0$. We have already seen a concrete example of this in Remark 6.3 (b): in that case we had $y\neq 0\in R$, but $\frac{y}{1}=\frac{0}{1}\in S^{-1}R$.
2. In Definition 6.2 (a) of a multiplicatively closed subset we have not excluded the case $0\in S$, i. e. that we “want to allow division by $0$”. However, in this case we trivially get $S^{-1}R=0$, since we can then always take $u=0$ in Definition 6.2 (b).

###### Example 6.5 (Standard examples of localization).

Let us now give some examples of multiplicatively closed sets in a ring $R$, and thus of localizations. In fact, the following are certainly the most important examples — probably any localization that you will meet is of one of these forms.

1. Of course, $S=\{1\}$ is a multiplicatively closed subset, and leads to the localization $S^{-1}R\cong R$.
2. Let $S$ be the set of non-zero-divisors in $R$. Then $S$ is multiplicatively closed: if $a,b\in S$ then $ab$ is also not a zero-divisor, since $abc=0$ for some $c\in R$ first implies $bc=0$ since $a\in S$, and then $c=0$ since $b\in S$.

Of particular importance is the case when $R$ is an integral domain. Then $S=R\backslash\{0\}$, and every non-zero element $\frac{a}{s}$ is a unit in $S^{-1}R$, with inverse $\frac{s}{a}$. Hence $S^{-1}R$ is a field, the so-called quotient field $\operatorname{Quot}R$ of $R$.

Moreover, in this case every localization $T^{-1}R$ at a multiplicatively closed subset $T$ with $0\notin T$ is naturally a subring of $\operatorname{Quot}R$, since

$T^{-1}R\to\operatorname{Quot}R,\;\;\frac{a}{s}\mapsto\frac{a}{s}$

is an injective ring homomorphism. In particular, by (a) the ring $R$ itself can be thought of as a subring of its quotient field $\operatorname{Quot}R$ as well.
3. For a fixed element $a\in R$ let $S=\{a^{n}:n\in\mathbb{N}\}$. Then $S$ is obviously multiplicatively closed. The corresponding localization $S^{-1}R$ is often written as $R_{a}$; we call it the localization of $R$ at the element $a$.
4. Let $P\trianglelefteq R$ be a prime ideal. Then $S=R\backslash P$ is multiplicatively closed, since $a\notin P$ and $b\notin P$ implies $ab\notin P$ by Definition 2.1 (a). The resulting localization $S^{-1}R$ is usually denoted by $R_{P}$ and called the localization of $R$ at the prime ideal $P$.

In fact, this construction of localizing a ring at a prime ideal is probably the most important case of localization. In particular, if $R=A(X)$ is the ring of functions on a variety $X$ and $P=I(a)=\{f\in A(X):f(a)=0\}$ the ideal of a point $a\in X$ (which is maximal and hence prime, see Remark 2.7), the localization $R_{P}$ is exactly the ring of local functions on $X$ at $a$ as in Remark 6.1 (b). So localizing a coordinate ring at the maximal ideal corresponding to a point can be thought of as studying the variety locally around this point.

###### Example 6.6 (Localizations of $\mathbb{Z}$).

As concrete examples, let us apply the constructions of Example 6.5 to the ring $R=\mathbb{Z}$ of integers. Of course, localizing at $\mathbb{Z}\backslash\{0\}$ as in (b) gives the quotient field $\operatorname{Quot}\mathbb{Z}=\mathbb{Q}$ as in Remark 6.1 (a). If $p\in\mathbb{Z}$ is a prime number then localization at the element $p$ as in (c) gives the ring

$\mathbb{Z}_{p}=\left\{\frac{a}{p^{n}}:a\in\mathbb{Z},n\in\mathbb{N}\right\}\quad\subset\mathbb{Q},$

whereas localizing at the prime ideal $(p)$ as in (d) yields

$\mathbb{Z}_{(p)}=\left\{\frac{a}{b}:a,b\in\mathbb{Z},p\nmid b\right\}\quad\subset\mathbb{Q}$

(these are both subrings of $\mathbb{Q}$ by Example 6.5 (b)). So note that we have to be careful about the notations, in particular since $\mathbb{Z}_{p}$ is usually also used to denote the quotient $\mathbb{Z}/p\mathbb{Z}$.

######

---

Andreas Gathmann

After having seen many examples of localizations, let us now turn to the study of their properties. We will start by relating ideals in a localization $S^{-1}R$ to ideals in $R$.

**Proposition 6.7** (Ideals in localizations). Let $S$ be a multiplicatively closed subset of a ring $R$. In the following, we will consider contractions and extensions by the ring homomorphism $\varphi : R \to S^{-1}R$.

(a) For any ideal $I \trianglelefteq R$ we have $I^{e} = \{\frac{a}{s} : a \in I, s \in S\}$.

(b) For any ideal $I \trianglelefteq S^{-1}R$ we have $(I^{c})^{e} = I$.

(c) Contraction and extension by $\varphi$ give a one-to-one correspondence

$$
\begin{array}{l}
\left\{\text{prime ideals in } S^{-1}R \right\} \quad \xleftarrow{1:1} \quad \left\{\text{prime ideals } I \text{ in } R \text{ with } I \cap S = \emptyset \right\} \\
I \quad \longmapsto \quad I^{c} \\
I^{e} \quad \longleftarrow \quad I.
\end{array}
$$

**Proof.**

(a) As $\frac{1}{s} \in S^{-1}R$ for $s \in S$, the ideal $I^e$ generated by $\varphi(I)$ must contain the elements $\frac{1}{s} \cdot \varphi(a) = \frac{a}{s}$ for $a \in I$. But it is easy to check that $\{\frac{a}{s} : a \in I, s \in S\}$ is already an ideal in $S^{-1}R$, and so it has to be equal to $I^e$.

(b) By Exercise 1.19 (b) it suffices to show the inclusion “$\supset$”. So let $\frac{a}{s} \in I$. Then $a \in \varphi^{-1}(I) = I^c$ since $\varphi(a) = \frac{a}{1} = s \cdot \frac{a}{s} \in I$. By (a) applied to $I^c$ it follows that $\frac{a}{s} \in (I^c)^e$.

(c) We have to check a couple of assertions.

The map “$\rightarrow$” is well-defined: If $I$ is a prime ideal in $S^{-1}R$ then $I^c$ is a prime ideal in $R$ by Exercise 2.9 (b). Moreover, we must have $I^c \cap S = \emptyset$ as all elements of $S$ are mapped to units by $\varphi$, and $I$ cannot contain any units.

The map “$\leftarrow$” is well-defined: Let $I \trianglelefteq R$ be a prime ideal with $I \cap S = \emptyset$. We have to check that $I^e$ is a prime ideal. So let $\frac{a}{s} : \frac{b}{s} \in S^{-1}R$ with $\frac{a}{s} : \frac{b}{s} \in I^e$. By (a) this means that $\frac{ab}{st} = \frac{c}{n}$ for some $c \in I$ and $u \in S$, i.e. there is an element $v \in S$ with $v(abu - stc) = 0$. This implies that $uvab \in I$. Since $I$ is prime, one of these four factors must lie in $I$. But $u$ and $v$ are in $S$ and thus not in $I$. Hence we conclude that $a \in I$ or $b \in I$, and therefore $\frac{a}{s} \in I^e$ or $\frac{b}{s} \in I^e$ by (a).

$(I^{c})^{e} = I$ for any prime ideal $I$ in $S^{-1}R$: this follows from (b).

$(I^{e})^{c} = I$ for any prime ideal $I$ in $R$ with $I \cap S = \emptyset$: By Exercise 1.19 (a) we only have to check the inclusion “$\subset$”. So let $a \in (I^{e})^{c}$, i.e. $\varphi(a) = \frac{a}{1} \in I^{e}$. By (a) this means $\frac{a}{1} = \frac{b}{s}$ for some $b \in I$ and $s \in S$, and thus there is an element $u \in S$ with $u(as - b) = 0$. Therefore $sua \in I$, which means that one of these factors is in $I$ since $I$ is prime. But $s$ and $u$ lie in $S$ and hence not in $I$. So we conclude that $a \in I$.

**Example 6.8** (Prime ideals in $R_P$). Applying Proposition 6.7 (c) to the case of a localization of a ring $R$ at a prime ideal $P$, i.e. at the multiplicatively closed subset $R \setminus P$ as in Example 6.5 (d), gives a one-to-one correspondence by contraction and extension

$$
\left\{\text{prime ideals in } R_P \right\} \xleftarrow{1:1} \left\{\text{prime ideals } I \text{ in } R \text{ with } I \subset P \right\}. \tag{*}
$$

One should compare this to the case of prime ideals in the quotient ring $R / P$: by Lemma 1.21 and Corollary 2.4 we have a one-to-one correspondence

$$
\left\{\text{prime ideals in } R/P \right\} \xleftarrow{1:1} \left\{\text{prime ideals } I \text{ in } R \text{ with } I \supset P \right\},
$$

this time by contraction and extension by the quotient map. Unfortunately, general ideals do not behave as nicely: whereas ideals in the quotient $R / P$ still correspond to ideals in $R$ containing $P$, the analogous statement for general ideals in the localization $R_P$ would be false.

As we will see now, another consequence of the one-to-one correspondence $(*)$ is that the localization $R_P$ has exactly one maximal ideal (of course it always has at least one by Corollary 2.17). Since this is a very important property of rings, it has a special name.

**Definition 6.9** (Local rings). A ring is called local if it has exactly one maximal ideal.

---

###### Corollary 6.10 ($R_{P}$ is local).

Let $P$ be a prime ideal in a ring $R$. Then $R_{P}$ is local with maximal ideal $P^{e}=\{\frac{a}{s}:a\in P,s\notin P\}$.

###### Proof.

Obviously, the set of all prime ideals of $R$ contained in $P$ has the upper bound $P$. So as the correspondence $(*)$ of Example 6.8 preserves inclusions, we see that every prime ideal in $R_{P}$ is contained in $P^{e}$. In particular, every maximal ideal in $R_{P}$ must be contained in $P^{e}$. But this means that $P^{e}$ is the only maximal ideal. The formula for $P^{e}$ is just Proposition 6.7 (a). ∎

Note however that arbitrary localizations as in Definition 6.2 are in general not local rings.

###### Remark 6.11 (Rings of local functions on a variety are local).

If $R=A(X)$ is the coordinate ring of a variety $X$ and $P=I(a)$ the maximal ideal of a point $a\in X$, the localization $R_{P}$ is the ring of local functions on $X$ at $a$ as in Example 6.5 (d). By Corollary 6.10, this is a local ring with unique maximal ideal $P^{e}$, i. e. with only the maximal ideal corresponding to the point $a$. This fits nicely with the interpretation of Remark 6.1 (b) that $R_{P}$ describes an “arbitrarily small neighborhood” of $a$: although every function in $R_{P}$ is defined on $X$ in a neighborhood of $a$, there is no point except $a$ at which every function in $R_{P}$ is well-defined.

###### Exercise 6.12 (Universal property of localization).

Let $S$ be a multiplicatively closed subset of a ring $R$. Prove that the localization $S^{-1}R$ satisfies the following *universal property*: for any homomorphism $\alpha:R\to R^{\prime}$ to another ring $R^{\prime}$ that maps $S$ to units in $R^{\prime}$ there is a unique ring homomorphism $\varphi:S^{-1}R\to R^{\prime}$ such that $\varphi(\frac{r}{1})=\alpha(r)$ for all $r\in R$.

###### Exercise 6.13.

1. Let $R=\mathbb{R}[x,y]/(xy)$ and $P=(x-1)\trianglelefteq R$. Show that $P$ is a maximal ideal of $R$, and that $R_{P}\cong\mathbb{R}[x]_{(x-1)}$. What does this mean geometrically?
2. Let $R$ be a ring and $a\in R$. Show that $R_{a}\cong R[x]/(ax-1)$, where $R_{a}$ denotes the localization of $R$ at $a$ as in Example 6.5 (c). Can you give a geometric interpretation of this statement?

###### Exercise 6.14.

Let $S$ be a multiplicatively closed subset in a ring $R$, and let $I\trianglelefteq R$ be an ideal with $I\cap S=\emptyset$. Prove the following “localized version” of Corollary 2.17:

1. The ideal $I$ is contained in a prime ideal $P$ of $R$ such that $P\cap S=\emptyset$ and $S^{-1}P$ is a maximal ideal in $S^{-1}R$.
2. The ideal $I$ is not necessarily contained in a maximal ideal $P$ of $R$ with $P\cap S=\emptyset$.

###### Exercise 6.15 (Saturations).

For a multiplicatively closed subset $S$ of a ring $R$ we call

$\overline{S}:=\{s\in R:as\in S\text{ for some }a\in R\}$

the *saturation* of $S$. Show that $\overline{S}$ is a multiplicatively closed subset as well, and that $\overline{S}^{-1}R\cong S^{-1}R$.

###### Exercise 6.16 (Alternative forms of Nakayama’s Lemma for local rings).

Let $M$ be a finitely generated module over a local ring $R$. Prove the following two versions of *Nakayama’s Lemma* (see Corollary 3.27):

1. If there is a proper ideal $I\trianglelefteq R$ with $IM=M$, then $M=0$.
2. If $I\trianglelefteq R$ is the unique maximal ideal and $m_{1},\ldots,m_{k}\in M$ are such that $\overline{m_{1}},\ldots,\overline{m_{k}}$ generate $M/IM$ as an $R/I$-vector space, then $m_{1},\ldots,m_{k}$ generate $M$ as an $R$-module.

So far we have only applied the technique of localization to rings. But in fact this works equally well for modules, so let us now give the corresponding definitions. However, as the computations to check that these definitions make sense are literally the same as in Lemma 6.2, we will not repeat them here.

###### Definition 6.17 (Localization of modules).

Let $S$ be a multiplicatively closed subset of a ring $R$, and let $M$ be an $R$-module. Then

$(m,s)\sim(m^{\prime},s^{\prime})\ \ \Leftrightarrow\ \ \text{there is an element }u\in S\text{ such that }u(s^{\prime}m-sm^{\prime})=0$

---

is an equivalence relation on $M\times S$. We denote the equivalence class of $(m,s)\in M\times S$ by $\frac{m}{s}$. The set of all equivalence classes

$S^{-1}M:=\Big{\{}\frac{m}{s}:m\in M,s\in S\Big{\}}$

is then called the localization of $M$ at $S$. It is an $S^{-1}R$-module together with the addition and scalar multiplication

$\frac{m}{s}+\frac{m^{\prime}}{s^{\prime}}:=\frac{s^{\prime}m+sm^{\prime}}{ss^{\prime}}\quad\text{and}\quad\frac{a}{s}\cdot\frac{m^{\prime}}{s^{\prime}}:=\frac{am^{\prime}}{ss^{\prime}}$

for all $a\in R$, $m,m^{\prime}\in M$, and $s,s^{\prime}\in S$.

In the cases of example 6.5 (c) and (d), when $S$ is equal to $\{a^{n}:n\in\mathbb{N}\}$ for an element $a\in R$ or $R\backslash P$ for a prime ideal $P\unlhd R$, we will write $S^{-1}M$ also as $M_{a}$ or $M_{P}$, respectively.

###### Example 6.18.

Let $S$ be a multiplicatively closed subset of a ring $R$, and let $I$ be an ideal in $R$. Then by Proposition 6.7 (a) the localization $S^{-1}I$ in the sense of Definition 6.17 is just the extension $I^{r}$ of $I$ with respect to the canonical map $R\to S^{-1}R,\ a\mapsto\frac{a}{1}$.

In fact, it turns out that the localization $S^{-1}M$ of a module $M$ is just a special case of a tensor product. As one might already expect from Definition 6.17, it can be obtained from $M$ by an extension of scalars from $R$ to the localization $S^{-1}R$ as in Construction 5.16. Let us prove this first, so that we can then carry over some of the results of Chapter 5 to our present situation.

###### Lemma 6.19 (Localization as a tensor product).

Let $S$ be a multiplicatively closed subset in a ring $R$, and let $M$ be an $R$-module. Then $S^{-1}M\cong M\otimes_{R}S^{-1}R$.

###### Proof.

There is a well-defined $R$-module homomorphism

$\varphi:S^{-1}M\to M\otimes_{R}S^{-1}R,\ \ \frac{m}{s}\mapsto m\otimes\frac{1}{s},$

since for $m^{\prime}\in M$ and $s^{\prime}\in S$ with $\frac{m}{s}=\frac{m^{\prime}}{s^{\prime}}$, i. e. such that $u(s^{\prime}m-sm^{\prime})=0$ for some $u\in S$, we have

$m\otimes\frac{1}{s}-m^{\prime}\otimes\frac{1}{s^{\prime}}=u(s^{\prime}m-sm^{\prime})\otimes\frac{1}{uss^{\prime}}=0.$

Similarly, by the universal property of the tensor product we get a well-defined homomorphism

$\psi:M\otimes_{R}S^{-1}R\to S^{-1}M\quad\text{with}\quad\psi\Big{(}m\otimes\frac{a}{s}\Big{)}=\frac{am}{s},$

as for $a^{\prime}\in R$ and $s^{\prime}\in S$ with $u(s^{\prime}a-sa^{\prime})=0$ for some $u\in S$ we also get $u(s^{\prime}am-sa^{\prime}m)=0$, and thus $\frac{am}{s^{\prime}}=\frac{a^{\prime}m}{s^{\prime}}$. By construction, $\varphi$ and $\psi$ are inverse to each other, and thus $\varphi$ is an isomorphism. ∎

###### Remark 6.20 (Localization of homomorphisms).

Let $\varphi:M\to N$ be a homomorphism of $R$-modules, and let $S\subset R$ be a multiplicatively closed subset. Then by Construction 5.16 there is a well-defined homomorphism of $S^{-1}R$-modules

$\varphi\otimes\mathrm{id}:M\otimes_{R}S^{-1}R\to N\otimes_{R}S^{-1}R\quad\text{such that}\quad(\varphi\otimes\mathrm{id})\Big{(}m\otimes\frac{a}{s}\Big{)}=\varphi(m)\otimes\frac{a}{s}.$

By Lemma 6.19 this can now be considered as an $S^{-1}R$-module homomorphism

$S^{-1}\varphi:S^{-1}M\to S^{-1}N\quad\text{with}\quad S^{-1}\varphi\Big{(}\frac{m}{s}\Big{)}=\frac{\varphi(m)}{s}.$

We will call this the localization $S^{-1}\varphi$ of the homomorphism $\varphi$. As before, we will denote it by $\varphi_{a}$ or $\varphi_{P}$ if $S=\{a^{n}:n\in\mathbb{N}\}$ for an element $a\in R$ or $S=R\backslash P$ for a prime ideal $P\unlhd R$, respectively.

The localization of rings and modules is a very well-behaved concept in the sense that it is compatible with almost any other construction that we have seen so far. One of the most important properties is that it preserves exact sequences, which then means that it is also compatible with everything that can be expressed in terms of such sequences.

---

###### Proposition 6.21 (Localization is exact).

For every short exact sequence

$0\longrightarrow M_{1}\xrightarrow{\varphi}M_{2}\xrightarrow{\psi}M_{3}\longrightarrow 0$

of $R$-modules, and any multiplicatively closed subset $S\subset R$, the localized sequence

$0\longrightarrow S^{-1}M_{1}\xrightarrow{S^{-1}\varphi}S^{-1}M_{2}\xrightarrow{S^{-1}\psi}S^{-1}M_{3}\longrightarrow 0$

is also exact.

###### Proof.

By Lemma 6.19, localization at $S$ is just the same as tensoring with $S^{-1}R$. But tensor products are right exact by Proposition 5.22 (b), hence it only remains to prove the injectivity of $S^{-1}\varphi$.

So let $\frac{m}{s}\in S^{-1}M_{1}$ with $S^{-1}\varphi(\frac{m}{s})=\frac{\varphi(m)}{s}=0$. This means that there is an element $u\in S$ with $u\varphi(m)=\varphi(um)=0$. But $\varphi$ is injective, and therefore $um=0$. Hence $\frac{m}{s}=\frac{1}{us}\cdot um=0$, i. e. $S^{-1}\varphi$ is injective. ∎

###### Corollary 6.22.

Let $S$ be a multiplicatively closed subset of a ring $R$.

- For any homomorphism $\varphi:M\to N$ of $R$-modules we have $\ker(S^{-1}\varphi)=S^{-1}\ker\varphi$ and $\operatorname{im}(S^{-1}\varphi)=S^{-1}\operatorname{im}\varphi$.

In particular, if $\varphi$ is injective / surjective then $S^{-1}\varphi$ is injective / surjective, and if $M$ is a submodule of $N$ then $S^{-1}M$ is a submodule of $S^{-1}N$ in a natural way.
- If $M$ is a submodule of an $R$-module $N$ then $S^{-1}(N/M)\cong S^{-1}N/S^{-1}M$.
- For any two $R$-modules $M$ and $N$ we have $S^{-1}(M\oplus N)\cong S^{-1}M\oplus S^{-1}N$.

###### Proof.

- Localizing the exact sequence $0\longrightarrow\ker\varphi\longrightarrow M\xrightarrow{\varphi}\operatorname{im}\varphi\longrightarrow 0$ of Example 4.3 (a) at $S$, we get by Proposition 6.21 an exact sequence

$0\longrightarrow S^{-1}\ker\varphi\longrightarrow S^{-1}M\xrightarrow{S^{-1}\varphi}S^{-1}\operatorname{im}\varphi\longrightarrow 0.$

But again by Example 4.3 this means that the modules $S^{-1}\ker\varphi$ and $S^{-1}\operatorname{im}\varphi$ in this sequence are the kernel and image of the map $S^{-1}\varphi$, respectively.
- This time we localize the exact sequence $0\longrightarrow M\longrightarrow N\longrightarrow N/M\longrightarrow 0$ of Example 4.3 (b) to obtain by Proposition 6.21

$0\longrightarrow S^{-1}M\longrightarrow S^{-1}N\longrightarrow S^{-1}(N/M)\to 0,$

which by Example 4.3 means that the last module $S^{-1}(N/M)$ in this sequence is isomorphic to the quotient $S^{-1}N/S^{-1}M$ of the first two.
- This follows directly from the definition, or alternatively from Lemma 5.8 (c) as localization is the same as taking the tensor product with $S^{-1}R$. ∎

###### Remark 6.23.

If an operation such as localization preserves short exact sequences as in Proposition 6.21, the same then also holds for longer exact sequences: in fact, we can split a long exact sequence of $R$-modules into short ones as in Remark 4.5, localize it to obtain corresponding short exact sequences of $S^{-1}R$-modules, and then glue them back to a localized long exact sequence by Lemma 4.4 (b).

###### Exercise 6.24.

Let $S$ be a multiplicatively closed subset of a ring $R$, and let $M$ be an $R$-module. Prove:

- For $M_{1},M_{2}\leq M$ we have $S^{-1}(M_{1}+M_{2})=S^{-1}M_{1}+S^{-1}M_{2}$.
- For $M_{1},M_{2}\leq M$ we have $S^{-1}(M_{1}\cap M_{2})=S^{-1}M_{1}\cap S^{-1}M_{2}$. However, if $M_{i}\leq M$ for all $i$ in an arbitrary index set $J$, it is in general not true that $S^{-1}\big{(}\bigcap_{i\in J}M_{i}\big{)}=\bigcap_{i\in J}S^{-1}M_{i}$. Does at least one inclusion hold?
- For an ideal $I\unlhd R$ we have $S^{-1}\sqrt{I}=\sqrt{S^{-1}I}$.

---

###### Example 6.25.

Let $P$ and $Q$ be maximal ideals in a ring $R$; we want to compute the ring $R_{Q}/P_{Q}$. Note that this is also an $R_{Q}$-module, and as such isomorphic to $(R/P)_{Q}$ by Corollary 6.22 (b). So when viewed as such a module, it does not matter whether we first localize at $Q$ and then take the quotient by $P$ or vice versa.

1. If $P\neq Q$ we must also have $P\not\subset Q$ since $P$ is maximal and $Q\neq R$. So there is an element $a\in P\backslash Q$, which leads to $\frac{1}{1}=\frac{a}{a}\in P_{Q}$. Hence in this case the ideal $P_{Q}$ in $R_{Q}$ is the whole ring, and we obtain $R_{Q}/P_{Q}=(R/P)_{Q}=0$.
2. On the other hand, if $P=Q$ there is a well-defined ring homomorphism

$\varphi:R/P\to R_{P}/P_{P},\ \ \overline{a}\mapsto\overline{\left(\frac{a}{1}\right)}.$

We can easily construct an inverse of this map as follows: the morphism $R\to R/P$, $a\mapsto\overline{a}$ sends $R\backslash P$ to units since $R/P$ is a field by Lemma 2.3 (b), hence it passes to a morphism

$R_{P}\to R/P,\ \ \frac{a}{s}\mapsto\overline{s}^{-1}\overline{a}$

by Exercise 6.12. But $P_{P}$ is in the kernel of this map, and thus we get a well-defined ring homomorphism

$R_{P}/P_{P}\to R/P,\ \ \overline{\left(\frac{a}{s}\right)}\mapsto\overline{s}^{-1}\overline{a},$

which clearly is an inverse of $\varphi$. So the ring $R_{P}/P_{P}$ is isomorphic to $R/P$.

Note that this result is also easy to understand from a geometric point of view: let $R$ be the ring of functions on a variety $X$ over an algebraically closed field, and let $p,q\in X$ be the points corresponding to the maximal ideals $P$ and $Q$, respectively (see Remark 2.7 (a)). Then taking the quotient by $P=I(p)$ means restricting the functions to the point $p$ by Lemma 0.9 (d), and localizing at $Q$ corresponds to restricting them to an arbitrarily small neighborhood of $q$ by Example 6.5 (d).

So first of all we see that the order of these two operations should not matter, since restrictions of functions commute. Moreover, if $p\neq q$ then our small neighborhood of $q$ does not meet $p$, and we get the zero ring as the space of functions on the empty set. In contrast, if $p=q$ then after restricting the functions to the point $p$ another restriction to a neighborhood of $p$ does not change anything, and thus we obtain the isomorphism of (b) above.

As an application of this result, we get the following refinement of the notion of length of a module: not only is the length of all composition series the same, but also the maximal ideals occurring in the quotients of successive submodules in the composition series as in Definition 3.18 (a).

###### Corollary 6.26 (Length of localized modules).

Let $M$ be an $R$-module of finite length, and let

$0=M_{0}\subsetneq M_{1}\subsetneq\cdots\subsetneq M_{n}=M$

be a composition series for $M$, so that $M_{i}/M_{i-1}\cong R/I_{i}$ by Definition 3.18 (a) with some maximal ideals $I_{i}\unlhd R$ for $i=1,\ldots,n$.

Then for any maximal ideal $P\unlhd R$ the localization $M_{P}$ is of finite length as an $R_{P}$-module, and its length $l_{R_{P}}(M_{P})$ is equal to the number of indices $i$ such that $I_{i}=P$. In particular, up to permutations the ideals $I_{i}$ (and their multiplicities) as above are the same for all choices of composition series.

###### Proof.

Let $P\unlhd R$ be a maximal ideal. From the given composition series we obtain a chain of localized submodules

$0=(M_{0})_{P}\subset(M_{1})_{P}\subset\cdots\subset(M_{n})_{P}=M_{P}.$ ($\ast$)

For its successive quotients $(M_{i})_{P}/(M_{i-1})_{P}$ for $i=1,\ldots,n$ we get by Corollary 6.22 (b)

$(M_{i})_{P}/(M_{i-1})_{P}\cong(M_{i}/M_{i-1})_{P}\cong(R/I_{i})_{P}\cong R_{P}/(I_{i})_{P}.$

But by Example 6.25 this is $0$ if $I_{i}\neq P$, whereas for $I_{i}=P$ it is equal to $R_{P}$ modulo its unique maximal ideal $P_{P}$ by Corollary 6.10. So by deleting all equal submodules from the chain ($\ast$) we obtain a composition series for $M_{P}$ over $R_{P}$ whose length equals the number of indices $i\in\{1,\ldots,n\}$ with $I_{i}=P$. ∎

##

---

6. Localization

We can rephrase Corollary 6.26 by saying that the length of a module is a "local concept": if an  $R$ -module  $M$  is of finite length and we know the lengths of the localized modules  $M_P$  for all maximal ideals  $P \triangleleft R$ , we also know the length of  $M$ : it is just the sum of all the lengths of the localized modules.

In a similar way, there are many other properties of an  $R$ -module  $M$  that carry over from the localized modules  $M_P$ , i.e. in geometric terms from considering  $M$  locally around small neighborhoods of every point. This should be compared to properties in geometric analysis such as continuity and differentiability: if we have e.g. a function  $f: U \to \mathbb{R}$  on an open subset  $U$  of  $\mathbb{R}$  we can define what it means that it is continuous at a point  $p \in U$  — and to check this we only need to know  $f$  in an arbitrarily small neighborhood of  $p$ . In total, the function  $f$  is then continuous if and only if it is continuous at all points  $p \in U$ : we can say that "continuity is a local property". Here are some algebraic analogues of such local properties:

Proposition 6.27 (Local properties). Let  $R$  be a ring.

(a) If  $M$  is an  $R$ -module with  $M_P = 0$  for all maximal ideals  $P \triangleleft R$ , then  $M = 0$ .
(b) Consider a sequence of  $R$ -module homomorphisms

$$
0 \longrightarrow M _ {1} \xrightarrow {\varphi_ {1}} M _ {2} \xrightarrow {\varphi_ {2}} M _ {3} \longrightarrow 0. \tag {*}
$$

If the localized sequences of  $R_P$ -modules

$$
0 \longrightarrow (M _ {1}) _ {P} \xrightarrow {(\varphi_ {1}) _ {P}} (M _ {2}) _ {P} \xrightarrow {(\varphi_ {2}) _ {P}} (M _ {3}) _ {P} \longrightarrow 0
$$

are exact for all maximal ideals  $P \trianglelefteq R$ , then the original sequence  $(*)$  is exact as well.

We say that being zero and being exact are "local properties" of a module and a sequence, respectively. Note that the converse of both statements holds as well by Proposition 6.21.

Proof.

(a) Assume that  $M \neq 0$ . If we then choose an element  $m \neq 0$  in  $M$ , its annihilator  $\mathrm{ann}(m)$  does not contain  $1 \in R$ , so it is a proper ideal of  $R$  and thus by Corollary 2.17 contained in a maximal ideal  $P$ . Hence for all  $u \in R \setminus P$  we have  $u \notin \mathrm{ann}(m)$ , i.e.  $um \neq 0$  in  $M$ . This means that  $\frac{m}{1}$  is non-zero in  $M_P$ , and thus  $M_P \neq 0$ .
(b) It suffices to show that a three-term sequence  $L \xrightarrow{\varphi} M \xrightarrow{\psi} N$  is exact if all localizations  $L_P \xrightarrow{\varphi_P} M_P \xrightarrow{\psi_P} N_P$  are exact for maximal  $P \triangleleft R$ , since we can then apply this to all three possible positions in the five-term sequence of the statement.

To prove this, note first that

$$
\begin{array}{l} \left(\psi \left(\varphi (L)\right)\right) _ {P} = \left\{\frac {\psi \left(\varphi (m)\right)}{s}: m \in L, s \in S \right\} = \left\{\psi_ {P} \left(\varphi_ {P} \left(\frac {m}{s}\right)\right): m \in L, s \in S \right\} \\ = \psi_ {P} \left(\varphi_ {P} \left(L _ {P}\right)\right) = 0, \\ \end{array}
$$

since the localized sequence is exact. This means by (a) that  $\psi (\varphi (L)) = 0$ , i.e.  $\mathrm{im}\varphi \subset \ker \psi$ . We can therefore form the quotient  $\ker \psi /\mathrm{im}\varphi$ , and get by the exactness of the localized sequence

$$
\left(\ker \psi / \operatorname {i m} \varphi\right) _ {P} \cong \left(\ker \psi\right) _ {P} / \left(\operatorname {i m} \varphi\right) _ {P} = \ker \psi_ {P} / \operatorname {i m} \varphi_ {P} = 0
$$

using Corollary 6.22. But this means  $\ker \psi / \operatorname{im} \varphi = 0$  by (a), and so  $\ker \psi = \operatorname{im} \varphi$ , i.e. the sequence  $L \xrightarrow{\varphi} M \xrightarrow{\psi} N$  is exact.

Remark 6.28. As usual, Proposition 6.27 (b) means that all properties that can be expressed in terms of exact sequences are local as well: e.g. an  $R$ -module homomorphism  $\varphi : M \to N$  is injective (resp. surjective) if and only if its localizations  $\varphi_P : M_P \to N_P$  for all maximal ideals  $P \triangleleft R$  are injective (resp. surjective). Moreover, as in Remark 6.23 it follows that Proposition 6.27 (b) holds for longer exact sequences as well.

Exercise 6.29. Let  $R$  be a ring. Show:

---

Andreas Gathmann

(a) Ideal containment is a local property: for two ideals $I, J \triangleleft R$ we have $I \subset J$ if and only if $I_P \subset J_P$ in $R_P$ for all maximal ideals $P \triangleleft R$.

(b) Being reduced is a local property, i.e. $R$ is reduced if and only if $R_P$ is reduced for all maximal ideals $P \triangleleft R$.

(c) Being an integral domain is not a local property, i.e. $R$ might not be an integral domain although the localizations $R_P$ are integral domains for all maximal ideals $P \triangleleft R$. Can you give a geometric interpretation of this statement?