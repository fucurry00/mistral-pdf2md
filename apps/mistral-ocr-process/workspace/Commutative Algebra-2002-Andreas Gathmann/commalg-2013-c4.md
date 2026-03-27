## 4 Exact Sequences

In the last chapter we have studied many structures related to modules, such as submodules, quotient modules, and module homomorphisms together with their images and kernels. We now want to introduce a very useful piece of notation that can be used to deal with all these concepts in a unified way: the so-called *exact sequences*. In many cases they provide an easy and almost “graphical” way to express and prove statements that are in principle elementary, but tedious to write down without this language due to the sheer number of spaces, morphisms, or relations involved.

###### Definition 4.1 (Exact sequences).

Let $R$ be a ring, and let $n\in\mathbb{N}_{\geq 3}$. A sequence

$M_{1}\xrightarrow{\varphi_{1}}M_{2}\xrightarrow{\varphi_{2}}\cdots\xrightarrow{\varphi_{n-1}}M_{n}$

of $R$-modules $M_{1},\ldots,M_{n}$ and $R$-module homomorphisms $\varphi_{i}:M_{i}\to M_{i+1}$ for $i=1,\ldots,n-1$ is called exact at position $i\in\{2,\ldots,n-1\}$ if $\operatorname{im}\varphi_{i-1}=\ker\varphi_{i}$. It is called exact if it is exact at every position $i\in\{2,\ldots,n-1\}$.

In such sequences, we will often not label an arrow with its morphism if it is clear from the context what the morphism is. In particular, this is the case if the source or target of the map is the zero module, so that the map is necessarily the zero morphism.

###### Example 4.2 (Exact sequences with few modules).

1. A sequence $0\longrightarrow M\xrightarrow{\varphi}N$ is exact if and only if $\ker\varphi=0$, i. e. if and only if $\varphi$ is injective.

A sequence $M\xrightarrow{\varphi}N\longrightarrow 0$ is exact if and only if $\operatorname{im}\varphi=N$, i. e. if and only if $\varphi$ is surjective.
2. The sequence $0\longrightarrow M\longrightarrow 0$ is exact if and only if $M=0$.

By (a), the sequence $0\longrightarrow M\xrightarrow{\varphi}N\longrightarrow 0$ is exact if and only if $\varphi$ is injective and surjective, i. e. if and only if $\varphi$ is an isomorphism.

###### Example 4.3 (Short exact sequences).

By Example 4.2, the first interesting case of an exact sequence occurs if it has at least three non-zero terms. Therefore, an exact sequence of the form

$0\longrightarrow M_{1}\xrightarrow{\varphi}M_{2}\xrightarrow{\psi}M_{3}\longrightarrow 0$ $$ $$

is called a short exact sequence. There are two main sources for such short exact sequences:

1. For any $R$-module homomorphism $\psi:M\to N$ the sequence

$0\longrightarrow\ker\psi\longrightarrow M\xrightarrow{\psi}\operatorname{im}\psi\longrightarrow 0$

is exact, where the first map is the inclusion of $\ker\psi$ in $M$.
2. For any submodule $N$ of an $R$-module $M$ the sequence

$0\longrightarrow N\longrightarrow M\longrightarrow M/N\longrightarrow 0$

is exact, where the first map is again the inclusion, and the second the quotient map.

In fact, up to isomorphisms every short exact sequence is of these forms: in a short exact sequence as in $(*)$ the second map $\psi$ is surjective, and thus $\operatorname{im}\psi=M_{3}$. Moreover, $\ker\psi=\operatorname{im}\varphi=\varphi(M_{1})\cong M_{1}$, where the last isomorphism follows from the injectivity of $\varphi$. So the given sequence is of the type as in (a). If we set $N=\ker\psi\leq M_{2}$ and use the homomorphism theorem $\operatorname{im}\psi\cong M_{2}/\ker\psi=M_{2}/N$ of Proposition 3.10 (a), we can also regard it as a sequence as in (b).

A nice feature of exact sequences is that there are simple rules to create new sequences from old ones. The simplest way to do this is to split and glue exact sequences as follows.

---

###### Lemma 4.4 (Splitting and gluing exact sequences).

1. (Splitting) If

