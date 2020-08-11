-- Script that prepares a MySQL server for the project:
-- Creates the database hbnb_dev_db
-- Creates a new user hbnb_dev (in localhost) with password hbnb_dev_pwd
-- Grants all privileges to hbnb_dev in the database hbnb_dev_db
-- Grants SELECT privileges to hbnb_dev in the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
