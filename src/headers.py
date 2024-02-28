__all__ = ['headers', 'url']


url = 'https://wgmods.net/api/mods/?limit=1&offset=None&ordering=-rating&recommended_only=1&game_version_id=175&language=ru&realm=ru'

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    # 'Cookie': 'csrftoken=e4b4R3qTbCzGsEo7bkFrYAh8Dvqo0YLWtPlYeSM0keLqyhQiOJfQCqPqaqENsLY8; _ga=GA1.2.1788961493.1677259912; tmr_lvid=617f75fd639b35e0aa680d1809c11359; tmr_lvidTS=1677259912007; cm.internal.bs_id=8aef63df-fe95-455c-d3c7-cdebfcbdd682; userrealm=ru; tmr_detect=1%7C1709089552166',
    'Referer': 'https://wgmods.net/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-CSRFToken': 'kG5CoG3ec3S0sTf0OcYGgN3TrHZgzNLuzrfwLvpllF4KywHbrBy5UDBbYCdF1AYG',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}