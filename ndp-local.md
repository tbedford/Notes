# Simplified guide to running NDP locally

* This assumes you have Git installed and running
* Also assumes you have brew installed and running
* Assumes you have cloned NDP locally
* Assumes you are running on a Mac (tweaks required if not)

## Updated 2020-07-09

We have now Gemified NDP

You need to run Ruby 2.5.8

## Install your bits

Install tools:

``` shell
brew install postgres rbenv
```

and might as well start Postgres:

``` shell
brew services start postgresql
```

## Fix up your `.env`

``` shell
cp .env.example .env
```

Open the file and comment out the Redis line as we're not using it locally (for testing docs).

## Set Ruby version

``` shell
rbenv 2.5.8
rbenv global 2.5.8
gem install bundle
bundle install
```

## Submodules

You also need to have the submodules present locally:

``` shell
git submodule init && git submodule update
git config --global submodule.recurse true
```

## Run the Gem

Run the Gem with:

```shell
OAS_PATH="`pwd`/_open_api/api_specs/definitions" bundle exec nexmo-developer --docs=`pwd`
```

Then go to localhost:3000 with your browser.
