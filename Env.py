from Interfaces import IProp


class Environment:

    def __init__(self):
        self.__prop_list = list()

    def spawn_prop(self, prop: IProp, x):
        if isinstance(prop, IProp):
            prop.spawn(x)
            self.__prop_list.append(prop)

    @property
    def prop_list(self):
        return self.__prop_list

    def remove_prop(self):
        for prop in self.__prop_list:
            if prop.coord[0] <= 0:
                self.__prop_list.remove(prop)

    def update(self):
        for prop in self.__prop_list:
            prop.update()
        self.remove_prop()
