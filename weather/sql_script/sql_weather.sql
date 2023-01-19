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

