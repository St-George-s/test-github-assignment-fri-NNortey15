

SELECT comicTitle, issue , publisherName ,valuation
FROM Comic C ,publisher P
WHERE valuation >= (

        SELECT AVG(valuation) + 300
        FROM Comic
        )
GROUP BY ;

-- SELECT characterName, COUNT(valuation) + 300 AS 'Total Valuation'
-- FROM CharacterInfo CI ,Comic C;
-- WHERE characterName == %Duck%; 
