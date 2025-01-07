select
    isnull(
        (select top 1 *
        from myNumbers
        group by num
        having count(*) = 1
        order by num desc),
        null) as 'num'