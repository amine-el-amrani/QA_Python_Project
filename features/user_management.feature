Feature: User management
  Scenario: Create a new user
    Given I am an API client
    When I send a POST request to /users with name "Test User"
    Then I should receive a 201 status code
    And the user "Test User" should be created