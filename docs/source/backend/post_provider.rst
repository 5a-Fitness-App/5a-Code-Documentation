Post Provider
====================

**File**: flutter/lib/backend/models/post.dart

Posts Model
----------------

This model stores workout post data for the user and their friends. It is used for displaying the workout feed in the app.

Posts Class
~~~~~~~~~~~~~~~~~~~~

.. class:: Posts

   Represents a collection of workout data split into user and friend categories.

   **Constructor Parameters**:

   - **userWorkouts** (*List[Map[String, dynamic]]*): A list of workouts posted by the user.
   - **friendsWorkouts** (*List[Map[String, dynamic]]*): A list of workouts posted by the user's friends.

   .. method:: copyWith(userWorkouts=None, friendsWorkouts=None)

      Returns a new `Posts` object with optionally updated fields.

      :param userWorkouts: (optional) A new list of user workouts.
      :param friendsWorkouts: (optional) A new list of friends' workouts.

Posts Notifier Class
~~~~~~~~~~~~~~~~~~~~

.. class:: PostNotifier

   Handles operations related to workout posts including loading, liking, and unliking.

   **Constructor Parameters**:

   - **ref** (*Ref*): A reference to the provider container.

   .. method:: loadUserWorkouts()

      Loads the current user's workouts from the backend and updates the state.

      **Workflow**:
      1. Gets current user info from userNotifier
      2. Fetches user's workouts from API
      3. Checks like status for each workout
      4. Updates state with new workout data

   .. method:: loadFriendsWorkouts()

      Loads friends' workouts from the backend and updates the state.

      **Workflow**:
      1. Gets current user info from userNotifier
      2. Fetches friends' workouts from API
      3. Checks like status for each workout
      4. Updates state with new workout data

   .. method:: likeWorkoutPost(workoutID)

      Handles liking a workout post.

      :param workoutID: The ID of the workout to like.

      **Workflow**:
      1. Gets current user info
      2. Sends like request to API
      3. Refreshes both workout lists

   .. method:: unlikeWorkoutPost(workoutID)

      Handles unliking a workout post.

      :param workoutID: The ID of the workout to unlike.

      **Workflow**:
      1. Gets current user info
      2. Sends unlike request to API
      3. Refreshes both workout lists

Dependencies
~~~~~~~~~~~~~~~~~~~~

- Uses :class:`userNotifier` to get current user information
- Relies on backend API functions:
  - :func:`getUserWorkouts`
  - :func:`getFriendsWorkouts`
  - :func:`hasUserLikedWorkout`
  - :func:`likeWorkout`
  - :func:`unlikeWorkout`

State Management
~~~~~~~~~~~~~~~~~~~~

The provider maintains two separate lists of workouts:
1. User's own workouts
2. Friends' workouts

Each workout includes:
- Workout data
- Like status (hasLiked flag)

Example Usage
~~~~~~~~~~~~~~~~~~~~

.. code-block:: dart

   // Watch the post state
   final posts = ref.watch(postNotifier);
   
   // Load workouts
   ref.read(postNotifier.notifier).loadUserWorkouts();
   ref.read(postNotifier.notifier).loadFriendsWorkouts();
   
   // Like a workout
   ref.read(postNotifier.notifier).likeWorkoutPost(123);