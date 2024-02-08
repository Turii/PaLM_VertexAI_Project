from list_models import get_list_of_models_names


def test_list_models_returns_non_empty_list():
    model_names = get_list_of_models_names()
    for name in get_list_of_models_names():
        print(f"Model name: {name}")
    assert len(model_names) > 0, 'Expected at least one model in the list '
