class Tree:
    class Node:
        def __init__(self, parent, value):
            self.parent = parent
            self.value = value

        def __repr__(self):
            try:
                return "parent: " + str(self.parent.value) + " - value: " + str(self.value)
            except AttributeError:
                return "parent: None -" + " value: " + str(self.value)

    def __init__(self):
        self.people = []

    def add_person(self, person):
        person_nodes = []
        if len(self.people) == 0:
            for person_loved_beer in person:
                person_nodes.append(self.Node(None, person_loved_beer))
        else:
            parent_beer_nodes = self.people[-1]
            parent_beers = []
            for beer_node in parent_beer_nodes:
                parent_beers.append(beer_node.value)
            for person_loved_beer in person:
                for parent_loved_node in parent_beer_nodes:
                    if person_loved_beer in parent_beers and parent_loved_node.value != person_loved_beer:
                        continue
                    person_nodes.append(self.Node(parent_loved_node, person_loved_beer))
        if person_nodes != []:
            self.people.append(person_nodes)

    def find_shortest_way(self):
        shortest_way_len = 0
        if len(self.people) == 0:
            return 0
        for beer in self.people[-1]:
            way = []
            while not beer is None:
                way.append(beer.value)
                beer = beer.parent
            way = list(dict.fromkeys(way))
            if len(way) < shortest_way_len or shortest_way_len == 0:
                shortest_way_len = len(way)

        return shortest_way_len