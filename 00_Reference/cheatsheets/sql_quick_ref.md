# SQL Quick Reference

## Basic queries

```sql
SELECT column_name
FROM table_name;

SELECT *
FROM table_name
WHERE condition;
```

## Important clauses

- `WHERE`: filter rows
- `GROUP BY`: group rows together
- `ORDER BY`: sort results
- `HAVING`: filter grouped results
- `JOIN`: combine tables
- `LIMIT`: restrict number of rows

## Common joins

- `INNER JOIN`: match rows in both tables
- `LEFT JOIN`: all rows from left, matched rows from right
- `RIGHT JOIN`: all rows from right, matched rows from left
- `FULL OUTER JOIN`: all rows from both sides

## Aggregations

- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

## Example

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;
```

## Interview reminder

- know the difference between `WHERE` and `HAVING`
- practice join logic and grouping
- be comfortable with window functions later
