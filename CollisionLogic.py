from PhysxObj import PhysicalObject


class CollisionLogic:
    @staticmethod
    def check_collision(hero: PhysicalObject, prop: PhysicalObject):
        hero_coord = hero.coord
        hero_size = hero.size

        prop_coord = prop.coord
        prop_size = prop.size

        h_ld_p = hero_coord
        h_rd_p = hero_coord + (hero_size[0], 0)

        p_lu_p = prop_coord + (0, prop_size[1])
        p_ru_p = prop_coord + prop_size

        bool_p1 = p_lu_p[0] >= h_rd_p[0] and p_lu_p[1] >= h_rd_p[1]
        bool_p2 = p_ru_p[0] >= h_ld_p[0] and p_ru_p[1] >= h_ld_p[1]

        return bool_p1 or bool_p2




