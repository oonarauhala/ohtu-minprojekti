*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Log In Correctly
    Input Login Info  testikayttis  HyväSalasana
    Click Button  Kirjaudu
    Main Page Should Be Open
