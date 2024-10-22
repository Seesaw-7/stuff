SELECT r.contest_id, ROUND(COUNT(r.user_id)/(select COUNT(1) from Users)*100, 2) AS percentage
FROM Users u
JOIN Register r
ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC

-- order by can have multiple desc/asc choices
-- use sub queries if need to use multiple tables