Feature: UI Test Automation Playground

  @tag-005
  Scenario: Dynamic ID test - positive case (use of stable selector based on element's text)
    Given the UI Playground page is launched
    When the user clicks "Dynamic ID" link to navigate to "Dynamic ID" page
    And the user clicks button with text "Button with Dynamic ID"
    Then the user should be still on the "Dynamic ID" page


  @tag-006
  Scenario: Dynamic ID test - negative case (use of unstable selector based on element's ID)
    Given the UI Playground page is launched
    When the user clicks "Dynamic ID" link to navigate to "Dynamic ID" page
    And the user waits for the button with ID "#d27033bd-d3fc-f16c-db74-6e27579059cc" to be visible for "3" seconds
    Then the button with ID "#d27033bd-d3fc-f16c-db74-6e27579059cc" should not be visible