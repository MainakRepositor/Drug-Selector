"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Drug Selection System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            DISCOVERING AND ACCEPTING DRUGS<br>
            <hr>
            The process of compound screening and prediction, especially in drug discovery, is influenced by various factors. Below are some key factors that affect this process, particularly when predicting the biological activity of drug compounds and using models like QSAR (Quantitative Structure-Activity Relationship):

### 1. **Chemical Structure of Compounds**
   - **Molecular Descriptors**: These are numerical values representing the chemical structure, including atom types, bonds, molecular weight, hydrophobicity (logP), etc. They help in determining the relationship between structure and activity.
   - **Functional Groups**: Specific functional groups in a compound can greatly affect its reactivity and interaction with biological targets.
   - **Stereochemistry**: The 3D arrangement of atoms in the molecule, which can affect the binding to specific biological targets.

### 2. **Biological Target Properties**
   - **Target Structure**: The three-dimensional structure of the protein, enzyme, or receptor that the compound interacts with. Even small changes in the structure of the target can affect how well a compound binds.
   - **Binding Sites**: Identifying the correct binding pocket on a biological target is crucial for understanding how a compound may interact with it. Variations in the binding site can influence screening results.
   - **Target Flexibility**: Some proteins or enzymes are flexible, which can change their structure in response to different compounds, affecting binding and activity.

### 3. **Data Quality and Availability**
   - **Chemical Databases**: High-quality chemical and biological data from databases (e.g., PubChem, ChEMBL) are essential for building reliable predictive models. Errors or inconsistencies in these databases can lead to inaccurate predictions.
   - **Experimental Data**: The availability and quality of biological activity data from experiments (e.g., IC50, EC50 values) are critical for training prediction models like QSAR.

### 4. **Algorithm Selection and Model Development**
   - **Machine Learning Techniques**: The selection of machine learning algorithms (e.g., decision trees, support vector machines, deep learning) used to build predictive models influences accuracy and reliability.
   - **Feature Selection**: Identifying the most relevant molecular descriptors or features is essential for improving the predictive power of QSAR models.
   - **Validation**: Cross-validation and external validation of the models are necessary to ensure that the predictions are reliable and can generalize to new compounds.

### 5. **Physicochemical Properties**
   - **Solubility and Permeability**: These factors determine whether the compound can be absorbed and transported to the target site in a biological system.
   - **Lipophilicity**: The ability of a compound to dissolve in fats, oils, and lipids influences its interaction with the biological membrane and its bioavailability.
   - **Stability**: Both chemical and metabolic stability of a compound determine whether it can maintain its structure long enough to reach and interact with the target.

### 6. **Pharmacokinetics and Pharmacodynamics**
   - **Absorption, Distribution, Metabolism, Excretion (ADME)**: These factors influence how the compound behaves in a biological system and whether it can reach the desired target site at an effective concentration.
   - **Toxicity**: Even if a compound is biologically active, it might be too toxic to be a drug candidate. Predicting potential toxicity is essential to avoid harmful effects in humans.

### 7. **Compound Diversity and Libraries**
   - **Compound Libraries**: Screening libraries with diverse chemical scaffolds can lead to the identification of novel drug-like compounds.
   - **Structural Diversity**: Greater structural diversity in compound libraries improves the chances of finding active compounds, as it increases coverage of the chemical space.

### 8. **Drug-Likeness and Filtering**
   - **Rule of Five (Lipinski’s Rules)**: Drug-likeness rules, such as Lipinski’s Rule of Five, help filter out compounds with poor drug-like properties (e.g., too large or too hydrophobic).
   - **Fragment-based Filtering**: Screening small fragments that can bind to the target and later be optimized for higher affinity.

### 9. **Environmental and Experimental Conditions**
   - **Assay Conditions**: Variations in experimental conditions, such as pH, temperature, or solvent, can affect the screening results and biological activity of compounds.
   - **Reproducibility**: The ability to reproduce the biological activity of compounds across different experimental setups and conditions is essential for verifying predictions.

### 10. **QSAR Model Factors**
   - **Training Data Size**: Larger datasets with accurate biological activity measurements improve the robustness of QSAR models.
   - **Descriptor Selection**: Proper selection of molecular descriptors is vital for creating a model that accurately reflects the structure-activity relationship.
   - **Applicability Domain**: QSAR models are only valid within the chemical space of compounds used for training. Predictions outside this space can be unreliable.


        </p>
    """, unsafe_allow_html=True)
