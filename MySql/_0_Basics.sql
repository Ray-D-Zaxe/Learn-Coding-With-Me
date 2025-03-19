-- This is a comment



-- @block
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);



-- @block
INSERT INTO Users(email, bio, country)
VALUES ("example@123.com", "I love strangers.", 'IN'),
("example@456.com", "I like strangers.", 'US'),
("example@789.com", "I hate strangers.", 'JP');



-- To read the entire table
-- @block
SELECT * FROM Users;



-- To read a specific column
-- @block
SELECT email, ID FROM Users;



-- @block
SELECT email, ID FROM users
LIMIT 2;



-- @block
SELECT email, ID FROM users
ORDER BY id ASC -- or DESC for descending order
LIMIT 2;



-- @block
SELECT email, ID FROM users
WHERE country = 'JP'
ORDER BY id ASC
LIMIT 2;



-- @block
SELECT email, ID FROM users
WHERE country = 'JP'
AND id > 1
ORDER BY id ASC
LIMIT 2;



-- @block
SELECT email, ID FROM users
WHERE email LIKE '%3.com' -- where the email ends with 3.com
ORDER BY id ASC
LIMIT 2;



-- @block
SELECT email, ID FROM users
WHERE country = 'JP'
AND email LIKE 'exa%' -- where the email ends with exa
ORDER BY id ASC
LIMIT 2;



-- Creating an index based on the email coloum of the Users table
-- It should help make email based pattern queries faster
-- @block
CREATE INDEX emailIndex ON Users(email);



-- @block
CREATE TABLE Rooms(
    id INT AUTO_INCREMENT,
    street VARCHAR(255),
    owner_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id) REFERENCES Users(id)
);



-- @block
INSERT INTO Rooms(owner_id, street)
VALUES
    (1, "Main Street"),
    (1, 'Blue Heaven'),
    (1, "Golden Carnival"),
    (1, "Roasted Harvest");



-- @block
SELECT * FROM Rooms;



-- Using INNER JOIN only shows users who have rooms
-- @block
SELECT * FROM Users
INNER JOIN Rooms
ON Rooms.owner_id = Users.id;



-- Using LEFT JOIN shows all the users and their rooms if they have any otherwise NULL
-- @block
SELECT * FROM Users
LEFT JOIN Rooms
ON Rooms.owner_id = Users.id;



-- @block
SELECT * FROM Users
RIGHT JOIN Rooms
ON Rooms.owner_id = Users.id;



-- OUTER JOIN is not supported in MySQL
-- SELECT * FROM Users OUTER JOIN Rooms ON Rooms.owner_id = Users.id;



-- @block
SELECT
    Users.id AS user_id,
    Rooms.id AS room_id,
    email,
    street
FROM Users
INNER JOIN Rooms
ON Rooms.owner_id = Users.id;



-- @block
CREATE TABLE Bookings(
    id INT PRIMARY KEY AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATE NOT NULL,
    FOREIGN KEY (guest_id) REFERENCES Users(id),
    FOREIGN KEY (room_id) REFERENCES Rooms(id)
);



-- @block Rooms a user has booked
SELECT
    guest_id,
    street,
    check_in
FROM BOokings
INneR JOIN roOMs
ON ROomS.owner_id = gUESt_id
WHERE guest_id = 1;



-- DROP TABLE Users or DROP DATABASE database_name will deleate these objects
