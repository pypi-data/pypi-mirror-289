import pytest


def test_baserow_client_setup(baserow_client):
    # Verify that the baserow_client fixture is set up correctly
    assert baserow_client is not None
    assert baserow_client.url is not None
    assert baserow_client.token is not None


def test_table_setup(test_table):
    # Verify that the test_table fixture is set up correctly
    assert test_table is not None
    assert test_table.id > 0

    # Access fields to ensure they are loaded
    fields = test_table.fields
    assert len(fields) > 0
