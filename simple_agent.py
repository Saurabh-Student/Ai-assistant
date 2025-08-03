from dotenv import load_dotenv
from jarvis_search import google_search
from jarvis_prompt import _Behavoiur_prompts, Reply_prompts

load_dotenv()

def main():
    print("Jarvis Assistant - Simple Version")
    print("=================================")
    print("Type 'quit' to exit")
    print()
    
    while True:
        query = input("Enter your search query: ").strip()
        
        if query.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not query:
            print("Please enter a valid query.")
            continue
            
        print("Searching...")
        result = google_search(query)
        print(result)
        print()

if __name__ == "__main__":
    main()
