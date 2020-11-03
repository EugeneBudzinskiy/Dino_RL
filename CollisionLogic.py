from PhysxObj import PhysicalObject


class CollisionLogic:
    @staticmethod
    def check_collision(hero: PhysicalObject, prop: PhysicalObject):
        hero_coord = hero.coord
        hero_size = hero.size

        prop_coord = prop.coord
        prop_size = prop.size

        hero_left_down_p = hero_coord
        hero_right_up_p = (hero_coord[0] + hero_size[0], hero_coord[1] + hero_size[1])

        prop_left_down_p = prop_coord
        prop_right_up_p = (prop_coord[0] + prop_size[0], prop_coord[1] + prop_size[1])

        bool_1 = hero_right_up_p[0] >= prop_left_down_p[0] and hero_left_down_p[1] <= prop_right_up_p[1]
        bool_2 = hero_left_down_p[0] <= prop_right_up_p[0] and hero_right_up_p[1] >= prop_left_down_p[1]

        return bool_1 and bool_2
