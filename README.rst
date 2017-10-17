======================================
PyConfluence REST API wrapper ("Pyco")
======================================

.. image:: https://img.shields.io/pypi/v/pyconfluence.svg
   :target: https://img.shields.io/pypi/v/pyconfluence

.. image:: https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.3%2C%203.4%2C%203.5-orange.svg
   :target: https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.3%2C%203.4%2C%203.5-orange

.. image:: https://travis-ci.org/FulcrumIT/pyconfluence.svg
   :target: https://travis-ci.org/FulcrumIT/pyconfluence
   :alt: Travis build status

.. _Twitter: https://twitter.com/MuddyTM

.. _blog: http://muddytm.github.io/

PyConfluence is an API wrapper for Atlassian's Confluence service that is used
extensively in automated documentation here at `Fulcrum Technologies <http://www.fulcrum.net/>`__.
It is designed with convenience in mind and allows for easy interaction with the
numerous services Confluence offers.

Setup
---------------

To get going with PyConfluence (or "Pyco", because "PyConfluence" has lots of
letters in it), you're first going to want to install "pyconfluence" with pip:

    pip install pyconfluence

Once that's done, you'll need to give it your credentials by setting them as
environment variables. Here's the step-by-step process:

1. Create a file named ".pyconfluence" in your home directory ("~/.pyconfluence").
2. In that file, input the following lines (with appropriate credentials):

    export PYCONFLUENCE_USER=[username for Confluence account]

    export PYCONFLUENCE_TOKEN=[password for Confluence account]

    export BASE_URL=[url of your Confluence website]

3. Save the file, then add this to ".bash_profile" in your home directory ("~/.bash_profile"):

    source ~/.pyconfluence

4. Once this is done, on startup these environment variables will be loaded.

5. There is no step 5, because you're done! Woo!

How to use
---------------

Import PyConfluence in your Python script by transcribing this tremendously
difficult and complex series of keywords:

    import pyconfluence

Whew! You did it. Now we can begin using Pyco (remember, that's PyConfluence).

Wait, wait; I lied. We can't yet, because there's some basic stuff about
Confluence that should be explained first as it pertains to Pyco.

What does [x] mean?
---------------

Here are some words/phrases you're going to need to be familiar with, and their
definitions:

- A **page ID** is a unique identifier (in form of a number) that is given to
  each and every page. There is no known way to control what page ID a page
  receives. To find this ID, go to the editing interface for that page and find
  it at the end of the URL. Alternatively, use the **get_page_id()** function in
  Pyco. Note: in actions.py, the variable "id" is the same as the page ID.

- A **space** is a group of pages in Confluence in essence; however for purposes
  in context of Pyco, this word is the same as the **space identifier**. To find
  this identifier, go to the space and look at the URL. You'll find it right
  after ".../wiki/display/". Unless that gets changed. Then feel free to send me
  hatemail!

- A **parent ID** is the same as a **page ID** and can be found the same way.
  The key difference is that a page can only be created when given a parent to
  sit under; the page whose ID is given as a parent ID will become the parent to
  the newly created page. Capiche? See the function **create_page()** for more
  details.

- A **page name** is...yeah, you guess it. The name for a page. In Highlander
  style, *there can only be one* in any given space. You can also decide exactly
  what page name you want, unlike page IDs.

- **Content** is the source **XHTML** for any given page. Let me repeat: that's
  **XHTML**...*not* HTML. There are subtle differences between the two that will
  often give you a headache when trying to create pages. Unfortunately there's
  no easy way to look at the XHTML of a page without using the API. Try
  **get_page_content()** and learn some stuff!

PyConfluence functions
---------------

Now that you know all of those terms and have memorized all their definitions
word-for-word, you can begin using Pyco without breaking a sweat. Although one
would wonder why you were sweating in the first place.

Below I will list the current functions for PyConfluence. I'll be updating this
list as long as the script itself is being updated. For more information, check
out **pyconfluence/actions.py**.

- **create_page(name, parent_id, space, content)**:
  Create a page in Confluence.

- **delete_page(id)**:
  Delete a page from Confluence.

- **delete_page_full(id)**:
  Delete a page from Confluence, along with its children.

- **get_page_full(id)**:
  Return JSON containing information about page.

- **get_page_full_more(name, space)**:
  Return content different than that from get_page_content, in JSON.

- **get_page_content(id)**:
  Return XHTML content of a page.

- **get_page_name(id)**:
  Return name of a page based on passed page id.

- **get_page_id(name, space)**:
  Return id of a page based on passed page name and space.

- **page_exists(name, space)**:
  Return True if named page currently exists in specified space.

- **get_page_children(id)**:
  Return list of a page's children as JSON.

You've reached the end!
---------------

So...time for some self-promotion!

Follow me on Twitter_, and/or check out my blog_!
