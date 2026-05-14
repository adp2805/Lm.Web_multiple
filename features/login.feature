Feature: This feature will validate the functionality of the login page

  Scenario: Positive Testing: Valid username, valid password => login successful
    Given  I access the Lm.web homepage
    When I insert username
    And  I insert password
    And  I click login button
    And I should be logged in and I should see the LM.web homepage
    And I click Succursales button
    And I select one succursale from the list
    And I click on modify succursale
    And I delete the current name
    And I modify the name or the limit
    And I click on save succursale
    And I click on home button
    And I click on regional center button
    And I click on succursale drop_down list
    And I select the succursale from the list
    And I select the second regional center from the list
    And I click on modify button
    And I clear the phone number text box
    And I complete with a new phone number
    And I click on save
    And I click on home button
    And I click on retailers section
    And I click on select retailer by id
    And I insert retailer ID
    And I click on search retailer
    And I select the firs retailer
    And I click on modify retailer
    And I clear the name
    And I insert the new name
    And I clic on save retailer
    And I click on Terminal section
    And I click on ID to search a terminal by ID
    And I fill-out the terminal id
    And I click on search button
    And I click on the selected terminal
    And I click on modify terminal button
    And I manage group allocation
    And I click on save terminal
   # And I should not see any err message: {err}
    And I click on home button
    And I should get back to the homepage
    Then I click on Logout button
    @regresion
  Scenario Outline: Negative Testing: Login unsuccessful - INVALID CREDENTIALS
    Given I access the Lm.web homepage
    When I insert username "<username_value>"
    And I insert password "<password>"
    And I click login button
    Then I should receive an unsuccessful login message: "<expected_err_message>"
    Examples:
      | username_value | password | expected_err_message       |
      | editec         | editec1  | Wrong username or password |
      | editec1        | editec   | Wrong username or password |
      | editec1        | editec1  | Wrong username or password |
      | null           | editec   | Wrong username or password |
      | editec         | null     | Wrong username or password |
      | editec1        | null     | Wrong username or password |
      | null           | editec1  | Wrong username or password |
      | null           | null     | Wrong username or password |




