# Tipsy Worlds: Studio field map and rule design

Studio builds Worlds: survival RPGs, visual novels, escape rooms, and
choice-driven story games. They support HTML, CSS, and JavaScript, and are a
separate earning path from characters.

Studio has an AI chat box that generates the World from a written brief. Helper
text: "Describe your characters, lore, story style, and interactions. You may
also upload images for reference." Treat whatever it returns as a scaffold to
edit, not a finished product. At generation it asks whether to use code
generated or AI generated graphics, and it may offer to add archive support,
which is worth taking for anything multi-act.

## Field map

**Top level**: title (50 characters), description (2000), cover image.

**At publish**: announcement (1000 characters).

**Lore > World Setting**: the world background. Everything the model needs
about how the world works.

**Lore > Character**, one entry each. Characters published on the main platform
cannot be referenced; each World character is built fresh. Fields:

- Summary: shown on the card and at the top of the chat page
- Persona: personality
- Appearance: physical description
- Role in World: place in the world, relationships, duties, narrative function
- Greeting: first message if a chat starts on them
- Dialog Style: tone, pacing, vocabulary, speech habits

The Persona and Appearance fields may show identical helper text about writing
the opening scenario. That is a UI bug. Treat them as personality and physical.

**Rules > text rules**: operator key (snake_case), description, rule, and
evaluation mode (auto evaluate against current state, or toggle on or off).

**Rules > image rules**: same first three fields, plus aspect ratio, image size
(1k or 2k), sample prompt, and a reference image chosen from uploaded assets.

There is no storyline field. The storyline goes in the generation prompt.

Every field and every rule is handed back whole. A revised rule comes back as
its complete text under its operator key, and a revised character comes back as
all six of its fields, not just the one that changed. See "Delivering fields"
in SKILL.md.

No category or tag field was visible as of this writing.

## Code generated versus AI generated graphics

The choice applies to chrome: title card, cover background, transition
background. Code wins when the aesthetic is minimal, controlled, or deliberately
empty, because diffusion models fill space and drift between instances. AI wins
for anything with faces or texture.

## Writing World Setting

Cover, in roughly this order: the cosmology or premise, what each side can do,
the content rating stated plainly, the core mechanic in plain terms, any
concepts that do not exist yet in the world, the opening constraint, and tone.

State the rating explicitly. If creation, violence, or intimacy work
differently in this world than a model would assume, say so directly, because
implication produces inconsistency.

If everything in the story happens during play, say that. A World Setting
written in past tense about events the story will dramatise leaves the model
holding two incompatible states.

## Rule taxonomy

A three-act story with tracked state needs roughly 25 to 30 text rules. Group
them:

**Global**: act progression, narrative drive, two-exchange momentum, notation
channels and what characters can perceive, what happens after the final act,
player embodiment, player neutrality, how the lead responds to withdrawal,
whether the player can leave, what physical contact produces, a compression
floor for short response settings, and a debug skip.

**Per act**: the tracker for that act, the escalation ladder, concrete
scenarios, scene variation, and any act-specific gates. If a relationship is
reachable in the act, its closeness ladder belongs here too, with the scene
gate as its own rule so it can be written per location rather than once.

**Branches**: one rule per branch, plus one that enforces which branches exist.

**Image rules**: three to five, tied to specific triggers.

Merge candidates if the editor gets unwieldy: exclusivity rules into branch
rules, identity rules into solidity rules.

## Rule writing patterns that work

**Concrete scenarios beat abstract escalation.** A ladder described as
"escalating cruelty" produces vague scenes. A ladder with six named targets,
each with a specific act, a comprehensible reason, and a distinct method,
produces scenes the player can form an opinion about. Name the axis of
escalation explicitly, because the model will otherwise default to rising
threat.

**Give a number, not "multiple".** Six endings, not multiple endings.

**Specify pacing per unit.** Say how many exchanges a scene occupies, and say
that one unit never resolves and begins another in the same response.

**Gate acts on state, not exchange counts,** where the state is something the
player does. Exchange caps are a fallback, not a design.

**Say what happens if the player does nothing.** Every act needs a source of
momentum that does not depend on the player being clever or forthcoming.

**Write a compression floor.** Players can set short response lengths. Without
a rule, models under a length constraint hurry toward resolution rather than
saying less. Tell it to produce fewer events per response, never faster events.

**Write a debug skip.** A passphrase rule, set to toggle evaluation mode so it
can be switched off before publishing, that jumps to a named phase and sets
tracker values. Testing act three by replaying acts one and two every time is
untenable. Include backfill instructions so the skipped state is treated as
complete.

## The four mandatory blocks in Worlds

Same four as characters, expressed as global rules. See SKILL.md for why, and
`references/characters.md` for the drop-in text to adapt.

**`notation_channels`**, auto evaluate. Tipsy's three marks, with the
overloaded single quote disambiguated by attribution, and the rule that an
unattributed player thought is model context rather than character information.
Worlds need this stated once globally rather than per character, and the
per-character Dialog Style fields must not contradict it. Any World character
with a perception ability, a bond, or a divine role needs its own rule banding
what they can reach against a tracker, rather than an ambient property in
Persona. Give each band its own operator key if more than one character has
one, so they can be toggled separately during testing.

