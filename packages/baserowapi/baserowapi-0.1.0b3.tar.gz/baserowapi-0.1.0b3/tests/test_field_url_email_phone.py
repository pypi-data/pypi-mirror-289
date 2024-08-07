import pytest


def test_url_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test URL", "URL": "https://example.com"}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None

    assert "URL" in row.content
    assert row.content["URL"] == "https://example.com"


def test_email_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Email", "Email": "test@example.com"}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None

    assert "Email" in row.content
    assert row.content["Email"] == "test@example.com"


def test_phone_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Phone", "Phone": "+1234567890"}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None

    assert "Phone" in row.content
    assert row.content["Phone"] == "+1234567890"
