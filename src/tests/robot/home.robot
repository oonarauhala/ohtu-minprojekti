*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Click Uusi Vinkki Link
    Click Link  Uusi vinkki
    New Page Should Be Open

Click Lista Link
    Click Link  Lista
    List Page Should Be Open