# -*- coding: utf-8 -*-
#
# (c) 2013-2019 Wishtack
#
from dataclasses import dataclass

from rest_framework import serializers
from rest_framework.serializers import Serializer


@dataclass
class Todo:
    id: str
    title: str


class TodoSerializer(Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
