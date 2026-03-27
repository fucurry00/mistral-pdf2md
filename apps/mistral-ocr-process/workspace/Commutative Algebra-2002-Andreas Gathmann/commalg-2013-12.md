Andreas Gathmann

# 12. Valuation Rings

In the remaining two chapters of this class we will restrict our attention to 1-dimensional rings, i.e. geometrically to curves. More precisely, we will only deal with 1-dimensional rings whose localizations at all maximal ideals are regular. For a curve  $X$  over an algebraically closed field, when the maximal ideals of  $A(X)$  are in one-to-one correspondence with points of  $X$  by Remark 10.11, this means precisely that we will require  $X$  to be smooth, i.e. that all points of  $X$  are smooth in the sense of Example 11.37 and Definition 11.38.

In the current chapter we will consider such rings and varieties from a local point of view, postponing their global study to Chapter 13. Such 1-dimensional regular local rings are probably the "nicest" rings (that are not fields) — they have a very special structure as we will see in the following key lemma and its geometric interpretation.

Lemma 12.1. Let  $R$  be a 1-dimensional regular local ring.

(a) The maximal ideal  $P$  of  $R$  is a non-zero principal ideal.
(b) For every element  $a \in R \setminus \{0\}$  there is a unique number  $n \in \mathbb{N}$  such that  $(a) = P^n$ . We will call it the valuation of  $a$  (see Remark 12.15 (a)).

# Proof.

(a) By assumption, the vector space dimension of  $P / P^2$  over  $R / P$  is 1. But this is also the minimum number of generators for  $P$  by Lemma 11.36 (a), hence  $P$  is principal and nonzero.
(b) By Proposition 11.40 we know that  $R$  is an integral domain. So it has a unique minimal prime ideal 0 and a unique maximal ideal  $P$ , and since  $\dim R = 1$  these two prime ideals are in fact the only ones. Hence by Lemma 2.21 we know that  $\sqrt{(a)}$  is equal to  $P$  or  $R$ . In both cases it follows that  $P^n \subset (a)$  for some  $n \in \mathbb{N}$  by Exercise 7.22 (b). Since  $P$  is principal by (a), we can write this equivalently as  $t^n = ba$  for some  $b \in R$  and a generator  $t$  of  $P$ .

Now choose  $n$  minimal with this property. Then  $b$  must be a unit: otherwise  $(b)$  is contained in a maximal ideal by Corollary 2.17, which must be  $P$ . Hence  $b = b' t$  for some  $b' \in R$ , so  $t^n = b' t a$ , and thus  $t^{n-1} = b' a$  since  $R$  is an integral domain — in contradiction to the minimality of  $n$ .

So with this choice of  $n$  we get  $t^n = ba$  for a unit  $b$ , which means that  $(a) = (t^n) = P^n$ . Moreover, no other choice of exponent would work: if we had  $t^k = ca$  for a unit  $c$  and  $k &lt; n$  (resp.  $k &gt; n$ ), then this would imply that  $t^{n - k} = bc^{-1}$  (resp.  $t^{k - n} = cb^{-1}$ ) is a unit, in contradiction to  $t \in P$ .

Remark 12.2 (Geometric interpretation: orders of vanishing). Let  $x$  be a fixed smooth point on a curve  $X$ , and let  $R$  be the ring of local functions on  $X$  at  $x$ , i.e. the localization of  $A(X)$  at the maximal ideal  $I(x)$  as in Example 6.5 (d). Then  $R$  is a 1-dimensional regular local ring.

![img-0.jpeg](images/img-0.jpeg)

The maximal ideal  $P$  of  $R$  then consists of all local functions that vanish at  $x$ , and a generator  $t$  for  $P$  as in Lemma 12.1 (a) can be thought of as a local coordinate for  $X$  in a neighborhood of  $x$  (that has the value 0 at  $x$ , and vanishes to order 1 there). Consequently, if  $a \in R$  is a local function on  $X$  at  $x$  the equation  $(a) = P^n$  of Lemma 12.1 (b), i.e.  $a = ct^n$  for a unit  $c$ , means that  $a$  vanishes to order  $n$  at  $x$ . We can therefore think of the valuation constructed in Lemma 12.1 as an order of vanishing of a local function on a curve at a point.

