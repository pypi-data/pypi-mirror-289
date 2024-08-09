# SSQL API DOCUMENTATION
## Overview
The SSQL package allows you to use MySQL in the most simple and efficient way possible. It provides an easy way to access databases, create new ones, insert data, retrieve data and so much more. The project is still in development and for now it has a limited number of methods, but I'm planning in expanding it more. This library require MySQL to be already installed on the machine.
## Tutorial
You can decide to follow the tutorial right below, or you can just see all the methods (bottom of the page)!

Let's start by importing the API into our python project
```python
from ssql import SSQL
```
### SSQL() - Main Class
- host (str): The MySQL server host (default: `localhost`)
- user (str): The MySQL user
- passoword (str): The MySQL user password
- database (str): The database name (optional)
- logging (bool): Enable logging (default: `True`)
- logname (str): Logger name (default: `__name__`)

```python
from ssql import SSQL

# Initialize SSQL
ssql = SSQL(host="localhost", user="root", password="password", logname="SSQL_Logs")
```

Once created the SSQL object, the connection to the MySQL server will be automatically initialized with the parameters that we put.
Now that we have created and established the connection, we need to create a database in order to be able to work with more advanced things.

```python
from ssql import SSQL

# Initialize SSQL
ssql = SSQL(host="localhost", user="root", password="password", logname="SSQL_Logs")
# Create a database named "people"
ssql.createDB(database="people", connect=True)
```

With the function `createDb()`, we create a database, and because connect is True, it'll update the connection, and it will connect us to the database. Now that we have a database and we are connected to it, we can now create our first table!

```python
from ssql import SSQL
from ssql import Data

# Initialize SSQL
ssql = SSQL(host="localhost", user="root", password="password", database="people" logname="SSQL_Logs")
# Create a table named customers
ssql.createTable(name="customers",
                columns=["id", "name", "email", "wallet"],
                datatype=[Data.INT, Data.VARCHAR, Data.VARCHAR, Data.INT],
                sizes=[0, 20, 50, 0],
                constraints=["AUTO_INCREMENT PRIMARY KEY". "NOT NULL", "NOT NULL", ""])
```
This might seems like a lot of code, but once you understand it, it'll become easier. First of all we specify the name of the table. Then we provide 4 lists: the first one `columns` contains the names of the colums we want to create; the second one `datatype` contains the type of data that each column will have; the third one `sizes` rapresent the max size of each columns, 0 is the default value for MAX; and the last one `constraints` contains the constraints of each column. I'll show you a rapresentation of table taht we've just created

| id    | name  | email | wallet    |
| ----- | ----- | ----- | --------- |
|       |       |       |           |

As you can see, the table right now is empty, we should put some information into that.

```python
from ssql import SSQL

# Initialize SSQL
ssql = SSQL(host="localhost", user="root", password="password", database="people" logname="SSQL_Logs")
# Insert 2 customer into the table
ssql.insert(table="customers",
            columns=["name", "email", "wallet"],
            values=[("John", "john1234@example.com", 1000),
                    ("Harry", "harry4321@example.com", 0)])
```

Now our table should look like this:

| id    | name  | email                 | wallet    |
| ----- | ----- | --------------------- | --------- |
|0      |John   |john1234@example.com   |1000       |
|1      |Harry  |harry4321@example.com  |0          |

Look at that, fantastic! Wait Harry has 0 in his wallet. Let's fix that. We can use the `update()` function to edit his wallet.

```python
from ssql import SSQL

# Initialize SSQL
ssql = SSQL(host="localhost", user="root", password="password", database="people" logname="SSQL_Logs")
# Update Harry's wallet
ssql.update(table="customers", column="wallet", value="2000", condition="WHERE name = 'Harry'")
```

Perfect, now the table should look like this:

| id    | name  | email                 | wallet    |
| ----- | ----- | --------------------- | --------- |
|0      |John   |john1234@example.com   |1000       |
|1      |Harry  |harry4321@example.com  |2000       |

Well, what if we want to retrive all the data from this table? We can use the `selectAll()` method!

```python
from ssql import SSQL

# Initialize SSQL
ssql = SSQL(host="localhost", user="root", password="password", database="people" logname="SSQL_Logs")
# Retrive all the data from the table
data = ssql.selectAll(table="customers", order="ORDER BY id")
print(data)
```

Now we have the all the data from the table, ordered by the id. The tutorial ends here, for more info and advanced things, check the all the methods down below!

## SSQL() - Main Class
Main class of the packet, you need to initialize this class in order to operate with MySQL. In the
initialization process you need to specify 'host', 'user', and 'password'. Optional are 'database' and
'logging'. If you don't specify the database from the creation of the object, you can use the function
'connectDB(database)' to connect after.

