class Building:
    def __init__(self, lego_id):
        self.lego_id = lego_id
        self.nearest_ports = list()
        self.nearest_bridges = list()
        self.south_port = None
        self.north_port = None
        self.south_bridge = None
        self.north_bridge = None
        self.port_on_same_lego = None
        self.bridge_on_same_lego = None

    def find_nearest_ports(self, ports):
        self.south_port = next((port for port in ports if port.lego_id < self.lego_id), None)
        self.north_port = next((port for port in ports if port.lego_id > self.lego_id), None)
        self.port_on_same_lego = next((port for port in ports if port.lego_id == self.lego_id), None)

    def find_nearest_bridges(self, bridges):
        self.south_bridge = next((bridge for bridge in bridges if bridge.lego_id < self.lego_id), None)
        self.north_bridge = next((bridge for bridge in bridges if bridge.lego_id > self.lego_id), None)
        self.bridge_on_same_lego = next((bridge for bridge in bridges if bridge.lego_id == self.lego_id), None)

    def __repr__(self):
        return self.__str__()


class House(Building):
    def __init__(self, lego_id):
        super().__init__(lego_id)

    def __str__(self):
        return f"House@{self.lego_id}"


class Shop(Building):
    def __init__(self, lego_id):
        super().__init__(lego_id)

    def __str__(self):
        return f"Shop@{self.lego_id}"


class RoadConnector:
    def __init__(self, lego_id):
        self.lego_id = lego_id

    def __repr__(self):
        return self.__str__()


class Bridge(RoadConnector):
    def __init__(self, lego_id):
        super().__init__(lego_id)

    def distance_to(self, obj):
        return abs(self.lego_id - obj.lego_id)

    def __str__(self):
        return f"Bridge@{self.lego_id}"


class Port(RoadConnector):
    def __init__(self, lego_id):
        super().__init__(lego_id)

    def distance_to(self, obj):
        return 2 * abs(self.lego_id - obj.lego_id)

    def __str__(self):
        return f"Port@{self.lego_id}"


class Distance:

    def __init__(self, house, shop, best_distance):
        self.house = house
        self.shop = shop
        self.best_distance = best_distance

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Distance from {self.house} to {self.shop} is {self.best_distance}"


class Solution:
    def __init__(self, houses, shops, ports, bridges):
        self.houses = houses
        self.shops = shops
        self.ports = ports
        self.bridges = bridges
        self.source_to_river_distance_dict = dict()
        self.river_to_destination_distance_dict = dict()
        self.calculated_distances = list()

    def source_to_destination_distance(self, house, shop):
        potential_distances = list()
        for connector in [house.south_port, house.north_port, house.port_on_same_lego,
                          house.south_bridge, house.north_bridge, house.bridge_on_same_lego]:
            if connector:
                choice = self.source_to_river_distance_dict[house][connector] + connector.distance_to(shop)
                potential_distances.append(choice)
        return min(potential_distances) + 2

    def calculated_distances_between_source_and_river(self, house, connector):
        sub_destination = connector.distance_to(house)
        if house in self.source_to_river_distance_dict:
            self.source_to_river_distance_dict[house][connector] = sub_destination
        else:
            self.source_to_river_distance_dict.update({
                house: {
                    connector: sub_destination
                }
            })

    def source_to_river(self, house):
        if house.north_port:
            self.calculated_distances_between_source_and_river(house=house, connector=house.north_port)
        if house.south_port:
            self.calculated_distances_between_source_and_river(house=house, connector=house.south_port)
        if house.port_on_same_lego:
            self.calculated_distances_between_source_and_river(house=house, connector=house.port_on_same_lego)
        if house.north_bridge:
            self.calculated_distances_between_source_and_river(house=house, connector=house.north_bridge)
        if house.south_bridge:
            self.calculated_distances_between_source_and_river(house=house, connector=house.south_bridge)
        if house.bridge_on_same_lego:
            self.calculated_distances_between_source_and_river(house=house, connector=house.bridge_on_same_lego)

    def river_to_destination(self):
        for shop in self.shops:
            for port in self.ports:
                if port in self.river_to_destination_distance_dict:
                    self.river_to_destination_distance_dict[port][shop] = 2 * abs(port.lego_id - shop.lego_id)
                else:
                    self.river_to_destination_distance_dict.update({
                        port: {
                            shop: 2 * abs(port.lego_id - shop.lego_id)
                        }
                    })
            for bridge in self.bridges:
                if bridge in self.river_to_destination_distance_dict:
                    self.river_to_destination_distance_dict[bridge][shop] = abs(bridge.lego_id - shop.lego_id)
                else:
                    self.river_to_destination_distance_dict.update({
                        bridge: {
                            shop: abs(bridge.lego_id - shop.lego_id)
                        }
                    })

    def solve(self):
        is_fliped = False
        if len(self.houses) < len(self.shops):
            self.shops, self.houses = self.houses, self.shops
        for house in self.houses:
            house.find_nearest_ports(self.ports)
            house.find_nearest_bridges(self.bridges)
        self.river_to_destination()
        for house in self.houses:
            self.source_to_river(house)
            for shop in self.shops:
                dest = self.source_to_destination_distance(house, shop)
                if is_fliped:
                    self.calculated_distances.append(Distance(shop, house, dest))
                else:
                    self.calculated_distances.append(Distance(house, shop, dest))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '\n'.join([str(d) for d in self.calculated_distances])

