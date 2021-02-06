# brief: class implements logic like lambda-expression
class Lambda:
    def __init__(self, action, *args, **kwargs):
        self._action = action
        self._params1 = args
        self._params2 = kwargs

    def __call__(self):
        return self._action(*self._params1, **self._params2)
