-- list all cities of California 
SELECT id, name FROM cities
-- subquery for get the id 
    WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
    ORDER by id;