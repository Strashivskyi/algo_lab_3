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
            parent_beers = self.people[-1]
            for person_loved_beer in person:
                does_parent_loves = False
                for parent_loved_node in parent_beers:
                    if parent_loved_node.value == person_loved_beer:
                        does_parent_loves = True
                for parent_loved_node in parent_beers:
                    if parent_loved_node.value == person_loved_beer:
                        person_nodes.append(self.Node(parent_loved_node, person_loved_beer))
                    elif not does_parent_loves:
                        person_nodes.append(self.Node(parent_loved_node, person_loved_beer))
        if person_nodes != []:
            self.people.append(person_nodes)

    def find_shortest_way(self):
        shortest_way_len = 0
        shortest_way = list()

        if len(self.people) == 0:
            return 0
        print("==============================================================================")
        print("every possible way:")
        for beer in self.people[-1]:
            way = []
            while not beer is None:
                way.append(beer.value)
                beer = beer.parent
            print(way)
            way = list(dict.fromkeys(way))

            if (len(way) < shortest_way_len != 0) or (len(way) > shortest_way_len == 0):
                shortest_way_len = len(way)
                shortest_way = way

        print("shortest way:")
        print(shortest_way)
        print("Minimum beer number:")
        print(shortest_way_len)

        return shortest_way_len