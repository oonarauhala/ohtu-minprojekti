*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page And Log In
Test Teardown  Log Out

*** Test Cases ***
Click Uusi Kirjavinkki Link
    Click Link  Uusi kirjavinkki
    New Book Page Should Be Open

Click Uusi Blogivinkki Link
    Click Link  Uusi blogivinkki
    New Blog Page Should Be Open

Click Uusi Videovinkki Link
    Click Link  Uusi videovinkki
    New Video Page Should Be Open

Click Uusi Podcastvinkki Link
    Click Link  Uusi podcastvinkki
    New Podcast Page Should Be Open

Click Lista Link
    Click Link  Lista
    List Page Should Be Open


