
# Repo Analyst

## Overview
Repo Analyst is a Python package designed to analyze GitHub repositories. It leverages the GitHub API to fetch data, performs statistical analysis, and visualizes insights about repository popularity and activity.

## Features
- **Data Fetching**: Retrieve repository data using the GitHub API.
- **Statistical Analysis**: Analyze data to identify trends and patterns.
- **Customizable Visualizations**: Generate plots and graphs to visualize data.
- **Configurable Settings**: Tailor analysis through YAML configuration files.

## Installation
Ensure Python is installed on your system. You can install Repo Analyst using pip:

```bash
pip install repo-analyst
```

## Configuration
The package uses three YAML files for configuration:
- `system_config.yml`: Contains global settings.
- `user_config.yml`: For user-specific settings.
- `analysis_config.yml`: For analysis/job-specific settings.

Make sure to provide a valid GitHub API token in the configuration.

## Usage
To use Repo Analyst, follow these steps:

```python
from repo_analyst.analysis import Analysis

# Initialize Analysis with your configuration file
analysis = Analysis('path_to_job_analysis_config.yml')

# Fetch data from GitHub
analysis.load_data()

# Perform analysis
analysis.compute_analysis()

# Generate and view a plot
analysis.plot_data()
```

## Testing
To run the tests included with Repo Analyst:

```bash
python -m unittest discover -s tests
```

## Contributing
Contributions to Repo Analyst are welcomed. Please read `CONDUCT.md` for guidelines on contributions.

## License
This project is licensed under Free For All License.

## Contact
For support or queries, contact Reza Kopaee at [rkopaee@gmail.com].
