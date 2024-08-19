SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND p.Id = v.PostId 
AND p.Id = c.PostId 
AND u.Id = b.UserId 
AND p.Id = ph.PostId 
AND p.AnswerCount>=0 
AND p.CommentCount>=0 
AND b.Date<='2014-09-11 21:46:02'::timestamp 
AND u.Reputation>=1 
AND u.Reputation<=642 
AND u.DownVotes>=0;