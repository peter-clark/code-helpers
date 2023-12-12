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
-- ON DELETE CASCADE: deletes every row where the instance is deleted
