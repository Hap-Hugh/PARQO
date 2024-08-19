SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 users as u 
WHERE p.Id = pl.PostId 
AND p.Id = ph.PostId 
AND p.Id = c.PostId 
AND u.Id = c.UserId 
AND u.Id = v.UserId 
AND c.CreationDate<='2014-09-11 13:24:22'::timestamp 
AND p.PostTypeId=1 
AND p.Score=2 
AND p.FavoriteCount<=12 
AND pl.CreationDate>='2010-08-13 11:42:08'::timestamp 
AND pl.CreationDate<='2014-08-29 00:27:05'::timestamp 
AND ph.CreationDate>='2011-01-03 23:47:35'::timestamp 
AND ph.CreationDate<='2014-09-08 12:48:36'::timestamp 
AND v.CreationDate>='2010-07-27 00:00:00'::timestamp 
AND u.Reputation>=1 
AND u.DownVotes>=0;