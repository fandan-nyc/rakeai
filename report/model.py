from pydantic import  BaseModel
from typing import Dict, List
from enum import Enum

class AnalyzeMetaData(BaseModel):
    name: str
    structure: str
    probability: str

class DataStructure(BaseModel):
    title: str
    type: str
    base_information: Dict[str, str]
    data: List[AnalyzeMetaData]
