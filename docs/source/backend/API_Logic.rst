API Logic / Services
====================

DbService
=========

A singleton class responsible for handling PostgreSQL database operations.

This class abstracts the connection setup and provides reusable methods for executing SQL queries such as insert, read, update, and delete.

Singleton Pattern
-----------------

.. class:: DbService

   Ensures that a single shared database connection is used throughout the app.

   **Usage**:

   Use the global instance ``dbService`` to perform operations.

Initialization
--------------

.. method:: init()

   Initializes the database connection using PostgreSQL credentials and connection settings.

   - Connects to the local Postgres server (default host: ``10.0.2.2`` for Android Emulator).
   - Skips reinitialization if already connected.

CRUD Operations
---------------

.. method:: insertQuery(sql, values)

   Executes an ``INSERT`` query with named parameters.

   :param sql: The SQL query string (with named parameters).
   :param values: A map of parameter names to values.

.. method:: insertAndReturnId(sql, values)

   Executes an ``INSERT`` and returns the generated primary key (ID).

   :returns: The ID of the inserted row.

.. method:: readQuery(sql, [values])

   Executes a ``SELECT`` query and returns the result rows.

   :returns: A list of result rows (as ``ResultRow`` objects).

.. method:: updateQuery(sql, values)

   Executes an ``UPDATE`` query and returns the number of affected rows.

   :returns: Number of rows updated.

.. method:: deleteQuery(sql, values)

   Executes a ``DELETE`` query and returns the number of affected rows.

   :returns: Number of rows deleted.

Global Instance
---------------

.. data:: dbService

   A globally accessible instance of the ``DbService`` singleton.
