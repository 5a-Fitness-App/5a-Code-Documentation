Profile Page
============

**File:** `flutter/lib/frontend/states/profile_page.dart`

Displays user information, including:

- Username and user profile photo
- Number of friends 
    - When this text is clicked, the friends modal is shown
- User biography

How it works
-----

- Fetch user data from backend (`getUserById`)
- Display earned achievements
- Show friends list and user-specific activity