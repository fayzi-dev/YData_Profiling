
# YData_Profiling.ipynb


!pip install -U ydata-profiling

import pandas as pd
from ydata_profiling import ProfileReport


df = pd.read_csv("/content/drive/MyDrive/MY_Project/Churn_Modelling.csv")


print(df.head())

profile = ProfileReport(df, title = "Churn_Modelling Profile Report")
print(profile)



profile.to_file("report.html")
