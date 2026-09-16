# Uploaded knowledge files

The create form takes up to 10 files at 2MB each, sitting under Background.
Tipsy has documented none of it and has not answered creators asking for
worldbook support, so everything here is creator-tested rather than published.
Five things are settled as of September 2026: TXT uploads carry a severe cost
penalty and JSON does not, file contents are private, a file surfaces only when
the conversation makes it relevant rather than sitting in context, the
upload field is only on the form while HTML Styling is off, and an already
uploaded file stops firing while HTML Styling is on and fires again once it is
switched back off.

## HTML Styling removes the field

On the single-character form, switch HTML Styling on and the upload
disappears. Switch it off and it comes back. Observed in August 2026 and again on the September 2026 form. So a single
character gets styled Description and Opening fields or knowledge files, not
both. The Multi-character form has no HTML Styling toggle, so a container always
keeps its upload.

Raise this before writing a file, not after. A creator who ships a styled card
and then decides the build needs a world file has to strip the HTML out of both
public fields and rewrite them in markdown to get the upload back.

A file uploaded while HTML Styling was off stays attached after the toggle
goes on, but it stops firing. Creator-tested and confirmed in September 2026:
HTML Styling blocks the model's access to the JSON, and switching HTML Styling
back off reactivates injection from the same file with no re-upload. Nothing
is lost by toggling, but there is no state where styled public fields and a
live file coexist, so never plan a build that needs both.

The practical consequence for a creator debugging a silent file: check the
HTML Styling toggle before suspecting the JSON. A file that retrieved fine
last week and returns nothing now, on a card whose Description was recently
restyled, is this and not a key-matching problem.

## The hard rule: JSON only, never TXT

That includes a JSON object saved with a `.txt` extension, which is the trap
most creators fall into, because the content looks correct and the file bloats
anyway.

Creator testing puts the plain text ingestion penalty at roughly **15x the
file's own token count**, charged on top of everything already in the
character's fields. A 2,000 token text file, which is only 5 to 6 KB, takes a
2,000 token character to somewhere near 32,000 tokens of context. Every player
pays that in gems on every message, and the creator pays it worst, because
testing a build means sending far more messages than any one player will.

The same object in a `.json` file does not do this. The character stays its own
size and the content still reaches the model when it is needed.

So when a user asks for a text file, do not make one. Say why, hand back JSON,
and offer a Markdown copy they keep locally as the readable version that never
gets uploaded. Do not soften this into a preference. It is a cost bug, the
platform has not acknowledged it, and the text version has no upside.

## Retrieval is the thing to design around

Entries surface when relevant, so an entry nobody triggers costs nothing. Two
consequences run in opposite directions and both matter.

**Volume is cheap.** Unlike Background, breadth here is close to free. Big
gazetteers, long minor-cast rosters, shop inventories, festival calendars,
family trees, and the history nobody asks about until they do are all correct
uses. Write more than you think the story needs.

**Presence is never guaranteed.** An entry that does not fire is not in the
prompt at all. That single fact decides what may live in a file. Anything the
character must honour on every message has to be in a field, because fields are
always there and files are not.

Nothing load bearing goes in a file. Not the reveal timing, not the gates, not
the trackers, not the notation and perception rules, not the closeness ladder,
not the post-objective rotation, not momentum. Those are in Reply Settings and
Background, where the model reads them every turn. A gate that lives in a file
is a gate that opens whenever retrieval happens to miss.

The subject of a gated secret can live in a file. The rule governing when it is
revealed cannot.

## Writing entries that fire

Retrieval failure is the failure mode here, and it is quiet: the character just
does not know something, and the creator concludes the file did not upload.

**Key on what a player types, not on what you named it.** The in-world name,
the shortened form everyone actually uses, the epithet, the misspelling that
autocorrect produces, and the role. A player types "the market," not "The Salt
Market of the Lower Terraces."

**Every entry stands alone.** It arrives without the rest of the file around
it, so it cannot lean on a parent key, a heading, or the entry above it. Name
the subject inside the value, in a full sentence, every time. An entry reading
"Closed by noon" is useless when it surfaces on its own.