Actually, the full algebraic notion of a valuation is more general than above: one considers valuations on general integral domains and in fact also on their quotient fields, and allows their values to be in

---

12. Valuation Rings

any ordered Abelian group instead of just in $\mathbb{N}$ or $\mathbb{Z}$. Let us give the precise definition now, returning to our special case of 1-dimensional regular local rings later in Proposition 12.14.

**Definition 12.3 (Valuations and valuation rings).**

(a) An **ordered group** is an Abelian group $G$ (usually written additively) with a total order $\leq$ such that $m \leq n$ implies $m + k \leq n + k$ for all $m, n, k \in G$.

(b) Let $K$ be a field; as usual we write $K^{*}$ for $K \setminus \{0\}$. A **valuation** on $K$ is a map $\nu : K^{*} \to G$ for an ordered group $G$ such that for all $a, b \in K^{*}$ we have

(i) $\nu(ab) = \nu(a) + \nu(b)$ (i.e. $\nu$ is a homomorphism of groups); and

(ii) $\nu(a + b) \geq \min(\nu(a), \nu(b))$ if $a + b \neq 0$.

We extend this map formally to all of $K$ by setting $\nu(0) := \infty$, so that (i) and (ii) hold for all $a, b \in K$.

(c) For a valuation $\nu : K^{*} \to G$ the subgroup $\nu(K^{*}) \leq G$ is called the **value group**, and

$$
R_{\nu} := \{a \in K : \nu(a) \geq 0\}
$$

the **valuation ring** of $\nu$. Note that it is indeed a ring: we clearly have $\nu(0) = \infty \geq 0$ and $\nu(1) = 0$, and for $a, b \in K$ with $\nu(a) \geq 0$ and $\nu(b) \geq 0$ it follows immediately from (i) and (ii) above that $\nu(a + b) \geq 0$ and $\nu(ab) \geq 0$ as well.

**Example 12.4.**

(a) Any field $K$ allows the **trivial valuation** $\nu : K^{*} \to \{0\}$, $a \mapsto 0$. Its value group is $\{0\}$, and its valuation ring is $K$ itself. Note that even in this case we still have $\nu(0) = \infty$ by definition.

(b) The groups $\mathbb{Z}$, $\mathbb{Q}$, and $\mathbb{R}$ are all ordered. In fact, the most common non-trivial value group in our examples will be $\mathbb{Z}$ (see Proposition 12.13). But for general valuations other groups may occur as well, as we will see e.g. in (e) below, and in the proof of Proposition 12.8.

(c) The most important example of a valuation is the following. Fix a prime element $p$ in a unique factorization domain $R$, and let $K = \operatorname{Quot} R$. Note that every non-zero element of $R$ can be written uniquely as $a p^n$ for some $n \in \mathbb{N}$ and $a \in R$ with $p \nmid a$, and consequently every element of $K^*$ can be written uniquely as $a p^n$ for some $n \in \mathbb{Z}$ and $a \in K^*$ that can be written as a quotient of elements of $R$ that do not contain $p$ as a factor. With this representation there is an obvious map

$$
\nu : K^{*} \to \mathbb{Z}, \quad a p^n \mapsto n
$$

that assigns to every element the exponent of $p$ in its prime factorization. It is clearly well-defined and a homomorphism of groups. It also satisfies condition (ii) of Definition 12.3 (b): for any two such elements $a p^n$ and $b p^m$ (with $a, b \in K^*$ not containing the prime factor $p$, and $n, m \in \mathbb{Z}$), without loss of generality with $n \geq m$, we have

$$
\nu(a p^n + b p^m) = \nu\big(p^m (a p^{n - m} + b)\big) = m + \nu(a p^{n - m} + b) \stackrel{(*)}{\geq} m = \nu(b p^m),
$$

where $(*)$ follows since $a p^{n - m} + b$ does not contain the factor $p$ in its denominator. Hence $\nu$ is a valuation on $K$. Its value group is obviously $\mathbb{Z}$, and its valuation ring is

$$
R_{\nu} = \{a p^n : a \in K^*, n \in \mathbb{N}, a \text{ does not contain } p\} \cup \{0\},
$$

i.e. precisely the localization $R_{(p)}$ of $R$ at the prime ideal $(p)$ as in Example 6.5 (d).

(d) Let $L$ be a field, and let

