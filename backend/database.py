from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def init_db():
    from models.service import Service  

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    if db.query(Service).count() == 0:
        default_services = [
            Service(name="Website Development", description="Creation of a corporate or landing page website"),
            Service(name="SEO Promotion", description="Website optimization for search engines"),
            Service(name="SMM", description="Brand promotion on social media"),
        ]
        db.add_all(default_services)
        db.commit()
    db.close()
