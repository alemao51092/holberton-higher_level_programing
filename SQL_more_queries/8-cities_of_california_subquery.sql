-- list all cities of California 
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER by cities.id ASC;