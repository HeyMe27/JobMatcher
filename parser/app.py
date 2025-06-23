
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp.pdf", "wb") as f:
        f.write(contents)

    doc = fitz.open("temp.pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    skills = []
    for kw in ["Java", "Python", "React", "Node", "Spring", "AWS", "SQL"]:
        if kw.lower() in text.lower():
            skills.append(kw)

    return {"skills": skills}