$$
K = \left\{\sum_{n \in \mathbb{Z}} a_n t^n : a_n \in L \text{ for all } n, \text{ the set } \{n \in \mathbb{Z} : a_n \neq 0\} \text{ is bounded below} \right\}
$$

be the set of all formal “power series with integer exponents” in one variable $t$. As in the case of the usual power series ring $L[[t]]$, there are no convergence requirements on the coefficients of the series [G1, Definition 9.1]. We do require however that for a non-zero element $f \in K$ there is a minimum exponent of $t$ occurring in $f$, which implies that we can write $f$ uniquely as $f = t^n g$ for some $n \in \mathbb{Z}$ and $g \in L[[t]]$ with non-zero constant coefficient. With

---

Andreas Gathmann

this definition $K$ is in fact a field: it is obvious that it is a ring, and since a power series with non-zero constant coefficient is invertible [G1, Exercise 9.12], a multiplicative inverse of $t^n g$ as above is $t^{-n}g^{-1}$. We call $K$ the field of (formal) Laurent series over $L$.

It is now obvious that

$$
\nu : K^* \to \mathbb{Z}, \quad \sum_{n \in \mathbb{Z}} a_n t^n \mapsto \min \{n \in \mathbb{Z} : a_n \neq 0\}
$$

is a valuation on $K$. Its valuation ring is simply the ring $L[[t]]$ of power series over $L$. In fact, this construction is a special case of (c) since one can show that $L[[t]]$ is a unique factorization domain with $t \in L[[t]]$ prime, and $K = \mathrm{Quot}(L[[t]])$.

(c) The idea of (d) can be generalized to construct a valuation with value group $\mathbb{Q}$: for a field $L$ we now consider the set

$$
\begin{array}{c}
K = \Big\{ \sum_{q \in \mathbb{Q}} a_q t^q : a_q \in L \text{ for all } q, \text{ the set } \{q \in \mathbb{Q} : a_q \neq 0\} \text{ is bounded below} \\
\text{and has bounded denominators} \Big\} \\
\end{array}
$$

of all formal "power series with rational exponents", and the same map

$$
\nu : K^* \to \mathbb{Q}, \quad \sum_{q \in \mathbb{Q}} a_q t^q \mapsto \min \{q \in \mathbb{Q} : a_q \neq 0\}
$$

as above. It can then be checked that $K$ is again a field — we will not do this here as we will not need this field again — and that $\nu$ is a valuation with value group $\mathbb{Q}$. The field $K$ is called the field of (formal) Puiseux series over $L$.

**Remark 12.5.**

(a) We will see in Propositions 12.13 and 12.14 that a 1-dimensional regular local ring is a unique factorization domain, and that in this case the construction of Example 12.4 (c) specializes to our original situation of Lemma 12.1 and Remark 12.2. For the moment it suffices to note that, in the geometric situation, we should imagine $K$ in Definition 12.3 to be the field of rational functions on a variety $X$ around a smooth point $a$. The valuation $\nu(f) \in \mathbb{Z}$ of an element $f \in K^*$ can then be thought of as the order of the zero (if $\nu(f) &gt; 0$) or pole (if $\nu(f) &lt; 0$) of $f$ at $a \in X$.

(b) It is clear from Definition 12.3 that every valuation ring $R_\nu$ of a valuation $\nu$ is an integral domain, since it is a subring of a field. In fact, valuation rings have many more nice properties. Let us prove the most important ones now.

**Lemma 12.6 (Properties of valuation rings).** Let $R = R_\nu$ be the valuation ring of a valuation $\nu: K^* \to G$ as in Definition 12.3.

(a) For all $a \in K^*$ we have $a \in R$ or $a^{-1} \in R$.

(b) For all $a, b \in R$ we have $\nu(a) \leq \nu(b)$ if and only if $b \in (a)$.

(c) The group of units of $R$ is $R^* = \{a \in R : \nu(a) = 0\}$.

(d) $R$ is a local ring with maximal ideal $P = \{a \in R : \nu(a) &gt; 0\}$.

(e) $R$ is a normal domain.

**Proof.**

(a) Since $\nu(a) + \nu(a^{-1}) = \nu(aa^{-1}) = \nu(1) = 0$ we must have $\nu(a) \geq 0$ or $\nu(a^{-1}) \geq 0$, and thus $a \in R$ or $a^{-1} \in R$.

