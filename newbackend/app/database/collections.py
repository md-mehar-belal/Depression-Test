from app.database.database import get_db

# ARCHITECTURAL VIOLATION:
# Repository code treated these collection accessors as collection
# objects, even though this layer is responsible for returning
# collections through functions. That boundary mismatch causes runtime
# attribute errors and makes persistence wiring ambiguous.
#
# Legacy problematic shape preserved for traceability:
# def users_collection():
#     db = get_db()
#     return db["users"]
#
# def predictions_collection():
#     db = get_db()
#     return db["predictions"]

def users_collection():
    db = get_db()
    return db["users"]

def predictions_collection():
    db = get_db()
    return db["predictions"]
