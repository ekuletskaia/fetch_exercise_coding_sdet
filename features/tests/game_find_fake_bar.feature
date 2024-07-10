# Created by elena.kuletsky at 7/10/2024
Feature: Game - Find Fake Bar Tests

  Background:
    Given Open the game page

  Scenario: Find Fake Bar
    When Placing 3 bars on each bowl and perform first weighing
    And Click Reset
    When Perform second weighing and finding fake bar
    And Click the button to indicate the fake bar
    And Get the alert message
    Then Verify Fake bar was found and Yay! You find it! displayed
