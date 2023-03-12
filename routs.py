from core.router import Router, Route
from admin.callback import register, login, log_out
from link_shortner.callback import show_by_link, show, shortner, private, remove


router = Router(
    Route('Main', description='Dynamic Menu, CLI', children=[
        Route('Register', callback=register),
        Route('User login', callback=login),
        Route('User log_out', callback=log_out),
        Route('User tools', children=[
            Route('Show links', children=[
                Route('Show All', callback=show),
                Route('Show by link', callback=show_by_link)
            ]),
            Route('Remove links', callback=remove),
            Route('Link shortener', children=[
                Route('Private shortner links', callback=private),
                Route('Local shortner links', callback=shortner),
            ])
        ])
])
)