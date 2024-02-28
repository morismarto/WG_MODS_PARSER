__all__ = ['Mods']

from pydantic import BaseModel
from typing import List

class Version(BaseModel):
    version: str
    download_url: str

class Localization(BaseModel):
    title: str

class Mods(BaseModel):
    localizations: List[Localization]
    versions: List[Version]
    

