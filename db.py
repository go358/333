from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.config import DB_PATH
engine = create_engine(f'sqlite:///{DB_PATH}')
SessionLocal = sessionmaker(bind=engine)
