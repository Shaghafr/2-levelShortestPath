from RiverPassing import House, Shop, Bridge, Port, Solution


class InputHandler:

    def __init__(self):
        self.houses, self.house_lego_ids = self.get_input(House)
        self.shops, self.shops_lego_ids = self.get_input(Shop)
        self.bridges, self.bridges_lego_ids = self.get_input(Bridge)
        self.ports, self.ports_lego_ids = self.get_input(Port)

    def get_input(self, object_class):
        obj_lego_ids = list()
        objs = list()
        obj_count = int(input(f"Enter {object_class.__name__} Count:\n "))
        i = 0
        while i < obj_count:
            obj_lego_id = int(input(f"Enter lego id for {object_class.__name__} #{i + 1} :\n "))
            if obj_lego_id in obj_lego_ids:
                print(f"You have already entered {obj_lego_id}")
                continue
            elif object_class.__name__ == 'Port' and obj_lego_id in self.bridges_lego_ids:
                    print(f"You have already created a bridge on logo #{obj_lego_id}")
                    continue
            else:
                objs.append(object_class(obj_lego_id))
                obj_lego_ids.append(obj_lego_id)
                i += 1
        print(f"{object_class.__name__.upper()}S:", objs)
        return objs, obj_lego_ids
