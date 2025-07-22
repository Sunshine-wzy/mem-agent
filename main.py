from . import memory


if __name__ == '__main__':
    messages = [
        {
            "role": "user",
            "content": "I like to drink coffee in the morning and go for a walk"
        }
    ]
    result = memory.add(messages, user_id="alice", metadata={"category": "preferences"})

    related_memories = memory.search("Should I drink coffee or tea?", user_id="alice")
    print(related_memories)
