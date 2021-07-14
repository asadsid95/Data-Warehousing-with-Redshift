# Project: Data Warehousing with Redshift

## Background

Note: This project builds onto the client, Sparkify's evolving requirements from project 1 and 2.

In previous projects, Sparkify wanted a Postgres/Cassandra database (the data was assumed to be stored in local directories), and ETL pipeline. This was in pursuit to understand what their songs users were listening by being able to query their data *which had been transformed for cleaning purpose*, however they like.   

**Now**, Sparkify's data storage and infrastructure have evolved. Before their data was assumed to be stored locally. Now, their data resides in the cloud, on Amazon S3. Sparkify's overarching requirement remains the same, of being able to find insights in what songs their users are listening to.   


For this project, the Data Engineering team is tasked with building an ETL pipeline to extract their data from S3, stage it in Amazon Redshift, and then  transform and place it into a Star Schema (consisting of fact and dimensional tables). 
This would circle back into the overarching requirement as it enables the Analytics team to continue finding insights of what songs their users are listening to.


Data Engineering team will be conducting 2 tasks: 

1. Create table schemas to include 4 dimensions and 1 fact table (Star schema)
2. Write ETL pipeline to extract, transform and load data from 2 local directories (data/song_data and data/log_data) into these tables   

## Database Schema Design 

Star schema design is chosen for this project to allow for JOIN operations needed for its fact table from dimension tables.

**Before describing fact & dimensions tables, 2 staging tables are described:**

### Staging table's attributes/columns, data types are as follows:

Name of table: staging_events
Attribute/Data-Type/Constraints (if applicable):

*JSON path file is provided for this table, in S3*

- artist VARCHAR
- auth VARCHAR
- firstName VARCHAR
- gender VARCHAR
- itemInSession INTEGER
- lastName VARCHAR
- length NUMERIC
- level VARCHAR
- location VARCHAR
- method VARCHAR
- page VARCHAR
- registration FLOAT
- sessionId INTEGER
- song VARCHAR
- status INTEGER
- ts BIGINT
- userAgent VARCHAR
- userId VARCHAR

Name of table: staging_songs
Attribute/Data-Type/Constraints (if applicable):

- num_songs INTEGER
- artist_id VARCHAR
- artist_latitude FLOAT
- artist_longitude FLOAT
- artist_location VARCHAR
- artist_name VARCHAR
- song_id VARCHAR
- title VARCHAR
- duration FLOAT
- year INTEGER

### Fact table's attributes/columns, data types and constraints are as follows:

Name of table: songplays
Attribute/Data-Type/Constraints (if applicable):

*\* Similar to 'SERIAL' in Postgres for auto-incremental values, 'IDENTITY' is used by Reshift of which (0,1) describes the starting value 0 with an increment of 1.
Also, IDENTITY implies column are NOT NULL by default like Postgres's SERIAL*

- songplay_id BIGINT IDENTITY(0,1) PRIMARY KEY \*
- start_time TIMESTAMP
- user_id VARCHAR
- level VARCHAR
- song_id VARCHAR
- artist_id VARCHAR
- sessionId INTEGER
- artist_location VARCHAR
- userAgent VARCHAR 

### Dimension tables' attributes/columns, data types and constraints are as follows:

Name of table: users
Attribute/Data-Type/Constraints (if applicable):

- user_id VARCHAR NOT NULL PRIMARY KEY
- firstName VARCHAR
- lastName VARCHAR
- gender VARCHAR
- level VARCHAR

Name of table: songs
Attribute/Data-Type/Constraints (if applicable):

- song_id VARCHAR NOT NULL PRIMARY KEY
- title VARCHAR
- artist_id VARCHAR
- year INTEGER
- duration FLOAT

Name of table: artists
Attribute/Data-Type/Constraints (if applicable):

- artist_id VARCHAR NOT NULL PRIMARY KEY
- artist_name VARCHAR
- artist_location VARCHAR
- artist_latitude FLOAT
- artist_longitude FLOAT

Name of table: time
Attribute/Data-Type/Constraints (if applicable):

- start_time TIMESTAMP NOT NULL PRIMARY KEY
- hour INTEGER
- day VARCHAR
- week INTEGER
- month INTEGER
- year INTEGER
- weekday VARCHAR

## How to run the scripts

To run this project:

*It is assumed that IAM role and Redshift cluster have been created and connected to. This project was conducted using code rather than 'click-and-fill' method to connect to Redshift and other clients.*

1. Run create_tables.py
2. Run etl.py

## Curiosity question
 *I tend to think of how I would perform work in a setting where collcboration takes place across various roles and teams

1. Assuming Analytics team may not know what data they require in the beginning, how can Data Engineering teams collaborate to effectively provide data?
