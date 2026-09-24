import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

st.set_page_config(
    page_title="Jiya's App",  # The text that appears in the browser tab
    page_icon="🚀",  # Can be an emoji or a path to an image/favicon file
    layout="wide",  # Optional: 'centered' or 'wide'
)



#TRAVEL THEMED BACKGROUND.....
st.markdown("""

<style>

.stApp {
    background: linear-gradient(
        135deg,
        #081B33,
        #123C69,
        #1E6091,
        #38A3A5,
        #6A4C93,
        #123C69
    );

    background-size: 400% 400%;

    animation: backgroundMove 12s ease infinite;
}


/* BACKGROUND COLOUR ANIMATION */

@keyframes backgroundMove {

    0% {
        background-position: 0% 50%;
    }

    25% {
        background-position: 50% 100%;
    }

    50% {
        background-position: 100% 50%;
    }

    75% {
        background-position: 50% 0%;
    }

    100% {
        background-position: 0% 50%;
    }

}


/* TRAVEL EMOJIS */

.travel-emoji {
    position: fixed;
    font-size: 35px;
    z-index: 0;
    pointer-events: none;
    opacity: 0.8;

    animation: floatEmoji 5s ease-in-out infinite;
}

.emoji1 {
    left: 3%;
    top: 12%;
}

.emoji2 {
    right: 3%;
    top: 12%;
    animation-delay: 1s;
}

.emoji3 {
    left: 3%;
    bottom: 12%;
    animation-delay: 2s;
}

.emoji4 {
    right: 3%;
    bottom: 12%;
    animation-delay: 3s;
}


/* EMOJI MOVEMENT */

@keyframes floatEmoji {

    0% {
        transform: translateY(0px);
        opacity: 0.5;
    }

    50% {
        transform: translateY(-12px);
        opacity: 0.9;
    }

    100% {
        transform: translateY(0px);
        opacity: 0.5;
    }

}

</style>

<div class="travel-emoji emoji1">🌍</div>
<div class="travel-emoji emoji2">🧳</div>
<div class="travel-emoji emoji3">🗺️</div>
<div class="travel-emoji emoji4">🏝️</div>

""", unsafe_allow_html=True)



# Custom UI styles
st.markdown(
    """
    <style>
    /* This makes the text colors shift like a rainbow */
    @keyframes rainbow-text {
        0% { color: #FF512F; }
        25% { color: #FFD700; }
        50% { color: #00C9FF; }
        75% { color: #92FE9D; }
        100% { color: #FF512F; }
    }

    /* This makes the globe spin slowly */
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* This makes the airplane fly up and down in a loop */
    @keyframes fly {
        0% { transform: translateX(0px) translateY(0px) scale(1); }
        50% { transform: translateX(20px) translateY(-12px) scale(1.1); }
        100% { transform: translateX(0px) translateY(0px) scale(1); }
    }

    .moving-globe {
        display: inline-block;
        animation: spin 6s linear infinite;
    }

    .flying-plane {
        display: inline-block;
        animation: fly 2.5s ease-in-out infinite;
    }

    .my-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        animation: rainbow-text 6s ease infinite;
        margin-bottom: 0px;
    }

    .my-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #a0aec0;
        margin-top: 8px;
    }

    /* A glowing colorful divider line */
    .cool-line {
        border: none;
        height: 4px;
        background: linear-gradient(90deg, #FF512F, #FFD700, #00C9FF, #92FE9D);
        margin: 25px auto;
        width: 70%;
        border-radius: 4px;
    }
    </style>

    <div>
        <h1 class="my-title">
            <span class="moving-globe">🌍</span> Travel Assistant <span class="flying-plane">✈️</span>
        </h1>
        <p class="my-subtitle">Your colorful, friendly helper for planning amazing trips!</p>
        <hr class="cool-line">
    </div>
    """,
    unsafe_allow_html=True,
)



# Colorful centered subtitle using HTML text coloring.......
st.markdown(
    "<h3 style='text-align: center; color: #FFD700;'>✨ YOUR PERSONAL TRAVEL PLANNER ✨</h3>",
    unsafe_allow_html=True,
)




