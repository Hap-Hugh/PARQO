SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 votes as v,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND p.Id = v.PostId 
AND p.Id = c.PostId 
AND c.Score=0 
AND c.CreationDate<='2014-09-10 02:47:53'::timestamp 
AND p.Score>=0 
AND p.Score<=19 
AND p.CommentCount<=10 
AND p.CreationDate<='2014-08-28 13:31:33'::timestamp 
AND v.CreationDate<='2014-09-12 00:00:00'::timestamp 
AND u.DownVotes>=0;