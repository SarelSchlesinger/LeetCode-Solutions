select a.unique_id, b.name
from EmployeeUNI a right join Employees b
on a.id = b.id
