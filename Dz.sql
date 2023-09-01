CREATE TABLE doctors (
    name VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(10, 2)
);
INSERT INTO doctors (name, position, salary) VALUES ('Врач 1', 'Хирург', 2000.00);
INSERT INTO doctors (name, position, salary) VALUES ('Врач 2', 'Гинеколог', 1800.00);
INSERT INTO doctors (name, position, salary) VALUES ('Врач 3', 'Терапевт', 1500.00);
SELECT name, position, salary FROM doctors WHERE position = 'Хирург';