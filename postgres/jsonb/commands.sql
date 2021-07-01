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

SELECT jsonb_array_elements_text(data->'hobbies') AS hobbies  FROM emp;
SELECT distinct(jsonb_array_elements_text(data->'hobbies')) AS hobbies  FROM emp;

SELECT emp_id, jsonb_array_elements_text(data->'hobbies') AS hobbies  FROM emp;

SELECT emp_id, data FROM emp WHERE data->'hobbies' @> '["Gaming"]'::jsonb; 
SELECT emp_id, data FROM emp WHERE data->'hobbies' @> '["Movies"]'::jsonb; 


drop table emp;




