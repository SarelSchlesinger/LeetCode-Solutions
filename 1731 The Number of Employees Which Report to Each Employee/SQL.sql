select
    b.employee_id,
    b.name,
    count(a.reports_to) as 'reports_count',
    round(avg(a.age * 1.0), 0) as 'average_age'
from employees a join employees b
on a.reports_to = b.employee_id
group by b.employee_id, b.name
order by b.employee_id