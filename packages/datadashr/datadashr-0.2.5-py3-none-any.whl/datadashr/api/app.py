from robyn import Robyn
from crud import *
from models import engine

app = Robyn(__file__)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def to_dict(obj):
    """
    Convert an SQLAlchemy object to a dictionary.
    """
    if obj is None:
        return None
    return {c.key: getattr(obj, c.key) for c in obj.__table__.columns}


@app.get("/")
def h(request):
    return "Hello, to Datadashr!"


# API Key CRUD
@app.get("/api/v1/keys")
def get_keys(request):
    db = next(get_db())
    keys = get_all_api_keys(db)
    return {"keys": [to_dict(key) for key in keys]}


@app.get("/api/v1/keys/:key_id")
def get_key(request):
    db = next(get_db())
    if key := get_api_key_by_id(db, request.path_params["key_id"]):
        return to_dict(key)
    return {"error": "API key not found"}


@app.post("/api/v1/keys")
def create_key(request):
    db = next(get_db())
    response = create_api_key(db, request.form_data["key"])
    if isinstance(response, dict) and "error" in response:
        return response
    return to_dict(response)


@app.delete("/api/v1/keys/:key_id")
def delete_key(request):
    db = next(get_db())
    if key := delete_api_key(db, request.path_params["key_id"]):
        return {"message": "API key deleted successfully"}
    return {"error": "API key not found"}


@app.put("/api/v1/keys/:key_id")
def update_key(request):
    db = next(get_db())
    if key := update_api_key(
            db, request.path_params["key_id"], request.form_data["key"]
    ):
        return to_dict(key)
    return {"error": "Failed to update API key"}


# Provider CRUD
@app.get("/api/v1/providers")
def get_providers(request):
    db = next(get_db())
    providers = get_all_providers(db)
    return {"providers": [to_dict(provider) for provider in providers]}


@app.get("/api/v1/providers/:provider_id")
def get_provider(request):
    db = next(get_db())
    if provider := get_provider_by_id(db, request.path_params["provider_id"]):
        return to_dict(provider)
    return {"error": "Provider not found"}


@app.post("/api/v1/providers")
def create_provider(request):
    db = next(get_db())
    response = create_provider(db, request.form_data)
    if isinstance(response, dict) and "error" in response:
        return response
    return to_dict(response)


@app.delete("/api/v1/providers/:provider_id")
def delete_provider(request):
    db = next(get_db())
    if provider := delete_provider(db, request.path_params["provider_id"]):
        return {"message": "Provider deleted successfully"}
    return {"error": "Provider not found"}


@app.put("/api/v1/providers/:provider_id")
def update_provider(request):
    db = next(get_db())
    if provider := update_provider(
            db, request.path_params["provider_id"], request.form_data
    ):
        return to_dict(provider)
    return {"error": "Failed to update provider"}


# Connector CRUD
@app.get("/api/v1/connectors")
def get_connectors(request):
    db = next(get_db())
    connectors = get_all_connectors(db)
    return {"connectors": [to_dict(connector) for connector in connectors]}


@app.get("/api/v1/connectors/:connector_id")
def get_connector(request):
    db = next(get_db())
    if connector := get_connector_by_id(db, request.path_params["connector_id"]):
        return to_dict(connector)
    return {"error": "Connector not found"}


@app.post("/api/v1/connectors")
def create_connector(request):
    db = next(get_db())
    response = create_connector(db, request.form_data)
    if isinstance(response, dict) and "error" in response:
        return response
    return to_dict(response)


@app.delete("/api/v1/connectors/:connector_id")
def delete_connector(request):
    db = next(get_db())
    if connector := delete_connector(db, request.path_params["connector_id"]):
        return {"message": "Connector deleted successfully"}
    return {"error": "Connector not found"}


@app.put("/api/v1/connectors/:connector_id")
def update_connector(request):
    db = next(get_db())
    if connector := update_connector(
            db, request.path_params["connector_id"], request.form_data
    ):
        return to_dict(connector)
    return {"error": "Failed to update connector"}


# vector_store CRUD
@app.get("/api/v1/vector_stores")
def get_vector_stores(request):
    db = next(get_db())
    vector_stores = get_all_vector_dbs(db)
    return {"vector_stores": [to_dict(vector_store) for vector_store in vector_stores]}


@app.get("/api/v1/vector_stores/:vector_store_id")
def get_vector_store(request):
    db = next(get_db())
    if vector_store := get_vector_db_by_id(db, request.path_params["vector_store_id"]):
        return to_dict(vector_store)
    return {"error": "Vector store not found"}


@app.post("/api/v1/vector_stores")
def create_vector_store(request):
    db = next(get_db())
    name = request.form_data["name"]
    vector_name = request.form_data["vector_name"]
    vector_params = request.form_data["vector_params"]
    response = create_vector_db(db, name, vector_name, vector_params)
    if isinstance(response, dict) and "error" in response:
        return response
    return to_dict(response)


@app.delete("/api/v1/vector_stores/:vector_store_id")
def delete_vector_store(request):
    db = next(get_db())
    if vector_store := delete_vector_db(db, request.path_params["vector_store_id"]):
        return {"message": "Vector store deleted successfully"}
    return {"error": "Vector store not found"}


@app.put("/api/v1/vector_stores/:vector_store_id")
def update_vector_store(request):
    db = next(get_db())
    name = request.form_data["name"]
    vector_name = request.form_data["vector_name"]
    vector_params = request.form_data["vector_params"]
    if vector_store := update_vector_db(
            db, request.path_params["vector_store_id"], name, vector_name, vector_params
    ):
        return to_dict(vector_store)
    return {"error": "Failed to update vector store"}


app.start()
