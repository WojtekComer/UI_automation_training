import pytest

from ..utils.data_utils import DataUtils


@pytest.hookimpl(hookwrapper=False)
def pytest_bdd_before_step(step):
    print(f'STEP STARTED {DataUtils.current_date_and_time()}. {step.keyword}: {step.name}')


@pytest.hookimpl(hookwrapper=False)
def pytest_bdd_after_step(step):
    print(f'STEP FINISHED {DataUtils.current_date_and_time()}. {step.keyword}: {step.name}')
    print('-' * (18 + len(DataUtils.current_date_and_time()) + len(step.keyword) + len(step.name)))


@pytest.hookimpl(hookwrapper=False)
def pytest_bdd_before_scenario(scenario):
    print(f'\n        *** TEST STARTED -> scenario: {scenario.name} ***\n')


@pytest.hookimpl(hookwrapper=False)
def pytest_bdd_after_scenario(scenario):
    print(f'        ***  TEST FINISHED -> Scenario: {scenario.name} ***')
