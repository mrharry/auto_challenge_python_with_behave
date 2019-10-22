Feature: Validate the login page

  Background:
    Given I navigate to the login page

  Scenario: When I navigate to the login page
    Then I should see the Free Agent Login page

  Scenario: When I log in with an incorrect email/password combination
    When I login with an "invalid" credential combination
    Then I should see the invalid credentials login error message
      """
      The email and password you entered were incorrect
      """

  Scenario: When I log in with a valid registered email/password combination
    When I login with a "registered" credential combination
    Then I should see the Free Agent Overview page