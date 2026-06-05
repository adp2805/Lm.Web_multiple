Feature: Positive Testing

  Background:
    Given  I access the Lm.web homepage
    When I insert username
    And  I insert password
    And  I click login button
    And I should be logged in and I should see the LM.web homepage

  @positive_testing
  Scenario Outline: Testing online payment limit for succursale

    And I click Succursales button
    And I select one succursale from the list
    And I click on modify succursale
    And I delete the current name
    And I modify the name or the limit with "<succursale_name>"
    And I delete the current online payment limit
    And I insert the new value "<payment_value>"
    And I click on save succursale
    Then I click on Logout button

    Examples:
      | succursale_name            | payment_value | expected_err |
      | Editec_automatizare_python | 99999         |              |

  @negative_testing
  Scenario Outline: Testing online payment limit for retailer
    When I click Succursales button
    And I select one succursale from the list
    And I click on modify succursale
    And I delete the current name
    And I modify the name or the limit with "<succursale_name>"
    And I delete the current online payment limit
    And I insert the new value "<payment_value>"
    And I click on save succursale
    And I should see an succursale error message "<expected_err>"
    Then I click on Logout button
    Examples:
      | succursale_name            | payment_value     | expected_err                                              |
      | Editec_automatizare_python | 99999999999999999 | Limite de paiement Online doit etre entre 0 et 2147483647 |


