# Complexity Basics

This topic teaches how to reason about how efficient an algorithm is.

## Core ideas

- Time complexity tells you how runtime grows with input size
- Space complexity tells you how much memory is used
- Big-O notation is a common way to describe complexity

## Common Big-O cases

- O(1): constant time
- O(log n): logarithmic time
- O(n): linear time
- O(n log n): efficient sorting behavior
- O(n^2): nested loops

## Practice questions

1. What is the time complexity of a loop over n values?
2. What is the complexity of a nested loop?
3. Compare a dictionary lookup and a list search
4. Why is hashing often faster for counting tasks?
5. Explain the time cost of recursion with repeated subproblems
6. Compare linear search vs binary search
7. Why is O(n^2) slower than O(n log n) for large inputs?

## Interview tip

You do not need to memorize every formula. Learn the pattern: one loop is usually O(n), nested loops are often O(n^2), and hash lookups are close to O(1).

Here is a brief recap of nested loop time complexities:
O(n^2)$ (Quadratic): Standard nested loops where both the outer and inner loops iterate up to $n$ times (or where the inner loop depends linearly on the outer loop counter).
O(n log n)$ (Linearithmic): Outer loop runs $n$ times while the inner loop grows/shrinks exponentially (e.g., doubling or halving the counter each step).
O(n . m)$: Outer loop runs $n$ times and inner loop runs $m$ times for two independent input sizes.
O(1)$ (Constant): Both loops iterate a fixed number of times regardless of input size n.

Key Takeaway: Multiply the average iteration count of the inner loop by the total iterations of the outer loop. Auxiliary space complexity remains O(1) unless memory allocation happens inside the loop body.