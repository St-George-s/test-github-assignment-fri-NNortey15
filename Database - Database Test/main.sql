DESCRIBE ALL TABLES;

-- SELECT episodeTitle, showName , maxViewers, episodedate
-- FROM show S ,Episode E 
-- WHERE S.showID = E.showID;

SELECT showName ,episodeTitle
FROM Show S  
JOIN Episode EP ON  EP.showID = S.showID 
WHERE episodeDate LIKE '2024-12-__%';

-- -- UPDATE  Timeslot 
-- -- SET endtime = '19:30'
-- -- WHERE episodeDate = '2024-12-24' AND showName = 'Star Cooks';

-- SELECT showName AS 'ShowName', COUNT(ratingValue) AS 'TotalRatings'
-- FROM Show S , Episode E, ViewerRating VR
-- WHERE S.showID = E.showID
-- AND E.episodeID = VR.episodeID
-- GROUP BY showName
-- ORDER BY  VR.episodeID ASC;