from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from database import Base
import datetime
import collections

class Plot(Base):
  __tablename__ = 'plots'
  id = Column(Integer, primary_key=True)
  title = Column(String(80))
  xlabel = Column(String(80))
  xvar =  Column(String(80))
  yvars = Column(String(260))
  ylabel = Column(String(80))
  query = Column(Text())
  created_at = Column(DateTime)
  num_series = Column(Integer )
  page = Column(String(80))
  graph_type = Column(String(80))

  def __init__(self, title, xlabel, ylabel, query, num_series, page, graph_type, xvar, yvars):
    self.title = title
    self.xlabel = xlabel
    self.ylabel = ylabel
    self.query = query
    self.num_series = num_series
    self.created_at = datetime.datetime.utcnow()
    self.page = page
    self.graph_type = graph_type
    self.xvar = xvar
    self.yvars = yvars
    
  def exec_query(self, db_session):
    result = db_session.execute(self.query)
    self.data = collections.defaultdict(list)
    for row in result:
      for column, value in row.items():
        self.data[column].append(value)

  def __repr__(self):
    return '<plot %r>' % self.id


  
