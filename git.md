# git troubleshooting

## git asks me for the user name and password every time I pull and push
Use the SSH URL instead of the HTTPS URL.

### The SSH URL

Your github user name is actually just part of the path.

```
nix-user@domain.com:path/to/project.git
```

## User incompetence

### I forgot what I did between the last commit and now

```
git status
```

### I forgot what I did for some specific commit

``
git show (sha1)
``
### I accidentally deleted a file, and thought I could just check it back out
`git checkout (deleted file)` won't bring it back. Run `git reset HEAD (deleted file)`, then `git checkout -- (deleted file)`.

### I accidentally deleted a file, and I have already made a commit after that
`git checkout $(git rev-list -n 1 HEAD -- "$file")^ -- "$file"`

### I accidentally added a file, and luckily I haven't committed anything yet
`git reset HEAD (added file)`

### I am an idiot

[This one-liner][stackoverflow] shows your addition/removal statistics.

```
git log --author="Brian Lai" --pretty=tformat: --numstat | awk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "added lines: %s removed lines : %s total lines: %s\n",add,subs,loc }' -
```

[This other one-liner][stackoverflow 2] compares you with others, in the current code base.

```
git ls-tree --name-only -z -r HEAD|egrep -z -Z -E '\.(js|css|py|html|sh)$' | xargs -0 -n1 git blame --line-porcelain|grep "^author "|sort|uniq -c|sort -nr
```

## booboos

### I used a GUI for git and the diffs/patches/merges/pull requests don't turn out right

Be a man.

### I used git in the terminal and the diffs/patches/merges/pull requests don't turn out right

Reset your branch to match the one upstream:

```
git reset --soft HEAD^  # stash your last commit (or more, if you made more than one commit)
git stash
git fetch
git reset --hard origin/(branch name)
git stash apply
```

### I pushed stupid things onto the remote server
Run a rebase on your local branch with `git rebase -i HEAD~1`, then force a push to your branch with `git push origin +(branch)`. The commit will still be accessible by commit ID.

### I pushed really stupid things onto the remote server
Follow [this guide][github].

### I committed to the wrong branch
#### If you haven't pushed the branch to remote yet
Run `git reset --soft HEAD^ && git stash && git checkout (correct branch) && git stash pop`.
Optionally, run `git commit -a` to commit the correct branch.
#### If you've already tainted the remote repo
Run `git reset --soft HEAD^ && git stash && git checkout (correct branch) && git stash pop`.
Commit your local branch with `git commit -a`, and force-push to cover your remote using `git push --force origin (branch)`.

#### If you just want your change live

Use this syntax to push from a local branch to a remote branch that has a different name.

```
git push origin local_branch:remote_branch
```

This is also how you [fast forward remote branches][stackoverflow 15].

### I merged a pull request I didn't want / That PR broke everything and I want it out

Follow any one of [these advice][stackoverflow 3]:

```
git revert -m 1 (the hash where the PR merge happened)  # Preserves history
git reset --merge (the hash where the PR merge happened)  # Removes history
```

### I forgot where I committed my code

If it's in the stash, either [`git log -g stash`][stackoverflow 4] or `git diff -g stash` will show the commit.

If it's in a branch, consider running `git log -S "(keyword from diff)" --source --all`, or any other solution [here][stackoverflow 5].

### I want to remove all commits.
1. Find the ID of the first commit ever. It will be a hash. Remember the first six characters, e.g. `a1b2c3`.
2. Run `git checkout (e.g. a1b2c3)`.
3. Delete everything on that branch, and commit the branch with `git commit -a`. Give yourself a good reason why you're doing this.
4. Run `git gc`.
5. Run [`git filter-branch --parent-filter "sed 's/-p (e.g. a1b2c3)//'" HEAD`][stackoverflow 6].
6. Optionally, push to remote.

### I was smart enough to use `--depth=1`, but too dumb to undo it
Well, now you need `--depth=999`.

## "Your branch is ahead of..."
*Your branch has different code than the remote one even if a `git pull origin (branch)` tells you `Already up-to-date.` This will make you deploy incorrect code. Beware!*
On the branch that says that, do [`git reset --hard origin/(branch) && git pull`][stackoverflow 7]

## Cannot checkout master for some reason
You got this message:

'''
$ git checkout master
error: pathspec 'master' did not match any file(s) known to git.
'''

If you really have a `master` branch, then try `git checkout -b master && git pull origin master` as a hack.

## "error: pathspec '(remote branch)' did not match any file(s) known to git."
Run `git pull`. You can now checkout the branch.

## "You are in 'detached HEAD' state"
`git stash && git checkout -b (new branch) && git stash pop`

## git submodules
### Can't tell if I will be committing a file to the repo or the submodule
The file will be committed to the closest `.git` repository.

```
repo
+ submodule
| - foo.txt  (to submodule)
+ bar.txt  (to main repo)
```

### I edited a file in one of my submodules
`cd (submodule path) && git reset --hard HEAD`

### "fatal: Not a git repository: (one of your submodules)"
Nudge around your `.git/modules/(submodule name)/config` file and see if any obvious errors are in place.

### I cloned a repository without the `--recursive` flag
At project root, `git submodule init && git submodule update --recursive`

