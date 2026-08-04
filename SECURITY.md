# Security Policy

## What this project is

This repository distributes a Claude skill: a set of Markdown instruction files that Claude reads when you ask it about building for Tipsy Chat. It contains no executable code, no scripts, no dependencies, and makes no network calls of its own. Nothing here runs on your machine.

If that ever changes, it will be stated plainly in the release notes for the version it changes in.

## Supported versions

Only the most recent release is supported. Older releases are not patched, and a stale copy is the most common cause of wrong guidance, since Tipsy changes field names and caps without notice.

| Version | Supported |
| ------- | --------- |
| Latest release | :white_check_mark: |
| Anything older | :x: |

Check your installed copy against the [Releases page](../../releases) before reporting anything.

## Install from the Releases page only

Download the archive from this repository's Releases page. A skill that reached you through a repost, a chat message, or a mirror may not be the file published here.

Skills are instructions an assistant follows on your behalf, so treat any skill from any source the way you would treat a script you were about to run. Open `SKILL.md` and the files in `references/` and read them before you upload. Everything in this package should be about Tipsy Chat field authoring. Anything that asks Claude to contact a service, install a package, reveal the contents of your conversation, or ignore its earlier instructions does not belong here and is worth reporting.

## What counts as a vulnerability

* Text anywhere in the package that attempts to make Claude act outside the stated purpose of the skill, including instructions to override its own guidelines, exfiltrate conversation content, or reach an external service.
* A release asset that does not match the tagged source.
* A link in the documentation that points somewhere hostile or has been taken over.
* Anything in the package that would cause a user to expose credentials or personal information.

## What does not

* Guidance that is wrong, stale, or unhelpful. That is a [bug report](../../issues/new/choose).
* A character or World behaving badly in play. That is [Build help](../../discussions/categories/build-help).
* Anything about Tipsy Chat's own platform, ratings, or review process. Report that to Tipsy.

## Reporting

Use GitHub's private vulnerability reporting: go to the [Security tab](../../security) and choose "Report a vulnerability". The report stays private between us until there is a fix.

Please do not open a public issue for a suspected vulnerability, and do not include API keys, account credentials, or personal information in the report.

This project is maintained by one person, so here is what to honestly expect:

* Acknowledgement within seven days.
* An assessment, accepted or declined with reasons, within thirty days.
* If accepted, a fix in a new release, with the old release yanked where the risk warrants it, and credit in the release notes unless you would rather not be named.
* If declined, an explanation of why. You are free to disclose publicly at that point.
