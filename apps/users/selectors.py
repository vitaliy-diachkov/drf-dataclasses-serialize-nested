from apps.users.dataclasses import Group, Profile, SocialSecurityNumber, User


def get_users() -> list[User]:
    return [
        User(
            id=1,
            username='My username',
            profile=Profile(
                email='admin@gmail.com',
                social_security_number=SocialSecurityNumber(
                    number='12345678'
                )
            ),
            groups=[
                Group(name='Users'),
                Group(name='Admins')
            ]
        )
    ]
