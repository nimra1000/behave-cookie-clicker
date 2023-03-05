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
    | category        |
    | Cookies         |
    | Factories       |
    | Money           |
    And I should see the relevant input fields
    | category        |
    | cookies-to-sell |
    | factories-to-buy|
    And I should see the relevant buttons
    | category        |
    | click           |
    | sell-cookies    |
    | buy-factories   |


#  TODO:
#  @bug Scenario: If a user joins with a username used in the past (from leaderboard), the Old scores will be overwritten with the newer instance
#  @bug Scenario: Can join a game via URL manipulation (new and existing user)
#  @bug Scenario: No validation on user. E.g. Integers and Symbols can be used. Also no limit on the characters, which messes up the UI structure if the username is extremely long.
#  @bug Scenario: It is possible to join and continue any instance of the games linked on the leaderboard (unsure if this was purposeful)
#  @bug Scenario: The leaderboard for 'High Score' is not sorted in descending order of integers.


