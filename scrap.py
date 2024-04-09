import requests
import pandas as pd
import time

# List of LinkedIn URLs
linkedin_urls = [
"http://www.linkedin.com/in/krishnakumar2409"

]

# List to store results
results = []

# API endpoint
api_endpoint = "https://api.apollo.io/v1/people/match"

# Headers
headers = {
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json'
}

# Chunk size to control the buffer
chunk_size = 1 # Adjust as needed

# Delay between chunks (in seconds)
delay_between_chunks = 1

# Iterate over LinkedIn URLs in chunks
for i in range(0, len(linkedin_urls), chunk_size):
    chunk_urls = linkedin_urls[i:i+chunk_size]

    # Iterate over chunked LinkedIn URLs
    for url in chunk_urls:
        try:
            # Data for the request
            data = {
                "api_key": "PCwz88MOSkup1bfSUqyW_Q",
                "linkedin_url": url
            }

            # Making the HTTP POST request
            response = requests.post(api_endpoint, headers=headers, json=data)

            # Checking if the request was successful
            if response.status_code == 200:
                # Extracting JSON data from the response
                json_data = response.json()
                
                results.append(json_data)
            else:
                # Print error message
                print(f"Error fetching data for URL: {url}. Status Code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching data for URL: {url}. Error: {str(e)}")

    # Introduce a delay between chunks to avoid overwhelming the server
    time.sleep(delay_between_chunks)

# Converting the list of results to a DataFrame
df = pd.DataFrame(results)

# Extracting emails, LinkedIn URLs, names, and titles from the results
emails = [item['person']['email'] if 'email' in item['person'] else 'N/A' for item in results]
linkedin_urls = [item['person']['linkedin_url'] if 'linkedin_url' in item['person'] else 'N/A' for item in results]
names = [item['person']['name'] if 'name' in item['person'] else 'N/A' for item in results]
titles = [item['person']['title'] if 'title' in item['person'] else 'N/A' for item in results]

# Adding emails, LinkedIn URLs, names, and titles to the DataFrame
df['Name'] = names
df['Title'] = titles
df['Email'] = emails
df['Linkedin_url'] = linkedin_urls


# Writing DataFrame to a CSV file with index included
csv_file = str(input("Enter your file name "))
df.to_csv(csv_file, index=True)
print(f"Data successfully saved to {csv_file}")





