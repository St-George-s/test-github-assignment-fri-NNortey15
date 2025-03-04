DESCRIBE ALL TABLES;

-- SELECT comicTitle, issue , publisherName, valuation
-- FROM Comic C ,publisher P;
-- WHERE  valuation > 300
-- GROUP BY comicTitle; 


SELECT characterName, COUNT(valuation) + 300 AS 'Total Valuation'
FROM CharacterInfo CI ,Comic C;
WHERE characterName == %Duck%; 
