from PhysxObj import PhysicalObject


class CollisionLogic:
    @staticmethod
    def check_collision(hero: PhysicalObject, prop: PhysicalObject):
        hero_coord = hero.coord
        hero_size = hero.size

        prop_coord = prop.coord
        prop_size = prop.size

        hero_left_down_x = hero_coord[0]
        hero_left_down_y = hero_coord[1]
        hero_right_up_x = hero_coord[0] + hero_size[0]
        hero_right_up_y = hero_coord[1] + hero_size[1]

        prop_left_down_x = prop_coord[0]
        prop_left_down_y = prop_coord[1]
        prop_right_up_x = prop_coord[0] + prop_size[0]
        prop_right_up_y = prop_coord[1] + prop_size[1]

        result_a = hero_right_up_x > prop_left_down_x and hero_left_down_x < prop_right_up_x
        result_b = hero_right_up_y > prop_left_down_y and hero_left_down_y < prop_right_up_y

        return result_a and result_b
