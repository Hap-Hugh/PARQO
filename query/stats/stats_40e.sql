SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND p.Id = v.PostId 
AND p.Id = c.PostId 
AND p.Id = pl.PostId 
AND p.Id = ph.PostId 
AND p.PostTypeId=1 
AND p.AnswerCount>=0 
AND p.CreationDate>='2010-07-21 15:23:53'::timestamp 
AND p.CreationDate<='2014-09-11 23:26:14'::timestamp 
AND pl.CreationDate>='2010-11-16 01:27:37'::timestamp 
AND pl.CreationDate<='2014-08-21 15:25:23'::timestamp 
AND ph.PostHistoryTypeId=5 
AND v.CreationDate>='2010-07-21 00:00:00'::timestamp 
AND u.UpVotes>=0 
AND u.CreationDate<='2014-09-11 20:31:48'::timestamp;