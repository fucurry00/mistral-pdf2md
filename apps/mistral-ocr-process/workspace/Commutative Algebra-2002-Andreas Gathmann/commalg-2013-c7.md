7 Chain Conditions

In the previous chapters we have met several finiteness conditions: an algebra can be finitely generated as in Definition 1.26 (b), a module can also be finitely generated as in Definition 3.3 (b) or have finite length as in Definition 3.18, and in our study of Zorn’s Lemma in Remark 2.13 we discussed whether an increasing chain of ideals in a ring has to stop after finitely many steps. Of course, this can often make a difference: for example, a reduced algebra over a field is the coordinate ring of a variety if and only if it is finitely generated (see Remark 1.31), and the Cayley-Hamilton theorem in Proposition 3.25 together with its corollaries such as Nakayama’s Lemma in Corollary 3.27 only hold for finitely generated modules. So we will now take some time to study such finiteness questions in more detail and see how they are related.

The key idea is to consider chains of submodules in a given module and check whether they have to stop after finitely many terms.

###### Definition 7.1 (Noetherian and Artinian modules).

Let $M$ be an $R$-module.

1. $M$ is called Noetherian if every ascending chain

$M_{0}\subset M_{1}\subset M_{2}\subset\cdots$

of submodules of $M$ becomes stationary, i. e. if for every such chain there is an index $n\in\mathbb{N}$ such that $M_{k}=M_{n}$ for all $k\geq n$. Obviously, this is the same as saying that there is no infinite strictly ascending chain $M_{0}\subsetneq M_{1}\subsetneq M_{2}\subsetneq\cdots$.
2. Similarly, $M$ is called Artinian if every descending chain

$M_{0}\supset M_{1}\supset M_{2}\supset\cdots$

of submodules becomes stationary. Again, this is equivalent to requiring that there is no infinite strictly descending chain $M_{0}\supsetneq M_{1}\supsetneq M_{2}\supsetneq\cdots$.

The conditions of (a) and (b) are often referred to as the ascending and descending chain condition, respectively. The ring $R$ itself is called Noetherian or Artinian if it has this property as an $R$-module; the submodules above are then just ideals of $R$ by Example 3.4 (a).

###### Example 7.2.

1. Any field $K$ is trivially Noetherian and Artinian as it has only the trivial ideals $(0)$ and $K$. More generally, a $K$-vector space $V$ is Noetherian if and only if it is Artinian if and only if it is finite-dimensional (i. e. finitely generated):

- If $V$ is finite-dimensional, there can only be finite strictly ascending or descending chains of vector subspaces of $V$ since the dimension has to be strictly increasing or decreasing in such a chain, respectively.
- If $V$ is infinite-dimensional, we can obviously form a chain $M_{0}\subsetneq M_{1}\subsetneq M_{2}\subsetneq\cdots$ with $\dim_{K}M_{n}=n$ for all $n\in\mathbb{N}$: set $M_{0}=0$, and $M_{n+1}=M_{n}+\langle v_{n+1}\rangle$ with $v_{n+1}\notin M_{n}$ for all $n\in\mathbb{N}$. Similarly, we can also find an infinite descending chain $M_{0}\supsetneq M_{1}\supsetneq M_{2}\supsetneq\cdots$ of infinite-dimensional subspaces of $V$ with $\dim_{K}(M/M_{n})=n$ for all $n$: let $M_{0}=M$, and $M_{n+1}=M_{n}\cap\ker\varphi_{n+1}$ for some linear map $\varphi_{n+1}:V\to K$ that is not identically zero on $M_{n}$. Then $M/M_{n}\cong\left(M/M_{n+1}\right)/\left(M_{n}/M_{n+1}\right)$ by Proposition 3.10 (b), and so $\dim M_{n}/M_{n+1}=1$ implies $\dim M/M_{n}=n$ for all $n$ by induction.
2. The ring $\mathbb{Z}$ is Noetherian: if we had a strictly increasing chain of ideals $I_{0}\subsetneq I_{1}\subsetneq I_{2}\subsetneq\cdots$ in $\mathbb{Z}$, then certainly $I_{1}\neq 0$, and thus $I_{1}=(a)$ for some non-zero $a\in\mathbb{Z}$. But there are only finitely many ideals in $\mathbb{Z}$ that contain $I_{1}$ since they correspond to ideals of the finite ring $\mathbb{Z}/(a)$ by Lemma 1.21. Hence the chain cannot be infinitely long, and thus $\mathbb{Z}$ is Noetherian.

---

On the other hand, $\mathbb{Z}$ is not Artinian, since there is an infinite decreasing chain of ideals

$\mathbb{Z}\supsetneq 2\mathbb{Z}\supsetneq 4\mathbb{Z}\supsetneq 8\mathbb{Z}\supsetneq\cdots.$

Let $R=\bigcup_{n\in\mathbb{N}}\mathbb{R}[x_{0},x_{1},\ldots,x_{n}]$ be the polynomial ring over $\mathbb{R}$ in infinitely many variables. Then $R$ is neither Noetherian nor Artinian, since there are infinite chains of ideals

