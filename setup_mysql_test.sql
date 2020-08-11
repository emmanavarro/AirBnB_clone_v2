-- Script that prepares a MySQL server for the project:
-- Creates the database hbnb_test_db
-- Creates a new user hbnb_test (in localhost) with password hbnb_test_pwd
-- Grants all privileges to hbnb_test in the database hbnb_test_db
-- Grants SELECT privileges to hbnb_test in the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
