SELECT COUNT(*) 
FROM posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 badges as b,
 users as u 
WHERE p.Id = pl.RelatedPostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND u.Id = ph.UserId 
AND u.Id = v.UserId 
AND p.CommentCount>=0 
AND p.CommentCount<=13 
AND ph.PostHistoryTypeId=5 
AND ph.CreationDate<='2014-08-13 09:20:10'::timestamp 
AND v.CreationDate>='2010-07-19 00:00:00'::timestamp 
AND b.Date<='2014-09-09 10:24:35'::timestamp 
AND u.Views>=0 
AND u.DownVotes>=0 
AND u.CreationDate>='2010-08-04 16:59:53'::timestamp 
AND u.CreationDate<='2014-07-22 15:15:22'::timestamp;