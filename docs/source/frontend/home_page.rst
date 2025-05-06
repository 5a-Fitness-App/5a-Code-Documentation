Home Page
=========

**File:** `lib/home_page.dart`

The Home Page is the main page the user will enter after logging in/ signing up. 
It will display the user's fitness progress, including daily streak goals, workout logging options, and recent activity posts from other users.

Components
----------

- **Streak Section (Hard Coded):** Displays a circular progress indicator at the top of the page, showing the percentage of daily goals met using `CircularPercentIndicator`.
    - If this section was fully functional: 
        - The Streak is updated daily as long as the user maintains their activity on the app
        - The Streak is lost when the user has not been active for more than 48hrs 
        - The percentage would change
- **Log Workout:** Log workout button opens the log workout modal
    - Log workout screen takes the user to page where they can input their finished workout with details like duration, type and description of the workout. 
- **Recent Activity Feed:** Dynamically displays friends and user workout posts .
    - At the center of the home page the user will be able to views their posts and their friends posts of recent workouts uploaded 
    - The user will also be able to interact with these posts with features like comments and likes.
    - Refreshes with changes

How it works
-----

- A post provider hold a two list of posts: one for the user, and one for the user's friends
    - located in backend/providers/post_provider.dart
    - There are two methods of the provider to update the provider with the each of the lists
    - located in api.dart is two functions....
- Connect button actions to navigation and backend logic.