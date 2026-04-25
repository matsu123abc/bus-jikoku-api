from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# -------------------------
# データ分類
# -------------------------

# バス時刻表
TIMETABLES = [
    # --- 茨城交通 ---
    {
        "stop_name": "城東小学校前（茨城交通）",
        "url": "https://bus.ibako.co.jp/timetable/select/?no=2220&f_from_type=1&f_from=%E5%9F%8E%E6%9D%B1"
    },
    {
        "stop_name": "水戸駅北口（茨城交通）",
        "url": "https://bus.ibako.co.jp/timetable/result/?no=4176&de=3&f_from_type=1&f_from_genre=&f_from=%E6%B0%B4%E6%88%B8%E9%A7%85"
    },

    # --- 関東鉄道 ---
    {
        "stop_name": "トッパン前（関東鉄道）",
        "url": "https://kantetsu.jorudan.biz/?p=d&sc=4530&pn=1&v=&b1=%E3%83%88%E3%83%83%E3%83%91%E3%83%B3%E5%89%8D&m=b"
    },
    {
        "stop_name": "水戸駅北口（関東鉄道）",
        "url": "https://www.kantetsu.co.jp/cms/wp-content/themes/kr/pdf/bus/timetable_files/mt/mt07.pdf"
    }
]

# バス位置情報
REALTIME = [
    {
        "stop_name": "バス位置情報（城東小学校 → 水戸駅）【茨城交通】",
        "url": "https://mc.bus-vision.jp/ibako/view/approach.html?stopCdFrom=792&stopCdTo=51&searchHour=&searchMinute=&searchAD=-1&searchVehicleTypeCd=&searchCorpCd=&lang=0"
    }
]

# 鉄道時刻表（JR）
TRAINS = [
    {
        "stop_name": "水戸駅（JR東日本）",
        "url": "https://timetables.jreast.co.jp/timetable/list1471.html"
    },
    {
        "stop_name": "東京駅（JR東日本）",
        "url": "https://timetables.jreast.co.jp/timetable/list1039.html"
    }
]

# 特急ひたち・ときわ運行情報（JR）
TRAIN_STATUS = [
    {
        "stop_name": "在来線特急運行情報（JR東日本）",
        "url": "https://traininfo.jreast.co.jp/train_info/express.aspx?group=hitachi_tokiwa"
    }
]

# 東京駅レストラン
RESTAURANTS = [
    {
        "stop_name": "東京駅レストラン（GRANSTA）",
        "url": "https://www.gransta.jp/shop/search.html?po=di"
    }
]

# -------------------------
# UI（トップページ）
# -------------------------
@app.get("/", response_class=HTMLResponse)
def index():
    html = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>交通情報リンク</title>
        <style>
            body { font-family: sans-serif; padding: 20px; background: #f5f5f5; }
            h1 { font-size: 22px; margin-bottom: 10px; }
            h2 { font-size: 20px; margin-top: 30px; }
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
        <h1>交通情報リンク</h1>

        <h2>🕒 バス時刻表</h2>
    """

    # バス時刻表
    for stop in TIMETABLES:
        html += f"""
        <div class="stop-box">
            <a href="{stop['url']}" target="_blank">{stop['stop_name']}</a>
        </div>
        """

    html += """
        <h2>🚌 バス位置情報（リアルタイム）</h2>
    """

    # バス位置情報
    for stop in REALTIME:
        html += f"""
        <div class="stop-box">
            <a href="{stop['url']}" target="_blank">{stop['stop_name']}</a>
        </div>
        """

    html += """
        <h2>🚆 鉄道時刻表（JR東日本）</h2>
    """

    # 鉄道時刻表
    for stop in TRAINS:
        html += f"""
        <div class="stop-box">
            <a href="{stop['url']}" target="_blank">{stop['stop_name']}</a>
        </div>
        """

    html += """
        <h2>⚠️ 在来線特急運行情報</h2>
    """

    # 在来線特急運行情報
    for stop in TRAIN_STATUS:
        html += f"""
        <div class="stop-box">
            <a href="{stop['url']}" target="_blank">{stop['stop_name']}</a>
        </div>
        """

    html += """
        <h2>🍽️ 東京駅レストラン</h2>
    """

    # レストラン
    for stop in RESTAURANTS:
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


# -------------------------
# API：/stops（アプリ用）
# -------------------------
@app.get("/stops")
def get_stops():
    return {
        "timetables": TIMETABLES,
        "realtime": REALTIME,
        "trains": TRAINS,
        "train_status": TRAIN_STATUS,
        "restaurants": RESTAURANTS
    }
