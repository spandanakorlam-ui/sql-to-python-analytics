# sql-to-python-analytics
# SQL to Python Analytics – Average Salary by Department

## 📌 Project Overview
This mini project demonstrates how *SQL GROUP BY logic* can be implemented using *core Python* (without Pandas).

The goal is to calculate *average salary per department* from employee data.

---

## 🧠 SQL Logic
```sql
SELECT dept, AVG(salary)
FROM employees
GROUP BY dept;
