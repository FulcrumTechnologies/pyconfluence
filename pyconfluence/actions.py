import pyconfluence.api as _api
import json as _json


def get_page_full(id):
    """Return JSON containing information about page.
    Parameters:
    - id: id of a Confluence Page.
    Example output:
    {
        "_expandable": {
            "ancestors": "",
            "children": "/rest/api/content/12456789/child",
            "container": "/rest/api/space/TestChambers",
            "descendants": "/rest/api/content/12456789/descendant",
            "history": "/rest/api/content/12456789/history",
            "metadata": "",
            "operations": "",
            "space": "/rest/api/space/TestChambers",
            "version": ""
        },
        "_links": {
            "base": "https://aperturescience.atlassian.net/wiki",
            "collection": "/rest/api/content",
            "context": "/wiki",
            "self": "https://aperturescience.atlassian.net/wiki/rest/api/content/12456789",
            "tinyui": "/x/glAdos",
            "webui": "/display/TestChambers/Thinking+in+Portals"
        },
        "body": {
            "_expandable": {
                "anonymous_export_view": "",
                "editor": "",
                "export_view": "",
                "styled_view": "",
                "view": ""
            },
            "storage": {
                "_expandable": {
                    "content": "/rest/api/content/12456789"
                },
                "representation": "storage",
                "value": "<p>Please assume the emergency party escort submission position.</p>"
            }
        },
        "extensions": {
            "position": "none"
        },
        "id": "12456789",
        "status": "current",
        "title": "Thinking in Portals",
        "type": "page"
    }
    """
    return _api.rest("/" + str(id) + "?expand=body.storage")


def get_page_full_more(name, space):
    """Return content different than that from get_page_content, in JSON.
    Parameters:
    - name: name of a Confluence page.
    - space: space the Confluence page is in.
    Example output:
    {
        "_links": {
            "base": "https://blackmesa.atlassian.net/wiki",
            "context": "/wiki",
            "self": "https://blackmesa.atlassian.net/wiki/rest/api/content?spaceKey=TheoreticalPhysics&expand=history&title=How%20to%20Tame%20Antlions"
        },
        "limit": 25,
        "results": [
            {
                "_expandable": {
                    "ancestors": "",
                    "body": "",
                    "children": "/rest/api/content/98765421/child",
                    "container": "/rest/api/space/TheoreticalPhysics",
                    "descendants": "/rest/api/content/98765421/descendant",
                    "metadata": "",
                    "operations": "",
                    "space": "/rest/api/space/TheoreticalPhysics",
                    "version": ""
                },
                "_links": {
                    "self": "https://blackmesa.atlassian.net/wiki/rest/api/content/98765421",
                    "tinyui": "/x/dGman",
                    "webui": "/display/TheoreticalPhysics/How+to+Tame+Antlions"
                },
                "extensions": {
                    "position": "none"
                },
                "history": {
                    "_expandable": {
                        "lastUpdated": "",
                        "nextVersion": "",
                        "previousVersion": ""
                    },
                    "_links": {
                        "self": "https://blackmesa.atlassian.net/wiki/rest/api/content/98765421/history"
                    },
                    "createdBy": {
                        "_links": {
                            "self": "https://blackmesa.atlassian.net/wiki/rest/experimental/user?key=169636a0108150507f0ecc0002ff8088"
                        },
                        "displayName": "Gordon Freeman",
                        "profilePicture": {
                            "height": 48,
                            "isDefault": false,
                            "path": "/wiki/download/attachments/52625418/user-avatar",
                            "width": 48
                        },
                        "type": "known",
                        "userKey": "169636a0108150507f0ecc0002ff8088",
                        "username": "the1freeman"
                    },
                    "createdDate": "2015-12-17T14:20:46.280-08:00",
                    "latest": true
                },
                "id": "98765421",
                "status": "current",
                "title": "How to Tame Antlions",
                "type": "page"
            }
        ],
        "size": 1,
        "start": 0
    }
    """
    return _api.rest("?title=" + name.replace(" ", "%20") + "&spaceKey="
                     "" + space + "&expand=history")


def get_page_content(id):
    """Return XHTML content of a page.
    Parameters:
    - id: id of a Confluence page.
    """
    data = _json.loads(_api.rest("/" + str(id) + "?expand=body.storage"))
    return data["body"]["storage"]["value"]


def get_page_name(id):
    """Return name of a page based on passed page id.
    Parameters:
    - id: id of a Confluence page.
    """
    data = _json.loads(_api.rest("/" + str(id) + "?expand=body.storage"))
    return data["title"]


