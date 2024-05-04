from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from backend.server.db.database import SqlAlchemyBase


class APIKey(SqlAlchemyBase):
    """
    Describes the API key for AI access
    """

    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)
    """
    The id of the key
    """

    user_id = Column(Integer, ForeignKey("users.id"))
    """
    The ID of the user which owns key
    """

    api_key = Column(String(16384))
    """
    The AI access key
    """


class User(SqlAlchemyBase):
    """
    Describes the user of The Project
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    """
    The id of the user
    """

    user_key = Column(String(8192))
    """
    The user API access key
    """

    api_keys = relationship("APIKey", backref="user")
    """
    The list of api keys of this user
    """