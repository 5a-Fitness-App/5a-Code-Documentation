.. _login-screen:

Login Screen
============

**File:** `flutter/lib/frontend/states/login_screen.dart`



Overview: 
---------
This screen is used to authenticate credentials when signing in. 
It is the main screen when you open the app and are required to either sign up or sign in.

Widget Hierarchy
---------------
- ``LoginScreen`` (ConsumerStatefulWidget)
  - ``LoginScreenState`` (ConsumerState)
    - Form (Sign In/Sign Up)
    - Various form fields
    - Profile image selectors

Components
-------------------------

WeightUnitsLabel Enum
^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Value
     - Label
   * - kg
     - "kg"
   * - lb
     - "lb"

LoginScreen Class
^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Description
   * - registerOverride
     - Optional function override for registration

LoginScreenState Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - signUpFormKey
     - GlobalKey<FormState>
     - Form validation key
   * - emailController
     - TextEditingController
     - Email input controller
   * - selectedProfileImage
     - String
     - Currently selected image (default: 'fish')
   * - registrationMode
     - bool
     - Toggles between forms (default: false)

Methods 
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Method
     - Description
   * - _selectImage()
     - Sets profile image
   * - _selectDate()
     - Shows date picker
   * - login()
     - Handles sign-in
   * - registerButton()
     - Handles registration
   * - buildSignInForm()
     - Returns login form widget
   * - buildSignUpForm()
     - Returns registration form widget



Sign In Form
------------
**Fields:**
- Email (required, valid format)
- Password (required, toggle visibility)



Sign Up Form
------------
**Fields:**
- Profile Image (fish/shark/crab/dolphin)
- Username (required, alphanumeric)
- Email (same as sign-in)
- Password + Confirm (must match)
- Birthday (date picker)
- Weight + Unit (kg/lb)

UI Structure (From build() method)
---------------------------------
1. Gradient header with logo
2. Form toggle buttons
3. Dynamic form area showing either:
   - Sign In form (email + password)
   - Sign Up form (all fields + profile images)

Image Assets Used
----------------
From ``assets/`` directory:
- Logo.png
- fish.png
- shark.png
- crab.png
- dolphin.png

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

Image References
-----------------
.. image:: ../_static/login_screen_registration2.png
   :width: 400px
   :align: center

.. image:: ../_static/login_screen_sign_in.png
   :width: 400px
   :align: center