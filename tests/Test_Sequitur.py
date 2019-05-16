from utilities.grammar_algorithms.k_Sequitur import k_Sequitur

def test_generate_1_layer_of_rules():
    """Tests generate_1_layer_of_rules"""
    obj = k_Sequitur(2)
    string = [0, 1, 0, 0, 1, 0, 0, 0, 0]
    rules, reverse_rules = obj.generate_1_layer_of_rules(string)
    assert rules["R0"] == (0, 1)
    assert rules["R1"] == (0, 0)
    assert set(rules.keys()) == {"R0", "R1"}
    assert reverse_rules[(0, 1)] == "R0"
    assert reverse_rules[(0, 0)] == "R1"
    assert set(reverse_rules.keys()) == {(0, 1), (0, 0)}

    obj = k_Sequitur(2)
    string = [0, 1, 0, 0, 1, 0, 0, 0]
    rules, reverse_rules  = obj.generate_1_layer_of_rules(string)
    assert rules["R0"] == (0, 1)
    assert set(rules.keys()) == {"R0"}
    assert reverse_rules[(0, 1)] == "R0"
    assert set(reverse_rules.keys()) == {(0, 1)}

    obj = k_Sequitur(3)
    string = [0, 1, 0, 0, 1, 0, 0, 0]
    rules, reverse_rules  = obj.generate_1_layer_of_rules(string)
    print(rules)
    assert set(rules.keys()) == set()
    assert set(reverse_rules.keys()) == set()

    obj = k_Sequitur(3)
    string = [0, 1, 0, 0, 1, 0, 0, 0, 0]
    rules, reverse_rules  = obj.generate_1_layer_of_rules(string)
    print(rules)
    assert set(rules.keys()) == {"R0"}
    assert set(reverse_rules.keys()) == {(0, 0)}

    obj = k_Sequitur(2)
    string = [2, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 2, 0, 1]
    rules, reverse_rules = obj.generate_1_layer_of_rules(string)
    assert rules["R0"] == (0, 1)
    assert rules["R1"] == (0, 0)
    assert rules["R2"] == (2, 2)
    assert set(rules.keys()) == {"R0", "R1", "R2"}
    assert reverse_rules[(0, 1)] == "R0"
    assert reverse_rules[(0, 0)] == "R1"
    assert reverse_rules[(2, 2)] == "R2"
    assert set(reverse_rules.keys()) == {(0, 1), (0, 0), (2, 2)}

def test_convert_a_string_using_reverse_rules():
    """Tests convert_a_string_using_reverse_rules method"""
    obj = k_Sequitur(2)

    string = [0, 1, 0, 1, 2, 3, 4, 4, 4, 4]
    rules, reverse_rules  = obj.generate_1_layer_of_rules(string)
    new_string, _ = obj.convert_a_string_using_reverse_rules(string, reverse_rules)
    assert new_string == ["R0", "R0", 2, 3, "R1", "R1"]

    string = ["R0", "R1", "R0", "R1", 2, 3, "R1", "R1", 2, 3]
    rules, reverse_rules = obj.generate_1_layer_of_rules(string)
    new_string, _ = obj.convert_a_string_using_reverse_rules(string, reverse_rules)
    assert new_string == ["R2", "R2", "R3", "R1", "R1", "R3"]

    string = [0, 3, 1, 22, 44, "R1"]
    rules, reverse_rules = obj.generate_1_layer_of_rules(string)
    new_string, _ = obj.convert_a_string_using_reverse_rules(string, reverse_rules)
    assert new_string == string

    string = ["R3341341414", "R1"]
    rules, reverse_rules = obj.generate_1_layer_of_rules(string)
    new_string, _ = obj.convert_a_string_using_reverse_rules(string, reverse_rules)
    assert new_string == string

    obj = k_Sequitur(2)
    string = ["R12", "R12", "R1", "R12", "R1", "R1"]
    rules, reverse_rules = obj.generate_1_layer_of_rules(string)
    new_string, _ = obj.convert_a_string_using_reverse_rules(string, reverse_rules)
    assert new_string == ["R12", "R0", "R0", "R1"]

def test_get_next_rule_name():
    """Tests get_next_rule_name works correctly"""
    obj = k_Sequitur(2)
    string = [0, 1, 2, 3, 2, 3, 0, 1]
    assert obj.next_rule_name_ix == 0

    obj.generate_1_layer_of_rules(string)
    assert obj.next_rule_name_ix == 2

    obj.generate_1_layer_of_rules(string)
    assert obj.next_rule_name_ix == 4

    for ix in range(80):
        obj.generate_1_layer_of_rules(string)
        assert obj.next_rule_name_ix == 4 + (1+ix)*2

def test_generate_1_layer_of_rules_gives_reverse_rules_correctly():
    """Tests generate_1_layer_of_rules"""
    for string in ["agafsfaghghhghghgh", "afdfas", "a", "aabbababababdfdfdfoeorirjajdgsjgkdajfjafdkjasrjajjsjsjsjdjdjkafdkkdksjdfjsdkafklasfkafsl", "aaaaaaaaa"]:
        for k in range(1, 5):
            obj = k_Sequitur(2)
            rules, reverse_rules = obj.generate_1_layer_of_rules(string)
            assert reverse_rules == {v: k for k, v in rules.items()}

