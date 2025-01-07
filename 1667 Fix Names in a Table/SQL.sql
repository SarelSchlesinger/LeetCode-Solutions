select
    user_id,
    upper(left(name, 1)) + lower(right(name, len(name) - 1)) as 'name'
from users
order by user_id