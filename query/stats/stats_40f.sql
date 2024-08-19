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
AND c.CreationDate>='2010-07-26 19:37:03'::timestamp 
AND p.Score>=-2 
AND p.CommentCount<=18 
AND p.CreationDate>='2010-07-21 13:50:08'::timestamp 
AND p.CreationDate<='2014-09-11 00:53:10'::timestamp 
AND pl.CreationDate<='2014-08-05 18:27:51'::timestamp 
AND ph.CreationDate>='2010-11-27 03:38:45'::timestamp 
AND u.DownVotes>=0 
AND u.UpVotes>=0;