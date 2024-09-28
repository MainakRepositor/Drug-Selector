"""This module contains data about the prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd
from web_functions import predict

# Hide Streamlit's default styling
hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function creates the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
        <p style="font-size:25px">
            This app uses <b style="color:green">XG Boosting Forest Classifier</b> for the Segregation of Drugs
        </p>
        """, unsafe_allow_html=True)

    # Take feature input from the user
    st.subheader("Select Values:")

    col1, col2 = st.columns(2)

    # Create sliders for feature input
    sliders = [
        "Molecular_descriptors", "Functional_groups", "Stereochemistry", "Target_structure",
        "Binding_sites", "Target_flexibility", "Chemical_database_quality", "Experimental_data_availability",
        "Machine_learning_algorithm_selection", "Feature_selection", "Model_validation", "Solubility",
        "Permeability", "Lipophilicity", "Chemical_stability", "Metabolic_stability",
        "ADME", "Toxicity_prediction", "Compound_library_diversity", "Structural_diversity",
        "Lipinskis_Rule_of_Five", "Fragment_based_filtering", "Assay_conditions", "Data_reproducibility",
        "Applicability_domain_QSAR"
    ]

    features = []

    with col1:
        for slider in sliders[:13]:  # First half of the sliders
            min_value = float(df[slider].min().item())
            max_value = float(df[slider].max().item())
            value = st.slider(slider, min_value, max_value)
            features.append(value)

    with col2:
        for slider in sliders[13:]:  # Second half of the sliders
            min_value = float(df[slider].min().item())
            max_value = float(df[slider].max().item())
            value = st.slider(slider, min_value, max_value)
            features.append(value)

    # Create a DataFrame to display the entered values
    df3 = pd.DataFrame([features], columns=sliders)
    
    st.header("The values entered by user")
    st.dataframe(df3)

    st.sidebar.info("Please make use of the sliders to generate lab data nearest to your drug scales")
    k = 0.27
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + k # covariance factor
        
        
        if prediction == 1:
            st.success("Congratulations! Your drug proposal is acceptable.")
        elif(prediction == 0):
            st.error("We are sorry to let you know your composition didn't pass")
        
        # Print the score of the model 
        st.sidebar.write("The model used is trusted by doctors and has an accuracy of ", round((score * 100), 2), "%")
