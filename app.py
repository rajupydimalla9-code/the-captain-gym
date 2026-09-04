from flask import Flask, render_template, send_file
import qrcode
import os

app = Flask(__name__)

# =========================================================
# IMPORTANT:
# Online hosting tarvatha ee URL ni nee real website URL tho replace cheyyi.
# Example:
# https://your-gym-website.onrender.com
# =========================================================
PUBLIC_URL = "https://YOUR-GYM-WEBSITE-URL.com"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/qr")
def qr_code():
    # QR code generate cheyyadam
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4
    )

    qr.add_data(PUBLIC_URL)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    qr_path = os.path.join(
        "static",
        "images",
        "the_captain_gym_qr.png"
    )

    os.makedirs(os.path.dirname(qr_path), exist_ok=True)

    img.save(qr_path)

    return send_file(qr_path, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)