$(x_{0})\subsetneq(x_{0},x_{1})\subsetneq(x_{0},x_{1},x_{2})\subsetneq\cdots\qquad\text{and}\qquad(x_{0})\supsetneq(x_{0}^{2})\supsetneq(x_{0}^{3})\supsetneq\cdots.$

###### Exercise 7.3.

For a prime number $p\in\mathbb{N}$, consider $M=\mathbb{Z}_{p}/\mathbb{Z}$ as a $\mathbb{Z}$-module (i. e. as an Abelian group), where $\mathbb{Z}_{p}\subset\mathbb{Q}$ denotes the localization of $\mathbb{Z}$ at the element $p$ as in Example 6.5 (c). Show that:

1. Every proper submodule of $M$ is of the form $\left\langle\frac{1}{p^{n}}\right\rangle$.
2. $M$ is Artinian, but not Noetherian.

As you might expect, we will see in the following that Noetherian and Artinian modules have many similar properties that can be obtained from one another by just reversing all inclusions — as e. g. in the first two parts of the following lemma. However, there are also aspects in which the two concepts of Noetherian and Artinian modules are fundamentally different (in particular when we specialize to rings in the second half of this chapter). A first example of this is part (c) of the following equivalent reformulation of our chain conditions, which asserts that a module is Noetherian if and only if each of its submodules is finitely generated. There is no corresponding condition for Artinian modules, and in fact this is one of the main reasons why in practice Noetherian modules are much more important than Artinian ones.

###### Lemma 7.4 (Equivalent conditions for Noetherian and Artinian modules).

Let $M$ be an $R$-module.

1. $M$ is Noetherian if and only if every non-empty family of submodules of $M$ has a maximal element.
2. $M$ is Artinian if and only if every non-empty family of submodules of $M$ has a minimal element.
3. $M$ is Noetherian if and only if every submodule of $M$ is finitely generated.

###### Proof.

1. “$\Rightarrow$” Let $A$ be a non-empty family of submodules of $M$. If there was no maximal element of $A$, we could choose recursively a chain $M_{0}\subsetneq M_{1}\subsetneq M_{2}\subsetneq\cdots$ from $A$, contradicting the assumption that $M$ is Noetherian.

“$\Leftarrow$” Consider a chain $M_{0}\subset M_{1}\subset M_{2}\subset\cdots$ of submodules of $M$. By assumption, the set $A=\{M_{n}:n\in\mathbb{N}\}$ has a maximal element $M_{n}$. But then $M_{k}=M_{n}$ for all $k\geq n$, hence $M$ is Noetherian.
2. is proven in the same way as (a), just reversing all inclusions.
3. “$\Rightarrow$” Assume that we have a submodule $N\leq M$ that is not finitely generated. Then we can recursively pick $m_{0}\in N$ and $m_{n+1}\in N\backslash\langle m_{0},\ldots,m_{n}\rangle$ for $n\in\mathbb{N}$, and obtain a chain $M_{0}\subsetneq M_{1}\subsetneq M_{2}\subsetneq\cdots$ in $M$. This is a contradiction since $M$ is Noetherian.

“$\Leftarrow$” Let $M_{0}\subset M_{1}\subset M_{2}\subset\cdots$ be a chain of submodules of $M$. Then $N=\bigcup_{n\in\mathbb{N}}M_{n}$ is also a submodule of $M$ (which can be shown in the same way as in the proof of Corollary 2.17). So by assumption $N$ can be generated by finitely many elements $m_{1},\ldots,m_{r}\in N$. Now by definition of $N$ we must have $m_{i}\in M_{n_{i}}$ for all $i=1,\ldots,r$ and some $n_{1},\ldots,n_{r}\in\mathbb{N}$. With $n=\max\{n_{1},\ldots,n_{r}\}$ we then have $m_{1},\ldots,m_{r}\in M_{n}$. Hence $N=\langle m_{1},\ldots,m_{r}\rangle\leq M_{n}\leq N$, which implies $M_{k}=M_{n}=N$ for all $k\geq n$. ∎

###### Example 7.5.

1. Any principal ideal domain $R$ (as e. g. $R=\mathbb{Z}$ in Example 7.2 (b)) is Noetherian by Lemma 7.4 (c), since every ideal in $R$ is even generated by one element.

---

7. Chain Conditions

(b) Note that the  $\mathbb{R}$ -algebra  $\mathbb{R}[x]$  is a Noetherian ring by (a), but not a Noetherian  $\mathbb{R}$ -module by Example 7.2 (a) (as it is an infinite-dimensional  $\mathbb{R}$ -vector space). So when applying the chain conditions to algebras we have to be very careful whether we talk about Noetherian resp. Artinian rings or modules, as this might make a difference! There is one important case however in which there is no such difference:
(c) Let  $I$  be an ideal in a ring  $R$ , and let  $M$  be an  $R$ -module. Then  $M / IM$  is both an  $R / I$ -module and an  $R$ -module, and by definition a subset of  $M / IM$  is an  $R / I$ -submodule if and only if it is an  $R$ -submodule. So we conclude by Definition 7.1 that  $M / IM$  is Noetherian resp. Artinian as an  $R / I$ -module if and only if it has this property as an  $R$ -module.

