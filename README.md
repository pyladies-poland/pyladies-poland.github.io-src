Pyladies.pl Website
===================

This repository contains the code powering http://poland.pyladies.com/ website.

Setting up development env
--------------------------

First, you'll have to install an additional library. You will need:

* Pelican (https://github.com/getpelican/pelican)

###Running application

To generate static pages from files inside `content` directory:

`pelican content`

In development mode, you can add -r (--autoreload) option to track changes to content files:

`pelican -r content`

To serve generated sites, run:

`python -m pelican.server`


Contributing to poland.pyladies.com
-----------------------------------
* Install required libraries (see **Setting up development env**)
* Clone this repository
* Enter the folder you cloned into and run the following commands:

  `git submodule init`

  `git submodule update`

  This action fetches a module connected to this repository.
  The module points to a separate repository containing HTML files shown
  on PyLadies webiste: `https://github.com/pyladies-poland/pyladies-poland.github.io`
* Add, commit and push changes to this repository

*The following commands can be executed by running the `deploy.sh` script*

* Generate static content (HTML files) by executing:

  `make html`

* Commit changes to the HTML files in the other repository:

```
 cd output
 git add .
 git commit -m "Update the contents"
 git push origin master
```

* Commit changes to the module in the current repository:

```
 cd ..
 git add output
 git commit -m "Update output version"
 git push origin master
```

That's all, refresh `poland.pyladies.com`, your changes should be there!
