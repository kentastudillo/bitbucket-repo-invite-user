# Create a Bitbucket Repository

Create a bitbucket repository using the bitbucket api and AWS Lambda.

## Installation

Create an aws lambda function and upload the compressed code **create-bitbucket-repo.zip**.

Create an api gateway as a trigger.

## Calling the function

Headers

* **Content-Type** - The app requires the *application/json* content type.

Parameters

* **user** - (*required*) Your Bitbucket username.

* **pass** - (*required*)  Your Bitbucket password.

* **team** - (*required*) Your Bitbucket team. Go to Bitbucket profile and select Teams to check your teams.

* **repo_name** - (*required*) The name of the repository that you are trying to create.

* **data** - (*optional*) Customize the parameters. The application already have a default data. See [Bitbucket API](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D/%7Brepo_slug%7D#put) for the list of parameters.

## Sample Request

```
curl -X POST -H "Content-Type: application/json" \
https://5m5ds9xoix.execute-api.us-east-1.amazonaws.com/prod/create-bitbucket-repo \
-d '{"user": "john.doe@example.com, "pass": "pA$$w0rd", "team": "ateam", "repo_name": "new-repo"}'
```