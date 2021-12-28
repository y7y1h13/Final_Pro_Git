CREATE TABLE main (
  IDX SMALLINT(1) NOT NULL AUTO_INCREMENT,
  URL VARCHAR(2083) NOT NULL,
  PRIMARY KEY (`IDX`));

create table object(
	단어 varchar(20) not null primary key,
    idx JSON null);
    
create table action(
	단어 varchar(20) not null primary key,
    idx JSON null);
    
create table emotion(
	단어 varchar(20) not null primary key,
    idx JSON null);
    
    
-- emotion table    
    
   
    
insert into emotion (단어,idx) values ('기쁨', json_array(5,6));
insert into emotion (단어,idx) values ('낙담한', json_array(17));
insert into emotion (단어,idx) values ('눈밀이 나는',json_array(9,11,19));
insert into emotion (단어,idx) values ('느긋한', json_array(5));
insert into emotion (단어,idx) values ('당혹스러운',json_array(22));
insert into emotion (단어,idx) values ('두려운',json_array(4));
insert into emotion (단어,idx) values ('분노',json_array(1,2,3,22));
insert into emotion (단어,idx) values ('불안',json_array(4));
insert into emotion (단어,idx) values ('비통한',json_array(14,15,19));
insert into emotion (단어,idx) values ('상처',json_array(8));
insert into emotion (단어,idx) values ('성가신',json_array(3));
insert into emotion (단어,idx) values ('슬픔',json_array(9,14,15,16));
insert into emotion (단어,idx) values ('신이 난',json_array(6));
insert into emotion (단어,idx) values ('우울한',json_array(16,17));
insert into emotion (단어,idx) values ('짜증나는',json_array(1,2));
insert into emotion (단어,idx) values ('혼란스러운',json_array(18));
    
    
    
-- action table    
    
insert into action (단어,idx) values ('귀엽',json_array(16));
insert into action (단어,idx) values ('기어가',json_array(16));
insert into action (단어,idx) values ('깨',json_array(21));
insert into action (단어,idx) values ('나대',json_array(2));
insert into action (단어,idx) values ('놀라',json_array(18));
insert into action (단어,idx) values ('먹',json_array(20));
insert into action (단어,idx) values ('묻히',json_array(14));
insert into action (단어,idx) values ('부리',json_array(3,19));
insert into action (단어,idx) values ('서운',json_array(17));
insert into action (단어,idx) values ('섭섭',json_array(17));
insert into action (단어,idx) values ('안타깝',json_array(15));
insert into action (단어,idx) values ('열',json_array(19));
insert into action (단어,idx) values ('울',json_array(11,14,15));
insert into action (단어,idx) values ('웃',json_array(5));
insert into action (단어,idx) values ('일어나',json_array(21));
insert into action (단어,idx) values ('자',json_array(21));
insert into action (단어,idx) values ('짠히',json_array(15));
insert into action (단어,idx) values ('파묻히',json_array(14));
-- object table
insert into object (단어,idx) values ('개구리',json_array(11));
insert into object (단어,idx) values ('권총',json_array(1,10,11,12,13));
insert into object (단어,idx) values ('기운',json_array(4));
insert into object (단어,idx) values ('눈물',json_array(9,11,14,15,16));
insert into object (단어,idx) values ('당황',json_array(18));
insert into object (단어,idx) values ('먹방',json_array(20));
insert into object (단어,idx) values ('멘붕',json_array(22));
insert into object (단어,idx) values ('문',json_array(17));
insert into object (단어,idx) values ('선글라스',json_array(7));
insert into object (단어,idx) values ('에비츄',json_array(14,15,16,17,18,19,20,21,22));
insert into object (단어,idx) values ('웃음',json_array(5));
insert into object (단어,idx) values ('웨딩드레스',json_array(6));
insert into object (단어,idx) values ('잠',json_array(21));
insert into object (단어,idx) values ('전광렬',json_array(12));
insert into object (단어,idx) values ('절규',json_array(8));
insert into object (단어,idx) values ('정보석',json_array(10));
insert into object (단어,idx) values ('최민수',json_array(1,2,3,4,5,6,7,8,9));
insert into object (단어,idx) values ('투정',json_array(19));
insert into object (단어,idx) values ('폭식',json_array(20));
insert into object (단어,idx) values ('허세',json_array(3));
insert into object (단어,idx) values ('화생방',json_array(7));
-- main table-- 
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2015/03/85_55169c8522e98_1104.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2015/03/90_55169be836487_2752.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2015/04/20150402_551cd9aaacbf2.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('http://image.fmkorea.com/files/attach/new/20161105/486616/403814545/500519276/09c712bccc121896e3d9325c22575cba.PNG
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://i2.ruliweb.com/ori/19/04/12/16a10dd4c834ceb9f.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('http://file3.instiz.net/data/file3/2018/03/16/1/b/3/1b3e9717110340230e231557e20b3b09.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://i.imgur.com/b8XvmnP.gif
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://ohfun.net/contents/article/images/2019/0201/1549000316896142.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('http://file3.instiz.net/data/file3/2020/03/14/6/f/b/6fbb7943b3ef1f471b16c5fed25772aa.gif
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/view/%EA%B6%8C%EC%B4%9D/7490
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/view/%EA%B6%8C%EC%B4%9D/3582
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/view/%EA%B6%8C%EC%B4%9D/3560
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://img3.yna.co.kr/etc/inner/KR/2021/01/22/AKR20210122152851004_02_i_P4.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2017/12/20171209_5a2ad145ebf54.gif
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2016/08/20160818_57b542341b63f.jpg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2016/08/20160818_57b5426a26694.gif
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2020/10/20201031_5f9d63cc61901.jpeg
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2015/03/89_55169e24c389e_1599.png
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2020/09/20200913_5f5dfec85f7e7.gif
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2020/09/20200921_5f68ccc551abf.gif
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2016/08/20160818_57b5428f94d55.gif
');
INSERT INTO `chat`.`main` (`URL`) VALUES ('https://jjalbang.today/files/jjalbox/2016/09/20160910_57d3b07768682.jpg
');


