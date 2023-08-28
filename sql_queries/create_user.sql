-- a scripts that creates a user to our database .
-- using famec_01@localhost as the user
-- using famec_01_pwd
-- database name is famec_db
CREATE USER IF NOT EXISTS FAMEC_MYSQL_USER@localhost IDENTIFIED BY 'FAMEC_MYSQL_PWD';
GRANT ALL PRIVILEGES ON *.* TO FAMEC_MYSQL_USER@localhost;