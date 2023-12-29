from sortedcontainers import SortedDict


class Index:
    """
    Base class for Index
    Provides Interface for indexing/querying and removing indexes
    For now index storage is considered as a SortedDict(equivalent to balanced BST) but we can abstract this as well
    and make a generic storage interface , so that we can plugin different storages without ever changing indexing code.
    """

    def __init__(self, index_name, primary_key):
        """
        index_name : Name of the index , normally column_name
        primary_key: Primary key of the DB, this acts as a query result, ie. provides primary key of data which satisfies
        filter conditions.(we can remove it and take primary key while filtering as well)
        index_storage: Storage for indexes. can abstract the same into interface
        """
        self.index_name = index_name
        self.primary_key = primary_key
        self.index_storage = SortedDict()

    def index_row_data(self, row_data):
        """
        indexes the row data.
        we remove older index first so that we don't get wrong results
        """
        self.remove_indexed_val(row_data)
        self.index_data(row_data)

    def index_data(self, row_data):
        """
        does indexing of the data in index storage
        """
        raise Exception("No_default_implementation")

    def get_data(self, filter_val):
        """
        return values satisfying the condition, override as required
        """
        return self.index_storage.get(filter_val, set())

    def remove_indexed_val(self, row_data):
        """
        removes indexes
        """
        raise Exception("No_default_implementation")


class ReverseIndex(Index):
    """
    Basic Reverse index implementation. Just storing val<>key mapping
    """

    def index_data(self, row_data):
        """
        Indexes the val in index storage, basically val<>primary_key mapping
        """
        if not self.index_storage.get(row_data[self.index_name]):
            self.index_storage[row_data[self.index_name]] = set()
        self.index_storage[row_data[self.index_name]].add(row_data[self.primary_key])

    def remove_indexed_val(self, row_data):
        """
        Remove the indexed value
        """
        if row_data[self.primary_key] in self.index_storage:
            self.index_storage[row_data[self.index_name]].remove(row_data[self.primary_key])


class FuzzyIndex(Index):
    """
    Fuzzy indexes: Instead of directly storing a val<>key mapping , here we will tokenize the value and store primary
    key in each one of them.
    very basic implementation of fuzzy index
    """

    def __init__(self, index_name, primary_key, seperator=" "):
        """
        seperator: used to tokenize the value, default is space (" ")
        """
        super(FuzzyIndex, self).__init__(index_name, primary_key)
        self.seperator = seperator

    def get_fuzzy_values(self, row_data):
        """
        returns values after tokenization
        """
        _val_to_index = row_data[self.index_name]
        fuzzy_values = _val_to_index.split(self.seperator)
        return fuzzy_values

    def index_data(self, row_data):
        """
        Index each of the fuzzy values
        """
        for _val in self.get_fuzzy_values(row_data):
            if not self.index_storage.get(_val):
                self.index_storage[_val] = set()
            self.index_storage[_val].add(row_data[self.primary_key])

    def remove_indexed_val(self, row_data):
        """
        Removes each of the fuzzy indexed value
        """
        for _val in self.get_fuzzy_values(row_data):
            if _val not in self.index_storage:
                continue
            key_to_remove = row_data[self.primary_key]
            if key_to_remove not in self.index_storage[_val]:
                continue
            self.index_storage[_val].remove(key_to_remove)
