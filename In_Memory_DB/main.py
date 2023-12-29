"""

Components:
Database
	Members:
	tables({table_name: Table}}

	Functions:
	create_table(table_name,schema)
	delete_table(table_name)

ColumnDataType:
	Members:
	value
	Min
	max
	Functions:
	validate_data_value()
IntDataType(ColumnDataType)
StrDataType(ColumnDataType)
IndexType:
	Reverse
	Fuzzy
SchemaMember:
	Members:
	column_name
	column_type(ColumnDataType)
	required
index_type(IndexType)
allow_none(Boolean)

Functions:
validate_schema_member()


TableSchema:
	Members:
	schema_members(List<SchemaMember>)
	allow_undefined

	Functions:
	validate()

Table:
	Members:
	table_name
	table_schema(TableSchema)
	primary_key
	indexes(List<index_name: Index>)
	table_data {primary_key: data}

	Functions:
	add_row(row_data)
	index_row_values(row_data)
	delete_row(primary_key)
	filter_rows(filters){“key”:values”}

Index:
	Members:
	index_name(List)
	index_storage({“value”:[primary_keys])
	primary_key

	functions:
	index_row_data(row_data)
	get_values(value)

FuzzyIndex(Index):
index_row_data(row_data)

MultiColumnIndex(Index):
	index_row_data(row_data)


"""