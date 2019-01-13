from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


from org.models import (AbstractOrg, AbstractUser, AbstractDomain, )


class Org(AbstractOrg, ):
    pass


class Domain(AbstractDomain, ):
    pass


class User(AbstractUser):
    KIND_ADMINISTRATOR = 'administrator'

    KIND_CHOICES = (
        (KIND_ADMINISTRATOR, 'Administrator'),
    )
    kind = models.CharField(choices=KIND_CHOICES,
                            max_length=32, db_index=True, )
    KIND_MODELS = {}

    kind_entity_limit = models.Q()
    kind_entity_content_type = models.ForeignKey(
        ContentType, limit_choices_to=kind_entity_limit, on_delete=models.CASCADE, null=True, blank=True, default=None, )
    kind_entity_id = models.PositiveIntegerField(
        null=True, blank=True, default=None, )
    kind_entity = GenericForeignKey(
        'kind_entity_content_type', 'kind_entity_id')

    def __str__(self):
        return self.email

    class Meta(AbstractUser.Meta):
        abstract = False
