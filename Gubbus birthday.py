import os

def create_birthday_page(Gubbu):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Happy Birthday {Gubbu} 🎂❤️</title>
        <style>
            body {{
                text-align: center;
                background: url('https://i.ibb.co/0q7YVzM/sparkle-background.gif') no-repeat center center fixed;
                background-size: cover;
                font-family: 'Comic Sans MS', cursive, sans-serif;
                color: white;
            }}
            h1 {{
                font-size: 50px;
                margin-top: 20px;
                text-shadow: 2px 2px 5px #ff1493;
            }}
            h2 {{
                font-size: 30px;
                margin-top: 20px;
                text-shadow: 2px 2px 5px #ff69b4;
            }}
            .cake {{
                margin-top: 30px;
            }}
            .roses {{
                margin: 20px;
            }}
            .question {{
                margin-top: 40px;
                font-size: 28px;
                font-weight: bold;
                background: rgba(0,0,0,0.6);
                padding: 15px;
                border-radius: 15px;
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <h1>Happy Birthday {Gubbu}! 🎉🎂</h1>
        <div class="cake">
            <img src="https://i.ibb.co/3sfWwXZ/cake-with-candles.png" alt="Cake" width="300">
        </div>
        <h2>🎶 A special day just for you 🎶</h2>
        <audio autoplay loop>
            <source src="https://www2.cs.uic.edu/~i101/SoundFiles/HappyBirthdaySong.mp3" type="audio/mpeg">
        </audio>
        <div class="roses">
            <img src="https://i.ibb.co/2Wvjqfn/red-roses.png" width="250">
            <img src="https://i.ibb.co/2Wvjqfn/red-roses.png" width="250">
        </div>
        <video width="400" controls autoplay loop>
            <source src="your-video.mp4" type="video/mp4">
            Your browser does not support video.
        </video>
        <div class="question">💍 Will you be my Ardhagni in this life? ❤️</div>
    </body>
    </html>
    """

    with open("birthday_page.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Birthday page created! Open 'birthday_page.html' in your browser.")

# Replace with your girlfriend's name
create_birthday_page("My Love")
