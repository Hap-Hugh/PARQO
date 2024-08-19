SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u,
 badges as b 
WHERE u.Id = p.OwnerUserId 
AND p.OwnerUserId = ph.UserId 
AND ph.UserId = b.UserId 
AND ph.CreationDate>='2010-09-06 11:41:43'::timestamp 
AND ph.CreationDate<='2014-09-03 16:41:18'::timestamp 
AND p.Score>=-1 
AND p.ViewCount>=0 
AND p.ViewCount<=39097 
AND p.AnswerCount>=0 
AND p.CommentCount>=0 
AND p.CommentCount<=11 
AND p.FavoriteCount<=10 
AND p.CreationDate>='2010-08-13 02:18:09'::timestamp 
AND p.CreationDate<='2014-09-09 10:20:27'::timestamp 
AND u.Views>=0 
AND u.DownVotes>=0 
AND u.DownVotes<=0 
AND u.UpVotes>=0 
AND u.UpVotes<=37;