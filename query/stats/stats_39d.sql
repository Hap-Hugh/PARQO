SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 votes as v,
 badges as b,
 users as u 
WHERE p.Id = c.PostId 
AND p.Id = pl.RelatedPostId 
AND p.Id = v.PostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND c.Score=0 
AND p.AnswerCount>=0 
AND p.AnswerCount<=4 
AND p.CreationDate<='2014-09-12 15:56:19'::timestamp 
AND pl.LinkTypeId=1 
AND pl.CreationDate>='2011-03-07 16:05:24'::timestamp 
AND v.BountyAmount<=100 
AND v.CreationDate>='2009-02-03 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-11 00:00:00'::timestamp 
AND u.Views<=160 
AND u.CreationDate>='2010-07-27 12:58:30'::timestamp 
AND u.CreationDate<='2014-07-12 20:08:07'::timestamp;