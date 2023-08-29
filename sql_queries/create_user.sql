-- a scripts that creates a user to our database .
-- using FAMEC_MYSQL_USER@localhost as the user
-- using FAMEC_MYSQL_PWD
-- database name is FAMEC_DB
CREATE USER IF NOT EXISTS FAMEC_MYSQL_USER@localhost IDENTIFIED BY 'FAMEC_MYSQL_PWD';
GRANT ALL PRIVILEGES ON *.* TO FAMEC_MYSQL_USER@localhost;