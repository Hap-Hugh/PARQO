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
AND p.Score<=21 
AND p.AnswerCount<=3 
AND p.FavoriteCount>=0 
AND v.CreationDate>='2010-07-19 00:00:00'::timestamp 
AND b.Date<='2014-09-11 18:35:08'::timestamp 
AND u.Reputation<=240;