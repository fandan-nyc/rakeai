from model import DataStructure
from pydantic import BaseModel
import json


def generate_report(data: str):
    data: DataStructure = DataStructure.model_validate(obj=data)
    if data.type == "Individual":
        from individual import generate_individual
        generate_individual(data)
    else:
        ...


if __name__ == "__main__":
    with open("./data.json", "r") as f:
        data = json.loads(f.read())
    generate_report(data)
