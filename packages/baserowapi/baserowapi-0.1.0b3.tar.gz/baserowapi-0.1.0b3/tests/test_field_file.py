import pytest
import os

# File for testing
TEST_FILE_PATH = "./bike.png"
TEST_FILE_URL = "https://www.jimwitte.net/bison.jpg"


# CRUD Operation Tests
def test_create_file_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "FileField": [], "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["FileField"] == []


def test_read_file_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "FileField": [], "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["FileField"] == []


def test_update_file_field_with_local_file(
    baserow_client, test_table, test_row_manager
):
    new_row_data = {"Name": "Test Update Local", "FileField": [], "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    row = test_table.get_row(row_id)
    row.values["FileField"].upload_file_to_server(file_path=TEST_FILE_PATH)
    updated_row = row.update()
    assert len(updated_row["FileField"]) > 0
    assert updated_row["FileField"][0]["visible_name"] == os.path.basename(
        TEST_FILE_PATH
    )


def test_update_file_field_with_url(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update URL", "FileField": [], "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    row = test_table.get_row(row_id)
    row.values["FileField"].upload_file_to_server(url=TEST_FILE_URL)
    updated_row = row.update()
    assert len(updated_row["FileField"]) > 0
    assert updated_row["FileField"][0]["visible_name"] == "bison.jpg"


def test_delete_file_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "FileField": [], "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


def test_download_file(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Download", "FileField": [], "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    row = test_table.get_row(row_id)
    row.values["FileField"].upload_file_to_server(file_path=TEST_FILE_PATH)
    updated_row = row.update()

    download_directory = "/tmp"
    target_file_path = os.path.join(
        download_directory, os.path.basename(TEST_FILE_PATH)
    )

    # Remove the file if it exists
    if os.path.exists(target_file_path):
        os.remove(target_file_path)

    downloaded_files = row.values["FileField"].download_files(download_directory)
    assert len(downloaded_files) > 0
    assert os.path.basename(TEST_FILE_PATH) in downloaded_files
    assert os.path.exists(target_file_path)
