import google.generativeai as palm


def get_list_of_models():
    return palm.list_models()


if __name__ == "__main__":
    for model in get_list_of_models():
        print(f"name: {model.name}")
        print(f"description: {model.description}")
        print(f"generation methods:{model.supported_generation_methods}\n")


def get_list_of_models_names():
    models = palm.list_models()
    model_names = [model_n.name for model_n in models]  # Create a list of model names
    return model_names


if __name__ == "__main__":
    for name in get_list_of_models_names():
        print(f"Model name: {name}")

# import google.generativeai as palm

# for m in palm.list_models():
#    print(f"name: {m.name}")
#    print(f"description: {m.description}")
#    print(f"generation methods:{m.supported_generation_methods}\n")
