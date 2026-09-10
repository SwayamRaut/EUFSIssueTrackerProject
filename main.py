from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.routes.issue_routes import router as issues_router
from app.routes.component_routes import router as components_router
from app.database import engine, Base
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.schemas.error_schema import ErrorDetail, ErrorResponse


#Create tables on startup
#Base.metadata.create_all(engine)


app = FastAPI() #intialize fast api and set into a variable
app.include_router(issues_router) #take all the routes inside issues_router and attach them to the main FastAPI app.
app.include_router(components_router)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(status_code=exc.status_code, content=ErrorResponse(error=ErrorDetail(code="HTTP_ERROR", message=str(exc.detail))).model_dump())

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content=ErrorResponse(error=ErrorDetail(code="VALIDATION_ERROR", message="Request validation failed", details=exc.errors())).model_dump())


#We do not put all our routes in the main entry point
"""
#GET request route to show simple status
@app.get("/health")
def health_check():
    return {"status": "ok"}

items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
    {"id": 3, "name": "Item Three"},
]

#GET request to display items list
#@app.get("/items")
#def get_items():
    #return items

#get a single item by it's id
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

#GET request with query params
@app.get("/items")
def read_items(start: int = 0, limit: int=2):
    return items[start : start+limit]

#POST request route example
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return items

"""