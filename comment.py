from pydantic import BaseModel, constr


class Comment(BaseModel):
    text: constr(max_length=512)
