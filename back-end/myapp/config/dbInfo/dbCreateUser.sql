-- Create user and set password
CREATE USER `www-data`@`localhost` IDENTIFIED WITH mysql_native_password BY 'web123@@!';
-- User can only touch test2 database
GRANT Delete, Insert, Select, Update ON test2.* TO `www-data`@`localhost`;