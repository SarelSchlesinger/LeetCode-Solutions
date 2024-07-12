select p.product_id, isnull(round(sum(u.units * p.price) * 1.0 / sum(u.units), 2), 0) as 'average_price'
from prices p left join unitsSold u
on p.product_id = u.product_id and
    u.purchase_date between p.start_date and p.end_date
group by p.product_id