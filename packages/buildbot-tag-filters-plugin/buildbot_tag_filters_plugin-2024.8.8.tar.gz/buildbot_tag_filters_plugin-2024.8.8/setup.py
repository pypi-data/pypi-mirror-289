#!/usr/bin/env python

try:
    from buildbot_pkg import setup_www_plugin
except ImportError:
    import sys
    print('Please install buildbot_pkg module in order to install that '
          'package, or use the pre-build .whl modules available on pypi',
          file=sys.stderr)
    sys.exit(1)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup_www_plugin(
    name='buildbot-tag-filters-plugin',
    description='Add builders filters menu section',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=u'Denis Malyutin',
    author_email=u'denis.malyutin@fruct.org',
    url='https://github.com/pp1e',
    packages=['buildbot_tag_filters_plugin'],
    package_data={
        '': [
            'VERSION',
            'static/*',
            'static/assets/*'
        ]
    },
    entry_points="""
        [buildbot.www]
        tag_filters_plugin = buildbot_tag_filters_plugin:ep
    """,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
    ],
)
