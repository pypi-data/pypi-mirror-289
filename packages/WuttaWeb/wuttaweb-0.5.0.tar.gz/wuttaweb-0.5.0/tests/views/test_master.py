# -*- coding: utf-8; -*-

import functools
from unittest import TestCase
from unittest.mock import MagicMock, patch

from pyramid import testing
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

from wuttjamaican.conf import WuttaConfig
from wuttaweb.views import master
from wuttaweb.subscribers import new_request_set_user

from tests.views.utils import WebTestCase


class TestMasterView(WebTestCase):

    def test_defaults(self):
        master.MasterView.model_name = 'Widget'
        # TODO: should inspect pyramid routes after this, to be certain
        master.MasterView.defaults(self.pyramid_config)
        del master.MasterView.model_name

    ##############################
    # class methods
    ##############################

    def test_get_model_class(self):
        
        # no model class by default
        self.assertIsNone(master.MasterView.get_model_class())

        # subclass may specify
        MyModel = MagicMock()
        master.MasterView.model_class = MyModel
        self.assertIs(master.MasterView.get_model_class(), MyModel)
        del master.MasterView.model_class

    def test_get_model_name(self):
        
        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_model_name)

        # subclass may specify model name
        master.MasterView.model_name = 'Widget'
        self.assertEqual(master.MasterView.get_model_name(), 'Widget')
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Blaster')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_model_name(), 'Blaster')
        del master.MasterView.model_class

    def test_get_model_name_normalized(self):
        
        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_model_name_normalized)

        # subclass may specify *normalized* model name
        master.MasterView.model_name_normalized = 'widget'
        self.assertEqual(master.MasterView.get_model_name_normalized(), 'widget')
        del master.MasterView.model_name_normalized

        # or it may specify *standard* model name
        master.MasterView.model_name = 'Blaster'
        self.assertEqual(master.MasterView.get_model_name_normalized(), 'blaster')
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Dinosaur')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_model_name_normalized(), 'dinosaur')
        del master.MasterView.model_class

    def test_get_model_title(self):
        
        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_model_title)

        # subclass may specify  model title
        master.MasterView.model_title = 'Wutta Widget'
        self.assertEqual(master.MasterView.get_model_title(), "Wutta Widget")
        del master.MasterView.model_title

        # or it may specify model name
        master.MasterView.model_name = 'Blaster'
        self.assertEqual(master.MasterView.get_model_title(), "Blaster")
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Dinosaur')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_model_title(), "Dinosaur")
        del master.MasterView.model_class

    def test_get_model_title_plural(self):
        
        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_model_title_plural)

        # subclass may specify *plural* model title
        master.MasterView.model_title_plural = 'People'
        self.assertEqual(master.MasterView.get_model_title_plural(), "People")
        del master.MasterView.model_title_plural

        # or it may specify *singular* model title
        master.MasterView.model_title = 'Wutta Widget'
        self.assertEqual(master.MasterView.get_model_title_plural(), "Wutta Widgets")
        del master.MasterView.model_title

        # or it may specify model name
        master.MasterView.model_name = 'Blaster'
        self.assertEqual(master.MasterView.get_model_title_plural(), "Blasters")
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Dinosaur')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_model_title_plural(), "Dinosaurs")
        del master.MasterView.model_class

    def test_get_route_prefix(self):
        
        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_route_prefix)

        # subclass may specify route prefix
        master.MasterView.route_prefix = 'widgets'
        self.assertEqual(master.MasterView.get_route_prefix(), 'widgets')
        del master.MasterView.route_prefix

        # subclass may specify *normalized* model name
        master.MasterView.model_name_normalized = 'blaster'
        self.assertEqual(master.MasterView.get_route_prefix(), 'blasters')
        del master.MasterView.model_name_normalized

        # or it may specify *standard* model name
        master.MasterView.model_name = 'Dinosaur'
        self.assertEqual(master.MasterView.get_route_prefix(), 'dinosaurs')
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Truck')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_route_prefix(), 'trucks')
        del master.MasterView.model_class

    def test_get_url_prefix(self):
        
        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_url_prefix)

        # subclass may specify url prefix
        master.MasterView.url_prefix = '/widgets'
        self.assertEqual(master.MasterView.get_url_prefix(), '/widgets')
        del master.MasterView.url_prefix

        # or it may specify route prefix
        master.MasterView.route_prefix = 'trucks'
        self.assertEqual(master.MasterView.get_url_prefix(), '/trucks')
        del master.MasterView.route_prefix

        # or it may specify *normalized* model name
        master.MasterView.model_name_normalized = 'blaster'
        self.assertEqual(master.MasterView.get_url_prefix(), '/blasters')
        del master.MasterView.model_name_normalized

        # or it may specify *standard* model name
        master.MasterView.model_name = 'Dinosaur'
        self.assertEqual(master.MasterView.get_url_prefix(), '/dinosaurs')
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Machine')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_url_prefix(), '/machines')
        del master.MasterView.model_class

    def test_get_template_prefix(self):
        
        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_template_prefix)

        # subclass may specify template prefix
        master.MasterView.template_prefix = '/widgets'
        self.assertEqual(master.MasterView.get_template_prefix(), '/widgets')
        del master.MasterView.template_prefix

        # or it may specify url prefix
        master.MasterView.url_prefix = '/trees'
        self.assertEqual(master.MasterView.get_template_prefix(), '/trees')
        del master.MasterView.url_prefix

        # or it may specify route prefix
        master.MasterView.route_prefix = 'trucks'
        self.assertEqual(master.MasterView.get_template_prefix(), '/trucks')
        del master.MasterView.route_prefix

        # or it may specify *normalized* model name
        master.MasterView.model_name_normalized = 'blaster'
        self.assertEqual(master.MasterView.get_template_prefix(), '/blasters')
        del master.MasterView.model_name_normalized

        # or it may specify *standard* model name
        master.MasterView.model_name = 'Dinosaur'
        self.assertEqual(master.MasterView.get_template_prefix(), '/dinosaurs')
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Machine')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_template_prefix(), '/machines')
        del master.MasterView.model_class

    def test_get_config_title(self):

        # error by default (since no model class)
        self.assertRaises(AttributeError, master.MasterView.get_config_title)

        # subclass may specify config title
        master.MasterView.config_title = 'Widgets'
        self.assertEqual(master.MasterView.get_config_title(), "Widgets")
        del master.MasterView.config_title

        # subclass may specify *plural* model title
        master.MasterView.model_title_plural = 'People'
        self.assertEqual(master.MasterView.get_config_title(), "People")
        del master.MasterView.model_title_plural

        # or it may specify *singular* model title
        master.MasterView.model_title = 'Wutta Widget'
        self.assertEqual(master.MasterView.get_config_title(), "Wutta Widgets")
        del master.MasterView.model_title

        # or it may specify model name
        master.MasterView.model_name = 'Blaster'
        self.assertEqual(master.MasterView.get_config_title(), "Blasters")
        del master.MasterView.model_name

        # or it may specify model class
        MyModel = MagicMock(__name__='Dinosaur')
        master.MasterView.model_class = MyModel
        self.assertEqual(master.MasterView.get_config_title(), "Dinosaurs")
        del master.MasterView.model_class

    ##############################
    # support methods
    ##############################

    def test_get_index_title(self):
        master.MasterView.model_title_plural = "Wutta Widgets"
        view = master.MasterView(self.request)
        self.assertEqual(view.get_index_title(), "Wutta Widgets")
        del master.MasterView.model_title_plural

    def test_render_to_response(self):

        def widgets(request): return {}
        self.pyramid_config.add_route('widgets', '/widgets/')
        self.pyramid_config.add_view(widgets, route_name='widgets')

        # basic sanity check using /master/index.mako
        # (nb. it skips /widgets/index.mako since that doesn't exist)
        master.MasterView.model_name = 'Widget'
        view = master.MasterView(self.request)
        response = view.render_to_response('index', {})
        self.assertIsInstance(response, Response)
        del master.MasterView.model_name

        # basic sanity check using /appinfo/index.mako
        master.MasterView.model_name = 'AppInfo'
        master.MasterView.route_prefix = 'appinfo'
        master.MasterView.url_prefix = '/appinfo'
        view = master.MasterView(self.request)
        response = view.render_to_response('index', {})
        self.assertIsInstance(response, Response)
        del master.MasterView.model_name
        del master.MasterView.route_prefix
        del master.MasterView.url_prefix

        # bad template name causes error
        master.MasterView.model_name = 'Widget'
        self.assertRaises(IOError, view.render_to_response, 'nonexistent', {})
        del master.MasterView.model_name

    ##############################
    # view methods
    ##############################

    def test_index(self):
        
        # basic sanity check using /appinfo
        master.MasterView.model_name = 'AppInfo'
        master.MasterView.route_prefix = 'appinfo'
        master.MasterView.template_prefix = '/appinfo'
        view = master.MasterView(self.request)
        response = view.index()
        del master.MasterView.model_name
        del master.MasterView.route_prefix
        del master.MasterView.template_prefix

    def test_configure(self):
        model = self.app.model

        # setup
        master.MasterView.model_name = 'AppInfo'
        master.MasterView.route_prefix = 'appinfo'
        master.MasterView.template_prefix = '/appinfo'

        # mock settings
        settings = [
            {'name': 'wutta.app_title'},
            {'name': 'wutta.foo', 'value': 'bar'},
            {'name': 'wutta.flag', 'type': bool},
            {'name': 'wutta.number', 'type': int, 'default': 42},
            {'name': 'wutta.value1', 'save_if_empty': True},
            {'name': 'wutta.value2', 'save_if_empty': False},
        ]

        view = master.MasterView(self.request)
        with patch.object(self.request, 'current_route_url',
                          return_value='/appinfo/configure'):
            with patch.object(master.MasterView, 'configure_get_simple_settings',
                              return_value=settings):
                with patch.object(master, 'Session', return_value=self.session):

                    # get the form page
                    response = view.configure()
                    self.assertIsInstance(response, Response)

                    # post request to save settings
                    self.request.method = 'POST'
                    self.request.POST = {
                        'wutta.app_title': 'Wutta',
                        'wutta.foo': 'bar',
                        'wutta.flag': 'true',
                    }
                    response = view.configure()
                    # nb. should get redirect back to configure page
                    self.assertIsInstance(response, HTTPFound)

                    # should now have 5 settings
                    count = self.session.query(model.Setting).count()
                    self.assertEqual(count, 5)
                    get_setting = functools.partial(self.app.get_setting, self.session)
                    self.assertEqual(get_setting('wutta.app_title'), 'Wutta')
                    self.assertEqual(get_setting('wutta.foo'), 'bar')
                    self.assertEqual(get_setting('wutta.flag'), 'true')
                    self.assertEqual(get_setting('wutta.number'), '42')
                    self.assertEqual(get_setting('wutta.value1'), '')
                    self.assertEqual(get_setting('wutta.value2'), None)

                    # post request to remove settings
                    self.request.method = 'POST'
                    self.request.POST = {'remove_settings': '1'}
                    response = view.configure()
                    # nb. should get redirect back to configure page
                    self.assertIsInstance(response, HTTPFound)

                    # should now have 0 settings
                    count = self.session.query(model.Setting).count()
                    self.assertEqual(count, 0)

        # teardown
        del master.MasterView.model_name
        del master.MasterView.route_prefix
        del master.MasterView.template_prefix
