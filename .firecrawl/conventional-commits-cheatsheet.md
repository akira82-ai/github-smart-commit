[Skip to content](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#start-of-content)

[Gist Homepage ](https://gist.github.com/)

Search Gists

Search Gists

[All gists](https://gist.github.com/discover) [Back to GitHub](https://github.com/) [Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fqoomon%2F5dfcdf8eec66a051ecd85625518cfd13) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fqoomon%2F5dfcdf8eec66a051ecd85625518cfd13&source=header-gist)

[Gist Homepage ](https://gist.github.com/)

[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fqoomon%2F5dfcdf8eec66a051ecd85625518cfd13) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fqoomon%2F5dfcdf8eec66a051ecd85625518cfd13&source=header-gist)

You signed in with another tab or window. [Reload](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) to refresh your session.You signed out in another tab or window. [Reload](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) to refresh your session.You switched accounts on another tab or window. [Reload](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) to refresh your session.Dismiss alert

{{ message }}

Instantly share code, notes, and snippets.


[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=64&v=4)](https://gist.github.com/qoomon)

# [qoomon](https://gist.github.com/qoomon)/ **[conventional-commits-cheatsheet.md](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)**

Last active
47 minutes agoMarch 10, 2026 07:17

Show Gist options

- [Download ZIP](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13/archive/15c0b97925b1637559cf4d0d7c937dfe084c37b7.zip)

- [Star4,359(4,359)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fqoomon%2F5dfcdf8eec66a051ecd85625518cfd13) You must be signed in to star a gist
- [Fork620(620)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fqoomon%2F5dfcdf8eec66a051ecd85625518cfd13) You must be signed in to fork a gist

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

Clone this repository at &lt;script src=&quot;https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13.js&quot;&gt;&lt;/script&gt;

- Save qoomon/5dfcdf8eec66a051ecd85625518cfd13 to your computer and use it in GitHub Desktop.

[Code](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) [Revisions\\
184](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13/revisions) [Stars\\
4,352](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13/stargazers) [Forks\\
620](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13/forks)

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

Clone this repository at &lt;script src=&quot;https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13.js&quot;&gt;&lt;/script&gt;

Save qoomon/5dfcdf8eec66a051ecd85625518cfd13 to your computer and use it in GitHub Desktop.

[Download ZIP](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13/archive/15c0b97925b1637559cf4d0d7c937dfe084c37b7.zip)

Conventional Commits Cheatsheet


[Raw](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13/raw/15c0b97925b1637559cf4d0d7c937dfe084c37b7/conventional-commits-cheatsheet.md)

[**conventional-commits-cheatsheet.md**](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#file-conventional-commits-cheatsheet-md)

# Conventional Commit Messages [![starline](https://camo.githubusercontent.com/20d61e65c4b92a13f623b4580189ac41bc2d74bfc25214380a532beba52c4430/68747470733a2f2f737461726c696e65732e716f6f2e6d6f6e737465722f6173736574732f716f6f6d6f6e2f35646663646638656563363661303531656364383536323535313863666431334067697374)](https://github.com/qoomon/starline)

[Permalink: Conventional Commit Messages ](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#conventional-commit-messages-)

See how [a minor change](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#examples) to your commit message style can make a difference.

```
git commit -m"<type>(<optional scope>): <description>" \
  -m"<optional body>" \
  -m"<optional footer>"
```

Note

This cheatsheet is opinionated, however it does not violate the specification of [conventional commits](https://www.conventionalcommits.org/)

Tip

Take a look at **[git-conventional-commits](https://github.com/qoomon/git-conventional-commits)** ; a CLI util to ensure these conventions, determine version and generate changelogs.

## Commit Message Formats

[Permalink: Commit Message Formats](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#commit-message-formats)

### General Commit

[Permalink: General Commit](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#general-commit)

```
<type>(<optional scope>): <description>
empty line as separator
<optional body>
empty line as separator
<optional footer>
```

### Initial Commit

[Permalink: Initial Commit](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#initial-commit)

```
chore: init
```

### Merge Commit

[Permalink: Merge Commit](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#merge-commit)

```
Merge branch '<branch name>'
```

Follows default git merge message

### Revert Commit

[Permalink: Revert Commit](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#revert-commit)

```
Revert "<reverted commit subject line>"
```

Follows default git revert message

### Types

[Permalink: Types](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#types)

- Changes relevant to the API or UI:
  - `feat` Commits that add, adjust or remove a new feature to the API or UI
  - `fix` Commits that fix an API or UI bug of a preceded `feat` commit
- `refactor`Commits that rewrite or restructure code without altering API or UI behavior

  - `perf` Commits are special type of `refactor` commits that specifically improve performance
- `style` Commits that address code style (e.g., white-space, formatting, missing semi-colons) and do not affect application behavior
- `test` Commits that add missing tests or correct existing ones
- `docs` Commits that exclusively affect documentation
- `build` Commits that affect build-related components such as build tools, dependencies, project version, ...
- `ops` Commits that affect operational aspects like infrastructure (IaC), deployment scripts, CI/CD pipelines, backups, monitoring, or recovery procedures, ...
- `chore` Commits that represent tasks like initial commit, modifying `.gitignore`, ...

### Scopes

[Permalink: Scopes](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#scopes)

The `scope` provides additional contextual information.

- The scope is an **optional** part
- Allowed scopes vary and are typically defined by the specific project
- **Do not** use issue identifiers as scopes

### Breaking Changes Indicator

[Permalink: Breaking Changes Indicator](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#breaking-changes-indicator)

- A commit that introduce breaking changes **must** be indicated by an `!` before the `:` in the subject line e.g. `feat(api)!: remove status endpoint`
- Breaking changes **should** be described in the [commit footer section](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#footer), if the [commit description](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#description) isn't sufficiently informative

### Description

[Permalink: Description](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#description)

The `description` contains a concise description of the change.

- The description is a **mandatory** part
- Use the imperative, present tense: "change" not "changed" nor "changes"
  - Think of `This commit will...` or `This commit should...`
- **Do not** capitalize the first letter
- **Do not** end the description with a period (`.`)
- In case of breaking changes also see [breaking changes indicator](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#breaking-changes-indicator)

### Body

[Permalink: Body](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#body)

The `body` should include the motivation for the change and contrast this with previous behavior.

- The body is an **optional** part
- Use the imperative, present tense: "change" not "changed" nor "changes"

### Footer

[Permalink: Footer](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#footer)

The `footer` should contain issue references and informations about **Breaking Changes**

- The footer is an **optional** part, except if the commit introduce breaking changes
- _Optionally_ reference issue identifiers (e.g., `Closes #123`, `Fixes JIRA-456`)
- **Breaking Changes** **must** start with the word `BREAKING CHANGE:`
  - For a single line description just add a space after `BREAKING CHANGE:`
  - For a multi line description add two new lines after `BREAKING CHANGE:`

### Versioning

[Permalink: Versioning](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#versioning)

- **If**your next release contains commit with...

  - **Breaking Changes** incremented the **major version**
  - **API relevant changes** (`feat` or `fix`) incremented the **minor version**
- **Else** increment the **patch version**

### Examples

[Permalink: Examples](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#examples)

- ```
feat: add email notifications on new direct messages
```

- ```
feat(shopping cart): add the amazing button
```

- ```
feat!: remove ticket list endpoint

refers to JIRA-1337

BREAKING CHANGE: ticket endpoints no longer supports list all entities.
```

- ```
fix(shopping-cart): prevent order an empty shopping cart
```

- ```
fix(api): fix wrong calculation of request body checksum
```

- ```
fix: add missing parameter to service call

The error occurred due to <reasons>.
```

- ```
perf: decrease memory footprint for determine unique visitors by using HyperLogLog
```

- ```
build: update dependencies
```

- ```
build(release): bump version to 1.0.0
```

- ```
refactor: implement fibonacci number calculation as recursion
```

- ```
style: remove empty line
```


* * *

## Git Hook Scripts to ensure commit message header format

[Permalink: Git Hook Scripts to ensure commit message header format](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#git-hook-scripts-to-ensure-commit-message-header-format)

Click to expand

### commit-msg Hook (local)

[Permalink: commit-msg Hook (local)](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#commit-msg-hook-local)

- Create a commit-msg hook using [git-conventional-commits cli](https://github.com/qoomon/git-conventional-commits?tab=readme-ov-file#automatically-validate-commit-message-convention-before-commit)

### pre-receive Hook (server side)

[Permalink: pre-receive Hook (server side)](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#pre-receive-hook-server-side)

- create following file in your repository folder `.git/hooks/pre-receive`


```
#!/usr/bin/env bash

# Pre-receive hook that will block commits with messages that do not follow regex rule

commit_msg_type_regex='feat|fix|refactor|style|test|docs|build'
commit_msg_scope_regex='.{1,20}'
commit_msg_description_regex='.{1,100}'
commit_msg_regex="^(${commit_msg_type_regex})(\(${commit_msg_scope_regex}\))?: (${commit_msg_description_regex})\$"
merge_msg_regex="^Merge branch '.+'\$"

zero_commit="0000000000000000000000000000000000000000"

# Do not traverse over commits that are already in the repository
excludeExisting="--not --all"

error=""
while read oldrev newrev refname; do
    # branch or tag get deleted
    if [ "$newrev" = "$zero_commit" ]; then
      continue
    fi

    # Check for new branch or tag
    if [ "$oldrev" = "$zero_commit" ]; then
      rev_span=`git rev-list $newrev $excludeExisting`
    else
      rev_span=`git rev-list $oldrev..$newrev $excludeExisting`
    fi

    for commit in $rev_span; do
      commit_msg_header=$(git show -s --format=%s $commit)
      if ! [[ "$commit_msg_header" =~ (${commit_msg_regex})|(${merge_msg_regex}) ]]; then
        echo "$commit" >&2
        echo "ERROR: Invalid commit message format" >&2
        echo "$commit_msg_header" >&2
        error="true"
      fi
    done
done

if [ -n "$error" ]; then
    exit 1
fi
```


- ⚠ make `.git/hooks/pre-receive` executable (unix: `chmod +x '.git/hooks/pre-receive'`)

* * *

## References

[Permalink: References](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#references)

- [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/)
- [https://github.com/angular/angular/blob/master/CONTRIBUTING.md](https://github.com/angular/angular/blob/master/CONTRIBUTING.md)
- [http://karma-runner.github.io/1.0/dev/git-commit-msg.html](http://karma-runner.github.io/1.0/dev/git-commit-msg.html)

- [https://github.com/github/platform-samples/tree/master/pre-receive-hooks](https://github.com/github/platform-samples/tree/master/pre-receive-hooks)
- [https://github.community/t5/GitHub-Enterprise-Best-Practices/Using-pre-receive-hooks-in-GitHub-Enterprise/ba-p/13863](https://github.community/t5/GitHub-Enterprise-Best-Practices/Using-pre-receive-hooks-in-GitHub-Enterprise/ba-p/13863)

Load earlier comments...

[![@RobSmyth](https://avatars.githubusercontent.com/u/6183736?s=80&v=4)](https://gist.github.com/RobSmyth)


Copy link

### **[RobSmyth](https://gist.github.com/RobSmyth)**     commented    [on Nov 30, 2025Dec 1, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5886347\#gistcomment-5886347)

I do use `chore` and `build`. I would not like to see `misc` as an option on a project I was on as it would rapidly become the default for anybody who does not want to bother with the process (I have done this). I've never used "ops" but if the project had an clear separation of build and ops then I could see its use but would need to be convinced it added value.

I like the descriptions given [here](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

For example, provided that the commit **does not change ANY product behaviour** I use:

- `build`
  - If adding a new build tool/service like Github, TeamCity kotlin, Grunt (never actually used Grunt).
  - If changing build to fail automatically and not publish a build, if any automated test fails on the build (although that should be the case anyway).
  - If automating a previously manual process like, radically, automating the versioning :-).
- `chore`
  - If removing files that are no longer used like a readme file in a subfolder.
  - If not removing code files that are visible in an IDE as I would call that refactoring as it improves the readability of the code.

[@pycaw](https://github.com/pycaw): `chore` seems to me to be communicating intent like "just cleaning up (but not refactoring) ... nothing to see here". But I agree that `chore` is vague enough to be abused. Hmmm ... you make me think I ought to stop using it :-).

[@GabenGar](https://github.com/GabenGar): I would not use `chore` for dependency updates as they can, even if not intended, change product behaviour. If updating for a security issue then it is a bug fix as I recon security is a feature, a fix # would allow the fix to be recorded for next release (SBOM). If updating to avoid a future build failure then using `build` would be more useful to reflect that intent.

In any case conventional commits are only really interested in `feat`, `fix`, and `BREAKING CHANGE` / `!` commits anyway. It allows for use of other types but IMO any addtional types must service a purpose and not just a nice to have. I like to force a type on every commit so that `feat` and `fix` commits are not forgotten.

I think a long list of predfined types is useful to help others define there process but not as a predefined list in the tool as many are not relevant to a particular team's way of working. A team may want to enforce types that are used via a configurable white list. Or .. if the types are hard coded allow for users to define a type black list so that enforcement of useful types is enforced. Hey, maybe allow for a custom error reponse to include the team's policy along with why the rejected type is not used.

### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Dec 1, 2025Dec 1, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5886652\#gistcomment-5886652)

I agree `chore` is a complicated one. I just got used to it. Do you have a better wording in mind (incl. description) ?

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@RobSmyth](https://avatars.githubusercontent.com/u/6183736?s=80&v=4)](https://gist.github.com/RobSmyth)


Copy link

### **[RobSmyth](https://gist.github.com/RobSmyth)**     commented    [on Dec 1, 2025Dec 1, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5886877\#gistcomment-5886877)

> I agree `chore` is a complicated one. I just got used to it. Do you have a better wording in mind (incl. description) ?

I think a team should only use types that are of value to the team. `feat`, `fix`, and `BREAKING CHANGE` / `!` are the only ones that impact version so maybe a team would choose no other types or just "no\_ver\_change" (if underscore is alowed).

I'm not sure I would say `chore` is "complicated". More like I'm reevaluating if it provides value for the work I'm doing. If you have a need for a type then that need (problem) gives you the description and that will lead to the name. The various published practices show solutions others have found useful for their problems so they good starting point but no match your processes.

e.g: I like "refactor" as I value understanding that the commiter did not intend to changes any product behaviour.

- Useful on a PR as I can then look if the change can change behavior (\_Well ... unless you get the "I fixed it by refactoring the code" LOL).
- Useful when browsing history to, on first pass, skip over some commits as no change intended and also to understand huge code changes when looking at differences.

But a lot of developers do not do separate refactoring commits so for them dead useless.

Wild thoughts as examples of how a need may result in a type:

> #1 - When I'm doing TDD coding each time a test passes I commit. Great as the build system will run all tests and let me know if there is a failure. When doing this I usually commit every 5 to 15 minutes so lots of commits (I may before a PR squash these commits). So maybe a type of "tdd", "incremental", or no type at all would be useful here as most commits add working code that is probably not used by anything other than the unit tests (maybe an odd component test) .... dunno.

> #2 - On completing a functional change but leaving it hidden behind a switch for limited customer testing and later full release ... what would that be?

A type name here is a solution. Let problems lead to solutions. I have been looking for years for problems that could be solved by some great solutions I have. :-)

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@pycaw](https://avatars.githubusercontent.com/u/163207817?s=80&v=4)](https://gist.github.com/pycaw)


Copy link

### **[pycaw](https://gist.github.com/pycaw)**     commented    [on Dec 1, 2025Dec 1, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5886958\#gistcomment-5886958)

> I like "refactor" as I value understanding that the commiter did not intend to changes any product behaviour.

I only use refactor if the behavior of the application hasn't really changed. And in connection to this, I am an outlier in that I use `behavior` tag, sometimes with `!`, to not sell the modification as a "mere harmless refactor" but as what it is: a behavioral change -- not a fix, not a feature. It can often have meaning to the user as well, especially of course if it's breaking.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@RobSmyth](https://avatars.githubusercontent.com/u/6183736?s=80&v=4)](https://gist.github.com/RobSmyth)


Copy link

### **[RobSmyth](https://gist.github.com/RobSmyth)**     commented    [on Dec 1, 2025Dec 2, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5887906\#gistcomment-5887906)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

> ... I am an outlier in that I use `behavior` tag, sometimes with `!`, to not sell the modification as a "mere harmless refactor" but as what it is: a behavioral change -- not a fix, not a feature. It can often have meaning to the user as well, especially of course if it's breaking.

_"behavioral change"_ \- Is the context here team behavior (as refactoring cannot, by definition, change code behaviour)? If so ... I like the sound of that. Nice.

I want to understand how your using "!" and your intent/context better ...

`Q1`: Isnt refactoring harmless by definition?

`Q2`: How are you using "!"? Conventional commits define ! after the type as indicating an incompatible API change and hence will bump the major version number? ( [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/))?

Also, if the context is team behavioral change, would that only apply if:

- `Q3.1`: Refactoring is abnormal for the team or the team?
- `Q3.2:` Or the team is not skilled with refactoring patterns (hence risk)?

Sorry for all the question but I'm really interested.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 2, 2025Dec 2, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5888913\#gistcomment-5888913)

> I am an outlier in that I use `behavior` tag, sometimes with `!`, to not sell the modification as a "mere harmless refactor" but as what it is: a behavioral change -- not a fix, not a feature.

A behaviour change would, by definition, surely be a new feature? Otherwise why make the change? Can you give an example?

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@pycaw](https://avatars.githubusercontent.com/u/163207817?s=80&v=4)](https://gist.github.com/pycaw)


Copy link

### **[pycaw](https://gist.github.com/pycaw)**     commented    [on Dec 2, 2025Dec 2, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5889411\#gistcomment-5889411)

> > I am an outlier in that I use `behavior` tag, sometimes with `!`, to not sell the modification as a "mere harmless refactor" but as what it is: a behavioral change -- not a fix, not a feature.
>
> A behaviour change would, by definition, surely be a new feature? Otherwise why make the change? Can you give an example?

I don't see it that way, many other repos I think don't either if you consider how they categorize changes by the new-changed-fixed methodology. But speaking for myself, a change is only considered a feature if it actually brings something new to the table; if it's a tweak, a removal or a replacement of an existing feature, of it's just too tiny, it doesn't.

Few examples from a changelog of a project of mine:

- behavior(execute): disable logs with `... -- --help`
- behavior!: (CLI) config files now have .yaml extension instead of .yml
- behavior!: no more -D/--auto-dir-name
- behavior: slightly reworked config upgrade mechanics
- behavior(rip): not compressing logs anymore

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@RobSmyth](https://avatars.githubusercontent.com/u/6183736?s=80&v=4)](https://gist.github.com/RobSmyth)


Copy link

### **[RobSmyth](https://gist.github.com/RobSmyth)**     commented    [on Dec 2, 2025Dec 3, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5889675\#gistcomment-5889675)

Hi [@pycaw](https://github.com/pycaw),

You said:

> many other repos I think don't either if you consider how they categorize changes by the new-changed-fixed methodology

Yea there are many many ways peeple like to stucture their commit messages. Not so many teams use the [convention commit (CC)](https://www.conventionalcommits.org/en/v1.0.0/) standard. Some versioning tool authors say their tool is a "opinionated" variation of the CC standard (and tell you how they vary from CC) and that is fine. If your doing a variation of CC, that is fine, but say so to avoid confusion and allow people to understand version numbers.

My comments here are about CC as this discussion's title is `Conventional Commits Cheatsheet`.

In a CC context, anything that changes the product's public behaviour is either a fix or a feature. Ask the question: _Does an end user use it or needs to know about the change?_

`behavior` seems vague in a CC context. I had thought you were talking about team behaviour, sorry.

To use the commit message examples you gave:

- behavior(execute): disable logs with ... -- --help

> If command line you describe is used by users then it is part of the product's public behaviour and the change is either a bug fix or a feature. If the command is line is not used or exposed (e.g: documented) to any users then it is not a feature or fix.

- behavior!: (CLI) config files now have .yaml extension instead of .yml

> If users use this config file then it is a breaking change (hence the "!"). If somebody complained that it ought to have been `.yaml` (maybe they asked for `.yaml` inthe first place) then this is a fix.

> Note: About the use of the `!` symbol here. CC says: " _BREAKING CHANGE: a commit that has a footer BREAKING CHANGE:, or appends a `!` after the type/scope, introduces a breaking API change (correlating with [MAJOR](http://semver.org/#summary) in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type._". So this `behavior!` flags to users a breaking change and the major version number will bump.

- behavior!: no more -D/--auto-dir-name

> Not sure about `behavior` as I do not have a definition and I do not know why the change is being made. Looks fine to me. Sounds like a feature has been dropped and users need to be notified of the breaking change.

- behavior: slightly reworked config upgrade mechanics

> I do not know what "mechanics" is so I cannot comment on this one.

- behavior(rip): not compressing logs anymore

> The question is _why_ and if users need to know. If users were decompressing log files and this makes life easier then it is a feature " _hey users you no longer need to decompress logs_". If it was doen to improve performance then question is if anybody complained about the performance. A fix if the was a real problem or a new feature (better performance) **if the user may notice**.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@pycaw](https://avatars.githubusercontent.com/u/163207817?s=80&v=4)](https://gist.github.com/pycaw)


Copy link

### **[pycaw](https://gist.github.com/pycaw)**     commented    [on Dec 3, 2025Dec 3, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5889942\#gistcomment-5889942)

[@RobSmyth](https://github.com/RobSmyth)

> Hi [@pycaw](https://github.com/pycaw),
>
> You said:
>
> > many other repos I think don't either if you consider how they categorize changes by the new-changed-fixed methodology
>
> Yea there are many many ways peeple like to stucture their commit messages. Not so many teams use the [convention commit (CC)](https://www.conventionalcommits.org/en/v1.0.0/) standard. Some versioning tool authors say their tool is a "opinionated" variation of the CC standard (and tell you how they vary from CC) and that is fine. If your doing a variation of CC, that is fine, but say so to avoid confusion and allow people to understand version numbers.
>
> My comments here are about CC as this discussion's title is `Conventional Commits Cheatsheet`.
>
> In a CC context, anything that changes the product's public behaviour is either a fix or a feature. Ask the question: _Does an end user use it or needs to know about the change?_
>
> `behavior` seems vague in a CC context. I had thought you were talking about team behaviour, sorry.
>
> To use the commit message examples you gave:
>
> ```
> * behavior(execute): disable logs with ... -- --help
> ```
>
> > If command line you describe is used by users then it is part of the product's public behaviour and the change is either a bug fix or a feature. If the command is line is not used or exposed (e.g: documented) to any users then it is not a feature or fix.
>
> ```
> * behavior!: (CLI) config files now have .yaml extension instead of .yml
> ```
>
> > If users use this config file then it is a breaking change (hence the "!"). If somebody complained that it ought to have been `.yaml` (maybe they asked for `.yaml` inthe first place) then this is a fix.
>
> > Note: About the use of the `!` symbol here. CC says: " _BREAKING CHANGE: a commit that has a footer BREAKING CHANGE:, or appends a `!` after the type/scope, introduces a breaking API change (correlating with [MAJOR](http://semver.org/#summary) in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type._". So this `behavior!` flags to users a breaking change and the major version number will bump.
>
> ```
> * behavior!: no more -D/--auto-dir-name
> ```
>
> > Not sure about `behavior` as I do not have a definition and I do not know why the change is being made. Looks fine to me. Sounds like a feature has been dropped and users need to be notified of the breaking change.
>
> ```
> * behavior: slightly reworked config upgrade mechanics
> ```
>
> > I do not know what "mechanics" is so I cannot comment on this one.
>
> ```
> * behavior(rip): not compressing logs anymore
> ```
>
> > The question is _why_ and if users need to know. If users were decompressing log files and this makes life easier then it is a feature " _hey users you no longer need to decompress logs_". If it was doen to improve performance then question is if anybody complained about the performance. A fix if the was a real problem or a new feature (better performance) **if the user may notice**.

It looks like to me your answer partly validated this technique, and partly brought in ambiguous criteria.

For example, the .yml vs .yaml change, maybe it was the janitor in the office dungeons that whispered to the dev that .yaml is the way to go. Let's assume this API has not been broadly exposed yet so making the change is relatively okay (still `!`). Why would one need to grind themselves over to coerce it into a feature or a fix when it is neither?

Regarding the log compression one, maybe for 1/3 of the users it is a feature because they don't have to decompress it themselves, for 1/3 it is a an "anti-feature" because they preferred as it was, and for 1/3 it is an unimportant behavioral change. Basing the change's categorization on why the modification was made isn't generally feasible with many projects, but even you can do so, miscommunication can occur due to feat/fix coercion which is uncalled for in the first place in my opinion.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 3, 2025Dec 3, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5890561\#gistcomment-5890561)

> behavior(execute): disable logs with ... -- --help

I see what you mean, you're changing how the system operates, hence "behaviour". However I wonder if it would fit in chore?

> behavior!: (CLI) config files now have .yaml extension instead of .yml

Remember that commit messages are supposed to be written in the imperative, present tense (which is the git standard). So this should be: "rename all .yml file extensions to .yaml". Again it seems like a chore?

> behavior: slightly reworked config upgrade mechanics

This seems like the definition of a refactor, no?

> behavior(rip): not compressing logs anymore

Disabling compression would be a feature change, IMO. It directly affects the users of the system: you're now serving the logs in an uncompressed format.

Just my perspective.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@pycaw](https://avatars.githubusercontent.com/u/163207817?s=80&v=4)](https://gist.github.com/pycaw)


Copy link

### **[pycaw](https://gist.github.com/pycaw)**     commented    [on Dec 3, 2025Dec 3, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5890759\#gistcomment-5890759)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

> > behavior(execute): disable logs with ... -- --help
>
> I see what you mean, you're changing how the system operates, hence "behaviour". However I wonder if it would fit in chore?

Users are interested in logs. If they had appeared when they shouldn't, and now they don't, they should also be notified. This one borders the fix tag btw.

> > behavior!: (CLI) config files now have .yaml extension instead of .yml
>
> Remember that commit messages are supposed to be written in the imperative, present tense (which is the git standard). So this should be: "rename all .yml file extensions to .yaml". Again it seems like a chore?

Users themselves manage such config files, it is a primary feature. You are right I suppose about imperative present tense , I have been unable to get myself to adopt it for a long time for reasons beyond me.

> > behavior: slightly reworked config upgrade mechanics
>
> This seems like the definition of a refactor, no?

My usage of behavior sort of begins where refactor ends. These changes were very much visible from the outside as users deal with configs themselves. But, with the behavior tag under my tool belt, I go beyond and apply the behavior tag for changes that are well below what's visible from outside. This allows me to have a smaller scope for refactor so that they are applied to changes where not even the internal API of the particular module had changed. "refactor" is overused imo.

> > behavior(rip): not compressing logs anymore
>
> Disabling compression would be a feature change, IMO. It directly affects the users of the system: you're now serving the logs in an uncompressed format.

I said what I said regarding this, could have been an "anti-feature" flag just as well as "feature". I'd rather not call such changes features. It comes across as misdirected, insincere, and reminds me of the tendency in management realm -- nowadays especially -- to prioritize sales over substance.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@RobSmyth](https://avatars.githubusercontent.com/u/6183736?s=80&v=4)](https://gist.github.com/RobSmyth)


Copy link

### **[RobSmyth](https://gist.github.com/RobSmyth)**     commented    [on Dec 3, 2025Dec 3, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5890936\#gistcomment-5890936)

Hi [@JohnnyWalkerDigital](https://github.com/JohnnyWalkerDigital),

> > behavior(execute): disable logs with ... -- --help
>
> I see what you mean, you're changing how the system operates, hence "behaviour". However I wonder if it would fit in chore?

Do you think this change needs to be user documentation, release notes, or bump the version? I wonder if your using Semmantic Versioning as that would impact process here.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@raed-bash](https://avatars.githubusercontent.com/u/16381816?s=80&v=4)](https://gist.github.com/raed-bash)


Copy link

### **[raed-bash](https://gist.github.com/raed-bash)**     commented    [on Dec 4, 2025Dec 4, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5892244\#gistcomment-5892244)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

> what if we fix typing errors? what should we put before a commit message?

put `refactor`

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 4, 2025Dec 4, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5892245\#gistcomment-5892245)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

Attempt at a flow chart:

Did you fix a bug?

Yes: It's `fix:`

No: Did you change functionality or affect UI?

Yes: It's `feat:`

No: Did you add or change tests?

Yes: It's `test:`

No: Did you change code style or formatting (doesn't affect code behaviour)?

Yes: It's `style:`

No: Did you make changes to documentation?

Yes: It's `docs:`

No: Did you change how the project is built (eg. packages, dependencies, dockerfile, etc)?

Yes: It's `build:`

No: Did you change something related to devops (eg. operational or deployment/CI pipelines)?

Yes: It's `ops:`

No: Did you complete a maintenance task or other non-code task for the project (eg. modifying .gitignore or making initial commit)?

Yes: It's `chore:`

No: Did you rewrite or restructure code _specifically for performance?_

Yes: It's `perf:`

No: It's `refactor:`

Also [Mermaid Gist](https://gist.github.com/JohnnyWalkerDigital/7207004e8efd79751dbf55ece0420ef2).

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@ttytm](https://avatars.githubusercontent.com/u/34311583?s=80&v=4)](https://gist.github.com/ttytm)


Copy link

### **[ttytm](https://gist.github.com/ttytm)**     commented    [on Dec 5, 2025Dec 5, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5893039\#gistcomment-5893039)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[@JohnnyWalkerDigital](https://github.com/JohnnyWalkerDigital)

> Attempt at a flow chart:

> \[...\]

> Did you fix a bug?
>
> Yes: It's `fix:`
>
> No: Did you change functionality or affect UI?
>
> Yes: It's `feat:`
>
> No: Did you add or change tests?
>
> Yes: It's `test:`
>
> No: Did you change code style or formatting?
>
> Yes: It's `style:`
>
> No: Did you make changes to documentation?
>
> Yes: It's `docs:`
>
> No: Did you change things related to build or deploy operations?
>
> Yes: It's `build:`
>
> No: Did you change something related to devops, infrastructure or backups?
>
> Yes: It's `ops:`
>
> No: Did you complete a maintenance task or other non-code task for the project (eg. modifying .gitignore or making initial commit)?
>
> Yes: It's `chore:`
>
> No: Did you rewrite or restructure code _specifically for performance?_
>
> Yes: It's `perf:`
>
> No: It's `refactor:`

I think using a flowchart makes the solution more complicated.

AFAIK GitHub renders mermaid diagrams, so it should become visible here:

Render

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Yes

No

Did you fix a bug?

It's fix

Did you change functionality or affect UI?

It's feat

Did you add or change tests?

It's test

Did you change code style or formatting?

It's style

Did you make changes to documentation?

It's docs

Did you change things related to build or deploy operations?

It's build

Did you change something related to devops, infrastructure or backups?

It's ops

Did you complete a maintenance task or other non-code task?

It's chore

Did you rewrite or restructure code specifically for performance?

It's perf

It's refactor

```
flowchart TD
    A[Did you fix a bug?]
    A -- Yes --> B[It's fix]
    A -- No --> C[Did you change functionality or affect UI?]

    C -- Yes --> D[It's feat]
    C -- No --> E[Did you add or change tests?]

    E -- Yes --> F[It's test]
    E -- No --> G[Did you change code style or formatting?]

    G -- Yes --> H[It's style]
    G -- No --> I[Did you make changes to documentation?]

    I -- Yes --> J[It's docs]
    I -- No --> K[Did you change things related to build or deploy operations?]

    K -- Yes --> L[It's build]
    K -- No --> M[Did you change something related to devops, infrastructure or backups?]

    M -- Yes --> N[It's ops]
    M -- No --> O[Did you complete a maintenance task or other non-code task?]

    O -- Yes --> P[It's chore]
    O -- No --> Q[Did you rewrite or restructure code specifically for performance?]

    Q -- Yes --> R[It's perf]
    Q -- No --> S[It's refactor]
```

Since every decision is a simple yes/no that ends in exactly one category, a decision table (or ordered checklist) is likely a better fit.

### Checklist attempt based on the order of the original answer

01. If it fixes a bug → fix
02. Else if it changes functionality or UI → feat
03. Else if it adds or changes tests → test
04. Else if it changes code style or formatting → style
05. Else if it changes documentation → docs
06. Else if it affects build or deploy → build
07. Else if it affects devops, infrastructure, or backups → ops
08. Else if it’s a maintenance or non-code task → chore
09. Else if it improves performance → perf
10. Else → refactor

### Table attempt based on the order of the original answer

| Question | If Yes → Use Type |
| --- | --- |
| Fixes a bug? | fix |
| Changes functionality or UI? | feat |
| Adds or changes tests? | test |
| Code style or formatting only? | style |
| Documentation only? | docs |
| Build or deploy related? | build |
| DevOps / infra / backups? | ops |
| Maintenance or non-code? | chore |
| Performance-focused change? | perf |
| Otherwise | refactor |

### Table attempt with structural improvement

While the order in your answer is already a strong foundation. I think the priority order can be improved. Attempt below trying to match the current conventional Commit semantics:

| Question | If Yes → Type |
| --- | --- |
| Bug fix? | fix |
| New or changed feature in API/UI? | feat |
| Performance improvement? | perf |
| Code restructuring without behavior change? | refactor |
| Formatting only? | style |
| Tests added/corrected? | test |
| Documentation only? | docs |
| Build tools, dependencies, versions? | build |
| DevOps, infrastructure, or backups? | ops |
| Anything else | chore |

Overall the intent here is minimizing mental load, improve long-term consistency, use `chore` as true fallback to preventing it's lazy overuse.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@AchiraNadeeshan](https://avatars.githubusercontent.com/u/85824425?s=80&v=4)](https://gist.github.com/AchiraNadeeshan)


Copy link

### **[AchiraNadeeshan](https://gist.github.com/AchiraNadeeshan)**     commented    [on Dec 6, 2025Dec 6, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5894242\#gistcomment-5894242)

correct typo "I case" to "In case" in commit message description rules.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 9, 2025Dec 9, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5898098\#gistcomment-5898098)

Personally I find `ops:` to be unnecessarily detailed with little benefit over using `build:`. I also think `perf:` is unnecessary... the description of a `refactor:` can indicate performance improvements.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Dec 15, 2025Dec 15, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5905525\#gistcomment-5905525)

[@AchiraNadeeshan](https://github.com/AchiraNadeeshan) thanks, I fixed it

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Dec 15, 2025Dec 15, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5905542\#gistcomment-5905542)

> I also think perf: is unnecessary... the description of a refactor: can indicate performance improvements.

You don't have to use `perf:`, however it can be handy for generating changelogs automatically because in general `refactoring:` commits (especially those that only improves code readability) are not worth mentioning in a change log for users except performance improvements

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 15, 2025Dec 15, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5905936\#gistcomment-5905936)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[@qoomon](https://github.com/qoomon) Yep, I get that logic. Makes sense 👍

I still don't understand the inclusion of `ops:`. It's not part of the [official specification](https://www.conventionalcommits.org/en/v1.0.0/#specification), and if I'm having to stop and think about which prefix to use, then something has gone wrong.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Dec 15, 2025Dec 15, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5906121\#gistcomment-5906121)

[@JohnnyWalkerDigital](https://github.com/JohnnyWalkerDigital) what would you label a commit that changes backup mechanism e.g. the schedule

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 15, 2025Dec 15, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5906132\#gistcomment-5906132)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

> [@JohnnyWalkerDigital](https://github.com/JohnnyWalkerDigital) what would you label a commit that changes backup mechanism e.g. the schedule

DevOps are always handled at a platform-level on projects I work on, not a code level. But if they were code-level then I'd just consider it another feature of the code (so `feat:`, `refactor:` or `fix:` depending on what I was doing).

If I was altering something on the platform-level via files in the repo (eg. altering the backup schedule somehow) I guess I'd choose `chore:`.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Dec 16, 2025Dec 16, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5907713\#gistcomment-5907713)

IMHO `ops:` would be a better fit. It can not be feat or fix because no api change for the clients and refactoring is also not reflecting the change. and chore seems also not the right choice

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 16, 2025Dec 16, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5907857\#gistcomment-5907857)

Sorry, maybe I wasn't clear. I said, if a backup occurred at code-level, then it would be `feat:`, `refactor:` or `fix:` because it would be a feature for the software. This is standard for all features of the software.

If it was altering something at the platform level, then it fits with the description of `chore:` IMO. These descriptions, and the related diagram, is quite helpful I think.

[conventional-commits/conventionalcommits.org#634 (comment)](https://github.com/conventional-commits/conventionalcommits.org/issues/634#issuecomment-2948248673)

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Dec 17, 2025Dec 17, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5908389\#gistcomment-5908389)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[@JohnnyWalkerDigital](https://github.com/JohnnyWalkerDigital) It depends if your referring to an OSS project I would agree then it's a `feat:` or `fix:` commit. However if it's an closed source company project then it would be `ops:` because this change does not change any behaviour a client is able to recognise

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Dec 19, 2025Dec 19, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5912267\#gistcomment-5912267)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[@qoomon](https://github.com/qoomon) I think it's irrelevant if it's OSS or not. "Backup" is vaguely defined. It might be an important feature of the software itself, or it might be something at a platform level, as I said. That is the only difference.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Dec 22, 2025Dec 22, 2025](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5914669\#gistcomment-5914669)

By OSS I mean if the change affects the clients/users

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@RedCMD](https://avatars.githubusercontent.com/u/33529441?s=80&v=4)](https://gist.github.com/RedCMD)


Copy link

### **[RedCMD](https://gist.github.com/RedCMD)**     commented    [on Jan 9Jan 9, 2026](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5935270\#gistcomment-5935270)

what about improving the performance of a test?

still just `test:` or change to `perf:`

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@JohnnyWalkerDigital](https://avatars.githubusercontent.com/u/6763222?s=80&v=4)](https://gist.github.com/JohnnyWalkerDigital)


Copy link

### **[JohnnyWalkerDigital](https://gist.github.com/JohnnyWalkerDigital)**     commented    [on Jan 9Jan 9, 2026](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5935366\#gistcomment-5935366)

> what about improving the performance of a test? still just `test:` or change to `perf:`

If you follow [the flow I made](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5892245#gistcomment-5892245), it answers this for you. (It's also why I didn't do what ttytm did in their version.)

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[![@qoomon](https://avatars.githubusercontent.com/u/3963394?s=80&v=4)](https://gist.github.com/qoomon)


Copy link

Author

### **[qoomon](https://gist.github.com/qoomon)**     commented    [on Jan 11Jan 11, 2026](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13?permalink_comment_id=5937385\#gistcomment-5937385)

[@RedCMD](https://github.com/RedCMD) it's `test:`. `perf:` is an special `refactor:` commit. And refactor should only be used for feature related refactoring.

Sorry, something went wrong.


### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).

[Sign up for free](https://gist.github.com/join?source=comment-gist) **to join this conversation on GitHub**.
Already have an account?
[Sign in to comment](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fqoomon%2F5dfcdf8eec66a051ecd85625518cfd13)

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