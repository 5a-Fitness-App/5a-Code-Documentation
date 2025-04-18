Database Connection
===================

**File:** `lib/connect_database.dart`

Manages PostgreSQL connection and executes queries.

Key Functions
-------------

- `createUser(...)`
- `getUsers()` / `getUserById()`
- `createWorkout(...)`
- `getWorkouts()` / `getWorkoutById()`
- `updateUser(...)`
- `deleteWorkout(...)`

How it works
-----

- Add streak calculation
- Secure password hashing (already uses `crypt(...)`)