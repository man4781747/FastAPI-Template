from fastapi import FastAPI

from .models.AppTemplate import *

def runApp(fastAPI_app):
  Template_app(fastAPI_app)
  return fastAPI_app