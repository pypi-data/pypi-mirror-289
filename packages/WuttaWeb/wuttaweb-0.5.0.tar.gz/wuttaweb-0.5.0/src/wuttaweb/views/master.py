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
Base Logic for Master Views
"""

from pyramid.renderers import render_to_response

from wuttaweb.views import View
from wuttaweb.util import get_form_data
from wuttaweb.db import Session


class MasterView(View):
    """
    Base class for "master" views.

    Master views typically map to a table in a DB, though not always.
    They essentially are a set of CRUD views for a certain type of
    data record.

    Many attributes may be overridden in subclass.  For instance to
    define :attr:`model_class`::

       from wuttaweb.views import MasterView
       from wuttjamaican.db.model import Person

       class MyPersonView(MasterView):
           model_class = Person

       def includeme(config):
           MyPersonView.defaults(config)

    .. note::

       Many of these attributes will only exist if they have been
       explicitly defined in a subclass.  There are corresponding
       ``get_xxx()`` methods which should be used instead of accessing
       these attributes directly.

    .. attribute:: model_class

       Optional reference to a data model class.  While not strictly
       required, most views will set this to a SQLAlchemy mapped
       class,
       e.g. :class:`wuttjamaican:wuttjamaican.db.model.auth.User`.

       Code should not access this directly but instead call
       :meth:`get_model_class()`.

    .. attribute:: model_name

       Optional override for the view's data model name,
       e.g. ``'WuttaWidget'``.

       Code should not access this directly but instead call
       :meth:`get_model_name()`.

    .. attribute:: model_name_normalized

       Optional override for the view's "normalized" data model name,
       e.g. ``'wutta_widget'``.

       Code should not access this directly but instead call
       :meth:`get_model_name_normalized()`.

    .. attribute:: model_title

       Optional override for the view's "humanized" (singular) model
       title, e.g. ``"Wutta Widget"``.

       Code should not access this directly but instead call
       :meth:`get_model_title()`.

    .. attribute:: model_title_plural

       Optional override for the view's "humanized" (plural) model
       title, e.g. ``"Wutta Widgets"``.

       Code should not access this directly but instead call
       :meth:`get_model_title_plural()`.

    .. attribute:: config_title

       Optional override for the view's "config" title, e.g. ``"Wutta
       Widgets"`` (to be displayed as **Configure Wutta Widgets**).

       Code should not access this directly but instead call
       :meth:`get_config_title()`.

    .. attribute:: route_prefix

       Optional override for the view's route prefix,
       e.g. ``'wutta_widgets'``.

       Code should not access this directly but instead call
       :meth:`get_route_prefix()`.

    .. attribute:: url_prefix

       Optional override for the view's URL prefix,
       e.g. ``'/widgets'``.

       Code should not access this directly but instead call
       :meth:`get_url_prefix()`.

    .. attribute:: template_prefix

       Optional override for the view's template prefix,
       e.g. ``'/widgets'``.

       Code should not access this directly but instead call
       :meth:`get_template_prefix()`.

    .. attribute:: listable

       Boolean indicating whether the view model supports "listing" -
       i.e. it should have an :meth:`index()` view.  Default value is
       ``True``.

    .. attribute:: configurable

       Boolean indicating whether the master view supports
       "configuring" - i.e. it should have a :meth:`configure()` view.
       Default value is ``False``.
    """

    ##############################
    # attributes
    ##############################

    # features
    listable = True
    configurable = False

    # current action
    configuring = False

    ##############################
    # index methods
    ##############################

    def index(self):
        """
        View to "list" (filter/browse) the model data.

        This is the "default" view for the model and is what user sees
        when visiting the "root" path under the :attr:`url_prefix`,
        e.g. ``/widgets/``.

        By default, this view is included only if :attr:`listable` is
        true.
        """
        context = {
            'index_url': None,  # avoid title link since this *is* the index
        }
        return self.render_to_response('index', context)

    ##############################
    # configure methods
    ##############################

    def configure(self):
        """
        View for configuring aspects of the app which are pertinent to
        this master view and/or model.

        By default, this view is included only if :attr:`configurable`
        is true.  It usually maps to a URL like ``/widgets/configure``.

        The expected workflow is as follows:

        * user navigates to Configure page
        * user modifies settings and clicks Save
        * this view then *deletes* all "known" settings
        * then it saves user-submitted settings

        That is unless ``remove_settings`` is requested, in which case
        settings are deleted but then none are saved.  The "known"
        settings by default include only the "simple" settings.

        As a general rule, a particular setting should be configurable
        by (at most) one master view.  Some settings may never be
        exposed at all.  But when exposing a setting, careful thought
        should be given to where it logically/best belongs.

        Some settings are "simple" and a master view subclass need
        only provide their basic definitions via
        :meth:`configure_get_simple_settings()`.  If complex settings
        are needed, subclass must override one or more other methods
        to achieve the aim(s).

        See also related methods, used by this one:

        * :meth:`configure_get_simple_settings()`
        * :meth:`configure_get_context()`
        * :meth:`configure_gather_settings()`
        * :meth:`configure_remove_settings()`
        * :meth:`configure_save_settings()`
        """
        self.configuring = True
        config_title = self.get_config_title()

        # was form submitted?
        if self.request.method == 'POST':

            # maybe just remove settings
            if self.request.POST.get('remove_settings'):
                self.configure_remove_settings()
                self.request.session.flash(f"All settings for {config_title} have been removed.",
                                           'warning')

                # reload configure page
                return self.redirect(self.request.current_route_url())

            # gather/save settings
            data = get_form_data(self.request)
            settings = self.configure_gather_settings(data)
            self.configure_remove_settings()
            self.configure_save_settings(settings)
            self.request.session.flash("Settings have been saved.")

            # reload configure page
            return self.redirect(self.request.current_route_url())

        # render configure page
        context = self.configure_get_context()
        return self.render_to_response('configure', context)

    def configure_get_context(
            self,
            simple_settings=None,
    ):
        """
        Returns the full context dict, for rendering the
        :meth:`configure()` page template.

        Default context will include ``simple_settings`` (normalized
        to just name/value).

        You may need to override this method, to add additional
        "complex" settings etc.

        :param simple_settings: Optional list of simple settings, if
           already initialized.  Otherwise it is retrieved via
           :meth:`configure_get_simple_settings()`.

        :returns: Context dict for the page template.
        """
        context = {}

        # simple settings
        if simple_settings is None:
            simple_settings = self.configure_get_simple_settings()
        if simple_settings:

            # we got some, so "normalize" each definition to name/value
            normalized = {}
            for simple in simple_settings:

                # name
                name = simple['name']

                # value
                if 'value' in simple:
                    value = simple['value']
                elif simple.get('type') is bool:
                    value = self.config.get_bool(name, default=simple.get('default', False))
                else:
                    value = self.config.get(name)

                normalized[name] = value

            # add to template context
            context['simple_settings'] = normalized

        return context

    def configure_get_simple_settings(self):
        """
        This should return a list of "simple" setting definitions for
        the :meth:`configure()` view, which can be handled in a more
        automatic way.  (This is as opposed to some settings which are
        more complex and must be handled manually; those should not be
        part of this method's return value.)

        Basically a "simple" setting is one which can be represented
        by a single field/widget on the Configure page.

        The setting definitions returned must each be a dict of
        "attributes" for the setting.  For instance a *very* simple
        setting might be::

           {'name': 'wutta.app_title'}

        The ``name`` is required, everything else is optional.  Here
        is a more complete example::

           {
               'name': 'wutta.production',
               'type': bool,
               'default': False,
               'save_if_empty': False,
           }

        Note that if specified, the ``default`` should be of the same
        data type as defined for the setting (``bool`` in the above
        example).  The default ``type`` is ``str``.

        Normally if a setting's value is effectively null, the setting
        is removed instead of keeping it in the DB.  This behavior can
        be changed per-setting via the ``save_if_empty`` flag.

        :returns: List of setting definition dicts as described above.
           Note that their order does not matter since the template
           must explicitly define field layout etc.
        """

    def configure_gather_settings(
            self,
            data,
            simple_settings=None,
    ):
        """
        Collect the full set of "normalized" settings from user
        request, so that :meth:`configure()` can save them.

        Settings are gathered from the given request (e.g. POST)
        ``data``, but also taking into account what we know based on
        the simple setting definitions.

        Subclass may need to override this method if complex settings
        are required.

        :param data: Form data submitted via POST request.

        :param simple_settings: Optional list of simple settings, if
           already initialized.  Otherwise it is retrieved via
           :meth:`configure_get_simple_settings()`.

        This method must return a list of normalized settings, similar
        in spirit to the definition syntax used in
        :meth:`configure_get_simple_settings()`.  However the format
        returned here is minimal and contains just name/value::

           {
               'name': 'wutta.app_title',
               'value': 'Wutta Wutta',
           }

        Note that the ``value`` will always be a string.

        Also note, whereas it's possible ``data`` will not contain all
        known settings, the return value *should* (potentially)
        contain all of them.

        The one exception is when a simple setting has null value, by
        default it will not be included in the result (hence, not
        saved to DB) unless the setting definition has the
        ``save_if_empty`` flag set.
        """
        settings = []

        # simple settings
        if simple_settings is None:
            simple_settings = self.configure_get_simple_settings()
        if simple_settings:

            # we got some, so "normalize" each definition to name/value
            for simple in simple_settings:
                name = simple['name']

                if name in data:
                    value = data[name]
                else:
                    value = simple.get('default')

                if simple.get('type') is bool:
                    value = str(bool(value)).lower()
                elif simple.get('type') is int:
                    value = str(int(value or '0'))
                elif value is None:
                    value = ''
                else:
                    value = str(value)

                # only want to save this setting if we received a
                # value, or if empty values are okay to save
                if value or simple.get('save_if_empty'):
                    settings.append({'name': name,
                                     'value': value})

        return settings

    def configure_remove_settings(
            self,
            simple_settings=None,
    ):
        """
        Remove all "known" settings from the DB; this is called by
        :meth:`configure()`.

        The point of this method is to ensure *all* "known" settings
        which are managed by this master view, are purged from the DB.

        The default logic can handle this automatically for simple
        settings; subclass must override for any complex settings.

        :param simple_settings: Optional list of simple settings, if
           already initialized.  Otherwise it is retrieved via
           :meth:`configure_get_simple_settings()`.
        """
        names = []

        # simple settings
        if simple_settings is None:
            simple_settings = self.configure_get_simple_settings()
        if simple_settings:
            names.extend([simple['name']
                          for simple in simple_settings])

        if names:
            # nb. must avoid self.Session here in case that does not
            # point to our primary app DB
            session = Session()
            for name in names:
                self.app.delete_setting(session, name)

    def configure_save_settings(self, settings):
        """
        Save the given settings to the DB; this is called by
        :meth:`configure()`.

        This method expected a list of name/value dicts and will
        simply save each to the DB, with no "conversion" logic.

        :param settings: List of normalized setting definitions, as
           returned by :meth:`configure_gather_settings()`.
        """
        # app = self.get_rattail_app()

        # nb. must avoid self.Session here in case that does not point
        # to our primary app DB
        session = Session()
        for setting in settings:
            self.app.save_setting(session, setting['name'], setting['value'],
                                  force_create=True)

    ##############################
    # support methods
    ##############################

    def get_index_title(self):
        """
        Returns the main index title for the master view.

        By default this returns the value from
        :meth:`get_model_title_plural()`.  Subclass may override as
        needed.
        """
        return self.get_model_title_plural()

    def get_index_url(self, **kwargs):
        """
        Returns the URL for master's :meth:`index()` view.

        NB. this returns ``None`` if :attr:`listable` is false.
        """
        if self.listable:
            route_prefix = self.get_route_prefix()
            return self.request.route_url(route_prefix, **kwargs)

    def render_to_response(self, template, context):
        """
        Locate and render an appropriate template, with the given
        context, and return a :term:`response`.

        The specified ``template`` should be only the "base name" for
        the template - e.g.  ``'index'`` or ``'edit'``.  This method
        will then try to locate a suitable template file, based on
        values from :meth:`get_template_prefix()` and
        :meth:`get_fallback_templates()`.

        In practice this *usually* means two different template paths
        will be attempted, e.g. if ``template`` is ``'edit'`` and
        :attr:`template_prefix` is ``'/widgets'``:

        * ``/widgets/edit.mako``
        * ``/master/edit.mako``

        The first template found to exist will be used for rendering.
        It then calls
        :func:`pyramid:pyramid.renderers.render_to_response()` and
        returns the result.

        :param template: Base name for the template.

        :param context: Data dict to be used as template context.

        :returns: Response object containing the rendered template.
        """
        defaults = {
            'master': self,
            'route_prefix': self.get_route_prefix(),
            'index_title': self.get_index_title(),
            'index_url': self.get_index_url(),
            'config_title': self.get_config_title(),
        }

        # merge defaults + caller-provided context
        defaults.update(context)
        context = defaults

        # first try the template path most specific to this view
        template_prefix = self.get_template_prefix()
        mako_path = f'{template_prefix}/{template}.mako'
        try:
            return render_to_response(mako_path, context, request=self.request)
        except IOError:

            # failing that, try one or more fallback templates
            for fallback in self.get_fallback_templates(template):
                try:
                    return render_to_response(fallback, context, request=self.request)
                except IOError:
                    pass

            # if we made it all the way here, then we found no
            # templates at all, in which case re-attempt the first and
            # let that error raise on up
            return render_to_response(mako_path, context, request=self.request)

    def get_fallback_templates(self, template):
        """
        Returns a list of "fallback" template paths which may be
        attempted for rendering a view.  This is used within
        :meth:`render_to_response()` if the "first guess" template
        file was not found.

        :param template: Base name for a template (without prefix), e.g.
           ``'custom'``.

        :returns: List of full template paths to be tried, based on
           the specified template.  For instance if ``template`` is
           ``'custom'`` this will (by default) return::

              ['/master/custom.mako']
        """
        return [f'/master/{template}.mako']

    ##############################
    # class methods
    ##############################

    @classmethod
    def get_model_class(cls):
        """
        Returns the model class for the view (if defined).

        A model class will *usually* be a SQLAlchemy mapped class,
        e.g. :class:`wuttjamaican:wuttjamaican.db.model.base.Person`.

        There is no default value here, but a subclass may override by
        assigning :attr:`model_class`.

        Note that the model class is not *required* - however if you
        do not set the :attr:`model_class`, then you *must* set the
        :attr:`model_name`.
        """
        if hasattr(cls, 'model_class'):
            return cls.model_class

    @classmethod
    def get_model_name(cls):
        """
        Returns the model name for the view.

        A model name should generally be in the format of a Python
        class name, e.g. ``'WuttaWidget'``.  (Note this is
        *singular*, not plural.)

        The default logic will call :meth:`get_model_class()` and
        return that class name as-is.  A subclass may override by
        assigning :attr:`model_name`.
        """
        if hasattr(cls, 'model_name'):
            return cls.model_name

        return cls.get_model_class().__name__

    @classmethod
    def get_model_name_normalized(cls):
        """
        Returns the "normalized" model name for the view.

        A normalized model name should generally be in the format of a
        Python variable name, e.g. ``'wutta_widget'``.  (Note this is
        *singular*, not plural.)

        The default logic will call :meth:`get_model_name()` and
        simply lower-case the result.  A subclass may override by
        assigning :attr:`model_name_normalized`.
        """
        if hasattr(cls, 'model_name_normalized'):
            return cls.model_name_normalized

        return cls.get_model_name().lower()

    @classmethod
    def get_model_title(cls):
        """
        Returns the "humanized" (singular) model title for the view.

        The model title will be displayed to the user, so should have
        proper grammar and capitalization, e.g. ``"Wutta Widget"``.
        (Note this is *singular*, not plural.)

        The default logic will call :meth:`get_model_name()` and use
        the result as-is.  A subclass may override by assigning
        :attr:`model_title`.
        """
        if hasattr(cls, 'model_title'):
            return cls.model_title

        return cls.get_model_name()

    @classmethod
    def get_model_title_plural(cls):
        """
        Returns the "humanized" (plural) model title for the view.

        The model title will be displayed to the user, so should have
        proper grammar and capitalization, e.g. ``"Wutta Widgets"``.
        (Note this is *plural*, not singular.)

        The default logic will call :meth:`get_model_title()` and
        simply add a ``'s'`` to the end.  A subclass may override by
        assigning :attr:`model_title_plural`.
        """
        if hasattr(cls, 'model_title_plural'):
            return cls.model_title_plural

        model_title = cls.get_model_title()
        return f"{model_title}s"

    @classmethod
    def get_route_prefix(cls):
        """
        Returns the "route prefix" for the master view.  This prefix
        is used for all named routes defined by the view class.

        For instance if route prefix is ``'widgets'`` then a view
        might have these routes:

        * ``'widgets'``
        * ``'widgets.create'``
        * ``'widgets.edit'``
        * ``'widgets.delete'``

        The default logic will call
        :meth:`get_model_name_normalized()` and simply add an ``'s'``
        to the end, making it plural.  A subclass may override by
        assigning :attr:`route_prefix`.
        """
        if hasattr(cls, 'route_prefix'):
            return cls.route_prefix

        model_name = cls.get_model_name_normalized()
        return f'{model_name}s'

    @classmethod
    def get_url_prefix(cls):
        """
        Returns the "URL prefix" for the master view.  This prefix is
        used for all URLs defined by the view class.

        Using the same example as in :meth:`get_route_prefix()`, the
        URL prefix would be ``'/widgets'`` and the view would have
        defined routes for these URLs:

        * ``/widgets/``
        * ``/widgets/new``
        * ``/widgets/XXX/edit``
        * ``/widgets/XXX/delete``

        The default logic will call :meth:`get_route_prefix()` and
        simply add a ``'/'`` to the beginning.  A subclass may
        override by assigning :attr:`url_prefix`.
        """
        if hasattr(cls, 'url_prefix'):
            return cls.url_prefix

        route_prefix = cls.get_route_prefix()
        return f'/{route_prefix}'

    @classmethod
    def get_template_prefix(cls):
        """
        Returns the "template prefix" for the master view.  This
        prefix is used to guess which template path to render for a
        given view.

        Using the same example as in :meth:`get_url_prefix()`, the
        template prefix would also be ``'/widgets'`` and the templates
        assumed for those routes would be:

        * ``/widgets/index.mako``
        * ``/widgets/create.mako``
        * ``/widgets/edit.mako``
        * ``/widgets/delete.mako``

        The default logic will call :meth:`get_url_prefix()` and
        return that value as-is.  A subclass may override by assigning
        :attr:`template_prefix`.
        """
        if hasattr(cls, 'template_prefix'):
            return cls.template_prefix

        return cls.get_url_prefix()

    @classmethod
    def get_config_title(cls):
        """
        Returns the "config title" for the view/model.

        The config title is used for page title in the
        :meth:`configure()` view, as well as links to it.  It is
        usually plural, e.g. ``"Wutta Widgets"`` in which case that
        winds up being displayed in the web app as: **Configure Wutta
        Widgets**

        The default logic will call :meth:`get_model_title_plural()`
        and return that as-is.  A subclass may override by assigning
        :attr:`config_title`.
        """
        if hasattr(cls, 'config_title'):
            return cls.config_title

        return cls.get_model_title_plural()

    ##############################
    # configuration
    ##############################

    @classmethod
    def defaults(cls, config):
        """
        Provide default Pyramid configuration for a master view.

        This is generally called from within the module's
        ``includeme()`` function, e.g.::

           from wuttaweb.views import MasterView

           class WidgetView(MasterView):
               model_name = 'Widget'

           def includeme(config):
               WidgetView.defaults(config)

        :param config: Reference to the app's
           :class:`pyramid:pyramid.config.Configurator` instance.
        """
        cls._defaults(config)

    @classmethod
    def _defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        url_prefix = cls.get_url_prefix()

        # index
        if cls.listable:
            config.add_route(route_prefix, f'{url_prefix}/')
            config.add_view(cls, attr='index',
                            route_name=route_prefix)

        # configure
        if cls.configurable:
            config.add_route(f'{route_prefix}.configure',
                             f'{url_prefix}/configure')
            config.add_view(cls, attr='configure',
                            route_name=f'{route_prefix}.configure')
