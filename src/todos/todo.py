from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()

todo_list = []


@todo_router.get('/todo')
async def handler_todo_get() -> dict:
	return {
		'todos': todo_list
	}


@todo_router.post('/todo')
async def handler_todo_post(todo: Todo) -> dict:
	todo_list.append(todo)

	return {
		'message': 'todo added successfully'
	}


@todo_router.get('/todo/{todo_id}')
async def handler_todo_id_get(todo_id: int = Path(..., title='The ID of the todo to retrieve')) -> dict:
	for todo in todo_list:
		if todo.id == todo_id:
			return {
				'todo': todo
			}

	return {
		'message': f'todo with id {todo_id} does not exist'
	}


@todo_router.put('/todo/{todo_id}')
async def hander_todo_id_put(todo_data: TodoItem, todo_id: int = Path(..., title='The ID of the todo to be updated')) -> dict:
	for todo in todo_list:
		if todo.id == todo_id:
			todo.item = todo_data.item

			return {
				'message': 'todo is updated successfully'
			}

	return {
		'message': f'todo with id {todo_id} does not exist'
	}


@todo_router.delete('/todo/{todo_id}')
async def handler_todo_id_delete(todo_id: int) -> dict:
	for i in range(len(todo_list)):
		todo = todo_list[i]
		if todo.id == todo_id:
			todo_list.pop(i)

			return {
				'message': 'todo is deleted successfully'
			}

	return {
		'message': f'todo with id {todo_id} does not exist'
	}


@todo_router.delete('/todo')
async def handler_todo_delete() -> dict:
	todo_list.clear()

	return {
		'message': 'all todo are deleted successfully'
	}
