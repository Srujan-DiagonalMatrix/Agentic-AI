from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

# Connection manager to Postgres
engine = create_engine(url=settings.database_url,
                       echo=True)

# creates DB session for your code.
sessionLocal = sessionmaker(bind=engine,
             autoflush=False,
             expire_on_commit=False
             )