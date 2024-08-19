SELECT COUNT(*) 
FROM postLinks as pl,
 posts as p,
 users as u,
 badges as b 
WHERE p.Id = pl.RelatedPostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND pl.LinkTypeId=1 
AND p.Score>=-1 
AND p.CommentCount<=8 
AND p.CreationDate>='2010-07-21 12:30:43'::timestamp 
AND p.CreationDate<='2014-09-07 01:11:03'::timestamp 
AND u.Views<=40 
AND u.CreationDate>='2010-07-26 19:11:25'::timestamp 
AND u.CreationDate<='2014-09-11 22:26:42'::timestamp;