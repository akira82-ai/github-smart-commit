[Skip to content](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#start-of-content)

[Gist Homepage ](https://gist.github.com/)

Search Gists

Search Gists

[All gists](https://gist.github.com/discover) [Back to GitHub](https://github.com/) [Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Flisawolderiksen%2Fa7b99d94c92c6671181611be1641c733) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Flisawolderiksen%2Fa7b99d94c92c6671181611be1641c733&source=header-gist)

[Gist Homepage ](https://gist.github.com/)

[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Flisawolderiksen%2Fa7b99d94c92c6671181611be1641c733) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Flisawolderiksen%2Fa7b99d94c92c6671181611be1641c733&source=header-gist)

You signed in with another tab or window. [Reload](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733) to refresh your session.You signed out in another tab or window. [Reload](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733) to refresh your session.You switched accounts on another tab or window. [Reload](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733) to refresh your session.Dismiss alert

{{ message }}

Instantly share code, notes, and snippets.


[![@lisawolderiksen](https://avatars.githubusercontent.com/u/35797988?s=64&v=4)](https://gist.github.com/lisawolderiksen)

# [lisawolderiksen](https://gist.github.com/lisawolderiksen)/ **[git-commit-template.md](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733)**

Last active
5 days agoMarch 5, 2026 16:46

Show Gist options

- [Download ZIP](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733/archive/97903441f1f5b052c5f22a84245cb82634df3c0e.zip)

- [Star687(687)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Flisawolderiksen%2Fa7b99d94c92c6671181611be1641c733) You must be signed in to star a gist
- [Fork89(89)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Flisawolderiksen%2Fa7b99d94c92c6671181611be1641c733) You must be signed in to fork a gist

- Embed








# Select an option





























  - Embed
    Embed this gist in your website.
  - Share
    Copy sharable link for this gist.
  - Clone via HTTPS
    Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

Clone this repository at &lt;script src=&quot;https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733.js&quot;&gt;&lt;/script&gt;

- Save lisawolderiksen/a7b99d94c92c6671181611be1641c733 to your computer and use it in GitHub Desktop.

[Code](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733) [Revisions\\
11](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733/revisions) [Stars\\
687](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733/stargazers) [Forks\\
89](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733/forks)

Embed

# Select an option

- Embed
Embed this gist in your website.
- Share
Copy sharable link for this gist.
- Clone via HTTPS
Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

Clone this repository at &lt;script src=&quot;https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733.js&quot;&gt;&lt;/script&gt;

Save lisawolderiksen/a7b99d94c92c6671181611be1641c733 to your computer and use it in GitHub Desktop.

[Download ZIP](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733/archive/97903441f1f5b052c5f22a84245cb82634df3c0e.zip)

Use a Git commit message template to write better commit messages


[Raw](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733/raw/97903441f1f5b052c5f22a84245cb82634df3c0e/git-commit-template.md)

[**git-commit-template.md**](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#file-git-commit-template-md)

# Using Git Commit Message Templates to Write Better Commit Messages

[Permalink: Using Git Commit Message Templates to Write Better Commit Messages](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#using-git-commit-message-templates-to-write-better-commit-messages)

The always enthusiastic and knowledgeable mr. [@jasaltvik](https://github.com/jasaltvik) shared with our team
an article on writing (good) Git commit messages:
[How to Write a Git Commit Message](https://cbea.ms/git-commit/).
This excellent article explains why _good_ Git commit messages are important,
and explains what constitutes a good commit message. I wholeheartedly agree
with what [@cbeams](https://github.com/cbeams) writes in his article. (Have you read it yet? If not, go
[read it now](https://cbea.ms/git-commit/). I'll wait.)
It's sensible stuff. So I decided to start following the
[seven rules](https://cbea.ms/git-commit/#seven-rules)
he proposes.

...There's only one problem: My mind is already stuffed with things I should do
and things to remember. The chance of me remembering every rule every time I
commit something, are next to 0. So I made myself a Git commit message
template. That way, I don't have to remember the rules, they are presented to
me whenever I write a commit message. So now, when I do `git commit`, this is
what I see in my editor:

```
# Title: Summary, imperative, start upper case, don't end with a period
# No more than 50 chars. #### 50 chars is here:  #

# Remember blank line between title and body.

# Body: Explain *what* and *why* (not *how*). Include task ID (Jira issue).
# Wrap at 72 chars. ################################## which is here:  #

# At the end: Include Co-authored-by for all contributors.
# Include at least one empty line before it. Format:
# Co-authored-by: name <user@users.noreply.github.com>
#
# How to Write a Git Commit Message:
# https://chris.beams.io/posts/git-commit/
#
# 1. Separate subject from body with a blank line
# 2. Limit the subject line to 50 characters
# 3. Capitalize the subject line
# 4. Do not end the subject line with a period
# 5. Use the imperative mood in the subject line
# 6. Wrap the body at 72 characters
# 7. Use the body to explain what and why vs. how

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
# Your branch is up to date with 'origin/main'.
#
# Changes to be committed:
#       new file:   installation.md
#
```

What I see consists of two parts; first my own template, then Git's standard
message asking me to "Please enter the commit message".
No need to remember everything - or really much at all, except to _not_ use
`git commit -m "Commit message"`, as this means I won't see the template
I made.

**NOTE**: This kind of "template", strictly speaking consisting only of "commented out" stuff, depends on the `commit.cleanup` config being `strip` so the comments will be stripped out (ignored) in the commit message. `strip` is the default setting, so if you haven't changed it you should be good. (Thanks, [@devdrops](https://github.com/devdrops), for making me aware of this.)

## Template File

[Permalink: Template File](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#template-file)

Here is my template\*, which i put in a file called `.gitmessage` in my
home directory:

```
# Title: Summary, imperative, start upper case, don't end with a period
# No more than 50 chars. #### 50 chars is here:  #

# Remember blank line between title and body.

# Body: Explain *what* and *why* (not *how*). Include task ID (Jira issue).
# Wrap at 72 chars. ################################## which is here:  #

# At the end: Include Co-authored-by for all contributors.
# Include at least one empty line before it. Format:
# Co-authored-by: name <user@users.noreply.github.com>
#
# How to Write a Git Commit Message:
# https://chris.beams.io/posts/git-commit/
#
# 1. Separate subject from body with a blank line
# 2. Limit the subject line to 50 characters
# 3. Capitalize the subject line
# 4. Do not end the subject line with a period
# 5. Use the imperative mood in the subject line
# 6. Wrap the body at 72 characters
# 7. Use the body to explain what and why vs. how
```

## Git Configuration

[Permalink: Git Configuration](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#git-configuration)

To tell Git to use the template file (globally, not just in the current repo),
I used the following command:

`git config --global commit.template ~/.gitmessage`

And that's all there was to it. (Except I have my dotfiles in a repo, so I had
to do some symlinking and update one of my config-scripts to be able to
recreate this setup from scratch if I need to.)

## Links and Documentation

[Permalink: Links and Documentation](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#links-and-documentation)

The Git documentation contains a chapter on
[Customizing Git - Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
which in turn contains a section on the `commit.template` configuration value.

[Better Commit Messages with a .gitmessage Template](https://thoughtbot.com/blog/better-commit-messages-with-a-gitmessage-template)
has a different kind of template, which is an actual template: It contains text
which will become a part of the commit message.

I also made a Gist on [Adding co-authors to Git commits](https://gist.github.com/lisawolderiksen/f9747a3ae1e58e9daa7d176ab98f1bad) to share the credit for collaborative efforts.

## Addendum

[Permalink: Addendum](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#addendum)

An easy way to get this config using a single command:

`printf "# Title: Summary, imperative, start upper case, don't end with a period\n# No more than 50 chars. #### 50 chars is here:  #\n\n# Remember blank line between title and body.\n\n# Body: Explain *what* and *why* (not *how*). Include task ID (Jira issue).\n# Wrap at 72 chars. ################################## which is here:  #\n\n\n# At the end: Include Co-authored-by for all contributors. \n# Include at least one empty line before it. Format: \n# Co-authored-by: name <user@users.noreply.github.com>\n#\n# How to Write a Git Commit Message:\n# https://chris.beams.io/posts/git-commit/\n#\n# 1. Separate subject from body with a blank line\n# 2. Limit the subject line to 50 characters\n# 3. Capitalize the subject line\n# 4. Do not end the subject line with a period\n# 5. Use the imperative mood in the subject line\n# 6. Wrap the body at 72 characters\n# 7. Use the body to explain what and why vs. how\n" > ~/.gitmessage && git config --global commit.template ~/.gitmessage`

Thanks a lot to [@manav148](https://github.com/manav148), [@rany2](https://github.com/rany2) and [@drjasonharrison](https://github.com/drjasonharrison) for the suggestions in the comments! The command I included above includes some updates I made to the template that were not there at the time of the comments; the line length indicators and the missing space in the first item of the numbered list.

## Footnotes

[Permalink: Footnotes](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733#footnotes)

\*) It may be argued that this is, strictly speaking, not a template, as
no part of it is actually used/included in the commit message. :)

[![@DervishD](https://avatars.githubusercontent.com/u/12148736?s=80&v=4)](https://gist.github.com/DervishD)


Copy link

### **[DervishD](https://gist.github.com/DervishD)**     commented    [on Feb 14, 2021Feb 14, 2021](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=3631195\#gistcomment-3631195)

Hi Lisa!

First of all, thanks for the template, quite useful if you ask me, specially when one is writing commit messages in a hurry, and SPECIALLY when one is collaborating with other developers. Brillian 👍

One question, though. The markers for the 50 and 72 limits are off-by-one (they point at 49 and 71 chars, respectively). Is this on purpose, to accommodate newlines? Because in my experience this is not needed, you can use the full 50/72 chars and have newlines without problem, even though I may be utterly wrong, of course. I'm just curious...

Again, thanks!

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@lisawolderiksen](https://avatars.githubusercontent.com/u/35797988?s=80&v=4)](https://gist.github.com/lisawolderiksen)


Copy link

Author

### **[lisawolderiksen](https://gist.github.com/lisawolderiksen)**     commented    [on Mar 22, 2021Mar 22, 2021](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=3675672\#gistcomment-3675672)

> First of all, thanks for the template, quite useful if you ask me, specially when one is writing commit messages in a hurry, and SPECIALLY when one is collaborating with other developers. Brillian 👍

You're very welcome! I'm glad you find it useful. 😄

> One question, though. The markers for the 50 and 72 limits are off-by-one (they point at 49 and 71 chars, respectively). Is this on purpose, to accommodate newlines? Because in my experience this is not needed, you can use the full 50/72 chars and have newlines without problem, even though I may be utterly wrong, of course. I'm just curious...

No worries. I use the # to signal the last character **within** the 50/72 char limit. So when I type my commit message, I make sure that the last character I write is before **or at** the # mark. Just my quirky way of thinking, I guess. 😃

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@DervishD](https://avatars.githubusercontent.com/u/12148736?s=80&v=4)](https://gist.github.com/DervishD)


Copy link

### **[DervishD](https://gist.github.com/DervishD)**     commented    [on Mar 23, 2021Mar 23, 2021](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=3677190\#gistcomment-3677190)

Thanks a lot for the explanation. And again, for the template. Now my only concern is that Visual Studio Code supports commit templates with commented lines without stripping the comments, rendering them useless. For now, I'll use your template with my ol' faithful Vim ;)

Happy coding!

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@goswamia](https://avatars.githubusercontent.com/u/5492348?s=80&v=4)](https://gist.github.com/goswamia)


Copy link

### **[goswamia](https://gist.github.com/goswamia)**     commented    [on May 27, 2021May 27, 2021](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=3759329\#gistcomment-3759329)

Hi,

Thanks a lot for sharing this file. But I am facing one issue, when I am trying to commit this I always get abort error message. any input

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@Paul-weqe](https://avatars.githubusercontent.com/u/19515462?s=80&v=4)](https://gist.github.com/Paul-weqe)


Copy link

### **[Paul-weqe](https://gist.github.com/Paul-weqe)**     commented    [on Dec 27, 2021Dec 27, 2021](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4009222\#gistcomment-4009222)

[@goswamia](https://github.com/goswamia) I can see I am a couple of months on this. Don't know if you ever got your answer.

If you didn't, could you look if you have any `post-commit` hooks running ?

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@drjasonharrison](https://avatars.githubusercontent.com/u/6044603?s=80&v=4)](https://gist.github.com/drjasonharrison)


Copy link

### **[drjasonharrison](https://gist.github.com/drjasonharrison)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026657\#gistcomment-4026657)

I think you want a space inserted between the "1." and "Separate subject from body with a blank line"

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@manav148](https://avatars.githubusercontent.com/u/1429961?s=80&v=4)](https://gist.github.com/manav148)


Copy link

### **[manav148](https://gist.github.com/manav148)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026672\#gistcomment-4026672)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

For the procrastinators out there;

```
printf "# Title: Summary, imperative, start upper case, don't end with a period\n# No more than 50 chars. #### 50 chars is here: #\n\n# Remember blank line between title and body.\n\n# Body: Explain *what* and *why* (not *how*). Include task ID (Jira issue).\n# Wrap at 72 chars. ################################## which is here: #\n\n\n# At the end: Include Co-authored-by for all contributors. \n# Include at least one empty line before it. Format: \n# Co-authored-by: name <user@users.noreply.github.com>\n#\n# How to Write a Git Commit Message:\n# https://chris.beams.io/posts/git-commit/\n#\n# 1.Separate subject from body with a blank line\n# 2. Limit the subject line to 50 characters\n# 3. Capitalize the subject line\n# 4. Do not end the subject line with a period\n# 5. Use the imperative mood in the subject line\n# 6. Wrap the body at 72 characters\n# 7. Use the body to explain what and why vs. how\n" > ~/.gitmessage && git config --global commit.template ~/.gitmessage
```

Edited as per [@rany2](https://github.com/rany2) and [@drjasonharrison](https://github.com/drjasonharrison) comments

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@drjasonharrison](https://avatars.githubusercontent.com/u/6044603?s=80&v=4)](https://gist.github.com/drjasonharrison)


Copy link

### **[drjasonharrison](https://gist.github.com/drjasonharrison)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026677\#gistcomment-4026677)

[@manav148](https://github.com/manav148) echo doesn't expand \\n, you should use printf. Did you test this?

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@manav148](https://avatars.githubusercontent.com/u/1429961?s=80&v=4)](https://gist.github.com/manav148)


Copy link

### **[manav148](https://gist.github.com/manav148)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026689\#gistcomment-4026689)

Yes I used the command to setup on the mac.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@rany2](https://avatars.githubusercontent.com/u/71077389?s=80&v=4)](https://gist.github.com/rany2)


Copy link

### **[rany2](https://gist.github.com/rany2)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026701\#gistcomment-4026701)

`echo` does different things on different OSes and shells. Some don't even have `-e` to expand backslashes. For anything advanced, use `printf`. I guess what happened is that [@drjasonharrison](https://github.com/drjasonharrison) was on bash which doesn't expand backslashes by default (needs -e) and [@manav148](https://github.com/manav148) uses zsh which does...

For the lazies, this one should work everywhere:

```
printf "# Title: Summary, imperative, start upper case, don't end with a period\n# No more than 50 chars. #### 50 chars is here: #\n\n# Remember blank line between title and body.\n\n# Body: Explain *what* and *why* (not *how*). Include task ID (Jira issue).\n# Wrap at 72 chars. ################################## which is here: #\n\n\n# At the end: Include Co-authored-by for all contributors. \n# Include at least one empty line before it. Format: \n# Co-authored-by: name <user@users.noreply.github.com>\n#\n# How to Write a Git Commit Message:\n# https://chris.beams.io/posts/git-commit/\n#\n# 1.Separate subject from body with a blank line\n# 2. Limit the subject line to 50 characters\n# 3. Capitalize the subject line\n# 4. Do not end the subject line with a period\n# 5. Use the imperative mood in the subject line\n# 6. Wrap the body at 72 characters\n# 7. Use the body to explain what and why vs. how\n" > ~/.gitmessage && git config --global commit.template ~/.gitmessage
```

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@ALiwoto](https://avatars.githubusercontent.com/u/70187458?s=80&v=4)](https://gist.github.com/ALiwoto)


Copy link

### **[ALiwoto](https://gist.github.com/ALiwoto)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026740\#gistcomment-4026740)

Thanks for the template.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@ryankearney](https://avatars.githubusercontent.com/u/116006?s=80&v=4)](https://gist.github.com/ryankearney)


Copy link

### **[ryankearney](https://gist.github.com/ryankearney)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026752\#gistcomment-4026752)

```
$ echo -n "# No more than 50 chars. #### 50 chars is here: #" | wc -m
      49
$ echo -n "# Wrap at 72 chars. ################################## which is here: #" | wc -m
      71
```

Close, but off by 1.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@drjasonharrison](https://avatars.githubusercontent.com/u/6044603?s=80&v=4)](https://gist.github.com/drjasonharrison)


Copy link

### **[drjasonharrison](https://gist.github.com/drjasonharrison)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026771\#gistcomment-4026771)

[@ryankearney](https://github.com/ryankearney) as noted before the limits are the last valid column, not the first invalid column.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@rjray](https://avatars.githubusercontent.com/u/48159?s=80&v=4)](https://gist.github.com/rjray)


Copy link

### **[rjray](https://gist.github.com/rjray)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026775\#gistcomment-4026775)

Great template, I plan to use it (or a close simile) going forward!

One edit, though... this line:

`# 1.Separate subject from body with a blank line`

should maybe have a space between the number and the "S"?

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@joelparkerhenderson](https://avatars.githubusercontent.com/u/27145?s=80&v=4)](https://gist.github.com/joelparkerhenderson)


Copy link

### **[joelparkerhenderson](https://gist.github.com/joelparkerhenderson)**     commented    [on Jan 12, 2022Jan 12, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026777\#gistcomment-4026777)

Here's our similar git commit template with extras that can help with tag categories, keyword searches, and issue tracker links:

[https://github.com/joelparkerhenderson/git-commit-template](https://github.com/joelparkerhenderson/git-commit-template)

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@ryankearney](https://avatars.githubusercontent.com/u/116006?s=80&v=4)](https://gist.github.com/ryankearney)


Copy link

### **[ryankearney](https://gist.github.com/ryankearney)**     commented    [on Jan 12, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4026948\#gistcomment-4026948)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[@drjasonharrison](https://github.com/drjasonharrison) your explanation did not make sense, since “at the # mark” would be 49 and 71 characters respectively, not 50 and 72.

Let’s say we wanted the limit to be 10. If we marked it with 10-1 it would look like this.

```
###TEST##
1234567890
```

Note the 10th character is beyond the end of the 9th character (#)

A proper guard would include all 10 characters.

```
###TEST###
1234567890
```

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@DervishD](https://avatars.githubusercontent.com/u/12148736?s=80&v=4)](https://gist.github.com/DervishD)


Copy link

### **[DervishD](https://gist.github.com/DervishD)**     commented    [on Jan 13, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4027027\#gistcomment-4027027)

[@ryankearney](https://github.com/ryankearney) look a the second message on this thread, just after mine. [@lisawolderiksen](https://github.com/lisawolderiksen) explains why she chose to do that, it's not a matter of correctness, but a matter of preference.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@marcelarie](https://avatars.githubusercontent.com/u/62728887?s=80&v=4)](https://gist.github.com/marcelarie)


Copy link

### **[marcelarie](https://gist.github.com/marcelarie)**     commented    [on Jan 13, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4027067\#gistcomment-4027067)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

Thanks for the template. On your colleague article he uses the last part of the commit for the tracking of other issues.

The `Resolves: #123` at my work are `Fix: #123`, but we put it in the title, like: **Fix: #123 - Title: Summary, imperative, ...**

Do you consider that a bad practice?

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@mihaigalos](https://avatars.githubusercontent.com/u/16443090?s=80&v=4)](https://gist.github.com/mihaigalos)


Copy link

### **[mihaigalos](https://gist.github.com/mihaigalos)**     commented    [on Jan 13, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4027136\#gistcomment-4027136)

Suggest lint of commit message for meeting rules (1st letter uppercase, no full-stop at end, etc.). Nice work!

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@gwd](https://avatars.githubusercontent.com/u/1247773?s=80&v=4)](https://gist.github.com/gwd)


Copy link

### **[gwd](https://gist.github.com/gwd)**     commented    [on Jan 13, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4027377\#gistcomment-4027377)

This is mostly about the style; the content description is pretty vague.

My internal "template" for a good commit message looks like this:

1. Explain what's the current situation
2. Explain why that's a problem
3. Explain how this patch fixes the problem
4. Anything else needed to understand the patch (e.g,. alternate solutions, links to issue numbers, &c)

Then the job of a reviewer is simply verification: Is #1 true? Is the problem in #2 actually a problem? Does #3 fix the problem, and does the patch actually do #3?

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@lisawolderiksen](https://avatars.githubusercontent.com/u/35797988?s=80&v=4)](https://gist.github.com/lisawolderiksen)


Copy link

Author

### **[lisawolderiksen](https://gist.github.com/lisawolderiksen)**     commented    [on Jan 13, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4027889\#gistcomment-4027889)

Thanks, everyone, for the comments and feedback!

[@drjasonharrison](https://github.com/drjasonharrison) and [@rjray](https://github.com/rjray): Yes, you both are correct. There was a missing space in the first item of the numbered list. I've corrected it now. Thanks!

[@manav148](https://github.com/manav148) and [@rany2](https://github.com/rany2): Thanks for suggesting commands for Mac and "anywhere" to create the gitmessage file and configure Git to use it. Great stuff. 😄

[@ryankearney](https://github.com/ryankearney): You are absolutely correct about the character limits of 50/72 for title/message strictly speaking being off by one. [@DervishD](https://github.com/DervishD) is also correct; I prefer it that way and I'm not very concerned about breaking a line a bit early because of it. 😇 I'll probably update the gist so the last # is **at** the last char mark, since this will probably make more sense to most people. (My own .gitmessage in my dotfile-repo remains unchanged, however 😉)

[@joelparkerhenderson](https://github.com/joelparkerhenderson): Thanks for the link to your commit template! Yours _is_ actually a template, since it includes text that will be part of the commit message. I think the prompts of "Why: " and "How:" are especially useful.

[@marcelarie](https://github.com/marcelarie): Good question. I think one major benefit of including the issue tracker ID in the title is that it makes it a lot easier to see when looking at git log outputs + it possibly simplifies some kind of automation based on commit titles. I wouldn't put it there myself, as the issue tracker IDs are more "secondary" info for the work I usually do. The issue tracking stuff is more temporary than the code itself so we choose to include it at the end of the message. Another problem for me would be the 50 characters limit, I don't think I would be able to fit all I wanted to say after `myteam-1234:`. Those 50 chars are few and precious. 😄

[@mihaigalos](https://github.com/mihaigalos): I like the suggestion of linting the commit messages - do you have any suggestion on how to do it in practice?

[@gwd](https://github.com/gwd): Those are excellent questions to answer in the commit message. Especially the focus on the current situation (which in most cases I think are part of the "why do we do this", but can be easily forgotten in the description of "why").

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@mihaigalos](https://avatars.githubusercontent.com/u/16443090?s=80&v=4)](https://gist.github.com/mihaigalos)


Copy link

### **[mihaigalos](https://gist.github.com/mihaigalos)**     commented    [on Jan 13, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4027898\#gistcomment-4027898)

[@lisawolderiksen](https://github.com/lisawolderiksen), check out [commitlint](https://github.com/conventional-changelog/commitlint).

For more generic linting (not only limited to the commit message), see [pre-commit](https://github.com/pre-commit/pre-commit).

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@lisawolderiksen](https://avatars.githubusercontent.com/u/35797988?s=80&v=4)](https://gist.github.com/lisawolderiksen)


Copy link

Author

### **[lisawolderiksen](https://gist.github.com/lisawolderiksen)**     commented    [on Jan 13, 2022Jan 13, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4027941\#gistcomment-4027941)

[@mihaigalos](https://github.com/mihaigalos) Thanks!

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@BenjaminEngeset](https://avatars.githubusercontent.com/u/99641908?s=80&v=4)](https://gist.github.com/BenjaminEngeset)


Copy link

### **[BenjaminEngeset](https://gist.github.com/BenjaminEngeset)**     commented    [on Mar 25, 2022Mar 25, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4110330\#gistcomment-4110330)

[@lisawolderiksen](https://github.com/lisawolderiksen)

Thank you for sharing! We are in a situation where commits and pull requests are spammed with lacking information. This is truly helpful!

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@jpluimers](https://avatars.githubusercontent.com/u/2033367?s=80&v=4)](https://gist.github.com/jpluimers)


Copy link

### **[jpluimers](https://gist.github.com/jpluimers)**     commented    [on Apr 18, 2022Apr 18, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4136302\#gistcomment-4136302)

Thanks for the great work, not just the template: also separating most of the documentation out to a markdown file so the actual template still is manageable in the editor.

A few ideas for improvement:

- add an additional file `.gitmessage` containing the actual template
- add additional files for common shells (`sh` on Linux/BSD/... and `cmd` or `PowerShell` on Windows) that generate the `.gitmessage` file (I can help with the Windows side)
- add a few more fields in the template like (indirectly via [@mihaigalos](https://github.com/mihaigalos)) [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/) and what [@joelparkerhenderson](https://github.com/joelparkerhenderson) has in their template (for instance tracking, see, sponsored by)

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@devdrops](https://avatars.githubusercontent.com/u/1259313?s=80&v=4)](https://gist.github.com/devdrops)


Copy link

### **[devdrops](https://gist.github.com/devdrops)**     commented    [on Nov 9, 2022Nov 9, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4363751\#gistcomment-4363751)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

Thank you very much [@lisawolderiksen](https://github.com/lisawolderiksen)! Just FYI, the original site reference for this template has changed to [https://cbea.ms/git-commit/](https://cbea.ms/git-commit/) (though the old link still redirects to it 😉)

Also: it's worth mentioning that, in order for this template to work as expected, the `commit.cleanup` config must be `strip`. Otherwise, the comments will not be ignored.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@lisawolderiksen](https://avatars.githubusercontent.com/u/35797988?s=80&v=4)](https://gist.github.com/lisawolderiksen)


Copy link

Author

### **[lisawolderiksen](https://gist.github.com/lisawolderiksen)**     commented    [on Nov 21, 2022Nov 21, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4376385\#gistcomment-4376385)

> Thank you very much [@lisawolderiksen](https://github.com/lisawolderiksen)! Just FYI, the original site reference for this template has changed to [https://cbea.ms/git-commit/](https://cbea.ms/git-commit/) (though the old link still redirects to it 😉)
>
> Also: it's worth mentioning that, in order for this template to work as expected, the `commit.cleanup` config must be `strip`. Otherwise, the comments will not be ignored.

Thanks for the heads up, [@devdrops](https://github.com/devdrops) ! Fixed the URLs now. :)

Regarding the `commit.cleanup` config: Ah. Did not know that! Since the default is `strip`, I'll hope that people who've changed it themselves will know this and make templates that fit their setup. 😇 But I'll include a sentence or two about it to be sure. :)

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[![@joelparkerhenderson](https://avatars.githubusercontent.com/u/27145?s=80&v=4)](https://gist.github.com/joelparkerhenderson)


Copy link

### **[joelparkerhenderson](https://gist.github.com/joelparkerhenderson)**     commented    [on Nov 21, 2022Nov 22, 2022](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733?permalink_comment_id=4377210\#gistcomment-4377210)

Thanks [@devdrops](https://github.com/devdrops). I didn't know that either. I've added a usage note about strip to my template at [https://github.com/joelparkerhenderson/git-commit-template](https://github.com/joelparkerhenderson/git-commit-template)

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733).

[Sign up for free](https://gist.github.com/join?source=comment-gist) **to join this conversation on GitHub**.
Already have an account?
[Sign in to comment](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Flisawolderiksen%2Fa7b99d94c92c6671181611be1641c733)

## Footer

[GitHub Homepage](https://github.com/)
© 2026 GitHub, Inc.


### Footer navigation

- [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
- [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
- [Security](https://github.com/security)
- [Status](https://www.githubstatus.com/)
- [Community](https://github.community/)
- [Docs](https://docs.github.com/)
- [Contact](https://support.github.com/?tags=dotcom-footer)
- Manage cookies

- Do not share my personal information


You can’t perform that action at this time.