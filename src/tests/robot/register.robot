*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register Incorrectly
    Input Register Info  ansku  kissa123  kissa123
    Submit Registration
    Error Page Should Be Open

Register Correctly
    ${RANDOM NAME}  Create Random Username
    Input Register Info  ${RANDOM NAME}  kissa123  kissa123
    Submit Registration
    Main Page Should Be Open

