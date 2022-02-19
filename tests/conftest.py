import mariadb
import os
import pytest


@pytest.fixture(scope="package")
def connected_database():
    conn = mariadb.connect(
        user="root",
        password=os.getenv('DATABASE_PASSWORD'),
        host="127.0.0.1",
        port=3306,
        database="example"
    )
    yield conn
    conn.close()
