"""Functions needed to access the Confluence API."""
import os
import sys

try:
    import requests
except ImportError:
    sys.stderr.write("You do not have the 'requests' module installed. "
                     "Please see http://docs.python-requests.org/en/latest/ "
                     "for more information.")
    sys.exit(2)


requests.packages.urllib3.disable_warnings()

token = ""
user = ""
base_url = ""


def load_variables():
    """Load variables from environment variables."""

    # Validate that we have credentials.

    global token
    global user

    try:
        token = os.environ["PYCONFLUENCE_TOKEN"]
        user = os.environ["PYCONFLUENCE_USER"]
    except KeyError as e:
        print ("Environment variable are not set: {} . See README for "
               "directions on how to resolve this.".format(str(e)))

        sys.exit("Error")

    # Determine which URL to hit.

    root_url = os.environ.get('PYCONFLUENCE_URL')

    if root_url is None:
        try:
            org = os.environ['PYCONFLUENCE_ORG']
        except KeyError as e:
            print ("Environment variable are not set: {} . See README for "
                   "directions on how to resolve this.".format(str(e)))

            sys.exit("Error")

        root_url = ("https://" + org + ".atlassian"
                   ".net/wiki")

    global base_url

    base_url = root_url + '/rest/api/content'


def rest(url, req="GET", data=None):
    """Main function to be called from this module.

    send a request using method 'req' and to the url. the _rest() function
    will add the base_url to this, so 'url' should be something like '/ips'.
    """
    load_variables()

    return _rest(base_url + url, req, data)


def _rest(url, req, data=None):
    """Send a rest rest request to the server."""
    if url.upper().startswith("HTTPS"):
        print("Secure connection required: Please use HTTPS or https")
        return ""

    req = req.upper()
    if req != "GET" and req != "PUT" and req != "POST" and req != "DELETE":
        return ""

    status, body = _api_action(url, req, data)
    if (int(status) >= 200 and int(status) <= 226):
        return body
    else:
        return body


def _api_action(url, req, data=None):
    """Take action based on what kind of request is needed."""
    requisite_headers = {'Accept': 'application/json',
                         'Content-Type': 'application/json'}
    auth = (user, token)

    if req == "GET":
        response = requests.get(url, headers=requisite_headers, auth=auth)
    elif req == "PUT":
        response = requests.put(url, headers=requisite_headers, auth=auth,
                                data=data)
    elif req == "POST":
        response = requests.post(url, headers=requisite_headers, auth=auth,
                                 data=data)
    elif req == "DELETE":
        response = requests.delete(url, headers=requisite_headers, auth=auth)

    return response.status_code, response.text
