User Provider
====================

**File**: flutter/lib/backend/models/user.dart

User Model
-------------

This model stores the logged in user's data for sharing the users data across the app's states

User Class
~~~~~~~~~~~~~~~~~~~~

.. class:: User

   Represents a registered user with personal and account-related information.

   **Constructor Parameters**:

   - **userID** (*int?*): Unique identifier for the user (optional).
   - **userName** (*String*): Display name of the user. Defaults to an empty string.
   - **userProfilePhoto** (*String*): File or identifier for the user's profile picture. Defaults to `'fish'`.
   - **userBio** (*String?*): Optional user biography. Defaults to an empty string.
   - **userDOB** (*DateTime*): User's date of birth (**required**).
   - **userWeight** (*double*): User's weight in `userUnits`. Defaults to `0.0`.
   - **userUnits** (*String*): Unit of weight measurement (e.g., `'kg'`, `'lb'`). Defaults to `'kg'`.
   - **accountCreationDate** (*DateTime*): Timestamp when the account was created (**required**).
   - **userEmail** (*String*): User’s email address. Defaults to an empty string.
   - **friendCount** (*int*): Number of friends. Defaults to `0`.

   .. method:: copyWith(...)

      Creates a modified copy of the `User` instance. Only provided fields are replaced.

      :param userID: (optional) New user ID
      :param userName: (optional) New user name
      :param userProfilePhoto: (optional) New profile photo
      :param userBio: (optional) New bio
      :param userDOB: (optional) New date of birth
      :param userWeight: (optional) New weight
      :param userUnits: (optional) New unit system
      :param accountCreationDate: (optional) New account creation date
      :param userEmail: (optional) New email
      :param friendCount: (optional) New friend count

User Notifier Class
~~~~~~~~~~~~~~~~~~~~

.. class:: UserNotifier

   Handles user authentication, profile management, and account operations.

   **Constructor Parameters**:

   - **ref** (*Ref*): A reference to the provider container.

   **Initial State**: 
   - Default User object with current DateTime for accountCreationDate and userDOB

   .. method:: login(email, password)

      Authenticates a user with email and password.

      :param email: User's email address
      :param password: User's password
      :return: String? (error message) or null on success

      **Workflow**:
      1. Verifies email exists in database
      2. Compares provided password with stored password
      3. On success, loads complete user profile
      4. Updates application state with user data

   .. method:: updateFriendCount()

      Updates the friend count for the current user.

      **Workflow**:
      1. Fetches current friend count from database
      2. Updates user state
      3. Refreshes both workout post lists

   .. method:: logOut()

      Logs out the current user by resetting all user data to default values.

   .. method:: deleteUserAccount()

      Permanently deletes the user account and resets application state.

      **Workflow**:
      1. Calls API to delete account from database
      2. Resets all user data to default values

User Model Structure
====================

The provider maintains these user properties:
- userID
- userName
- userEmail
- userProfilePhoto
- userBio
- userDOB
- userWeight
- userUnits (weight measurement)
- accountCreationDate
- friendCount

Dependencies
============

- Uses :class:`postNotifier` to refresh workout posts
- Relies on backend services:
  - :class:`dbService` for database queries
  - :func:`getFriendCount`
  - :func:`deleteAccount`

Example Usage
=============

.. code-block:: dart

   // Watch the user state
   final user = ref.watch(userNotifier);
   
   // Perform login
   final error = await ref.read(userNotifier.notifier).login(email, password);
   if (error != null) {
     // Handle login error
   }
   
   // Update friend count
   ref.read(userNotifier.notifier).updateFriendCount();
   
   // Logout
   ref.read(userNotifier.notifier).logOut();