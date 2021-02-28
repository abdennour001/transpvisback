from enum import Enum


class ChoicesEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: (c.value, c.value), cls))

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class StakeholderTypes(ChoicesEnum):
    INFORMATION_PROVIDER = "Information provider"
    INFORMATION_RECEIVER = "Information receiver"


class InformationElementTypes(ChoicesEnum):
    DATA = "data"
    PROCESS = "process"
    POLICY = "policy"


class StakeholderInformationRelationshipTypes(ChoicesEnum):
    PRODUCTION = "production"
    OPTIONAL = "optional"
    OBLIGATORY = "obligatory"
    RESTRICTED = "restricted"
    UNDECIDED = "undecided"