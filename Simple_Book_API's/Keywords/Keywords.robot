*** Settings ***
Library    SeleniumLibrary
Library    chromedriver_binary
Library    String
Library    JSONLibrary
Library    Collections
Library    RequestsLibrary


Resource    C:/Users/Hp/Desktop/Simple_Book_API's/Locators/Locators.robot

*** Keywords ***
#Tc_001    
Generate API Token for Authentication
    
# Create session and make the API authentication request
    Create Session    MySession    ${Base_URL}
    ${body}    Create Dictionary    clientName=vasanth    clientEmail=Hello123@gmail.com
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${Response}    Post Request    MySession    ${Resouce_Get_API_Authentication}    data=${body}    headers=${headers}
    Log To Console    ${Response.content}
    Log To Console    ${Response.status_code}

# Extract the access token and remove square brackets and quotes
    ${Access_value}    Get Value From Json    ${Response.json()}    $..accessToken
    ${Accesstoken}     Convert Json To String    ${Access_value}
    ${Accesstoken}=    Replace String    ${Accesstoken}    [    ${EMPTY}
    ${Accesstoken}=    Replace String    ${Accesstoken}    ]    ${EMPTY}
    ${Accesstoken}=    Replace String    ${Accesstoken}    ""    ${EMPTY}
    ${Accesstoken}=    Replace String    ${Accesstoken}    "    ${EMPTY}
    Log To Console    ${Accesstoken}

# Set the cleaned access token as a global variable
    Set Global Variable     ${Accesstoken}

Configure Submit the order

    create session    MySession    ${Base_URL}
    ${headers}=    create dictionary        Authorization=Bearer ${Accesstoken}        Content-Type=application/json
    ${body}    create dictionary    bookId=3    customerName=The Vanishing Half
    ${Response}    Post Request    MySession    ${Resouce_Submit order}    data=${body}     headers=${headers}
    Log To Console    ${Response.content}
    Log To Console    ${Response.status_code}
# Extract the book order Id and remove square brackets and quotes   
    ${Order_ID_value}    Get Value From Json    ${Response.json()}    $..orderId
    ${Order_ID}     Convert Json To String    ${Order_ID_value}
    ${Order_ID}=    Replace String    ${Order_ID}    [    ${EMPTY}
    ${Order_ID}=    Replace String    ${Order_ID}    ]    ${EMPTY}
    ${Order_ID}=    Replace String    ${Order_ID}    ""    ${EMPTY}
    ${Order_ID}=    Replace String    ${Order_ID}    "    ${EMPTY}
    Log To Console    ${Order_ID}  
    Set Global Variable     ${Order_ID}

Configure Get an order   
    create session    MySession    ${Base_URL}
    ${headers}=    create dictionary        Authorization=Bearer ${Accesstoken}
    ${Response}    Get Request    MySession    ${Resouce_Get_an_order}/${Order_ID}      headers=${headers}
    Log To Console    ${Response.content}     
    Log To Console    ${Response.status_code}

Configure Update an order
    create session    MySession    ${Base_URL}
    ${headers}=    create dictionary        Authorization=Bearer ${Accesstoken}      Content-Type=application/json
    ${body}    create dictionary        customerName=The robot
    ${Response}    Patch Request    MySession     ${Resouce_Update_an_order}/${Order_ID}   data=${body}     headers=${headers}
    Log To Console    ${Response.content}    
    Log To Console    ${Response.status_code}
Configure Get all orders

    create session    MySession    ${Base_URL}
    ${headers}=    create dictionary        Authorization=Bearer ${Accesstoken}
    ${Response}    Get Request    MySession    ${Resouce_Get_all_order}        headers=${headers}
    Log To Console    ${Response.content}
    Log To Console    ${Response.status_code}
Configure Delete an order    
    create session    MySession    ${Base_URL}
    ${headers}=    create dictionary        Authorization=Bearer ${Accesstoken}
    ${Response}    Delete Request    MySession   ${Resouce_Delete_an_order}/${Order_ID}         headers=${headers}
    Log To Console    ${Response.content}  
    Log To Console    ${Response.status_code}
Configure list of books
#create the session passing the book value manually
    # create session    MySession    ${Base_URL}
    # ${Response}    GET On Session    MySession     ${Resouce_list of books}
    # ${single_value}    Get Value From Json    ${Response.json()}    $..id
    # Set Global Variable    ${single_value}
    # Log To Console    ${single_value}

    create session    MySession    ${Base_URL}
    ${Response}    GET On Session    MySession     ${Resouce_list of books}
    ${book_ids}    Get Value From Json    ${Response.json()}    $..id
    ${random_index}    Evaluate    random.randint(0, len(${book_ids})-1)
    ${random_book_id}      Set Variable     ${book_ids}[${random_index}]
    Log To Console    Random Book ID: ${random_book_id}
    Set Global Variable    ${random_book_id}
    Log To Console    ${Response.status_code}

Configure the Single book ID

    create session    MySession    ${Base_URL}
    ${Response}    GET On Session    MySession    ${Resouce_list of books}/${random_book_id}
    # ${Response}    GET On Session    MySession    ${Resouce_list of books}/${single_value}[2]
    Log To Console    ${Response.content}    
    Log To Console    ${Response.status_code}
