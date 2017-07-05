""" Import required libraries """
import json
import requests

URL = "https://api.bitbucket.org/1.0/invitations/{accountname}/{repo_slug}/{email_address}"


def main(username, password, accountname, repo_slug, email_address, permission="read"):
    """ Send an invitation to join the repository. """

    response = {}
    response["type"] = "error"

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        result = requests.post(
            URL.format(
                accountname=accountname,
                repo_slug=repo_slug,
                email_address=email_address),
            auth=(username, password),
            data={"permission": permission},
            headers=headers)

        if result.status_code == 200:
            result = json.loads(result.text)
        elif result.status_code == 401:
            response["error"] = {}
            response["error"]["message"] = "Authentication failed. "
        elif result.status_code in [400, 404]:
            response["error"] = {}
            response["error"]["message"] = result.text
    except requests.exceptions.HTTPError as err:
        response["error"] = {}
        response["error"]["message"] = "Failed to connect."
    except Exception as err:
        response["error"] = {}
        response["error"]["message"] = str(err)
    else:
        response["type"] = "success"
        response["data"] = result

    return response