In particular, applying this result to  $M = R$  we see that the  $R$ -algebra  $R / I$  is Noetherian resp. Artinian as a ring if and only if it has this property as an  $R$ -module.

Remark 7.6 (Maximal ideals in Noetherian rings). Let  $I$  be an ideal in a Noetherian ring  $R$  with  $I \neq R$ . Then every ascending chain of ideals in  $R$  becomes stationary, so by Remark 2.13 this means that the existence of a maximal ideal in  $R$  that contains  $I$  is trivial and does not require Zorn's Lemma (for which we had to work quite a bit). In fact, this is just the statement of Lemma 7.4 (a) which tells us that the family of all proper ideals of  $R$  containing  $I$  must have a maximal element.

Let us now prove some basic properties of Noetherian and Artinian modules.

Lemma 7.7. Let  $N$  be a submodule of an  $R$ -module  $M$ .

(a)  $M$  is Noetherian if and only if  $N$  and  $M / N$  are Noetherian.
(b)  $M$  is Artinian if and only if  $N$  and  $M / N$  are Artinian.

Proof. We just prove (a), since (b) can be proven in the same way, reversing all inclusions.

"  $\Rightarrow$  " Let  $M$  be Noetherian. First of all, any chain  $N_0\subset N_1\subset N_2\subset \dots$  of submodules of  $N$  is also a chain of submodules of  $M$ , and thus becomes stationary. Hence  $N$  is Noetherian.

Similarly, let  $P_0 \subset P_1 \subset P_2 \subset \dots$  be a chain of submodules of  $M / N$ . If we set  $M_k = q^{-1}(P_k)$  for all  $k \in \mathbb{N}$ , where  $q: M \to M / N$  is the quotient map, then  $M_0 \subset M_1 \subset M_2 \subset \dots$  is a chain of submodules of  $M$ . As  $M$  is Noetherian, we have  $M_k = M_n$  for all  $k \geq n$  with some  $n \in \mathbb{N}$ . But since  $q$  is surjective we then also have  $P_k = q(M_k) = q(M_n) = P_n$  for all  $k \geq n$ . Hence  $M / N$  is Noetherian.

"  $\Leftarrow$  " Let  $M_0\subset M_1\subset M_2\subset \dots$  be an ascending chain of submodules in  $M$  . If we set  $N_{k}\coloneqq M_{k}\cap N$  and  $P_{k}\coloneqq (M_{k} + N) / N$  for all  $k\in \mathbb{N}$  , then

$$
N _ {0} \subset N _ {1} \subset N _ {2} \subset \dots \quad \text {a n d} \quad P _ {0} \subset P _ {1} \subset P _ {2} \subset \dots
$$

are chains of submodules of  $N$  and  $M / N$ , respectively. By assumption, both of them become stationary, and hence there is an element  $n \in \mathbb{N}$  such that  $N_{k} = N_{n}$  and  $P_{k} = P_{n}$  for all  $k \geq n$ . But then we obtain a commutative diagram for all  $k \geq n$

![img-0.jpeg](images/img-0.jpeg)

whose rows are exact by Proposition 3.10 (c) and Example 4.3 (b), and whose columns are induced by the inclusions  $M_{n} \to M_{k}$ . As the left and right vertical map are isomorphisms, so is the middle one by Corollary 4.12, and thus we have  $M_{k} = M_{n}$  for  $k \geq n$  as well. Hence  $M$  is Noetherian.

# Remark 7.8.

(a) Of course, by Example 4.3 we can rephrase Lemma 7.7 by saying that for any short exact sequence  $0 \longrightarrow N \longrightarrow M \longrightarrow P \longrightarrow 0$  of  $R$ -modules the middle entry  $M$  is Noetherian (or Artinian) if and only if  $N$  and  $P$  are Noetherian (or Artinian).

---

.
2. Let $I$ be an ideal in a Noetherian (resp. Artinian) ring $R$. Combining Lemma 7.7 with Example 7.5 (c) we see that then the quotient $R/I$ is a Noetherian (resp. Artinian) ring as well.

###### Corollary 7.9.

Let $M$ and $N$ be $R$-modules.

1. The direct sum $M\oplus N$ is Noetherian if and only if $M$ and $N$ are Noetherian.
2. If $R$ is Noetherian and $M$ is finitely generated, then $M$ is also Noetherian.

The same statements also hold with “Noetherian” replaced by “Artinian”.

###### Proof.

Again, we only show the statement for Noetherian modules, since the Artinian counterpart follows in exactly the same way.

1. By Remark 7.8 (a), this follows from the exact sequence $0\longrightarrow M\longrightarrow M\oplus N\longrightarrow N\longrightarrow 0$.
2. Let $M=\langle\,m_{1},\ldots,m_{k}\,\rangle$ for some $m_{1},\ldots,m_{k}\in M$. Then the module homomorphism

