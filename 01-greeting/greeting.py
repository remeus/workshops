def give_and(names):
    return names[0] + ' and ' + names[1]


def greet_3(names):
    return give_and([", ".join(names[:len(names)-1]), names[-1]])


def greet(name):
    if name is None:
        return "Hello, my friend."

    if isinstance(name, list):
        name = ', '.join(name)
        name = name.split(", ")

        if len(name) > 2:
            upper_names = []
            lower_names = []

            for item in name:
                if item.isupper():
                    upper_names.append(item)
                else:
                    lower_names.append(item)

            if len(upper_names) == 0:
                return f"Hello, {greet_3(lower_names)}."
            else:
                return greet(lower_names) + " AND " + greet(upper_names[0])
        else:
            return f"Hello, {give_and(name)}."
    if name.isnumeric():
        return "Hello, robot."
    if name.upper() == name:
        return f"HELLO {name}!"
    return f"Hello, {name}."
