# Google_booksからデータを取得
import requests

async def get_book_data_google(isbn):
    url_google = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}' 
    
    response_google = requests.get(url_google).json() #情報の取得,json変換

    title = ""
    author = ""
    description = ""
    publishedDate = ""
    page_count = ""

    if response_google:
      try:
        # 追加部分
        title = response_google['items'][0]['volumeInfo']['title']
        author = response_google['items'][0]['volumeInfo']['authors'][0]

        description = response_google['items'][0]['volumeInfo']['description']
        publishedDate = response_google['items'][0]['volumeInfo']['publishedDate']
        page_count = response_google['items'][0]['volumeInfo']['pageCount']

        google_fetch = True

      except KeyError:
        google_fetch = False

    else:
        print("Book not found in Google Books.")
        google_fetch = False

    if not google_fetch:
      return {
          # 追加部分
          "title": "",
          "authors":"",

          "google_data": False,
          "description": "",
          "publishedDate": "",
          "page_count": "",
      }
    return {
        # 追加部分
        "title": title,
        "author": author,

        "google_data": google_fetch,
        "description": description,
        "publishedDate": publishedDate,
        "page_count": page_count,
    }