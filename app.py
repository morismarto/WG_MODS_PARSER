from requests import Response, get
from multiprocessing import Pool
from src import headers, url, get_exec_time, save_json, save_csv, Mods, create_csv


def get_page(url: str) -> None:
    response = get(url=url, headers=headers)
    mods = Mods(**response.json()['results'][0])
    save_json(mods, response)
    save_csv(mods, response)



@get_exec_time
def main() -> None:
    create_csv()
    urls = [url.replace('None', str(i)) for i in range(1, 136)]
    with Pool(36) as pool:
        pool.map(get_page, urls)
    
        
    
if __name__ =='__main__':
    main()


