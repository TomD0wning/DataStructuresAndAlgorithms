# Sets and Logic

## Contents



### Finite Sets

A set is an **unordered collection** of **distinct** elements, each of which is called either an element or a memeber of that set. These enities might be physical entities, such as people, bacteria, books or planets. In contrast they can also be **abstract** entities, like numbers, computer programs, or other sets. The simplest way of describing a set is a lsit of it members between curly braces, sperated by a comma. For instance a set of whole numbers between 3 & 8 inclusive is written as {3,4,5,6,7,8} however the ordering is not important.

When a set is reffered to as **distinct**, it means that no element occurs more than once in the set, so 4,5,8,6,4,3,4,5,8,3,7,5,7 when formed into a set would be {3,4,5,6,7,8}.

Writing sets with all the elements explicitly listed is described as the set **enumeration**. Sets can also be described by giving the propertiess of the elements of the set. The set above could also be written as {x: x is a while number between 3 & 8}.This method is known as set **comprehension**, which is often used to describe sets where the enumeration would be too complicated or too lengthy to write.

An example of array vs set outputs in python for a string that contains duplicates
``` python

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

Generally A is a subset of B if every memeber of A is also a member of B. Note that every set has both itself and the empty set as a subset A ⊑ A and ∅ ⊑ A

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


The intersection of two sets is the set of elements which are common members of each of the two sets. This is written as A ∩ B, this can also be written as A ∩ B = {x: x ∈ A and x ∈ B}. For instance
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