$M_{1}\xrightarrow{\varphi_{1}}M_{2}\xrightarrow{\varphi_{2}}M_{3}\xrightarrow{\varphi_{3}}M_{4}$ (A)

is an exact sequence of $R$-modules, the two sequences

$M_{1}\xrightarrow{\varphi_{1}}M_{2}\xrightarrow{\varphi_{2}}N\longrightarrow 0\qquad\text{and}\qquad 0\longrightarrow N\longrightarrow M_{3}\xrightarrow{\varphi_{3}}M_{4}$ (B)

are also exact, where $N=\operatorname{im}\varphi_{2}=\ker\varphi_{3}$, and the middle map in the second sequence is the inclusion of $\ker\varphi_{3}$ in $M_{3}$.
2. (Gluing) Conversely, if

$M_{1}\xrightarrow{\varphi_{1}}M_{2}\xrightarrow{\varphi_{2}}N\longrightarrow 0\qquad\text{and}\qquad 0\longrightarrow N\longrightarrow M_{3}\xrightarrow{\varphi_{3}}M_{4}$ (B)

are two exact sequences, with $N\leq M_{3}$ a submodule and the middle map in the second sequence the inclusion, the sequence

$M_{1}\xrightarrow{\varphi_{1}}M_{2}\xrightarrow{\varphi_{2}}M_{3}\xrightarrow{\varphi_{3}}M_{4}$ (A)

is also exact.

###### Proof.

1. The first sequence of (B) is exact at $M_{2}$ since $\operatorname{im}\varphi_{1}=\ker\varphi_{2}$, and exact at $N$ as $N=\operatorname{im}\varphi_{2}$. The second sequence of (B) is exact $N$ as the middle map is an inclusion, and exact at $M_{3}$ since $N=\ker\varphi_{3}$.
2. The sequence of (A) is exact at $M_{2}$ since $\operatorname{im}\varphi_{1}=\ker\varphi_{2}$. Moreover, in (B) exactness of the first sequence at $N$ and of the second sequence at $M_{3}$ means that $\operatorname{im}\varphi_{2}=N=\ker\varphi_{3}$, which implies that (A) is exact at $M_{3}$. ∎

###### Remark 4.5 (Splitting an exact sequence into short ones).

With Lemma 4.4 (a) every exact sequence

$0\longrightarrow M_{1}\xrightarrow{\varphi_{1}}M_{2}\xrightarrow{\varphi_{2}}\;\;\cdots\;\;\xrightarrow{\varphi_{n-1}}M_{n}\longrightarrow 0$ (*)

(for simplicity with zero modules at the end) can be split up into short exact sequences

$0\longrightarrow\ker\varphi_{i}\longrightarrow M_{i}\xrightarrow{\varphi_{i}}\operatorname{im}\varphi_{i}\longrightarrow 0$

for $i=2,\ldots,n-1$ as in Example 4.3 (a), where $M_{1}=\ker\varphi_{2}$ and $M_{n}=\operatorname{im}\varphi_{n-1}$. Conversely, such short exact sequences with $M_{1}=\ker\varphi_{2}$, $M_{n}=\operatorname{im}\varphi_{n-1}$, and $\operatorname{im}\varphi_{i-1}=\ker\varphi_{i}$ for $i=3,\ldots,n-1$ can be glued back together by Lemma 4.4 (b) to the long exact sequence $(*)$.

###### Example 4.6 (Exact sequence of a homomorphism).

Let $\varphi:M\to N$ be a homomorphism of $R$-modules. By Example 4.3 (a) and (b) there are then short exact sequences

$0\longrightarrow\ker\varphi\longrightarrow M\xrightarrow{\varphi}\operatorname{im}\varphi\longrightarrow 0\qquad\text{and}\qquad 0\longrightarrow\operatorname{im}\varphi\longrightarrow N\longrightarrow N/\operatorname{im}\varphi\longrightarrow 0,$

and hence we get a glued exact sequence

$0\longrightarrow\ker\varphi\longrightarrow M\xrightarrow{\varphi}N\longrightarrow N/\operatorname{im}\varphi\longrightarrow 0$

by Lemma 4.4 (b). So any homomorphism can be completed both to the left and to the right to an exact sequence with zero modules at the ends. Of course, the exactness of this sequence could also be checked directly, without using Lemma 4.4 (b).

