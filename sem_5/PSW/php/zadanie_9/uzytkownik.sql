CREATE user 'pwr'@'localhost' identified by 'pwr';
GRANT select, insert, update, delete, create, drop, references, execute ON *.* TO 'pwr'@'localhost';
