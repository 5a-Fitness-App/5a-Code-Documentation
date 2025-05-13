Friends Page
======================

**File:** flutter/lib/frontend/modal/show_friends_modal.dart

Overview
----------
The FriendsPage is a Flutter widget that displays a user's friends list and friend requests. It provides functionality to manage friendships including accepting/declining requests and removing friends.

Components
-----------
FriendsPage
^^^^^^^^^^^
- The main widget that displays both friend requests and friends list

Properties
~~~~~~~~~~~~~~~~~~~~
.. int:: userID
   - The ID of the currently logged in user, provided by userProvider.dart

State Management
~~~~~~~~~~~~~~~~~~~~
- Uses Riverpod's ConsumerStatefulWidget for state management 
- Maintains two futures:
   .. : friends: A list of current friends
   .. : friendRequests: List of pending friend requests

Key Features
~~~~~~~~~~~~~~~~~~~~
- Displays friend requests at the top 
- Shows friends list underneath
- Handles loading states

FriendWidget
^^^^^^^^^^^^^^^^^^
- Displays an individual friend in the friends list
- Displays their profile photo and username, which can be clicked to bring up their profile page as a bottom sheet modal

Properties
~~~~~~~~~~~~~~~~~~~~
State Management
~~~~~~~~~~~~~~~~~~~~
Key Features
~~~~~~~~~~~~~~~~~~~~

Widget
^^^^^^^^^^^^^^^^^^
Properties
~~~~~~~~~~~~~~~~~~~~
State Management
~~~~~~~~~~~~~~~~~~~~
Key Features
~~~~~~~~~~~~~~~~~~~~

*Properties* 
- friend (Map<String, dynamic>): Friend data including:
   - .. int: user_ID: Friend's userID
 - When the user taps on 'friends' underneath their usrname on the profile page it will bring up a bottom sheet modal showing their friend request and friends
 - 'showDialog' function is implemented to display the list of friends usernames
 - Provider is used to fetch the list of friends
 - View friends' profile using action button for each friend
 - Accept or decline Friend requests 


Image Reference
-----------------
.. image:: ../_static/show_friends_modal.png
   :width: 400px
   :align: center
