from datetime import date, datetime, timedelta, time

from _decimal import Decimal

from .logger import Log
from typing import Self

import mysql.connector


class SSQL:
    def __init__(self, host: str = "localhost", user: str = None, password: str = None, database: str = None,
                 logging: bool = True, logname: str = __name__):
        """
        Main class of the packet, you need to initialize this class in order to operate with MySQL. In the
        initialization process you need to specify 'host', 'user', and 'password'. Optional are 'database' and
        'logging'. If you don't specify the database from the creation of the object, you can use the function
        'connectDB(database)' to connect after.

        :param host: Field related to the host address of MySQL (default: localhost)
        :param user: Field related to the user of MySQL (e.g. admin, root)
        :param password: Field related to the MySQL user's password
        :param database: Field related to the database you want to work with
        :param logging: Boolean field related to the logging of the events of MySQL (default: True)
        :param logname: This field is related to the logging system. If logging is enabled, put here the name of the file that uses the SSQL class or methods (e.g. __name__)
        """

        # Initialization of the local variables of the class
        self.host: str = host
        self.user: str = user
        self.password: str = password
        self.database: str = database
        self.logging: bool = logging
        self.log: Log = Log(logname)
        self.last_result: list[tuple] = None
        self.connection: mysql.connector.connection.MySQLConnection | mysql.connector.connection.MySQLConnectionAbstract = None
        self.cursor: mysql.connector.connection.MySQLCursor = None

        # Checking the user inputs
        if not self.user or not self.password:
            if logging:
                self.log.logger.error("User or Password non configured correctly, be sure to input them!")

            return

        # Connection startup
        self.connect()

    def connect(self) -> Self | None:
        """
        This method is called by default in the __init__ of the class to establish a connection with MySQL. It
        connects without a database if you don't specify one when creating the object. You can call this method to
        reestablish a MySQL connection.

        :return:
        """
        # Checking if there is an active connections and close it
        if self.connection:
            self.connection.close()
            self.log.logger.info("Connection to MySQL closed!")

        # Check if the database is already specified
        if not self.database:
            # Trying the connection on the mysql server
            try:
                # Creating the connection with 'user', 'user' and 'password'
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password
                )

                # Creating the MySQL cursor
                self.cursor = self.connection.cursor()

                # Checking if logging is enabled
                if self.logging:
                    # Logging the info
                    self.log.logger.info("Connection to MySQL established!")

                return self
            # Raise an Interface Error
            except mysql.connector.errors.InterfaceError as e:
                # Checking if logging is enabled
                if self.logging:
                    # Logging the error
                    self.log.logger.error(f"Interface Error: {e.msg}")
                    return
            except mysql.connector.errors.ProgrammingError as e:
                # Checking if logging is enabled
                if self.logging:
                    # Logging the error
                    self.log.logger.error(f"Programming Error: {e.msg}")
                    return

        # Trying the connection on the mysql server with database
        try:
            # Creating the connection with 'user', 'user', 'password' and 'database'
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            # Creating the MySQL cursor
            self.cursor = self.connection.cursor()

            # Checking if logging is enabled
            if self.logging:
                # Logging the info
                self.log.logger.info(f"Connection to MySQL established! Working with {self.database}")

            return self

        # Excepting the errors!
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                self.log.logger.error("This error usually occurs because of a wrong password")
                return

    def close(self) -> Self | None:
        """
        This method allows you to close the MySQL connection with the server. You can still connect again with the
        method connect()

        :return:
        """

        if not self.connection:
            self.log.logger.error("Connection already closed!")
            return self

        # Trying the connection on the mysql server with database
        try:
            self.connection.close()

            # Checking if logging is enabled
            if self.logging:
                self.log.logger.info(f"Successfully close MySQL connection!")

            return self

        # Excepting the errors!
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                self.log.logger.error("This error usually occurs because of a wrong password")
                return

    def connectDB(self, database: str) -> Self:
        """
        This method allows you to connect to a database if you didn't specify one when creating the object.

        :param database: Database name
        :return:
        """
        if self.dbList().findB(database):
            self.database = database
            if self.logging:
                self.log.logger.info(f"Connected to Database: {database}")
                return self

        if self.logging:
            self.log.logger.error("Database not found!")
        return self

    def dbList(self) -> Self | None:
        """
        This method retrieves a list of all created databases. If a connection is not initialized, it will create one
        by default. Instead of returning a list of tuples, this method returns the object itself. Each time a query
        is executed, the class saves the results in a local variable. By returning the object, you can chain multiple
        methods together and utilize these results with subsequent methods. For example: `SSQL.dbList().find("Users")`.

        :return:
        """

        # Checking if the connection is established
        if not self.connection:
            # Connect to MySQL
            self.connect()

        # Trying the execution of the query
        try:
            # Executing the query
            self.cursor.execute("SHOW DATABASES;")
            self.log.logger.info("Executing Query")
            # Fetching the results
            result = self.cursor.fetchall()
            self.log.logger.info("Fetching Results")
            # Updating last result
            self.last_result = result
            # Returning the results
            return self
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def getDBList(self) -> list[tuple[
        Decimal | bytes | date | datetime | float | int | set[str] | str | timedelta | None | time, ...]] | None:
        """
        This method allows you to retrieve the list of all the created databases and returns it. If a connection is
        not initialized, it'll create one by default.

        :return:
        """

        # Checking if the connection is established
        if not self.connection:
            # Connect to MySQL
            self.connect()

        # Trying the execution of the query
        try:
            # Executing the query
            self.cursor.execute("SHOW DATABASES;")
            self.log.logger.info("Executing Query")
            # Fetching the results
            result = self.cursor.fetchall()
            self.log.logger.info("Fetching Results")
            # Updating last result
            self.last_result = result
            # Returning the results
            return result
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def getTableList(self) -> list[tuple[
        Decimal | bytes | date | datetime | float | int | set[str] | str | timedelta | None | time, ...]] | None:
        """
        This method allows you to retrieve the list of all the created tables in a specified database. If a
        connection is not initialized, it'll create one by default. If the database is not defined, this method won't
        work.

        Returns
        -------
        list:   list of tuple containing the tables names
        :return:
        """

        # Checking if the connection is established
        if not self.connection:
            # Connect to MySQL
            self.connect()
            if not self.database:
                self.log.logger.error(f"Interface Error: No database specified for this query")

        # Trying the execution of the query
        try:
            # Executing the query
            self.cursor.execute("SHOW TABLES;")
            self.log.logger.info("Executing Query")
            # Fetching the results
            result = self.cursor.fetchall()
            # Updating last result
            self.last_result = result
            self.log.logger.info("Fetching Results")
            # Returning the results
            return result
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def tableList(self) -> Self | None:
        """
        This method allows you to retrieve the list of all the created tables in a specified database. If a
        connection is not initialized, it'll create one by default. If the database is not defined, this method won't
        work. Instead of returning a list of tuples, this method returns the object itself. Each time a query is
        executed, the class saves the results in a local variable. By returning the object, you can chain multiple
        methods together and utilize these results with subsequent methods. For example: `SSQL.tableList().find("Customers")`.

        :return:
        """

        # Checking if the connection is established
        if not self.connection:
            # Connect to MySQL
            self.connect()
            if not self.database:
                self.log.logger.error(f"Interface Error: No database specified for this query")

        # Trying the execution of the query
        try:
            # Executing the query
            self.cursor.execute("SHOW TABLES;")
            self.log.logger.info("Executing Query")
            # Fetching the results
            result = self.cursor.fetchall()
            # Updating last result
            self.last_result = result
            self.log.logger.info("Fetching Results")
            # Returning the results
            return self
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def findB(self, search: str = "default", result: list[tuple] = None) -> bool:
        """
        With this function you can find a specified thing inside a query result. This method returns a boolean value,
        true if it finds a match, false otherwise. You can use this method alone, by giving in input the result of a
        query:

        result = SSQL.getDBList()

        boolean = SSQL.findB('Customers', result)


        or you can put it after another function that get a query result and return the SSQL object:

        boolean = SSQL.dbList().findB('Customers')


        :param search: Field related to the searching value
        :param result: (Optional) Field related to the query that need to be searched
        :return:
        """

        # Checking if the there is a result input
        if result is None:
            # Checking if there is a query result cached in the object
            if self.last_result is None:
                # Checking if the logging is enabled
                if self.logging:
                    # Log the error
                    self.log.logger.error("There is no Query Result cached in the SSQL object")
                return False

            # Iteration over the cached result
            for tupl in self.last_result:
                # Check every tuple to find the match
                if search in tupl:
                    # Checking if the logging is enabled
                    if self.logging:
                        # If found, log the event
                        self.log.logger.info(f"Search finished correctly! Found {search}!")
                    return True

            # If not found, log the event
            self.log.logger.info(f"Search finished correctly! Not found {search}!")
            return False

        # Iteration over the provided query result
        for tupl in result:
            # Check every tuple to find the match
            if search in tupl:
                # Checking if the logging is enabled
                if self.logging:
                    # If found, log the event
                    self.log.logger.info(f"Search finished correctly! Found {search}!")
                return True

        # If not found, log the event
        self.log.logger.info(f"Search finished correctly! Not found {search}!")
        return False

    def findI(self, search: str = "default", result: list[tuple] = None) -> int:
        """
        With this function you can find a specified thing inside a query result. This method returns a integer value,
        precisely, the index of where the value was found. It returns -1 if the value wasn't found You can use this
        method alone, by giving in input the result of a query:

        result = SSQL.getDBList()
        index = SSQL.findB('Customers', result)


        or you can put it after another function that get a query result and return the SSQL object:

        index = SSQL.dbList().findB('Customers')


        :param search: Field related to the searching value
        :param result: (Optional) Field related to the query that need to be searched
        :return:
        """

        index: int = 0
        if result is None:
            # Checking if there is a query result cached in the object
            if self.last_result is None:
                # Checking if the logging is enabled
                if self.logging:
                    # Log the error
                    self.log.logger.error("There is no Query Result cached in the SSQL object")
                return -1

            # Iteration over the cached result
            for tupl in self.last_result:
                # Check every tuple to find the match
                if search in tupl:
                    # Checking if the logging is enabled
                    if self.logging:
                        # If found, log the event
                        self.log.logger.info(f"Search finished correctly! Found {search}!")

                    return index

                index += 1

            # If not found, log the event
            self.log.logger.info(f"Search finished correctly! Not found {search}!")
            return -1

        # Iteration over the provided query result
        for tupl in result:
            # Check every tuple to find the match
            if search in tupl:
                # Checking if the logging is enabled
                if self.logging:
                    # If found, log the event
                    self.log.logger.info(f"Search finished correctly! Found {search}!")
                return index

            index += 1

        # If not found, log the event
        self.log.logger.info(f"Search finished correctly! Not found {search}!")
        return -1

    def _buildSQLTable(self, columns: list[str], types: list[str], values: list[int],
                       constraints: list[str] = None) -> str:

        query: str = ""
        tempquery: str = ""

        if constraints is None:
            if len(columns) == len(types) and len(types) == len(values):
                for i in range(len(columns)):
                    if values[i] == 0:
                        tempquery = query + " " + columns[i] + " " + types[i] + ","
                        query = tempquery
                    else:
                        tempquery = query + " " + columns[i] + " " + types[i] + "(" + str(values[i]) + ")" + ","
                        query = tempquery

                tempquery = "(" + query[1:-1] + ")"
                return tempquery
        else:
            if len(columns) == len(types) and len(types) == len(values) and len(values) == len(constraints):
                for i in range(len(columns)):
                    if values[i] == 0:
                        tempquery = query + " " + columns[i] + " " + types[i] + " " + constraints[i] + ","
                        query = tempquery
                    else:
                        tempquery = query + " " + columns[i] + " " + types[i] + "(" + str(values[i]) + ") " + \
                                    constraints[i] + ","
                        query = tempquery

                tempquery = "(" + query[1:-2] + ")"
                return tempquery

    def createDB(self, database: str, connect: bool = False) -> Self | None:
        """
        This function allows you to create a database. First, it checks if a database with the same name you provided
        exists. If it doesn't exist, it'll create one. You can also decide to connect directly to the new database.

        :param database: Name of the database that needs to be created
        :param connect: Allows you to connect directly to the database that has been created
        :return:
        """

        # Check if there is a connection established
        if not self.connection:
            # Create a MySQL connection
            self.connect()

        # Check if a database with the name that was provided already exists
        if self.dbList().findB(search=database):
            # Check if logging is enabled
            if self.logging:
                # Log the error
                self.log.logger.error("Database with this name already exists!")
                return self

        # Try to create the database
        try:
            # Execute the query statement with the cursor
            self.cursor.execute(f"CREATE DATABASE `{database}`;")
            # Check if logging is enabled
            if self.logging:
                # Log the affected Rows
                self.log.logger.info(f"Affected Rows: {self.cursor.rowcount}!")
            # Check if the option `connect` is True
            if connect:
                # Update the database in the settings
                self.database = database
                # Reestablish a connection with MySQL
                self.connect()

            return self
        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if lo  gging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def dropDB(self, database: str) -> Self | None:
        """
        With this method, you can delete a database form MySQL. If the database you specify doesn't exist,
        you'll get an error

        :param database: Name of the database that needs to be deleted
        :return:
        """

        # Check if there is a connection established
        if not self.connection:
            # Create a MySQL connection
            self.connect()

        # Check if a database with the name that was provided doesn't exist
        if not self.dbList().findB(search=database):
            # Check if logging is enabled
            if self.logging:
                # Log the error
                self.log.logger.error("Database with this name doesn't exist")
                return self

            # Try to drop the database
            try:
                # Execute the query statement with the cursor
                self.cursor.execute(f"DROP DATABASE `{database}`;")
                # Check if logging is enabled
                if self.logging:
                    # Log the affected Rows
                    self.log.logger.info(f"Affected Rows: {self.cursor.rowcount}!")

                return self
            # Interface Error
            except mysql.connector.errors.InterfaceError as e:
                # Checking if logging is enabled
                if self.logging:
                    # Logging the error
                    self.log.logger.error(f"Interface Error: {e.msg}")
                    return
            # Programming Error
            except mysql.connector.errors.ProgrammingError as e:
                # Checking if logging is enabled
                if self.logging:
                    # Logging the error
                    self.log.logger.error(f"Programming Error: {e.msg}")
                    return

    def createTable(self, name: str, columns: list[str], datatype: list[str], sizes: list[int],
                    constraints: list[str] = None) -> Self | None:
        """
        This function allows you to create a table inside a database. If a table with the same name already exists,
        you'll get an error. The lists `columns`, `datatype`, `sizes`, and `constraints` must all have the same
        length and the elements must be in corresponding order.

        :param name: The name of the table you want to create
        :param columns: A list of the columns name you want in the table (e.g. `['id', 'Username', 'Email']`)
        :param datatype: The type of data you want for each column (e.g. `[Data.INT, Data.VARCHAR, Data.VARCHAR]`)
        :param sizes: The max size of each column (you can put 0 for max size) (e.g. `[0, 20, 50]`)
        :param constraints: (Optional) You can put here the constraints (leave blank if you don't need anything) (e.g. `['AUTO_INCREMENT PRIMARY KEY', 'NOT NULL', '']`)
        :return:
        """

        # Check if the connection exists
        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name already exists
        if self.tableList().findB(name):
            # Log error
            self.log.logger.error(f"Table {name} already exists")
            return self

        # Try to create the table
        try:
            # Get the main query part from this other funtion that builds it
            query = self._buildSQLTable(columns=columns, types=datatype, values=sizes, constraints=constraints)
            # Build the query and executes it
            self.cursor.execute(f"CREATE TABLE `{name}` {query}")
            # Check if logging is enabled
            if self.logging:
                # Log successfully
                self.log.logger.info("Table created successfully")

            return self
        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def dropTable(self, table: str) -> Self | None:
        """
        This function allows you to drop a table by its name. If the table doesn't exist, you'll get an error.

        :param table: Table's name
        :return:
        """

        # Check if the connection exists
        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name doesn't exist
        if not self.tableList().findB(table):
            # Log error
            self.log.logger.error(f"Table {table} doesn't exist")
            return self

        # Try to drop the table
        try:
            # Execute the query
            self.cursor.execute(f"DROP TABLE `{table}`")
            # Check if logging is enabled
            if self.logging:
                # Log successfully
                self.log.logger.info("Table deleted successfully")

            return self
        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def insert(self, table: str, columns: list[str], values: list[tuple]) -> Self | None:
        """
        With this function, you'll be able to insert your data into the specified columns of a table. The number of
        columns in the column list must be the same exact number as the tuples in the value list.

        :param table: The table's name
        :param columns: The columns
        :param values: The values to insert into the table
        :return:
        """

        values_number = ["%s" for x in range(len(columns))]

        # Check if the connection exists
        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name doesn't exist
        if not self.tableList().findB(table):
            # Log error
            self.log.logger.error(f"Table {table} doesn't exist")
            return self

        try:
            query: str = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(values_number)})"
            self.cursor.executemany(query, values)
            self.connection.commit()
            if self.logging:
                self.log.logger.info(f"Affected Rows: {self.cursor.rowcount} | Last ID: {self.cursor.lastrowid}")

            return self
        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def selectAll(self, table: str, filter: str = None, order: str = None, limit: int = None, results: bool = True) -> list[tuple[
        Decimal | bytes | date | datetime | float | int | set[str] | str | timedelta | None | time, ...]] | None | Self:
        """
        This method allow you to execute the query `SELECT *` from a specified table. You can also filter the query
        by integer and conditions, order it by column, limit the number of results that the query returns. You can
        also decide if you want this function to return the query result or the SSQL object.


        :param table: Table's name
        :param filter: (Optional) Add a filter to the `SELECT *` query (e.g. `WHERE example_column = 'example'`)
        :param order: (Optional) Order the query results by column. (e.g. `ORDER BY example_column` or `ORDER BY example_column DESC`)
        :param limit: (Optional) Limit the query results (`LIMIT 10`)
        :param results: True, returns the query results. False, return the SSQL object (Default=True)
        :return:
        """

        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name doesn't exist
        if not self.tableList().findB(table):
            # Log error
            self.log.logger.error(f"Table {table} doesn't exist")
            return self

        try:
            query = ["SELECT * FROM", table]
            if filter is not None:
                query.append(filter)
            if order is not None:
                query.append(order)
            if limit is not None:
                query.append(order)

            self.cursor.execute(" ".join(query) + ";")

            result = self.cursor.fetchall()

            self.last_result = result

            if results:
                return result

            return self


        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def select(self, columns: list[str], table: str, filter: str = None, order: str = None, limit: int = None, results: bool = True) -> \
    list[tuple[
        Decimal | bytes | date | datetime | float | int | set[str] | str | timedelta | None | time, ...]] | None | Self:
        """
        This method allow you to execute the query `SELECT` from a specified table. You can also filter the query
        by integer and conditions, order it by column, limit the number of results that the query returns. You can
        also decide if you want this function to return the query result or the SSQL object.


        :param columns: List of the columns that are needed for the query
        :param table: Table's name
        :param filter: (Optional) Add a filter to the `SELECT *` query (e.g. `WHERE example_column = 'example'`)
        :param order: (Optional) Order the query results by column. (e.g. `ORDER BY example_column` or `ORDER BY example_column DESC`)
        :param limit: (Optional) Limit the query results (`LIMIT 10`)
        :param results: (Optional) True, returns the query results. False, return the SSQL object (Default=True)
        :return:
        """

        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name doesn't exist
        if not self.tableList().findB(table):
            # Log error
            self.log.logger.error(f"Table {table} doesn't exist")
            return self

        try:
            query = ["SELECT", ", ".join(columns), "FROM", table]
            if filter is not None:
                query.append(filter)
            if order is not None:
                query.append(order)
            if limit is not None:
                query.append(order)

            self.cursor.execute(" ".join(query) + ";")

            result = self.cursor.fetchall()

            self.last_result = result

            if results:
                return result

            return self


        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return
        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def delete(self, table: str, condition: str) -> Self | None:
        """
        With this method you'll be able to delete records which match a condition

        :param table: Table's name
        :param condition: The condition to delete the records (e.g. `WHERE example_column = 'example'`)
        :return:
        """

        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name doesn't exist
        if not self.tableList().findB(table):
            # Log error
            self.log.logger.error(f"Table {table} doesn't exist")
            return self

        try:
            query = f"DELETE FROM {table} {condition};"
            self.cursor.execute(query)
            self.connection.commit()

            if self.logging:
                self.log.logger.info(f"Records Deleted: {self.cursor.rowcount}")
            return self

        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return

        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def deleteAll(self, table: str) -> Self | None:
        """
        With this method you'll be able to delete all the records of a table

        :param table: Table's name
        :return:
        """

        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name doesn't exist
        if not self.tableList().findB(table):
            # Log error
            self.log.logger.error(f"Table {table} doesn't exist")
            return self

        try:
            query = f"DELETE FROM {table};"
            self.cursor.execute(query)
            self.connection.commit()

            if self.logging:
                self.log.logger.info(f"Records Deleted: {self.cursor.rowcount}")
            return self

        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return

        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return

    def update(self, table: str, column: str, value: str, condition: str) -> Self | None:
        """
        This method allows you to update all the existing records with a certain value if a condition is satisfied

        :param table: Table's name
        :param column: Column to update (e.g. `example_column`)
        :param value: Value of the update (e.g. `example_value`)
        :param condition: Condition to satisfy to update the records (e.g. `WHERE example_column = 'example'`)
        :return:
        """

        if not self.connection:
            # Connects to MySQL
            self.connect()
            # Check if the connection is linked with a database
            if self.database is None:
                # Log error
                self.log.logger.error(f"Interface Error: No database specified for this query")
                return self

        # Check if a table with the same name doesn't exist
        if not self.tableList().findB(table):
            # Log error
            self.log.logger.error(f"Table {table} doesn't exist")
            return self

        try:
            query = f"UPDATE {table} SET {column} = '{value}' {condition}"
            self.cursor.execute(query)
            self.connection.commit()

            if self.logging:
                self.log.logger.info(f"Affected Rows: {self.cursor.rowcount}")
            return self

        # Interface Error
        except mysql.connector.errors.InterfaceError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Interface Error: {e.msg}")
                return

        # Programming Error
        except mysql.connector.errors.ProgrammingError as e:
            # Checking if logging is enabled
            if self.logging:
                # Logging the error
                self.log.logger.error(f"Programming Error: {e.msg}")
                return


