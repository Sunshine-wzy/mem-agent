from dotenv import load_dotenv
from mem0 import Memory
from openai import OpenAI

load_dotenv()

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "deepseek-v3",
            "temperature": 0.2,
            "max_tokens": 2000
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "qwen3-embedding-4b",
            "embedding_dims": 2560
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "mem_agent",
            "url": "http://43.143.119.223:6333",
            "embedding_model_dims": 2560
        }
    }
}

openai_client = OpenAI()
memory = Memory.from_config(config)