CREATE TABLE main (
  IDX SMALLINT(1) NOT NULL AUTO_INCREMENT,
  URL VARCHAR(2083) NOT NULL,
  PRIMARY KEY (`IDX`));

create table object(
	단어 varchar(20) not null primary key,
    idx varchar(500));
    
create table action(
	단어 varchar(20) not null primary key,
    idx varchar(500));
    
create table emotion(
	단어 varchar(20) not null primary key,
    idx varchar(500));
