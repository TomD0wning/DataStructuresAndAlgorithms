# Sets and Logic

## Contents

### Finite Sets

A set is an **unordered collection** of **distinct** elements, each of which is called either an element or a member of that set. These entities might be physical entities, such as people, bacteria, books or planets. In contrast they can also be **abstract** entities, like numbers, computer programs, or other sets. The simplest way of describing a set is a list of its members between curly braces, separated by a comma. For instance a set of whole numbers between 3 & 8 inclusive is written as {3,4,5,6,7,8} however the ordering is not important.

When a set is referred to as **distinct**, it means that no element occurs more than once in the set, so 4,5,8,6,4,3,4,5,8,3,7,5,7 when formed into a set would be {3,4,5,6,7,8}.

Writing sets with all the elements explicitly listed is described as the set **enumeration**. Sets can also be described by giving the properties of the elements of the set. The set above could also be written as {x: x is a while number between 3 & 8}.This method is known as set **comprehension**, which is often used to describe sets where the enumeration would be too complicated or too lengthy to write.

An example of array vs set outputs in python for a string that contains duplicates

```python

[c for c in 'aardvark']
# ['a', 'a', 'r', 'd', 'v', 'a', 'r', 'k']

{c for c in 'aardvark'}
# {'a', 'd', 'k', 'r', 'v'}
```

It's also worth noting that a set is not the same as it's members {1,2,3} and {{1,2,3}} are different, the former containing 3 numbers and the latter contains one set, which contains 3 numbers. An empty set is written as {} or ∅. however {∅} is not the same as ∅.

### Basic set operations

#### Set membership

If _S_ is a set then x ∈ _S_ means that x is a member of the set _S_ whereas x ∉ _S_ means that x is not a member of set _S_

As python code:

``` python
setA = {'a', 'd', 'k', 'r', 'v'}
'a' in setA # true
'z' not in setA # true
```

given this all the below would return true

3 ∈ {1,2,3,4,5}
8 ∉ {1,2,3,4,5}
a ∈ {c: c is a letter in 'aardvark'}
b ∉ ∅

As sets are unordered, entities are  either in the set or they are not, there isn't a concept of saying x is the nth member of a set.

#### Subset

If all the elements of a set are to be found in another set, then the first set is a subset of the second. This is written as
A ⊑ B

Generally A is a subset of B if every member of A is also a member of B. Note that every set has both itself and the empty set as a subset A ⊑ A and ∅ ⊑ A

If A is a subset of B and  is not equal to B, then A us described as a proper subset of B, written as A ⊏ B 

```python
setA = {'a','r'}
setB = {'a', 'd', 'k', 'r', 'v'}
setA.issubset(setB) # true
```

#### Equality of sets

Two sets are equal if they contain exactly the same members. This is written as A = B.

set equality can also be defined in terms of sub sets: A = B if and only if A ⊑ B and B ⊑ A


#### Set union

The union of two sets is a set containing  all the members of those two sets. This is written as A ∪ B.

This can also be written as A ∪ B = {x :x ∈ A or x ∈ B} where or is inclusive for example:

- {1,2,3} ∪ {3,4,5} = {1,2,3,4,5}
- ∅ ∪ A = A, where A is any set

And as sets do not contain duplicates, 3 only appears once, even though it's in both sets

```python
setA = {'a','r'}
setB = {'a', 'd', 'k', 'r', 'v'}
setA.union(setB) # {'a', 'd', 'k', 'r', 'v'}
```

#### Set intersection

The intersection of two sets is the set of elements which are common members of each of the two sets. This is written as A ∩ B, this can also be written as A ∩ B = {x: x ∈ A and x ∈ B}. For instance.

- {1,2,3} ∩ {3,4,5} = {3}
- ∅ ∩ A = ∅

```python
setA = {1,2,3}
setB = {3,4,5}
setA.intersection(setB) # {3}
```

#### Set difference

The difference of a set A and a set B is the set of elements of A which are not elements of B. Written as
A - B, also written as A - B = {x: x ∈ A and x ∉ B}

examples are:

- {a,b,c,d,e} - {d,b} = {a,c,e}
- {1,2,3,4} - {3,4,5,6} = {1,2}
- {x: x is an integer} - {x: x is an even number} = {x: x is an odd number}

For two sets A & B, A - B is not the same as B - A unless the two sets are equal.

```python
setA = {1,2,3}
setB = {3,4,5}
setA.difference(setB) # {1,2}
```

### Cardinality of finite sets

Cardinality is a key idea in sets. For finite sets, the cardinality of a set is just the number of entities that is has; this is often simple to calculate, for instance for set {1,2,3} the cardinality is 3 and for a set of {x : x is a prime number less than 20 } the cardinality is 8 as the enumeration is {2,3,5,7,11,13,17,19}.

There are also sets that can be difficult to calculate , such as a set of the currently living human race.

Cardinality of a set is denoted by placing the set between two pipes, |{1,2,3}| = 3. However when a set contains multiple sets, the cardinality is not the number of items in the sub sets, but the number of sub sets and the highest level elements. For instance {{1,2,3},{3,2,1}} has a cardinality of 2 even though the sets each have a cardinality of 3. The cardinality of an empty set {∅} is 1 even though it has no members.

### Tuples and Cartesian products

A tuple is a sequence of elements, which unlike a set, is ordered and can contain duplicates. Unlike sets tuples are finite. Tuples which contain n elements are referred to as n-tuples, this is normally denoted with standard brackets rather than curly braces, like so (a1,a2,a3).

A 2-tuple has two members, also known as an ordered pair, a 3-tuple has three members, called a triple, a 10-tuple has 10 elements and so on.

Two tuples are the same only if they have the same elements in the same sequence, for instance (1,2,3) is not the same as (3,2,1). And as with sets, there is a 0-tuple with no members ().

The concept of an ordered pair can be used to define the **Cartesian product** for two sets. The Cartesian product of two sets, A & B, is written as A x B and is the set of all the ordered pairs (x,y) where x is a member of A and y is a member of B. This can also be written as a set comprehension A x B  = {(x,y) : x ∈ A and y ∈ B}. For instance {1,2} x {1,3,5} = {(1,1),{1,3},(1,5),(2,1),(2,3),(2,5)}.

A simple strategy for finding the Cartesian product is:

- Choose an element. Place element in the first position of an ordered pair. Then work through the other set forming pairs with each element in the set.
- repeat as above for every other element.

```python
setA = {1,2,3}
setB ={1,2}
setC = {'apple','banana'}

{{x,y,z} for x in setA for y in setB for z in setC}
```
