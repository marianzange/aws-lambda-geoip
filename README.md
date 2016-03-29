# IP based geo-location with AWS Lambda

This is a simple Python handler for AWS Lambda to determine a user's geo-location based on their IP. To map IP's to countries (or cities if you choose), we use MaxMind's GeoLite2 database which can be downloaded here: https://dev.maxmind.com/geoip/geoip2/geolite2/

## Exposing through Amazon API Gateway

There are many ways to configure API Gateway to fit your needs. The minimum things you need to do to expose this lambda function are the following:

  1. Create a new resource and add a GET method
  2. To the *Body Mapping Templates* in the *Integration Request* add the following:
  
  ```json
  {
    "requesterIp" : "$context.identity.sourceIp"
  }
  ```
  
  3. Congrats! This is the minimal setup to request your lambda function through API gateway.

