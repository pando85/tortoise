from django.utils.encoding import smart_text
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from tortoise.main.models.user import User
from tortoise.main.models.tag import Tag
from tortoise.main.models.task import Task


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(
                **{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist',
                      slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class TaskSerializer(serializers.ModelSerializer):
    tags = CreatableSlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        slug_field='name')

    class Meta:
        model = Task
        fields = ('name', 'description', 'deadline', 'members', 'tags', 'pk')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = [
            'is_staff', 'is_superuser', 'date_joined', 'last_login',
            'is_active', 'id']
