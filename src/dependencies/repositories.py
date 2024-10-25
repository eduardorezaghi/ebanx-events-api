from src.repositories import BalanceRepository

# This is the in-memory datastore embedded within the Python process for FastAPI, to at least simulate a database.
# I would use a NoSQL database like TinyDB, Mongo or Redis to keep O(1) time complexity for read/write operations.
# If relational data is needed, I would use SQLite or PostgreSQL.
global_balance_repo = BalanceRepository()


def get_balance_repository():
    yield global_balance_repo
