from app.database.models.sync_engine import sync_engine
from sqlalchemy.orm import sessionmaker


sync_session = sessionmaker(bind=sync_engine)