! Important Note: each method that gets a query result (e.g. `selectAll()`, `dbList()`) will cache it, in order to use methods like `findB()` or `findI()`, without giving a `result`. This will clean your code, because you won't need to necessarily save the results.

### Builder Attributes
- host (str): The MySQL server host (default: `localhost`)
- user (str): The MySQL user
- passoword (str): The MySQL user password
- database (str): The database name (optional)
- logging (bool): Enable the logging of event (default: `True`)
- logname (str): Logger name (default: `__name__`)

### connect() -> [SSQL or None] 
This method is called by default in the __init__ of the class to establish a connection with MySQL. It
connects without a database if you don't specify one when creating the object. You can call this method to
reestablish a MySQL connection.

Exceptions:
- Interface Error -> None
- Programming Error -> None

### close() -> [SSQL or None]
This method allows you to close the MySQL connection with the server. You can still connect again with the
`connect()` method. If the connection is already closed, it'll drop an error, but it'll continue the execution

Exceptions:
- Interface Error -> None
- Programming Error -> None

### connectDB(database: str) -> [SSQL]
This method allows you to connect to a database if you didn't specify one when creating the object. It starts a search among the database to find the specified one. 

Parameters:
- database (str): You need to provide the name of the database in which you want to connect

### dbList() -> [SSQL or None]
This method retrieves a list of all created databases. If a connection is not initialized, it will create one
by default. Instead of returning a list of tuples, this method returns the object itself. Each time a query
is executed, the class saves the results in a local variable. By returning the object, you can chain multiple
methods together and utilize these results with subsequent methods. For example: `SSQL.dbList().find("people")`

Exceptions:
- Interface Error -> None
- Programming Error -> None

### getDBList() -> [list[tuple] | None]
This method allows you to retrieve the list of all the created databases and returns it. If a connection is not initialized, it'll create one by default.

Exceptions:
- Interface Error -> None
- Programming Error -> None

### tableList() -> [SSQL or None]
This method allows you to retrieve the list of all the created tables in a specified database. If a
connection is not initialized, it'll create one by default. If the database is not defined, this method won't
work. Instead of returning a list of tuples, this method returns the object itself. Each time a query is
executed, the class saves the results in a local variable. By returning the object, you can chain multiple
methods together and utilize these results with subsequent methods. For example: `SSQL.tableList().find("customers")`.

Exceptions:
- Interface Error -> None
- Programming Error -> None

### getTableList() -> [list[tuple]]
This method allows you to retrieve the list of all the created tables in a specified database. If a
connection is not initialized, it'll create one by default. If the database is not defined, this method won't
work.

Exceptions:
- Interface Error -> None
- Programming Error -> None

### findB(search: str, result: list[tuple]) -> bool
With this function you can find a specified thing inside a query result. This method returns a boolean value,
true if it finds a match, false otherwise. You can use this method alone, by giving in input the result of a
query:

```python
result = SSQL.getDBList()
boolean = SSQL.findB('people', result)
```

or you can put it after another function that get a query result and return the SSQL object:

```python
boolean = SSQL.dbList().findB('people')
```

Parameters:
- search (str): keyword to search among a query result
- result (list[tuple]): (Optional) the query result

### findI(search: str, result: list[tuple]) -> int
With this function you can find a specified thing inside a query result. This method returns a integer value,
precisely, the index of where the value was found. It returns -1 if the value wasn't found You can use this
method alone, by giving in input the result of a query:

```python
result = SSQL.getDBList()
index = SSQL.findB('people', result)
```

or you can put it after another function that get a query result and return the SSQL object:

```python
index = SSQL.dbList().findB('people')
```

Parameters:
- search (str): keyword to search among a query result
- result (list[tuple]): (Optional) the query result

### createDB(database: str, connect: bool) -> [SSQL or None]
This function allows you to create a database. First, it checks if a database with the same name you provided
exists. If it doesn't exist, it'll create one. You can also decide to connect directly to the new database.

Parameters:
- database (str): Name of the database that needs to be created
- connect (bool): (default=False) Allow you to directly connect to the database that has been created

Exceptions:
- Interface Error -> None
- Programming Error -> None

### dropDB(database: str) -> [SSQL or None]
With this method, you can delete a database form MySQL. If the database you specify doesn't exist,
you'll get an error

Parameters:
- database (str): Name of the database that needs to be deleted

Exceptions:
- Interface Error -> None
- Programming Error -> None

### createTable(name: str, columns: list[str], datatype: list[str], sizes: list[int], constraints: list[str]) -> [SSQL or None]
This function allows you to create a table inside a database. If a table with the same name already exists,
you'll get an error. The lists `columns`, `datatype`, `sizes`, and `constraints` must all have the same
length and the elements must be in corresponding order.

