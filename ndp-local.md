# Simplified guide to running NDP locally

* This assumes you have Git installed and running
* Also assumes you have brew installed and running
* Assumes you have cloned NDP locally

## Install your bits

Install tools:

``` shell
brew install postgres rbenv yarn nvm
```

and might as well start Postgres:

``` shell
brew services start postgresql
```

## .bash_profile

Best way is to use `nvm` as we are fussy about Node versions. For managing Ruby installs use `rbenv`.

Add the following to your bash profile:

``` shell
eval "$(rbenv init -)"
export NVM_DIR="$HOME/.nvm"
. "/usr/local/opt/nvm/nvm.sh"
```

Restart Terminal for this to take effect.

## Fix up your `.env`

``` shell
cp .env.example .env
```

Open the file and comment out the Redis line as we're not using it locally (for testing docs).

## Set Ruby version

Set Ruby version and install gems:

``` shell
rbenv install 2.5.7
rbenv global 2.5.7
gem install bundle
bundle install
```

## Set Node version

Set Node version and install Node packages:

``` shell
nvm install 12
nvm use 12
yarn install
```

## Submodules

You also need to have the submodules present locally:

``` shell
git submodule init && git submodule update
git config --global submodule.recurse true
```

## Run NDP

Run the following:

``` shell
bundle install
rails db:setup
yarn install
rails s
```

Then go to localhost:3000 with your browser.
