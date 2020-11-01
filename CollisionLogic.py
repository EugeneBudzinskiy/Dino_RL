from PhysxObj import PhysicalObject


class CollisionLogic:
    @staticmethod
    def check_collision(hero: PhysicalObject, prop: PhysicalObject):
        hero_coord_x = hero.coord[0]
        hero_coord_y = hero.coord[1]
        hero_size_w = hero.size[0]

        prop_coord_x = prop.coord[0]
        prop_coord_y = prop.coord[1]
        prop_size_w = prop.size[0]
        prop_size_h = prop.size[1]

        h_ld_p = (hero_coord_x, hero_coord_y)
        h_rd_p = (hero_coord_x + hero_size_w, hero_coord_y)

        p_lu_p = (prop_coord_x, prop_coord_y + prop_size_h)
        p_ru_p = (prop_coord_x + prop_size_w, prop_coord_y + prop_size_h)

        bool_p1 = p_lu_p[0] >= h_rd_p[0] and p_lu_p[1] >= h_rd_p[1]
        bool_p2 = p_ru_p[0] >= h_ld_p[0] and p_ru_p[1] >= h_ld_p[1]

        return bool_p1 or bool_p2
    pass




