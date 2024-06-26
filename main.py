from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

from typing import Annotated

app = FastAPI()

# Import File
"""
@app.post("/files", response_model = dict[str, object])
async def read_file_as_bytes(file: Annotated[bytes, File()]):
  return {"size": len(file)}

@app.post("/upload_files", response_model = dict[str, object])
async def read_file_as_upload_file(file: Annotated[UploadFile, File()]):
  filename = file.filename
  content_type = file.content_type
  size = file.size
  content = await file.read()
  await file.close()

  return {
    "filename": filename,
    "content_type": content_type,
    "size": size,
    "content": content
  }
"""

# Optional File Upload
"""
@app.post("/files", response_model = dict[str, object])
async def read_file_as_bytes(file: Annotated[bytes | None, File()] = None):
  if not file:
    return {"message": "No file"}

  return {"size": len(file)}

@app.post("/upload_files", response_model = dict[str, object])
async def read_file_as_upload_file(file: Annotated[UploadFile | None, File()] = None):
  if not file:
    return {"message": "No file"}

  filename = file.filename
  content_type = file.content_type
  size = file.size
  content = await file.read()
  await file.close()

  return {
    "filename": filename,
    "content_type": content_type,
    "size": size,
    "content": content
  }
"""

# UploadFile with Additional Metadata
@app.post("/files", response_model = dict[str, object])
async def read_file_as_bytes(file: Annotated[bytes, File(description = "A file read as bytes")]):
  return {"size": len(file)}

@app.post("/upload_files", response_model = dict[str, object])
async def read_file_as_upload_file(file: Annotated[UploadFile, File(description = "A file read as bytes")]):
  filename = file.filename
  content_type = file.content_type
  size = file.size
  content = await file.read()
  await file.close()

  return {
    "filename": filename,
    "content_type": content_type,
    "size": size,
    "content": content
  }

# Multiple File Uploads
@app.post("/bulk_files")
async def read_files_as_bytes(files: Annotated[list[bytes], File()]):
  return { "sizes": [len(file) for file in files]}

@app.post("/bulk_upload_files")
async def read_files_as_upload_file(files: Annotated[list[UploadFile], File()]):
  return { "sizes": [file.size for file in files]}
