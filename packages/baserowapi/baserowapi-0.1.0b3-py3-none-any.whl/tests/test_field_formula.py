import pytest
from baserowapi.models.field import FormulaField
from baserowapi.models.row_value import FormulaRowValue


# Read Operation Test
def test_read_formula_field(baserow_client, test_table, test_row_manager):
    # Ensure there's a row with a formula field to read
    rows = list(test_table.get_rows())
    assert len(rows) > 0

    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    assert row is not None

    # Ensure the formula field exists and has the correct value
    formula_value = row["Formula"]
    assert (
        formula_value == {'label': 'Baserow Home', 'url': 'https://baserow.io'}
    )


# Field-specific Properties Tests
def test_formula_field_properties(baserow_client, test_table):
    formula_field = test_table.fields["Formula"]

    assert hasattr(formula_field, "formula")
    assert hasattr(formula_field, "formula_type")
    assert hasattr(formula_field, "error")
    assert hasattr(formula_field, "array_formula_type")
    assert formula_field.is_read_only is True


def test_formula_row_value(baserow_client, test_table, test_row_manager):
    rows = list(test_table.get_rows())
    assert len(rows) > 0

    row_id = rows[-1].id
    row = test_table.get_row(row_id)
    formula_value = row["Formula"]

    assert formula_value == {'label': 'Baserow Home', 'url': 'https://baserow.io'}
