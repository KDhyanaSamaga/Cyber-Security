# Basic Set Theory

## 1. What is a Set?

A **set** is a well-defined collection of distinct objects.

The objects contained in a set are called **elements** or **members** of the set.

A set is usually represented using **capital letters**, while its elements are represented using lowercase letters or other symbols.

### Example

Let:

    A = {1, 2, 3, 4, 5}

Here:

- `A` is the set.
- `1, 2, 3, 4, 5` are the elements of `A`.
- `2 ∈ A` means `2` belongs to `A`.
- `8 ∉ A` means `8` does not belong to `A`.

### Important Characteristics of a Set

1. The elements of a set are **distinct**.
2. The order of elements does not matter.
3. A set must be **well-defined**, meaning we should be able to determine whether an object belongs to the set or not.

For example:

    A = {1, 2, 3}

and

    B = {3, 1, 2}

represent the same set because the order does not matter.

Therefore:

    A = B

---

# 2. Examples of Sets

### Example 1: Set of Natural Numbers

    N = {1, 2, 3, 4, 5, ...}

### Example 2: Set of Vowels

    V = {a, e, i, o, u}

### Example 3: Set of Even Numbers

    E = {2, 4, 6, 8, 10, ...}

### Example 4: Set of Students

Suppose a class contains five students:

    S = {Alice, Bob, Charlie, David, Eve}

Here, each student is an element of the set `S`.

---

# 3. Methods of Representing a Set

There are several ways to represent a set.

## 3.1 Roster / Tabular Form

In the **roster method**, all elements of the set are explicitly listed inside curly brackets `{ }`.

### Example

    A = {2, 4, 6, 8, 10}

This represents the set of the first five positive even numbers.

### Example

    V = {a, e, i, o, u}

### Advantages

- Simple and easy to understand.
- Suitable when the number of elements is small.
- Elements can be directly identified.

### Limitation

It becomes inconvenient when the set contains a very large or infinite number of elements.

For example:

    N = {1, 2, 3, 4, 5, ...}

---

# 3.2 Set-Builder Form

In the **set-builder method**, we describe the property that every element of the set satisfies.

The general form is:

    A = {x | x satisfies a given condition}

The symbol `|` means **"such that"**.

It can also be written using a colon:

    A = {x : x satisfies a given condition}

### Example

The set of positive even numbers less than 10 can be written as:

    A = {x | x is an even number and 0 < x < 10}

Therefore:

    A = {2, 4, 6, 8}

### Mathematical Form

We can also write:

    A = {x ∈ N | x is even and x < 10}

This means:

> A contains all natural numbers `x` such that `x` is even and `x < 10`.

### Advantages

- Useful for large sets.
- Useful for infinite sets.
- Describes the underlying rule or property of the set.

---

# 3.3 Venn Diagram

A **Venn diagram** represents sets graphically using closed curves, usually circles or ellipses.

The rectangle surrounding the sets represents the **universal set**.

For example:

    U = {1, 2, 3, 4, 5, 6}

Suppose:

    A = {1, 2, 3}
    B = {3, 4, 5}

The element `3` belongs to both `A` and `B`.

Therefore, the overlapping region represents:

    A ∩ B = {3}

Venn diagrams are particularly useful for visualizing:

- Union
- Intersection
- Difference
- Complement
- Disjoint sets

---

# 3.4 Descriptive Form

A set can also be described in words.

### Example

    A = {x | x is a prime number less than 10}

In descriptive form:

> A is the set of prime numbers less than 10.

Therefore:

    A = {2, 3, 5, 7}

---

# 4. Basic Set Operations

## 4.1 Union

The **union** of two sets contains all elements that belong to either set or to both sets.

It is represented by:

    A ∪ B

### Example

    A = {1, 2, 3}
    B = {3, 4, 5}

Then:

    A ∪ B = {1, 2, 3, 4, 5}

---

## 4.2 Intersection

The **intersection** of two sets contains elements that are common to both sets.

It is represented by:

    A ∩ B

### Example

    A = {1, 2, 3}
    B = {3, 4, 5}

Therefore:

    A ∩ B = {3}

---

## 4.3 Difference

The difference between `A` and `B` contains elements that belong to `A` but not to `B`.

It is represented by:

    A - B

### Example

    A = {1, 2, 3}
    B = {3, 4, 5}

Therefore:

    A - B = {1, 2}

Similarly:

    B - A = {4, 5}

---

## 4.4 Complement

The complement of a set `A` contains all elements in the universal set `U` that are not in `A`.

It is represented by:

    Aᶜ

### Example

    U = {1, 2, 3, 4, 5}
    A = {1, 2, 3}

Therefore:

    Aᶜ = {4, 5}

---

# 5. Important Properties of Sets

Set operations follow several important laws.

---

## 5.1 Commutative Law

The order of sets does not affect the result of union or intersection.

### Union

    A ∪ B = B ∪ A

### Intersection

    A ∩ B = B ∩ A

