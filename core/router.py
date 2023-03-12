from logs.log_prog import logger_info, logger_error
from core.tools import banner
from core.state import StateManager

class CallBack:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func()


class Route:

    def __init__(self, name, description=None, callback=None, children=None):
        self.parent = None
        self.children = None
        self.name = name
        self.description = description
        self.callback = callback
        children and self._set_parent(children)

    def _set_parent(self, children):
        for child in children:
            child.parent = self
        self.children = children

    def _get_route(self):
        try:
            banner(StateManager.get_current_route_name())
            print(self.description or '', end='\n')

            if self.children:
                for child in self.children:
                    print(f"\t{self.children.index(child) + 1}. {child.name}")
                print(f'\n\t0. ' + ('Exit' if not self.parent else f'Back -> {self.parent.name}'))
                logger_info('Show the menu for user')

                index = int(input('\n> ')) - 1
                route = self.children[index] if index != -1 else self.parent

                if not route:
                    banner('Exit')

                    if input('Do you want to exit ? (y|n) ').strip().lower()[0] == 'y':
                        print('The user hit exit')
                        logger_info('The user hit exit')
                        exit()
                    else:
                        self()
                return route
            else:
                return self()
        except (IndexError, ValueError, KeyboardInterrupt):
            banner('Error')
            input('Please enter a valid item\nPress Enter to continue ... ')
            logger_error('User enter a invalid item')
            self()

    def __call__(self, *args, **kwargs):
        StateManager.add_route_name(self.name)

        route = self._get_route()

        if self.parent == route:
            StateManager.delete_last_route_name()
            route()
        elif route.children:
            route()
        else:
            try:
                banner(route.name)
                route.callback and route.callback()
            except Exception as e:
                banner('Error')
            input('\nPress Enter to continue ... ')
            logger_error('invalid input')
            StateManager.delete_last_route_name()
            route.parent()


class Router:

    def __init__(self, route: Route):
        self.route = route
        StateManager.add_route_name(route.name)

    def __call__(self, *args, **kwargs):
        self.route()