(b) The statement is obvious for $a = 0$, so let us assume that $a \neq 0$. If $\nu(a) \leq \nu(b)$ then $\nu\left(\frac{b}{a}\right) = \nu(b) - \nu(a) \geq 0$, hence $\frac{b}{a} \in R$, and thus $b = \frac{b}{a} \cdot a \in (a)$. Conversely, if $b \in (a)$ then $b = ca$ for some $c \in R$, and therefore $\nu(b) = \nu(c) + \nu(a) \geq \nu(a)$.

(c) Let $a \in R$ with $a \neq 0$, so $\nu(a) \geq 0$. Then $a \in R^*$ if and only if $a^{-1} \in R$, i.e. $\nu(a^{-1}) = -\nu(a) \geq 0$ as well, which is the case if and only if $\nu(a) = 0$.

---

.
4. It is clear that $P$ is an ideal, since $a,b\in P$ and $r\in R$ imply $\nu(a+b)\geq\min(\nu(a),\nu(b))>0$ and $\nu(ra)=\nu(r)+\nu(a)>0$. Moreover, any bigger ideal contains an element with valuation $0$, i. e. a unit by (c), and thus is equal to $R$.
5. Let $a\in K^{*}$ be integral over $R$. Then $a^{n}+c_{n-1}a^{n-1}+\cdots+c_{0}=0$ for some $n\in\mathbb{N}$ and $c_{0},\ldots,c_{n-1}\in R$. Assume that $a\notin R$. Then $a^{-1}\in R$ by (a), which leads to the contradiction

$a=-c_{n-1}-\cdots-c_{0}a^{-n+1}\quad\in R.$

Hence we must have $a\in R$ as claimed. ∎

So far, we have always started with a valuation $\nu$ on a field $K$, and then constructed a valuation ring $R_{\nu}\subset K$ from it. We will now show that this process can be reversed: the valuation ring $R_{\nu}$ itself contains in fact enough information to reconstruct the valuation $\nu$ from it.

###### Construction 12.7 (Reconstruction of the valuation from its valuation ring).

Let $R=R_{\nu}$ be the valuation ring of a valuation $\nu:K^{*}\to G$ as in Definition 12.3. Then $\nu$ can be recovered completely from $R$ up to isomorphisms in the following sense:

1. We must have $K=\operatorname{Quot}R$: the inclusion “$\supset$” is obvious, and “$\subset$” follows from Lemma 12.6 (a), since both $a\in R$ and $a^{-1}\in R$ imply $a\in\operatorname{Quot}R$.
2. The group homomorphism $\nu:K^{*}\to G$ has kernel $R^{*}$ by Lemma 12.6 (c), and image $\nu(K^{*})$. Hence the homomorphism theorem implies that the value group $\nu(K^{*})$ is isomorphic to $K^{*}/R^{*}$ (which is uniquely determined by $R$ due to (a)), and that with this isomorphism the valuation map $\nu:K^{*}\to K^{*}/R^{*}$ is just the quotient map.
3. The order on $\nu(K^{*})$ is determined by $R$ since for $a,b\in K^{*}$ we have $\nu(a)\leq\nu(b)$ if and only if $\nu(\frac{b}{a})\geq 0$, i. e. if $\frac{b}{a}\in R$.

So we can say that every valuation ring belongs to a unique valuation (if we assume the valuation to be surjective, i. e. we can of course not recover the whole group $G$ from $R$, but only the valuation subgroup $\nu(K^{*})$ of $G$). In fact, there is even an easy criterion to determine whether a given ring is such a valuation ring:

###### Proposition 12.8 (Alternative characterization of valuation rings).

For a ring $R$ the following statements are equivalent:

1. $R$ is the valuation ring of a valuation $\nu:K^{*}\to G$ (which is then unique up to isomorphisms by Construction 12.7).
2. $R$ is an integral domain, and for all $a\in\operatorname{Quot}R\backslash\{0\}$ we have $a\in R$ or $a^{-1}\in R$.

###### Proof.

The implication (a) $\Rightarrow$ (b) is just Lemma 12.6 (a). For the opposite direction, let $R$ be an integral domain, set $K=\operatorname{Quot}(R)$ and $G=K^{*}/R^{*}$. Note that, in contrast to Definition 12.3 (a), the group $G$ will be written *multiplicatively* in this proof. Now

