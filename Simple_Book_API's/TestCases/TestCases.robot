*** Settings ***

Library     SeleniumLibrary
Library     OperatingSystem
Resource     C:/Users/Hp/Desktop/Simple_Book_API's/Keywords/Keywords.robot

*** Test Cases ***
#Tc_001
Verify the simple book API'S

    
    Given Generate API Token for Authentication    
    When Configure Submit the order
    And Configure Get an order
    And Configure Update an order
    And Configure Get all orders
    And Configure Delete an order
    And Configure list of books
    Then Configure the Single book ID

