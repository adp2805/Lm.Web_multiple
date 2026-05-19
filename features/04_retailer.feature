Feature: Positive Testing

  Background:
    Given  I access the Lm.web homepage
    When I insert username
    And  I insert password
    And  I click login button
    And I should be logged in and I should see the LM.web homepage


  Scenario Outline: Testing online payment limit for retailer
    And I click on retailers section
    And I click on select retailer by id
    And I insert retailer ID
    And I click on search retailer
    And I select the firs retailer
    And I click on modify retailer
    And I clear the name
    And I insert the new name
    And I modify the online payment limit with "<payment_limit>"
    And I clic on save retailer
    And I should see error message "<expected_err>"
    And I click on Logout button

    @negative_testing
    Examples:
      | payment_limit | expected_err                               |
      | 999999999     | retailer value higher than regional center |

    @positive_testing
    Examples:
      | payment_limit |   expected_err |
      | 99999         |                |
