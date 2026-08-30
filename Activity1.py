import sqlite3
import pandas as pd

conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()

cursor.executescript("""
drop table if exists team;
drop table if exists match;
drop table if exists player_match;

create table team (
    team_id  integer primary key,
    team_name text
);

create table match(
    match_id      integer primary key,
    seaason_id    integer,
    match_winner  integer,
    win_margin    integer
);

create table player_match (
    match_id   integer,
    player_id  integer
);

insert into team values
    (1,'chennai super kings'),(2, 'delhi capitals'),
    (3,'decan chargers'),(4, 'delhi daredevils'),
    (5,'mumbai indians'),(6,'kolkata knight riders'),
    (7,'rajasthan royals'),(8,'kings 11 punjab');

insert into match values
    (1,7,5,35),(2,7,5,22),(3,8,5,45),(4,8,5,8),
    (5,8,1,67),(6,8,6,19),(7,9,5,33),(8,9,1,28),
    (9,9,5,12),(10,9,6,55),(11,9,3,38),(12,9,7,4);

insert into player_match values
    (1,101),(1,102),(2,103),(3,101),(4,108),(5,102);

""")
conn.commit()
print('database ready!')


#part 2
tables = pd.read_sql("""select *
    from sqlite_master
    where type ='table';""",conn)
print(tables)

matches = pd.read_sql("""select *
    from match;""",conn)
print(matches)
print('rows and colums:', matches.shape)

#part 3
teams = pd.read_sql("""selct *
    from team;""", conn)
print(teams)

team_names = pd.read_sql("""select team_id, team_name
    from teams;""", conn)
print(team_names)

player_matches = pd.read_sql("""select match_id, player_id
    from player match;""", conn)
print(player_matches)

#part 4
rr_wins = pd.read_sql("""select *
    froim match
    where match_winner == 7;""",conn)
print(rr_wins)

mi_recent = pd.read_sql("""select *
    from match
    where match_winner == 5 and season_id in (8, 9);""",conn)
print(mi_recent)


