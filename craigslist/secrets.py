# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y$dhg!4)71(p2x1ih7^)3=5^t)h88is&y=fhonu$%qs945r#rr'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cl',
        'USER': 'hrumba',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
