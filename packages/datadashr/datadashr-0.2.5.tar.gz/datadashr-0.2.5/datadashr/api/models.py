import os
import json

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float, Sequence, func
from sqlalchemy.orm import declarative_base
from datetime import datetime

DATABASE_URL = "sqlite:///datadashr_app.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class APIKey(Base):
    """
    APIKey is a SQLAlchemy model class that represents an API key.
    """
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    key = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Provider(Base):
    """
    Provider is a SQLAlchemy model class that represents a data provider.
    """
    __tablename__ = "providers"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True)
    service_endpoint = Column(String, unique=True, index=True)
    api_key = Column(String, index=True)
    model = Column(String, index=True)
    model_token_limits = Column(Integer, index=True)
    model_type = Column(String, index=True)  # e.g. chat, data, embeddings
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Connectors(Base):
    """
    Connectors is a SQLAlchemy model class that represents data connectors.
    """
    __tablename__ = "connectors"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True)
    connection_type = Column(String, index=True)  # e.g. sql, api, file
    connection_params = Column(Text, index=True)  # Use Text to store JSON as string
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def set_connection_params(self, params):
        """
        Set the connection parameters as a JSON string.
        :param params:
        :return:
        """
        self.connection_params = json.dumps(params)

    def get_connection_params(self):
        """
        Get the connection parameters as a JSON object.
        :return:
        """
        return json.loads(self.connection_params)


class VectorDB(Base):
    """
    VectorDB is a SQLAlchemy model class that represents a vector database.
    """
    __tablename__ = "vector_db"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True)
    vector_name = Column(String, index=True)  # e.g. pinecone, faiss, chromadb
    vector_params = Column(Text, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def set_vector_params(self, params):
        """
        Set the vector parameters as a JSON string.
        :param params:
        :return:
        """
        self.vector_params = json.dumps(params)

    def get_vector_params(self):
        """
        Get the vector parameters as a JSON object.
        :return:
        """
        return json.loads(self.vector_params)


# Create the tables if they do not exist
Base.metadata.create_all(bind=engine)
