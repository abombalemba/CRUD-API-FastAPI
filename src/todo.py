from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory='templates/')


@todo_router.get('/todo', response_model=TodoItems)
async def handler_todo_get(request: Request):
	return templates.TemplateResponse('todo.html', {
		'request': request,
		'todos': todo_list
	})


@todo_router.post('/todo')
async def handler_todo_post(request: Request, todo: Todo = Depends(Todo.as_form)):
	todo.id = len(todo_list) + 1
	todo_list.append(todo)

	return templates.TemplateResponse('todo.html', {
		'request': request,
		'todos': todo_list
	})


@todo_router.delete('/todo')
async def handler_todo_delete() -> dict:
	todo_list.clear()

	return {
		'message': 'all todo are deleted successfully'
	}


@todo_router.get('/todo/{todo_id}')
async def handler_todo_id_get(trequest: Request, todo_id: int = Path(..., title='The ID of the todo to retrieve')):
	for todo in todo_list:
		if todo.id == todo_id:
			return templates.TemplateResponse('todo.html', {
				'request': request,
				'todo': todo
			})
	
	raise HTTPException(
		status_code=status.HTTP_404_NOT_FOUND,
		detail=f'todo with id {todo_id} does not exist'
	)


@todo_router.put('/todo/{todo_id}')
async def hander_todo_id_put(request: Request, todo_data: TodoItem, todo_id: int = Path(..., title='The ID of the todo to be updated')) -> dict:
	for todo in todo_list:
		if todo.id == todo_id:
			todo.item = todo_data.item

			return {
				'message': 'todo is updated successfully'
			}

	raise HTTPException(
		status_code=status.HTTP_404_NOT_FOUND,
		detail=f'todo with id {todo_id} does not exist'
	)


@todo_router.delete('/todo/{todo_id}')
async def handler_todo_id_delete(request: Request, todo_id: int) -> dict:
	for i in range(len(todo_list)):
		todo = todo_list[i]
		if todo.id == todo_id:
			todo_list.pop(i)

			return {
				'message': 'todo is deleted successfully'
			}

	raise HTTPException(
		status_code=status.HTTP_404_NOT_FOUND,
		detail=f'todo with id {todo_id} does not exist'
	)
