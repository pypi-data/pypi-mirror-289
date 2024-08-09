from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import APIKey, Provider, Connectors, VectorDB, engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# CRUD operations for API keys
def create_api_key(db: Session, key: str):
    try:
        api_key = APIKey(key=key)
        db.add(api_key)
        db.commit()
        db.refresh(api_key)
        return api_key
    except IntegrityError:
        db.rollback()
        return {"error": "API key already exists"}
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating API key: {e}")
        return {"error": "Failed to create API key"}


def get_api_key_by_id(db: Session, api_key_id: int):
    """
    Get an API key by ID.
    :param db: 
    :param api_key_id: 
    :return: 
    """
    try:
        return db.query(APIKey).filter(APIKey.id == api_key_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching API key by ID: {e}")
        return None


def get_all_api_keys(db: Session):
    """
    Get all API keys.
    :param db: 
    :return: 
    """
    try:
        return db.query(APIKey).all()
    except SQLAlchemyError as e:
        print(f"Error fetching all API keys: {e}")
        return []


def get_api_key_by_key(db: Session, key: str):
    """
    Get an API key by key.
    :param db: 
    :param key: 
    :return: 
    """
    try:
        return db.query(APIKey).filter(APIKey.key == key).first()
    except SQLAlchemyError as e:
        print(f"Error fetching API key by key: {e}")
        return None


def delete_api_key(db: Session, api_key_id: int):
    """
    Delete an API key.
    :param db: 
    :param api_key_id: 
    :return: 
    """
    try:
        api_key = db.query(APIKey).filter(APIKey.id == api_key_id).first()
        if api_key:
            db.delete(api_key)
            db.commit()
        return api_key
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting API key: {e}")
        return None


def update_api_key(db: Session, api_key_id: int, new_key: str):
    """
    Update an API key.
    :param db: 
    :param api_key_id: 
    :param new_key: 
    :return: 
    """
    try:
        api_key = db.query(APIKey).filter(APIKey.id == api_key_id).first()
        if api_key:
            api_key.key = new_key
            db.commit()
            db.refresh(api_key)
        return api_key
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating API key: {e}")
        return None


# CRUD operations for providers
def create_provider(db: Session, name: str, service_endpoint: str, api_key: str, model: str, model_token_limits: int,
                    model_type: str):
    """
    Create a provider.
    :param db: 
    :param name: 
    :param service_endpoint: 
    :param api_key: 
    :param model: 
    :param model_token_limits: 
    :param model_type: 
    :return: 
    """
    try:
        provider = Provider(name=name, service_endpoint=service_endpoint, api_key=api_key, model=model,
                            model_token_limits=model_token_limits, model_type=model_type)
        db.add(provider)
        db.commit()
        db.refresh(provider)
        return provider
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating provider: {e}")
        return None


def get_provider_by_id(db: Session, provider_id: int):
    """
    Get a provider by ID.
    :param db: 
    :param provider_id: 
    :return: 
    """
    try:
        return db.query(Provider).filter(Provider.id == provider_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching provider by ID: {e}")
        return None


def get_all_providers(db: Session):
    """
    Get all providers.
    :param db: 
    :return: 
    """
    try:
        return db.query(Provider).all()
    except SQLAlchemyError as e:
        print(f"Error fetching all providers: {e}")
        return []


def get_provider_by_name(db: Session, name: str):
    """
    Get a provider by name.
    :param db: 
    :param name: 
    :return: 
    """
    try:
        return db.query(Provider).filter(Provider.name == name).first()
    except SQLAlchemyError as e:
        print(f"Error fetching provider by name: {e}")
        return None


def delete_provider(db: Session, provider_id: int):
    """
    Delete a provider.
    :param db: 
    :param provider_id: 
    :return: 
    """
    try:
        provider = db.query(Provider).filter(Provider.id == provider_id).first()
        if provider:
            db.delete(provider)
            db.commit()
        return provider
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting provider: {e}")
        return None


def update_provider(db: Session, provider_id: int, new_name: str, new_service_endpoint: str, new_api_key: str,
                    new_model: str, new_model_token_limits: int, new_model_type: str):
    """
    Update a provider.
    :param db: 
    :param provider_id: 
    :param new_name: 
    :param new_service_endpoint: 
    :param new_api_key: 
    :param new_model: 
    :param new_model_token_limits: 
    :param new_model_type: 
    :return: 
    """
    try:
        provider = db.query(Provider).filter(Provider.id == provider_id).first()
        if provider:
            provider.name = new_name
            provider.service_endpoint = new_service_endpoint
            provider.api_key = new_api_key
            provider.model = new_model
            provider.model_token_limits = new_model_token_limits
            provider.model_type = new_model_type
            db.commit()
            db.refresh(provider)
        return provider
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating provider: {e}")
        return None


# CRUD operations for connectors
def create_connector(db: Session, name: str, connection_type: str, connection_params: dict):
    """
    Create a connector.
    :param db: 
    :param name: 
    :param connection_type: 
    :param connection_params: 
    :return: 
    """
    try:
        return _extracted_from_create_connector(
            name, connection_type, connection_params, db
        )
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating connector: {e}")
        return None


def _extracted_from_create_connector(name, connection_type, connection_params, db):
    """
    Helper method to create a connector.
    :param name: 
    :param connection_type: 
    :param connection_params: 
    :param db: 
    :return: 
    """
    connector = Connectors(name=name, connection_type=connection_type)
    connector.set_connection_params(connection_params)
    db.add(connector)
    db.commit()
    db.refresh(connector)
    return connector


def get_connector_by_id(db: Session, connector_id: int):
    """
    Get a connector by ID.
    :param db: 
    :param connector_id: 
    :return: 
    """
    try:
        return db.query(Connectors).filter(Connectors.id == connector_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching connector by ID: {e}")
        return None


def get_all_connectors(db: Session):
    """
    Get all connectors.
    :param db: 
    :return: 
    """
    try:
        return db.query(Connectors).all()
    except SQLAlchemyError as e:
        print(f"Error fetching all connectors: {e}")
        return []


def get_connector_by_name(db: Session, name: str):
    """
    Get a connector by name.
    :param db: 
    :param name: 
    :return: 
    """
    try:
        return db.query(Connectors).filter(Connectors.name == name).first()
    except SQLAlchemyError as e:
        print(f"Error fetching connector by name: {e}")
        return None


def delete_connector(db: Session, connector_id: int):
    """
    Delete a connector.
    :param db: 
    :param connector_id: 
    :return: 
    """
    try:
        connector = db.query(Connectors).filter(Connectors.id == connector_id).first()
        if connector:
            db.delete(connector)
            db.commit()
        return connector
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting connector: {e}")
        return None


def update_connector(db: Session, connector_id: int, new_name: str, new_connection_type: str,
                     new_connection_params: dict):
    """
    Update a connector.
    :param db: 
    :param connector_id: 
    :param new_name: 
    :param new_connection_type: 
    :param new_connection_params: 
    :return: 
    """
    try:
        connector = db.query(Connectors).filter(Connectors.id == connector_id).first()
        if connector:
            connector.name = new_name
            connector.connection_type = new_connection_type
            connector.set_connection_params(new_connection_params)
            db.commit()
            db.refresh(connector)
        return connector
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating connector: {e}")
        return None


# CRUD operations for vector databases
def create_vector_db(db: Session, name: str, vector_name: str, vector_params: dict):
    """
    Create a vector database.
    :param db: 
    :param name: 
    :param vector_name: 
    :param vector_params: 
    :return: 
    """
    try:
        return _extracted_from_create_vector_db(
            name, vector_name, vector_params, db
        )
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating vector database: {e}")
        return None


def _extracted_from_create_vector_db(name, vector_name, vector_params, db):
    vector_db = VectorDB(name=name, vector_name=vector_name)
    vector_db.set_vector_params(vector_params)
    db.add(vector_db)
    db.commit()
    db.refresh(vector_db)
    return vector_db


def get_vector_db_by_id(db: Session, vector_db_id: int):
    """
    Get a vector database by ID.
    :param db: 
    :param vector_db_id: 
    :return: 
    """
    try:
        return db.query(VectorDB).filter(VectorDB.id == vector_db_id).first()
    except SQLAlchemyError as e:
        print(f"Error fetching vector database by ID: {e}")
        return None


def get_all_vector_dbs(db: Session):
    """
    Get all vector databases.
    :param db: 
    :return: 
    """
    try:
        return db.query(VectorDB).all()
    except SQLAlchemyError as e:
        print(f"Error fetching all vector databases: {e}")
        return []


def get_vector_db_by_name(db: Session, name: str):
    """
    Get a vector database by name.
    :param db: 
    :param name: 
    :return: 
    """
    try:
        return db.query(VectorDB).filter(VectorDB.name == name).first()
    except SQLAlchemyError as e:
        print(f"Error fetching vector database by name: {e}")
        return None


def delete_vector_db(db: Session, vector_db_id: int):
    """
    Delete a vector database.
    :param db: 
    :param vector_db_id: 
    :return: 
    """
    try:
        vector_db = db.query(VectorDB).filter(VectorDB.id == vector_db_id).first()
        if vector_db:
            db.delete(vector_db)
            db.commit()
        return vector_db
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error deleting vector database: {e}")
        return None


def update_vector_db(db: Session, vector_db_id: int, new_name: str, new_vector_name: str, new_vector_params: dict):
    """
    Update a vector database.
    :param db: 
    :param vector_db_id: 
    :param new_name: 
    :param new_vector_name: 
    :param new_vector_params: 
    :return: 
    """
    try:
        vector_db = db.query(VectorDB).filter(VectorDB.id == vector_db_id).first()
        if vector_db:
            vector_db.name = new_name
            vector_db.vector_name = new_vector_name
            vector_db.set_vector_params(new_vector_params)
            db.commit()
            db.refresh(vector_db)
        return vector_db
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error updating vector database: {e}")
        return None
