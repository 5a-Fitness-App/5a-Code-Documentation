.. _friends-page:

Friends Page
============

**Source File:** ``flutter/lib/frontend/modal/show_friends_modal.dart``

Overview
--------
The Friends Page is a modal page that allows users to view and manage their social connections. It displays pending friend requests and the current friends list, and provides options to accept, reject, or remove connections.

UI Structure
------------
1. **Header**
   - Back button
   - Page title: "Friends"
2. **Friend Requests Section**
   - Header: "Friend Requests"
   - List of `FriendRequestWidget` items, each with:
     - Avatar
     - Username
     - Accept and decline buttons
3. **Friends List Section**
   - Header: "Your Friends"
   - List of `FriendWidget` items, each with:
     - Avatar
     - Username
     - "Remove Friend" button

Widget Hierarchy
----------------
- ``FriendsPage`` (ConsumerWidget)
  - Builds the entire modal view
  - Renders two lists (requests and current friends)

Components
----------

FriendRequestWidget
^^^^^^^^^^^^^^^^^^^
Represents a single pending friend request.

**UI Elements:**
- Avatar (dynamic asset)
- Username
- Accept button
- Decline button

FriendWidget
^^^^^^^^^^^^
Represents an existing friend connection.

**UI Elements:**
- Avatar (dynamic asset)
- Username
- "Remove Friend" button

State Management
----------------
- Uses Riverpod `userNotifier` to access:
  - `incomingFriendRequests`
  - `friendUserData`
- Uses methods from the notifier to:
  - Accept/reject requests
  - Remove friends

Methods
-------
- `acceptFriendRequest(friendID)`
- `declineFriendRequest(friendID)`
- `removeFriend(friendID)`



Image Reference
---------------
.. image:: ../_static/friends_page.png
   :width: 400px
   :align: center