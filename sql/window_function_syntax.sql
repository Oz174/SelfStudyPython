select * from table_1;

select region, sum(price)
from table_1
group by region;

-- first window function
select 
* ,
sum(price) over () as total_price,
sum(price) over (PARTITION BY region) as price_per_region
from 
table_1 ;

select 
* ,
sum(price) over (PARTITION BY region ORDER BY table_1.date) as running_price_per_region
from 
table_1 ;


select 
* ,
sum(price) over (ORDER BY id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) as useless_price
from 
table_1 ;



select 
* ,
sum(price) over (PARTITION BY region , quarter(table_1.date)) as quarter_revenue
from 
table_1;

-- adding regions in the same quarter 
INSERT INTO table_1 VALUES
(7,'2023-02-01','North',4500),
(8,'2023-11-01','North', 3200),
(9,'2023-11-01','South', 8400);

select * from table_1;

SELECT
    *,
    RANK() OVER (PARTITION BY region ORDER BY price DESC) as table_1_rank
    -- RANK() OVER (ORDER BY price DESC) as overall_rank
FROM
    table_1;
-- ORDER BY region, price DESC;