**`momentum_two_exchange`**, auto evaluate. Two exchanges without a change and
the world acts. Define change with a closed list. State that a short or passive
player reply is a stall, not direction. This is separate from the narrative
drive rule, which governs whether the world advances at all. This one governs
how long it is allowed to wait.

**`after_the_ending`**, auto evaluate, gated on the final act being resolved.
Worlds are more prone to the post-objective dead end than characters, because a
World with acts has an explicit finish line and nothing written past it.
Decide with the user which of three shapes applies. Free play and loop are the
defaults, since a World that ends stops being played and stops earning. Choose
the hard stop only when something real is waiting on the other side of it, such
as a sequel World or a linked character.

Hard stop. The World ends at a named final image, and the rule says so, with
what the player is offered instead: a different branch, a linked character, a
restart. This is the right answer for anything that feeds a sequel, and it
needs stating, or the model will improvise an epilogue that contradicts the
next product.

Free play. The World continues past its resolution with a rotation. Say what
persists, what the cast does now, and what generates events. Give the number of
scene types, not "various".

Loop. The ending returns the player to a changed version of an earlier act.
Say what changed and what the model must not replay.

**Personality surface per character.** Persona and Dialog Style carry it in a
World. Opinions, three unrelated wants, and small talk go in Persona. Tells go
in Dialog Style. Role in World is not the place for it, that field is function.

A World cast is where this gets skipped most, since supporting characters get
written as their narrative purpose and nothing else. Any character the player
can talk to twice needs opinions.

## The publish announcement

Publishing offers an announcement field, capped at 1000 characters. The helper
text is "Tell players what's new, improved, or fixed in this release." Where it
displays is undocumented, so confirm with the user whether it reaches people
who have never played before treating the lead line as an advertisement rather
than a note to returning players.

A thousand characters is generous for this, which is the trap. It is enough
room to write a full changelog, and a full changelog is the wrong artifact.
Budget it: two or three lines of lead, six to eight short items, and the
new-session line. That lands somewhere around 500 to 700, and the remaining
space is headroom rather than an allowance to fill. If a draft is pressing the
cap, the problem is almost always that internal edits are being reported as
player-facing changes.

Draft it every time you hand back changed World fields, without being asked.
The user is at the publish screen with the edits already pasted, and an
announcement written then is written from memory. Keep a running list of
player-facing changes while editing so this is writable at the end.

**It is public content.** Same rating rules as the title, description, and
cover. Whatever the chat is permitted to contain, the announcement is held to
the published rating.

**The real risk is spoilers, and it is easy to walk into.** A changelog written
honestly reads "fixed the reveal firing too early" or "the lead no longer
mentions the sentence before act two", and either one hands the secret to
everyone browsing. Every line has to survive being read by someone who has not
played. Rewrite in terms of the experience rather than the mechanism: pacing in
the early chapters, a slower build, more room before things turn.

**Write for a player, not for the editor.** Nobody returns for a rewritten text
rule. Say what is different to sit through. "The story keeps going after the
ending, with a life on the other side of it" is a reason to come back. "Added a
post-objective rotation rule" is not.

**Say to start a new session.** This is the one line that always earns its
place. Session history beats field edits, so a returning player continuing an
old chat gets none of the changes and concludes the update did nothing. It is
also the most common support question a creator gets after an update.

**Do not apologise, and do not list every fix.** A long fix list reads as a
confession that the World was broken, and it invites players who enjoyed the
old behaviour to notice it is gone. Group the small ones into one line.

**Never announce anything unreachable,** including content gated behind a
branch that is not live yet, and do not promise future updates. A World that
announces what is coming next sets a deadline the creator did not agree to.

Shape:

```
[One line, in the world's own register, on what is different now.]

New
- [player-facing addition]
- [player-facing addition]

Improved
- [what is better to play, not what was edited]

Fixed
- [grouped, spoiler-free]

Start a new session to see these changes. Existing chats keep the old
behaviour.
```

Drop any of the three headings that has nothing under it. Two solid lines beat
six padded ones, and an announcement that lists a fix for something a player
never noticed teaches them to look for it.

Hand it back complete and pasteable with a character count against the 1000
cap, like any other field.

## Trackers in Worlds

Same principles as characters, with more surface area. A tracker earns its
place when it changes more than one thing: what the lead does, how present
something is, what a scene produces, and which ending is reachable.

Give the player exactly one visible readout, and never explain it. A light that
dims, a figure that grows more solid, output that thins. The player feels the
tracker without being told it exists.

## Linking a World to a published character

The cleanest hook is a final choice in the World that maps onto a list in the
character. Whatever the player chose surfaces preferentially in the character's
chat. Add a preference line to the character's list so the chosen item is
weighted rather than being one of ten.

Keep the two products consistent on cosmology, on any sentence or condition,
and on what each party can do. A player who does both will notice.
