from dotenv import load_dotenv
from mem0 import Memory
from openai import OpenAI

load_dotenv()

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