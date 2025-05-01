CREATE DATABASE puppy_d;
CREATE TABLE puppies (
	puppy_id INT PRIMARY KEY,
    puppy_name VARCHAR (50),
	FOREIGN KEY (kennel_id) REFERENCES kennel(kennel_id),
    FOREIGN KEY (breed_id) REFERENCES breed(breed_id)
);
