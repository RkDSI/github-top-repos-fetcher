# analysis.py

import logging
import requests
import matplotlib.pyplot as plt
import yaml
from typing import Any, Optional

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Analysis:
    def __init__(self, analysis_config: str):
        """
        Load config into an Analysis object.
        
        Parameters
        ----------
        analysis_config : str
            Path to the analysis/job-specific configuration file
        """
        self.config = self._load_config(analysis_config)
        self.data = None

    def _load_config(self, analysis_config: str) -> dict:
        with open('system_config.yml', 'r') as file:
            system_config = yaml.safe_load(file)
        with open('user_config.yml', 'r') as file:
            user_config = yaml.safe_load(file)
        with open(analysis_config, 'r') as file:
            analysis_config = yaml.safe_load(file)

        return {**system_config, **user_config, **analysis_config}

    
     def load_data(self):
        """
        Retrieve data from the GitHub API.
        """
        try:
            # Set up the endpoint and parameters for the GitHub API request to search repositories
            search_url = 'https://api.github.com/search/repositories'
            search_params = {
                'q': 'stars:>1',  # Find repositories with stars greater than 1
                'sort': 'stars',  # Sort by number of stars
                'order': 'desc',  # Order by descending (most stars first)
                'per_page': 20    # Limit results to top 20
            }

            # Prepare headers for the GitHub API request to include the token
            headers = {
                'Authorization': f'token {self.config.get("github_api_token")}'
            }

            # Send a GET request to the GitHub API
            response = requests.get(search_url, headers=headers, params=search_params)

            # Validate the response
            if response.status_code != 200:
                logging.error("Failed to fetch data from GitHub API. Status Code: %s", response.status_code)
                self.data = []
                return

            # Parse the JSON response into a Python dictionary
            self.data = response.json()['items']

        except requests.exceptions.RequestException as e:
            logging.error("A requests exception occurred: %s", e)
            self.data = []
        except Exception as e:
            logging.error("An error occurred: %s", e)
            self.data = []

    def compute_analysis(self, n=20) -> list:
        """
        Analyze previously-loaded data.

        Parameters
        ----------
        n : int
            Number of top repositories to analyze

        Returns
        -------
        analysis_output : list
            List of dictionaries containing details of top repositories
        """
        assert self.data is not None, "Data has not been loaded."

        try:
            # Ensure data is sorted by stars and limit to top N
            top_repos = sorted(self.data, key=lambda x: x['stargazers_count'], reverse=True)[:n]

            # Extract and print details for each repo
            analysis_output = []
            for repo in top_repos:
                repo_details = {
                    'Name': repo['name'],
                    'Stars': repo['stargazers_count'],
                    'Owner': repo['owner']['login'],
                    'Created At': repo['created_at']
                }
                analysis_output.append(repo_details)
                print(f"Name: {repo_details['Name']}, Stars: {repo_details['Stars']}, Owner: {repo_details['Owner']}, Created At: {repo_details['Created At']}")

            return analysis_output

        except Exception as e:
            logging.error("An error occurred: %s", e)
            return []

    
    def plot_data(self, save_path: Optional[str] = None) -> plt.Figure:
        """
        Analyze and plot data.

        Parameters
        ----------
        save_path : str, optional
            Save path for the generated figure

        Returns
        -------
        fig : matplotlib.Figure
        """
        try:
            assert self.data is not None, "Data has not been loaded."

            # Initialize lists to hold repository names and star counts
            repo_names = [repo['name'] for repo in self.data]
            stars = [repo['stargazers_count'] for repo in self.data]

            # Create a horizontal bar chart
            fig, ax = plt.subplots(figsize=self.config.get('figure_size', (12, 8)))
            ax.barh(repo_names, stars, color=self.config.get('plot_color', 'skyblue'))
            ax.set_xlabel('Stars')
            ax.set_ylabel('Repository')
            ax.set_title(self.config.get('plot_title', 'Top 20 Most Starred GitHub Repositories'))
            ax.invert_yaxis()

            # Save plot if save_path is provided
            if save_path is None:
                save_path = self.config.get('default_save_path', 'plot.png')
            fig.savefig(save_path)

            # Display the plot
            plt.show()
            logging.info("Plot created successfully.")

            return fig

        except AssertionError as e:
            logging.error(e)
        except Exception as e:
            logging.error("An error occurred: %s", e)
            return None
