# -*- coding: utf-8 -*-
#
# (c) 2013-2019 Wishtack
#

from rest_framework.serializers import Serializer


def deserialize(serializer_class, data, partial=False):
    serializer_instance = serializer_class(data=data, partial=partial)  # type: Serializer

    serializer_instance.is_valid(raise_exception=True)

    return serializer_instance.validated_data


def serialize(serializer_class, instance, many=False):
    serializer = serializer_class(instance=instance, many=many)  # type: Serializer

    return serializer.data
