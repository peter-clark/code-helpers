-- CONNECT TO COMMAND LINE
-- > mysql -u root -p
-- > use 'database'


-- EXAMPLE
CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT
);

CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

-- #### CONSTRAINTS ####
-- NOT NULL - forces entry to have a value  
-- UNIQUE - forces entry to be unique
-- DEFAULT ____ - if no entry, assign value _____
-- AUTO_INCREMENT - no need to define id every time


-- ON DELETE SET NULL: every entry associated with that employee is set to NULL (including as a foreign key)
-- ON DELETE CASCADE: deletes every row where the instance is deleted (useful when PRIMARY KEYs or anything can't be NULL)


-- % any characters matching, _ 1 character matching
SELECT * FROM branch_supplier
WHERE supplier_name LIKE '% Label%';
--# second % will match any with Label;

SELECT * FROM employee
WHERE birth_day LIKE '____-10%';

-- INT
--DECIMAL (M,N)   - (M-total digits, N-after decimal)
--VARCHAR(N)      - string of length N
--BLOB            - Binary Large Object
--DATE            - 'YYYY-MM-DD'
--TIMESTAMP       - 'YYYY-MM-DD HH:MM:SS'



CREATE TABLE trigger_test (
    message VARCHAR(100)
);


-- BELOW IS WHAT WILL BE PUT INTO COMMAND LINE --

-- TRIGGER trigger_name (BEFORE/AFTER) (INSERT UPDATE DELETE) ON table_name

DELIMITER $$
CREATE
    TRIGGER trigger2 BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END $$
DELIMITER ;
-- The reason you change delimiter for the trigger, is you need the 
-- standard ; delimiter inside of the trigger.

INSERT INTO employee
VALUES(110, 'Kevin', 'Malone', '1969-02-09', 'M', 69000, 106, 3);
SELECT * FROM trigger_test;


DELIMITER $$
CREATE
    TRIGGER trigger3 BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        IF NEW.sex = 'M' THEN
            INSERT INTO trigger_test VALUES(NEW.first_name, 'M');
        ELSEIF NEW.sec= 'F' THEN
            INSERT INTO trigger_test VALUES(NEW.first_name, 'F');
        ELSE
            INSERT INTO trigger_test VALUES(NEW.first_name, 'AYY LMAO');
        END IF; 
    END $$
DELIMITER ;

-- IF Statments must be ended