$\overline{a}\leq\overline{b}\ \ :\Leftrightarrow\ \ \frac{b}{a}\in R$

is a well-defined relation on $G$ (for $a,b\in K^{*}$ and $c,d\in R^{*}$ with $\frac{b}{a}\in R$ we have $\frac{bd}{ac}\in R$) and makes $G$ into an ordered group (for $a,b,c\in K^{*}$ with $\frac{b}{a}\in R$ we have $\frac{bc}{ac}\in R$). Let $\nu:K^{*}\to G$ be the quotient map, so that $\nu(a)\leq\nu(b)$ for $a,b\in K^{*}$ if and only if $\frac{b}{a}\in R$. Then $\nu$ is a valuation:

1. The relation $\nu(ab)=\nu(a)\,\nu(b)$ is obvious.
2. Let $a,b\in K^{*}$. By assumption we have $\frac{a}{b}\in R$ or $\frac{b}{a}\in R$. In the first case $\frac{a+b}{b}=\frac{a}{b}+1\in R$ and thus $\nu(a+b)\geq\nu(b)$, whereas in the second case we get similarly $\nu(a+b)\geq\nu(a)$. Hence $\nu(a+b)\geq\min(\nu(a),\nu(b))$.

Its valuation ring $R_{\nu}$ is now exactly $R$, since we have $\nu(a)\geq 0=\nu(1)$ for $a\in K^{*}$ if and only if $\frac{a}{1}\in R$. ∎

---

Andreas Gathmann

Remark 12.9.

Proposition 12.8 states that we could alternatively define a valuation ring to be an integral domain $R$ such that $a\in R$ or $a^{-1}\in R$ for all $a\in\mathrm{Quot}R\backslash\{0\}$. In fact, one will often find this definition in the literature, and in the following we will also often talk about a valuation ring $R$ without mentioning a valuation first. Our results above show that even then the ring $R$ always has a unique valuation $\nu:K\to G$ associated to it such that $R=R_{\nu}$ and $\nu$ is surjective.

This alternative characterization of valuation rings allows us to prove some more of their properties that would be harder to see using the original Definition 12.3. The following lemma and proposition give two examples of this.

###### Lemma 12.10 (Enlarging valuation rings).

Let $R$ be a valuation ring, and let $R^{\prime}$ be another ring with $R\subset R^{\prime}\subset\mathrm{Quot}R$. Then $R^{\prime}$ is also a valuation ring, with $\mathrm{Quot}R^{\prime}=\mathrm{Quot}R$.

###### Proof.

Taking quotient fields in the inclusion $R\subset R^{\prime}\subset\mathrm{Quot}R$ we see that $\mathrm{Quot}R^{\prime}=\mathrm{Quot}R$. Now if $a\in\mathrm{Quot}R^{\prime}=\mathrm{Quot}R$ we have $a\in R$ or $a^{-1}\in R$ by Proposition 12.8, and hence also $a\in R^{\prime}$ or $a^{-1}\in R^{\prime}$. Therefore $R^{\prime}$ is a valuation ring by Proposition 12.8 again. ∎

###### Proposition 12.11 (Integral closure from valuation rings).

Let $R$ be an integral domain, and let $\overline{R}$ be its integral closure in $\mathrm{Quot}R$. Then

\[ \overline{R}=\bigcap_{\begin{subarray}{c}R\subset R^{\prime}\subset\mathrm{Quot}R\\
R^{\prime}\text{ valuation ring}\end{subarray}}R^{\prime}. \]

###### Proof.

“$\subset$” Let $x\in\overline{R}$, and let $R^{\prime}$ be a valuation ring with $R\subset R^{\prime}\subset\mathrm{Quot}R$. So $x\in\mathrm{Quot}R=\mathrm{Quot}R^{\prime}$ is integral over $R$, and thus also over $R^{\prime}$. But then $x\in R^{\prime}$ since $R^{\prime}$ is normal by Lemma 12.6 (e).

“$\supset$” Let $x\notin\overline{R}$. We will construct a valuation ring $R^{\prime}$ with $R\subset R^{\prime}\subset\mathrm{Quot}R$ and $x\notin R^{\prime}$.

