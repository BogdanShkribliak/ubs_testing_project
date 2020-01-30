Feature: Testing Main menu tabs

      In order to be able to use all tabs from main menu
      As a client
      I want to open all tabs and check that pages loaded correctly



  Scenario Outline: Checking Careers tab

    Given I am on main page
    When I click <tab_name> tab and choose <sub_tab_name> section
    Then Page <page_name> is loaded


  Examples:
  |tab_name         |sub_tab_name          |page_name               |
  |"Careers"        |"Students"            |"Students and graduates"|
  |"Careers"        |"Meet us"             |"Meet us"               |


  Scenario Outline: Checking Investment Bank tab

    Given I am on main page
    When I click <tab_name> tab and choose <sub_tab_name> section
    Then Page <page_name> is loaded


  Examples:
  |tab_name                 |sub_tab_name          |page_name       |
  |"Investment Bank"        |"What we offer"       |"What we offer" |
  |"Investment Bank"        |"In focus"            |"In focus"      |



  Scenario Outline: Checking Asset Management tab

    Given I am on main page
    When I click "Asset Management" tab and choose <sub_tab_name> section
    Then Page <page_name> is loaded


  Examples:
  |sub_tab_name        |page_name       |
  |"What we offer"     |"What we offer" |
  |"Insights"          |"Insights"      |
