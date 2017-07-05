# Invite a user to join a Bitbucket Repository

A [Supercode](http://gosupercode.com) function that invites a user to join a Bitbucket repository.

## Usage

```
import supercode

repo = supercode.call(
    "super-code-function",
    "your-supercode-api-key",
    username="john.doe@example.com",
    password="p@s$w0rd",
    accountname="ateam", # can be a team or account
    repo_slug="my-repo",
    email_address="kent@example.com")

pprint(repo)
```

**Note:** Supercode has not been launched yet. This is for internal testing only.
