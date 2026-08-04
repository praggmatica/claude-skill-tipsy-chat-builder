# Tipsy Chat Builder — Claude Skill

A Claude Agent Skill that builds Tipsy chat experiences. The skill lives in this repository as a
`SKILL.md` file plus any supporting reference files, following the
[Agent Skills](https://code.claude.com/docs/en/skills) format.

## Requirements

- **Claude Code** (CLI, desktop app, or IDE extension), or
- **Claude** on claude.ai (Pro/Max/Team/Enterprise plan with Skills enabled)

## Installation

### Claude Code — personal skill (available in every project)

Copy the skill into your personal skills directory:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/praggmatica/claude-skill-tipsy-chat-builder.git \
    ~/.claude/skills/tipsy-chat-builder
```

Or download a [release](https://github.com/praggmatica/claude-skill-tipsy-chat-builder/releases)
and extract it to `~/.claude/skills/tipsy-chat-builder/`.

### Claude Code — project skill (available in one project)

From the root of the project where you want the skill available:

```bash
mkdir -p .claude/skills
git clone https://github.com/praggmatica/claude-skill-tipsy-chat-builder.git \
    .claude/skills/tipsy-chat-builder
```

Commit `.claude/skills/tipsy-chat-builder/` to share the skill with everyone working in that
repository.

### claude.ai (web and desktop apps)

1. Download the latest [release](https://github.com/praggmatica/claude-skill-tipsy-chat-builder/releases)
   zip (or zip the repository contents yourself — `SKILL.md` must sit at the top level of the zip).
2. In Claude, open **Settings → Capabilities → Skills**.
3. Click **Upload skill** and select the zip.
4. Toggle the skill on.

### Verify the install

Start a new Claude Code session and type `/` — `tipsy-chat-builder` should appear in the skill
list. You can also ask Claude directly: *"What skills do you have available?"*

## Usage

<!-- TODO: skill-specific usage instructions go here. -->

## Development

Validation runs automatically in CI on every push and pull request (see
`.github/workflows/ci-skill.yml`). To validate locally:

```bash
npm run validate:skills
```

This checks every `SKILL.md` in the repository for valid frontmatter, naming, field types, and
broken file references, plus general file hygiene.

## License

[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This skill is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to use it, adapt it, and build on it, including commercially. Two conditions:

- **Attribution.** Credit this project and link back to it.
- **ShareAlike.** If you adapt the skill and distribute your version, license that version under
  CC BY-SA 4.0 as well.

### What the license does not cover

The characters, Worlds, field text, and images you create while using this skill are yours. The
ShareAlike condition applies to adapted versions of the skill itself, meaning a fork or a derived
skill package, not to the builds you produce with it. Nothing here asks you to license your
characters, publish your field text, or credit this project on your Tipsy profile.

This is a plain-language summary rather than legal advice. The
[legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode) governs.

Contributions are accepted under the same license.
