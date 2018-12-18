# write-html-2-windows.py
 
import webbrowser
 
f = open('map_UI_cluster.html','w')
 
message = """<html lang="en">
 <head>
   <meta charset="utf-8">

  <title>Title</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.4/dist/leaflet.css" />
  
  <style>
      #mapID{
          position: absolute;
          top:0;
          right:0;
          bottom:0;
          left: 0;
      }
  </style>
</head>

 
  <body>
    <!-- Should be included after Leaflet's CSS declaration -->
	<div id="mapID"</div>
    <script src="https://unpkg.com/leaflet@1.3.4/dist/leaflet.js"
	 integrity="sha512-nMMmRyTVoLYqjP9hrbed9S+FzjZHW5gY1TWCHA5ckwXZBadntCNs8kEqAWdrb9O7rxbCaA4lKTIWjDXZxflOcA=="
	 crossorigin=""> 
	 </script>
	
	
	<script>
		var map = L.map('mapID').setView([10,10], 2);
		
		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
       	}).addTo(map);
		
		var markers = [
			{pos: [39.267326, -76.798309], popup: "Ellicott City"},
			{pos: [39.401497, -76.601913], popup: "Towson"},
			{pos: [39.419552, -76.780251], popup: "Owings Mills"},
			{pos: [39.272050, -76.731846], popup: "Catonsville"},
			{pos: [39.257411, -76.523675], popup: "Dundalk"},
			{pos: [39.381934, -76.457304], popup: "White Marsh"},
			{pos: [39.307507, -76.479036], popup: "Essex"},
			{pos: [39.377329, -76.539688], popup: "Parkville"},
			{pos: [39.217522, -76.868729], popup: "Columbia"},
			{pos: [39.290386, -76.612190], popup: "Baltimore"}];		;
			
			
		markers.forEach(function (obj) {
			var m = L.marker(obj.pos).addTo(map),
			p = new L.popup()
					.setContent(obj.popup)
					.setLatLng(obj.pos);
			m.bindPopup(p);
		});	
	</script>
	</body> 
  </html>"""
f.write(message)
f.close()
 
webbrowser.open_new_tab('map_UI_cluster.html')
 