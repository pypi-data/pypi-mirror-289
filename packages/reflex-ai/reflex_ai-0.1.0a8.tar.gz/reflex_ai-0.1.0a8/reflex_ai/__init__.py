"""The local Reflex agent."""

import types
import reflex as rx


def enable(app: rx.App):
    """Enable the agent on an app.

    Args:
        app: The app to enable the agent on.

    Note:
        For now, this must be called before add_page is called as
        we override the add_page method.
    """

    from .selection import clickable
    from .toolbar import playground

    def add_page(self, component, *args, **kwargs):
        route = kwargs.pop("route", rx.utils.format.format_route(component.__name__))
        rx.App.add_page(self, component, *args, route=route, **kwargs)
        rx.App.add_page(
            self,
            clickable()(lambda: playground(component)),
            route=f"/{route}/edit",
        )

    app.add_page = types.MethodType(add_page, app)
