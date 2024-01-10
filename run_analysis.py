# Import the Analysis class from the repo_analyst package
from  repo_analyst import analysis

# Initialize the Analysis object with a configuration file
# Replace 'path_to_config.yml' with the actual path to your configuration file
config_file = 'analysis_config.yml'
my_analysis = analysis.Analysis(config_file)

# Load data using the load_data method
my_analysis.load_data()

# Perform the analysis using the compute_analysis method
# You can specify the number of top repositories to analyze (e.g., top 20)
top_n = 20
analysis_results = my_analysis.compute_analysis(top_n)

# Optionally, you can print or process the analysis_results here

# Plot the data using the plot_data method
# If you want to save the plot, specify the save path
save_path = 'output_plot.png'  # Optional: Specify a path to save the plot
my_analysis.plot_data(save_path)



