import requests  # Import the requests module to make HTTP requests
import json  # Import the json module to handle JSON data

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
        # Extracting the URL from the thumbnail image
        image_url = data.get("thumbnail", {}).get("source")
        # Returning the summary text and the image URL
        return summary, image_url
    else:
        # Returning an error message if fetching information failed
        return "Failed to fetch information. Please try again later.", None

def save_image_from_url(image_url, filename):
    # Making a GET request to fetch the image data from the given URL
    response = requests.get(image_url)
    # Checking if the response status code is 200 (indicating success)
    if response.status_code == 200:
        # Opening the file in write-binary mode
        with open(filename, "wb") as f:
            # Writing the image data to the file
            f.write(response.content)
            # Printing a message indicating that the image has been saved
            print(f"Image saved successfully as {filename}")
    else:
        # Printing an error message if fetching the image failed 
        print("Failed to fetch image")

def main():
    # Printing a welcome message
    print("Welcome to Wikipedia Summaries")
    # Prompting the user to enter the topic they want to learn about 
    topic = input("Enter a topic you want to learn about: ")
    # Calling the get_wikipedia_summary function to fetch the summary and image URL
    summary, image_url = get_wikipedia_summary(topic)
    # Printing the summary text 
    print("Summary:")
    print(summary)
  
    # Checking if an image URL is available 
    if image_url:
        filename = f"{topic.replace(' ', '_')}.jpeg"  # Example filename
        # Calling the save_image_from_url function to save the image
        save_image_from_url(image_url, filename)
    else:
        # Printing a response if no image is available for the topic
        print("\nNo image available for this topic")

if __name__ == "__main__":
    main()