### Example

    A = {1, 2, 3}
    B = {3, 4, 5}

Then:

    A ∪ B = {1, 2, 3, 4, 5}

and:

    B ∪ A = {1, 2, 3, 4, 5}

Therefore:

    A ∪ B = B ∪ A

---

# 5.2 Associative Law

The grouping of sets does not affect the result.

### Union

    (A ∪ B) ∪ C = A ∪ (B ∪ C)

### Intersection

    (A ∩ B) ∩ C = A ∩ (B ∩ C)

### Example

Let:

    A = {1, 2}
    B = {2, 3}
    C = {3, 4}

Then:

    (A ∪ B) ∪ C
    = {1, 2, 3} ∪ {3, 4}
    = {1, 2, 3, 4}

And:

    A ∪ (B ∪ C)
    = {1, 2} ∪ {2, 3, 4}
    = {1, 2, 3, 4}

Therefore:

    (A ∪ B) ∪ C = A ∪ (B ∪ C)

---

# 5.3 Identity Law

The identity law states that certain sets do not change a set when used with union or intersection.

Let `U` be the universal set and `∅` be the empty set.

### Union Identity

    A ∪ ∅ = A

### Intersection Identity

    A ∩ U = A

### Example

    A = {1, 2, 3}

Then:

    A ∪ ∅ = {1, 2, 3}

and:

    A ∩ U = A

The empty set acts as the identity for union, while the universal set acts as the identity for intersection.

---

# 5.4 Idempotent Law

Applying the same set operation to a set with itself does not change the set.

### Union

    A ∪ A = A

### Intersection

    A ∩ A = A

### Example

    A = {1, 2, 3}

Then:

    A ∪ A = {1, 2, 3}

and:

    A ∩ A = {1, 2, 3}

Therefore:

    A ∪ A = A
    A ∩ A = A

---

# 5.5 Involution Law

The complement of the complement of a set gives the original set.

    (Aᶜ)ᶜ = A

This is called the **Involution Law**.

### Example

Let:

    U = {1, 2, 3, 4, 5}
    A = {1, 2, 3}

Then:

    Aᶜ = {4, 5}

Taking the complement again:

    (Aᶜ)ᶜ = {1, 2, 3}

Therefore:

    (Aᶜ)ᶜ = A

---

# 5.6 Distributive Law

The distributive laws describe how union and intersection interact with each other.

### Intersection over Union

    A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

### Union over Intersection

    A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

These are analogous to the distributive property in algebra.

For example:

    a(b + c) = ab + ac

is similar in structure to:

    A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

---

# 5.7 Complement Laws

Two important complement laws are:

### Complement of Universal Set

    Uᶜ = ∅

### Complement of Empty Set

    ∅ᶜ = U

This follows directly from the definition of a complement.

---

# 5.8 Domination Laws

The universal set and empty set can dominate certain operations.

### Union with Universal Set

    A ∪ U = U

### Intersection with Empty Set

    A ∩ ∅ = ∅

---

# 5.9 Complement Laws for Union and Intersection

These are known as **De Morgan's Laws**.

### First De Morgan's Law

    (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ

Meaning:

> The complement of the union is the intersection of the complements.

### Second De Morgan's Law

    (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ

Meaning:

> The complement of the intersection is the union of the complements.

These laws are extremely important in mathematical logic and computer science.

---

# 6. Sets in Cybersecurity

Set theory is not just a theoretical mathematical topic. It is used in several areas of computer science and cybersecurity.

## Example: User Permissions

Suppose:

    A = {users with read permission}
    B = {users with write permission}

Then:

    A ∩ B

represents users who have **both read and write permissions**.

While:

    A ∪ B

represents users who have **either read or write permission**.

---

## Example: Network Security

Suppose:

    A = {IP addresses allowed by Firewall Rule 1}
    B = {IP addresses allowed by Firewall Rule 2}

Then:

    A ∩ B

represents IP addresses allowed by **both rules**.

And:

    A - B

represents IP addresses allowed by Rule 1 but not Rule 2.

This type of set reasoning is useful when analyzing:

- Firewall rules
- Access-control policies
- User permissions
- IP address ranges
- Security groups
- Network segmentation

---

# 7. Summary of Important Set Laws

| Law | Union | Intersection |
|---|---|---|
| Commutative | `A ∪ B = B ∪ A` | `A ∩ B = B ∩ A` |
| Associative | `(A ∪ B) ∪ C = A ∪ (B ∪ C)` | `(A ∩ B) ∩ C = A ∩ (B ∩ C)` |
| Identity | `A ∪ ∅ = A` | `A ∩ U = A` |
| Idempotent | `A ∪ A = A` | `A ∩ A = A` |
| Domination | `A ∪ U = U` | `A ∩ ∅ = ∅` |

### Complement Laws

    Uᶜ = ∅

    ∅ᶜ = U

    (Aᶜ)ᶜ = A

### De Morgan's Laws

    (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ

    (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ

### Distributive Laws

    A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

    A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
