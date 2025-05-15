User Provider
====================


User Model
-----------
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