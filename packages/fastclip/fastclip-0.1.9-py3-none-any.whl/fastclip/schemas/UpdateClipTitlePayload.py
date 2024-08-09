from pydantic import BaseModel


class UpdateClipTitlePayload(BaseModel):
    title: str

    def to_json(self):
        return {"title": self.title}
