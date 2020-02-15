Select 
    e1.Name AS Employee 
FROM Employee e1 JOIN Employee e2 
    ON e1.ManagerId = e2.Id 
    and e1.salary > e2.salary;