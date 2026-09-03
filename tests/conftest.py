import pytest

from ooc.api.deps import reset_all


@pytest.fixture(autouse=True)
def clean_registry():
    """Каждый тест начинает с пустого реестра психик."""
    reset_all()
    yield
    reset_all()
