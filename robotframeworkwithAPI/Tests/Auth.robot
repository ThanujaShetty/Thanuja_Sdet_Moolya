*** Settings ***
Resource        ../keywords/keywords.robot


*** Test Cases ***
GENERATE API TOKEN
        Generate Random email
        Generate API token for Authentication
        Submit an order
        update an order
#        Get an order
#        Delete an order
