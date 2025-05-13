Login Screen
============

**File:** `flutter/lib/frontend/states/login_screen.dart`


.. contents:: Table of Contents
   :local:
   :depth: 2


Overview: 
---------
This screen is used to authenticate credentials when signing in. 
It is the main screen when you open the app and are required to either sign up or sign in.



UI Components
-------------

Header Section
^^^^^^^^^^^^^^
- Displays the application logo and name "FitFish"
- Features a gradient background from light blue to darker blue

Form Toggle
^^^^^^^^^^^
- Two tab-style buttons for switching between "Sign In" and "Sign Up" modes
- Visual indicator shows active form

Authentication Forms
^^^^^^^^^^^^^^^^^^^

Sign In Form
~~~~~~~~~~~~
.. figure:: /_static/login_form.png
   :width: 300
   :align: center
   :alt: Sign In Form

   The login form with email and password fields.

Fields:
- **Email**: Validates email format
- **Password**: Includes visibility toggle

Sign Up Form
~~~~~~~~~~~~
.. figure:: /_static/register_form.png
   :width: 300
   :align: center
   :alt: Sign Up Form

   The registration form with additional fields.

Fields:
- Profile image selection (fish, shark, crab, dolphin)
- Username
- Email
- Password (with confirmation)
- Birthday (date picker)
- Weight (with kg/lb selector)

API Reference
-------------

LoginScreen Class
^^^^^^^^^^^^^^^^^
.. autoclass:: LoginScreen
   :members:
   :exclude-members: build, createState

Properties
~~~~~~~~~~
.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - registerOverride
     - Function?
     - Optional registration function override for testing

LoginScreenState Class
^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: LoginScreenState
   :members:
   :exclude-members: build

State Properties
~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - registrationMode
     - bool
     - Toggles between login/registration views
   * - hidePassword
     - bool
     - Controls password visibility
   * - selectedProfileImage
     - String
     - Currently selected profile avatar
   * - selectedWeightUnit
     - WeightUnitsLabel?
     - Selected weight measurement unit

Methods
~~~~~~~
.. automethod:: LoginScreenState.login
.. automethod:: LoginScreenState.registerButton
.. automethod:: LoginScreenState._selectDate
.. automethod:: LoginScreenState._selectImage

Enums
-----
WeightUnitsLabel
^^^^^^^^^^^^^^^^
.. autoclass:: WeightUnitsLabel
   :members:

Validation Rules
---------------
+----------------+-----------------------------------------------+
| Field          | Validation Criteria                           |
+================+===============================================+
| Email          | - Required                                    |
|                | - Valid email format                          |
+----------------+-----------------------------------------------+
| Password       | - Required                                    |
|                | - Minimum 8 characters                        |
+----------------+-----------------------------------------------+
| Username       | - Required                                    |
|                | - Alphanumeric with underscores/dots          |
+----------------+-----------------------------------------------+
| Weight         | - Required                                    |
|                | - Valid decimal number                        |
+----------------+-----------------------------------------------+
| Birthday       | - Required                                    |
|                | - Must be in past                             |
+----------------+-----------------------------------------------+

Error States
------------
.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Error Case
     - User Feedback
   * - Invalid email
     - "Enter a valid email address"
   * - Existing account
     - "An account with this email already exists"
   * - Password mismatch
     - "Passwords do not match"
   * - Invalid credentials
     - "Login failed. Please check your credentials"



See Also
--------
:ref:`friends-page` - The social connections interface
:ref:`user-profile` - User profile management screen