from Tree import Tree, string_to_people

def main():
    input_string = "YNY YNY YNY NYY NYY NYN"
    people = string_to_people(input_string)
    tree = Tree()
    for person in people:
        tree.add_person(person)

    for person in tree.people:
        print(person)

    print(tree.do_it())

if __name__ == "__main__":
    main()