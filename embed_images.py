import base64

# List your downloaded file paths and desired keys
file_paths = [
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

# Encode each image and print HTML-ready snippet
for path, key in file_paths:
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
        print(f"{key} = 'data:image/png;base64,{encoded}'\n")