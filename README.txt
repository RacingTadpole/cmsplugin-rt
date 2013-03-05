=====
cmsplugin-rt
=====

This package contains a number of basic plugins to kick start your Django-CMS project.
Some default to the Twitter Bootstrap look, but can be adjusted using the setting RT_FRONT_END_FRAMEWORK
Currently "BOOTSTRAP" and "JQUERY-MOBILE" are recognised.

button                     a Twitter Bootstrap or JQueryMobile button, with html special characters allowed
text_minimal_markup        plain text with an h2 heading, with links and email addresses activated and html special codes allowed, e.g. &copy;
resizeable_picture         a subclass of cms.plugin.picture which allows absolute or % width and height (sorry about the spelling mistake here!)
navbar                     a Twitter Bootstrap navbar, with self-calculating links to the home page's children, and quick links for admins
self_calc_pagination       shows pagination links where pages after 1 are all the children of page 1 (tailored to Twitter Bootstrap)
hbar                       a simple html <hr> element
spacer                     adds a .spacer div, which I style as clear:both, to switch off float:left and float:right

facebook_button            lots of options allowed
twitter_button             lots of options allowed
mailchimp_form             an inline mailchimp form (tailored to Twitter Bootstrap)
google_font                link to Google fonts (use them via the style modifier plugin)
google_analytics           include tracking code for Google analytics

style_modifier             a plugin that lets the admin change the css directly
                           (a number of Twitter Bootstrap and JQueryMobile classes are pre-configured)
                           add RT_MORE_STYLE_CLASSES to settings.py to add more options to the drop-down list

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
          'cmsplugin_rt.google_analytics',
          'cmsplugin_rt.google_font',
          'cmsplugin_rt.hbar',
          'cmsplugin_rt.mailchimp_form',
          'cmsplugin_rt.meta_icons',
          'cmsplugin_rt.navbar',
          'cmsplugin_rt.open_graph',
          'cmsplugin_rt.resizeable_picture',
          'cmsplugin_rt.self_calc_pagination',
          'cmsplugin_rt.spacer',
          'cmsplugin_rt.style_modifier',
          'cmsplugin_rt.text_minimal_markup',
          'cmsplugin_rt.twitter_button',
      )

2. If you are using JQueryMobile, add to settings.py:

      RT_FRONT_END_FRAMEWORK = "JQUERY-MOBILE"  # "BOOTSTRAP" is the default; only these two are known

   You can also set this to "" to remove Style Modifier's default Bootstrap class options.

3. To add custom classes to the Style Modifier, add to settings.py something like this:

      from django.utils.translation import ugettext_lazy as _
      RT_MORE_STYLE_CLASSES = ((".banner", _("banner")),
                     (".warning", _("warning text")),      # example classes only
                     )

4. The button template is configured for Twitter Bootstrap, although the admin panel shows choices appropriate for
   JQueryMobile as well.
   If you want to use buttons with JQueryMobile, override the template by adding to your own project the file:
      templates/button_plugin.html, containing:

      {% load allow_special %}
      <a data-role="button" {% ifequal instance.button_type "inline" %}data-inline="true"{% endifequal %}
            {% ifequal instance.button_size "btn-mini" %}data-mini="true"{% endifequal %} data-ajax="false" href="{{ link }}">
        {{ instance.button_text|allow_special }}
        {% if instance.arrows %} &raquo; {% endif %}
      </a>

5. Run `python manage.py syncdb` (or use `python manage.py migrate` if you are using South) to create the models.

6. Add the plugins to your CMS pages in the admin panel.

7. Some plugins use 'spacer', 'align-center', 'align-left', 'align-right' classes, which you should implement in your css, e.g.:
    .align-right {
	    float: right;
    }
    .align-left {
	    float: left;
    }
    .align-center {
	    margin-left:auto;
	    margin-right:auto;
	    text-align:center;
	    display: block;  /* text-align:center and display:block are critical to getting this to work */
    }
    .spacer {
	    clear: both;
    }