$\varphi:R^{k}\to M,\;\;(a_{1},\ldots,a_{k})\mapsto a_{1}m_{1}+\cdots+a_{k}m_{k}$

is surjective, so that we have an exact sequence $0\longrightarrow\ker\varphi\longrightarrow R^{k}\xrightarrow{\varphi}M\longrightarrow 0$. Now as $R$ is Noetherian, so is $R^{k}$ by (a), and hence also $M$ by Remark 7.8 (a). ∎

###### Remark 7.10 (Structure Theorem for finitely generated Abelian groups).

Let $M$ be a finitely generated Abelian group, viewed as a finitely generated $\mathbb{Z}$-module as in Example 3.2 (d). Of course, $M$ is then a Noetherian $\mathbb{Z}$-module by Corollary 7.9 (b). But we can follow the idea of the proof of this statement one step further: the $\mathbb{Z}$-module $\ker\varphi$ occurring in the proof is (again by Remark 7.8 (a)) finitely generated as well, and so we also find a surjective ring homomorphism $\psi:\mathbb{Z}^{l}\to\ker\varphi$ for some $l\in\mathbb{N}$. This results in another short exact sequence $0\longrightarrow\ker\psi\longrightarrow\mathbb{Z}^{l}\xrightarrow{\psi}\ker\varphi\longrightarrow 0$, and thus by gluing as in Lemma 4.4 (b) in the exact sequence

$0\longrightarrow\ker\psi\longrightarrow\mathbb{Z}^{l}\xrightarrow{\psi}\mathbb{Z}^{k}\xrightarrow{\varphi}M\longrightarrow 0,$

which means that $M\cong\mathbb{Z}^{k}/\ker\varphi=\mathbb{Z}^{k}/\operatorname{im}\psi$.

Now $\psi\in\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}^{l},\mathbb{Z}^{k})$ is just given by an integer $k\times l$ matrix by Remark 3.17 (b). Similarly to the case of matrices over a field *[x13, Proposition 16.42]* one can show that it is possible to change bases in $\mathbb{Z}^{l}$ and $\mathbb{Z}^{k}$ such that the matrix of $\psi$ has non-zero entries only on the diagonal. But this means that $\operatorname{im}\psi$ is generated by $a_{1}e_{1},\ldots,a_{k}e_{k}$ for some $a_{1},\ldots,a_{k}\in\mathbb{Z}$, where $e_{1},\ldots,e_{k}$ denotes the standard basis of $\mathbb{Z}^{k}$. Thus

$M\;\;\cong\;\;\mathbb{Z}^{k}/\operatorname{im}\psi\;\;\cong\;\;\mathbb{Z}/a_{1}\mathbb{Z}\times\cdots\times\mathbb{Z}/a_{k}\mathbb{Z},$

and so we conclude that every finitely generated Abelian group is a product of cyclic groups. Of course, by the Chinese Remainder Theorem *[x12, Proposition 11.22]* this can also be rewritten as

$M\;\;\cong\;\;\mathbb{Z}^{r}\times\mathbb{Z}/q_{1}\mathbb{Z}\times\cdots\times\mathbb{Z}/q_{n}\mathbb{Z}$

for $r,n\in\mathbb{N}$ and (not necessarily distinct) prime powers $q_{1},\ldots,q_{n}$.

Let us now see how the finite length condition on modules is related to the concepts introduced in this chapter.

###### Lemma 7.11.

An $R$-module $M$ is of finite length if and only if it is both Noetherian and Artinian.

###### Proof.

If $M$ is of finite length, then all strict chains of submodules of $M$ are finite by Exercise 3.19 (b) and (c). So in this case $M$ is clearly both Noetherian and Artinian.

Conversely, assume that $M$ is both Noetherian and Artinian. Starting from $M_{0}=0$, we try to construct a chain $M_{0}\subsetneq M_{1}\subsetneq M_{2}\subsetneq\cdots$ of submodules of $M$ as follows: for $n\in\mathbb{N}$ let $M_{n+1}$ be a minimal submodule of $M$ that strictly contains $M_{n}$ — as long as $M_{n}\neq M$ this works by Lemma 7.4 (b) since $M$ is Artinian. But as $M$ is Noetherian as well, we cannot get such an infinite ascending chain of submodules, and thus we conclude that we must have $M_{n}=M$ for some $n\in\mathbb{N}$. The resulting chain $0=M_{0}\subsetneq M_{1}\subsetneq\cdots\subsetneq M_{n}=M$ is then a composition series for $M$, since by construction there are no submodules between $M_{i-1}$ and $M_{i}$ for all $i=1,\ldots,n$. ∎

######

---

###### Exercise 7.12.

Let $M$ be an $R$-module, and let $\varphi:M\to M$ be an $R$-module homomorphism. If $M$ is Noetherian (hence finitely generated) and $\varphi$ is surjective, you already know by Corollary 3.28 that $\varphi$ has to be an isomorphism.

Now show that if $M$ is Artinian and $\varphi$ is injective, then $\varphi$ is again an isomorphism.

