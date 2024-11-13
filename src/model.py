from pydantic import BaseModel


class Todo(BaseModel):
	id: int
	item: str

	class Config:
		schema_extra = {
			'example': {
				'id': 1,
				'item': 'example schema'
			}
		}


class TodoItem(BaseModel):
	item: str

	class Config:
		schema_extra = {
			'example': {
				'item': 'this is item'
			}
		}