Parameters:
- name (str): The name of the table you want to create
- columns (list[str]): A list of the columns name you want in the table (e.g. `['id', 'Username', 'Email']`)
- datatype (list[str]): The type of data you want for each column (e.g. `[Data.INT, Data.VARCHAR, Data.VARCHAR]`). You can either use `Data.*` or a string like `INT`.
- sizes (list[int]): The max size of each column (you can put 0 for max size) (e.g. `[0, 20, 50]`)
- constraints (list[str]): (Optional) You can put here the constraints (leave blank if you don't need anything) (e.g. `['AUTO_INCREMENT PRIMARY KEY', 'NOT NULL', '']`)

Exceptions:
- Interface Error -> None
- Programming Error -> None

### dropTable(table: str) -> [SSQL or None]
This function allows you to drop a table by its name. If the table doesn't exist, you'll get an error.

Parameters:
- table (str): The name of the table that needs to be deleted

Exceptions:
- Interface Error -> None
- Programming Error -> None

### insert(table: str, colunmns: list[str], values: list[tuple]) -> [SSQL or None]
With this function, you'll be able to insert your data into the specified columns of a table. The number of
columns in the column list must be the same exact number as the tuples in the value list.

Parameters:
- table (str): The name of the table
- columns (list[str]): The columns in which the values are put
- values (list[str]): The values to insert into the table

Exceptions:
- Interface Error -> None
- Programming Error -> None

### selectAll(table: str, filter: str, order: str, limit: int, results: bool) -> [list[tuple] or SSQL or None]
This method allow you to execute the query `SELECT *` from a specified table. You can also filter the query
by integer and conditions, order it by column, limit the number of results that the query returns. You can
also decide if you want this function to return the query result or the SSQL object.

Parameters:
- table (str): The name of the table
- filter (str): (Optional) Add a filter to the `SELECT *` query (e.g. `WHERE example_column = 'example'`)
- order (str): (Optional) Order the query results by column. (e.g. `ORDER BY example_column` or `ORDER BY example_column DESC`)
- limit (int): (Optional) Limit the number of query results (`LIMIT 10`)
- results (bool): True, returns the query results. False, return the SSQL object (Default=True)

Exceptions:
- Interface Error -> None
- Programming Error -> None

### select(columns: list[str], table: str, filter: str, order: str, limit: int, results: bool) -> [list[tuple] or SSQL or None]
This method allow you to execute the query `SELECT` from a specified table. You can also filter the query
by integer and conditions, order it by column, limit the number of results that the query returns. You can
also decide if you want this function to return the query result or the SSQL object.

Parameters:
- columns (list[str]): List of the columns that are needed for the query
- table (str): The name of the table
- filter (str): (Optional) Add a filter to the `SELECT *` query (e.g. `WHERE example_column = 'example'`)
- order (str): (Optional) Order the query results by column. (e.g. `ORDER BY example_column` or `ORDER BY example_column DESC`)
- limit (int): (Optional) Limit the number of query results (`LIMIT 10`)
- results (bool): True, returns the query results. False, return the SSQL object (Default=True)

Exceptions:
- Interface Error -> None
- Programming Error -> None

### delete(table: str, condition: str) -> [SSQL or None]
With this method you'll be able to delete specified records which match a condition

Parameters:
- table (str): The name of the table
- condition (str): The condition to delete the records (e.g. `WHERE example_column = 'example'`)

Exceptions:
- Interface Error -> None
- Programming Error -> None

### deleteAll(table: str) -> [SSQL or None]
With this method you'll be able to delete all the records of a table

Parameters:
- table (str): The name of the table

Exceptions:
- Interface Error -> None
- Programming Error -> None

### update(table: str, column: str, value: str, condition: str) -> [SSQL or None]
This method allows you to update all the existing records with a certain value if a condition is satisfied

Parameters:
- table (str): The name of the table
- column (str): Column to update (e.g. `example_column`)
- value (str): Value of the update (e.g. `example_value`)
- condition (str): Condition to satisfy to update the records (e.g. `WHERE example_column = 'example'`)

Exceptions:
- Interface Error -> None
- Programming Error -> None

----

## Data
You noticed that in the `createTable()` method, in the `datatype` parameter, i used a list: `[Data.INT, Data.VARCHAR, Data.VARCHAR]`. This is just a semplification for using the common datatypes. You can either use them in a string, like: `"INT"` or `"VARCHAR"`, or you can use them with the `Data.*`. In order to do that, you also need to import the Data.py file into the project:
```python
import SSQL.Data
```

Then, you can write `Data.*` and you'll find all the datatypes that can be used.

----

# Conclusion

This is the end of the documentation. For any problem or info, create a new `issue` on the github!
