Home Page
=========

**File:** `lib/home_page.dart`

The Home Page is the main page the user will enter after logging in/ signing up. 
It will display the user's fitness progress, including daily streak goals, workout logging options, and recent activity posts from other users.

Components
----------

- **Streak Section:** Displays a circular progress indicator at the top of the page, showing the percentage of daily goals met using `CircularPercentIndicator`.
    - The Streak is updated daily as long as the user maintains their activity on the app
    - The Streak is lost when the user has not been active for more than 48hrs 
- **Log Workout / Start Workout:** Buttons allow navigation to the workout logging screen or starting a workout.
    - Log workout screen takes the user to page where they can input their finished workout with details like duration, type and descpription of the workout. 
    - Start workout button allows the user to time their current workout and ....
- **Recent Activity Feed:** Dynamically displays friends and user workout posts .
    - At the center of the home page the user will be able to views their posts and their friends posts of recent workouts uploaded 
    - The user will also be able to interact with these posts with features like comments and likes.

How it works
-----

- Integrate workout post fetching from PostgreSQL.
- Connect button actions to navigation and backend logic.