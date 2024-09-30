CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    phone_number TEXT,	-- User's primary phone number
    created_at TEXT DEFAULT CURRENT_TIMESTAMP -- ISO 8601 format
);

CREATE TABLE contacts (
    contact_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL, -- FK
    title TEXT,
    phone_number TEXT,
    address TEXT,
    country TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (full_name, email, phone_number) VALUES
('Alice Johnson', 'alice@example.com', '123-456-7890'),
('Bob Smith', 'bob@example.com', '987-654-3210'),
('Charlie Brown', 'charlie@example.com', '555-123-4567'),
('David Lee', 'david@example.com', '777-888-9999'),
('Emily Davis', 'emily@example.com', '444-555-6666'),
('Frank Thomas', 'frank@example.com', '333-222-1111'),
('Grace Adams', 'grace@example.com', '000-111-2222'),
('Henry Baker', 'henry@example.com', '777-777-7777'),
('Ivy Clark', 'ivy@example.com', '666-666-6666'),
('Jack Wilson', 'jack@example.com', '555-555-5555');

INSERT INTO contacts (user_id, title, phone_number, address, country) VALUES
(1, 'home', '111-222-3333', '123 Main St, Cityville, USA', 'United States'),
(1, 'home', '444-555-6666', '456 Elm St, Townville, USA', 'United States'),
(2, 'home', '777-888-9999', '789 Oak St, Countryville, USA', 'United States'),
(3, 'home', '333-222-1111', '101 Pine St, Villageville, USA', 'United States'),
(4, 'work', '555-123-4567', '234 Maple St, Cityville, USA', 'United States'),
(5, 'work', '987-654-3210', '567 Willow St, Townville, USA', 'United States'),
(6, 'work', '123-456-7890', '890 Cedar St, Countryville, USA', 'United States'),
(7, 'work', '777-777-7777', '111 Main St, Cityville, USA', 'United States'),
(8, 'work', '666-666-6666', '222 Elm St, Townville, USA', 'United States'),
(9, 'home', '555-555-5555', '333 Oak St, Countryville, USA', 'United States'),
(10, 'home', '444-555-6666', '456 Maple St, Cityville, USA', 'United States');


-- SELECT users.full_name, contacts.country 
-- FROM contacts 
-- INNER JOIN users ON contacts.user_id = users.user_id;