# Load packages
import pandas as pd

# Load review data
F23url = 'https://raw.githubusercontent.com/matthew-zahn/as.180.369/main/history/input/F23CourseReviews.csv'
#F23url = 'https://raw.githubusercontent.com/llorracc/as.180.369/main/history/input/F23CourseReviews.csv'
F23df = pd.read_csv(F23url,sep=";")
print(F23df.head())

# Export as a pickle
#F23url = 'https://raw.githubusercontent.com/llorracc/as.180.369/main/history/output/F23CourseReviews.pkl'
outpath = 'F23CourseReviews.pkl'
F23df.to_pickle(outpath)

# Load example
#df = pd.read_pickle(outpath)
# EOF

# exclude rows with NaN
df_NaN=F23df_noNaN=F23dfd.dropna()
df=F23df_noNaN
# exclude courses taught by writing department 
rit = df['Dept'].str.contains('rit',regex=True,na=False)
norit = df_big[~rit]

# exclude courses taught by language departments
lang = norit['Dept'].str.contains('angua',regex=True,na=False)
nolang =norit[~lang]

#exclude the English department
english=nolang['Dept'].str.contains('nglis',regex=True)
noenglish=nolang[~english]

# Calc stats
meanvals = noenglish[['Dept','Title','OverallMean','QualityMean','FeedbackRate','ClassSize']]
meanvals.sort_values(by='OverallMean',ascending=False)
meanvals['Count'] = list(range(1, len(noeng)+1))
meanvals

