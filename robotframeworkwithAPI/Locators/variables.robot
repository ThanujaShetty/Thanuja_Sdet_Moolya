*** Settings ***
Resource       ../keywords/keywords.robot
Resource        ../keywords/keywords.robot

*** Variables ***
${base_url}                 https://simple-books-api.glitch.me


${Auth_endpoint}            /api-clients/
${submit-order-ep}          /orders
${book_list_ep}                /books
${single_book_ep}           /books/:bookId
${update_order_ep}         /orders/



