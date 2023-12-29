from constants.exceptions import OutOfRangeException


class ColumnDataType:
    """
    Base class wrapper over primitive data types
    """

    def __init__(self, data_type):
        self.data_type = data_type

    def validate(self, val):
        if not isinstance(val, self.data_type):
            raise Exception("Invalid_data_point_type")
        return val


class IntDataType(ColumnDataType):
    """
    IntData type class provides validations over integer like, min and max values allowed
    """

    def __init__(self, _min_value, _max_value):
        self.min_value = _min_value
        self.max_value = _max_value
        super(IntDataType, self).__init__(int)

    def validate(self, val):
        """
        validate min and max values
        """
        super(IntDataType, self).validate(val)
        if not self.min_value <= val <= self.max_value:
            raise OutOfRangeException("int_out_of_range")
        return val


class StrDataType(ColumnDataType):

    def __init__(self, _min_value, _max_value):
        self.min_value = _min_value
        self.max_value = _max_value
        super(StrDataType, self).__init__(str)

    def validate(self, val):
        """
        validate max len of the string
        """
        super(StrDataType, self).validate(val)
        if not self.min_value <= len(val) <= self.max_value:
            raise OutOfRangeException("string_len_out_of_range")
        return val