# Custom CSS for styling and Airplane Animation....
st.markdown(
    """
    <style>
    /* Dark Theme Styling */
    .stApp {
        background-color: #12181b;
        color: #ffffff;
    }

    /* Main Container Card Styling */
    div.stBlock {
        background-color: #1e2930;
        border-radius: 12px;
        padding: 20px;
    }

    /* Airplane Keyframe Animation (Bottom to Top) */
    @keyframes flyUp {
        0% {
            bottom: -150px;
            opacity: 0;
            transform: translateX(-50%) scale(0.6);
        }
        50% {
            opacity: 1;
            transform: translateX(-50%) scale(1.1);
        }
        100% {
            bottom: 100vh;
            opacity: 0;
            transform: translateX(-50%) scale(0.8);
        }
    }

    /* Floating Airplane Container */
    .airplane-container {
        position: fixed;
        left: 50%;
        bottom: -150px;
        z-index: 9999;
        pointer-events: none;
        animation: flyUp 5.0s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    }

    /* Airplane Image/Icon Styling */
    .airplane-icon {
        width: 180x;
        height: auto;
        filter: drop-shadow(0px 10px 15px rgba(0, 191, 255, 0.4));
    }
    </style>
    """,
    unsafe_allow_html=True,
)



# Simple user inputs decorated with emojis......
#  🗺️ SECTION 1: DESTINATION
destination = st.text_input("Where do you want to go? 🗺️", placeholder="e.g., Goa, Paris, Norway...")

col_date, col_days = st.columns(2)
with col_date:
    start_date = st.date_input("📅 Starting Date")
with col_days:
    days = st.number_input("🔢 How many days of trip?", min_value=1, max_value=30, value=5)

# 💰 SECTION 2: BUDGET
st.markdown("### 💰 Budget")
col_budget_val, col_budget_type = st.columns(2)
with col_budget_val:
    budget_amount = st.text_input("What is your budget? 💰", value="70000")
with col_budget_type:
    budget_type = st.selectbox("Budget Type", ["Total Trip Budget", "Daily Budget"])

# 👥 SECTION 3: TRAVELLERS
st.markdown("### 👥 Travellers")
col_with, col_count = st.columns(2)
with col_with:
    travelers = st.selectbox("Whom You're Travelling With...?", ["Solo", "Couple", "Friends", "Family"])
with col_count:
    num_travelers = st.number_input("Number of Travellers", min_value=1, max_value=20, value=1)

# ⚙️ SECTION 4: YOUR PREFERENCES
st.markdown("### ⚙️ Your Preferences")
interests = st.multiselect(
    "What are you interested in?",
    ["Nature", "Mountains", "Culture", "Food", "Adventure", "Photography", "Nightlife", "Shopping", "Skiing", "Relaxation", "Trekking"],
    default=["Nature"]
)

col_hotel, col_transport = st.columns(2)
with col_hotel:
    hotel_pref = st.selectbox("🏨 Hotel Preference", ["Budget", "Mid-range comfort", "Luxury / Splurge"])
with col_transport:
    transport_pref = st.selectbox("🚊 Transportation Preference", ["Public transport", "Rental Car", "Private Driver"])

food_pref = st.selectbox("🍲 Food Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Anything goes"])
trip_type = st.selectbox("⏳ What type of trip do you want?", ["Balanced", "Fast-paced", "Relaxed & Slow"])
additional_notes = st.text_area("📝 Anything else you want?", placeholder="Example: I don't want too much walking. I want to visit famous food places...")




# Prompt....
prompt = f"""CRITICAL RULE: You must start your response with a cheerful greeting (like "Good morning!" or "Hello!") and you must end your response with a polite goodbye message. If you miss either, the task is wrong.

Now, act as an expert travel planner and create a trip plan for this user:
- Destination: {destination}
- Duration: {days} days
- - Budget: {budget_amount} {budget_type}
- Traveling with: {travelers} ({num_travelers} people)
- Preferences: Interests: {', '.join(interests)}, Hotel: {hotel_pref}, Transport: {transport_pref}, Food: {food_pref}, Type: {trip_type}
- Additional Info: {additional_notes}

Format your response with:
1. The greeting at the very beginning.
2. Clear bullet points for the day-by-day itinerary, must-try foods, and travel tips.
3. The goodbye message at the very end."""




# Simple loading spinner with custom text.....
if st.button("✨ Plan Trip", type="primary"):
  if not destination:
        st.warning("Please enter a destination first!")
  else:
# Trigger the animated airplane overlay (Bottom to Top movement)....
        st.markdown(
            """
            <div class="airplane-container">
                <img src="https://cdn-icons-png.flaticon.com/512/7893/7893979.png" class="airplane-icon" alt="Airplane" />
            </div>
            """,
            unsafe_allow_html=True,
        )

# Spinner/status while airplane animates....
        with st.spinner("✈️ Flying to your destination..."):
            # using Gemini to generate response.....
           model_type = ["gemini-3.5-flash-lite" , "gemini-3.8-flash"]
           interaction = client.interactions.create(
                model=model_type[0],
                input=prompt)
             
                
 


 # Success Message.....
        st.success("🎉 Voila! Here are some fab suggestions...")
        st.markdown("---")
        st.write(interaction.output_text)
        st.toast("Your passport to adventure is ready! 🎫✈️", icon="🌍")