Note that $x\notin R[\frac{1}{x}]$, since otherwise there would be a relation $x=a_{0}+a_{1}x^{-1}+\dots+a_{n}x^{-k}$ with $a_{0},\dots,a_{k}\in R$, which means that $x^{k+1}-a_{0}x^{k}-a_{1}x^{k-1}-\dots-a_{k}=0$, and thus that $x$ would be integral over $R$ in contradiction to $x\notin\overline{R}$. So the set

$M=\{R^{\prime}:R^{\prime}\text{ is a ring with }R[\frac{1}{x}]\subset R^{\prime}\subset\mathrm{Quot}R\text{ and }x\notin R^{\prime}\}$

is non-empty since it contains $R[\frac{1}{x}]$. By Zorn’s Lemma as in Proposition 2.16 it contains a maximal element $R^{\prime}$. Of course we then have $R\subset R^{\prime}\subset\mathrm{Quot}R$ and $x\notin R^{\prime}$, so it only remains to show that $R^{\prime}$ is a valuation ring.

We will prove this using the criterion of Proposition 12.8 (b). So let $a\in\mathrm{Quot}R^{\prime}=\mathrm{Quot}R$, and assume for a contradiction that $a\notin R^{\prime}$ and $a^{-1}\notin R^{\prime}$. Then $R^{\prime}[a]$ and $R^{\prime}[a^{-1}]$ strictly contain $R^{\prime}$, and thus by maximality of $R^{\prime}$ in $M$ we conclude that $x\in R^{\prime}[a]$ and $x\in R^{\prime}[a^{-1}]$. So we can write

$x=\sum_{i=0}^{n}r_{i}a^{i}=\sum_{i=0}^{m}s_{i}a^{-i}$

for some $n,m\in\mathbb{N}$ and $r_{0},\dots,r_{n},s_{0},\dots,s_{m}\in R^{\prime}$. We can choose $n$ and $m$ minimal, and assume without loss of generality that $m\leq n$. Then

$x$ $=s_{0}+(x-s_{0})\,x^{-1}\,\sum_{i=0}^{n}r_{i}a^{i}$
$=s_{0}+(x-s_{0})\,x^{-1}\,\sum_{i=0}^{n-1}r_{i}a^{i}+\sum_{i=1}^{m}s_{i}a^{-i}\,x^{-1}\,r_{n}a^{n}$

is a polynomial expression of degree less than $n$ in $a$ with coefficients in $R^{\prime}$, in contradiction to the minimality of $n$. Hence our assumption $a\notin R^{\prime}$ and $a^{-1}\notin R^{\prime}$ must have been wrong, and we conclude that $R^{\prime}$ is a valuation ring. ∎

###### Exercise 12.12.

Let $R$ be a valuation ring with value group $G$. Let us call a subset $A\subset G$ non-negative if $a\geq 0$ for all $a\in G$, and saturated if for all $a,b\in G$ with $a\leq b$ and $a\in A$ we have $b\in A$. Show:

---

12. Valuation Rings

(a) There is a natural inclusion-preserving one-to-one correspondence between ideals of $R$ and non-negative saturated subsets of $G$.
(b) For any two ideals $I, J \subset R$ we have $I \subset J$ or $J \subset I$.

So far we have considered arbitrary valuation rings. However, as most rings occurring in practice are Noetherian, we now want to specialize to this case. Surprisingly, this seemingly small additional assumption has far-reaching consequences: it fixes the value group to be $\mathbb{Z}$, restricts the possibilities to the 1-dimensional regular local rings of Lemma 12.1, and leads to many other nice properties as the following two propositions show.

**Proposition and Definition 12.13 (Discrete valuation rings).** For a valuation ring $R$ with unique maximal ideal $P$ (see Lemma 12.6 (d)) the following statements are equivalent:

(a) $R$ is Noetherian, but not a field.
(b) $R$ is a principal ideal domain, but not a field.
(c) The value group of $R$ is $\mathbb{Z}$.

Moreover, in this case the valuation $\nu(a) \in \mathbb{Z}$ of an element $a \in R \setminus \{0\}$ is the unique natural number $n$ such that $(a) = P^n$.

If the above equivalent conditions hold, we say that $R$ is a discrete valuation ring (short: DVR).

