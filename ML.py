maimport marimo

__generated_with = "0.10.2"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(
        r"""
        # Data Preprocessing - Before Building Machine learning model #
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ![1.jpg](attachment:1.jpg)
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import csv
    return csv, np, pd, plt, sns


@app.cell
def _(mo):
    mo.md(
        r"""
        # step 1: import necessary libraries #
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # step 2: Read Data set #
        """
    )
    return


@app.cell
def _(pd):
    df=pd.read_csv("Life Expectancy Data.csv")
    #df=pd.read_csv("D:\CEN\ML_Anandkumar 2024-2025_S4\Jupiter note books\archive\Life Expectancy Data.csv")
    return (df,)


@app.cell
def _(df):
    #to disp head
    df.head()
    return


@app.cell
def _(df):
    #to disp bottom 
    df.tail()
    return


@app.cell
def _(pwd):
    pwd
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # step 3: Sanity check of data #
        """
    )
    return


@app.cell
def _():
    # to check outlier , row , column info and so on
    return


@app.cell
def _(df):
    # to find row and column info
    df.shape
    return


@app.cell
def _(df):
    #we can understand over all information , data types etc.,
    df.info()
    return


@app.cell
def _(df):
    #to find missing values
    df.isnull().sum()
    return


@app.cell
def _(df):
    #percentage of missing to take action
    df.isnull().sum()/df.shape[0]*100
    return


@app.cell
def _(df):
    # finding duplicates
    df.duplicated().sum()
    return


@app.cell
def _(df):
    for _i in df.select_dtypes(include='object').columns:
        print(df[_i].value_counts())
        print('****' * 5)
    return


@app.cell
def _(df):
    #to get the descriptive statistics
    df.describe().T
    return


@app.cell
def _(df):
    #to get descriptive info object column
    df.describe(include="object")
    return


@app.cell
def _(df, plt, sns):
    for _i in df.select_dtypes(include='number').columns:
        sns.histplot(data=df, x=_i)
        plt.show()
    return


@app.cell
def _(df, plt, sns):
    for _i in df.select_dtypes(include='number').columns:
        sns.boxplot(data=df, x=_i)
        plt.show()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Step :4 scatter plot to understand the relationship this is to be filled #  

        """
    )
    return


@app.cell
def _(df):
    df.select_dtypes(include="number").columns
    return


@app.cell
def _(df, plt, sns):
    for _i in ['Year', 'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B', 'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure', 'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population', ' thinness  1-19 years', ' thinness 5-9 years', 'Income composition of resources', 'Schooling']:
        sns.scatterplot(data=df, x=_i, y='Life expectancy ')
        plt.show()
    return


@app.cell
def _(df):
    #to find the correlation 
    df.select_dtypes(include="number").corr()
    return


@app.cell
def _(df):
    s=df.select_dtypes(include="number").corr()
    return (s,)


@app.cell
def _(s, sns):
    #to get the heat with value . simply s will not give values 
    sns.heatmap(s)
    return


@app.cell
def _(plt, s, sns):
    plt.figure(figsize=(15,15)) 
    sns.heatmap(s,annot=True)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Step :5 Missing value treatments #
        """
    )
    return


@app.cell
def _(df):
    #choose the method for imputng the values using mean, median , mode also KNNimputer
    df.isnull().sum() #once again taking it to treat missing values
    return


@app.cell
def _(df):
    for _i in [' BMI ', 'Polio', 'Income composition of resources']:
        df[_i].median()
    return


@app.cell
def _(df):
    df.isnull().sum()
    return


@app.cell
def _():
    from sklearn.impute import KNNImputer
    impute=KNNImputer()
    return KNNImputer, impute


@app.cell
def _(df):
    df.isnull().sum()
    return


@app.cell
def _(df, i, impute):
    for _i in df.select_dtypes(include='number').columns:
        df[i] = impute.fit_transform(df[[i]])
        df.isnull().sum
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Step :6 Outliers Treatments #
        """
    )
    return


@app.cell
def _(np):
    def wisker(col):
        q1,q3=np.percentile(col,[25,75])
        iqr=q3-q1
        lw=q1-1.5*iqr
        uw=q3+1.5*iqr
        return lw,uw
    return (wisker,)


@app.cell
def _(df, wisker):
    wisker (df['GDP'])
    return


@app.cell
def _(df):
    df.select_dtypes(include="number").columns
    return


@app.cell
def _(df, i, np, wisker):
    for _i in ['GDP', 'Total expenditure', ' thinness  1-19 years', ' thinness 5-9 years']:
        lw, uw = wisker(df[i])
        df[i] = np.where(df[i] < lw, lw, df[i])
        df[i] = np.where(df[i] > uw, uw, df[i])
    return lw, uw


@app.cell
def _(df, plt, sns):
    for _i in ['GDP', 'Total expenditure', ' thinness  1-19 years', ' thinness 5-9 years']:
        sns.boxplot(df[_i])
        plt.show()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Step7  Duplicates and garbage value treatments #
        """
    )
    return


@app.cell
def _(df):
    df.drop_duplicates()
    # similerly we can do for garbage also
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # Step 8 : Encoding of data #
        """
    )
    return


@app.cell
def _(df, pd):
    d=pd.get_dummies(data=df,columns=["Country","Status"],drop_first=True)
    #after this the data has only numerical
    return (d,)


@app.cell
def _():
    #pip install pandas-profiling
    #from pandas_profiling import ProfileReport
    #profile = ProfileReport(df)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ![2.jpg](attachment:0674c6ad-443e-4720-bcd7-4a358ff25ada.jpg)
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

