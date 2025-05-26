from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, BigInteger

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    name = Column(String)
    role = Column(String, default='client')

engine = create_engine('sqlite:///db.sqlite3')
print("[INIT] Создание таблиц...")
Base.metadata.create_all(bind=engine)
