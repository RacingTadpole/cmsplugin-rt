=====
cmsplugin-rt
=====

This package contains a number of basic plugins to kick start your Django-CMS project.
Some of them use classes appropriate for Twitter Bootstrap, but my intention is to broaden this.

button                     a Twitter Bootstrap button, with html special characters allowed
text_minimal_markup        plain text with an h2 heading, with links and email addresses activated and html special codes allowed, e.g. &copy;
resizeable_picture         a subclass of cms.plugin.picture which allows absolute or % width and height
self_calc_pagination       shows pagination links where pages after 1 are all the children of page 1 (tailored to Twitter Bootstrap)
hbar                       a simple html hbar element
spacer                     adds a .spacer div, which I style as clear:both, to switch off float:left and float:right

facebook_button            lots of options allowed
twitter_button             lots of options allowed
mailchimp_form             an inline mailchimp form (tailored to Twitter Bootstrap)

style_modifier             a plugin that lets the admin change the css directly (tailored to Twitter Bootstrap)

meta_icons                 include favicon and Apple touch icons in your header
open_graph                 include open-graph tags in your header

Detailed documentation is in the "docs" directory.

Requirements
--------------

I built these using:

* Django 1.4
* Django-CMS 2.3.5

Quick start
-----------

1. Add plugins from cmsplugin-rt to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'cmsplugin_rt.button',
          'cmsplugin_rt.facebook_button',
          'cmsplugin_rt.hbar',
          'cmsplugin_rt.mailchimp_form',
          'cmsplugin_rt.meta_icons',
          'cmsplugin_rt.open_graph',
          'cmsplugin_rt.resizeable_picture',
          'cmsplugin_rt.self_calc_pagination',
          'cmsplugin_rt.spacer',
          'cmsplugin_rt.style_modifier',
          'cmsplugin_rt.text_minimal_markup',
          'cmsplugin_rt.twitter_button',
      )

2. Run `python manage.py syncdb` (or use `python manage.py migrate` if you are using South) to create the models.

3. Add the plugins to your CMS pages in the admin panel.

