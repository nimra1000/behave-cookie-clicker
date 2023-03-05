@cookies
Feature: Check the basic functionality of the Cookie feature

  @two
  Scenario: Retrieval of the cookie currency
    Given I login as 'Robot'
    And I should have 0 cookies
    When I click on the 'click' button
    And I click on the 'click' button
    Then I should have 2 cookies
    
  @three
  Scenario: Expenditure of cookies which do not exist
    Given I login as 'Robot'
    And I should have 0 cookies
    When I type '10' into the 'cookies-to-sell' input field
    And I click on the 'sell-cookies' button
    Then I should have 0 cookies

  @four
  Scenario: Sensible expenditure of cookies which do exist
    Given I login as 'Robot'
    And I have 3 cookies
    When I type '1' into the 'cookies-to-sell' input field
    And I click on the 'sell-cookies' button
    Then I should have 2 cookies

  @five @bug 
  Scenario: A user is not able to sell their cookies if the amount entered is equal to the current balance
    Given I login as 'Robot'
    And I have 5 cookies
    When I type '5' into the 'cookies-to-sell' input field
    And I click on the 'sell-cookies' button
    Then I should have 0 cookies

#  @bug Scenario: A user is not able to sell their cookies if the amount entered is equal to the current balance
