from fastapi import FastAPI
from todos.todo import todo_router

app = FastAPI()


@app.get('/')
async def handler_index_get() -> dict:
	return {
		'key': 'value'
	}


app.include_router(todo_router)
