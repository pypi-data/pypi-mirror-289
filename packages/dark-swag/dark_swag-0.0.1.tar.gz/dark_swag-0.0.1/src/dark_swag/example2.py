from dark_router import get_dark_router
from fastapi import FastAPI



app = FastAPI(docs_url=None, title='MyTestApp')

dark_router = get_dark_router(app,
                              '/_fastapi_static/darkswag.svg',
                              'Example 2')
app.include_router(dark_router)



@app.get('/test', tags=['default section'])
async def test():
    return {'hello': 'world'}

