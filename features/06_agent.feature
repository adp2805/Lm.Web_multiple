Feature: Positive Testing

  Background:
    Given  I access the Lm.web homepage
    When I insert username
    And  I insert password
    And  I click login button
    And I should be logged in and I should see the LM.web homepage

    @positive_testing
  Scenario Outline: Multiple functionalities testing
    And I click on Agent button
    And I click on Search by Id
    And I insert the Agent Id
    And i click on agent search button
    And I click on the specify agent
    And I click on modify agent
    And I manage terminals allocation
    And I clear the phone number
    And I insert the new phone number as "<phone_number>"
    And I click on add phone number
    And I click on save
    Then I click on Logout button
    Examples:
      | phone_number | expected_err |
      |0766696235    |              |


  @negative_testing
  Scenario Outline:
    When I click on Agent button
    And I click on Search by Id
    And I insert the Agent Id
    And i click on agent search button
    And I click on the specify agent
    And I click on modify agent
    And I clear agent_nb textbox
    And I insert an existing External Reference as "<agent_nb>"
    And I click on save
    Then I should see error message "<expected_err>"
    Examples:
      | agent_nb | expected_err |
      | 3        | Existe déjà  |
