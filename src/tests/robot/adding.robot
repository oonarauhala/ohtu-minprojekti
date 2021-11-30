*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To New Page

*** Test Cases ***
Add A Title
    Input Title  testi
    Submit lukuvinkki
    List Page Should Be Open