def get_page_id(name, space):
    """Return id of a page based on passed page name and space.
    Parameters:
    - name: name of a Confluence page.
    - space: space the Confluence page is in.
    """
    data = _json.loads(_api.rest("?title=" + name.replace(" ", "%20") + "&"
                       "spaceKey=" + space + "&expand=history"))
    try:
        return data["results"][0]["id"]
    except:
        return ("Page not found!")


def page_exists(name, space):
    """Return True if named page currently exists in specified space.
    Parameters:
    - name: name of a Confluence page.
    - space: space the Confluence page is in.
    """
    data = _json.loads(_api.rest("?title=" + name.replace(" ", "%20") + "&"
                       "spaceKey=" + space + "&expand=history"))
    return (data["size"] > 0)


def get_page_children(id):
    """Return list of a page's children as JSON.
    Parameters:
    - id: id of a Confluence page whose children you want information about.
    Example output:
    {
        "_links": {
            "base": "https://kingdomofhyrule.atlassian.net/wiki",
            "context": "/wiki",
            "self": "https://kingdomofhyrule.atlassian.net/wiki/rest/api/content/40842631/child/page"
        },
        "limit": 1000,
        "results": [
            {
                "_expandable": {
                    "ancestors": "",
                    "body": "",
                    "children": "/rest/api/content/40842631/child",
                    "container": "/rest/api/space/GanonsStuff",
                    "descendants": "/rest/api/content/40842631/descendant",
                    "history": "/rest/api/content/40842631/history",
                    "metadata": "",
                    "operations": "",
                    "space": "/rest/api/space/GanonsStuff",
                    "version": ""
                },
                "_links": {
                    "self": "https://fulcrumtech.atlassian.net/wiki/rest/api/content/40842631",
                    "tinyui": "/x/DaLZe",
                    "webui": "/display/GanonsStuff/My+favorite+evil+schemes"
                },
                "extensions": {
                    "position": "none"
                },
                "id": "40842631",
                "status": "current",
                "title": "My favorite evil schemes",
                "type": "page"
            },
            {...(to be continued!)
            ...
            ...
            ...
            }
        ],
        "size": 71,
        "start": 0
    }
    """
    data = _api.rest("/" + str(id) + "/child/page?limit=1000")
    return data


def create_page(name, parent_id, space, content, representation='storage'):
    """Create a page in Confluence.
    Parameters:
    - name: name of the Confluence page to create.
    - parent_id: ID of the intended parent of the page.
    - space: key of the space where the page will be created.
    - content: Content to be written to the page.
    - representation: Confluence markup type
    Notes: the page id can be obtained by getting ["id"] from the returned JSON.
    """
    data = {}
    data["type"] = "page"
    data["title"] = name
    data["ancestors"] = [{"id": str(parent_id)}]
    data["space"] = {"key": space}
    data["body"] = {"storage": {"value": content,
                                "representation": representation}}
    return _api.rest("/", "POST", _json.dumps(data))


def edit_page(id, name, space, content, representation='storage'):
    """Update a page in Confluence.
    Parameters:
    - id: ID of the page you wish to edit.
    - name: name you would like to give to the page (usually the same name).
    - space: space where the page lives.
    - content: Content to be written to the page.
    - representation: Confluence markup type
    Notes: it is required to try an initial update to find the page version.
    """
    data = {}
    data["id"] = str(id)
    data["type"] = "page"
    data["title"] = name
    data["space"] = {"key": space}
    data["body"] = {"storage": {"value": content,
                                "representation": representation}}
    data["version"] = {"number": 1}

    response = _api.rest("/" + str(id), "PUT", _json.dumps(data))
    new_version = int(_json.loads(response)["message"].split()[-1]) + 1
    data["version"]["number"] = new_version

    return _api.rest("/" + str(id), "PUT", _json.dumps(data))


def delete_page(id):
    """Delete a page from Confluence.
    Parameters:
    - id: id of a Confluence page.
    Notes:
    - Getting a 204 error is expected! It means the page can no longer be found.
    """
    return _api.rest("/" + str(id), "DELETE")


def delete_page_full(id):
    """Delete a page from Confluence, along with its children.
    Parameters:
    - id: id of a Confluence page.
    Notes:
    - Getting a 204 error is expected! It means the page can no longer be found.
    """

    children = _json.loads(get_page_children(id))

    for i in children["results"]:
        delete_page_full(i["id"])

    return delete_page(id)
