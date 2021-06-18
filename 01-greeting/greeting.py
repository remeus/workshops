def give_and(names):
    return names[0] + ' and ' + names[1]


def greet_3(names):
    return give_and([", ".join(names[:len(names)-1]), names[-1]])


def greet(name):
    if name is None:
        return "Hello, my friend."
    if isinstance(name, list):
        if len(name) > 2:
            return f"Hello, {greet_3(name)}."
        else:
            return f"Hello, {give_and(name)}."
    if name.isnumeric():
        return "Hello, robot."
    if name.upper() == name:
        return f"HELLO {name}!"
    return f"Hello, {name}."
