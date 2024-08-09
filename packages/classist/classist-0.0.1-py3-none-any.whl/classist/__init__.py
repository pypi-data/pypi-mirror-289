import inspect


def decorator(cls):
    print("Decorating", cls)
    base_classes = cls.__bases__

    assert isinstance(base_classes, tuple)
    assert len(base_classes) > 0

    # If the first base class is an object, then there is nothing to be decorated
    if base_classes[0].__name__ == "object":
        return cls

    print("Getting methods.")
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    base_methods = {
        method_name: method
        for base_cls in base_classes
        for method_name, method in inspect.getmembers(
            base_cls, predicate=inspect.isfunction
        )
    }
    print(methods)

    for method_name, method in methods:
        base_method = base_methods.get(method_name)

        print("Method:", method_name)

        # Skip the method if it is not a method of any base class
        if base_method is None:
            continue

        # Skip the method if it is the same as the method of the base class
        if method == base_method:
            continue

        method_signature = inspect.signature(method)
        base_method_signature = inspect.signature(base_method)

        parameters = {
            **base_method_signature.parameters,
            **method_signature.parameters,
        }

        method.__signature__ = inspect.Signature(parameters.values())

    return cls
