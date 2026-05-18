Feature: Positive Testing

  Background:
    Given  I access the Lm.web homepage
    When I insert username
    And  I insert password
    And  I click login button
    And I should be logged in and I should see the LM.web homepage

    @positive_testing
  Scenario:
    And I click Succursales button
    And I select one succursale from the list
    And I click on modify succursale
    And I delete the current name
    And I modify the name or the limit
    And I click on save succursale
    Then I click on Logout button