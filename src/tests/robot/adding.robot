*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page And Log In
Test Teardown  Log Out

*** Test Cases ***
Add A Book
    Go To New Book Page
    Input Book Info  testi  testikirjoittaja  01234  hyva kirja
    Submit vinkki
    List Page Should Be Open

Add A Book Wrong
    Go To New Book Page
    Input Book Info  testi  \  01234  hyva kirja
    Submit vinkki
    Error Page Should Be Open

Add A Book By ISBN
    Go To New Book Page
    Input ISBN  951-31-1146-6
    Submit ISBN/URL
    Confirm Page Should Be Open

Add A Book By Wrong ISBN
    Go To New Book Page
    Input ISBN  123
    Submit ISBN/URL
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

Add A Video
    Go To New Video Page
    Input Video Info  testivideo  videon tekija  youtube.com/asgfhj  hyvä vidi
    Submit vinkki
    List Page Should Be Open

Add A Video Wrong
    Go To New Video Page
    Input Video Info  testivideo  aaa  \  paras vidi
    Submit vinkki
    Error Page Should Be Open

Add A Video By URL
    Go To New Video Page
    Input URL  https://www.youtube.com/watch?v=kffacxfA7G4
    Submit ISBN/URL
    Confirm Video Page Should Be Open

Add A Video By Wrong URL
    Go To New Video Page
    Input URL  www.youtube.com
    Submit ISBN/URL
    Error Page Should Be Open

Add A Podcast
    Go To New Podacst Page
    Input Podcast Info  podacst  julien  eka jakso  paras podcast
    Submit vinkki
    List Page Should Be Open

Add A Podcast Wrong
    Go To New Podacst Page
    Input Podcast Info  podcast  julien  \  ok
    Submit vinkki
    Error Page Should Be Open

