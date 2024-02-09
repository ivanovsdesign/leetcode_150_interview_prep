# Write your MySQL query statement below
WITH union_cte AS (
    SELECT requester_id, accepter_id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id, requester_id FROM RequestAccepted
)

SELECT requester_id as id, COUNT(*) as num FROM union_cte
GROUP BY requester_id
ORDER BY num DESC LIMIT 1