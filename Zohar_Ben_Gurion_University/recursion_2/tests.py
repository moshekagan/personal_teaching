from Zohar_Ben_Gurion_University.recursion_2.main import dict_depth, nested_get, is_valid_integer_csv, connected_nodes

if __name__ == '__main__':
        assert dict_depth({1: "a", 2: "b"}) == 0
        assert dict_depth({1: {1: "a", 2: "b"}, 2: "b"}) == 1
        assert dict_depth({1: {1: "a", 2: "b"}, 2: {1: {1: "a", 2: "b"}, 2: "b"}}) == 2
        assert dict_depth({}) == 0
        try:
            res = dict_depth(None)
        except TypeError as e:
            assert str(e) == "None id not a dict!"

        assert nested_get({1: "a", 2: "b"}, 2) == ["b"]
        assert nested_get({1: {1: "a", 2: "b"}, 2: "b"}, 3) == []
        assert nested_get({1: {1: "a", 2: "b"}, 2: {1: {1: "c", 2: "b"}, 2: "b"}}, 1) == ["a", "c"]
        assert nested_get(None, 1) == []

        assert is_valid_integer_csv("a.csv")
        assert not is_valid_integer_csv("b.csv")
        assert is_valid_integer_csv("c.csv")
        assert not is_valid_integer_csv("d.csv")
        assert not is_valid_integer_csv("e.csv")

        assert sorted(connected_nodes({"A": ["B"], "B": ["D"], "C": ["A", "B"], "D": ["A"]}, "A")) == sorted(["A", "B", "D"])
        assert sorted(connected_nodes({"A":[]},"A")) == sorted(["A"])
        assert sorted(connected_nodes({"A": ["B"], "B": ["D"], "C": ["A", "B"], "D": ["A", "C"]}, "A")) == sorted(["A", "B", "C", "D"])
        assert sorted(connected_nodes({"A": ["B"], "B": ["D"], "C": ["A", "B"], "D": ["A"]}, "C")) == sorted(["A", "B", "C", "D"])
        assert sorted(connected_nodes({"A": ["B"], "B": ["D"], "C": ["A", "B"], "D": []}, "B")) == sorted(["D", "B"])

        print("All pass :) ")
