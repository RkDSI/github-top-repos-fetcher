import requests
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to validate the operation parameter
def validate_operation(operation):
    valid_operations = ['mean', 'max', 'min']
    if operation not in valid_operations:
        raise ValueError(f"Invalid operation '{operation}'. Valid options are {valid_operations}.")

# Function to fetch and plot the top 20 most starred GitHub repositories
def fetch_and_plot_repos():
    try:
        # Set up the endpoint and parameters for the GitHub API request to search repositories
        search_url = 'https://api.github.com/search/repositories'
        search_params = {
            'q': 'stars:>1',  # Find repositories with stars greater than 1
            'sort': 'stars',  # Sort by number of stars
            'order': 'desc',  # Order by descending (most stars first)
            'per_page': 20    # Limit results to top 20
        }

        # Send a GET request to the GitHub API
        response = requests.get(search_url, params=search_params)

        # Validate the response
        if response.status_code != 200:
            logging.error("Failed to fetch data from GitHub API. Status Code: %s", response.status_code)
            return

        # Parse the JSON response into a Python dictionary
        search_results = response.json()

        # Initialize lists to hold repository names and star counts
        repo_names = []
        stars = []

        # Loop through each item in the search results
        for repo in search_results['items']:
            # Add the repo name and star count to the respective lists
            repo_names.append(repo['name'])
            stars.append(repo['stargazers_count'])

        logging.info("Successfully fetched data from GitHub API.")

        # Create a horizontal bar chart
        plt.figure(figsize=(12, 8))  # Set the figure size
        plt.barh(repo_names, stars, color='skyblue')  # Create horizontal bars
        plt.xlabel('Stars')  # Set the x-axis label
        plt.ylabel('Repository')  # Set the y-axis label
        plt.title('Top 20 Most Starred GitHub Repositories')  # Set the title
        plt.gca().invert_yaxis()  # Invert the y-axis to show the top repo at the top
        plt.show()  # Display the plot
        logging.info("Plot created successfully.")

    except requests.exceptions.RequestException as e:
        logging.error("A requests exception occurred: %s", e)
    except Exception as e:
        logging.error("An error occurred: %s", e)

# Call the function to fetch and plot the repositories
fetch_and_plot_repos()
