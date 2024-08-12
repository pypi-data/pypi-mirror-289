from dataclasses import dataclass

from pyawsopstoolkit_models.__validation__ import _validate_type


@dataclass
class PermissionsBoundary:
    """
    A class representing an IAM permissions boundary.
    """

    type: str
    arn: str

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        from pyawsopstoolkit_validators.arn_validator import arn

        field_value = getattr(self, field_name)
        if field_name in ['type']:
            _validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['arn']:
            arn(field_value, True)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the PermissionsBoundary object.

        :return: Dictionary representation of the PermissionsBoundary object.
        :rtype: dict
        """
        return {
            "type": self.type,
            "arn": self.arn
        }