(Hint: Consider the images of $\varphi^{n}$ for $n\in\mathbb{N}$.)

So far we have mostly considered chain conditions for general modules. For the rest of this chapter we now want to specialize to the case of rings. In this case we can obtain stronger results, however we will also see that this is where the Noetherian and Artinian conditions begin to diverge drastically. So let us consider these two conditions in turn, starting with the more important case of Noetherian rings.

The one central result on Noetherian rings is Hilbert’s Basis Theorem, which implies that “most rings that you will meet in practice are Noetherian”.

###### Proposition 7.13 (Hilbert’s Basis Theorem).

If $R$ is a Noetherian ring, then so is the polynomial ring $R[x]$.

###### Proof.

Assume that $R[x]$ is not Noetherian. Then by Lemma 7.4 (c) there is an ideal $I\unlhd R[x]$ that is not finitely generated. We can therefore pick elements $f_{0},f_{1},f_{2},\ldots\in I$ as follows: let $f_{0}\in I$ be a non-zero polynomial of minimal degree, and for $k\in\mathbb{N}$ let $f_{k+1}$ be a polynomial of minimal degree in $I\setminus\langle\,f_{0},\ldots,f_{k}\,\rangle$.

Now for all $k\in\mathbb{N}$ let $d_{k}\in\mathbb{N}$ be the degree and $a_{k}\in R$ the leading coefficient of $f_{k}$, so that we can write $f_{k}=a_{k}\,x^{d_{k}}+$ (lower order terms). Note that $d_{k}\leq d_{k+1}$ for all $k$ by construction of the polynomials. Moreover, since $R$ is Noetherian the chain of ideals $(a_{0})\subset(a_{0},a_{1})\subset(a_{0},a_{1},a_{2})\subset\cdots$ becomes stationary, and thus we must have $a_{n+1}=c_{0}a_{0}+\cdots+c_{n}a_{n}$ for some $n\in\mathbb{N}$ and $c_{0},\ldots,c_{n}\in R$. We can therefore cancel the leading term in $f_{n+1}$ by subtracting a suitable linear combination of $f_{0},\ldots,f_{n}$: in the polynomial

$f_{n+1}^{\prime}:=f_{n+1}-\sum_{k=0}^{n}c_{k}x^{d_{n+1}-d_{k}}f_{k}$

the $x^{d_{n+1}}$-coefficient is $a_{n+1}-c_{0}a_{0}-\cdots-c_{n}a_{n}=0$. But this means that $\deg f_{n+1}^{\prime}<\deg f_{n+1}$, and as $f_{n+1}\notin\langle\,f_{0},\ldots,f_{n}\,\rangle$ we must have $f_{n+1}^{\prime}\notin\langle\,f_{0},\ldots,f_{n}\,\rangle$ as well. This contradicts our choice of $f_{n+1}$, proving that an ideal $I$ as above cannot exist, and thus that $R[x]$ is Noetherian. ∎

###### Corollary 7.14.

Any finitely generated algebra over a Noetherian ring is itself a Noetherian ring.

###### Proof.

Let $R$ be a Noetherian ring. By Lemma 1.30, any finitely generated $R$-algebra is of the form $R[x_{1},\ldots,x_{n}]/I$ for an ideal $I$ in the polynomial ring $R[x_{1},\ldots,x_{n}]$. Hilbert’s Basis Theorem now implies by induction that the polynomial ring $R[x_{1},\ldots,x_{n}]=R[x_{1}][x_{2}]\cdots[x_{n}]$ is Noetherian. So by Remark 7.8 (b) the quotient $R[x_{1},\ldots,x_{n}]/I$ is a Noetherian ring as well. ∎

###### Remark 7.15 (Geometric interpretation of Noetherian and Artinian rings).

We have seen in Remark 1.31 that any coordinate ring $A(X)$ of a variety $X$ over a field $K$ is a finitely generated $K$-algebra. So by Corollary 7.14 we see that $A(X)$ is always a Noetherian ring. In particular, by Lemma 7.4 (c) this means that every ideal in $A(X)$ is finitely generated, and hence that any subvariety of $X$ can be defined by *finitely many* polynomial equations.

It is also instructive to study the original chain conditions of Definition 7.1 in a geometric setting. As the correspondence of Remark 1.10 between (radical) ideals in $A(X)$ and subvarieties of $X$ reverses inclusions, the ascending chain condition on ideals for the Noetherian ring $A(X)$ translates into a descending chain condition on subvarieties of $X$, i. e. every chain

$X_{0}\supset X_{1}\supset X_{2}\supset\cdots$

of subvarieties of $X$ must become stationary. The geometric picture behind this is the following: to make a subvariety smaller one has to drop an irreducible component or to reduce the dimension of the subvariety (a concept that we will introduce in Chapter 11), and this process must always

---

Andreas Gathmann

terminate since the number of components and the dimension are natural numbers. For example, in  $X = \mathbb{A}_{\mathbb{R}}^{2}$  we could have the following descending chain of subvarieties:

![img-1.jpeg](images/img-1.jpeg)

