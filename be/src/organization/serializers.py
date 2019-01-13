from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from django.core import exceptions

from rest_framework import serializers

from org.serializers import (UserSerializer as OriginalUserSerializer, )
from .models import User


class UserSerializer(OriginalUserSerializer):
    password = serializers.CharField(allow_blank=True, write_only=True)
    kind_entity = serializers.IntegerField(
        label=_('Kind Entity'), source='kind_entity_id', allow_null=True, min_value=1)

    def validate_kind(self, kind):
        if self.instance and self.instance.kind and self.instance.kind != kind:
            raise serializers.ValidationError(
                _("Kind of user cannot be changed once created."))
        return kind

    def validate(self, data):
        errors = {}
        if data.get('kind') and data.get('kind') in [User.KIND_ADMINISTRATOR, ] and data.get('kind_entity_id'):
            errors['kind_entity'] = _(
                "This field must be blank for user of the given kind."
            )
        elif data.get('kind') and data.get('kind') not in [User.KIND_ADMINISTRATOR, ] and not data.get('kind_entity_id'):
            errors['kind_entity'] = _("This field may not be blank.")

        if not self.instance and ('password' not in data or not data['password']):
            errors['password'] = _("This field may not be blank.")

        if 'password' in data:
            try:
                password_validation.validate_password(
                    password=data['password'], user=self.instance)
                data['password'] = make_password(data['password'])
            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)[0]

        if errors:
            raise serializers.ValidationError(errors)

        return data

    class Meta(OriginalUserSerializer.Meta):
        fields = OriginalUserSerializer.Meta.fields + \
            ('kind_entity', 'password')
