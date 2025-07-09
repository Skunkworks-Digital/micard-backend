import base64

# Define your images and keys
images = [
    ("591AB1E9-275E-4AE6-B407-27143228624B.png", "LOGO"),
    ("CE437D47-CFA1-4715-BBC6-CCB670A767FB.png", "INTRO_GRAPHIC"),
    ("039E3592-2B06-4CB9-91FF-B8B8C9BA1EBE.png", "PROFILE_SETUP"),
    ("FA0FBC9F-06A8-4F6F-821F-E95906BCA4E7.png", "QR_NFC"),
    ("9577FB4B-9910-4E61-80CF-2EACDE59F4D9.png", "ANALYTICS"),
    ("47AE9B5E-10F5-4C22-A27D-8417AECF8455.png", "PUBLIC_PROFILE"),
    ("12337C03-9EDD-4096-A75C-73D0B69C3032.png", "USERFLOW1"),
    ("573A60EE-954F-4A0C-9F11-C4C10E0044A3.png", "USERFLOW2"),
    ("E8A70414-74A3-49A8-9730-E4FDB384FF7E.png", "TECHREQS")
]

# Encode each image
encoded = {}
for path, key in images:
    with open(path, "rb") as f:
        encoded[key] = "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

# Create the final index.html with embedded images
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MiCrad | Smart Business Cards</title>
  <style>
    body {{ font-family: 'Segoe UI', Roboto, Arial, sans-serif; margin:0; padding:0; background: #f9fafb; color:#333; }}
    header, section, footer {{ padding: 40px 20px; max-width: 1200px; margin:auto; }}
    header {{ background: #11376A; color: white; text-align: center; }}
    header img {{ max-width: 150px; margin-bottom: 20px; }}
    h1 {{ font-size: 2.5em; margin: 0; }}
    p {{ font-size: 1.1em; }}
    h2 {{ color: #11376A; margin-top: 60px; }}
    .modules, .userflow {{ display: flex; flex-wrap: wrap; justify-content: space-around; gap: 30px; margin-top: 40px; }}
    .modules div {{ flex: 1; min-width: 220px; background: white; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.05); padding: 20px; text-align: center; }}
    .modules img {{ width: 80px; margin-bottom: 10px; }}
    .userflow img {{ max-width: 100%; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
    footer {{ text-align: center; background: #11376A; color: white; padding: 30px 20px; margin-top: 60px; }}
  </style>
</head>
<body>

<header>
  <img src="{encoded['LOGO']}" alt="MiCrad Logo" />
  <h1>MiCrad</h1>
  <p>Transforming business cards into dynamic digital profiles with NFC & QR code technology.</p>
</header>

<section>
  <h2>Introduction</h2>
  <p>MiCrad is a mobile-first platform transforming traditional business cards into interactive digital experiences. Professionals share dynamic profiles seamlessly with a tap or scan, bridging physical and digital networking.</p>
  <img src="{encoded['INTRO_GRAPHIC']}" alt="Introduction Graphic" style="max-width:100%; margin-top:20px;">
</section>

<section>
  <h2>Core Features & Modules</h2>
  <div class="modules">
    <div>
      <img src="{encoded['PROFILE_SETUP']}" alt="Profile Setup" />
      <h3>Profile Setup</h3>
      <p>Setup & customise user profiles.</p>
    </div>
    <div>
      <img src="{encoded['QR_NFC']}" alt="QR/NFC Integration" />
      <h3>QR/NFC Integration</h3>
      <p>Generate NFC and QR codes instantly.</p>
    </div>
    <div>
      <img src="{encoded['ANALYTICS']}" alt="Analytics Dashboard" />
      <h3>Analytics Dashboard</h3>
      <p>Track scans, taps, and profile views.</p>
    </div>
    <div>
      <img src="{encoded['PUBLIC_PROFILE']}" alt="Public Profile Access" />
      <h3>Public Profile Access</h3>
      <p>Effortless profile viewing and sharing.</p>
    </div>
  </div>
</section>

<section>
  <h2>User Flow</h2>
  <div class="userflow">
    <img src="{encoded['USERFLOW1']}" alt="User Flow Diagram 1" />
    <img src="{encoded['USERFLOW2']}" alt="User Flow Diagram 2" />
  </div>
</section>

<section>
  <h2>Technical Requirements & Compatibility</h2>
  <img src="{encoded['TECHREQS']}" alt="Technical Requirements" style="max-width:100%;">
</section>

<footer>
  &copy; 2025 MiCrad. All rights reserved.
</footer>

</body>
</html>
"""

# Write the final index.html
with open("index.html", "w") as f:
    f.write(html)

print("✅ index.html generated with embedded images.")