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
            {"name": "Website Development", "description": "Full-cycle website creation", "price": 1200},
            {"name": "SMM", "description": "Brand promotion on social media", "price": 600},
            {"name": "SEO Optimization", "description": "Improving website ranking in search engines", "price": 800},
            {"name": "Logo Design", "description": "Unique logo for your business", "price": 350},
            {"name": "Mobile App Development", "description": "iOS and Android app creation", "price": 2000},
            {"name": "Technical Support", "description": "Ongoing website and IT support", "price": 300},
            {"name": "Content Writing", "description": "Professional copywriting for your site", "price": 250},
            {"name": "UI/UX Audit", "description": "Analysis and improvement of user experience", "price": 400},
            {"name": "Email Marketing", "description": "Setup and management of email campaigns", "price": 450},
            {"name": "Cloud Migration", "description": "Moving infrastructure to the cloud", "price": 1500},
        ]
        db.add_all([Service(**s) for s in default_services])
        db.commit()
    db.close()
