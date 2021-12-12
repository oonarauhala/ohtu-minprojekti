*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page And Log In
Test Teardown  Log Out

*** Test Cases ***
Click Merkitse Luetuksi
    Go To Lista Page
    Click Link  Merkitse luetuksi
    Element Text Should Be  (//td)[6]  kyllä