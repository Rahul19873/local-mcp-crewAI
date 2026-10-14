import ollama

response=ollama.chat(
    model='qwen2.5:1.5b',
    message=[
        {"role":"user",
         "content":"explain AGENTIC AI in artificial intelligence"
         }
        
    ]
    
)

print("\nQWEN RESPONSE:\n")
print(response['message']['content'])

