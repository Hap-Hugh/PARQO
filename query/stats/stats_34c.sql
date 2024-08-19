SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 badges as b,
 users as u 
WHERE u.Id = ph.UserId 
AND u.Id = b.UserId 
AND u.Id = p.OwnerUserId 
AND u.Id = c.UserId 
AND c.Score=0 
AND p.Score>=-2 
AND p.CommentCount>=0 
AND p.CommentCount<=12 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=6 
AND ph.CreationDate<='2014-08-18 08:54:12'::timestamp 
AND u.Views=0 
AND u.DownVotes>=0 
AND u.DownVotes<=60;