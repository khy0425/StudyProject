BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY,     username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'KimHoYoung','osu355@gmail.com','010-7556-0317','github.com/khy0425','2020-12-13 19: 22: 54');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-7556-0317','github.com/park','2020-12-13 19: 22: 54');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-1111-1111','Lee.com','2020-12-13 19: 22: 54');
INSERT INTO "users" VALUES(4,'Cho','chodaum.net','010-2222-2222','Cho.com','2020-12-13 19: 22: 54');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@google.com','010-3333-3333','Yoo.net','2020-12-13 19: 22: 54');
COMMIT;
