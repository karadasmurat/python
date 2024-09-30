CREATE TABLE hogwarts_students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    house_id INTEGER,
    std_year INTEGER,
    birthdate DATE,
    gender TEXT,
    patronus_form TEXT,
    FOREIGN KEY (house_id) REFERENCES houses(house_id)
);

CREATE TABLE hogwarts_houses (
    house_id INTEGER PRIMARY KEY,
    name TEXT
);

-- CREATE TABLE house_heads (
--    house_head_id INTEGER PRIMARY KEY,
--    house_id INTEGER,
--    head_of_house TEXT,
--    start_date DATE,
--    end_date DATE,
--    FOREIGN KEY (house_id) REFERENCES houses(house_id)
-- );

INSERT INTO hogwarts_houses (name) VALUES
('Gryffindor'),
('Ravenclaw'),
('Hufflepuff'),
('Slytherin');

-- INSERT INTO house_heads (house_id, head_of_house, start_date, end_date) VALUES
-- (1, 'Minerva McGonagall', '1991-09-01', NULL),
-- (2, 'Filius Flitwick', '1991-09-01', NULL),
-- (3, 'Pomona Sprout', '1991-09-01', NULL),
-- (4, 'Severus Snape', '1991-09-01', '1997-05-02'),
-- (4, 'Horace Slughorn', '1997-05-02', NULL);

INSERT INTO hogwarts_students (first_name, last_name, house_id, std_year, birthdate, gender, patronus_form) VALUES
('Harry', 'Potter', 1, 1, '1980-07-31', 'Male', 'stag'),
('Ron', 'Weasley', 1, 1, '1980-03-01', 'Male', 'jack russell terrier'),
('Hermione', 'Granger', 1, 1, '1979-09-19', 'Female', 'otter'),
('Draco', 'Malfoy', 4, 1, '1980-05-05', 'Male', 'white dove'),
('Luna', 'Lovegood', 2, 1, '1981-13-02', 'Female', 'Thestral'),
('Neville', 'Longbottom', 1, 1, '1980-07-30', 'Male', 'boar'),
('Fred', 'Weasley', 1, 2, '1978-04-01', 'Male', 'jack russell terrier'),
('George', 'Weasley', 1, 2, '1978-04-01', 'Male', 'jack russell terrier'),
('Ginny', 'Weasley', 1, 2, '1979-08-11', 'Female', 'horse'),
('Percy', 'Weasley', 1, 3, '1976-08-22', 'Male', 'rat'),
('Bill', 'Weasley', 1, 4, '1970-11-03', 'Male', 'wolf'),
('Charlie', 'Weasley', 1, 5, '1972-02-12', 'Male', 'dragon'),
('Lavender', 'Brown', 1, 2, '1980-08-14', 'Female', 'rabbit'),
('Parvati', 'Patil', 1, 2, '1980-08-14', 'Female', 'peacock'),
('Dean', 'Thomas', 1, 2, '1980-07-20', 'Male', 'boar'),
('Seamus', 'Finnigan', 1, 2, '1980-08-03', 'Male', 'otter'),
('Cho', 'Chang', 2, 2, '1980-02-17', 'Female', 'swan'),
('Terry', 'Boot', 2, 2, '1980-07-14', 'Male', 'otter'),
('Michael', 'Corner', 2, 2, '1980-08-02', 'Male', 'boar'),
('Padma', 'Patil', 2, 2, '1980-08-14', 'Female', 'peacock'),
('Zacharias', 'Smith', 2, 2, '1980-12-16', 'Male', 'boar'),
('Ernie', 'Macmillan', 3, 2, '1980-11-01', 'Male', 'badger'),
('Hannah', 'Abbott', 3, 2, '1980-04-02', 'Female', 'otter'),
('Justin', 'Finch-Fletchley', 3, 2, '1980-08-05', 'Male', 'boar'),
('Susan', 'Bones', 3, 2, '1980-06-03', 'Female', 'otter');