
def describe_call(*args, **kwargs) -> str:
    if args and kwargs:
        return f'args: {args}, kwargs: {kwargs}'
    elif args:
        return f'args: {args}'
    elif kwargs:
        return f'kwargs: {kwargs}'
    else:
        return "no arguments"