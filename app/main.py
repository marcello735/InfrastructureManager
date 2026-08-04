from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Base, Server


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Infrastructure Manager",
    description="DevOps Infrastructure Management API",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Infrastructure Manager"
    }


@app.get("/servers")
def get_servers(db: Session = Depends(get_db)):
    servers = db.query(Server).all()
    return servers


@app.post("/servers")
def create_server(
    hostname: str,
    ip_address: str,
    operating_system: str,
    status: str,
    db: Session = Depends(get_db)
):
    server = Server(
        hostname=hostname,
        ip_address=ip_address,
        operating_system=operating_system,
        status=status
    )

    db.add(server)
    db.commit()
    db.refresh(server)

    return server
