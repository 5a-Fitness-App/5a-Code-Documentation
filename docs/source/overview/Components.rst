Main Components
===============

This section outlines the core modules of the application and their responsibilities.

Authentication Module
----------------------
- Provides user authentication using email and password.
- Built with database authentication.
- Handles user registration, login, logout, and session management.

Workout Tracker
---------------
- Allows users to log workout entries including:
  - Type of activity (strength, cardio, yoga or etc...)
  - Duration or repetitions
  - Optional notes
- Workouts can be grouped into a single session and saved to the user’s account.
- Data is stored securely in the database.

Workout Post View
----------------------
- Displays a listview of all friends logged workouts with the most recently posted at the top.
- Each workout entry can be tapped to view more details.
- Helps users track consistency and feel the more competitive with their friends.

Profile View
-------------------
- Allows users to update personal information:
  - Display name
  - Profile picture / Avatar
  - Goals achieved
- Provides logout functionality.

