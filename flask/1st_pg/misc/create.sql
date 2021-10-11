CREATE TABLE weather2 (
  id SERIAL NOT NULL,
  city  varchar(80),
  temp_lo INTEGER,
  temp_hi INTEGER,
  prcp  REAL,
  date_inputed TIMESTAMP
)
