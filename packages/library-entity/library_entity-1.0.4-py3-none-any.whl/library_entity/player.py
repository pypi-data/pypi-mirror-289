from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Player(Base):
    __tablename__ = 'PLAYER'
    id:Mapped[int]= mapped_column(Integer,autoincrement=True, primary_key=True,unique=True,nullable=False,name='ID',)
    weight:Mapped[int]= mapped_column(Integer, name='WEIGHT')
    hight:Mapped[int]= mapped_column(Integer, name='HIGHT')
    dorsal_number:Mapped[str]= mapped_column(String(255), name='DORSAL_NUMBER')
    position:Mapped[str]= mapped_column(String(255), name='POSITION')
    skil_ful_foot:Mapped[str]= mapped_column(String(255), name='SKIL_FUL_FOOT')
    