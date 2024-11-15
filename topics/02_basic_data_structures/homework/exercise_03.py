"""
2. Research about fronzenset(). You are building a test automation framework and want to store a collection of test case
   scenarios (with unique steps) in an immutable set so that the test scenarios can’t be altered. Each test scenario is
   a list of test steps, and you want to avoid duplicates.
   - Use frozenset() to store the test steps of each scenario in an immutable set.
   - Store each test scenario in a dictionary where the key is the test case name and the value is the frozenset of steps
   - Write a function that, given a test case name, prints whether the scenario already exists in the dictionary
   - Examples of test steps for different scenarios:
     - steps_1 = ["open browser", "navigate to page", "click login"]
     - steps_2 = ["open browser", "navigate to page", "fill form"]
     - steps_3 = ["open browser", "navigate to page", "click login"] # duplicate steps
"""
from typing import List


def get_key_from_value(dict_to_check: dict[str, frozenset], target_value: frozenset) -> str | None:
    for k, v in dict_to_check.items():
        if v == target_value:
            return k
    return None


def add_test_scenario(scenarios: dict[str, frozenset], test_case_name: str, steps: List[str]) -> None:
    scenario = frozenset(steps)
    if scenario in scenarios.values():
        key = get_key_from_value(scenarios, scenario)
        print(f"The test scenario for '{key}' already exists.")
    else:
        scenarios[test_case_name] = scenario
        print(f"Test scenario '{test_case_name}' added successfully.")


test_scenarios = {}

steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"]  # duplicate steps

all_steps = [steps_1, steps_2, steps_3]
index_test_case = 0  # Helper to naming the test cases
for step in all_steps:
    test_case = f"TC_{index_test_case}"
    add_test_scenario(test_scenarios, test_case, step)
    index_test_case += 1

print("\nAll test scenarios from the dictionary:")
for k, v in test_scenarios.items():
    print(f"Test Case '{k}': {list(v)}")

"""
Output:
    Test scenario 'TC_0' added successfully.
    Test scenario 'TC_1' added successfully.
    The test scenario for 'TC_0' already exists.
    
    All test scenarios from the dictionary:
    Test Case 'TC_0': ['click login', 'navigate to page', 'open browser']
    Test Case 'TC_1': ['navigate to page', 'fill form', 'open browser']
"""