There is another much more subtle way to construct new exact sequences from old ones. This time, instead of gluing two sequences such that the ending module of the first sequence is the starting module of the second, we consider two short exact sequences such that one of them can be mapped to the other by a sequence of homomorphisms.

---

4. Exact Sequences

Lemma 4.7 (Snake Lemma). Let

![img-0.jpeg](images/img-0.jpeg)

be a commutative diagram of  $R$ -modules with exact rows. Then there is a long exact sequence

$\ker \alpha \longrightarrow \ker \beta \longrightarrow \ker \gamma \longrightarrow M' / \operatorname{im} \alpha \longrightarrow N' / \operatorname{im} \beta \longrightarrow P' / \operatorname{im} \gamma.$  (*)

Moreover:

- if  $\varphi$  is injective, then so is the first map in the sequence  $(\ast)$ ;
- if  $\psi'$  is surjective, then so is the last map in the sequence  $(\ast)$ .

Remark 4.8. There is a nice graphical way to express the assertion of Lemma 4.7 as follows. First of all, if we complete the vertical homomorphisms  $\alpha$ ,  $\beta$ , and  $\gamma$  to exact sequences as in Example 4.6 we obtain the solid arrows in the following diagram, in which all columns are exact.

![img-1.jpeg](images/img-1.jpeg)

The statement of the lemma is now the existence of an exact sequence indicated by the dashed arrows above. In particular, the probably unexpected homomorphism from  $\ker \gamma$  to  $M' / \operatorname{im} \alpha$  is the reason for the name "Snake Lemma". The dotted arrows represent the additional statements of Lemma 4.7: one can read the diagram with or without both dotted arrows on the left, and with or without both dotted arrows on the right.

Proof of Lemma 4.7. In the following proof, we will denote elements of  $M, N, P, M', N', P'$  by the corresponding lower case letters.

First of all let us construct the homomorphisms in the sequence

$\ker \alpha \xrightarrow{\bar{\varphi}} \ker \beta \xrightarrow{\bar{\psi}} \ker \gamma \xrightarrow{\delta} M' / \operatorname{im} \alpha \xrightarrow{\bar{\varphi}'} N' / \operatorname{im} \beta \xrightarrow{\bar{\psi}'} P' / \operatorname{im} \gamma.$  (*)

(a) The first two maps. Let  $\bar{\varphi}:\ker \alpha \to \ker \beta$ ,  $m\mapsto \varphi (m)$  be the restriction of  $\varphi$  to  $\ker \alpha$ . Note that its image lies indeed in  $\ker \beta$ : for  $m\in \ker \alpha$  we have  $\beta (\varphi (m)) = \varphi^{\prime}(\alpha (m)) = 0$  since the given diagram is commutative. In the same way, let  $\bar{\psi}$  be the restriction of  $\psi$  to  $\ker \beta$ .
(b) The last two maps. We have  $\varphi'(\operatorname{im}\alpha) \subset \operatorname{im}\beta$ , since  $\varphi'(\alpha(m)) = \beta(\varphi(m))$ . Hence we get a well-defined map  $\bar{\varphi}': M' / \operatorname{im}\alpha \to N' / \operatorname{im}\beta$ ,  $\overline{m'} \mapsto \overline{\varphi'(m')}$ . Similarly, set  $\bar{\psi}'(\overline{n'}) := \overline{\psi'(n')}$ .
(c) The middle map  $\delta$ . The existence of this map from a submodule of  $P$  to a quotient module of  $M'$  — it is usually called the connecting homomorphism — is the central part of this lemma.

---

Andreas Gathmann

Schematically, its idea is shown by the dashed arrow in the picture below: take an inverse image under  $\psi$ , then the image under  $\beta$ , and then again an inverse image under  $\varphi'$ .

![img-2.jpeg](images/img-2.jpeg)

