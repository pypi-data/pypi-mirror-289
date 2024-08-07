# -*- coding: utf-8; -*-

from tests.views.utils import WebTestCase

from wuttaweb.views import settings


class TestAppInfoView(WebTestCase):

    def test_index(self):
        # sanity/coverage check
        view = settings.AppInfoView(self.request)
        response = view.index()

    def test_configure_get_simple_settings(self):
        # sanity/coverage check
        view = settings.AppInfoView(self.request)
        simple = view.configure_get_simple_settings()

    def test_configure_get_context(self):
        # sanity/coverage check
        view = settings.AppInfoView(self.request)
        context = view.configure_get_context()
