from table.table import Table

class Database:

    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, column_map, index_map):
        if Table.table_name in self.tables:
            raise Exception("Table_already_Exists")
        self.tables[Table.table_name] = table_name

    def delete_table(self, table_name):
        if table_name not in self.tables:
            raise Exception(f"no_such_table_{table_name}")
        del self.tables[table_name]
