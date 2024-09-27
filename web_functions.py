"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('compound_screening_dataset.csv')

    # Perform feature and target split
    X = df[["Molecular_descriptors", "Functional_groups", "Stereochemistry", "Target_structure", "Binding_sites", "Target_flexibility", "Chemical_database_quality", "Experimental_data_availability", "Machine_learning_algorithm_selection", "Feature_selection", "Model_validation", "Solubility", "Permeability", "Lipophilicity", "Chemical_stability", "Metabolic_stability", "ADME", "Toxicity_prediction", "Compound_library_diversity", "Structural_diversity", "Lipinskis_Rule_of_Five", "Fragment_based_filtering", "Assay_conditions", "Data_reproducibility", "Applicability_domain_QSAR"]]
    y = df['Drug_accept_or_reject']

    return df, X, y

@st.cache_data()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1, 
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )
    # Fit the data on model
    model.fit(X, y)
    # Get the model score
    score = model.score(X, y)

    # Return the values
    return model, score

def predict(X, y, features):
    # Get model and model score
    model, score = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score