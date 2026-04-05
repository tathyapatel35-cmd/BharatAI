import requests
import json

def get_random_joke():
    """
    Fetches a random joke from the JokeAPI.
    
    Returns:
        dict: A dictionary containing the joke data or error message.
    """
    api_url = "https://v2.jokeapi.dev/joke/Any"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        joke_data = response.json()
        
        if joke_data.get('type') == 'twopart':
            joke = f"Setup: {joke_data.get('setup')}\nPunchline: {joke_data.get('delivery')}"
        else:
            joke = joke_data.get('joke', 'No joke found')
        
        return {
            'success': True,
            'joke': joke,
            'category': joke_data.get('category', 'General')
        }
    
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f"Failed to fetch joke: {str(e)}"
        }

def main():
    """Main function to run the joke generator."""
    print("=" * 50)
    print("🤣 Welcome to the Random Joke Generator! 🤣")
    print("=" * 50)
    
    while True:
        user_input = input("\nPress Enter to get a joke or type 'quit' to exit: ").strip().lower()
        
        if user_input == 'quit':
            print("\nThanks for laughing with us! Goodbye! 👋")
            break
        
        elif user_input == '':
            result = get_random_joke()
            
            if result['success']:
                print(f"\n📂 Category: {result['category']}")
                print(f"\n😄 Joke:\n{result['joke']}")
            else:
                print(f"\n❌ {result['error']}")
        
        else:
            print("Invalid input. Please press Enter to get a joke or type 'quit' to exit.")

if __name__ == "__main__":
    main()