# -*- coding: utf-8; -*-
################################################################################
#
#  wuttaweb -- Web App for Wutta Framework
#  Copyright © 2024 Lance Edgar
#
#  This file is part of Wutta Framework.
#
#  Wutta Framework is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option) any
#  later version.
#
#  Wutta Framework is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  Wutta Framework.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Views for app settings
"""

from collections import OrderedDict

from wuttaweb.views import MasterView
from wuttaweb.util import get_libver, get_liburl


class AppInfoView(MasterView):
    """
    Master view for the core app info, to show/edit config etc.

    Notable URLs provided by this class:

    * ``/appinfo/``
    * ``/appinfo/configure``
    """
    model_name = 'AppInfo'
    model_title_plural = "App Info"
    route_prefix = 'appinfo'
    configurable = True

    def configure_get_simple_settings(self):
        """ """
        return [

            # basics
            {'name': f'{self.app.appname}.app_title'},
            {'name': f'{self.app.appname}.production',
             'type': bool},

            # web libs
            {'name': 'wuttaweb.libver.vue'},
            {'name': 'wuttaweb.liburl.vue'},
            {'name': 'wuttaweb.libver.vue_resource'},
            {'name': 'wuttaweb.liburl.vue_resource'},
            {'name': 'wuttaweb.libver.buefy'},
            {'name': 'wuttaweb.liburl.buefy'},
            {'name': 'wuttaweb.libver.buefy.css'},
            {'name': 'wuttaweb.liburl.buefy.css'},
            {'name': 'wuttaweb.libver.fontawesome'},
            {'name': 'wuttaweb.liburl.fontawesome'},
            {'name': 'wuttaweb.libver.bb_vue'},
            {'name': 'wuttaweb.liburl.bb_vue'},
            {'name': 'wuttaweb.libver.bb_oruga'},
            {'name': 'wuttaweb.liburl.bb_oruga'},
            {'name': 'wuttaweb.libver.bb_oruga_bulma'},
            {'name': 'wuttaweb.liburl.bb_oruga_bulma'},
            {'name': 'wuttaweb.libver.bb_oruga_bulma_css'},
            {'name': 'wuttaweb.liburl.bb_oruga_bulma_css'},
            {'name': 'wuttaweb.libver.bb_fontawesome_svg_core'},
            {'name': 'wuttaweb.liburl.bb_fontawesome_svg_core'},
            {'name': 'wuttaweb.libver.bb_free_solid_svg_icons'},
            {'name': 'wuttaweb.liburl.bb_free_solid_svg_icons'},
            {'name': 'wuttaweb.libver.bb_vue_fontawesome'},
            {'name': 'wuttaweb.liburl.bb_vue_fontawesome'},

        ]

    def configure_get_context(self, **kwargs):
        """ """

        # normal context
        context = super().configure_get_context(**kwargs)

        # we will add `weblibs` to context, based on config values
        weblibs = OrderedDict([
            ('vue', "Vue"),
            ('vue_resource', "vue-resource"),
            ('buefy', "Buefy"),
            ('buefy.css', "Buefy CSS"),
            ('fontawesome', "FontAwesome"),
            ('bb_vue', "(BB) vue"),
            ('bb_oruga', "(BB) @oruga-ui/oruga-next"),
            ('bb_oruga_bulma', "(BB) @oruga-ui/theme-bulma (JS)"),
            ('bb_oruga_bulma_css', "(BB) @oruga-ui/theme-bulma (CSS)"),
            ('bb_fontawesome_svg_core', "(BB) @fortawesome/fontawesome-svg-core"),
            ('bb_free_solid_svg_icons', "(BB) @fortawesome/free-solid-svg-icons"),
            ('bb_vue_fontawesome', "(BB) @fortawesome/vue-fontawesome"),
        ])

        # import ipdb; ipdb.set_trace()

        for key in weblibs:
            title = weblibs[key]
            weblibs[key] = {
                'key': key,
                'title': title,

                # nb. these values are exactly as configured, and are
                # used for editing the settings
                'configured_version': get_libver(self.request, key,
                                                 configured_only=True),
                'configured_url': get_liburl(self.request, key,
                                             configured_only=True),

                # nb. these are for display only
                'default_version': get_libver(self.request, key, default_only=True),
                'live_url': get_liburl(self.request, key),
            }

        context['weblibs'] = list(weblibs.values())
        return context


def defaults(config, **kwargs):
    base = globals()

    AppInfoView = kwargs.get('AppInfoView', base['AppInfoView'])
    AppInfoView.defaults(config)


def includeme(config):
    defaults(config)
