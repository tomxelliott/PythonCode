
import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2009, season_type='Regular')
for pp in q.sort('receiving_yds').limit(10).as_aggregate():
        print pp.player, pp.receiving_yds

# this code will print out the 10 wide receivers with the highest receiving yards in the 2009 regular season. 