Of course, we can easily construct finite descending chains of subvarieties of  $\mathbb{A}_{\mathbb{R}}^2$  of any length in the same way, but infinite chains are impossible.

In contrast, as soon as  $X$  contains infinitely many points  $a_1, a_2, a_3, \ldots$ , it is easy to construct an infinite strictly ascending chain of subvarieties  $X_0 \subsetneq X_1 \subsetneq X_2 \subsetneq$  of  $X$  by setting  $X_n = \{a_k : k \leq n\}$  for all  $n \in \mathbb{N}$ . As this corresponds to a strictly decreasing chain of ideals in  $A(X)$ , we expect that a coordinate ring  $A(X)$  is Artinian if and only if  $X$  is a finite collection of points — so that the Artinian condition is a very strong one, in contrast to the Noetherian one.

To turn these expectations into rigorous statements, let us now study Artinian rings in detail and prove some algebraic results that all correspond to the geometric idea that an Artinian ring  $R$  should describe a finite union of points  $X$ . More precisely, consider the correspondence of subvarieties of  $X$  and ideals of  $R$  as in Remark 2.7: as the only irreducible subvarieties of  $X$  are single points, we would expect that any prime ideal of  $R$  is already maximal. Let us prove this now, together with the fact that in an Artinian ring the zero ideal is always a product of maximal ideals — which can also be translated into geometry by Remark 1.12 by saying that  $X$  is a union of finitely many points.

# Proposition 7.16. Let  $R$  be an Artinian ring.

(a) There are (not necessarily distinct) maximal ideals  $P_{1},\ldots ,P_{n}\triangleleft R$  such that  $P_{1}\cdot \dots \cdot P_{n} = 0$
(b)  $R$  has only finitely many prime ideals, all of them are maximal, and occur among the  $P_{1},\ldots ,P_{n}$  in (a).

# Proof.

(a) Let  $I = P_{1} \cdot \dots \cdot P_{n}$  be a product of maximal ideals  $P_{1}, \ldots, P_{n}$  such that  $I$  is minimal among all ideals that can be written in this form — such a minimal element exists by Lemma 7.4 (b) since  $R$  is Artinian. We need to show that  $I = 0$ . First we note:

(i)  $I^2$  is obviously also a product of maximal ideals, and we have  $I^2 \subset I$ . Hence  $I^2 = I$  by the minimality of  $I$ .
(ii) If  $P \triangleleft R$  is any maximal ideal, then  $PI$  is also a product of maximal ideals with  $PI \subset I$ . So again by the minimality of  $I$  we see that  $I = PI$ , which is clearly contained in  $P$ . Hence  $I$  is contained in every maximal ideal of  $R$ .

Now let us assume for a contradiction that  $I \neq 0$ . Then, as  $R$  is Artinian, Lemma 7.4 (b) implies that there is a minimal ideal  $J \triangleleft R$  with  $IJ \neq 0$ . About this ideal we note:

-  $J$  is a principal ideal (so in particular finitely generated): there must be an element  $b \in J$  with  $I \cdot (b) \neq 0$ , and we clearly have  $(b) \subset J$ , so  $(b) = J$  by the minimality of  $J$ .
-  $IJ = J$  again by the minimality of  $J$ , since  $IJ \subset J$  and  $I \cdot IJ = I^2 J = IJ \neq 0$  by (i).

Because of these two properties of  $J$  Nakayama's Lemma in Corollary 3.27 gives us an element  $a \in I$  with  $(1 - a)J = 0$ . As  $J \neq 0$ , this means that  $1 - a$  is not a unit in  $R$ . But then  $(1 - a) \neq R$ , hence  $1 - a$  is contained in a maximal ideal  $P \triangleleft R$ . But so is  $a \in I \subset P$  by (ii), and thus we obtain the contradiction  $1 = (1 - a) + a \in P$ . Hence we conclude that  $I = 0$ .

(b) Let  $P \triangleleft R$  be any prime ideal. Then  $P_i \subset P$  for some  $i = 1, \ldots, n$ , since otherwise there would be elements  $a_i \in P_i \backslash P$  for all  $i$ , which implies  $a_1 \cdot \dots \cdot a_n \in P_1 \cdot \dots \cdot P_n = 0 \subset P$  although no  $a_i$  lies in  $P$ . But  $P_i$  is maximal, and so we must have  $P = P_i$ .

---

7. Chain Conditions

A somewhat surprising consequence of this proposition is that every Artinian ring is Noetherian — a statement that is false for general modules as we have seen in Exercise 7.3:

**Proposition 7.17 (Hopkins).** For any ring $R$ we have:

$$
R \text{ is Artinian} \quad \Leftrightarrow \quad R \text{ is Noetherian and every prime ideal of } R \text{ is maximal}.
$$

**Proof.**

“$\Rightarrow$” Let $R$ be Artinian. Then every prime ideal is maximal by Proposition 7.16 (b). Moreover, by Proposition 7.16 (a) there are maximal ideals $P_{1}, \ldots, P_{n}$ of $R$ giving a chain

