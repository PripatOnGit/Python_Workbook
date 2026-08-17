# Stacks and Queues

These are linear data structures with very different access rules.

## Stack

- Last In, First Out (LIFO)
- Think of a pile of plates
- Common operations: push, pop, peek

## Queue

- First In, First Out (FIFO)
- Think of a line at a counter
- Common operations: enqueue, dequeue, front

## Practice problems

1. Check if a string has balanced parentheses
2. Reverse a string using a stack
3. Implement queue operations with a list
4. Simulate task processing order
5. Check if a sequence is valid using a stack
6. Evaluate whether a bracket expression is valid
7. Use a queue to process jobs in order
8. Implement a basic stack with push and pop

## Example

```python
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())
```

## Interview tip

Use stacks for nested structures like parentheses and backtracking; use queues for ordering and processing tasks in sequence.
