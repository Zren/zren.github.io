---
title: Ignoring KDE Work Branches
layout: post
---

I regularly use `git lga` (custom alias in `~/.gitconfig`) to view all branches. 

```ini
[alias]
	lg = log --oneline --graph
	lga = log --oneline --graph --all
```

With how active the KDE repositories are, it's a little annoying trying to read the relevant branches (`master`, `Plasma/5.25`, etc).

![](/pic/2022-07-11___14-23-05.png)

I don't really need to see all the work branches (which are normally hidden in forks on GitHub).

To clean things up, I found this on StackOverflow:
<https://stackoverflow.com/questions/16842426/can-git-permanently-ignore-a-remote-branch>

I worked out that I needed to run this in every kde repo:

```bash
git config --add remote.origin.fetch '^refs/heads/work/*'
```

Which adds the following line in the repository's `.git/config`.

```ini
[remote "origin"]
	url = kde:plasma/plasma-workspace.git
	fetch = +refs/heads/*:refs/remotes/origin/*
	fetch = ^refs/heads/work/*
```

Since I already have all the KDE source code downloaded, I'll need to delete the existing references to the work branches. This can be accomplished simply with:

```bash
rm -r './.git/refs/remotes/origin/work/'
```

Since KDE has nearly 400 repositories (ignoring non plasma kde apps), I wrote a script to automate these commands. It'll run the commands on git repositories 1-2 levels deep in `~/kde/src/` so it should work even if you use `directory-layout=flat` in `~/.config/kdesrc-buildrc`.

`kdesrc-ignoreworkbranches.sh`

```bash
#!/bin/bash

curDir=`pwd`

if [ ! -d ~/kde/src/ ]; then
	exit 1
fi

function delRemoteWorkBranches () {
	repoPath="$1"
	repoName=`basename "$repoPath"`
	# echo "$repoPath"
	cd "$repoPath"
	if [ -z "$(git config --get-all remote.origin.fetch | grep '\^refs/heads/work/\*')" ]; then
		echo "[$repoName] git config --add remote.origin.fetch"
		git config --add remote.origin.fetch '^refs/heads/work/*'
	fi
	if [ -d "./.git/refs/remotes/origin/work/" ]; then
		echo "[$repoName] rm -r './.git/refs/remotes/origin/work/'"
		rm -r './.git/refs/remotes/origin/work/'
	fi
}

for parentDirName in `ls ~/kde/src/`; do
	parentDirPath=`realpath ~/kde/src/"$parentDirName"`
	if [ -d "$parentDirPath" ]; then
		if [ -d "$parentDirPath"/.git/ ]; then
			delRemoteWorkBranches "$parentDirPath"
		else
			for dirName in `ls "$parentDirPath"/`; do
				dirPath=`realpath "$parentDirPath"/"$dirName"`
				if [ -d "$dirPath"/.git/ ]; then
					delRemoteWorkBranches "$dirPath"
				fi
			done
		fi
	fi
done

cd "$curDir"
```

After running the command, my git log looks clean like this!

![](/pic/2022-07-11___14-24-58.png)

