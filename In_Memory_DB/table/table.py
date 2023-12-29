from constants.constants import IndexType


class Table:

    def __init__(self, table_name, table_schema, primary_key):
        """
        Table Name : name of the table
        table_schema: Instance of TableSchemaClass
        indexes: Instances of IndexClass
        primary_key: Primary key of the table
        table_data: Storage for table [Can abstract it into an interface , in order to use any storage as plugin]
        """
        self.table_name = table_name
        self.table_schema = table_schema
        self.indexes = {}
        self.primary_key = primary_key
        self.table_data = {}

    def create_index(self, column_name, index_type):
        """
        Creates a new index by providing column and index type
        """
        if column_name in self.indexes:
            raise Exception(f"Index_already_exists_{column_name}")
        self.indexes[column_name] = IndexType[index_type].value(column_name, self.primary_key)

    def insert_data(self, row_data):
        """
        Insert data into table , steps:
        1. Verify data using TableSchema
        2. If verified, push data into table
        3. Index additional data if defined in indexes
        """
        self.table_schema.validate_row_data(row_data)
        self.table_data[row_data[self.primary_key]] = row_data
        self.index_row_data(row_data)

    def index_row_data(self, row_data):
        """
        Indexes the row data using IndexClass instance
        """
        for _index in self.indexes:
            if _index in row_data:
                self.indexes[_index].index_row_data(row_data)

    def delete_data(self, key):
        """
        Delete data from the table and removes any index as well
        """
        if key not in self.table_data:
            raise Exception(f"Record_not_present_with_key_{self.primary_key}")
        _data = self.table_data[key]
        del self.table_data[key]
        for _index in self.indexes:
            if _index in _data:
                self.indexes[_index].remove_indexed_val(_data)

    def scan_table(self, filters, data):
        """
        Scan complete data on the filters defined.
        """
        if not filters:
            return data
        filtered_data = []
        for row in data:
            valid_data = True
            for filter_key in filters:
                if filter_key not in row or (not (filters[filter_key] == row[filter_key])):
                    valid_data = False
            if valid_data:
                filtered_data.append(row)
        return filtered_data

    def filter_on_indexes(self, filters, indexes):
        """
        Filters data on the indexes.
        It only works as a "AND" filter. So we query all indexes and send back primary keys which satisfies all indexes
        """
        _filtered_data = None
        for _filter_key in indexes:
            if _filtered_data is None:
                _filtered_data = self.indexes[_filter_key].get_data(filters[_filter_key])
                continue
            _filtered_data &= self.indexes[_filter_key].get_data(filters[_filter_key])
        return _filtered_data

    def filter_data(self, filters):
        """
        Filter data on the provided filters.(only uses AND)
        This is a simple implementation as follows:
        1. Check if the column on which filter is needed has an index. if yes then query that first.
        2. After all columns with indexes have been queried , filter the resultant data set on non-indexed
            columns. [This is done as querying indexes is fast , and our non indexed scan can work on a smaller data
            set which we get from after querying on indexed columns]
        3. Combine result and return.
        """
        if self.primary_key in filters:
            if filters.get(self.primary_key) in self.table_data:
                return [self.table_data[filters.get(self.primary_key)]]
            return []
        _has_indexes = [_filter_key for _filter_key in filters if (_filter_key in self.indexes)]
        _no_indexes = [_filter_key for _filter_key in filters if (_filter_key not in self.indexes)]
        _filtered_data = self.filter_on_indexes(filters, _has_indexes)
        indexed_filtered_data = []
        if _filtered_data:
            indexed_filtered_data = [self.table_data[key] for key in _filtered_data]
        final_data = self.scan_table({k: filters[k] for k in _no_indexes},
                                     indexed_filtered_data if _has_indexes else self.table_data.values())
        return final_data