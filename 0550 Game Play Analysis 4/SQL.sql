select
	round(count(a.player_id) * 1.0 / (select count(distinct player_id) from activity), 2) as 'fraction'
from
	activity a
join
	activity b
on
	a.player_id = b.player_id
where
	datediff(day, a.event_date, b.event_date) = 1 
    and
    a.event_date = (select
                        min(event_date)
                    from 
                        activity c
                    where
                        c.player_id = a.player_id
                    group by
                        player_id)