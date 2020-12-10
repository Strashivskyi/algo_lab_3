import unittest
from Tree import Tree
from string_to_people import string_to_people


class TestTree(unittest.TestCase):
    def test_string_to_people(self):
        test_string = "YNYNY YNNYN YNNYN NYYYY NYNYY NYYNY"
        people = string_to_people(test_string)
        self.assertEqual([[1, 3, 5], [1, 4], [1, 4], [2, 3, 4, 5], [2, 4, 5], [2, 3, 5]], people)

    def test_shortest_way_count_easy(self):
        input_string = "YNN YNY YNY NYY NYY NYN"
        people = string_to_people(input_string)
        tree = Tree()
        for each_person in people:
            tree.add_person(each_person)
        ways = tree.find_shortest_way()
        self.assertEqual(2, ways)

    def test_shortest_way_count_hard(self):
        input_string_2 = "NNNNNNYYYN YNNNYNYYNN NNNNYNYYNN YYYNNNNYYY NNYNNNYNNN NYYYYNYYYY NNNNNNNNYN YYYYYNNNNN NNNNNYNNNN YYNNNYNNYY"
        people_2 = string_to_people(input_string_2)
        tree_2 = Tree()
        for each_person in people_2:
            tree_2.add_person(each_person)
        ways_2 = tree_2.find_shortest_way()
        self.assertEqual(4, ways_2)

    def test_shortest_way_count_medium(self):
        input_string_3 = "NNNNY YNNNY NNNNY YYYNN NNYNN NYYYY NNNNN YYYYY YNNNN YNNYY"
        people_3 = string_to_people(input_string_3)
        tree_3 = Tree()
        for each_person in people_3:
            tree_3.add_person(each_person)
        ways_3 = tree_3.find_shortest_way()
        self.assertEqual(3, ways_3)

    def test_empty_string(self):
        input_string = ""
        people = string_to_people(input_string)
        tree = Tree()
        for person in people:
            tree.add_person(person)
        ways = tree.find_shortest_way()
        self.assertEqual(0, ways)

if __name__ == '__main__':
    unittest.main()