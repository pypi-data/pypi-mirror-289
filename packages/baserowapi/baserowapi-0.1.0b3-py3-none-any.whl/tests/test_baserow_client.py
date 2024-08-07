# test_baserow_client.py


def test_get_rows(baserow_client, test_table, test_row_manager):
    # Create a row for the test
    new_row_data = {
        "Name": "Test Get Rows",
        "Notes": "Testing get rows",
        "Active": True,
    }
    test_row_manager(new_row_data)

    # Verify that rows can be retrieved correctly
    rows = test_table.get_rows()
    all_rows = list(rows)
    assert len(all_rows) > 0


def test_update_row(baserow_client, test_table, test_row_manager):
    # Create a row for the test
    new_row_data = {"Name": "Test Update", "Notes": "To be updated", "Active": True}
    added_row = test_row_manager(new_row_data)

    # Verify that a row can be updated correctly
    updated_data = {"id": added_row.id, "Name": "Test Updated"}
    updated_row = test_table.update_rows([updated_data])
    assert updated_row[0]["Name"] == "Test Updated"
