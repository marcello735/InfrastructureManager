from sqlalchemy import Column, Integer, String

from .database import Base


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String, index=True)
    ip_address = Column(String)
    operating_system = Column(String)
    status = Column(String)
