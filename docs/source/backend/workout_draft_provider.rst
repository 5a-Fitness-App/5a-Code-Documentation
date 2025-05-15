Workout Draft Provider
====================

**File**: flutter/lib/backend/models/workout_dart.dart

Models
---------------------

This module defines the data models for workouts and activities in a fitness app.

Weight Units
~~~~~~~~~~~~~~~~~~~~

.. enum:: WeightUnitsLabel

   Represents supported weight units.

   - **kg**: Kilograms
   - **lb**: Pounds

.. data:: entries

   :type: List[DropdownMenuEntry[WeightUnitsLabel]]

   A list of dropdown menu entries for selecting weight units.

Distance Units
~~~~~~~~~~~~~~~~~~~~

.. enum:: DistanceUnitsLabel

   Represents supported distance units.

   - **mi**: Miles
   - **km**: Kilometers

.. data:: entries

   :type: List[DropdownMenuEntry[DistanceUnitsLabel]]

   A list of dropdown menu entries for selecting distance units.

ActivityDraft Class
~~~~~~~~~~~~~~~~~~~~

.. class:: ActivityDraft

   Represents a draft of a single activity (e.g., a workout set or cardio run).

   **Constructor Parameters**:

   - **activityDraftID**: Unique ID for the draft.
   - **exerciseType**: Type of exercise (e.g., Running, Squat).
   - **metrics**: List of metrics associated with this activity.
   - **notesController**: Text controller for notes.
   - **setsController**, **repsController**, **hoursController**, etc.: Various `TextEditingController`s to capture user input.

   **Optional Fields**:

   - **selectedWeightUnit**: The unit selected for weight.
   - **selectedDistanceUnit**: The unit selected for distance.

   .. method:: copyWith({weightUnit, distanceUnit})

      Creates a modified copy of the activity, replacing specified unit selections.

   .. method:: toMap()

      Converts the activity to a `Map<String, dynamic>` for serialization or database storage.

WorkoutDraft Class
~~~~~~~~~~~~~~~~~~~~

.. class:: WorkoutDraft

   Represents a full workout composed of multiple `ActivityDraft` instances.

   **Fields**:

   - **activities**: List of `ActivityDraft` instances.
   - **captionController**: Text controller for the workout caption.

   .. method:: copyWith({activities})

      Returns a modified copy of the workout.

   .. method:: toMap()

      Serializes the workout and all its activities into a map.

WorkoutDraft Notifier Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. class:: WorkoutDraftNotifier

   Handles all operations related to creating and managing workout drafts.

   **Constructor Parameters**:

   - **ref** (*Ref*): A reference to the provider container.

   **Initial State**: 
   - Empty activities list
   - New TextEditingController for caption

   .. method:: getActivities()

      Returns the current list of activities in the draft.

      :return: List<ActivityDraft> of current activities

   .. method:: addActivity(exerciseName, metrics)

      Adds a new activity to the workout draft.

      :param exerciseName: Name of the exercise
      :param metrics: List of relevant metrics for this exercise type

      **Creates**:
      - New ActivityDraft with all required controllers
      - Auto-incremented activityID

   .. method:: deleteActivity(activity)

      Removes an activity from the workout draft.

      :param activity: ActivityDraft to remove

   .. method:: setDistanceUnit(activity, distanceUnit)

      Updates the distance measurement unit for a specific activity.

      :param activity: ActivityDraft to modify
      :param distanceUnit: New distance unit (DistanceUnitsLabel)

   .. method:: setWeightUnit(activity, weightUnit)

      Updates the weight measurement unit for a specific activity.

      :param activity: ActivityDraft to modify
      :param weightUnit: New weight unit (WeightUnitsLabel)

   .. method:: post()

      Posts the completed workout draft to the backend.

      :return: String with post status message

      **Workflow**:
      1. Converts draft to map format
      2. Gets current user ID
      3. Sends workout to API
      4. Clears draft state
      5. Returns success message

   .. method:: cancel()

      Cancels the current draft and resets all fields.


Dependencies
--------------

- Uses :class:`userNotifier` to get current user ID
- Relies on backend API function:
  - :func:`addWorkout`

Example Usage
--------------

.. code-block:: dart

   // Watch the draft state
   final draft = ref.watch(workoutDraftNotifier);
   
   // Add an activity
   ref.read(workoutDraftNotifier.notifier).addActivity('Running', ['distance', 'time']);
   
   // Update units
   ref.read(workoutDraftNotifier.notifier).setWeightUnit(activity, WeightUnitsLabel.lb);
   
   // Post workout
   final result = await ref.read(workoutDraftNotifier.notifier).post();
   
   // Cancel draft
   ref.read(workoutDraftNotifier.notifier).cancel();
