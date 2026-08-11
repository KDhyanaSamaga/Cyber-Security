# Proof of Distributive Laws of Sets

Set theory has two important distributive laws:

1. Union distributes over intersection
2. Intersection distributes over union

We will prove both using the **element method**.

---

# 1. Union Distributes Over Intersection

We need to prove:

$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$

## Step 1: Prove $A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)$

Let $x$ be an arbitrary element. Start with the left-hand side:

$$
\begin{aligned}
x \in A \cup (B \cap C) &\implies x \in A \lor x \in (B \cap C) \\
&\implies x \in A \lor (x \in B \land x \in C)
\end{aligned}
$$

Using the **distributive law of logic**: $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$

$$
\begin{aligned}
&\implies (x \in A \lor x \in B) \land (x \in A \lor x \in C) \\
&\implies x \in (A \cup B) \land x \in (A \cup C) \\
&\implies x \in (A \cup B) \cap (A \cup C)
\end{aligned}
$$

Therefore:

$$x \in A \cup (B \cap C) \implies x \in (A \cup B) \cap (A \cup C)$$

Hence:

$$A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)$$

---

## Step 2: Prove the Reverse Direction

Start from the right-hand side:

$$
\begin{aligned}
x \in (A \cup B) \cap (A \cup C) &\implies x \in (A \cup B) \land x \in (A \cup C) \\
&\implies (x \in A \lor x \in B) \land (x \in A \lor x \in C)
\end{aligned}
$$

Using the distributive law of logic: $(p \lor q) \land (p \lor r) \equiv p \lor (q \land r)$

$$
\begin{aligned}
&\implies x \in A \lor (x \in B \land x \in C) \\
&\implies x \in A \lor x \in (B \cap C) \\
&\implies x \in A \cup (B \cap C)
\end{aligned}
$$

Therefore:

$$(A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C)$$

---

## Step 3: Final Conclusion

We have proved both directions:

$$A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)$$

and:

$$(A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C)$$

Therefore:

$$\boxed{A \cup (B \cap C) = (A \cup B) \cap (A \cup C)}$$

---

# 2. Intersection Distributes Over Union

Now we prove the second distributive law:

$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$

---

## Step 1: Prove $A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)$

Let $x$ be an arbitrary element:

$$
\begin{aligned}
x \in A \cap (B \cup C) &\implies x \in A \land x \in (B \cup C) \\
&\implies x \in A \land (x \in B \lor x \in C)
\end{aligned}
$$

Using the **distributive law of logic**: $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$

$$
\begin{aligned}
&\implies (x \in A \land x \in B) \lor (x \in A \land x \in C) \\
&\implies x \in (A \cap B) \lor x \in (A \cap C) \\
&\implies x \in (A \cap B) \cup (A \cap C)
\end{aligned}
$$

Hence:

$$A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)$$

---

## Step 2: Prove the Reverse Direction

Start with:

$$
\begin{aligned}
x \in (A \cap B) \cup (A \cap C) &\implies x \in (A \cap B) \lor x \in (A \cap C) \\
&\implies (x \in A \land x \in B) \lor (x \in A \land x \in C)
\end{aligned}
$$

Using the distributive law of logic: $(p \land q) \lor (p \land r) \equiv p \land (q \lor r)$

$$
\begin{aligned}
&\implies x \in A \land (x \in B \lor x \in C) \\
&\implies x \in A \land x \in (B \cup C) \\
&\implies x \in A \cap (B \cup C)
\end{aligned}
$$

Hence:

$$(A \cap B) \cup (A \cap C) \subseteq A \cap (B \cup C)$$

---

## Step 3: Final Conclusion

Therefore:

$$\boxed{A \cap (B \cup C) = (A \cap B) \cup (A \cap C)}$$

---

# 3. The Two Distributive Laws

### Union over Intersection
$$\boxed{A \cup (B \cap C) = (A \cup B) \cap (A \cup C)}$$

### Intersection over Union
$$\boxed{A \cap (B \cup C) = (A \cap B) \cup (A \cap C)}$$

---

# 4. Important Connection With Logic

| Set Operation | Logical Operation |
|---|---|
| $x \in A \cup B$ | $x \in A \lor x \in B$ |
| $x \in A \cap B$ | $x \in A \land x \in B$ |
| $x \notin A$ | $\neg(x \in A)$ |

---
