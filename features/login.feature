@login
Feature: Login feature

  @one
  Scenario: Ensure a smooth user journey from the Landing to the Game page and all relevant elements display
    Given I am on the Landing page
    When I type 'Robot' into the 'name' input field
    And I click on the 'Start!' button
    Then I should be redirected to the Game page
    And I should be greeted
    And I should see the relevant info 
    | category      |
    | Cookies       |
    | Factories     |
    | Money         |
    And I should see the relevant input fields
    | category      |
    | Sell Cookies  |
    | Buy Factories |
    And I should see the relevant buttons
    | category      |
    | Click Cookie! |
    | Sell Cookies! |
    | Buy Factories!|