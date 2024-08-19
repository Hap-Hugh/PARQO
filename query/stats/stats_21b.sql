SELECT COUNT(*) 
FROM votes as v,
 posts as p,
 badges as b,
 users as u 
WHERE p.Id = v.PostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND v.CreationDate<='2014-09-12 00:00:00'::timestamp 
AND p.PostTypeId=1 
AND p.Score>=-1 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=20 
AND b.Date>='2010-07-20 19:02:22'::timestamp 
AND b.Date<='2014-09-03 23:36:09'::timestamp 
AND u.DownVotes<=2 
AND u.UpVotes>=0 
AND u.CreationDate>='2010-11-26 03:34:11'::timestamp;