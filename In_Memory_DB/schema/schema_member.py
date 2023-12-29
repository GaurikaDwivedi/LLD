from constants.exceptions import InvalidValueException


class SchemaMember:
    """
    This class provides the actual column to be used in schema
    It uses ColumnDataType class to enforce type
    """

    def __init__(self, column_name, column_type, required=True, allow_none=False):
        """
        column_name : Name of the column
        column_type: Instance of ColumnDataType class ie. can be IntDataType, StrDataType etc.
        required: Is the column value required in data or not
        allow_none: Is the column value allowed as null or not
        """
        self.column_name = column_name
        self.column_type = column_type
        self.required = required
        self.allow_none = allow_none

    def validate_value(self, val):
        """
        validates column value
        """
        if val is None and not self.allow_none:
            raise InvalidValueException(f"None_not_allowed_in_{self.column_name}")
        return self.column_type.validate(val)

