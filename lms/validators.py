from rest_framework.exceptions import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = dict(value).get(self.field)
        if not link.startswith('https://youtube.com'):
            raise ValidationError(
                'Ссылка на учебные материалы может быть только с YouTube и начинаться с https://youtube.com')

