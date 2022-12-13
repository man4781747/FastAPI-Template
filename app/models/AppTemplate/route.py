from fastapi import Request, Query, Path, Form, HTTPException, status, Response
from fastapi.responses import JSONResponse
from typing import Union, Optional
import json
import datetime
import sqlite3
import os
from pydantic import BaseModel
import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

S_sqlite3_folder_path = os.path.dirname(os.path.realpath(__file__))
S_db_file_path = os.path.join(S_sqlite3_folder_path,"TemplateDatabase.db")
S_schema_file_path = os.path.join(S_sqlite3_folder_path,"template_schema.sql")

# 定義sql得到的資料要怎麼儲存
def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

# 輸入Sql來獲得指定資料
def getDataBySQLCommand(S_sql, data, db_file_path=S_db_file_path):
  conn = sqlite3.connect(db_file_path)
  conn.row_factory = dict_factory
  c = conn.cursor()
  L_execute = c.execute(S_sql, data)
  L_return = []
  for row in L_execute:
    L_return.append(row)
  conn.commit()
  conn.close()
  if L_return != None:
    return L_return
  return []

# 初始化 DB
def init_db():
  if os.path.exists(S_db_file_path) == False:
    conn = sqlite3.connect(S_db_file_path)
    c = conn.cursor()
    with open(S_schema_file_path, mode='r') as f:
      S_contest = f.read()
      c.execute(S_contest)
    conn.commit()
    conn.close()
init_db()

async def Template_Manager_POST(
  response: Response,request: Request,):
  """
    https://github.com/tiangolo/fastapi/issues/246
  """
  try:

    response.status_code = 202
    return {"result": "success"}
  except Exception as e:
    return {"result":"fail", "data": str(e)}

