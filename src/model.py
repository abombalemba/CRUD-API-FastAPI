from fastapi import Form
from pydantic import BaseModel

from typing import List, Optional


class Todo(BaseModel):
	id: Optional[int]
	item: str

	@classmethod
	def as_form(cls, item: str = Form(...)):
		return cls(item=item)

	class Config:
		json_schema_extra = {
			'example': {
				'id': 1,
				'item': 'string'
			}
		}


class TodoItem(BaseModel):
	item: str

	class Config:
		json_schema_extra = {
			'example': {
				'item': 'string'
			}
		}


class TodoItems(BaseModel):
	todos: List[TodoItem]

	class Config:
		json_schema_extra = {
			'example': {
				'todos': [
					{
						'item': 'item1'
					},
					{
						'item': 'item2'
					},
					{
						'item': 'item3'
					}
				]
			}
		}
