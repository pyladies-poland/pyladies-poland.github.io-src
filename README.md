Pyladies.pl Website
===================

This repository contains the code powering http://pyladies.pl/ website.

Setting up development env
--------------------------

First, you'll have to install additional software. You will need:

* Pelican (https://github.com/getpelican/pelican)

Running application
--------------------

To generate static pages from files inside 'content' dictionary:

* pelican content

In development mode, you can add -r (--autoreload) option to track changes to content files:

* pelican -r content

To serve generated sites, run:

* python -m pelican.server
