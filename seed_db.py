from database import db_session
from models import  Plot

p1 = Plot(
    title='Plot 1',
    xlabel='xvar',
    ylabel='yvar',
    query='select a,b,c from data',
    num_series=2,
    page='home',
    graph_type='lineChart',
    xvar='a',
    yvars='b,c'
    )
p2 = Plot(
    title='Plot 2',
    xlabel='xvar',
    ylabel='yvar',
    query='select a,x,y from data',
    num_series=2,
    page='home',
    graph_type='lineChart',
    xvar='a',
    yvars='x,y'
    )
p3 = Plot(
    title='Plot 3',
    xlabel='xvar',
    ylabel='yvar',
    query='select a,z from data',
    num_series=1,
    page='home',
    graph_type='lineChart',
    xvar='a',
    yvars='z'
    )
p4 = Plot(
    title='Plot 4',
    xlabel='xvar',
    ylabel='yvar',
    query='select a,b from data',
    num_series=1,
    page='home',
    graph_type='lineChart',
    xvar='a',
    yvars='b'
    )
p5 = Plot(
    title='Plot 5',
    xlabel='xvar',
    ylabel='yvar',
    query='select a,b,c from data',
    num_series=2,
    page='home',
    graph_type='lineChart',
    xvar='a',
    yvars='b,c'
    )
p6 = Plot(
    title='Plot 6',
    xlabel='xvar',
    ylabel='yvar',
    query='select a,b,c from data',
    num_series=2,
    page='home',
    graph_type='lineChart',
    xvar='a',
    yvars='b,c'
    )





def seed_db():
  db_session.execute('''CREATE TABLE data 
    (a int, b int, c int, 
    x int , y int , z int) ''')
  db_session.execute('''INSERT INTO data VALUES (1,2,3,4,5,6)  ''')
  db_session.execute('''INSERT INTO data VALUES (2,2,3,6,5,10)  ''')
  db_session.execute('''INSERT INTO data VALUES (3,3,3,9,5,12)  ''')
  db_session.execute('''INSERT INTO data VALUES (4,3,2,3,5,14)  ''')
  db_session.execute('''INSERT INTO data VALUES (5,4,2,5,5,16)  ''')
  db_session.execute('''INSERT INTO data VALUES (6,4,2,1,5,18)  ''')
  db_session.execute('''INSERT INTO data VALUES (7,5,1,2,5,16)  ''')
  db_session.execute('''INSERT INTO data VALUES (8,5,1,8,5,16)  ''')
  db_session.execute('''INSERT INTO data VALUES (9,6,1,3,5,12)  ''')
  db_session.execute('''INSERT INTO data VALUES (10,7,1,5,5,10)  ''')
  db_session.execute('''INSERT INTO data VALUES (11,8,0,8,5,6)  ''')
  
  db_session.add_all([p1,p2,p3,p4,p5,p6])
  db_session.commit()

if __name__ == '__main__':
  seed_db()

