-- first approach
select name
from customer
where referee_id <> 2 or referee_id is null

-- second approach
select name
from customer
where coalesce(referee_id, 0) <> 2