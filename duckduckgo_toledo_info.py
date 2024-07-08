import requests

def fetch_url(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None
    except ValueError as e:
        print(f"Error: La respuesta no es un JSON válido. {e}")
        return None
    
def fetch_duckduckgo_results(query):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json"
    }
    
    data = fetch_url(url, params)
    if data:
        if 'AbstractSource' in data and 'Wikipedia' in data['AbstractSource']:
            return data.get('RelatedTopics', [])
        else:
            print("No se encontró la fuente 'Wikipedia' en AbstractSource.")
    return []

def print_topic_details(topics):
    for topic in topics:
        if 'FirstURL' in topic and 'Text' in topic:
            print(f"FirstURL: {topic['FirstURL']}")
            print(f"Text: {topic['Text']}")
            print()

def main():
    query = "Toledo"
    topics = fetch_duckduckgo_results(query)
    print_topic_details(topics)

if __name__ == "__main__":
    main()