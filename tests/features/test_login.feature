Feature: Login functionality

  Background:
    Given the login page is launched


  @test-001 @test-login-page
  Scenario: Positive login case with correct credentials
    Given the user types in the correct username into the username field
    And the user types in the correct password into the password field
    When the user pushes submit button
    Then the new page url should contain "practicetestautomation.com/logged-in-successfully/" text
    And the new page should contain "successfully logged in" text
    And the "Log out" button should be displayed on the new page


  @test-002 @test-login-page
  Scenario: Negative login case with correct user and wrong password
    Given the user types in the incorrect username into the username field
    And the user types in the correct password into the password field
    When the user pushes submit button
    Then the error message should be displayed
    And the error message text "Your username is invalid!" should be displayed


  @test-003 @test-login-page
  Scenario: Negative login case with incorrect user and correct password
    Given the user types in the correct username into the username field
    And the user types in the incorrect password into the password field
    When the user pushes submit button
    Then the error message should be displayed
    And the error message text "Your password is invalid!" should be displayed


  @test-004 @test-login-page
  Scenario Outline: Login with multiple credentials both valid and invalid
    Given the user types "<username>" username into the username field
    And the user types "<password>" password into the password field
    When the user pushes submit button
    Then the page url should contain "<text>" text
    And the message "<message>" should be displayed

    Examples:
      | username   | password    | text                   | message              |
      | student    | Password123 | logged-in-successfully | Congratulations      |
      | student    | wrong_pass  | practice-test-login    | password is invalid! |
      | wrong_user | Password123 | practice-test-login    | username is invalid! |
