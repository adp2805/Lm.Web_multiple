Feature: Positive Testing

  Background:
    Given  I access the Lm.web homepage
    When I insert username
    And  I insert password
    And  I click login button
    And I should be logged in and I should see the LM.web homepage

  Scenario:
    And I click on Terminal section
    And I click on ID to search a terminal by ID
    And I fill-out the terminal id
    And I click on search button
    And I click on the selected terminal
    And I click on modify terminal button
    And I manage group allocation
    And I click on save terminal
    And I click on home button
    And I should get back to the homepage
    Then I click on Logout button