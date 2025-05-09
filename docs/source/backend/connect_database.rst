Database Connection
===================

**File:** `flutter/lib/backend/services/db_service.dart`

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