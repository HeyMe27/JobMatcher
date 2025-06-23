
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_jobs(skills: str):
    skills_list = skills.split(",")
    response = requests.get("https://remotive.io/api/remote-jobs")
    jobs = response.json().get("jobs", [])

    matched = []
    for job in jobs:
        for skill in skills_list:
            if skill.lower() in job["title"].lower():
                matched.append({
                    "title": job["title"],
                    "company_name": job["company_name"],
                    "url": job["url"]
                })
                break
    return matched
