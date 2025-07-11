Feature: UI Test Automation Playground

  @test-005 @ui-playground
  Scenario: Dynamic ID test - positive case (use of stable selector based on element's text)
    Given the UI Playground page is launched
    When the user clicks "Dynamic ID" link to navigate to "Dynamic ID" page
    And the user clicks button with text "Button with Dynamic ID"
    Then the user should be still on the "Dynamic ID" page


  @test-006 @ui-playground
  Scenario: Dynamic ID test - negative case (use of unstable selector based on element's ID)
    Given the UI Playground page is launched
    When the user clicks "Dynamic ID" link to navigate to "Dynamic ID" page
    And the user waits for the button with ID "#d27033bd-d3fc-f16c-db74-6e27579059cc" to be visible for "3" seconds
    Then the button with ID "#d27033bd-d3fc-f16c-db74-6e27579059cc" should not be visible


  @test-007 @ui-playground
  Scenario: Class Attribute test - use of well defined class based selector
    Given the UI Playground page is launched
    When the user clicks "Class Attribute" link to navigate to "Class Attribute" page
    And the user clicks the blue primary button
    Then the alert message should be "Primary button pressed"


  @test-008 @ui-playground
  Scenario: Alerts - standard alert dialog handling
    Given the UI Playground page is launched
    When the user clicks "Alerts" link to navigate to "Alerts" page
    And the user clicks button with text "Alert"
    Then the alert message should be "Today is a working day. Or less likely a holiday."


  @test-009 @ui-playground
  Scenario: Alerts - confirm dialog handling - positive case (user accepts confirm type dialog message)
    Given the UI Playground page is launched
    When the user clicks "Alerts" link to navigate to "Alerts" page
    And the user clicks button with text "Confirm" and "accepts" the "Today is Friday. Do you agree?" confirm type dialog message
    Then the alert message should be "Yes"


  @test-010 @ui-playground
  Scenario: Alerts - confirm dialog handling - negative case (user dismisses confirm type dialog message)
    Given the UI Playground page is launched
    When the user clicks "Alerts" link to navigate to "Alerts" page
    And the user clicks button with text "Confirm" and "dismisses" the "Today is Friday. Do you agree?" confirm type dialog message
    Then the alert message should be "No"


  @test-011 @ui-playground
  Scenario: Alerts - prompt dialog handling - positive case (user enters value and accepts prompt type dialog message)
    Given the UI Playground page is launched
    When the user clicks "Alerts" link to navigate to "Alerts" page
    And the user clicks button with text "Prompt" enters "dogs" value and "accepts" prompt type dialog message
    Then the alert message should be "User value: dogs"


  @test-012 @ui-playground
  Scenario: Alerts - prompt dialog handling - negative case (user enters value and dismisses prompt type dialog message)
    Given the UI Playground page is launched
    When the user clicks "Alerts" link to navigate to "Alerts" page
    And the user clicks button with text "Prompt" enters "dogs" value and "dismisses" prompt type dialog message
    Then the alert message should be "User value: no answer"