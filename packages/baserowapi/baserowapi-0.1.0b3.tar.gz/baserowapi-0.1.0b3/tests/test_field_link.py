import pytest
from baserowapi.models.field import TableLinkField


# CRUD Operation Tests
def test_update_tablelinkfield_with_null_value(
    baserow_client, test_table, test_row_manager
):
    new_row_data = {
        "Name": "Test Link Row",
        "TableLink": [],
    }  # Empty list for null value
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["TableLink"] == []

    row_id = added_row.id
    updated_data = {"TableLink": []}  # Empty list for null value
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["TableLink"] == []


def test_get_options(baserow_client, test_table):
    table_link_field = next(
        (field for field in test_table.fields if field.name == "TableLink"), None
    )
    assert table_link_field is not None
    assert isinstance(table_link_field, TableLinkField)

    options = table_link_field.get_options()
    assert isinstance(options, list)
    assert len(options) > 0  # Assuming there are options in the linked table


def test_update_tablelinkfield_with_invalid_option(
    baserow_client, test_table, test_row_manager
):
    new_row_data = {"Name": "Test Link Row", "TableLink": []}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None

    row_id = added_row.id
    updated_data = {"TableLink": ["Invalid Option"]}  # Invalid option in list
    with pytest.raises(Exception):
        test_table.update_rows([{"id": row_id, **updated_data}])


def test_update_tablelinkfield_with_valid_option(
    baserow_client, test_table, test_row_manager
):
    table_link_field = next(
        (field for field in test_table.fields if field.name == "TableLink"), None
    )
    assert table_link_field is not None
    assert isinstance(table_link_field, TableLinkField)

    # Retrieve valid options from the linked table
    valid_options = table_link_field.get_options()
    assert len(valid_options) > 0  # Ensure there are valid options available

    valid_option = valid_options[0]  # Choose the first option for testing

    new_row_data = {"Name": "Test Link Row", "TableLink": [valid_option]}
    added_row = test_row_manager(new_row_data)
    assert added_row is not None
    assert added_row["TableLink"] == [valid_option]

    row_id = added_row.id
    updated_data = {"TableLink": [valid_option]}  # Valid option in list
    updated_rows = test_table.update_rows([{"id": row_id, **updated_data}])
    assert updated_rows[0]["TableLink"] == [valid_option]


def test_tablelinkfield_compatible_filters(baserow_client, test_table):
    table_link_field = next(
        (field for field in test_table.fields if field.name == "TableLink"), None
    )
    assert table_link_field is not None
    assert isinstance(table_link_field, TableLinkField)

    expected_filters = [
        "link_row_has",
        "link_row_has_not",
        "link_row_contains",
        "link_row_not_contains",
        "empty",
        "not_empty",
    ]
    assert table_link_field.compatible_filters == expected_filters


# Additional Tests
def test_link_row_limit_selection_view_id(baserow_client, test_table):
    table_link_field = next(
        (field for field in test_table.fields if field.name == "TableLink"), None
    )
    assert table_link_field is not None
    assert isinstance(table_link_field, TableLinkField)
    assert "link_row_limit_selection_view_id" in table_link_field.field_data
