# # pg vecor, supabase access helper

# import os
# from typing import List, Optional, Tuple, Union

# import numpy as np
# import pandas as pd
# import psycopg2
# from dotenv import load_dotenv
# from psycopg2 import sql
# from psycopg2.extensions import connection, cursor

# load_dotenv()

# # Constants
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")


# def get_db_connection() -> connection:
#     """Establish and return a connection to the PostgreSQL database."""
#     return psycopg2.connect(
#         host=DB_HOST,
#         port=DB_PORT,
#         dbname=DB_NAME,
#         user=DB_USER,
#         password=DB_PASSWORD,
#     )


# def get_db_cursor(conn: connection) -> cursor:
#     """Return a cursor from the given database connection."""
#     return conn.cursor()


# def close_db_connection(conn: connection) -> None:
#     """Close the given database connection."""
#     conn.close()


# def execute_query(
#     conn: connection, query: Union[str, sql.Composed], params: Optional