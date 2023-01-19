CREATE TABLE location (
	id SERIAL PRIMARY KEY,
	continent text,
	country text, 
	city text,
	latitude text,
	longitude text
);

CREATE TABLE forecast (
	id SERIAL PRIMARY KEY,
	location_id int,
	current_datetime timestamp,
	forecast_datetime timestamp, 
	temperature decimal(3,1),
	cloud_area_fraction decimal(4,1),
	humidity decimal(4,1),
	wind_speed decimal(3,1),
	weather_description text,
	precipitation decimal (4,1),
	FOREIGN KEY (location_id) REFERENCES location(id)
);

SELECT * FROM forecast;

INSERT INTO location (continent, country, city, latitude, longitude) 
VALUES
('Europe', 'Norway', 'Svalbard', '78', '17'), 
('Europe', 'Sweden', 'Åkersberga', '59', '18'), 
('Europe', 'Vatican', 'Vatican city', '42', '12'), 
('Africa', 'Tchad', 'N´Djamena', '12', '15'), 
('Africa', 'Congo', 'Kinshasa', '-4', '15'), 
('Africa', 'South Africa', 'Cape town', '-34', '18'), 
('Antarctica', 'Antarctica', 'Princess Elizabeth station', '-72', '23');


