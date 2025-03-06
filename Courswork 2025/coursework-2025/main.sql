

-- SELECT comicTitle, issue , publisherName ,valuation
-- FROM Comic C
-- JOIN Publisher P ON P.publisherID = C.publisherID
-- WHERE valuation >= (

--         SELECT AVG(valuation) 
--         FROM Comic
--         )+ 300;


-- SELECT characterName, SUM(Valuation) AS "Total Valuation"
-- FROM CharacterInfo CI ,Comic C ,ComicCharacter CC
-- WHERE characterName LIKE "%Duck%" ;


-- SELECT comicTitle, issue, publisherName,(valuation * 2 ) AS "Double Price"
-- FROM Comic C , Series S ,CharacterInfo CI , ComicCharacter CC 
-- Join Publisher P ON C.publisherID = P.publisherID
-- JOIN Series S ON C.seriesID = S.seriesID
-- JOIN ComicCharacter CC ON CI.characterID = CC.characterID
-- WHERE characterName = "Starlodly"
--  AND seriesName = (  SELECT seriesName
--                      FROM Series 
--                      WHERE seriesName = "The OK seven");

-- SELECT comicTitle,startYear,seriesName
-- FROM Series,Comic
-- WHERE startYear = "1980";


SELECT comicTitle , issue, publisherName , (valuation * 2) AS "Double Price"
FROM Comic , Series , CharacterInfo , ComicCharacter
JOIN Publisher ON Comic.publisherID = Publisher.publisherID
JOIN Series ON Comic.seriesID = Series.seriesID
JOIN ComicCharacter ON CharacterInfo.characterID = ComicCharacter.characterID
WHERE characterName = "Starlodly"
 AND seriesName = (  SELECT seriesName
                     FROM Series 
                     WHERE seriesName = "The OK seven");