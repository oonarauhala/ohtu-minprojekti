*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${NEW BOOK URL}  http://${SERVER}/new_book
${NEW BLOG URL}  http://${SERVER}/new_blog
${NEW VIDEO URL}  http://${SERVER}/new_video
${NEW PODCAST URL}  http://${SERVER}/new_podcast
${LISTA URL}  http://${SERVER}/list


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Main Page
    Go To  ${HOME URL}

Main Page Should Be Open
    Title Should Be  Etusivu

Go To New Book Page
    Go To  ${NEW BOOK URL}

Go To New Blog Page
    Go To  ${NEW BLOG URL}

Go To New Video Page
    Go To  ${NEW VIDEO URL}

Go To New Podacst Page
    Go To  ${NEW PODCAST URL}

New Book Page Should Be Open
    Title Should Be  Uusi kirjavinkki

New Blog Page Should Be Open
    Title Should be  Uusi blogivinkki

New Video Page Should Be Open
    Title Should Be  Uusi videovinkki

New Podcast Page Should Be Open
    Title Should be  Uusi podcastvinkki

Go To Lista Page
    Go To  ${LISTA URL}

List Page Should Be Open
    Title Should Be  Lukuvinkit

Error Page Should Be Open
    Title Should Be  Virhe

Input Book Info
    [Arguments]  ${otsikko}  ${kirjoittaja}  ${isbn}  ${kommentti}
    Input Text  otsikko  ${otsikko}
    Input Text  kirjoittaja  ${kirjoittaja}
    Input Text  isbn  ${isbn}
    Input Text  kommentti  ${kommentti}

Input Blog Info
    [Arguments]  ${nimi}  ${kirjoittaja}  ${url}  ${kommentti}
    Input Text  nimi  ${nimi}
    Input Text  kirjoittaja  ${kirjoittaja}
    Input Text  url  ${url}
    Input Text  kommentti  ${kommentti}

Input Video Info
    [Arguments]  ${nimi}  ${tekija}  ${url}  ${kommentti}
    Input Text  nimi  ${nimi}
    Input Text  tekija  ${tekija}
    Input Text  url  ${url}
    Input Text  kommentti  ${kommentti}

Input Podcast Info
    [Arguments]  ${nimi}  ${tekija}  ${jakson_nimi}  ${kommentti}
    Input Text  nimi  ${nimi}
    Input Text  tekija  ${tekija}
    Input Text  jakson_nimi  ${jakson_nimi}
    Input Text  kommentti  ${kommentti}

Submit vinkki
    Click Button  Luo vinkki