**Proof.**

(a) $\Rightarrow$ (b): As $R$ is Noetherian, every ideal $I$ in $R$ can be written as $I = (a_{1},\ldots ,a_{r})$ for some $a_1,\dots ,a_r$ by Lemma 7.4 (c). Now if $a_{i}$ has minimal valuation among these elements then $a_{j}\in (a_{i})$ for all $j = 1,\ldots ,r$ by Lemma 12.6 (b), and hence $I = (a_{i})$.
(b) $\Rightarrow$ (c): The maximal ideal $P$ must be non-zero as otherwise $R$ would be a field. So by assumption and Example 2.6 (a) it is of the form $P = (t)$ for a prime element $t \in R$. Localizing at $(t)$ again does not change $R$, and so $R = R_{(t)}$ is the localization of the unique factorization domain $R$ (see Example 8.3 (a)) at the ideal $(t)$. By Example 12.4 (c) it is thus a valuation ring with value group $\mathbb{Z}$, which shows (c).

Moreover, every non-zero element $a \in R$ can be written uniquely as $a = c t^n$ for some $n \in \mathbb{N}$ and $c \in R \setminus P$. Then $c$ is a unit by Lemma 12.6 (c) and (d), and hence $(a) = (t^n) = P^n$. Example 12.4 (c) shows that $\nu(a) = n$ in this case, proving the additional statement of the proposition.

(c) $\Rightarrow$ (a): It is clear that $R$ cannot be a field, since otherwise its valuation group would be $(\operatorname{Quot}R)^{+}/R^{+} = \{1\}$ by Construction 12.7.

Now let $I \trianglelefteq R$ be a non-zero ideal. As the value group of $R$ is $\mathbb{Z}$, there is a non-zero element $a \in I$ with minimal valuation $\nu(a)$. But then $I = (a)$, since for every element $b \in I$ we have $\nu(b) \geq \nu(a)$, and thus $b \in (a)$ by Lemma 12.6 (b).

**Proposition 12.14 (Equivalent conditions for discrete valuation rings).** For a Noetherian local ring $R$ the following statements are equivalent:

(a) $R$ is a discrete valuation ring.
(b) $R$ is a principal ideal domain, but not a field.
(c) $R$ is a 1-dimensional unique factorization domain.
(d) $R$ is a 1-dimensional normal domain.
(e) $R$ is a 1-dimensional regular ring.

**Proof.**

(a) $\Rightarrow$ (b) follows from Proposition 12.13.
(b) $\Rightarrow$ (c) holds by Example 8.3 (a) and Example 11.3 (c).
(c) $\Rightarrow$ (d) is Example 9.10.

---

Andreas Gathmann

(d) $\Rightarrow$ (e): As $R$ is a local 1-dimensional domain, its maximal ideal $P$ and the zero ideal are the only prime ideals in $R$. So if we choose $a \in P \setminus \{0\}$ then $\sqrt{(a)} = P$ by Lemma 2.21, and thus $P^n \subset (a)$ for some $n \in \mathbb{N}$ by Exercise 7.22 (b). Let us choose $n$ minimal. Note that certainly $n &gt; 0$ since otherwise $a$ would have to be a unit. So $P^{n-1} \not\subset (a)$, and we can pick $b \in P^{n-1} \setminus (a)$.

We set $t = \frac{a}{b} \in \operatorname{Quot} R$ and claim that $t \in R$ and $P = (t)$. To see this, note first that

$$
\frac {1}{t} P = \frac {b}{a} P \subset \frac {1}{a} P ^ {n} \subset \frac {1}{a} (a) \subset R,
$$

so $\frac{1}{t} P$ is an ideal in $R$. If it was contained in the maximal ideal $P$, the $R$-module homomorphism $P \to P$, $x \mapsto \frac{1}{t} x$ would satisfy a monic polynomial equation with coefficients in $R$ by Proposition 3.25. Thus $\frac{1}{t} \in \operatorname{Quot} R$ would be integral over $R$. As $R$ is assumed to be normal, this would imply $\frac{1}{t} \in R$ and hence $b = \frac{1}{t} a \in (a)$, in contradiction to our choice of $b$. So the ideal $\frac{1}{t} P$ is not contained in the unique maximal ideal $P$, which means that $\frac{1}{t} P = R$. In other words we have $P = (t)$, so $P$ is principal and hence $R$ is a regular 1-dimensional ring by Lemma 11.36 (a).

