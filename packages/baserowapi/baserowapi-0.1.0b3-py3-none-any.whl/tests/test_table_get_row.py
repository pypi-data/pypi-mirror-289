import pytest
from baserowapi.models.table import Table


def test_get_row_valid_id(baserow_client, test_table):
    # Assuming there's at least one row in the table to test with
    rows = list(test_table.get_rows(size=1))
    assert len(rows) > 0

    row_id = rows[0].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row.id == row_id


def test_get_row_invalid_id(baserow_client, test_table):
    invalid_row_id = 999999999  # Assuming this ID does not exist in the table
    with pytest.raises(Exception):
        test_table.get_row(invalid_row_id)


def test_get_row_no_id(baserow_client, test_table):
    with pytest.raises(ValueError):
        test_table.get_row(None)
