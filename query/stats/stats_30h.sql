SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v 
WHERE p.Id = pl.PostId 
AND p.Id = v.PostId 
AND p.Id = ph.PostId 
AND p.Id = c.PostId 
AND c.CreationDate<='2014-09-10 02:42:35'::timestamp 
AND p.Score>=-1 
AND p.ViewCount<=5896 
AND p.AnswerCount>=0 
AND p.CreationDate>='2010-07-29 15:57:21'::timestamp 
AND v.VoteTypeId=2;