# TempsBeta

Getting the best temps beta.
The idea is to make it easy to figure out where to go rock climbing given a location and the weather forecast.
Say you're in Vancouver and you're trying to figure out whether you should go to Squamish, Victoria or Fraser Valley 
for climbing, TempsBeta is what you would use. 

## Crawling MP

The database of climbing locations is generated by a python crawler using [scrapy](https://scrapy.org/).
The database is a cloud MongoDB Atlas.

### Setting up env

* Install [Poetry](https://python-poetry.org/docs/#installation)
* Set up the virtual env and install dependencies: `poetry shell && poetry install`
* Create a `.env` file and fill in with your info: `cp .env_example .env`

### Running the scraper

This scrapy spider will crawl though all the areas on [Mountain Project](https://www.mountainproject.com/route-guide) 
and get the location and name for each area.
```bash
scrapy crawl areas -o areas.json
```

## Back-End

The back-end is currently going to be Node.js netlify functions to keep things lean and simple.


## Front-End

The front-end is just a [Nuxt.js](https://nuxtjs.org/) app.

## Build Setup

```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev

# build for production and launch server
$ yarn build
$ yarn start

# generate static project
$ yarn generate
```

For detailed explanation on how things work, check out the [documentation](https://nuxtjs.org).

## Special Directories

You can create the following extra directories, some of which have special behaviors. Only `pages` is required; you can delete them if you don't want to use their functionality.

### `assets`

The assets directory contains your uncompiled assets such as Stylus or Sass files, images, or fonts.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/assets).

### `components`

The components directory contains your Vue.js components. Components make up the different parts of your page and can be reused and imported into your pages, layouts and even other components.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/components).

### `layouts`

Layouts are a great help when you want to change the look and feel of your Nuxt app, whether you want to include a sidebar or have distinct layouts for mobile and desktop.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/layouts).


### `pages`

This directory contains your application views and routes. Nuxt will read all the `*.vue` files inside this directory and setup Vue Router automatically.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/get-started/routing).

### `plugins`

The plugins directory contains JavaScript plugins that you want to run before instantiating the root Vue.js Application. This is the place to add Vue plugins and to inject functions or constants. Every time you need to use `Vue.use()`, you should create a file in `plugins/` and add its path to plugins in `nuxt.config.js`.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/plugins).

### `static`

This directory contains your static files. Each file inside this directory is mapped to `/`.

Example: `/static/robots.txt` is mapped as `/robots.txt`.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/static).

### `store`

This directory contains your Vuex store files. Creating a file in this directory automatically activates Vuex.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/store).
