select distinct l1.num as 'ConsecutiveNums'
from
    logs l1 join logs l2 on l1.num = l2.num
            join logs l3 on l3.num = l2.num
where l1.id + 1 = l2.id and l2.id + 1 = l3.id