*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Try Registering As    testuser    testpassword1
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Try Registering As    aa    testpassword1
    Registration Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Try Registering As    testuser    aa1
    Registration Should Fail With Message    Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Try Registering As    testuser    testpassword
    Registration Should Fail With Message    Password must contain both letters and numbers

Register With Nonmatching Password And Password Confirmation
    Try Registering As    testuser    testpassword1    notthesame
    Registration Should Fail With Message    Passwords do not match

Register With Username That Is Already In Use
    Create User    testuser    testpassword1
    Try Registering As    testuser    testpassword2
    Registration Should Fail With Message    User with username testuser already exists

Login After Successful Registration
    Try Registering As    testuser    testpassword1
    Try Login As    testuser    testpassword1
    Login Should Succeed

Login After Failed Registration
    Try Registering As    aa    aa
    Try Login As    aa    aa
    Login Should Fail


*** Keywords ***
Reset Application And Go To Register Page
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

Try Login As
    [Arguments]    ${username}    ${password}
    Go To Login Page
    Input Text    username    ${username}
    Input Text    password    ${password}
    Click Button    Login

Try Registering As
    [Arguments]    ${username}    ${password}    ${password_confirmation}=${None}
    Go To Register Page
    Set Username    ${username}
    IF    ${{$password_confirmation is None}}
        Set Password    ${password}    ${password}
    ELSE
        Set Password    ${password}    ${password_confirmation}
    END
    Submit Registration

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open
