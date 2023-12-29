from constants.exceptions import MissingValueException, UndefinedSchemaMember


class TableSchema:
    """
    Defines Schema of the table to be used
    It does validation/transformation over the row data
    """

    def __init__(self, allow_undefined=False):
        """
        schema_members: Instance of SchemaMember class
        allow_undefined: is any column for which schema member is not defined allowed?
        """
        self.schema_members = {}
        self.allow_undefined = allow_undefined

    def add_schema_member(self, schema_member):
        self.schema_members[schema_member.column_name] = schema_member

    def validate_row_data(self, row_data):
        """
        validates row data
        Multi level validation
        TableSchema : validates any undefined values
        SchemaMember : validates null check
        Column_data_type:  validates value type and ranges.
        """
        validated_data = {}
        for _col_name, _col_val in row_data.items():
            if _col_name not in self.schema_members and (not self.allow_undefined):
                raise UndefinedSchemaMember(f"undefined_schema_memeber_{_col_name}")
            if _col_name not in self.schema_members:
                validated_data[_col_name] = _col_val
                continue
            validated_data[_col_name] = self.schema_members[_col_name].validate_value(_col_val)

        for col_name in self.schema_members:
            if self.schema_members[col_name].required and col_name not in row_data:
                raise MissingValueException(f"col_name_{col_name}_missing")

        return validated_data