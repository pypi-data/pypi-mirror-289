from sqlalchemy import String, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import Mapped, relationship, mapped_column
from datetime import datetime
from .base import Base
from .city import City


class User(Base):
    __tablename__ = 'USER'
    uuid:Mapped[str]= mapped_column(String(255), primary_key=True,unique=True,nullable=False,name='UUID',)
    full_name:Mapped[str]= mapped_column(String(255), nullable=False, name='FULL_NAME')
    gender:Mapped[str]= mapped_column(String(255), name='GENDER')
    birthdate:Mapped[datetime]= mapped_column(DateTime, name='BIRTHDATE')
    email:Mapped[str]= mapped_column(String(255), name='EMAIL')
    cellphone:Mapped[str]= mapped_column(String(255), name='CELLPHONE')
    create_date:Mapped[datetime]= mapped_column(DateTime, name='CREATE_DATE', server_default=func.now())
    last_update_date:Mapped[datetime]= mapped_column(DateTime, name='LAST_UPDATE_DATE', server_default=func.now(), onupdate=func.now())
    nick_name:Mapped[str]= mapped_column(String(255), name='NICK_NAME')
    device_id:Mapped[str]= mapped_column(String(255), name='DEVICE_ID')
    player_id:Mapped[int]= mapped_column(Integer, ForeignKey('PLAYER.ID'), nullable=True,name='PLAYER_ID')
    city_id:Mapped[int]= mapped_column(Integer, ForeignKey('CITY.ID'), name='CITY_ID')

    