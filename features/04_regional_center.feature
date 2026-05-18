Feature: Positive Testing

  Background:
    Given  I access the Lm.web homepage
    When I insert username
    And  I insert password
    And  I click login button
    And I should be logged in and I should see the LM.web homepage


  Scenario:
    And I click on regional center button
    And I click on succursale drop_down list
    And I select the succursale from the list
    And I select the second regional center from the list
    And I click on modify button
    And I clear the phone number text box
    And I complete with a new phone number
    And I click on save
    Then I click on Logout button