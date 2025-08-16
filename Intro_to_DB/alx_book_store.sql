-- -----------------------------------------------------
-- Database: alx_book_store
-- -----------------------------------------------------

-- Drop database if it exists
DROP DATABASE IF EXISTS alx_book_store;

-- Create the database
CREATE DATABASE alx_book_store;

-- Use the database
USE alx_book_store;

-- -----------------------------------------------------
-- Table: Authors
-- -----------------------------------------------------
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- -----------------------------------------------------
-- Table: Books
-- -----------------------------------------------------
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- -----------------------------------------------------
-- Table: Customers
-- -----------------------------------------------------
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT
);

-- -----------------------------------------------------
-- Table: Orders
-- -----------------------------------------------------
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- -----------------------------------------------------
-- Table: Order_Details
-- -----------------------------------------------------
CREATE TABLE Order_Details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
