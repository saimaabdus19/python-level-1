import requests  # Import the requests module to make HTTP requests
import json  # Import the json module to handle JSON data
from datetime import datetime  # Import datetime to handle date and time

def get_wikipedia_summary(topic):
    # Constructing the URL to fetch Wikipedia summary based on the given topic
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    # Making a GET request to fetch data from the URL
    response = requests.get(url)
    # Checking if the response status code is 200 (indicating success)
    if response.status_code == 200:
        data = response.json()
        # Extracting the JSON data from the response
        summary = data.get("extract", "No summary available.")
        return summary
    else:
        # Returning an error message if fetching information failed
        return None

def save_summary_to_file(topic, summary):
    # Formatting the filename with the topic and current date
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{topic.replace(' ', '_')}-summary-{date_str}.txt"
    try:
        # Opening the file in write mode
        with open(filename, "w") as file:
            # Writing the topic, date, and summary to the file
            file.write(f"Topic: {topic}\n")
            file.write(f"Date: {date_str}\n\n")
            file.write(summary)
        # Printing a message indicating that the summary has been saved
        print(f"Summary retrieved and saved successfully. Check the '{filename}' file.")
    except Exception as e:
        # Printing an error message if saving the summary failed
        print(f"Failed to save summary to file: {e}")

def main():
    # Printing a welcome message
    print("Welcome to the Wikipedia Summary Fetcher!")
    # Prompting the user to enter the topic they want to learn about 
    topic = input("Please enter a topic you are interested in learning more about: ")
    # Calling the get_wikipedia_summary function to fetch the summary
    summary = get_wikipedia_summary(topic)
    if summary:
        # Printing the summary text 
        print("Summary:")
        print(summary)
        # Calling the save_summary_to_file function to save the summary
        save_summary_to_file(topic, summary)
    else:
        # Printing an error message if fetching the summary failed
        print("Failed to fetch information. Please try again later.")

if __name__ == "__main__":
    main()


