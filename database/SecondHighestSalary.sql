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