
-- 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+

-- 例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+


-- 解1，子查询
SELECT (
		SELECT DISTINCT salary
		FROM employee
		ORDER BY salary DESC
		LIMIT 1, 1
	) AS SecondHighestSalary;

-- 解2，使用IFNULL
SELECT IFNULL((
		SELECT DISTINCT salary
		FROM employee
		ORDER BY salary DESC
		LIMIT 1, 1
	), NULL) AS SecondHighestSalary;