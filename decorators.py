def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            func_name = func.name
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(result + '\n')
                else:
                    print(f"{func_name} ок")
                return result
            except Exception as e:
                inputs = f"Inputs: {args}" + (f", {kwargs}" if kwargs else "")
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{func_name} error: {type(e)}. {inputs}" + '\n')
                else:
                    print(f"{func_name} error: {type(e)}. {inputs}")
        return inner
    return wrapper
