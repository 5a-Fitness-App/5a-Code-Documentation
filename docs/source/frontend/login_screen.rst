.. _login-screen:

Login Screen
============

**Source File:** ``flutter/lib/frontend/states/login_screen.dart``

Overview
--------
The Login Screen is the entry point for users to authenticate with the app. It provides both **Sign In** and **Sign Up** functionality in a dynamic UI with toggles. It also allows users to choose a profile image and input personal details like birthday and weight.

UI Structure
------------
1. **Header**
   - Gradient background with app logo
2. **Toggle Buttons**
   - Buttons to switch between "Sign In" and "Sign Up"
3. **Form Area**
   - Renders either the Sign In or Sign Up form based on mode
4. **Submit Button**
   - Triggers login or registration flow

Sign In Form
------------
**Fields:**
- Email (required, valid format)
- Password (required, toggle visibility)

Sign Up Form
------------
**Fields:**
- Profile Image (fish, shark, crab, dolphin)
- Username (required, alphanumeric)
- Email (same as Sign In)
- Password + Confirm (must match)
- Birthday (date picker)
- Weight + Unit (kg/lb)

Validation Rules
----------------
+--------------+--------------------------------------------+
| Field        | Validation                                 |
+==============+============================================+
| Email        | Required, valid format                     |
+--------------+--------------------------------------------+
| Password     | Required, min. 8 characters                |
+--------------+--------------------------------------------+
| Username     | Required, alphanumeric with _ or .         |
+--------------+--------------------------------------------+
| Weight       | Required, valid decimal number             |
+--------------+--------------------------------------------+
| Birthday     | Required, must be a past date              |
+--------------+--------------------------------------------+

Components
----------

WeightUnitsLabel Enum
^^^^^^^^^^^^^^^^^^^^^
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
^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Description
   * - registerOverride
     - Optional override for custom registration flow

LoginScreenState Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - signUpFormKey
     - GlobalKey<FormState>
     - Form validation key
   * - emailController
     - TextEditingController
     - Controls email input
   * - selectedProfileImage
     - String
     - Stores profile avatar image name
   * - registrationMode
     - bool
     - Switches between sign-in/sign-up modes

Methods
-------
.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Method
     - Description
   * - _selectImage()
     - Opens image picker and updates selection
   * - _selectDate()
     - Displays date picker for birthday
   * - login()
     - Handles sign-in submission
   * - registerButton()
     - Handles registration submission
   * - buildSignInForm()
     - Builds and returns login form
   * - buildSignUpForm()
     - Builds and returns registration form

Image Assets Used
-----------------
From ``assets/`` directory:
- logo.png
- fish.png
- shark.png
- crab.png
- dolphin.png

Image References
----------------
.. image:: ../_static/login_screen_registration2.png
   :width: 400px
   :align: center

.. image:: ../_static/login_screen_sign_in.png
   :width: 400px
   :align: center