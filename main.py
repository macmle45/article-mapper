import models
from api_handler import ApiHandler
from simple_article import SimpleArticle


def download_data():
    # API links
    api_articles_list = 'https://mapping-test.fra1.digitaloceanspaces.com/data/list.json'
    # api_articles_media = f'https://mapping-test.fra1.digitaloceanspaces.com/data/media/{article_id}.json'

    # create api client for download article's basic data
    api_client = ApiHandler()
    articles_base_data = api_client.get_data(api_articles_list)

    # create list of 'SimpleArticle' objects for handling rest information about article
    articles = [SimpleArticle(article['id'], article['title']) for article in articles_base_data.json()]

    # downloading article details
    for article in articles:
        article_id = article.article_id
        api_articles_details = f'https://mapping-test.fra1.digitaloceanspaces.com/data/articles/{article_id}.json'
        article_details = api_client.get_data(api_articles_details)

        article.set_article_details(article_details.json())

    return articles


def map_data():
    pass


def main():
    result = download_data()

    for art in result:
        print(art.article_id, art.title, art.author, '-----', sep='\n')


if __name__ == '__main__':
    main()
