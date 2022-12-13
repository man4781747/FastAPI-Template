from . import route

def Template_app(fastAPI_app):
  fastAPI_app.add_api_route(
    '/Template_Manager', tags=["2選1選擇結果系統API"],
    endpoint=route.Template_Manager_POST, methods=["GET"],
    summary="123",
  )

