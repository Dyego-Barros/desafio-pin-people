import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

@pytest.fixture
def db_session_mock():
    return MagicMock(spec=Session)
