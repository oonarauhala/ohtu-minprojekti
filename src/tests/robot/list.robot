*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Lista Page

*** Test Cases ***
Click Merkitse Luetuksi
    Click Link  Merkitse luetuksi
    Element Text Should Be  (//td)[6]  kyllä