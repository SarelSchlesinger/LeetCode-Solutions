select a.id as 'id'
from weather a join weather b
on datediff(day, b.recordDate, a.recordDate) = 1
where a.temperature > b.temperature