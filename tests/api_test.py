# import mariadb
import sys
import requests


def test_app_for_default_values():
    response = requests.get("http://localhost:80/")
    assert response.status_code == 200
    assert len(response.text.split(",")) == 5


def test_app_after_new_record_inserted(connected_database):
    response = requests.get("http://localhost:80/")
    assert response.status_code == 200

    records_before_changes = len(response.text.split(","))

    cursor = connected_database.cursor()
    cursor.execute('INSERT INTO blog (title) VALUES ("new record")') 
    connected_database.commit()

    response_after_changes = requests.get("http://localhost:80/")
    assert response_after_changes.status_code == 200

    assert len(response_after_changes.text.split(",")) == records_before_changes + 1
