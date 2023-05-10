import pytest
from pytest_factoryboy import register
from tests.factories import ProfileFactory, UserFactory

register(ProfileFactory)
register(UserFactory)


@pytest.fixture
def base_user(db, user_factory):
    return user_factory.create()


@pytest.fixture
def super_user(db, user_factory):
    return user_factory.create(is_staff=True, is_superuser=True)


@pytest.fixture
def profile(db, profile_factory):
    return profile_factory.create()
