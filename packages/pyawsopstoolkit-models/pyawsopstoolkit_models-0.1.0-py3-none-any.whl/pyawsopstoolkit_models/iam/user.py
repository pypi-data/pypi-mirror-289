from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from pyawsopstoolkit_models.__validation__ import _validate_type
from pyawsopstoolkit_models.iam.permissions_boundary import PermissionsBoundary


@dataclass
class AccessKey:
    """
    A class representing the access key information of an IAM user.
    """

    id: str
    status: str
    created_date: Optional[datetime] = None
    last_used_date: Optional[datetime] = None
    last_used_service: Optional[str] = None
    last_used_region: Optional[str] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        from pyawsopstoolkit_validators.region_validator import region

        field_value = getattr(self, field_name)
        if field_name in ['id', 'status']:
            _validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['created_date', 'last_used_date']:
            _validate_type(field_value, Union[datetime, None], f'{field_name} should be a datetime.')
        elif field_name in ['last_used_service']:
            _validate_type(field_value, Union[str, None], f'{field_name} should be a string.')
        elif field_name in ['last_used_region']:
            if field_value is not None:
                region(field_value, True)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the AccessKey object.

        :return: Dictionary representation of the AccessKey object.
        :rtype: dict
        """
        return {
            "id": self.id,
            "status": self.status,
            "created_date": self.created_date.isoformat() if self.created_date is not None else None,
            "last_used_date": self.last_used_date.isoformat() if self.last_used_date is not None else None,
            "last_used_service": self.last_used_service,
            "last_used_region": self.last_used_region
        }


@dataclass
class LoginProfile:
    """
    A class representing the login profile information of an IAM user.
    """

    created_date: Optional[datetime] = None
    password_reset_required: Optional[bool] = False

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['created_date']:
            _validate_type(field_value, Union[datetime, None], f'{field_name} should be a datetime.')
        elif field_name in ['password_reset_required']:
            _validate_type(field_value, Union[bool, None], f'{field_name} should be a boolean.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the LoginProfile object.

        :return: Dictionary representation of the LoginProfile object.
        :rtype: dict
        """
        return {
            "created_date": self.created_date.isoformat() if self.created_date is not None else None,
            "password_reset_required": self.password_reset_required
        }


@dataclass
class User:
    """
    A class representing an IAM user.
    """
    from pyawsopstoolkit.account import Account

    account: Account
    name: str
    id: str
    arn: str
    path: str = '/'
    created_date: Optional[datetime] = None
    password_last_used_date: Optional[datetime] = None
    permissions_boundary: Optional[PermissionsBoundary] = None
    login_profile: Optional[LoginProfile] = None
    access_keys: Optional[list[AccessKey]] = None
    tags: Optional[list] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        from pyawsopstoolkit.account import Account
        from pyawsopstoolkit_validators.arn_validator import arn

        mappings = {
            'account': Account,
            'created_date': datetime,
            'password_last_used_date': datetime,
            'permissions_boundary': PermissionsBoundary,
            'login_profile': LoginProfile,
            'access_keys': AccessKey,
            'tags': list
        }
        field_value = getattr(self, field_name)
        field_type = mappings.get(field_name)
        if field_name in ['account']:
            _validate_type(field_value, field_type, f'{field_name} should be of {field_type.__name__} type.')
        elif field_name in ['name', 'id', 'path']:
            _validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['arn']:
            arn(field_value, True)
        elif field_name in ['created_date', 'password_last_used_date', 'permissions_boundary', 'tags', 'login_profile']:
            _validate_type(
                field_value, Union[field_type, None], f'{field_name} should be of {field_type.__name__} type.'
            )
        elif field_name in ['access_keys']:
            _validate_type(
                field_value, Union[list, None], f'{field_name} should be a list of {field_type.__name__} type.'
            )
            if field_value is not None and len(field_value) > 0:
                all(
                    _validate_type(
                        item, field_type, f'{field_name} should be a list of {field_type.__name__} type.'
                    ) for item in field_value
                )

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the User object.

        :return: Dictionary representation of the User object.
        :rtype: dict
        """
        return {
            "account": self.account.to_dict(),
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "arn": self.arn,
            "created_date": self.created_date.isoformat() if self.created_date is not None else None,
            "password_last_used_date": (
                self.password_last_used_date.isoformat() if self.password_last_used_date is not None else None
            ),
            "permissions_boundary": (
                self.permissions_boundary.to_dict() if self.permissions_boundary is not None else None
            ),
            "login_profile": self.login_profile.to_dict() if self.login_profile is not None else None,
            "access_keys": [
                key.to_dict() for key in self.access_keys
            ] if self.access_keys and len(self.access_keys) > 0 else None,
            "tags": self.tags
        }
