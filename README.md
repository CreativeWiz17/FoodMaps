<h1 style="font-size:48px; font-weight:bold; font-family:'Segoe UI', sans-serif; color:#e74c3c;">FoodMaps</h1>

<p style="font-size:18px; color:#2c3e50;">
  <strong>FoodMaps</strong> is an interactive map and website that helps users locate nearby food banks and donation centers — similar to the Whataburger map, but focused on community support.  
  It also includes distribution times so people can easily find where and when food is being given out in their area.
</p>

---

<h2 style="color:#f39c12;">How This Works</h2>
<p style="color:#7f8c8d;">
  <strong>Note:</strong> This is a prototype. No live data is currently available.
</p>

<ul>
  <li><span style="color:#e74c3c;"><strong>Streamlit</strong></span> runs the app and displays the UI in your browser.</li>
  <li><span style="color:#3498db;"><strong>Folium</strong></span> creates the interactive map (using Leaflet.js under the hood).</li>
  <li><span style="color:#9b59b6;"><strong>streamlit_folium</strong></span> bridges Folium maps into Streamlit apps.</li>
</ul>

---

<h2 style="color:#2ecc71;">Features You Can Add</h2>

<ul>
  <li>Add more <code style="color:#e67e22;">folium.Marker</code>, <code style="color:#e67e22;">folium.Circle</code>, <code style="color:#e67e22;">folium.PolyLine</code>, etc. to highlight locations.</li>
  <li>Use Streamlit widgets like sliders, dropdowns, and toggles to control the map.</li>
  <li>Integrate real-time schedules for food distribution.</li>
  <li>Add search functionality for zip codes or neighborhoods.</li>
</ul>

---

<h2 style="color:#9b59b6;">How to Run Locally</h2>

<ol>
  <li>Install dependencies:
    <pre><code style="color:#c0392b;">pip install streamlit folium streamlit-folium</code></pre>
  </li>
  <li>Run the app:
    <pre><code style="color:#2980b9;">streamlit run home.py</code></pre>
  </li>
  <li>Open the URL provided in your terminal to view the app in your browser.</li>
</ol>

---

<h2 style="color:#e74c3c;">Want to Contribute?</h2>
<p style="color:#2c3e50;">
  This project is open to ideas. Whether you're a developer, designer, or community organizer — your input can help make FoodMaps a powerful tool for food accessibility.
</p>

