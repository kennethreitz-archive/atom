Atom
====

This repo contains the code that is responsible for `atom.kennethreitz.com <http;//atom.kennethreitz.com>`_, powered by Elephant, Blackbox, Flask, and Heroku.

All content from the following sites conanically exists here:

- kennethreitz.com
- photo.kennethreitz.com
- music.kennethreitz.com

These sites consume the content from this service

All posts automatically replicate themselves to Blackbox.

Workflow
--------

- A peice of content (e.g. essay, article) is written in Markdown.
- The content is added to Atom via the API or the admin interface.
- The content is automatically replicted on Blackbox, preserving it for history.
- The content is associated with a Collection, which causes it to be "published" on a consuming service.
- Profit!

Basic Architecture
------------------

Content -> Category -> Collection

URL Strucuture
~~~~~~~~~~~~~~

/content/:uuid (atom.kennethreitz.org/8973594872357)
/:collection.atom (atom.kennethreitz.org/photo.atom)
/:collection/:category.atom (atom.kennethreitz.org/kr/expressions.atom)

Admin goals
-----------

- Simple drafting
- Simple publishing

Unclear
-------

The following items are currently unclear and need to be fully thought out:

- Editing on the frontend. Perhaps admin.kennethreitz.org? I think I'd like it to just be built in.