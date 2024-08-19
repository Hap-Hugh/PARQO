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
AND c.Score=2 
AND p.ViewCount<=7710 
AND p.CommentCount<=12 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=4 
AND p.CreationDate>='2010-07-27 03:58:22'::timestamp 
AND u.UpVotes>=0;