from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# 停留所データ（固定）
STOPS = [
    {
        "stop_name": "城東小学校前",
        "url": "https://bus.ibako.co.jp/timetable/select/?no=2220&f_from_type=1&f_from=%E5%9F%8E%E6%9D%B1"
    },
    {
        "stop_name": "水戸駅北口",
        "url": "https://bus.ibako.co.jp/timetable/result/?no=4176&de=3&f_from_type=1&f_from_genre=&f_from=%E6%B0%B4%E6%88%B8%E9%A7%85"
    }
]

# -------------------------------
# ① スマホ向け UI（トップページ）
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def index():
    html = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>茨城交通バス停リンク</title>
        <style>
            body { font-family: sans-serif; padding: 20px; background: #f5f5f5; }
            h1 { font-size: 22px; }
            .stop-box {
                background: white;
                padding: 15px;
                margin-bottom: 12px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            a {
                text-decoration: none;
                color: #0078D4;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>茨城交通 バス停リンク</h1>
        <p>見たい停留所をタップしてください。</p>
    """

    # 停留所リストを自動生成
    for stop in STOPS:
        html += f"""
        <div class="stop-box">
            <a href="{stop['url']}" target="_blank">{stop['stop_name']}</a>
        </div>
        """

    html += """
    </body>
    </html>
    """
    return html


# -------------------------------
# ② API：/stops（アプリ用）
# -------------------------------
@app.get("/stops")
def get_stops():
    return STOPS
