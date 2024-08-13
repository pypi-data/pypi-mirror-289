import pytest

from skys_llc_auth.exceptions import ParamsError, TokenError
from skys_llc_auth.token_validation import DefaultTokenParams, TokenValidation
from skys_llc_auth.utils import UserRole
from tests.fixtures import SETTINGS

default_token_params = DefaultTokenParams(config=SETTINGS)


def test_init_raises_error_when_missing_params():
    with pytest.raises(ParamsError) as e:
        DefaultTokenParams()
    assert e.value.args == ("key and algorithms, or config class must be provided",)


def test_token_validation_permission(gen_token_admin: str):
    token_valid = TokenValidation(gen_token_admin, default_token_params)
    assert token_valid.check_permission(role=UserRole.Administrator, exclude=False) is None


def test_token_validation_permission_list_role(gen_token_admin: str):
    token_valid = TokenValidation(
        gen_token_admin,
        default_token_params,
    )
    assert token_valid.check_permission(role=[UserRole.Administrator, UserRole.Instructor], exclude=False) is None


def test_token_validation_permission_list_role_exclude(gen_token_admin: str):
    token_valid = TokenValidation(
        gen_token_admin,
        default_token_params,
    )
    assert token_valid.check_permission(role=[UserRole.Server, UserRole.Student], exclude=True) is None


def test_token_validation_permission_role_exclude(gen_token_admin: str):
    token_valid = TokenValidation(
        gen_token_admin,
        default_token_params,
    )
    assert token_valid.check_permission(role=UserRole.Server, exclude=True) is None


def test_token_validation_not_permission(gen_token_admin: str):
    with pytest.raises(TokenError) as e:
        TokenValidation(
            gen_token_admin,
            default_token_params,
        ).check_permission(role=UserRole.Server, exclude=False)
    assert e.value.detail == "Permission denied"
    assert e.value.status_code == 403


def test_method_token_validation_user_id(gen_token_admin: str):
    user_id = TokenValidation(
        gen_token_admin,
        default_token_params,
    ).user_id()
    assert user_id == "60db7c59-e154-46df-bbd7-217cafcf6a2d"


def test_method_token_validation_without_user_id(gen_token_admin_without_id: str):
    with pytest.raises(TokenError) as e:
        TokenValidation(
            gen_token_admin_without_id,
            default_token_params,
        ).user_id()
    assert e.value.detail == "Token must have key id"
    assert e.value.status_code == 400


def test_token_validation_permission_none_role(gen_token_admin: str):
    with pytest.raises(ParamsError) as e:
        TokenValidation(
            gen_token_admin,
            deftokenpar=default_token_params,
        ).check_permission(role="", exclude=False)  # pyright: ignore[reportArgumentType] checking what happens if you pass a None value as role

    assert e.value.args == ("expected type role is list[UserRole] or UserRole",)


def test_token_validation_permission_none_role_exclude(gen_token_admin: str):
    with pytest.raises(ParamsError) as e:
        TokenValidation(
            gen_token_admin,
            deftokenpar=default_token_params,
        ).check_permission(role="", exclude=True)  # pyright: ignore[reportArgumentType] checking what happens if you pass a None value as role

    assert e.value.args == ("expected type role is list[UserRole] or UserRole",)


def test_token_valid_key_error():
    key = None
    algorithms = "HS256"

    with pytest.raises(ParamsError) as e:
        DefaultTokenParams(key, algorithms)
    assert e.value.args == ("key and algorithms, or config class must be provided",)


def test_method_token_validation_token_type_access(gen_token_admin: str):
    token_type = TokenValidation(
        gen_token_admin,
        default_token_params,
    ).is_access()
    assert token_type is True


def test_method_token_validation_token_type(gen_token_admin: str):
    token_type = TokenValidation(
        gen_token_admin,
        default_token_params,
    ).is_refresh()
    assert token_type is False


def test_method_token_validation_token_type_refresh(gen_token_admin_refresh: str):
    token_type = TokenValidation(
        gen_token_admin_refresh,
        default_token_params,
    ).is_access()
    assert token_type is False


def test_method_token_validation_token_type_refresh_(gen_token_admin_refresh: str):
    token_type = TokenValidation(
        gen_token_admin_refresh,
        default_token_params,
    ).is_refresh()
    assert token_type is True


def test_method_token_validation_user_role(gen_token_admin: str):
    user_role = TokenValidation(
        gen_token_admin,
        default_token_params,
    ).user_role()
    assert user_role == UserRole.Administrator.value


def test_attrs_token(gen_token_instr: str):
    list_group = TokenValidation(
        gen_token_instr,
        default_token_params,
    ).list_of_study_groups()
    assert list_group == ["sadfasdf", "dsaf"]


def test_attrs_token_st(gen_token_student: str):
    short_name = TokenValidation(
        gen_token_student,
        default_token_params,
    ).short_name_student()
    assert short_name == "short_name"


def test_attrs_token_stud_org_id(gen_token_student: str):
    org_id = TokenValidation(
        gen_token_student,
        default_token_params,
    ).user_organization_id()
    assert org_id == "asdasdasdasdasdaswqe"
