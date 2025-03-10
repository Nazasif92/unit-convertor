import streamlit as st # streamlit library for building web apps

st.markdown(
    """
    <style>
    .stApp {
        background-color: lightpink;
    }

    .stTextInput, stNumberInput, stsSelectbox {
        color: red !important;
        background-color: lightblue;
        border: 5px; solid orange;
        border-radius: 10px;
        padding: 10px;
    
    .stButton {
        border-radius: 10px;
        padding: 10px;
        background-color: red;
        width: 120px;
        color: red;
    }
    .result-text {
        color: blue;
        font-size: 32px;
        font-weight: bold;
    }
    .sttitle {
    color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def convert_unit(value, unit_from, unit_to):    

    conversions = {
        "length": {
            "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
            "kilometer_meter": 1000, # 1 kilometer = 1000 meters
            "meter_centimeter": 100, # 1 meter = 100 centimeters
            "centimeter_meter": 0.01, # 1 centimeter = 0.01 meters
            "meter_millimeter": 1000, # 1 meter = 1000 millimeters
            "millimeter_meter": 0.001, # 1 millimeter = 0.001 meters
            "kilometer_mile": 0.621371, # 1 kilometer = 0.621371 miles
            "mile_kilometer": 1.60934, # 1 mile = 1.60934 kilometers
        },
        "weight": {
            "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
            "kilogram_gram": 1000, # 1 kilogram = 1000 gram
            "gram_milligram": 1000, # 1 gram = 1000 milligrams
            "milligram_gram": 0.001, # 1 milligram = 0.001 gram
            "kilogram_milligram": 1e+6, # 1 kilogram = 1e+6 milligrams
            "milligram_kilogram": 1e-6, # 1 milligram = 1e-6 kilograms
        },
        "time": {
            "second_minute": 1/60, # 1 second = 1/60 minute
            "minute_second": 60, # 1 minute = 60 seconds
            "minute_hour": 1/60, # 1 minute = 1/60 hour
            "hour_minute": 60, # 1 hour = 60 minutes
            "second_hour": 1/3600, # 1 second = 1/3600 hour
            "hour_second": 3600, # 1 hour = 3600 seconds

        },
        "temperature": {
            "celsius_fahrenheit": lambda x: (x * 9/5) + 32, # Celsius to Fahrenheit
            "fahrenheit_celsius": lambda x: (x - 32) * 5/9, # Fahrenheit to Celsius
            "celsius_kelvin": lambda x: x + 273.15, # Celsius to Kelvin
            "kelvin_celsius": lambda x: x - 273.15, # Kelvin to Celsius
            "fahrenheit_kelvin": lambda x: (x + 459.67) * 5/9, # Fahrenheit to Kelvin
            "kelvin_fahrenheit": lambda x: (x * 9/5) - 459.67, # Kelvin to Fahrenheit
        },
        "volume": {
            "liter_milliliter": 1000, # 1 liter = 1000 milliliters
            "milliliter_liter": 0.001, # 1 milliliter = 0.001 liter
            "liter_gallon": 0.264172, # 1 liter = 0.264172 gallons
            "gallon_liter": 3.78541, # 1 gallon = 3.78541 liters
        },
        "area": {
            "sq_meter_sq_kilometer": 1e-6, # 1 sq meter = 1e-6 sq kilometer
            "sq_kilometer_sq_meter": 1e6, # 1 sq kilometer = 1e6 sq meters
            "sq_meter_sq_mile": 3.861e-7, # 1 sq meter = 3.861e-7 sq mile
            "sq_mile_sq_meter": 2.59e6, # 1 sq mile = 2.59e6 sq meters
            "sq_meter_sq_yard": 1.196, # 1 sq meter = 1.196 sq yards
            "sq_yard_sq_meter": 0.836127, # 1 sq yard = 0.836127 sq meters
            "sq_meter_sq_foot": 10.764, # 1 sq meter = 10.764 sq feet
            "sq_foot_sq_meter": 0.092903, # 1 sq foot = 0.092903 sq meters
            "sq_meter_hectare": 1e-4, # 1 sq meter = 1e-4 hectares
            "hectare_sq_meter": 10000, # 1 hectare = 10000 sq meters
            "sq_meter_acre": 0.000247105, # 1 sq meter = 0.000247105 acres
            "acre_sq_meter": 4046.86, # 1 acre = 4046.86 sq meters
            "hectare_acre": 2.47105, # 1 hectare = 2.47105 acres
            "acre_hectare": 0.404686, # 1 acre = 0.404686 hectares
        },
                
    }

    for category, conversions_dict in conversions.items():
        if f"{unit_from}_{unit_to}" in conversions_dict:
            conversions = conversions_dict[f"{unit_from}_{unit_to}"]
            return conversions(value) if callable(conversions) else value * conversions
    return "Conversion not Supported" 
        
st.title("Unit Converter")

categories = {
        "length": ["meter", "kilometer", "centimeter", "millimeter", "mile"],
        "weight": ["gram", "kilogram", "milligram"],
        "time": ["hour", "minute", "second"],
        "temperature": ["celsius", "fahrenheit", "kelvin"],
        "volume": ["liter", "milliliter", "gallon"],
        "area": ["sq_meter", "sq_kilometer", "sq_mile", "sq_yard", "sq_foot", "hectare", "acre"],
    } 
category = st.selectbox("Select Category :", list(categories.keys()))

units = categories[category]

value = st.number_input("Enter the value :", min_value=1.0, step=1.0)

unit_from = st.selectbox("Conver From :", units)
unit_to = st.selectbox("Convert To :", units)

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.markdown(f'<p style="color: blue; font-size: 20px;">Converted Value: {result}</p>', unsafe_allow_html=True)
st.markdown("---")
st.markdown("Devolped❤️ by ***Asif Ali***")