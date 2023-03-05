@factory
Feature: Factory features 
    
  @six
  Scenario: Purchase of a factory
    Given I login as 'Robot'
    #TODO: Once bug is fixed, change below quantity to 12
    And I have 13 cookies
    When I type '12' into the 'cookies-to-sell' input field
    And I click on the 'sell-cookies' button
    Then I should have 3 money
    When I type '1' into the 'factories-to-buy' input field
    And I click on the 'buy-factories' button
    Then I should have 0 money
    Then I should have 1 factories

  @seven @bug
  Scenario: Ensure factory can only be purchased when funds are available
    Given I login as 'Robot'
     #TODO: Once bug is fixed, we can remove this wait
    And I wait for 1 seconds
    Then I should have 0 money
    And I should have 0 factories
    When I type '1' into the 'factories-to-buy' input field
    And I click on the 'buy-factories' button
    Then I should have 0 money
    And I should have 0 factories


#  TODO:
# @bug Scenario: Users can go into a negative to purchase factories
#  Scenario: Use Timer to make sure factory is giving cookies at specified intervals
#  Scenario: Emsure quantity of factories is proportional to Cookie earning rate
#  @bug Scenario: When a user joins, the money amount is $0.0 for a second before it switches to 0
