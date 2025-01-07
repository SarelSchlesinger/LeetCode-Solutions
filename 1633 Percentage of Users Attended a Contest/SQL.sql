select 
    contest_id,
    round(count(*) * 100.0 / t.total_users, 2) as 'percentage'
from
    register
cross join
    (select count(*) as 'total_users' from users) t
group by contest_id, total_users
order by percentage desc, contest_id