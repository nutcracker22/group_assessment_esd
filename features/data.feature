# Created by nutcracker22 at 31.03.22
Feature: Data details
  """
  Confirm that we can browse the station_data pages on our site and select a station and show the respective data
  """

  Scenario: Success for visiting station_data pages
    Given I navigate to the data page
    When I choose a station and click 'submit'
    Then I should see the data for that station
