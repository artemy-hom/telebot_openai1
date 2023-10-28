import datetime
from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


#--------
#Не забывай коментить идиотина
#А то потом опять забудешь зачем всё это делал 💀💀💀
#--------

Base = declarative_base()

#Table with users in it 
class User(Base):
    __tablename__ = "users"
    #Telegram unique user id 
    user_id: Mapped[int] = mapped_column(primary_key=True)
    #Telegram user name
    username: Mapped[str] = mapped_column(String(30))
    #Register date
    reg_date: Mapped[DATE] = mapped_column(DATE, default=datetime.date.today())
    #Last update date
    up_date: Mapped[DATE] = mapped_column(DATE, onupdate=datetime.date.today())

    #Just debug function
    def __str__(self) -> str:
        return f"<User:{self.user_id}"

