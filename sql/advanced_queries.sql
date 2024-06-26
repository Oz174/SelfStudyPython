-- Section 1 : Subqueries and Joins

-- Subqueries with IN Clause 
-- Find the names of all the customers who have placed an order for product 'Pepsi'
SELECT customer_name
FROM customers
WHERE customer_id IN (SELECT customer_id
                      FROM orders
                      WHERE product_id = 'Pepsi');

-- Subqueries with EXISTS Clause
-- Find the names of all the customers who have placed an order for product 'Pepsi'
SELECT customer_name
FROM customers
WHERE EXISTS (SELECT 1
              FROM orders
              WHERE orders.customer_id = customers.customer_id
              AND product_id = 'Pepsi');

-- Self Join 
-- Selecting Employee and his manager name 
SELECT e.employee_name, m.employee_name AS manager_name
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id;

-- Section 2 : Window Functions 
-- ROW_NUMBER() for ranking

-- Example: Ranking employees by salary within each department
SELECT employee_name, salary, department_id,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Example : Ranking Top 3 employees by salary within each department
SELECT employee_name, salary, department_id,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM employees
WHERE salary_rank <= 3;

-- LEAD AND LAG functions for Time Series Analysis
-- Example: Analyzing the change in sales over time
SELECT order_date, total_sales,
       LAG(total_sales) OVER (ORDER BY order_date) AS previous_sales,
       LEAD(total_sales) OVER (ORDER BY order_date) AS next_sales
FROM orders;

-- Section 3 : Common Table Expressions (CTE)
-- Example: Selecting all employees in a hierarchical manner
WITH RECURSIVE EmployeeHierarchy AS (
  SELECT employee_id, employee_name, manager_id
  FROM employees
  WHERE manager_id IS NULL

UNION ALL
  SELECT e.employee_id, e.employee_name, e.manager_id
  FROM employees e
  JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM EmployeeHierarchy;

-- Example: Calculating the average salary difference from department average
WITH DepartmentAvg AS (
  SELECT department_id, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department_id
)
SELECT e.employee_name, e.salary, d.avg_salary, e.salary - d.avg_salary AS salary_difference
FROM employees e
JOIN DepartmentAvg d ON e.department_id = d.department_id;

-- Section 4 : Advanced Aggregations
-- GROUP_CONCAT() for string aggregation
-- Example: Concatenating employee names in each department
SELECT department_id, GROUP_CONCAT(employee_name ORDER BY employee_name ASC) AS employee_list
FROM employees
GROUP BY department_id;