def test_convert_symbol_to_raw_actions():
    """Tests convert_symbol_to_raw_actions"""
    obj = k_Sequitur(2)
    symbol = "R0"
    rules = {"R0": (0, 1)}
    converted_symbol = obj.convert_symbol_to_raw_actions(symbol, rules)
    assert  converted_symbol == (0, 1)

    symbol = "R1"
    rules = {"R1": (5, "R0"), "R0": (0, 1)}
    converted_symbol = obj.convert_symbol_to_raw_actions(symbol, rules)
    assert  converted_symbol == (5, 0, 1)

    symbol = "R5"
    rules = {"R5": ("R1", "R0"), "R1": (5, "R0"), "R0": (0, 1)}
    converted_symbol = obj.convert_symbol_to_raw_actions(symbol, rules)
    assert  converted_symbol == (5, 0, 1, 0, 1)

def test_generate_grammar_new_string_and_all_rules():
    """Tests generate_grammar"""
    obj = k_Sequitur(2)
    string = [0, 1, 0, 1,  0, 2, 0, 2, 0, 1, 0, 2, 0, 1, 4, 2]
    new_string, all_rules, _ = obj.generate_action_grammar(string)
    assert new_string == ["R0", "R2", "R1", "R2", "R0", 4, 2]
    assert all_rules == {"R0": (0, 1), "R1": (0, 2), "R2": ("R0", "R1")}

    obj = k_Sequitur(2)
    string = [0, 1, 0, 1, 0, 1, 0, 1]
    new_string, all_rules, _ = obj.generate_action_grammar(string)
    assert new_string == ["R1", "R1"], new_string
    assert all_rules == {"R0": (0, 1), "R1": ("R0", "R0")}

    for repetition in range(1, 16):
        obj = k_Sequitur(2)
        string = [0, 1] * repetition
        new_string, all_rules, _ = obj.generate_action_grammar(string)
        if repetition < 2:
            assert new_string == [0, 1]
            assert all_rules == {}
        elif repetition < 4:
            assert new_string == ["R0"] * repetition
            assert all_rules == {"R0": (0, 1)}
        elif repetition < 8:
            expected_string = ["R1"] * int(repetition/2)
            expected_string += ["R0"] * int(repetition % 2)
            assert new_string ==  expected_string
            assert all_rules == {"R0": (0, 1), "R1": ("R0", "R0")}
        elif repetition < 16:
            expected_string = ["R2"] * int(repetition / 4)
            expected_string += ["R1"] * int((repetition % 4)/2)
            expected_string += ["R0"] * int(repetition % 2)
            assert new_string == expected_string
            assert all_rules == {"R0": (0, 1), "R1": ("R0", "R0"), "R2": ("R1", "R1")}

def test_generate_action_grammar_action_usage_count():

    obj = k_Sequitur(2)
    string = [0, 1, 0, 1, 0, 1, 0, 1]
    _, _, action_usage_count = obj.generate_action_grammar(string)
    assert action_usage_count == {(0, 1): 4, (0, 1, 0, 1): 2}

    obj = k_Sequitur(3)
    string = [0, 1, 0, 1, 0, 1, 0, 1]
    _, _, action_usage_count = obj.generate_action_grammar(string)
    assert action_usage_count == {(0, 1): 4}

    obj = k_Sequitur(2)
    string = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
    _, _, action_usage_count = obj.generate_action_grammar(string)
    print(action_usage_count)
    assert action_usage_count == {(0, 0): 3, (1, 0): 3, (0, 0, 1, 0): 2}

def test_generate_grammar_deals_with_end_symbols_correctly():

    obj = k_Sequitur(2)
    string = [0, 1, 0, 1, 0, 1, 0, 1]
    new_string, all_rules, action_usage_count = obj.generate_action_grammar(string)
    assert action_usage_count == {(0, 1): 4, (0, 1, 0, 1): 2}
    assert new_string == ["R1", "R1"]
    assert all_rules == {"R0": (0, 1), "R1": ("R0", "R0")}

    obj = k_Sequitur(2)
    string = [0, 1, 0, 1, "/", 0, 1, 0, 1]
    new_string, all_rules, action_usage_count = obj.generate_action_grammar(string)
    assert action_usage_count == {(0, 1): 4, (0, 1, 0, 1): 2}
    assert new_string == ["R1", "/", "R1"]
    assert all_rules == {"R0": (0, 1), "R1": ("R0", "R0")}

    obj = k_Sequitur(2)
    string = [0, 1, "/", 0, 1, "/", 0, 1, 0, 1, 0, 1, 0, 1]
    new_string, all_rules, action_usage_count = obj.generate_action_grammar(string)
    assert action_usage_count == {(0, 1): 6, (0, 1, 0, 1): 2}
    assert new_string == ["R0", "/", "R0",  "/", "R1", "R1"]
    assert all_rules == {"R0": (0, 1), "R1": ("R0", "R0")}

    obj = k_Sequitur(2)
    string = [0, 1, 0, 1, 0, 1, "/", 0, 1]
    new_string, all_rules, action_usage_count = obj.generate_action_grammar(string)
    assert action_usage_count == {(0, 1): 4}
    assert new_string == ["R0", "R0", "R0", "/", "R0"]
    assert all_rules == {"R0": (0, 1)}

def test_ignores_end_symbol_correctly

    do this...