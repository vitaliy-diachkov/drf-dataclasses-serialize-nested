from dataclasses import dataclass, field

from apps.users.fields import SocialSecurityNumberField


@dataclass
class SocialSecurityNumber:
    number: str

    @property
    def hidden(self) -> str:
        return f'SSN <#{self.number}>'

    def __str__(self) -> str:
        return self.hidden


@dataclass
class Profile:
    email: str
    social_security_number: SocialSecurityNumber


@dataclass
class Group:
    name: str


@dataclass
class User:
    id: int
    username: str
    profile: Profile
    groups: list[Group]
