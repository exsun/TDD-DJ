from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from account.models import User
import pytest
from typing import Optional, List


@pytest.fixture
def app_user_group(db) -> Group:
    group = Group.objects.create(name="app_users")
    change_user_permission = Permission.objects.filter(
        codename__in=["change_user", "view_user"],
    )
    group.permissions.add(*change_user_permission)
    return group


@pytest.fixture
def app_user_factory(db, app_user_group:Group):

    def create_app_user(
        username: str ,
        password: Optional[str] = None,
        first_name: Optional[str] = "Ashkan",
        last_name: Optional[str] = "Eshtiagh",
        email: Optional[str] = "ash@gmail.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
        groups: List[Group] = []
        ) -> User:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active
            )
        user.groups.add(app_user_group)
        user.groups.add(*groups)
        return user
    return create_app_user


@pytest.fixture
def user_A(db, app_user_factory) -> User:
    return app_user_factory(username="A")
    

@pytest.fixture
def user_B(db, app_user_factory) -> User:
    return app_user_factory(username="B")
    
    
def test_should_create_user_with_username(user_A: User) -> None:
    assert user_A.username == "A"

def test_should_check_password_for_user(user_A: User) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True

def test_should_not_check_unusable_password(user_A: User) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False

def test_user_groups_exists(user_A: User) -> None:
    assert user_A.groups.filter(name="app_users").exists()

def test_should_create_two_users(user_A: User, user_B: User) -> None:
    assert user_A.username != user_B.username
    assert user_A.groups.name == user_B.groups.name