import streamlit as st
import anthropic

api_key = st.secrets["claude_api_key"]

# Function to call Claude AI API and get a personalized meal plan
def get_meal_plan(api_key, zzfasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    # Initialize the Claude AI client with the provided API key
    client = anthropic.Anthropic(api_key=api_key)
    
    # Define the prompt to send to Claude AI
    prompt = (
        f"My fasting sugar level is {fasting_sugar} mg/dL, "
        f"my pre-meal sugar level is {pre_meal_sugar} mg/dL, "
        f"and my post-meal sugar level is {post_meal_sugar} mg/dL. "
        f"My dietary preferences are {dietary_preferences}. "
        "Please provide a personalized meal plan in detail that can help me manage my blood sugar levels effectively."
    )
    
    # Call Claude AI API
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=250,
        temperature=0.7,
        system="You are a world-class nutritionist who specializes in diabetes management.",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    raw_context = message.content
    itinerary = raw_context[0].text
    return itinerary

# Streamlit app
st.title("Personal Meal Planner")

st.write("""
For those managing diabetes, **Personal Meal Planner** personalized meal planning tool is designed specifically 
for diabetic patients, allowing you to input your sugar levels and preferences to receive customized meal 
plans that support your individual needs and help you manage your blood sugar effectively.

""")

# Sidebar inputs for sugar levels and dietary preferences
st.sidebar.header("Enter Your Details")

fasting_sugar = st.sidebar.number_input("Fasting Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
pre_meal_sugar = st.sidebar.number_input("Pre-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
post_meal_sugar = st.sidebar.number_input("Post-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)

dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., vegetarian, low-carb)")

# Generate meal plan button
if st.sidebar.button("Generate Meal Plan"):
    meal_plan = get_meal_plan(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    st.write("Based on your sugar levels and dietary preferences, here is a personalized meal plan:")
    st.markdown(meal_plan)
        
# Disclaimer with background color
st.markdown(
    """
    <div style="background-color: #FFC38A; padding: 10px; border-radius: 5px;">
        <strong>Disclaimer:</strong> The meal plans provided by <b>Personal Meal Planner</b> are generated based on the 
        information you input and are intended for educational and informational purposes only. They should not 
        be considered a substitute for professional medical advice, diagnosis, or treatment.
    </div>
    """, unsafe_allow_html=True
)