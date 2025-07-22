from openai import OpenAI
from mem0 import Memory


config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "mem_agent",
            "url": "http://43.143.119.223:6333"
        }
    }
}

openai_client = OpenAI()
memory = Memory.from_config(config)