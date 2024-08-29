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

-- This example below solves: Most recent price change before a date, otherwise pricing it 10
WITH Prices AS (
    SELECT
        product_id,
        new_price,
        change_date,
        ROW_NUMBER() OVER (
            PARTITION BY product_id 
            ORDER BY change_date DESC
        ) AS recent -- ranking date by DESC means first row if most recent, used at end
    FROM
        Products
    WHERE
        change_date <= '2019-08-16'
)
SELECT
    p.product_id,
    COALESCE(pr.new_price,10) AS price -- use coalesce to check if price hasnt been set for product id
FROM (
    SELECT DISTINCT 
        product_id 
    FROM 
        Products
    ) p -- we only want each product once
LEFT JOIN 
    Prices pr
    ON pr.product_id = p.product_id
    AND pr.recent = 1;