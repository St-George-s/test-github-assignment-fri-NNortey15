DESCRIBE ALL TABLES;

-- SELECT  P.forename,P.surname,P.plannerNo, COUNT(W.walkID) AS "Total participants"
-- FROM   Walk W, Route R, Planner P 
-- WHERE W.routeID = R.routeID AND R.plannerNo =P.plannerNo
-- GROUP BY P.forename,
-- P.surname, P.plannerNo
-- ORDER BY "Total participants" DESC; 

-- SELECT W.walkerNo, W.forename,W.surname,W.telNo
-- FROM Walker W, Route R, Walk WK
-- WHERE 
--     W.WalkerNo = WK.WalkerNo 
--     AND Wk.routeID = R.routeID
--     AND R.distance = 
--         (
--             SELECT MAX(distance)
--             FROM Route AS "Longest"
--         )
-- GROUP BY W.telNo
-- ORDER BY W.walkerNo ASC;

SELECT Route.routeID, woodName, description
FROM Route
WHERE footwear = "Trail shoes"
OR footwear = "Waterproof shoes"
OR footwear = "Walking shoes";