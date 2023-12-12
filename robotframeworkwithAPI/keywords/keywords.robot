*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    String
Library    JSONLibrary
Library     Collections
Resource    ../Locators/variables.robot

*** Keywords ***
Generate Random email
     ${random_string}=    Generate Random String    5 	[LOWER]
     ${random_email}=    Set Variable    ${random_string}@example.com
     set suite variable    ${random_email}
     Log    Random Email: ${random_email}

Generate API token for Authentication
    Create Session    Simplebook    ${base_url}
    ${body}     create dictionary   clientName=Ram89    clientEmail=${random_email}
    ${Response}=    POST On Session     simplebook      ${Auth_endpoint}    json=${body}
    ${token}=   get value from json  ${Response.json()}     $[accessToken]
    log to console    ${token}
    ${global_variable}=    set variable    ${token[0]}
    set suite variable    ${global_variable}
    log to console    ${global_variable}


Submit an order
    create session    simplebook     ${base_url}
    ${body1}    create dictionary    bookId=1       customerName=Ram2
    ${headers}=  create dictionary      Authorization=Bearer ${global_variable}     Content-Type=application/json
    ${response}=    post request    simplebook   ${submit-order-ep}     json=${body1}   headers=${headers}
    ${order_id}=    get value from json    ${response.json()}      $[orderId]
    log to console    ${order_id}
    ${global_order_id}=      set variable    ${order_id[0]}
    set suite variable    ${global_order_id}
    log to console    ${global_order_id}

update an order
    create session    simplebook   ${base_url}
    ${headers}=  create dictionary      Authorization=Bearer ${global_variable}     Content-Type=application/json
    ${body}=    create dictionary    customerName=shiva
    ${response}=    patch on session    ${update_order_ep}/${global_order_id}     json=${body}     headers=${headers}
    log to console    ${response.status_code}

Get an order
    create session    simplebook    ${update_order_ep}
    ${headers}=  create dictionary      Authorization=Bearer ${global_variable}     Content-Type=application/json
    ${response}=    GET On Session   simplebook    ${global_order_id}   headers=${headers}
    log to console    ${response.status_code}

Delete an order
    create session    simplebook    ${update_order_ep}
    ${headers}=  create dictionary      Authorization=Bearer ${global_variable}     Content-Type=application/json
    ${response}=    DELETE On Session    simplebook    ${global_order_id}   headers=${headers}
    log to console    ${response.status_code}








