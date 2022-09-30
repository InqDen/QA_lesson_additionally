import types


def sentencify(name: str):
    import re
    return ' '.join(re.split('_+', name))


def step(fn):
    def fn_with_logging(*args, **kwargs):
        fn_name = sentencify(fn.__name__)
        is_method = (
                args
                and isinstance(args[0], object)
                and isinstance(getattr(args[0], fn.__name__), types.MethodType)
        )
        args_to_log = args[1:] if is_method else args
        print(
            (f'[{args[0].__class__.__name__}] ' if is_method else ' ')
            + fn_name
            + ((': ' + ', '.join(map(str, args_to_log))) if args else ' ')
        )
        return fn(*args, **kwargs)
    return fn_with_logging()

@step
def given_sign_up_form_opened():
    pass


class SigthForm:
    @step
    def fill_email(self, value):
        pass

    @step
    def fill_password(self, value):
        pass

    @step
    def submit(self):
        pass


class DashBoard:
    @step
    def go_to_user_profile(self):
        pass


sign_up_form = SigthForm
dashboard = DashBoard

given_sign_up_form_opened()
sign_up_form.fill_email(value='balbalba@mail.com')
sign_up_form.fill_password('123454321')
sign_up_form.submit()
dashboard.go_to_user_profile()
