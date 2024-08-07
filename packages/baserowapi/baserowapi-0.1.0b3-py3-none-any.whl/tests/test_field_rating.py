import pytest
from baserowapi.models.field import RatingField


# Initialization Tests
def test_ratingfield_initialization():
    field_data = {
        "id": 1358462,
        "table_id": 198958,
        "name": "Rating",
        "order": 4,
        "type": "rating",
        "primary": False,
        "read_only": False,
        "description": None,
        "max_value": 5,
        "color": "dark-orange",
        "style": "star",
    }
    rating_field = RatingField(name="Test Rating Field", field_data=field_data)
    assert rating_field.name == "Test Rating Field"
    assert rating_field.max_value == 5
    assert rating_field.color == "dark-orange"
    assert rating_field.style == "star"


# CRUD Operation Tests
def test_create_rating_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Create", "Rating": 3, "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["Rating"] == 3


def test_read_rating_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Read", "Rating": 3, "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    rows = list(test_table.get_rows())
    assert len(rows) > 0
    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None
    assert row["Rating"] == 3


def test_update_rating_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Update", "Rating": 3, "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"Rating": 4}
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["Rating"] == 4


def test_delete_rating_field(baserow_client, test_table, test_row_manager):
    new_row_data = {"Name": "Test Delete", "Rating": 3, "Active": True}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    status_code = test_table.delete_rows([row_id])
    assert status_code is True

    rows = list(test_table.get_rows())
    assert not any(row.id == row_id for row in rows)


# Compatibility Tests
def test_ratingfield_compatible_filters():
    field_data = {
        "id": 1358462,
        "table_id": 198958,
        "name": "Rating",
        "order": 4,
        "type": "rating",
        "primary": False,
        "read_only": False,
        "description": None,
        "max_value": 5,
        "color": "dark-orange",
        "style": "star",
    }
    rating_field = RatingField(name="Test Rating Field", field_data=field_data)
    expected_filters = ["equal", "not_equal", "higher_than", "lower_than"]
    assert rating_field.compatible_filters == expected_filters
