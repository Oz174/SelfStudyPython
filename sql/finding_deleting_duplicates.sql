CREATE TABLE employees (
   id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    department VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'John', 'Doe', 'john.doe@example.com', 'Sales'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', 'Marketing'),
(3, 'Bob', 'Johnson', 'bob.johnson@example.com', 'IT'),
(4, 'Alice', 'Williams', 'alice.williams@example.com', 'HR'),
(5, 'John', 'Doe', 'john.doe@example.com', 'Sales'),
(6, 'Sarah', 'Brown', 'sarah.brown@example.com', 'Marketing'),
(7, 'Bob', 'Johnson', 'bob.johnson@example.com', 'IT');



-- First Way (Group By and Count)
SELECT first_name,last_name,email, department ,COUNT(*)
FROM employees
GROUP BY first_name,last_name,email, department
HAVING COUNT(*) > 1;


-- Second Way (Window Functions and CTE)
with cte as (
SELECT *,
ROW_NUMBER() OVER (PARTITION BY first_name,last_name,email, department
ORDER BY id) as cnt
FROM employees
)
SELECT *
FROM cte
WHERE cnt > 1;

-- Third Way (Using Exists)
SELECT t1.*
FROM employees t1
WHERE EXISTS (
    SELECT 1 
    FROM employees t2
    WHERE t1.first_name = t2.first_name AND 
          t1.last_name = t2.last_name AND
          t1.email = t2.email AND
          t1.department = t2.department
          AND t1.id > t2.id
);

-- SELF JOIN
SELECT DISTINCT t1.*
FROM employees t1
INNER JOIN employees t2 ON 
 t1.first_name = t2.first_name AND 
 t1.last_name = t2.last_name AND
 t1.email = t2.email AND
 t1.department = t2.department AND
 t1.id > t2.id;


-- Need for a Unique Identifier:
-- For EXISTS and self-join methods, a unique identifier is necessary when finding exact duplicates.
-- This unique identifier (often an auto-incrementing ID or a primary key) helps distinguish between otherwise identical rows.
-- 2. Purpose of the Unique Identifier:

-- It allows us to compare rows without matching a row to itself.
-- It enables us to select only one row from each set of duplicates.
-- For large tables, consider these optimization techniques:

-- Ensure you have appropriate indexes on the columns you’re checking for duplicates.
-- If possible, use partitioning on the columns you frequently check for duplicates.
-- Consider using temporary tables or Common Table Expressions (CTEs) to break down complex queries.
-- Use EXPLAIN PLAN to analyze query performance and optimize accordingly.
-- For very large tables, consider using batch processing or parallel query execution if supported by your database system.





-- DELETING
WITH CTE AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY first_name,last_name,email, department -- list all columns that define a duplicate
               ORDER BY id -- preferably a primary key or unique identifier
           ) AS rn
    FROM employees
)
DELETE FROM CTE WHERE rn > 1;

SELECT * FROM employees;

-- The CTE uses ROW_NUMBER() to assign a number to each row within groups of duplicates.
-- PARTITION BY clause defines what constitutes a duplicate (list all columns that should be identical).
-- ORDER BY determines which duplicate to keep (the one with rn = 1).
-- The DELETE statement removes all rows where rn > 1, effectively deleting all but one of each set of duplicates.