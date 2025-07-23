# Streamlit app for an interactive map of the Houston metro area
# You can edit the code and comments to customize the map and features
import streamlit as st
import folium
from streamlit_folium import st_folium
import json
from streamlit_js_eval import streamlit_js_eval

# --- Page Configuration ---
st.set_page_config(
    page_title="Houston Pathways",
    page_icon="🗺️",
    layout="wide"
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #95a5a6;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Set the title of the web app
st.markdown('<div class="main-title">🗺️ Houston Pathways</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find the help you deserve</div>', unsafe_allow_html=True)

# Add a sidebar for user controls (optional)
st.sidebar.header("🛠️ Map Controls")

# Set the default location to the center of Houston
houston_coords = [29.7345, -95.3819]  # Latitude, Longitude

# Sidebar: Choose zoom level
zoom = st.sidebar.slider("🔍 Zoom Level", min_value=12, max_value=20, value=14, key="zoom_slider")

# Sidebar: Choose map style
map_style = st.sidebar.selectbox("🗺️ Map Style", 
[
    "OpenStreetMap",
    "CartoDB positron",
    "CartoDB dark_matter",
    "Esri.WorldImagery"
], 
key="map_style_select")

# Sidebar: Choose district to highlight
district_locations = {
    "Downtown": [29.7589, -95.3677],
    "Midtown": [29.7416, -95.3728],
    "Museum District": [29.7216, -95.3895],
    "Montrose": [29.7440, -95.3910],
    "Heights": [29.7980, -95.3995],
    "EaDo": [29.7523, -95.3422],
    "Galleria": [29.7390, -95.4670],
    "Medical Center": [29.7079, -95.4010]
}
district = st.sidebar.selectbox("🏙️ Highlight District", ["None"] + list(district_locations.keys()), key="district_select")

# Sidebar: Choose category to display
category = st.sidebar.selectbox("📂 Show Category", ["Food", "Mental Wellbeing", "Skills"], key="category_select")

# Load data from JSON files inside the .data folder
with open(".data/food.json", "r") as f:
    food_data = json.load(f)
with open(".data/skills.json", "r") as f:
    adult_data = json.load(f)
with open(".data/mental.json", "r") as f:
    mental_data = json.load(f)

# Create a Folium map centered on Houston with a softer tile style
m = folium.Map(
    location=houston_coords,
    zoom_start=zoom,
    tiles=map_style  # map style
)

# Example: Add a marker for downtown Houston with a softer color (green)
folium.Marker(
    location=houston_coords,
    popup="Ion Houston Office",
    tooltip="BAM Houston Location",
    icon=folium.Icon(color="blue", icon="info-sign")  # How will signs look?
).add_to(m)

# You can add more markers or features here
# Example: Add a circle for the Houston metro area (approximate)
folium.Circle(
    location=houston_coords,
    radius=20000,  # meters
    color="blue",
    fill=True,
    fill_opacity=0.1,
    popup="Approximate Houston Metro Area"
).add_to(m)

# Example: Highlight selected district with a circle (fixed size that doesn't change with zoom)
if district != "None":
    folium.Circle(
        location=district_locations[district],
        radius=500,  # Fixed radius in meters
        color="green",
        fill=True,
        fill_color="green",
        fill_opacity=0.6,
        popup=f"{district} District"
    ).add_to(m)

# 🥫 Food Donation Markers
if category == "Food":
    for place in food_data:
        popup_html = f"""
        <div style="width: 250px; font-size: 16px;">
            <strong>{place['name']}</strong><br>
            <em>{place['address']}</em><br>
            <p>{place['description']}</p>
        </div>
        """
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip="Food Donation Location - Click for details",
            icon=folium.Icon(color="red", icon="cutlery", prefix="fa")
        ).add_to(m)

# 📚 Adult Literacy Markers
if category == "Skills":
    for place in adult_data:
        popup_html = f"""
        <div style="width: 250px; font-size: 16px;">
            <strong>{place['name']}</strong><br>
            <em>{place['address']}</em><br>
            <p>{place['description']}</p>
        </div>
        """
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip="Adult Literacy Center - Click for details",
            icon=folium.Icon(color="orange", icon="book", prefix="fa")
        ).add_to(m)

# 🧠 Mental Health & Rehab Markers
if category == "Mental Wellbeing":
    for place in mental_data:
        popup_html = f"""
        <div style="width: 250px; font-size: 16px;">
            <strong>{place['name']}</strong><br>
            <em>{place['address']}</em><br>
            <p>{place['description']}</p>
        </div>
        """
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip="Mental Health Resource - Click for details",
            icon=folium.Icon(color="purple", icon="medkit", prefix="fa")
        ).add_to(m)

# 📍 Live Location Marker
loc = streamlit_js_eval(js_expressions="navigator.geolocation.getCurrentPosition", key="get_user_location")
if loc and "coords" in loc:
    user_lat = loc["coords"]["latitude"]
    user_lon = loc["coords"]["longitude"]
    folium.Marker(
        location=[user_lat, user_lon],
        popup="📍 You are here",
        tooltip="Your Current Location",
        icon=folium.Icon(color="black", icon="user", prefix="fa")
    ).add_to(m)

# Display the map in Streamlit, filling most of the screen
st_folium(m, width=1200, height=800)

# Accessibility note
st.markdown("""
<div style="text-align: center; font-size: 14px; color: #555;">
Use your keyboard arrows or mouse to navigate the map. Zoom with +/- keys or scroll.
</div>
""", unsafe_allow_html=True)

# Add a footer for polish and professionalism
st.markdown("""
    <div class="footer">
    Made with ❤️ using Streamlit & Folium<br>
    © 2025 BAM Houston
    </div>
""", unsafe_allow_html=True)

# ---
# How this works: (NO LIVE DATA CURRENTLY)
# - Streamlit runs the app and displays the UI in your browser.
# - Folium creates the interactive map (using Leaflet.js under the hood).
# - streamlit_folium bridges Folium maps into Streamlit apps.
#
# To add more features:
# - Add more folium.Marker, folium.Circle, folium.PolyLine, etc. to the map.
# - Use Streamlit widgets (sliders, dropdowns, etc.) to let users control the map.
#
# To run this app:
# 1. Install dependencies: pip install streamlit folium streamlit-folium streamlit-js-eval
# 2. Run: streamlit run home.py
# 3. Open the URL provided in your terminal to view the app.
