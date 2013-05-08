from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from database import Base
import datetime

class Plot(Base):
  __tablename__ = 'web_users'
  id = Column(Integer, primary_key=True)
  title = Column(String(80))
  xlabel = Column(String(80))
  ylabel = Column(String(80))
  query = Column(Text())
  created_at = Column(DateTime)
  num_series = Column(Integer )

  def __init__(self, title, xlabel, ylabel, num_series):
    self.title = title
    self.xlabel = xlabel
    self.ylabel = ylabel
    self.query = query
    self.num_series = num_series
    self.created_at = datetime.datetime.utcnow()

  def __repr__(self):
    return '<User %r>' % self.id

