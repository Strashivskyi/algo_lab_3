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
        self.people.append(person_nodes)

    def do_it(self):
        shortest_way = 0
        if len(self.people) == 0:
            return 0
        for beer_node in self.people[-1]:
            print(self.people[-1])
            beer = beer_node
            way = []
            while not beer is None:
                way.append(beer.value)
                beer = beer.parent
            way = list(dict.fromkeys(way))

            if (len(way) < shortest_way != 0) or (len(way) > shortest_way == 0):
                shortest_way = len(way)

        return shortest_way


def string_to_people(input_string):
    input_string = input_string.split(" ")
    people = []
    for i in range(len(input_string)):
        people.append([])
        for beer in range(len(input_string[i])):
            if input_string[i][beer] == "Y":
                people[i].append(beer + 1)

    return people