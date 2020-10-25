from prop import Prop


class Environment:

    def __init__(self):
        self.__prop_list = list()

    def spawn_prop(self, prop: Prop, x, y):
        if isinstance(prop, Prop):
            prop.spawn(x, y)
            self.__prop_list.append(prop)

    @property
    def prop_list(self):
        return self.__prop_list

    def update(self):
        for prop in self.__prop_list:
            prop.update()
