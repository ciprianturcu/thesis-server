from fastapi import APIRouter

from huggingface_model_inference import CodeSummarizer
from comment import Comment

summarizer = CodeSummarizer()

api_router = APIRouter()


@api_router.post("/getComment")
async def comment_code(code_snippet: Comment):
    return summarizer.summarize_code(code_snippet.text)
