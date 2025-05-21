import requests

def fetch_market_news():
    try:
        url = "https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=5"
        headers = {"Authorization": "Bearer YOUR_NEWSAPI_KEY"}
        res = requests.get(url, headers=headers)
        data = res.json()
        return [{"title": article["title"], "url": article["url"]} for article in data["articles"]]
    except Exception as e:
        return [{"title": "Failed to fetch news", "url": "#"}]
