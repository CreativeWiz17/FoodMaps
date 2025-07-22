<h1 style="color:#2c3e50; font-size:48px; font-weight:bold;">FoodMaps</h1>
<p style="font-size:18px; color:#7f8c8d;">
FoodMaps is an interactive map and website that helps users locate nearby food banks and donation centers — similar to the Whataburger map, but focused on community support.  
It also includes distribution times so people can easily find where and when food is being given out in their area.
</p>

<hr>

<h2 style="color:#34495e;">How This Works</h2>
<p style="color:#95a5a6;">
<strong>Note:</strong> This is a prototype. No live data is currently available.
</p>

<ul style="color:#2c3e50;">
  <li><strong>Streamlit</strong> runs the app and displays the UI in your browser.</li>
  <li><strong>Folium</strong> creates the interactive map (using Leaflet.js under the hood).</li>
  <li><strong>streamlit_folium</strong> bridges Folium maps into Streamlit apps.</li>
</ul>

<hr>

<h2 style="color:#34495e;">Features You Can Add</h2>

<ul style="color:#2c3e50;">
  <li>Add more <code>folium.Marker</code>, <code>folium.Circle</code>, <code>folium.PolyLine</code>, etc. to highlight locations.</li>
  <li>Use Streamlit widgets like sliders, dropdowns, and toggles to control the map.</li>
  <li>Integrate real-time schedules for food distribution.</li>
  <li>Add search functionality for zip codes or neighborhoods.</li>
</ul>

<hr>

<h2 style="color:#34495e;">How to Run Locally</h2>

<ol style="color:#2c3e50;">
  <li>Install dependencies:
    <pre><code>pip install streamlit folium streamlit-folium</code></pre>
  </li>
  <li>Run the app:
    <pre><code>streamlit run home.py</code></pre>
  </li>
  <li>Open the URL provided in your terminal to view the app in your browser.</li>
</ol>

<hr>

<h2 style="color:#34495e;">Want to Contribute?</h2>
<p style="color:#7f8c8d;">
This project is open to ideas. Whether you're a developer, designer, or community organizer — your input can help make FoodMaps a powerful tool for food accessibility.
</p>
