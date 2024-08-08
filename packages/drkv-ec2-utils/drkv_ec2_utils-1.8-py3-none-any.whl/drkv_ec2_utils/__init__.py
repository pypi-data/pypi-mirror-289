def validate_config(func):
    def valid(*args, **kwrgs):
        print("Args :", args)
        val, val_type = args[-3:-1:] if args and type(args[-1]) is bool else args[-2::]
        val = cast(val)
        print(val, val_type)
        print(isinstance(val, val_type), type(val))
        return func(*args, **kwrgs) if isinstance(val, val_type) else False
    return valid


def cast(value):
    try:
        return eval(value)
    except (NameError, SyntaxError, TypeError):
        return value


def check_and_cast_config(val):
    if "::" in val:
        val_type, val = val.split("::")
        val = cast(val)
        if val_type == type(val).__name__:
            return val
    else:
        return cast(val)
class A:
    def __init__(self, silent=True):
        self.silent = silent

    @validate_config
    def c(self, val, val_type, silent=True):
        print(val, val_type)
        val = f"{val_type.__name__}::{val if val else ' '}"
        return val

    def d(self, val):
        return check_and_cast_config(val)

    def e(self, vals):
        g = []
        for val in vals:
            if mv := check_and_cast_config(val):
                g.append(mv)
        return g

if __name__ == "__main__":
    # print("Method 1: ", A().c("1.0", float))
    print("Method 2: ", A().d("str::2"))
    print("Method 3: ", A().e(["4", "int::5", "float::4.0", "str::2"]))

