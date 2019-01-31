# -*- coding: utf-8 -*-
#
# (c) 2013-2019 Wishtack
#
from typing import List

from app.todo.todo import Todo


class TodoRepository:

    def get_todo_list(self) -> List[Todo]:
        return [
            Todo(id="0", title="Django Setup"),
            Todo(id="1", title="Django Rest Framework Setup"),
            Todo(id="2", title="Heroku Setup"),
            Todo(id="3", title="MongoDB Setup")
        ]
