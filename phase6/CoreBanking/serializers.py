from rest_framework.fields import IntegerField, CharField, FloatField, ChoiceField
from rest_framework.serializers import ModelSerializer, Serializer


class LoginSerializer(Serializer):
    username = CharField(max_length=50,
                         default='unknown',
                         style={'placeholder': 'Username'})
    password = CharField(max_length=50,
                         default='unknown',
                         style={'input_type': 'password', 'placeholder': 'Password'})


class CenterCreationSerializer(Serializer):
    center_id = IntegerField(default=0)
    name = CharField(max_length=30)
    address = CharField(max_length=100)


class BankManagerCreateUserSerializer(Serializer):
    melli_code = IntegerField(default=0)
    username = CharField(max_length=30, default='unknown')
    password = CharField(max_length=30, default='unknown',
                         style={'input_type': 'password', 'placeholder': 'Password'})
    membership_type = ChoiceField(
        choices=[
            "legal_expert",
            "center_manager",
            "cashier",
            "auditor",
            "accountant"
        ]
    )


class CenterManagerCreateUserSerializer(Serializer):
    melli_code = IntegerField(default=0)
    username = CharField(max_length=30, default='unknown')
    password = CharField(max_length=30, default='unknown',
                         style={'input_type': 'password', 'placeholder': 'Password'})
    membership_type = ChoiceField(
        choices=[
            "legal_expert",
            "center_manager",
            "cashier",
            "auditor",
            "accountant"
        ]
    )
