Testing
=======

To ensure stability and reliability, the app is tested using Flutter’s built-in testing tools.

How to Run Tests
----------------

- Navigate to the `test` folder under `flutter/test/` to open and run any of the test files related to their respective areas.
- Tests are written based on the specifications outlined in the **5A Test Plan**, which defines test scenarios, expected outcomes, and coverage.

Test Types
----------

- **Unit Tests**: Validate business logic.
- **Widget Tests**: Ensure UI components render and behave as expected.
- **Backend Tests**: Verify that the app can correctly execute CRUD operations with the database.
- **Integration Tests**: Simulate full flows (e.g., signing in, starting a workout, saving progress).

Test Structure
--------------

Each test file corresponds to a major module or feature, such as:

- Login
- Workouts
- Profile tracking

Tests are created to validate that certain operations work, based on the **5A Test Plan**.

Problems Encountered
--------------------

- **Mock Database**: Issues with creating a mock database. Many of the test errors are believed to have stemmed from mock data entries failing to load due to the app's high reliance on the database.
- **ElevatedButton.icon**: Issues with finding `ElevatedButton.icon` elements in widget tests. These buttons had to be located by identifying only the icon, which may be unreliable.
- **Flaky Tests**: Ongoing work includes improving test coverage and refining test setups to reduce test flakiness.
