import streamlit as st

# Conversion functions
def convert(value, from_unit, to_unit, conversion_type):
    if conversion_type == 'Length':
        conversions = {
            'meters': 1,
            'feet': 3.28084,
            'kilometers': 0.001,
            'miles': 0.000621371
        }
    elif conversion_type == 'Weight':
        conversions = {
            'kilograms': 1,
            'pounds': 2.20462,
            'grams': 1000,
            'ounces': 35.274
        }
    elif conversion_type == 'Temperature':
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return value + 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return value - 273.15
        return value
    elif conversion_type == 'Volume':
        conversions = {
            'liters': 1,
            'gallons': 0.264172,
            'milliliters': 1000,
            'fluid ounces': 33.814
        }
    elif conversion_type == 'Mass':
        conversions = {
            'kilograms': 1,
            'grams': 1000,
            'pounds': 2.20462,
            'ounces': 35.274
        }
    else:
        return None

    return value * conversions[to_unit] / conversions[from_unit]

# Streamlit app
st.title("Unit Converter App")
st.markdown("<style>body {background-color: #f0f0f0;}</style>", unsafe_allow_html=True)


# Conversion type selection
conversion_type = st.selectbox("Select conversion type:", ['Length', 'Weight', 'Temperature', 'Volume', 'Mass'], index=0)
st.markdown("<h2 style='color: #4CAF50;'>Convert Your Units Easily!</h2>", unsafe_allow_html=True)


# Input value
value = st.number_input("Enter value:", value=0.0, min_value=0.0, key="value_input")


st.write("### Enter the value you want to convert:")


# Unit selection based on conversion type
if conversion_type == 'Length':
    from_unit = st.selectbox("From unit:", ['meters', 'feet', 'kilometers', 'miles'])
    to_unit = st.selectbox("To unit:", ['meters', 'feet', 'kilometers', 'miles'])
elif conversion_type == 'Weight':
    from_unit = st.selectbox("From unit:", ['kilograms', 'pounds', 'grams', 'ounces'])
    to_unit = st.selectbox("To unit:", ['kilograms', 'pounds', 'grams', 'ounces'])
elif conversion_type == 'Temperature':
    from_unit = st.selectbox("From unit:", ['Celsius', 'Fahrenheit', 'Kelvin'])
    to_unit = st.selectbox("To unit:", ['Celsius', 'Fahrenheit', 'Kelvin'])
elif conversion_type == 'Volume':
    from_unit = st.selectbox("From unit:", ['liters', 'gallons', 'milliliters', 'fluid ounces'])
    to_unit = st.selectbox("To unit:", ['liters', 'gallons', 'milliliters', 'fluid ounces'])
elif conversion_type == 'Mass':
    from_unit = st.selectbox("From unit:", ['kilograms', 'grams', 'pounds', 'ounces'])
    to_unit = st.selectbox("To unit:", ['kilograms', 'grams', 'pounds', 'ounces'])

# Convert button
if st.button("Convert Now!", key="convert_button"):
    result = convert(value, from_unit, to_unit, conversion_type)
    st.success(f"{value} {from_unit} is **{result} {to_unit}**", icon="✅")
