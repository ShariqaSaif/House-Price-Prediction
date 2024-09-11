import streamlit as st
import pandas as pd
import pickle as pk

# Load the model and data
model = pk.load(open(r'C:\Users\Shaik Shariqa Saif\Documents\219X1A3229\House Price Prediction\House_prediction_model.pkl', 'rb'))
data = pd.read_csv(r'C:\Users\Shaik Shariqa Saif\Documents\219X1A3229\House Price Prediction\Cleaned_Data.csv')

# Inject custom CSS for full background image, fixed position, and improved styling
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://img.staticmb.com/mbcontent/images/crop/uploads/2022/12/Most-Beautiful-House-in-the-World_0_1200.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    padding: 0;
    margin: 0;
    overflow: hidden;
}

h1 {
    color: white; 
    text-shadow: 2px 2px 4px #000000;
    padding-top: 20px;
    margin: 0;
    text-align: center;
    font-size: 48px; /* Increased font size for the heading */
    font-family: 'Arial', sans-serif;
}

.stButton button {
    background-color: #4CAF50;
    color: white;
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    font-size: 30px; /* Adjusted font size */
    margin-top: 20px;
}

.stSelectbox label, .stNumberInput label {
    color: #FFFFFF; 
    font-size: 26px; /* Improved font size */
    font-weight: bold;
    text-shadow: 1px 1px 2px #000000;
}

.stNumberInput input {
    border: 2px solid #4CAF50;
    border-radius: 5px;
    font-size: 18px; /* Improved font size */
}

.container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.4);
    max-width: 500px;
    margin: 0 auto; /* Center container */
    position: relative; /* Center container */
    top: 20%;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# App Header
st.markdown('<h1>🏠 Innovative House Price Prediction </h1>', unsafe_allow_html=True)


# Inputs for the prediction
loc = st.selectbox('📍 Choose the location', data['location'].unique())
sqft = st.number_input("🏠 Enter total Sqft", min_value=1)
beds = st.number_input("🛏️ Enter No of Bedrooms", min_value=1)
bath = st.number_input("🛁 Enter No of Bathrooms", min_value=1)
balcony = st.number_input("🌳 Enter No of Balconies", min_value=0)

# Predict button
if st.button("Predict Price 💵"):
    input_data = pd.DataFrame([[loc, sqft, bath, balcony, beds]], 
                              columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])
    output = model.predict(input_data)
    
    # Display prediction
    st.success('🏷️ **Price of the House**: ₹{:.2f}'.format(output[0]))

st.markdown('</div>', unsafe_allow_html=True)