$$
0 = Q_{0} \subset Q_{1} \subset \cdots \subset Q_{n} = R
$$

of ideals in $R$, where $Q_{i} = P_{i+1} \cdot P_{i+2} \cdot \cdots \cdot P_{n}$ for $i = 0, \ldots, n$. Now for all $i = 1, \ldots, n$ the quotient $Q_{i} / Q_{i-1} = Q_{i} / P_{i}Q_{i}$ is an Artinian $R$-module by Lemma 7.7 (b), hence an Artinian $R / P_{i}$-vector space by Example 7.5 (c), therefore also a Noetherian $R / P_{i}$-vector space by Example 7.2 (a), and thus a Noetherian $R$-module again by Example 7.5 (c). So by induction on $i$ it follows from Lemma 7.7 (a) that $Q_{i}$ is a Noetherian $R$-module for all $i = 0, \ldots, n$. In particular, $R = Q_{n}$ is Noetherian.

“$\Leftarrow$” Assume that $R$ is Noetherian, but not Artinian. We have to find a prime ideal $P$ of $R$ that is not maximal.

Consider the family of all ideals $I$ of $R$ such that $R / I$ is not Artinian (as a ring or as an $R$-module, see Example 7.5 (c)). This family is non-empty since it contains the zero ideal, so as $R$ is Noetherian it must have a maximal element $P$ by Lemma 7.4 (a). Note that $P$ is certainly not a maximal ideal: otherwise $R / P$ would be a field by Lemma 2.3 (b), hence Artinian by Example 7.2 (a) — in contradiction to the choice of $P$.

It therefore suffices to prove that $P$ is prime, i.e. by Lemma 2.3 (a) that $S \coloneqq R / P$ is an integral domain. For any $a \in R$ consider the exact sequence

$$
0 \longrightarrow S / \operatorname{ann}(\bar{a}) \xrightarrow{\cdot\bar{a}} S \longrightarrow S / (\bar{a}) \longrightarrow 0
$$

of $S$-modules. As $S$ is not Artinian, we know by Remark 7.8 (a) that at least one of the rings $S / \operatorname{ann}(\bar{a})$ and $S / (\bar{a})$ cannot be Artinian either. But since $P$ was chosen to be maximal such that $S = R / P$ is not Artinian, taking a further quotient of $S$ by a non-zero ideal must yield an Artinian ring, and thus we conclude that $\operatorname{ann}(\bar{a}) = 0$ or $\bar{a} = 0$. In other words, every non-zero element of $R / P$ is a non-zero-divisor, i.e. $R / P$ is an integral domain.

**Example 7.18.** Let $I$ be a non-zero ideal in a principal ideal domain $R$. Then as in Example 1.4 we have $I = (a)$ with $a = p_1^{a_1} \cdots p_n^{a_n}$, where $a_1, \ldots, a_n \in \mathbb{N}_{&gt;0}$ and $p_1, \ldots, p_n$ are distinct prime elements of $R$. We want to check the conditions of Proposition 7.17 for the ring $S := R / I$.

First of all, by Lemma 1.21 the ideals of $S$ correspond to the ideals of $R$ that contain $I$. These are the ideals $(b)$ with $b \mid a$, i.e. such that $b = p_1^{b_1} \cdots p_n^{b_n}$ with $b_i \leq a_i$ for all $i$. In particular, $S$ has only finitely many ideals, which means by Definition 7.1 that $S$ is trivially Noetherian as well as Artinian.

Moreover, since $R$ is a principal ideal domain we have already seen in Example 2.6 (b) that every non-zero prime ideal in $R$ is maximal, and hence by Corollary 2.4 that every prime ideal in $S$ is maximal as well. Hence all three conditions of Proposition 7.17 are satisfied for $S$. In fact, the maximal ideals of $S$ are just the ideals $(\overline{p_i})$ for $i = 1,\ldots ,n$. So the equation $(\overline{p_1})^{a_1}\cdot \dots \cdot (\overline{p_n})^{a_n} = 0$ also verifies the statement of Proposition 7.16 (a).

**Example 7.19.** Specializing Example 7.18 to the geometric case $R = \mathbb{C}[x]$, we see that

$$
S = \mathbb{C}[x]/(f) \quad \text{with} \quad f = (x - x_1)^{a_1} \cdots (x - x_n)^{a_n}
$$

is an Artinian ring, where $x_1, \ldots, x_n \in \mathbb{C}$ are distinct and $a_1, \ldots, a_n \in \mathbb{N}_{&gt;0}$. In fact, $X = V(f) = \{x_1, \ldots, x_n\} \subset \mathbb{C}$ is a finite collection of points, in accordance with Remark 7.15. But $S$ is not reduced unless $a_1 = \cdots = a_n = 1$ since the class of $(x - x_1) \cdots (x - x_n)$ is nilpotent in $S$, and consequently $S$ is not the coordinate ring of $X$. Instead, the ring $S$ remembers the local multiplicity information at each point, i.e. the exponents $a_1, \ldots, a_n$ in $f$.

---

Andreas Gathmann

