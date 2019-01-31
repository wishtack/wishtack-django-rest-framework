# -*- coding: utf-8 -*-
#
# (c) 2013-2019 Wishtack
#
# $Id: $
#

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app.todo.todo import TodoSerializer
from app.todo.todo_repository import TodoRepository
from lib.serializer_helpers import serialize


class TodoViewSet(ViewSet):

    def __init__(self, *args, **kwargs):
        self._todo_repository = TodoRepository()

    def list(self, *args):
        """:returns: List of todos."""

        print(args)

        data = self._todo_repository.get_todo_list()

        return Response(
            status=200,
            data={
                'items': serialize(TodoSerializer, data, many=True)
            }
        )
