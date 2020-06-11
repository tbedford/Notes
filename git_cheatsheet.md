# My Git cheatsheet

## GitHub access

When 2-factor authentication is used you can't use your GitHub
password on the CLI. You need to generate a personal access
token. This can be done in the GitHub UI. 

> **IMPORTANT:** When generating the token it is vital to ensure you
> select repo access rights, otherwise you will not have access to
> push to repos.

After you generate the token, when prompted, use your GitHub username
and paste the token into the password field.

## Checking credential helper

You can check whether your credential helper is configured with:

``` shell
git config --local credential.helper
git config --global credential.helper
osxkeychain
git config --system credential.helper
osxkeychain
```

## Git workflows

Help on Git workflows

```
git help workflows
```

List branches:

``` shell
git branch
git branch -av
```

Switch HEAD to <branch>:

``` shell
git checkout <branch>
```

Create a new branch based on current HEAD:

``` shell
git branch <new_branch> 
```

Create a new tracking branch based on a remote branch:

``` shell
git checkout --track <remote/branch>
```

Push to remote:

``` shell
git push origin <branch_name>
```

Delete local branch:

``` shell
git branch -d feature/login
```

Delete remote branch:

``` shell
git push origin --delete feature/login
```

Rename a file:

``` shell
git mv old_filename new_filename
```

Link local branch with upstream server:

``` shell
git push --set-upstream origin test-branch
```

Create and checkout a branch (on one command)

``` shell
git checkout -b new-branch
```


How to merge the master branch into the feature branch:

``` shell
git checkout feature1
git merge master
```

Compare differences in two local branches:

``` shell
git diff master test-branch
```

Compare a file between branches:

``` shell
git diff master test-branch README.md
```

Compare local file in feature branch with local master:

``` shell
git diff HEAD:README.md README.md 
```

Compare a file between two branches:

``` shell
git diff mybranch master -- file.md
```

When you are using auto complete on the command line you sometimes find a whole load of branches that have been deleted from GitHub (via the GitHub web interface after merging) that still appear (they are actually in .git/refs/remotes/origin). Anyway, you can remove these unwanted branches using:

``` shell
git remote prune origin
```

They then no longer appear as autocomplete options.

## Submodules

``` shell
git submodule init && git submodule update
git checkout master && git pull origin master
git config --global submodule.recurse true
```

To find out info about submodules:

``` shell
.gitmodules file (subdirectories -> repo)
```

### When a submodule needs to be updated you need to:

1. Cd into submodule directory root
2. Git checkout master
3. Git pull

Then back in VSCode do a commit for your main (parent/container) branch.

## Revert a specific commit

How to revert a commit that's been pushed up:

``` shell
git revert <commit_number>
```

## Abort a merge

If you do something like a `git merge master` and you want to undo that:

```
git merge --abort
```

## Merged branches

To find out what branches have been merged into your current branch type:

```
git branch --merged
```

Useful for clean up. Once a local branch has been merged you can get rid of it.