(e) $\Rightarrow$ (a): By Lemma 12.1 we know that the maximal ideal of $R$ is generated by one element $t$, and that every $a \in R \setminus \{0\}$ can be written as a unit times $t^n$ for some $n \in \mathbb{N}$. Consequently, every element $a \in \operatorname{Quot} R \setminus \{0\}$ can be written as a unit times $t^n$ for $n \in \mathbb{Z}$. But then $a \in R$ (if $n \geq 0$) or $a^{-1} \in R$ (if $n \leq 0$), and thus $R$ is a valuation ring. It is discrete by Proposition 12.13 as it is Noetherian by assumption, and not a field since $\dim R = 1$.

---

## Remark 12.15.

(a) By Proposition 12.14, the 1-dimensional regular local rings considered in Lemma 12.1 are exactly the discrete valuation rings. Moreover, the additional statement in Proposition 12.13 shows that the “valuation” constructed in Lemma 12.1 is in fact the valuation in the sense of Definition 12.3 and Proposition 12.8.

(b) In this course we have met two conditions on rings that correspond geometrically to some sort of “non-singularity” statement: normality in Example 9.11, and regularity in Example 11.37. Proposition 12.14 states that these two conditions agree in the 1-dimensional case. One can show however that this is no longer true in higher dimensions: regular local rings are always normal, but the converse is in general false.

---

## Example 12.16.

(a) As in Remark 12.2, every ring of local functions at a smooth point on a curve is a 1-dimensional regular local ring, and thus by Proposition 12.14 a discrete valuation ring. By Remark 12.15 (a) its valuation can be interpreted as orders of vanishing as in Remark 12.2.

(b) The power series ring $L[[t]]$ over a field $L$ is a discrete valuation ring by Proposition 12.13, since it is a valuation ring with valuation group $\mathbb{Z}$ by Example 12.4 (d).

Our results above allow to give a very easy description of the ideals in a discrete valuation ring.

---

**Corollary 12.17** (Ideals in a discrete valuation ring). Let $R$ be a discrete valuation ring with unique maximal ideal $P$. Then the non-zero ideals of $R$ are exactly the powers $P^n$ for $n \in \mathbb{N}$. They form a strictly decreasing chain

$$
R = P ^ {0} \supseteq P ^ {1} \supseteq P ^ {2} \supseteq \dots .
$$

**Proof.** By Proposition 12.13, any non-zero ideal in $R$ is principal and of the form $P^n$ for some $n \in \mathbb{N}$. Moreover, these powers form a strict chain of ideals since $P^n = P^{n+1} = P \cdot P^n$ for some $n$ would imply $P^n = 0$ by Nakayama’s Lemma as in Example 6.16 (a), and thus the contradiction $P = 0$. ☐

Finally, the valuation in a discrete valuation ring can also be expressed in terms of the length of modules introduced in Definition 3.18.

---

12. Valuation Rings

Corollary 12.18 (Valuation and length). Let $R$ be a discrete valuation ring, and let $a \in R \setminus \{0\}$. Then $\nu(a) = l_R(R / (a))$.

Proof. By Proposition 12.13 (b) the maximal ideal $P$ of $R$ can be generated by one element $t$. Moreover, Proposition 12.13 shows that $(a) = P^{\nu(a)} = (t^{\nu(a)})$. Now

$$
0 = \left(t ^ {\nu (a)}\right) / (a) \subseteq \left(t ^ {\nu (a) - 1}\right) / (a) \subsetneq \dots \subsetneq \left(t ^ {0}\right) / (a) = R / (a) \tag {*}
$$

is a chain of submodules of $R / (a)$ with successive quotients $(t^{i - 1}) / (t^i)$ for $i = 1,\ldots ,\nu (a)$ by Proposition 3.10 (b). But

$$
R / (t) \rightarrow (t ^ {i - 1}) / (t ^ {i}), \bar {c} \mapsto \overline {{c t ^ {i - 1}}}
$$

is an isomorphism for all $i$, and thus $(*)$ is a composition series for $R / (a)$ as an $R$-module. Hence we conclude that $l_{R}(R / (a)) = \nu(a)$.