SELECT gnomeName, SUM(quantity) 
FROM Gnome G,Gnomepurchase P  
WHERE G.description LIKE "%solar%" 
and G.gnomeid = P.gnomeid 
GROUP BY gnomeName 
ORDER BY sum(quantity) DESC; 

SELECT gnomeID
FROM gnome
WHERE 