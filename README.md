# TempsBeta

Getting the best temps beta.

## Setting up dev env

* Install [Poetry](https://python-poetry.org/docs/#installation)
*  `poetry shell && poetry install`
* Create a `.env` file and fill in with your info
    ```
    MONGODB_PASSWORD=<your-mongodb-atlas-password>
    MONGODB_USER=<your-mongodb-atlas-user>
    MONGODB_CLUSTER=<your-mongodb-atlas-cluster>
    ```

## Crawling MP

```bash
cd mp_scraper
scrapy crawl areas -o areas.json
```