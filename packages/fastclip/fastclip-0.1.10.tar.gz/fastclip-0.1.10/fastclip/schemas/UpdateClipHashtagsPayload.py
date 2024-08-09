from typing import List
from pydantic import BaseModel


class UpdateClipHashtagsPayload(BaseModel):
    hashtags: List[str]

    def to_json(self):
        return {"hashtags": self.hashtags}
