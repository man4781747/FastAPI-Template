from . import route
from pydantic import BaseModel, Field


class OutputModelV1(BaseModel):
    "First version of output data"
    id: int | None = Field(description="Id")
    owner: int | None = Field(description="Owner Id")


class OutputModelV2(BaseModel):
    "Secnod version of output data. Ids moved to strings, owner name supplied as well."
    id: str | None = Field(description="Id")
    owner_id: str | None = Field(description="Owner Id")
    owner_name: str | None = Field(description="Owner Name")

def Template_app(fastAPI_app):
  fastAPI_app.add_api_route(
    '/Template_Manager', tags=["API TAG 分類測試","API TAG 分類測試-2"],
    endpoint=route.Template_Manager_POST, methods=["GET"],
    summary="summary測試", description="description測試",
    response_description="response_description測試",
    responses={ # https://fastapi.tiangolo.com/advanced/additional-responses/?h=responses
      201: {
        "description": "Status Code 201 Test",
        "content": {
          "application/json": {                    
            "schema": {
              "properties": {
                "message": {
                  "title": "Message",
                  "type": "string"
                },
                "objectTest": { 
                  "title": "Message",
                  "type": "object"
                },
              }
            }
          },
        },
        
      },
    },
    response_model=OutputModelV2
  )

