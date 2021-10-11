from rest_framework.fields import Field


class SocialSecurityNumberField(Field):
    def __init__(self, *args, **kwargs):
        kwargs.pop('dataclass', None)
        kwargs.pop('many', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        print('Called to_representation')
        return value.hidden