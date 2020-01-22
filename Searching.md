# Seaching

Searching is one of the most common operations in computing. In fact, solving most problems computationally can be seen as a form of search – looking for an answer amid a multitude of possibilities.

For instance finding the median in a list is a typical searching problem

What are the medians of [5, 7, 1, 6, 8, 22, 11, 34, 16, 4, 12] and of [6, 9, 2, 8, 17, 5, 31, 19, 3, 4, 15, 37]?

Sorting the lists we get:

[1, 4, 5, 6, 7, 8, 11, 12, 16, 22, 34] and

[2, 3, 4, 5, 6, 8, 9, 15, 17, 19, 31, 37].

therfore the median of the first list is 8 and the second list is 8.5 ((8+9)/2).

A median-finding problem is one instance of a more general problem of selection. Given an unordered list of n numbers, the selection task is to return the kth smallest item in the list. So, if k = 1 then we are looking for the smallest value in the list; k = 2 is the next smallest item after the minimum; and so on up to k = n, which is the maximum. So, the median-finding problem is just the selection problem with k = (n + 1)/2 if n is odd. (If n is even, then the median is the mean of the kth and (k +1)th smallest items, where k = n/2.)

Stated as a computational problem:

---

Name: Selection
Inputs: A sequence of integers S = (s1, s2, s3, …, sn), An integer k  
Outputs: An integer x  
Preconditions: Length of S > 0 and k > 0 and k ≤ n, For every sa, sb in S: if a ≠ b then sa ≠ sb  
Postcondition: x is the kth smallest item in S

---

a naive solution would be to sort the list (using quick sort) and then pick the kth smallest item, making the solution O(n log n). Alternatively, use a cut-down version of selection sort: find the smallest value and move it to the beginning of the list, then the next smallest, and go on doing this until the kth smallest item. But this has the same complexity as selection sort: it requires a nested loop, and so is O(n2)

![Quick Seach Example](./images/QuickSearch.png)  

Written as structued english:

```python
    IF length of S is 1

        return the first item in S

    set pivotValue to the first item in S

    set leftPart to an empty list

    set rightPart to an empty list

    ITERATE over S from the second item to the last item

        IF item is less than pivotValue

            append item to leftPart

        ELSE

            append item to rightPart

    IF length of leftPart greater than or equal to k

        return recursive call with (k, leftPart)

    ELSE IF length of leftPart equals k - 1

        return pivotValue

    ELSE

        return recursive call with (k - length of leftPart - 1, rightPart)
```

an example of quick search in python

```python
def quickSelect(k, aList):

    if len(aList) == 1:
        return aList[0]

    pivotValue = aList[0]
    leftPart = []
    rightPart = []

    for item in aList[1:]:
        if item < pivotValue:
             leftPart.append(item)
        else:
            rightPart.append(item)

    if len(leftPart) >= k:
        return quickSelect(k, leftPart)
    elif len(leftPart) == k - 1:
        return pivotValue
    else:
        return quickSelect(k - len(leftPart) -1, rightPart)
```

## Searching for Patterns


### Basic string search


