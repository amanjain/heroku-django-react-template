from django.contrib.contenttypes.models import ContentType

from org.viewsets import UserViewSet as OriginalUserViewSet
from .models import User


class UserViewSet(OriginalUserViewSet):
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.kind != 'administrator':
            qs = qs.none()
        return qs

    def perform_create(self, serializer):
        content_type = ContentType.objects.get_for_model(
            User.KIND_MODELS[serializer.validated_data['kind']]) if serializer.validated_data['kind'] in User.KIND_MODELS else None
        serializer.save(org=self.request.user.org,
                        kind_entity_content_type=content_type)
