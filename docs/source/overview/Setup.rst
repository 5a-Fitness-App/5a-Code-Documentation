Setup & Installation
=====================

The project repository can be found at:  
**https://github.com/5a-Fitness-App/fitness.git**

This document outlines how to set up, configure, and run the Fitness App locally.

Setup
---------
1. open psql and create the local database
    .. code-block:: sql
        CREATE DATABSE testfitness;

        \c testfitness;

2.  Navigate to: 'database/database.sql'. Copy all and paste into the terminal. ensure that you are in the testfitness database in psql

3. Once the database is created, you are ready to run the flutter app. Ensure that you change the following:
    a. In the file lib/main.dart, change localhost to the appropriate host id 
        .. code-block:: dart
            await dbService.init('localhost'); // TODO: '10.0.2.2' only works for android studio emulator, use 'localhost' for Xcode
    b. In the file 'lib/services/dbService.dart', change the connection details to your psql details
        .. code-block:: dart
            connection = await Connection.open(
                Endpoint(
                    host: host, // TODO: change the host id in main.dart
                    database:
                        'testfitness', // TODO: change this to what you have named the database in psql
                    username: 'jennydoan', // TODO: change this to your postgres username
                    password: 'Elgado29#', // TODO: change this to your postgres password
                ),
                settings: const ConnectionSettings(sslMode: SslMode.disable),
            );


System Requirements
-------------------
Before getting started, ensure the following tools are installed:

- [Flutter SDK](https://flutter.dev/docs/get-started/install) (>= 3.5.0)
- Dart SDK (included with Flutter)
- Git (for version control)
- PostgreSQL (>= 13) — used to store workout and user data
- An editor like VS Code or Android Studio
