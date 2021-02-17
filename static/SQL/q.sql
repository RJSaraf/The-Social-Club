Drop DATABASE login;

insert into persons values (1, 'swift', 'tylor', 'manhatan', 'newyork');

CREATE TABLE Persons
(
PersonID int primary key not null,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
);

create table login 
(
ID int primary key not null,
UserName varchar (20),
Pass_word varchar (20)
)
