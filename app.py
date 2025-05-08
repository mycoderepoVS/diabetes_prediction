import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app
from ml_app import run_ml_app
import os

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Diabetes Risk Prediction Machine Learning App Using Streamlit</h1>
		</div>
		"""

def main():

	# Retrieve the path in which the file is saved and move to that directory
	script_dir = os.path.dirname(os.path.abspath(__file__))
	os.chdir(script_dir)
	
	stc.html(html_temp)

	menu = ["Home","Exploratory Data Analysis","Machine Learning"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("""
			### Diabetes Risk Prediction App
			The dataset contains the signs and symptoms of newly diabetic or would be diabetic patient.
			#### Datasource
				https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset
			#### App Content
				EDA Section: Exploratory Data Analysis of Data
				ML Section: Machine Learning Prediction App

			""")

	elif choice == "Exploratory Data Analysis":
		run_eda_app()
	elif choice == "Machine Learning":
		run_ml_app()

if __name__ == '__main__':
	main()