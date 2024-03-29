# Naive Sorting

## Normal/Short bubble sort

In ordinary bubble sort, as we stated above, the outer loop makes n − 1 passes over the sequence of n items. The length of the sublist processed on each pass (let’s call this length p) diminishes by 1 on each pass. And on each pass p − 1 comparisons are made by the inner loop. On the first pass, p = n, so n − 1 comparisons are made. On the second pass, p reduces by 1, so n − 2 comparisons are made. The process continues until p is 1, so the algorithm will make (n − 1) + (n − 2) + ⋯ + 1 = ½n2 − ½n comparisons.

However, as we’ve already noted, the short bubble sort algorithm will stop as soon as the sequence is sorted. Thus, in the best case (where the sequence is already sorted), the outer loop will make only one pass, taking n − 1 comparisons (within a single execution of the inner loop) to establish this fact. In the worst case (the list is sorted in reverse order), the outer loop makes n − 1 passes, leading to a maximum of ½n2 − ½n comparisons, as outlined above.

In terms of the number of swaps, in the best case bubble sort will make no swaps (since the list is already sorted). In the worst case, every item will have to be swapped: every comparison will lead to a swap, so the number of swaps will equal the number of comparisons.

**_If we take our unit of computation to be the comparison, then, in the best case, the short bubble sort’s complexity is O(n). In the worst case, it is O(n2)._**

## Selection sort

Selection sort also makes n − 1 passes over a sequence of n elements. Its inner loop makes exactly the same number of comparisons as bubble sort, so the worst-case maximum number of comparisons will be the same. **_If the comparison is again taken as the unit of computation, selection sort’s worst-case complexity is O(n2), and in the best case it is also O(n2)._**

*Selection sort is worse than bubble sort on a sorted sequence because it doesn’t seem to be possible to stop the outer loop when no swaps are made, as is done in short bubble sort.*

However, since selection sort only makes one swap on each iteration of its inner loop, it will need to make a maximum of n − 1 swaps to move every item to its correct position.

## Insertion sort

Insertion sort works by placing items, one by one, into their correct positions in a sorted partition maintained at the start of the sequence. The correct position for an item is determined by comparing it with the items in the sorted partition and this requires a total of ½n2 − ½n comparisons, as with bubble and selection sorts, in the worst case, and only n − 1 comparisons in the best case.

However, insertion sort does not work by exchanging elements, but by shifting them. Whatever value is already in the slot to which an item is shifted is overwritten, rather than preserved and moved to a new place. Miller and Ranum note that this only takes one third of the computational effort of swapping.

**_Taking the unit of computation to be the comparison, in the best case, then, the insertion sort’s complexity is O(n). In the worst case, it is O(n2)._**

## Recap on iterative sorts

Short bubble sort is clearly the worst algorithm here. It makes as many comparisons as the other two, and generally makes many more swaps than the insertion or selection sorts.

Selection sort and insertion sort: in the worst case, both algorithms make the same number of comparisons as short bubble sort.

Insertion sort, working by shifting elements rather than swapping them, may be more efficient in practice. But in the end, with comparison as the unit of computation, all three algorithms have similar worst-case complexity of O(n2).

These three algorithms all involve what is termed **in-place sorting**, _that is, no other list needs to be created; the items are moved around within the original list. All of them depend on two loops, one embedded inside the other._

Considering the relative efficiency of these three algorithms by analysing their complexity.
There are two possible units of computation:

- Comparison of two items. The total number of comparisons made is a useful measure of the complexity of an algorithm. All sorting algorithms involve taking two elements and comparing their relative ordering, as specified by the ordering function.

- Swapping two elements. The total number of swaps made is also a useful measure of the complexity of an algorithm. Depending on the result of the comparison (1), it may be necessary for the algorithm to swap the positions of the two elements that have been compared.

In evaluating the complexity of an algorithm, the cost of comparing and of swapping two items is considered to be the same – O(1). However, in actual programs swapping is likely to be more expensive than comparing, so an O(n2) sorting algorithm that makes many swaps may actually run slower than an O(n2) algorithm that makes fewer, even on the same input. Most benchmark tests indicate that it is always better to try to minimise – if we can – the number of swaps.

**_Bubble sort, insertion sort and selection sort all  use one loop nested inside another. Thus, we have to multiply the number of computational steps which makes them O(n2)._**

---

## Recursive sorting

### Merge Sort

Merge sort is a recursive algorithm that continually splits a list in half, in effect using a divide and conquer technique which improves performance over sorting algorithms.

It initially checks the base case (list is empty or has one element), then recursively invokes a merge sort on both halves of the split list.

In general the merge sort a merge sort is a _O(n log n)_. Dividing a list in half is is _log2 n_, where n is the length of the list, the next step is merging which results in a list of size n, of which requires n operations. The result being log n splits, each of which cost n for a total of _n log n_ operations.

### Quick sort

Quick sort relies on a partitioning process in which a value is selected from the list and assigned to a variable pivotValue. Two pointers, leftmark and rightmark, are then progressively moved rightwards from the beginning, and leftwards from the end of the list. As the pointers move towards one another, items indicated by the left pointer that are greater than pivotValue are swapped with items indicated by the right pointer that are less than pivotValue.

When the pointers cross, the list is split into two partitions at the position at which the pointers have met, and quick sort is recursively performed on each of these two partitions.

The complexity of quick sort is O(n log n).

Quick sort is one of the fastest known sorting algorithms, however the choice of pivot can greatly affect the performance. In the best case, the pivot will split the list into two equal parts, in which the number of comparisons wil be _(n log n)_.  It can be shown that the total number of swaps in this case will be (n log n)/6. However, as the probability of the pivot being the exact median of the list is only 1/n on each iteration. In the average case, with the pivot being chosen at random, quick sort is O(n log n).

The worst case for quick sort  is when the pivot chosen at each step happens to be the largest or smallest item in the partition. The two new partitions formed will then be 0 and n − 1 items long. At the next step, sorting the partition of n − 1 items, picking the largest or smallest item as pivot, produces partitions of size 0 and one of size n − 2, … and so on. In this way, the list has to be split n times, and quick sort’s performance is then O(n2). It will also mean that the recursive version will require more memory for its stack, making the algorithm even less efficient.
