# Backend created by Node.js

## Build Setup
```bash
# Install dependencies
npm install

# Serve with hot reload at localhost:4000
npm start

# Run Unit test to ensure your setup is well done
npm run unit-test
```
## Remember to add credential information in .env
- Rename .env.example to .env
- Then change the following in .env
    - DB_USER=XXX
    - DB_PASS=XXX
    - MYSQL_DB=XXX
    - JWT_KEY=XXX
    - TWILIO_ACCOUNT_SID=XXX
    - TWILIO_AUTH_TOKEN=XXX
    - TELL=09XXX
- Replace GOOGLE_EMAIL_USER and GOOGLE_EMAIL_PASS in .env.example
    - Tutorial: [How to obtain Google App Passwards?](https://lininu.blogspot.com/2017/09/NodeJSSendMailService.html)

## Find restful-api examples
- Go to /backend/myapp/test/app.http and use the file to make requests
- [2021.05.20 Update] Since I added validation of JWT, thus /backend/myapp/test/app.http won't work anymore. Instead, use /backend/myapp/test/app-jwt.http to make requests.
    - Step 1: POST data to enroll user to Database 
    - Step 2: Login with correct username and password by POST and obtain the JWT 
    - Step 3: Replace the string after Bearer at the value of @authorization in /backend/myapp/test/app-jwt.http
    - Step 4: Test another requests to ensure you can use user service.
- Basic authentication for Python Server request
    - ![](https://i.imgur.com/6fayR5S.png)
    - In order to make request from Python Server, please replace those XXX with the credentials I posted in Trello -> backend.

## Use Google Cloud Vision API
- Examples. Please refer to [Examples - Try the API](https://cloud.google.com/vision/)
- Requirement:
    - Authentication: There are two ways to authenticate. One is by setting the environment variable, the other is by generating API key. Choose either one of those to authenticate. However, it's easier to use API key. 
        1. Step by step tutorial to generate environment variable. Please refer to [Getting started with authentication](https://cloud.google.com/docs/authentication/getting-started)
        2. Step by step tutorial to generate API key. Please refer to [Using API keys](https://cloud.google.com/docs/authentication/api-keys)
            - Remember to replace XXX in GOOGLE_VISION_API_KEY=XXX with the API key obtained from GCP.
- Miscellany
    - POST data:
        - How to post data? Please refer to [Authenticating to the Cloud Vision API](https://cloud.google.com/vision/product-search/docs/auth)
        - The requirement of posting data. Please refer to [POST data requirement](https://cloud.google.com/vision/docs/request)
    - Pricing. Please refer to [Pricing](https://cloud.google.com/vision/pricing)
    


### Let's GOGOGO!
