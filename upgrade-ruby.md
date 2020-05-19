# Ruby version for NDP

If you get this error (or similar):

rbenv: version `2.5.3' is not installed (set by /Users/abedford/checkouts/nexmo/nexmo-developer/.ruby-version)

Do this:

```
$ brew upgrade ruby-build

$ rbenv install 2.5.3

$ ruby --version
ruby 2.5.3p105 (2018-10-18 revision 65156) [x86_64-darwin17]

$ rails --version
rails --version
rbenv: rails: command not found

The `rails' command exists in these Ruby versions:
  2.4.1
  2.5.0
  2.5.1

$ gem install rails

$ rails --version

Could not find rake-12.3.1 in any of the sources
Run `bundle install` to install missing gems.

$ bundle install

$ rails --version

Rails 5.1.5
```

Hooray!!
