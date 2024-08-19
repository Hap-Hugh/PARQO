SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 users as u 
WHERE p.Id = c.PostId 
AND p.Id = pl.RelatedPostId 
AND p.OwnerUserId = u.Id 
AND c.CreationDate>='2010-07-21 11:05:37'::timestamp 
AND c.CreationDate<='2014-08-25 17:59:25'::timestamp 
AND u.UpVotes>=0 
AND u.CreationDate>='2010-08-21 21:27:38'::timestamp;