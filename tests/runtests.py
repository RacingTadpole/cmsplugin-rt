import os, sys
from django.conf import settings

DIRNAME = os.path.dirname(__file__)
settings.configure(DEBUG=True,
               DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                    }
                },
               #ROOT_URLCONF='myapp.urls',
               CMS_TEMPLATES = ( ('template_for_tests.html', 'Test template'), ),
               CMS_MODERATOR = False,
               CMS_PERMISSION = False,
               TEMPLATE_CONTEXT_PROCESSORS = (
                   'django.contrib.auth.context_processors.auth',
                   'django.core.context_processors.i18n',
                   'django.core.context_processors.request',
                   'django.core.context_processors.media',
                   'django.core.context_processors.static',
                   'cms.context_processors.media',
                   'sekizai.context_processors.sekizai',
               ),
               INSTALLED_APPS = (
                   #'cmsplugin-rt.cmsplugin_rt',
                   'cmsplugin_rt',
                   'cmsplugin_rt.button',
                   #'cmsplugin_rt.facebook_button',
                   #'cmsplugin_rt.hbar',
                   #'cmsplugin_rt.mailchimp_form',
                   #'cmsplugin_rt.meta_icons',
                   #'cmsplugin_rt.open_graph',
                   #'cmsplugin_rt.resizeable_picture',
                   #'cmsplugin_rt.self_calc_pagination',
                   #'cmsplugin_rt.spacer',
                   #'cmsplugin_rt.style_modifier',
                   #'cmsplugin_rt.text_minimal_markup',
                   #'cmsplugin_rt.twitter_button',
                   'django.contrib.auth',
                   'django.contrib.contenttypes',
                   'django.contrib.sessions',
                   'django.contrib.admin',
                   'django.contrib.sites',
                   'django.contrib.messages',
                   'django.contrib.staticfiles',
                   #'django.contrib.markup',
                   'south',
                   'cms',
                   'mptt',
                   'menus',
                   'sekizai',
                   'cms.plugins.file',
                   'cms.plugins.link',
                   'cms.plugins.picture',
                   'cms.plugins.text',
                   'cms.plugins.video',
               ),
               )


#from cms.test_utils.util.context_managers import SettingsOverride

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=2)
failures = test_runner.run_tests(['cmsplugin_rt', ])
if failures:
    sys.exit(failures)
