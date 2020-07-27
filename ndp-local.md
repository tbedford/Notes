# Simplified guide to running NDP locally

## Updated 2020-07-09

We have now 'Gemified' NDP. 

## Prerequisites

* This assumes you have `git` installed and running
* Also assumes you have `brew` installed and running
* Assumes you have cloned NDP locally (git clone https://github.com/Nexmo/nexmo-developer.git)
* Assumes you are running on a Mac (tweaks required if not)
* Assumes you know how to create GitHub Personal Access Tokens (PATs)

## Authentication

If you look at the Gemfile:

```
source 'https://rubygems.org'

source "https://rubygems.pkg.github.com/nexmo" do
  gem "nexmo-developer", "0.0.74"
end

gem 'oas_parser', '0.25.1'
gem 'nexmo-oas-renderer', github: 'nexmo/nexmo-oas-renderer', branch: 'ndp-gemification', require: false
gem 'nexmo_markdown_renderer', github: 'nexmo/nexmo-markdown-renderer', branch: 'consider-rails-root-for-views'
```

You can see you require access to https://rubygems.pkg.github.com/nexmo 

Instructions on how to do this are here: https://docs.github.com/en/packages/using-github-packages-with-your-projects-ecosystem/configuring-rubygems-for-use-with-github-packages

For example, I authenticated using Bundler and a GitHub Personal Access Token (PAT), using the command in the GitHub docs. The credentials can then be found in `~/.bundle/config`

In future this Gem will be in the public Gems repo, rubygems.org.

### SSO

If you sign up to Nexmo's SSO, then you will need to Enable SSO for this PAT in the GitHub interface. For the PAT you use for authentication, you choose 'Enable SSO' and then select Nexmo. If you don't do this when you run bundler you will get the following error:

```shell
$ bundle
Fetching gem metadata from https://rubygems.pkg.github.com/nexmo/.
Retrying dependency api due to error (2/4): Bundler::HTTPError Net::HTTPForbidden: Resource protected by organization SAML enforcement. You must grant your personal token access to this organization.
```

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
```

## Install packages

``` shell
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
