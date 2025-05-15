Post Provider
====================


Posts Model
===========

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