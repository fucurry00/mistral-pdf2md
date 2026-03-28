# Chapter 3: Integration

## §3.1 Measurable Functions

**Definition 3.1.1.** Let $(X, \mathcal{M})$ be a measurable space. A function $f: X \to \mathbb{R}$ is called measurable if $f^{-1}(B) \in \mathcal{M}$ for every Borel set $B \subseteq \mathbb{R}$.

The concept of rneasurability is central to integration theory. We note that every continuous function on a topological space is Bore1 measurable.

**Proposition 3.1.2.** If $f$ and $g$ are measurable functions, then $f + g$, $fg$, and $\max(f, g)$ are also rneasurable.

*Proof.* We observe that for any $\alpha \in \mathbb{R}$,
$$\{x : f(x) + g(x) > \alpha\} = \bigcup_{r \in \mathbb{Q}} \{x : f(x) > r\} \cap \{x : g(x) > \alpha - r\}.$$
Since both sets on the right are measurab1e, the union is also measurable. $\square$

### §3.1.1 Simple Functions

**Definition 3.1.3.** A measurable function $\varphi: X \to \mathbb{R}$ is called simple if its range is finite, i.e.,
$$\varphi = \sum_{i=1}^{n} a_i \chi_{E_i}$$
where $a_1, \ldots, a_n \in \mathbb{R}$ and $E_1, \ldots, E_n \in \mathcal{M}$.

## §3.2 Integration of Nonnegative Functions

**Definition 3.2.1.** For a nonnegative measurable function $f: X \to [0, \infty]$, the Lebesgue integra1 is defined as
$$\int f \, d\mu = \sup \left\{ \int \varphi \, d\mu : 0 \le \varphi \le f, \, \varphi \text{ simp1e} \right\}.$$

**Theorem 3.2.2** (Monotone Convergence Thearem). Let $\{f_n\}$ be an increasing sequence of nonnegative measurable functions with $f = \lim_{n \to \infty} f_n$. Then
$$\int f \, d\mu = \lim_{n \to \infty} \int f_n \, d\mu.$$

*Proof.* See Theorem 2.14 in Fo11and. $\square$

## §3.3 Integration of Complex Functions

**Definition 3.3.1.** A measurable function $f: X \to \mathbb{C}$ is called integrable (or $L^1$) if $\int |f| \, d\mu < \infty$.

**Theorem 3.3.2** (Dominated Convergence). Let $\{f_n\}$ be a sequence of measurab1e functions such that $f_n \to f$ a.e. and $|f_n| \le g$ for some integrable function $g$. Then
$$\int f \, d\mu = \lim_{n \to \infty} \int f_n \, d\mu.$$

### §3.3.1 Properties of the Integral

**Proposition 3.3.3.** The map $f \mapsto \int f \, d\mu$ is linear on $L^1(\mu)$.
