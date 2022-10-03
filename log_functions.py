import types
from functools import wraps


def humanify(name: str):
    import re
    return ' '.join(re.split('_+', name))


def step(fn):
    @wraps(fn)
    def fn_with_logging(*args, **kwargs):
        is_method = (
                args
                and isinstance(args[0], object)
                # and isinstance(getattr(args[0], fn.__name__), types.MethodType)
                and isinstance(getattr(args[0], fn.__name__), types.MethodType)
        )

        args_to_log = args[1:] if is_method else args
        args_and_kwargs_to_log_as_strings = [
            *map(str, args_to_log),
            *[f'{key}={value}' for key, value in kwargs.items()]
        ]
        args_and_kwargs_string = (
            (': ' + ', '.join(map(str, args_and_kwargs_to_log_as_strings)))
            if args_and_kwargs_to_log_as_strings
            else ''
        )

        print(
            (f'[{args[0].__class__.__name__}] ' if is_method else '')
            + humanify(fn.__name__)
            + args_and_kwargs_string
        )

        return fn(*args, **kwargs)

    return fn_with_logging


@step
def given_sign_up_form_opened():
    ...


class SignUpForm:
    @step
    def fill_name(self, first_name, surname):
        pass
        return self

    @step
    def fill_email(self, value):
        pass
        return self

    @step
    def fill_password(self, value):
        pass
        return self

    @step
    def submit(self):
        pass
        return self


class DashBoard:
    ...

    @step
    def go_to_user_profile(self):
        pass


sign_up_form = SignUpForm()
dashboard = DashBoard()

given_sign_up_form_opened()
(sign_up_form
 .fill_name('Inq', surname='.Den')
 .fill_email(value='balbalba@mail.com')
 .fill_password('123454321')
 .submit()
 )
dashboard.go_to_user_profile()

'''
given_sign_up_form_opened()
sign_up_form.fill_name('Inq', surname= '.Den')
sign_up_form.fill_email(value= 'adsa@asdfs.df')
sign_up_form.fill_password('234123')
sign_up_form.submit()
'''
