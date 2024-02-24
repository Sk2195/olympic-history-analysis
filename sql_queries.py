# DROP TABLES
athlete_table_drop = 'DROP TABLE IF EXISTS athlete;'
noc_regions_table_drop = 'DROP TABLE IF EXISTS noc_regions;'

# CREATE TABLE queries
athlete_table_create = """
CREATE TABLE IF NOT EXISTS athlete (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255),
    Sex VARCHAR(1),
    Age FLOAT,
    Height FLOAT,
    Weight FLOAT,
    Team VARCHAR(255),
    NOC VARCHAR(3),
    Year VARCHAR(255),
    Season VARCHAR(255),
    City VARCHAR(255),
    Sport VARCHAR(255),
    Event VARCHAR(255),
    Medal VARCHAR(255)
);
"""

noc_regions_table_create = """
CREATE TABLE IF NOT EXISTS noc_regions (
    noc VARCHAR(3) PRIMARY KEY,
    region VARCHAR(255),
    notes TEXT
);
"""

# INSERT INTO queries
# INSERT INTO queries
athlete_table_insert = """
INSERT INTO athlete (ID, Name, Sex, Age, Height, Weight, Team, NOC, Year, Season, City, Sport, Event, Medal)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (ID) DO NOTHING;
"""

noc_regions_table_insert = """
INSERT INTO noc_regions (noc, region, notes)
VALUES (%s, %s, %s)
ON CONFLICT (noc) DO NOTHING;
"""

# Lists to manage the creation and dropping of tables
create_table_queries = [athlete_table_create, noc_regions_table_create]
drop_table_queries = [athlete_table_drop, noc_regions_table_drop]