More precisely, let  $p \in \ker \gamma \leq P$ . As  $\psi$  is surjective there is an element  $n \in N$  with  $\psi(n) = p$ . Set  $n' = \beta(n)$ . Then  $\psi'(n') = \psi'(\beta(n)) = \gamma(\psi(n)) = \gamma(p) = 0$ , so that  $n' \in \ker \psi' = \operatorname{im} \varphi'$ . Hence there is an element  $m' \in M'$  with  $\varphi'(m') = n'$ . We want to set  $\delta(p) := \overline{m'} \in M' / \operatorname{im} \alpha$ .

We have to check that this is well-defined, i.e. does not depend on the two choices of inverse images. Note that the choice of  $m'$  was clearly unique since  $\varphi'$  is injective. Now let us suppose that we pick another inverse image  $\tilde{n} \in N$  of  $p$  in the first step, with image  $\tilde{n}' = \beta(\tilde{n})$  under  $\beta$  and inverse image  $\tilde{m}'$  under  $\varphi'$ . Then  $\psi(\tilde{n} - n) = 0$ , so  $\tilde{n} - n \in \ker \psi = \operatorname{im} \varphi$ , i.e.  $\tilde{n} - n = \varphi(m)$  for some  $m \in M$ . It follows that

$$
\varphi^ {\prime} \left(\tilde {m} ^ {\prime} - m ^ {\prime}\right) = \tilde {n} ^ {\prime} - n ^ {\prime} = \beta (\tilde {n} - n) = \beta (\varphi (m)) = \varphi^ {\prime} (\alpha (m)),
$$

and hence  $\tilde{m}^{\prime} - m^{\prime} = \alpha (m)$  since  $\varphi^\prime$  is injective. Consequently,  $\tilde{m}^{\prime}$  and  $m^{\prime}$  define the same class in  $M^{\prime} / \mathrm{im}\alpha$ , and thus  $\delta$  is in fact well-defined.

As all these maps are clearly homomorphisms, it only remains to prove that the sequence  $(\ast)$  is exact. The technique to do this is the same as in the construction of the connecting homomorphism  $\delta$  above: just following elements through the given commutative diagram, a so-called diagram chase. This is purely automatic and does not require any special ideas. The proof is therefore probably not very interesting, but we will give it here nevertheless for the sake of completeness.

- Exactness at  $\ker \beta$ . Clearly,  $\tilde{\psi}(\tilde{\varphi}(m)) = \psi(\varphi(m)) = 0$  for  $m \in \ker \alpha$ , and so  $\operatorname{im} \tilde{\varphi} \subset \ker \tilde{\psi}$ . Conversely, if  $n \in \ker \tilde{\psi} \leq N$  then  $n \in \ker \psi = \operatorname{im} \varphi$ , so  $n = \varphi(m)$  for some  $m \in M$ . This element satisfies  $\varphi'(\alpha(m)) = \beta(\varphi(m)) = \beta(n) = 0$  since  $n \in \ker \beta$ . By the injectivity of  $\varphi'$  this means that  $m$  lies in  $\ker \alpha$ , which is the source of  $\tilde{\varphi}$ . Hence  $n \in \operatorname{im} \tilde{\varphi}$ .
- Exactness at  $\ker \gamma$ . If  $p \in \operatorname{im} \tilde{\psi}$  then  $p = \psi(n)$  for some  $n \in \ker \beta$ . In the construction (c) of  $\delta$  above, we can then choose this element  $n$  as inverse image for  $p$ , so we get  $n' = \beta(n) = 0$  and thus  $\delta(p) = 0$ , i.e.  $p \in \ker \delta$ . Conversely, if  $p \in \ker \delta$  then  $m' = \alpha(m)$  for some  $m \in M$  in the construction of  $\delta$  in (c). Continuing in the notation of (c), we then have  $\beta(n) = n' = \varphi'(m') = \varphi'(\alpha(m)) = \beta(\varphi(m))$ . Hence,  $n - \varphi(m) \in \ker \beta$  with  $\tilde{\psi}(n - \varphi(m)) = \psi(n) - \psi(\varphi(m)) = \psi(n) = p$ , and thus  $p \in \operatorname{im} \tilde{\psi}$ .
- Exactness at  $M' / \operatorname{im} \alpha$ . If  $\overline{m'} \in \operatorname{im} \delta$ , then  $\tilde{\varphi}'(\overline{m'}) = \overline{n'} = 0$  in the notation of (c) since  $n' = \beta(n) \in \operatorname{im} \beta$ . Conversely, if  $\overline{m'} \in \ker \tilde{\varphi}'$ , then  $n' := \varphi'(m') \in \operatorname{im} \beta$ , so  $n' = \beta(n)$  for some  $n \in N$ . Then  $p := \psi(n)$  satisfies  $\gamma(p) = \gamma(\psi(n)) = \psi'(\beta(n)) = \psi'(n') = \psi'(\varphi'(m')) = 0$  and yields the given element  $\overline{m'}$  as image under  $\delta$ , so  $\overline{m'} \in \operatorname{im} \delta$ .
- Exactness at  $N' / \operatorname{im} \beta$ . If  $\overline{n'} \in \operatorname{im} \tilde{\varphi}'$  then  $\overline{n'} = \tilde{\varphi}'(\overline{m'})$  for some  $m' \in M'$ , and thus  $\tilde{\psi}'(\overline{n'}) = \overline{\psi'(\varphi'(m'))} = 0$ . Conversely, if  $\overline{n'} \in \ker \tilde{\psi}'$  then  $\psi'(n') \in \operatorname{im} \gamma$ , so  $\psi'(n') = \gamma(p)$  for some  $p \in P$ . As  $\psi$  is surjective, we can choose  $n \in N$  with  $\psi(n) = p$ . Then  $\psi'(n' - \beta(n)) = \gamma(p) - \gamma(\psi(n)) = 0$ , and hence  $n' - \beta(n) \in \ker \psi' = \operatorname{im} \varphi'$ . We therefore find an element  $m' \in M'$  with  $\varphi'(m') = n' - \beta(n)$ , and thus  $\tilde{\varphi}'(\overline{m'}) = \overline{n'} - \overline{\beta(n)} = \overline{n'}$ .
- Injectivity of  $\tilde{\varphi}$ . As  $\tilde{\varphi}$  is just a restriction of  $\varphi$ , it is clear that  $\tilde{\varphi}$  is injective if  $\varphi$  is.
- Surjectivity of  $\tilde{\psi}'$ . If  $\psi'$  is surjective then for any  $p' \in P'$  there is an element  $n' \in N'$  with  $\psi'(n') = p'$ , and thus  $\tilde{\psi}'(\overline{n'}) = \overline{p'}$ .

Exercise 4.9 (Hom  $(\cdot ,N)$  is left exact).

(a) Prove that a sequence

$$
M _ {1} \xrightarrow {\varphi_ {1}} M _ {2} \xrightarrow {\varphi_ {2}} M _ {3} \longrightarrow 0
$$

---

of $R$-modules is exact if and only if the sequence

$0\longrightarrow\operatorname{Hom}(M_{3},N)\xrightarrow{\varphi_{1}^{*}}\operatorname{Hom}(M_{2},N)\xrightarrow{\varphi_{1}^{*}}\operatorname{Hom}(M_{1},N)$ $$ $$

is exact for every $R$-module $N$, where $\varphi_{i}^{*}(\varphi)=\varphi\circ\varphi_{i}$ for $i\in\{1,2\}$.
2. Show that the statement of (a) is not true with an additional $0$ at the left and right end, respectively — i. e. that $\varphi_{1}^{*}$ need not be surjective if $\varphi_{1}$ is injective. We say that the operation $\operatorname{Hom}(\cdot,N)$ is *left exact* (because the sequence $(*)$ is exact with $0$ at the left), but not exact.

After having seen several ways to construct exact sequences, let us now study what sort of information we can get out of them. The general philosophy is that an exact sequence with zero modules at the end is “almost enough” to determine any of its modules in terms of the others in the sequence. As a first statement in this direction, let us show that in order to compute the length of a module it is enough to have the module somewhere in an exact sequence in which the lengths of the other modules are known — at least if all involved lengths are finite.

###### Corollary 4.10.

Let

$0\longrightarrow M_{1}\xrightarrow{\varphi_{1}}M_{2}\xrightarrow{\varphi_{2}}\quad\cdots\xrightarrow{\varphi_{n-1}}M_{n}\longrightarrow 0$

be an exact sequence of $R$-modules of finite length. Then $\sum_{i=1}^{n}(-1)^{i}l(M_{i})=0$.

###### Proof.

By Corollary 3.23 (b) applied to all morphisms $\varphi_{1},\ldots,\varphi_{n-1}$ and an index shift we get

$\sum_{i=1}^{n-1}(-1)^{i}l(M_{i})$ $=\sum_{i=1}^{n-1}(-1)^{i}\left(l(\ker\varphi_{i})+l(\operatorname{im}\varphi_{i})\right)$
$=-l(\ker\varphi_{1})+(-1)^{n-1}l(\operatorname{im}\varphi_{n-1})+\sum_{i=2}^{n-1}(-1)^{i}\left(l(\ker\varphi_{i})-l(\operatorname{im}\varphi_{i-1})\right).$

But $l(\ker\varphi_{1})=0$ since $\varphi_{1}$ is injective, $l(\operatorname{im}\varphi_{n-1})=l(M_{n})$ since $\varphi_{n-1}$ is surjective, and $l(\ker\varphi_{i})=l(\operatorname{im}\varphi_{i-1})$ for all $i=2,\ldots,n-1$ by the exactness of the sequence. Plugging this into the above formula, the result follows. ∎

Of course, knowing the length of a module does not mean that one knows the module up to isomorphism (as we have seen e. g. in Example 3.21). So let us now address the question to what extent a module in an exact sequence can be completely recovered from the other parts of the sequence. For simplicity, let us restrict to short exact sequences.

###### Example 4.11 (Recovering modules from an exact sequence).

Consider an exact sequence

$0\longrightarrow M\xrightarrow{\varphi}N\xrightarrow{\psi}P\longrightarrow 0$

of $R$-modules, and let us ask whether we can determine one of the three modules if we know the rest of the sequence.

Of course, if we know $M$ and $N$ together with the map $\varphi$ then $P$ is uniquely determined by this data: as we must have $\operatorname{im}\psi=P$ and $\ker\psi=\operatorname{im}\varphi$, the homomorphism theorem of Proposition 3.10 (a) tells us that $P\cong N/\ker\psi=N/\operatorname{im}\varphi$. In the same way, $M$ is uniquely determined if we know $N$ and $P$ together with the map $\psi$, since by the injectivity of $\varphi$ we have $M\cong\operatorname{im}\varphi=\ker\psi$.

The most interesting question is thus if we can recover the middle term $N$ if we know $M$ and $P$ (but none of the maps). The following two examples show that this is in general not possible.

1. In any case, a possible way to obtain a short exact sequence from given modules $M$ at the left and $P$ at the right is

$0\longrightarrow M\xrightarrow{\varphi}M\oplus P\xrightarrow{\psi}P\longrightarrow 0,$

where $\varphi$ is the inclusion of $M$ in $M\oplus P$, and $\psi$ the projection of $M\oplus P$ onto $P$.

---

Andreas Gathmann

(b) There is an exact sequence of  $\mathbb{Z}$ -modules

![img-3.jpeg](images/img-3.jpeg)

be a commutative diagram of  $R$ -modules with exact rows. If two of the maps  $\alpha, \beta$ , and  $\gamma$  are isomorphisms, then so is the third.

Proof. By the Snake Lemma 4.7 there is a long exact sequence

![img-4.jpeg](images/img-4.jpeg)

If now e.g.  $\alpha$  and  $\gamma$  are bijective then  $\ker \alpha = \ker \gamma = M' / \operatorname{im} \alpha = P' / \operatorname{im} \gamma = 0$ , and the sequence becomes

![img-5.jpeg](images/img-5.jpeg)

By Example 4.2 (b) this means that  $\ker \beta = N' / \operatorname{im} \beta = 0$ , and so  $\beta$  is bijective as well.

Of course, an analogous argument applies if  $\alpha$  and  $\beta$ , or  $\beta$  and  $\gamma$  are assumed to be bijective.

Remark 4.13. There are various versions of the 5-Lemma in the literature. In fact, looking at the proof above we see that our assumptions could be relaxed: in order to show that  $\beta$  is an isomorphism if  $\alpha$  and  $\gamma$  are, we do not need the additional zero modules on the left and right of the long exact sequence of the Snake Lemma 4.7. So for this case we do not have to require  $\varphi$  to be injective or  $\psi'$  to be surjective — this is only necessary if we want to conclude that  $\alpha$  or  $\gamma$  is an isomorphism, respectively.

More generally, if one wants to show that the middle vertical map is an isomorphism, one can show that it is enough to assume a commutative diagram

![img-6.jpeg](images/img-6.jpeg)

with exact rows in which the zero modules at the left and right ends have been replaced by arbitrary ones, and where now  $\beta_{1},\beta_{2},\beta_{4}$ , and  $\beta_{5}$  are required to be isomorphisms. This version of the lemma is actually the reason for the name "5-Lemma".

Using Corollary 4.12, we can now give easy criteria to check whether a given short exact sequence  $0 \longrightarrow M \longrightarrow N \longrightarrow P \longrightarrow 0$  is of the simple form as in Example 4.11 (a), i.e. whether the middle entry  $N$  is just the direct sum of  $M$  and  $P$ :

Corollary 4.14 (Splitting Lemma). For a short exact sequence

![img-7.jpeg](images/img-7.jpeg)

the following three statements are equivalent:

(a)  $N \cong M \oplus P$ , with  $\varphi$  being the inclusion of  $M$  in the first summand, and  $\psi$  the projection onto the second.

---

4. Exact Sequences

(b)  $\varphi$  has a left-sided inverse, i.e. there is a homomorphism  $\alpha : N \to M$  such that  $\alpha \circ \varphi = \mathrm{id}_M$ .
(c)  $\psi$  has a right-sided inverse, i.e. there is a homomorphism  $\beta : P \to N$  such that  $\psi \circ \beta = \mathrm{id}_P$ . In this case, the sequence is called split exact.

Proof.

(a)  $\Rightarrow$  (b) and (c): Under the assumption (a) we can take  $\alpha$  to be the projection from  $M\oplus P$  onto  $M$ , and for  $\beta$  the inclusion of  $P$  in  $M\oplus P$ .
(b)  $\Rightarrow$  (a): If  $\alpha$  is a left-sided inverse of  $\varphi$ , the diagram

![img-8.jpeg](images/img-8.jpeg)

is commutative with exact rows. As the left and right vertical map are obviously isomorphisms, so is the middle one by Corollary 4.12.

(c)  $\Rightarrow$  (a): If  $\beta$  is a right-sided inverse of  $\psi$ , the diagram

![img-9.jpeg](images/img-9.jpeg)

is commutative with exact rows, where  $(\varphi + \beta)(m,p) \coloneqq \varphi(m) + \beta(p)$ . Again, as the left and right vertical map are isomorphisms, so is the middle one by Corollary 4.12.

Example 4.15. Every short exact sequence

$$
0 \longrightarrow U \xrightarrow {\varphi} V \xrightarrow {\psi} W \longrightarrow 0
$$

of vector spaces over a field  $K$  is split exact: if  $(b_i)_{i\in I}$  is a basis of  $W$  we can pick inverse images  $c_{i}\in \psi^{-1}(b_{i})$  by the surjectivity of  $\psi$ . There is then a (unique) linear map  $\beta :W\to V$  with  $\beta (b_{i}) = c_{i}$  [G2, Corollary 16.27]. Hence  $\psi \circ \beta = \mathrm{id}_W$ , i.e. the above sequence is split exact. So by Corollary 4.14 we conclude that we always have  $V\cong U\oplus W$  in the above sequence.

Exercise 4.16. Let  $I$  and  $J$  be ideals in a ring  $R$ .

(a) Prove that there is an exact sequence of  $R$ -modules (what are the maps?)

$$
0 \longrightarrow I \cap J \longrightarrow I \oplus J \longrightarrow I + J \longrightarrow 0.
$$

(b) Use the Snake Lemma 4.7 to deduce from this an exact sequence

$$
0 \longrightarrow R / (I \cap J) \longrightarrow R / I \oplus R / J \longrightarrow R / (I + J) \longrightarrow 0.
$$

(c) Show by example that the sequences of (a) and (b) are in general not split exact.

Exercise 4.17. Let  $N$  be a submodule of a finitely generated  $R$ -module  $M$ . In Exercise 3.5 (c) you have seen that  $N$  need not be finitely generated in this case.

However, prove now that  $N$  is finitely generated if it is the kernel of a surjective  $R$ -module homomorphism  $\varphi : M \to R^n$  for some  $n \in \mathbb{N}$ .

(Hint: Show and use that the sequence  $0 \longrightarrow N \longrightarrow M \xrightarrow{\varphi} R^n \longrightarrow 0$  is split exact.)