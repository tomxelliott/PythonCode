import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2009, season_type='Regular')
for pp in q.sort('rushing_yds').limit(10).as_aggregate():
        print pp.player, pp.rushing_yds

# this code will print out the 10 running backs with the highest rushing yards in the 2009 regular season. 
