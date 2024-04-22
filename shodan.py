import shodan

def perform_search(query, filename, start, api_key):
    SHODAN_API_KEY = api_key
    api = shodan.Shodan(SHODAN_API_KEY)
    
    try:
        results = api.search(query, page=start // 1000 + 1)
        with open(filename, "a") as f:
            for result in results['matches']:
                ip = result['ip_str']
                port = result['port']
                hostname = result['hostnames'][0] if result['hostnames'] else ''
                os_info = result['os']
                f.write(f"{ip},{port},{hostname},{os_info}\n")
        print(f"Query {start // 1000 + 1} completed.")
    except Exception as e:
        print("Error:", e)

def main():
    query = "PUT YOUR QUERY HERE EX : port:587"
    total_results = 10000000
    chunk_size = 1000
    num_queries = total_results // chunk_size
    
    filename = "results.txt"
    
    api_keys = [
        "mjflOguXHtnUUIiK9mTWewPJw0N3ItZl",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
        # Add more API keys here
    ]
    
    key_index = 0
    
    for i in range(num_queries):
        start_index = i * chunk_size
        perform_search(query, filename, start_index, api_keys[key_index])
        key_index = (key_index + 1) % len(api_keys)
    
    print(f"All queries completed. Results saved to {filename}")

if __name__ == "__main__":
    main()
