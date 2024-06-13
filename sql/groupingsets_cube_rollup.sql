-- Grouping Sets
-- returns sum by city in n city rows and m fruit rows
Select Fruit , City , sum(Amt) 
from Spends
group By Grouping SETS ((Fruit) , (City));

-- Rollup
-- returns sum of the first argument in n rows of the first argument
-- returns sum of first arg N second argument (as if it accumulated)
-- returns the total also at the end 
Select Fruit , City , sum(Amt)
from Spends
group By Fruit , City with Rollup; -- or city , fruit

-- Cube
-- returns sum of the first argument in n rows of the first argument
-- for A , B , C it returns sum of A , B , C , A.B , A.C , B.C , A.B.C
-- returns total also 
Select Fruit , City , sum(Amt)
from Spends
group By Cube (Fruit , City); -- or city , fruit
