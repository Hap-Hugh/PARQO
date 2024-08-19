SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND p.Id = c.PostId 
AND p.Id = ph.PostId 
AND p.Id = v.PostId 
AND c.Score=0 
AND c.CreationDate<='2014-09-09 19:58:29'::timestamp 
AND p.Score>=-4 
AND p.ViewCount>=0 
AND p.ViewCount<=5977 
AND p.AnswerCount<=4 
AND p.CommentCount>=0 
AND p.CommentCount<=11 
AND p.CreationDate>='2011-01-25 08:31:41'::timestamp 
AND u.Reputation<=312 
AND u.DownVotes<=0;