**One subject per entry.** An entry covering three places fires on one of them
and drags the other two in, which spends context and invites the model to
volunteer things nobody asked about.

**Write values the way you want them spoken back.** Note form comes back as
note form. Two or three plain sentences is the right size.

**Duplication between a file and a field is allowed here**, since a sleeping
entry costs nothing, but wording that contradicts a field is not. A retrieved
entry lands late in the prompt, and later text beats earlier text, so a file
entry disagreeing with Background wins the disagreement it should have lost.
When both must exist, make the file entry the longer version of the same
claim, never a variant one.

## Shape: the SillyTavern World Info format

Creators are building these in SillyTavern and exporting the World Info JSON,
so that is the format to write. SillyTavern is at
github.com/SillyTavern/SillyTavern and its World Info documentation is at
docs.sillytavern.app/usage/core-concepts/worldinfo/. Read the docs before
inventing a field.

The top level is a single `entries` object keyed by stringified index, not an
array. Indices run from `"0"` and must match each entry's `uid`.

```json
{
  "entries": {
    "0": {
      "uid": 0,
      "key": ["the salt market", "the market", "market square", "Vekker"],
      "keysecondary": [],
      "comment": "The Salt Market",
      "content": "The Salt Market opens before dawn and closes by noon. The Vekker family have run it for three generations. It is the only place in the lower city that still trades in coin rather than credit, which is why smugglers drink at the north end.",
      "constant": false,
      "vectorized": false,
      "selective": true,
      "selectiveLogic": 0,
      "addMemo": true,
      "order": 100,
      "position": 1,
      "disable": false,
      "ignoreBudget": false,
      "excludeRecursion": false,
      "preventRecursion": false,
      "delayUntilRecursion": false,
      "probability": 100,
      "useProbability": true,
      "depth": 4,
      "group": "",
      "groupOverride": false,
      "groupWeight": 100,
      "scanDepth": null,
      "caseSensitive": null,
      "matchWholeWords": null,
      "useGroupScoring": null,
      "automationId": "",
      "role": null,
      "sticky": 0,
      "cooldown": 0,
      "delay": 0,
      "triggers": [],
      "displayIndex": 0,
      "characterFilter": { "isExclude": false, "names": [], "tags": [] }
    }
  }
}
```

Exports also carry `outletName` and several `match*` booleans
(`matchPersonaDescription`, `matchCharacterDescription`, and so on). Keep
whatever the exporter wrote. Do not hand-delete fields from an export, and give
every entry the identical field set, since a file with one ragged entry is the
kind of thing a stricter parser rejects wholesale.

## What each field actually does

Only three fields carry the writing:

- **`key`** is the trigger list. Case-insensitive by default. Single word keys
  match whole words only, so `king` hits "long live the king" and misses
  "liking". Multi-word keys match as substrings, which is why `attendant` also
  fires an entry keyed on `senior attendant`. Keys may be JavaScript regex
  with `/` delimiters.
- **`content`** is the only text that reaches the model. Keys, `comment`, and
  every other field stay out of the prompt. That is the mechanical reason
  entries must be self-contained: the model never sees the title.
- **`comment`** is your label. It is not used by the AI or by trigger logic, so
  write it for yourself.

The rest is behaviour, and the ones worth setting deliberately:

- **`order`** is priority under budget pressure. Higher numbers land closer to
  the end of the context and carry more weight, so order 250 beats order 100.
  A file where every entry is 100 has no priorities at all.
- **`position`** 1 is after character definitions, which is the strong slot and
  the right default. `depth` only applies at position 4, so `depth: 4` sitting
  next to `position: 1` is inert and harmless.
- **`constant: true`** inserts regardless of keys. Tempting and wrong for
  Tipsy: an always-on entry is Background with extra steps, and load bearing
  content belongs in a field. Leave it false.
- **`group`** is an inclusion group. When several entries in the same group
  fire at once, only one is inserted. This is the correct fix for two entries
  that legitimately compete for the same word.
