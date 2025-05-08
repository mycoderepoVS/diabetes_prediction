import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 
import os


@st.cache_data
def load_data(data):
	df = pd.read_csv(data)
	return df


def run_eda_app():
	st.subheader("Exploratory Data Analysis Section")

	df = load_data("data/diabetes_data_upload.csv")		# relative path
	df_clean = load_data("data/diabetes_data_clean.csv")
	freq_df = load_data("data/frequency_distribution_age.csv")

	submenu = st.sidebar.selectbox("SubMenu",["Descriptive Statistics","Plots"])
	if submenu == "Descriptive Statistics":
		st.subheader("Descriptive Statistics")
		st.dataframe(df)

		with st.expander("Data Types Summary"):
			st.dataframe(df.dtypes)

		with st.expander("Descriptive Summary"):
			st.dataframe(df_clean.describe())

		with st.expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())

		with st.expander("Class Distribution"):
			st.dataframe(df['class'].value_counts())
	else:
		st.subheader("Plots")

		# Layouts
		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Distribution Plot of Gender"):
				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Gender Type','Counts']
				# st.dataframe(gen_df)
				p01 = px.pie(gen_df,names='Gender Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

			with st.expander("Distribution Plot of Class"):
				fig = plt.figure()
				sns.countplot(df['class'])
				st.pyplot(fig)

		with col2:
			with st.expander("Gender Distribution"):
				st.dataframe(df['Gender'].value_counts())

			with st.expander("Class Distribution"):
				st.dataframe(df['class'].value_counts())
			

		with st.expander("Frequency Distribution Plot of Age"):
			plot = px.bar(freq_df,x='age',y='count')
			st.plotly_chart(plot)

		with st.expander("Outlier Detection Plot"):
			p3 = px.box(df,x='Age',color='Gender')
			st.plotly_chart(p3)

		with st.expander("Correlation Plot"):
			corr_matrix = df_clean.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)