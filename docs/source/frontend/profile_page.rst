.. _profile-page:

Profile Page
============

**Source File:** ``flutter/lib/frontend/states/profile_page.dart``

Overview
--------
The Profile Page displays a user's profile information and workout history. It also allows access to social features like viewing friends and interacting with workout posts. The interface supports modals for both friend and workout detail views.

UI Structure
------------
1. **Profile Summary**
   - Displays user avatar and username
   - Shows stats (e.g., total workouts, followers)
2. **Friend Interaction**
   - Clicking the friend count opens a modal with a full friends list
3. **Post History**
   - Lists workouts the user has logged
   - Each workout includes reactions, comments, and a view button

Widget Hierarchy
----------------
- ``ProfilePage`` (ConsumerStatefulWidget)
  - ``ProfilePageState`` (ConsumerState)
    - ``Dashboard`` (StatelessWidget)
    - ``MyPosts`` (ConsumerWidget)

Data Structure
--------------
Workout Post Data
^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Key
     - Type
     - Description
   * - user_profile_photo
     - String
     - Profile image asset name
   * - user_name
     - String
     - Poster’s username
   * - workout_date_time
     - DateTime
     - Post timestamp
   * - workout_public
     - bool
     - Visibility status
   * - workout_caption
     - String
     - Post content
   * - hasLiked
     - bool
     - Current user's like status
   * - total_likes
     - int
     - Like count
   * - total_comments
     - int
     - Comment count
   * - workout_ID
     - int
     - Unique workout identifier

Modal Components
----------------
1. **Friend Modal**
   - Triggered by clicking friend count
   - Displays `FriendsPage` from `show_friend_modal.dart`

2. **Workout Modal**
   - Triggered by clicking "View Workout"
   - Displays `MyWorkoutPage` from `show_workout_modal.dart`

Asset References
----------------
From ``assets/`` directory:
- [user_profile_photo].png (dynamic based on user data)
- Additional avatars used in friend modals

Image Reference
---------------
.. image:: ../_static/profile_page.png
   :width: 400px
   :align: center