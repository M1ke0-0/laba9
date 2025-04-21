from fastapi import FastAPI, Query
import wikipedia

app = FastAPI()

wikipedia.set_lang("ru")

@app.get("/page/{title}",summary = "Ручка один")
def root_first(title: str):
    page = wikipedia.page(title, auto_suggest=False)
    return {
        "title": page.title,
        "summary": page.summary,
        "url": page.url
    }

@app.get("/search", summary = "Ручка два")
def root_second(query: str = Query(..., min_length=2), limit: int = 5):
    results = wikipedia.search(query, results=limit)
    return {"results": results}

@app.post("/content", summary = "Ручка три")
def root_third(data: dict):
    page = wikipedia.page(data["query"], auto_suggest=False)
    return {
        "title": page.title,
        "content": page.content[:1000] + "..." if len(page.content) > 1000 else page.content,
        "url": page.url
    }

    