
# Recursion and more

## Induction

The goal of mathematical proof is to establish a proposition to be certainly true, not just in individual cases, but in all cases to which the proposition applies

for example take the proposition that for the sum of _n_ numbers is:

``` python
S(n) = n(n+1)/2
```

To prove that a proposition _P_(_n_), where n is a natural number, holds for any natural number, inductive proofs always proceed in the same way, in two steps:

- The base case. Prove that _P_(1) is true.

- The inductive step. Assume that _P_(_k_) is true, where _k_ is some natural number (the inductive hypothesis), and then show that, given this, _P_(_k_ + 1) must be true as well.

Proof:

The base case. For n = 1, the proposition is obviously true, since by definition S(1) is the sum of the first one natural number, so S(1) is 1;

and when n = 1:

```tex
\frac{n(n+1)}{2} = \frac{1(1+1)}{2} = 1
```

Thus we see that

```tex
S(n) = \frac{n(n+1)}{2}
```

when _n_ = 1. In other words, we have established that _P_(1) is true.

The inductive step. Assume the inductive hypothesis is true – that _P_(_k_) is true for the natural number k, i.e. that the sum of the first _k_ natural numbers, _S_(_k_), is:

```tex
S(k) = \frac{k(k+1)}{2}
```

and then show that P(k + 1) is true; in other words we aim to show that:

```tex
S(k+1) = \frac{(k+1)((k+1)+1)}{2}

or

s(k+1) = \frac{(k+1)(k+2)}{2}
```

by definition  ```S(k+1)``` is the sum of the first ```k+1``` natural numbers. 

In other words:
```S(k+1) = 1 + 2 + ... + k + (k+1)```

the  inductive hypothesis is that

```tex
S(k) = \frac{k(k+1)}{2}
```

 . On this basis, from the line above we can deduce that:

 ``` tex
S(k+1) = \frac{k(k+1)}{2} + (k+1).

rearranging the right side

S(k+1) = \frac{k(k+1)}{2} + \frac{2(k+1)}{2}

then...

S(k+1) = \frac{(k+1)(k+2)}{2}
 ```

Two thing can be gleaned from this

- the proposition P(n) is true for n = 1
- if the proposition is true for k it is also true for k + 1

**Remeber To prove a proposition, firstly proved the simplest possible case of the proposition. Then we based the second part of our proof on increasing the size of the problem by 1.**

## Reduction

a reduction is a special kind of transformation: the problem becomes smaller at every stage, and each step moves towards a problem so trivial that it can be solved instantly.


## Recursion

Recursion is a computational technique that involves a function calling itself. It can be used in the algorithmic quest to break down a problem into smaller and smaller sub-problems.

A recursive algorithm must:

    - Have a base case – usually a simple version of the problem that can be solved directly
    - Involve a state-change that moves the problem stepwise towards the base case
    - Call itself.