So even if $S$ corresponds to a finite collection of points, the structure of $S$ is not completely determined by giving these points: it also contains some local information at each of these points. The corresponding precise algebraic statement is that an Artinian ring is completely determined by its localizations at all maximal ideals:

**Proposition 7.20 (Structure Theorem for Artinian rings).** Every Artinian ring $R$ is a finite product of local Artinian rings.

More precisely, if $P_{1}, \ldots, P_{n}$ are the distinct maximal ideals of $R$ (see Proposition 7.16 (b)), then the localizations $R_{P_i}$ are also Artinian for all $i = 1, \ldots, n$, and the ring $R$ is isomorphic to $R_{P_1} \times \dots \times R_{P_n}$.

**Proof.** By Proposition 7.16 we can find $k \in \mathbb{N}$ such that $P_1^k \cdot \dots \cdot P_n^k = 0$. Note that $P_1^k, \ldots, P_n^k$ are pairwise coprime by Exercise 2.24. Hence $P_1^k \cap \dots \cap P_n^k = P_1^k \cdot \dots \cdot P_n^k = 0$ by Exercise 1.8, and so the Chinese Remainder Theorem of Proposition 1.14 implies that

$$
R \cong R / P _ {1} ^ {k} \times \dots \times R / P _ {n} ^ {k}.
$$

As the factors $R / P_i^k$ are clearly Artinian by Lemma 7.7 (b), it therefore only remains to be shown that the ring $R / P_i^k$ is isomorphic to the localization $R_{P_i}$ for all $i$. In fact, it is straightforward to construct mutually inverse ring homomorphisms, without loss of generality for $i = 1$:

- The ring homomorphism $R \to R_{P_1}$, $a \mapsto \frac{a}{1}$ contains $P_1^k$ in its kernel: if $a \in P_1^k$ we can choose $a_j \in P_j \setminus P_1$ for all $j = 2, \ldots, n$. Then $u := a_2^k \cdot \dots \cdot a_n^k \notin P_1$ since $P_1$ is prime, and $u a = a \cdot a_2^k \cdot \dots \cdot a_n^k \in P_1^k \cdot \dots \cdot P_n^k = 0$. This means that $\frac{a}{1} = 0$ in $R_{P_1}$. Hence the above map gives rise to a ring homomorphism $R / P_1^k \to R_{P_1}$, $\overline{a} \mapsto \frac{a}{1}$.
- Now consider the ring homomorphism $R \to R / P_1^k$, $a \mapsto \overline{a}$. It maps any $a \in R \setminus P_1$ to a unit: otherwise $(\overline{a})$ would be contained in a maximal ideal of $R / P_1^k$, which must be of the form $P / P_1^k$ for a maximal ideal $P \supset P_1^k$ of $R$ by Lemma 1.21 and Corollary 2.4. As $P$ is prime this means that $P \supset P_1$, and hence $P = P_1$ since $P_1$ is maximal. But $\overline{a} \in P_1 / P_1^k$ implies $a \in P_1$, a contradiction. By Exercise 6.12 we conclude that the above map gives us a ring homomorphism $R_{P_1} \to R / P_1^k$ with $\frac{a}{1} \mapsto \overline{a}$.

**Example 7.21.** Let us continue Example 7.18, i.e. consider the ring $S = R / I$ for a principal ideal domain $R$ and $I = (a)$ with $a = p_1^{a_1} \cdot \dots \cdot p_n^{a_n}$. In the proof of Proposition 7.20 we can then take any $k \in \mathbb{N}$ with $k \geq a_i$ for all $i = 1, \ldots, n$, and obtain

$$
S / (\bar {p _ {i}}) ^ {k} \cong R / (a, p _ {i} ^ {k}) = R / (p _ {i} ^ {a _ {i}})
$$

by Example 1.4 (a). So the decomposition of $S$ into local Artinian rings given by Proposition 7.20 is just

$$
S \cong R / (p _ {1} ^ {a _ {1}}) \times \dots \times R / (p _ {n} ^ {a _ {n}}),
$$

which by the proposition is also isomorphic to $S_{(p_1)} \times \dots \times S_{(p_n)}$.

**Exercise 7.22.** Let $R$ be a Noetherian ring. Show:

(a) If $R$ is an integral domain, every non-zero non-unit $a \in R$ can be written as a product of irreducible elements of $R$.
(b) For any ideal $I \trianglelefteq R$ there is an $n \in \mathbb{N}$ such that $(\sqrt{I})^n \subset I$.

**Exercise 7.23.** Let $S$ be a multiplicatively closed subset of a ring $R$. If $R$ is Noetherian (resp. Artinian), show that the localization $S^{-1}R$ is also Noetherian (resp. Artinian).

**Exercise 7.24.** Prove for any $R$-module $M$:

(a) If $M$ is Noetherian then $R / \operatorname{ann}M$ is Noetherian as well.
(b) If $M$ is finitely generated and Artinian, then $M$ is also Noetherian.

(Hint: You can reduce this to the statement of Proposition 7.17 that an Artinian ring is Noetherian.)