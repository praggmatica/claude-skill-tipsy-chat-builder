# Tipsy Chat Builder — Claude Skill

A Claude Agent Skill that builds experiences for [Tipsy Chat](https://tipsy.chat), the AI roleplay
platform — single characters, Multi-character ensembles, and interactive story Worlds. The skill
lives in this repository as a `SKILL.md` file plus supporting reference files, following the
[Agent Skills](https://code.claude.com/docs/en/skills) format.

## What the skill covers

- **All three creation surfaces.** Single characters, Multi-character casts (published single
  characters assembled into one scene through a Character List), and Studio-built Worlds with
  their own lore, cast, and rule engine. Each has its own field map and build order.
- **Field-by-field authoring.** Every field on every surface: what it does, its hard character
  limit, whether it is public, and what belongs in it — including the HTML presentation container
  for the public fields.
- **Rule design that actually holds.** Five core principles (mechanical gates over negative
  instructions, permitted alternatives for every prohibition, greeting/example reinforcement,
  field-over-rule precedence, session history beating field edits) and the drop-in blocks that
  ship with every build: notation and perception, life after the objective, personality surface,
  and two-exchange momentum.
- **Knowledge files, JSON only.** The no-TXT rule and the ingestion penalty behind it, the
  SillyTavern World Info format, retrieval-first entry design, key hygiene, and what must never
  live in a file.
- **Known failure modes with fixes.** Stalling, looping, rushed reveals, character drift, player
  insert problems, structural contradictions, and the Multi-character variants of each.
- **Image prompting.** Platform requirements, prompt syntax, writing exclusions without a
  negative prompt, working from reference images, and image rules in Worlds.
- **Rating compliance and spoiler surfaces.** SFW versus Limitless, which fields are public,
  where secrets can safely live, and how to write a publish announcement that gives nothing away.
- **A delivery contract.** Every field comes back complete and pasteable — one labelled code
  block per field, character counts on the capped ones, never a patch or a fragment.

## What's inside

| File | Covers |
|---|---|
| `SKILL.md` | Core workflow: surfaces, principles, mandatory blocks, build order, limits, ratings, delivery |
| `references/characters.md` | Single-character fields, HTML presentation, perception and closeness banding, trackers |
| `references/multi-character.md` | Character List, conventions contract, turn-taking, publish order |
| `references/worlds.md` | Studio field map, rule taxonomy, publish announcements, linking Worlds to characters |
| `references/knowledge-files.md` | JSON-only rule, SillyTavern World Info format, retrieval design, key hygiene |
| `references/images.md` | Platform requirements, prompt syntax, exclusions, reference images, image rules in Worlds |
| `references/failure-modes.md` | The full failure catalogue with fixes, indexed by symptom |

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

Or download `tipsy-chat-builder.skill` from the latest
[release](https://github.com/praggmatica/claude-skill-tipsy-chat-builder/releases) — it is a zip
archive that already contains a top-level `tipsy-chat-builder/` folder — and extract it into the
skills directory itself:

```bash
mkdir -p ~/.claude/skills
unzip tipsy-chat-builder.skill -d ~/.claude/skills
```

Do not extract into `~/.claude/skills/tipsy-chat-builder` — that nests the folder twice and the
skill will not load.

### Claude Code — project skill (available in one project)

From the root of the project where you want the skill available:

```bash
mkdir -p .claude/skills
git clone https://github.com/praggmatica/claude-skill-tipsy-chat-builder.git \
    .claude/skills/tipsy-chat-builder
```

Or, with the `.skill` file:

```bash
mkdir -p .claude/skills
unzip tipsy-chat-builder.skill -d .claude/skills
```

Commit `.claude/skills/tipsy-chat-builder/` to share the skill with everyone working in that
repository.

### claude.ai (web and desktop apps)

1. Download `tipsy-chat-builder.skill` from the latest
   [release](https://github.com/praggmatica/claude-skill-tipsy-chat-builder/releases).
2. In Claude, open **Settings → Capabilities → Skills**.
3. Click **Upload skill** and select the `.skill` file.
4. Toggle the skill on.

### Verify the install

Start a new Claude Code session and type `/` — `tipsy-chat-builder` should appear in the skill
list. You can also ask Claude directly: *"What skills do you have available?"*

## Usage

Once installed, Claude loads the skill automatically whenever the conversation is about Tipsy —
building or editing a character, assembling a cast, designing a World, or debugging one that is
misbehaving. You can also invoke it directly with `/tipsy-chat-builder`.

Things you can ask for:

- *"Build me a Tipsy character: a lighthouse keeper hiding that he is a storm god."*
- *"Turn these three published characters into a Multi-character scene."*
- *"Design a World where the player runs a failing tavern on a trade road."*
- *"My bot ends every reply asking the player what they want to do. Fix it."*
- *"Convert this worldbook TXT into a knowledge file."*
- *"Review my character sheet before I publish."*

Every field Claude touches comes back complete and ready to paste — one code block per field,
labelled with the editor's field name, with a character count on the capped fields. After any
substantial edit, start a fresh chat on Tipsy; session history beats field edits.

## Development

Validation runs automatically in CI on every push and pull request (see
`.github/workflows/ci-skill.yml`). To validate locally:

```bash
npm run validate:skills
```

This checks every `SKILL.md` in the repository for valid frontmatter, naming, field types, and
broken file references, plus general file hygiene.

To rebuild the `.skill` package after editing, zip the skill files under a top-level
`tipsy-chat-builder/` folder:

```bash
mkdir -p /tmp/skill-build/tipsy-chat-builder/references
cp SKILL.md /tmp/skill-build/tipsy-chat-builder/
cp references/*.md /tmp/skill-build/tipsy-chat-builder/references/
(cd /tmp/skill-build && zip -r tipsy-chat-builder.skill tipsy-chat-builder)
```

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
