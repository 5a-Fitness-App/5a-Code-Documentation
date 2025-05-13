.. _log-workout-modal:


Log Workout Page
================

Source File: ``flutter/lib/frontend/modals/log_workout_modal.dart``

This screen allows users to input workout data like title, duration, and calories burned.

Overview
--------
This screen allows users to input workout data like title, duration, and specific metrics.


Components
----------

ExerciseTypeLabel Enum
^^^^^^^^^^^^^^^^^^^^^
Contains 50+ exercise types categorized by:
- Legs (12)
- Glutes (3) 
- Chest (5)
- Back (9)
- Shoulders (7)
- Arms (9)
- Core (8)
- Cardio (7)

Each specifies required metrics:
- ``sets``, ``reps``, ``weight``
- ``time`` (HH/MM/SS)
- ``distance``, ``speed``, ``incline``

LogWorkoutPage
^^^^^^^^^^^^^^
**Elements:**
1. Header with Cancel/Post buttons
2. Caption text area
3. Activities list
4. Add activity controls

**Methods:**
- ``postWorkout()`` - Submits to backend
- Handles activity management

ActivityWidget
^^^^^^^^^^^^^
**Displays:**
- Exercise name
- Dynamic fields based on metrics
- Notes field
- Delete button

**Validation:**
- Numeric fields (weight/distance)
- Time format (HH/MM/SS)
- Required fields

Data Structure
-------------
**ActivityDraft contains:**
- exerciseType (String)
- metrics (List<String>)
- Controllers for all fields
- Weight/distance units

State Management
---------------
- Uses ``workoutDraftNotifier``
- Manages activities list
- Handles unit selections

Interactions
-----------
1. Add activities via dropdown
2. Fill exercise-specific metrics
3. Add notes
4. Post or cancel


Image Reference
------------------
.. image:: ../_static/log_workout_modal.png
   :width: 400px
   :align: center