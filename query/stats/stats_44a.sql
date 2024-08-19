SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 users as u 
WHERE pl.RelatedPostId = p.Id 
AND u.Id= c.UserId 
AND c.PostId = p.Id 
AND ph.PostId = p.Id 
AND c.CreationDate>='2010-07-11 12:25:05'::timestamp 
AND c.CreationDate<='2014-09-11 13:43:09'::timestamp 
AND p.CommentCount>=0 
AND p.CommentCount<=14 
AND pl.LinkTypeId=1 
AND ph.CreationDate>='2010-08-06 03:14:53'::timestamp 
AND u.Reputation>=1 
AND u.Reputation<=491 
AND u.DownVotes>=0 
AND u.DownVotes<=0;