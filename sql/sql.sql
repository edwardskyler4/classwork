CREATE DATABASE puppy;

USE puppy;

CREATE TABLE puppy (
	puppy_id INT PRIMARY KEY,
    puppy_name VARCHAR (20),
    kennel_id INT,
    breed_id INT,
	FOREIGN KEY (kennel_id) REFERENCES kennel(kennel_id),
    FOREIGN KEY (breed_id) REFERENCES breed(breed_id)
);

CREATE TABLE kennel (
	kennel_id INT PRIMARY KEY,
    kennel_name VARCHAR (30),
    location VARCHAR (50)
);

CREATE TABLE breed (
	breed_id INT PRIMARY KEY,
    breed_name VARCHAR (30)
);

CREATE TABLE trick (
	trick_id INT PRIMARY KEY,
    trick_name VARCHAR (20)
);

CREATE TABLE puppy_trick_skill (
	puppy_id INT,
    trick_id INT,
	FOREIGN KEY (puppy_id) REFERENCES puppy(puppy_id),
	FOREIGN KEY (trick_id) REFERENCES trick(trick_id),
    skill_level INT
);

DROP DATABASE puppy_db; 

INSERT INTO kennel
VALUE (1, "Happy Tails", "Madison County")

SELECT * FROM kennel;