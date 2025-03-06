

SELECT comicTitle, issue , publisherName ,valuation
FROM Comic C
JOIN Publisher P ON P.publisherID = C.publisherID
WHERE valuation >= (

        SELECT AVG(valuation) 
        FROM Comic
        )+ 300;



SELECT characterName, SUM(valuation) AS TotalValuation 
FROM CharacterInfo CI
JOIN ComicCharacter CC ON CI.characterID = CC.characterID
 JOIN Comic C  ON CC.comicID = C.comicID 
 WHERE characterName LIKE '%Duck%'
  GROUP BY characterName 
  ORDER BY TotalValuation DESC;

SELECT comicTitle, issue, publisherName, (valuation * 2) AS "Double Price"
FROM Comic 
JOIN Publisher ON Comic.publisherID = Publisher.publisherID 
JOIN Series ON Comic.seriesID = Series.seriesID
 JOIN ComicCharacter ON Comic.comicID = ComicCharacter.comicID 
JOIN CharacterInfo ON ComicCharacter.characterID = CharacterInfo.characterID 
WHERE Series.seriesName = 'The OK Seven' 
AND characterName = 'Starlordly';
