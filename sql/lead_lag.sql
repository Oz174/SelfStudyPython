UPDATE transactions SET AccountNumber = CASE ClientID 
                          WHEN 2 THEN 'ACC207' 
                          WHEN 3 THEN 'ACC307'
                          WHEN 4 THEN 'ACC407' 
                          WHEN 5 THEN 'ACC507'
                          WHEN 6 THEN 'ACC607'
                          WHEN 7 THEN 'ACC707'
                          WHEN 8 THEN 'ACC807'
                          WHEN 9 THEN 'ACC907'
                        END
                        where clientID in (2,3,4,5,6,7,8,9);

-- LAG 

SELECT 
    ClientID,
    AccountNumber,
    TransactionDate,
    TransactionAmount,
    LAG(TransactionAmount, 1, 0) OVER (PARTITION BY ClientID, AccountNumber ORDER BY TransactionDate) AS PrevTransactionAmount,
    TransactionAmount - LAG(TransactionAmount, 1, 0) OVER (PARTITION BY ClientID, AccountNumber ORDER BY TransactionDate) AS TransactionChange
FROM 
    transactions;

SELECT 
    ClientID,
    AccountNumber,
    TransactionDate,
    TransactionAmount,
    LEAD(TransactionAmount, 1, 0) OVER (PARTITION BY ClientID, AccountNumber ORDER BY TransactionDate) AS NextTransactionAmount,
    LEAD(TransactionAmount, 1, 0) OVER (PARTITION BY ClientID, AccountNumber ORDER BY TransactionDate) - TransactionAmount AS TransactionForecastChange
FROM 
    transactions;    
    
-- TIPS 

-- 1)
-- By creating an index that matches the ORDER BY clause in your query
-- you give your database a shortcut to finding the right rows quickly, without having to search through every single row.

create index date_index on transactions(TransactionDate); 
-- query time decreased from 0.015 seconds to 0.000 seconds

-- 2) Partitioning: Organize Your Data Like a Pro — Sometimes, your data is like a giant pizza. If you try to eat the whole thing at once, it's overwhelming (and slow!).
--  But if you slice it into smaller pieces, it's much easier to handle