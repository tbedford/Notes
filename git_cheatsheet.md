# My Git cheatsheet

Help on Git workflows:

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

```
git remote prune origin
```

They then no longer appear as autocomplete options.

