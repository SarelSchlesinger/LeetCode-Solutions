select
    max(b.name) as 'name'
from
    employee a join employee b
on
    a.managerID = b.id
group by b.id
having count(*) >= 5