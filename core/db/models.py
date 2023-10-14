import datetime
from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy.ext.declarative import declarative_base

#--------
#Не забывай коментить идиотина
#А то потом опять забудешь зачем всё это делал 💀💀💀
#--------

Base = declarative_base()

#Table with users in it 
class User(Base):
    __tablename__ = "users"
    #Telegram unique user id 
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    #Telegram user name
    username = Column(String(length=255), nullable=True)
    #Register date
    reg_date = Column(DATE, default=datetime.date.today())
    #Last update date
    up_date = Column(DATE, onupdate=datetime.date.today())

    #Just debug function
    def __str__(self) -> str:
        return f"<User:{self.user_id}"