- **`probability`** with `useProbability` is a chance to skip on activation.
  Useful for random colour, dangerous for anything a player might rely on.
- **`selective: true`** does nothing while `keysecondary` is empty, since the
  filter is ignored with no arguments. It only bites when you add secondary
  keys, and then `selectiveLogic` 0 means the primary key plus any one
  secondary.
- **`sticky`**, **`cooldown`**, and **`delay`** are timed effects measured in
  messages. Sticky keeps an entry live for N messages after it fires, which is
  the closest thing here to holding a scene's setting in place.

**Assume Tipsy honours only `key` and `content`.** Nothing published says it
reads the rest, and a file designed around `constant`, `probability`, or
inclusion groups will fail silently if it does not. Set those fields correctly
anyway, since they cost nothing and pay off if Tipsy is running the full
engine, but never build a story beat that depends on one.

## Key hygiene

This is where real files go wrong, and it is invisible until you look for it.

**Sweep for collisions before shipping.** List every key across every entry and
find the repeats. Two rooms that share a generic word in their names will
usually end up sharing it as a key, and then one mention pulls both and the
model narrates a composite of the two. Either specialise the keys, or put the
entries in the same inclusion group so only one wins.

**Merge near-duplicate entries rather than keying around them.** Separate
A concept and the people it applies to, split into two entries that share keys
and repeat each other's content, will both fire on the same word and spend
double the budget saying the same thing twice. One entry, both key sets.

**Cut keys that are ordinary conversation.** `request`, `accept`, `decline`,
`rules`, `conduct`, `behavior`, `standing`, `class`, `bar`, and `guard` all
read as lore triggers when you are writing the file and as everyday words the
moment someone plays it. An entry keyed on those fires almost every message,
eats the budget, and crowds out the entry that was actually relevant. When a
concept genuinely has no distinctive word, give it a distinctive one in the
fiction and key on that.

**Key every proper noun the file mentions.** If an entry names a character,
place, or object, something has to define it. A room entry that names the
person whose chair sits at its centre, with no entry keyed on that person, is a
name the model will happily invent a whole character for.

**Use recursion on purpose.** An entry whose content contains another entry's
key can pull that entry in too, so a room entry mentioning the Residents drags
the Residents entry along. That is useful when it is deliberate and expensive
when it is accidental. `excludeRecursion` stops an entry being pulled in this
way, `preventRecursion` stops it pulling others.

**Watch the punctuation you inherit.** Files passed between creators carry
their author's habits, em dashes included. Read the content, do not just
reformat the structure.

## Privacy

File contents are private, confirmed. That makes a file, along with Background
with its toggle off, one of the two places a secret can safely live. Compare
Description, Opening, Example Dialogues, and the Multi-character Character
List, all of which are public and all of which have spoiled builds.

Privacy is not permission to move the mechanism there. The lore behind the
twist can go in a file. What triggers it stays in a field.

## Testing

Retrieval is testable and worth testing, because a silent miss reads exactly
like a file that never uploaded.

Start a fresh chat, then ask out of character: "OOC: what do you know about the
Salt Market?" A correct answer means the entry fired. A vague or invented
answer means the trigger words are wrong, not that the content is bad. Fix the
keys before touching the value.

Then test the words a player would use rather than the ones you wrote. If
"the market" misses where "Salt Market" hits, the keys are too formal.

Then test the ordinary ones. Say something bland that uses a key in its
everyday sense and see whether an entry surfaces that had no business being
there. That is the over-broad key showing itself.

## Re-test triggers

Revisit this page, and tell the user the guidance is dated, when any of these
happen:

- Tipsy announces worldbook or lorebook support, or documents the field.
- Tipsy exposes retrieval controls such as scan depth, token budget, or a
  constant or always-on flag, all of which would change the advice above.
- Tipsy states which SillyTavern fields it honours, which would settle whether
  inclusion groups, probability, and timed effects are usable or decorative.
- A user reports a TXT upload that did not bloat, which would mean the cost fix
  shipped silently.
- The upload field appears on the form while HTML Styling is on, which would
  end the choice between styled public fields and files.
