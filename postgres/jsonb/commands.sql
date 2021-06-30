CREATE TABLE emp (  
  emp_id int NOT NULL,
  data jsonb
);

INSERT INTO emp VALUES 
(1, '{"name": "John", "hobbies": ["Movies", "Football", "Hiking"]}');  

INSERT INTO emp VALUES 
(2, '{"name": "Marc", "hobbies": ["Gaming", "Movies", "Music"]}');  



select data from emp;
select data->'name' from emp;
SELECT * FROM emp WHERE data->'name' = '"Marc"'; 
select data->'hobbies' from emp;
SELECT data->'hobbies' FROM emp WHERE data->'name' = '"Marc"';


