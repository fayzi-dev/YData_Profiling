# YData_Profiling
Data quality profiling and exploratory data analysis are crucial steps in the process of Data Science and Machine Learning development. YData-profiling is a leading tool in the data understanding step of the data science workflow as a pioneering Python package.
(https://docs.profiling.ydata.ai/latest/)

YData Profiling (formerly known as Pandas Profiling) is a Python library that generates profile reports from a pandas DataFrame. It provides a quick and comprehensive overview of the dataset, which is useful for data exploration and analysis.

### Key Features
- **Data Types**: Automatically identifies the data types of each column.
- **Statistics**: Provides descriptive statistics (mean, median, mode, etc.) for numerical and categorical columns.
- **Missing Values**: Highlights missing values and their percentage.
- **Distribution**: Visualizes the distribution of numerical features through histograms.
- **Correlation**: Displays correlation matrices for numerical features.
- **Sample Data**: Shows a sample of the dataset for a quick glance.

### Installation
You can install YData Profiling using pip:

```bash
pip install ydata-profiling
```

### Basic Usage
Here’s a simple example of how to use YData Profiling:

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Load your data into a pandas DataFrame
data = pd.read_csv('your_data.csv')

# Create a profile report
profile = ProfileReport(data, title='Pandas Profiling Report', explorative=True)

# Save the report to an HTML file
profile.to_file("report.html")
```

### Customization
You can customize the report generation using various parameters, such as:
- **`explorative`**: Set to `True` to enable advanced explorations like correlation and interactions.
- **`samples`**: To show a subset of the data.
- **`minimal`**: For a quick and less detailed report.

### Viewing the Report
After running the code, you can open `report.html` in a web browser to view the profiling report.

### Conclusion
YData Profiling is an excellent tool for quickly understanding your dataset, identifying potential issues, and making informed decisions about data preprocessing and modeling. If you need more specific examples or features, let me know!