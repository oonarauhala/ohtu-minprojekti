*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To New Book Page

*** Test Cases ***
Add A Book
    Input Book Info  testi  testikirjoittaja  01234  hyva kirja
    Submit lukuvinkki
    List Page Should Be Open

Add A Book Wrong
    Input Book Info  testi  \  01234  hyva kirja
    Submit lukuvinkki
    Error Page Should Be Open

