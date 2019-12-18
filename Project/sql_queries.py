# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays(
                            songplay_id SERIAL, 
                            start_time TIMESTAMP REFERENCES time(start_time) NOT NULL,
                            user_id VARCHAR(50) REFERENCES users(user_id) NOT NULL,
                            level VARCHAR(50) NOT NULL,
                            song_id VARCHAR(100) REFERENCES songs(song_id),
                            artist_id VARCHAR(100) REFERENCES artists(artist_id),
                            session_id BIGINT NOT NULL,
                            location VARCHAR(255),
                            user_agent TEXT,
                            PRIMARY KEY (songplay_id))""")

user_table_create = ("""CREATE TABLE users(
                        user_id VARCHAR,
                        firstName VARCHAR(255) NOT NULL,
                        lastName VARCHAR(255) NOT NULL,
                        gender VARCHAR(1) NOT NULL,
                        level VARCHAR(50) NOT NULL,
                        PRIMARY KEY (user_id))""")


song_table_create = ("""CREATE TABLE songs(
                        song_id VARCHAR(100),
                        title VARCHAR(255) NOT NULL,
                        artist_id VARCHAR(100) NOT NULL,
                        year INTEGER NOT NULL,
                        duration DOUBLE PRECISION NOT NULL,
                        PRIMARY KEY (song_id))""")


artist_table_create = ("""CREATE TABLE artists(
                          artist_id VARCHAR(100),
                          name VARCHAR(255) NOT NULL,
                          location VARCHAR(255),
                          latitude DOUBLE PRECISION, 
                          longitude DOUBLE PRECISION,
                          PRIMARY KEY (artist_id))""")



time_table_create = ("""CREATE TABLE time(
                        start_time TIMESTAMP, 
                        hour INTEGER NOT NULL,
                        day INTEGER NOT NULL, 
                        week INTEGER NOT NULL, 
                        month INTEGER NOT NULL, 
                        year INTEGER NOT NULL,
                        weekday INTEGER NOT NULL,
                        PRIMARY KEY(start_time))""")
 
# INSERT RECORDS


songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")


user_table_insert = ("""INSERT INTO users (user_id, firstName, lastName, gender, level) 
                        VALUES(%s, %s, %s, %s, %s) 
                        ON CONFLICT (user_id) 
                        DO UPDATE SET firstName=users.firstName, lastName=users.lastName, gender=users.gender, level=users.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE SET title=songs.title, artist_id=songs.artist_id, year=songs.year, duration=songs.duration
""")


artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                          VALUES (%s, %s, %s, %s, %s) 
                          ON CONFLICT (artist_id) 
                          DO UPDATE SET name=artists.name, location=artists.location, latitude=artists.latitude, longitude=artists.longitude""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) 
                        DO UPDATE SET hour=time.hour, day=time.day, week=time.week, month=time.month, year=time.year, weekday=time.weekday
""")

# FIND SONGS
song_select = ("""SELECT s.song_id, a.artist_id 
                  FROM songs s 
                  LEFT JOIN artists a ON a.artist_id = s.artist_id 
                  WHERE s.title = %s 
                      AND a.name = %s 
                      AND s.duration = %s""")


# QUERY LISTS

create_table_queries = [ user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]