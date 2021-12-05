*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To New Book Page

*** Test Cases ***
Add A Book
    Input Book Info  testi  testikirjoittaja  01234  hyva kirja
    Submit vinkki
    #List Page Should Be Open
    Error Page Should Be Open

Add A Book Wrong
    Input Book Info  testi  \  01234  hyva kirja
    Submit vinkki
    Error Page Should Be Open

Add A Blog
    Go To New Blog Page
    Input Blog Info  testi  testikirjoittaja  wwww.fi.fi  hyva blogi
    Submit vinkki
    List Page Should Be Open

Add A Blog Wrong
    Go To New Blog Page
    Input Blog Info  testi  \  wwww.fi.fi  hyva blogi
    Submit vinkki
    Error Page Should Be Open


