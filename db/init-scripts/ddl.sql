CREATE TABLE users (id SERIAL,
    name char(200) NOT NULL,
    email char(200) NOT NULL,
    phone varchar(200) NOT NULL,
    cell varchar(200) NOT NULL,
    gender varchar(200) NOT NULL,
    nat varchar(200) NOT NULL,
    PRIMARY KEY (id)
);
