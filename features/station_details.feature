# Created by wwtki at 01.04.22
Feature: Station details
  # Confirm that we can browse the home page, select a station and show the station details

  Scenario: Success for visiting station details pages
    Given I navigate to the home page
    When I choose a station and click on it
    Then I should see the details for that station

