*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    testuser
    Set Password    testpassword1
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username    aa
    Set Password    testpassword1
    Submit Registration
    Registration Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username    testuser
    Set Password    aa1
    Submit Registration
    Registration Should Fail With Message    Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username    testuser
    Set Password    testpassword
    Submit Registration
    Registration Should Fail With Message    Password must contain both letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username    testuser
    Set Password    testpassword1    notthesame
    Submit Registration
    Registration Should Fail With Message    Passwords do not match

Register With Username That Is Already In Use
    Create User    testuser    testpassword1
    Go To Register Page
    Set Username    testuser
    Set Password    testpassword1
    Submit Registration
    Registration Should Fail With Message    User with username testuser already exists


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}    ${password_confirmation}=${password}
    Input Password    password    ${password}
    Input Password    password_confirmation    ${password_confirmation}

Submit Registration
    Click Button    Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Registration Page Should Be Open
    Page Should Contain    ${message}