### There is nothing in my submodule folders
At project root, `git submodule init && git submodule update --recursive`

### I couldn't remove a submodule
Edit the `.gitmodules` file in the project root. Remove references to the submodule.
Run `git rm --cached (path/to/submodule) && git commit -a`

### fatal: reference isn’t a tree: (submodule repo had a force-push)
`cd (submodule path) && git reset --hard origin/(branch) && git pull`

### What if I want to change where the submodule comes from?
To [change origin of submodules that have already been cloned][stackoverflow 8], follow these steps:

```
cd submodule_folder
git config remote.origin.url (repo ssh url)
```


## `M` (modified) flags won't go away after a hard reset
git does not have permission to modify your files. Give it write permission one way or another, using something like `chmod -R 664 .` (untested)

## I don't want to share my commit history with others
[`git archive -o latest.zip HEAD`][stackoverflow 9]

## I can't overwrite untracked local files when pulling
Try `git fetch --all && git reset --hard origin/(branch)`.

## Tried to cherry-pick a range of commits, but it didn't include the oldest commit
You need a `^`. Run `git cherry-pick -m 1 --ff (older hash)^..(newer hash)`. `m` isn't necessarily 1.

## I can't cherry pick something from remote

Fetch the repository first. Then, the hash of the commit can be cherry picked.

## My tags won't go onto the remote repo
`git push --tags`

## ... but I accidentally all the tags
Delete a tag locally, then push it.
```
git tag -d 12345
git push origin :refs/tags/12345
```

### Checking out a tag
`git checkout tags/{tag name}`

## [zsh isn't showing diffs in colour][stackoverflow 10]

```
git config color.diff auto --global
git config color.status auto --global
```

## Want to search for a change in history
`git grep <regex> $(git rev-list --all)`

## Want to revert, like, one file from a booboo commit
Run `git checkout HEAD^ -- path_to_file`. The file will be popped out to its previous state.

## git 1.7.1 couldn't create orphan branches

[Solution][stackoverflow 11]

```
git symbolic-ref HEAD refs/heads/newbranch 
rm .git/index 
git clean -fdx 
<do work> 
git add your files 
git commit -m 'Initial commit'
```

## Git keeps asking me for my SSH password
[The agent][stackoverflow 12] must be run with `eval \`ssh-agent -s\``. And only after that can you run `ssh-add`.


* `git clean` is a version of `git reset --hard HEAD` that removes all untracked files.

## ` ! [remote rejected] a/b -> a/b (failed to lock)`
You already have a branch called `a`.
You cannot have another branch called `a/b`.

## Git patches

### Adding only some of the staged things

* `git add -p` (p stands for patch)

### Creating a patch
* Save a patch: `git format-patch -n HEAD^`
* Save a patch file under any name: `git format-patch (branch name) --stdout > diff.patch`

### Applying a patch

* Check what's in the patch: `git apply --stat diff.patch`
* Check if the patch can be applied: `git apply --check diff.patch`
* Apply the patch: `git apply diff.patch`, **OR**
* If you want to sign off what you apply, `git am --signoff < diff.patch`

## Blaming people

* Basic blame: `git blame HEAD -- file`
* Blame with `sudo apt-get git-gui`: `git gui blame file`

### Some idiot impersonated me

Then [sign your commits][mikegerwitz] with `git commit -S -am`

And [verify them][stackoverflow 13] with `git log --show-signature`

See also: [backing up your keys][stackoverflow 14]

## The Stash

* Stashed something, can't get it back out: `git stash apply` or `git stash pop` (the latter removes the stash)


## GitHub

* [Permission classes][github 2]

[github]: https://help.github.com/articles/remove-sensitive-data
[github 2]: https://help.github.com/articles/permission-levels-for-an-organization-repository
[mikegerwitz]: http://mikegerwitz.com/papers/git-horror-story
[stackoverflow]: http://stackoverflow.com/a/7010890/1558430
[stackoverflow 10]: http://stackoverflow.com/a/12255443/1558430
[stackoverflow 11]: http://stackoverflow.com/a/1384336/1558430
[stackoverflow 12]: http://stackoverflow.com/a/17848593/1558430
[stackoverflow 13]: http://stackoverflow.com/questions/17371955/verifying-signed-git-commits
[stackoverflow 14]: http://stackoverflow.com/questions/5587513/gnupg-encryption-how-to-export-private-secret-asc-key-to-decrypt-gpg-files-i
[stackoverflow 15]: http://stackoverflow.com/questions/10605895/how-to-fast-forward-a-remote-branch
[stackoverflow 2]: http://stackoverflow.com/a/13687302/1558430
[stackoverflow 3]: http://stackoverflow.com/questions/2389361/undo-a-git-merge
[stackoverflow 4]: http://stackoverflow.com/questions/14988929/show-all-stashes-in-git-log
[stackoverflow 5]: http://stackoverflow.com/questions/24828819
[stackoverflow 6]: http://stackoverflow.com/a/6149972
[stackoverflow 7]: http://stackoverflow.com/a/3882696
[stackoverflow 8]: http://stackoverflow.com/questions/10317676/git-change-origin-of-cloned-submodule
[stackoverflow 9]: http://stackoverflow.com/questions/160608
