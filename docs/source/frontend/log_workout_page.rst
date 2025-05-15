.. _log-workout-modal:

Log Workout Page
================

**Source File:** ``flutter/lib/frontend/modals/log_workout_modal.dart``

Overview
--------
The Log Workout Page allows users to create and submit workout logs that include a list of exercises, duration, notes, and calorie data. It provides dynamic forms based on selected activity types and includes real-time validation for metrics input.

UI Structure
------------
1. **Header Bar**
   - Cancel and Post buttons to manage submission.
2. **Workout Caption Input**
   - Free-form text area for entering comments or workout summary.
3. **Activities List**
   - Shows added exercises and their associated inputs.
4. **Add Activity Section**
   - Dropdown for selecting exercise type.
   - Button to add exercise to the list.

Exercise Type Options
---------------------
Represented by the `ExerciseTypeLabel` enum, which includes over 50 exercises grouped into categories:

- **Legs** (12)
- **Glutes** (3)
- **Chest** (5)
- **Back** (9)
- **Shoulders** (7)
- **Arms** (9)
- **Core** (8)
- **Cardio** (7)

Each exercise type may require different input fields:
- Reps, sets, weight
- Time (HH:MM:SS)
- Distance, speed, incline

ActivityWidget Component
------------------------
Represents a single entry in the workout log.

**UI Elements:**
- Exercise name (title)
- Metric fields (auto-generated based on exercise type)
- Notes field
- Delete activity button

**Input Validation:**
- Ensures all required fields are filled
- Validates number formatting
- Time must match `HH:MM:SS`

Data Model
----------
Each activity is stored in an `ActivityDraft` object with the following fields:

- `exerciseType`: String
- `metrics`: List of String
- `controllers`: Mapped to input fields
- `unit`: Measurement unit for weight/distance

State Management
----------------
- Powered by `workoutDraftNotifier`
- Tracks all exercises currently added
- Updates UI and internal state on every change
- Manages selected units (e.g., kg vs. lb)

Methods
-------
- `postWorkout()`: Sends the complete workout to the backend.
- Activity add/remove handlers.
- Internal state handlers for dynamic form rendering.

User Interactions
-----------------
1. Select an exercise type from dropdown
2. Fill in required fields based on exercise
3. Add notes if desired
4. Tap "Post" to submit workout

Image Reference
---------------
.. image:: ../_static/log_workout_modal.png
   :width: 400px
   :align: center