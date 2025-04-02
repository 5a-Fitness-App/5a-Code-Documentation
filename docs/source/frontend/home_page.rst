Home Page
=========

**File:** `lib/home_page.dart`

The Home Page displays the user's fitness progress, including daily streak goals, workout logging options, and recent activity posts.

Components
----------

- **Streak Section:** Displays percentage of daily goals met using `CircularPercentIndicator`.
- **Log Workout / Start Workout:** Buttons allow navigation to the workout logging screen or starting a workout.
- **Recent Activity Feed:** Dynamically displays friend and user workout posts (to be fetched from backend).

To-Do
-----

- Integrate workout post fetching from PostgreSQL.
- Connect button actions to navigation and backend logic.