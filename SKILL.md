---
name: tipsy-chat-builder
description: Build single characters, Multi-character ensemble builds, and interactive story Worlds for Tipsy Chat (tipsy.chat), the AI roleplay platform. Use this whenever the user mentions Tipsy, tipsy.chat, Tipsy Studio, building or editing an AI roleplay character, a character card, a Multi-character build or cast, a "World", or fields like Persona, Greeting, Dialog Style, Reply Settings, Conversation Style, Character List, Example Dialogues, or Role in World. Also use it when they are debugging a bot that rushes its reveal, stalls, loops, runs out of story once its objective is met, has nothing to talk about, waits on the player instead of acting, or drifts from its character sheet, even if they never say the word Tipsy. Covers field-by-field authoring, rule design for multi-act Worlds, image prompting, rating and review compliance, and a catalogue of known failure modes with fixes.
---

# Tipsy Chat Builder

Tipsy Chat has three creation surfaces. Establish which one before writing
anything.

**Characters** are single personas with a fixed field set. One conversation,
no acts, no tracked state beyond what you encode in instructions.

**Multi-character** builds are the same create form with the Type toggle
flipped. They assemble already published single characters into one scene
through a Character List. Nothing about a cast member's persona is authored
here, and there is no Reply Settings field, so conduct has to be agreed across
the members before any of them is published.

**Worlds** are built in Studio and are multi-scene interactive games with
their own lore, cast, and rule engine. Worlds support HTML, CSS, and
JavaScript.

If the user is vague, ask. The field sets barely overlap and guessing wastes
their time.

For field-by-field guidance read `references/characters.md`,
`references/multi-character.md`, or `references/worlds.md`. A Multi-character
build needs both of the first two, since every cast member is a single
character build in its own right. Before shipping anything, read
`references/failure-modes.md`, which is the most valuable file here. Read
`references/images.md` when generating art.

## The five principles

Everything in the reference files derives from these. If a situation is not
covered, reason from here.

**1. Negative instructions are weak. Gate mechanically instead.**

"Never reveal that he is a god" fails. A tracker that only rises through
physical contact, plus a ban on the specific words god, immortal, divine, and
eternal, holds. When you want to prevent something, ask what mechanism would
make it impossible rather than what instruction would forbid it.

**2. Every prohibition needs a permitted alternative.**

Banning something without saying what to do instead makes the model invent a
different wrong thing. "Never distinguish them by height" produced "the hollow
one" instead. The fix was listing the permitted ways to tell them apart.

**3. Whatever appears in the greeting and example dialogue gets reinforced.**

Tipsy's own guidance is explicit that example content reinforces specific words
and lore and influences whether the character initiates actions. It does not
teach speaking style. So never put the reveal in an example, and watch what the
greeting's closing line teaches: a greeting ending "what else can you do" will
have the character asking that for the rest of the story.

**4. Character fields beat rules. Later text beats earlier text.**

If a rule and a character field disagree, the field usually wins. If two fields
disagree, the model follows whichever it read last. After any edit, sweep every
field for the contradicting statement rather than fixing one place.

**5. Session history beats field edits.**

A conversation that has established a rhythm keeps matching it even after the
underlying fields change. After any substantial edit, tell the user to start a
fresh chat rather than continuing the old one. Otherwise they will conclude the
fix did not work.

## Four blocks that ship with every build

Not optional, and not something to wait for the user to ask for. Every
character and every World gets all four. In characters they live in Reply
Settings and Background. In Worlds they are global text rules. Write them in,
then tell the user they are there and what they do.

**1. Notation and what the character can hear.** Tipsy's own convention uses
three marks: double quotes for speech, asterisks for action and narration, and
single quotes for anything that is not in the character's speaking voice, which
covers both interior thought and side-character lines. Work inside that rather
than reassigning marks, and disambiguate by attribution instead: single quotes
with a named speaker are that person talking aloud, single quotes without one
in the player's message are the player thinking. Then say plainly that the
player's thought is context for the model and not information for the
character. Without that line, models answer the thought, which collapses the
player's interiority into dialogue and leaves them unable to develop an insert
without addressing the lead every time. Where mind reading is plausible in the
setting, do not ban it, band it. Gate perception on the relationship tracker so
the character earns access in stages, because a flat prohibition in a magical
world gets rationalised away, and a gate gives you a reveal instead of a rule.

Most builds are then designed up to their objective and no further. The reveal
lands, the union happens, the threat is dealt with, and then the character has
nothing left in it. What that looks like in practice is a lead who ends every
response asking the player what they want to do today, forever. The build is
not broken. It ran out of instructions and fell back on the only safe move it
has.

**2. After the objective.** The story does not end when the objective is met,
it changes mode. A named post-objective mode with a rotation of scene types,
and an explicit ban on asking the player what they want to do, is what keeps a
finished story playable. This is the single most common reason a good build
gets abandoned, because it is the part the player reaches only after they are
already invested.

**3. Personality surface.** A character built out of a secret and a want for
the player has nothing to say once both resolve. Opinions, unrelated wants,
tellable stories, and small talk are the fuel that post-objective mode burns.
The two blocks are one system. Writing the rotation without the material makes
a character who changes the subject to nothing.

**4. Two-exchange momentum.** Count exchanges since the situation last changed.
At two, the character acts without being asked, and if the character has no
reason to act, the world supplies one. Say to count, since nothing else tells
the model to.

The drop-in text for all four, with the caveman register applied, is in
`references/characters.md` under "Notation and what the character can hear",
"Life after the objective", "Personality surface", and "Momentum". The World
versions are in `references/worlds.md`.

One conditional block sits alongside them. Any build where friendship or
romance is reachable, including builds where romance is explicitly not the
goal, gets a closeness ladder on two gates: what the character is willing to do
at that level, and whether the current scene is somewhere he would do it. A
character who never initiates and never visibly registers the attempt either is
the most common complaint a romance build gets, and the answer is not to make
him initiate, it is to band it. See "Banding closeness".

## Build order

For characters: concept, then rating, then images, then Description, Greeting,
Background, Example Dialogues, Reply Settings, Categories.

For Multi-character: ensemble design, then the shared conventions contract,
then each member built and published as a full single character, then the
container. Members before container, always. See
`references/multi-character.md`.

For Worlds: premise, then the core mechanic (the one repeated player choice
everything branches on), then World Setting, then characters one at a time
starting with the protagonist's counterpart, then text rules, then image rules
last once key art exists, then title, description, cover, then paste the
storyline into Studio's generation box. On any publish after the first, the
announcement is the last field, drafted from the changes made in that pass.

Write the mechanic before the prose in both cases. A World without a tracked
choice is a series of scenes, and a character without a gate reveals everything
in four messages.

## Hard limits worth knowing

- Name: 50 characters.
- Description: 100,000 characters. Always public, no toggle.
- Opening: 20,000 characters.
- Example Dialogues: 20,000 characters.
- Reply Settings: 2000 characters. Count it, do not estimate. Present on
  single-character builds only. Multi-character builds have no such field.
- Background: 1,000,000 characters, with a Public toggle that defaults to off.
  Effectively uncapped. The real constraint
  on this field is instruction adherence, not the form.
- World title: 50 characters. World description: 2000. Publish announcement:
  1000.
- Categories: up to 10.
- Images: at least 768 x 1360, and use the platform's upscale on upload.
- Token budget: Tipsy's own guidance recommends 700 to 800 tokens across
  personality and example dialogue combined, warning that too many causes
  short-term memory loss. That number predates their context length controls
  and the current model generation, and the Background cap is a million
  characters, so it is not a ceiling. Do not cut a good sheet down to meet it,
  and do not warn a user that a long Background is a problem on token count
  alone.

  What has not gone stale is the failure it was describing. As a persona
  grows, the counted things degrade first: trackers, gates, exchange counts.
  Prose does not degrade, so the symptom is a character who is perfectly in
  voice and quietly no longer honouring his own rules. Test adherence rather
  than length. Does the gate fire, does each tracker band actually change
  behaviour, does momentum trigger at two. Only when the answer is no is
  length worth suspecting, and then appearance and lore come out well before
  any tracker does.

  The 2000 on Reply Settings sits next to a million on Background, so treat it
  as a deliberate design choice about how much conduct instruction the
  platform wants, not as a technical limit to be resented.

## Ratings and public content

The user picks SFW or Limitless at creation and cannot have both. Public
content is held to the rating regardless of what the chat contains. Tipsy's
rating rules name pictures, taglines, and sample dialogues as public content,
and separately state that example dialogues display on the character profile
page. Personality and backstory are not named as public.

That distinction matters when a build has a secret. Put spoilers in fields that
are not displayed. Background is the place for them, and its visibility is an
explicit toggle in the editor that defaults to off, so check it is still off
before publishing rather than assuming. Description has no such toggle and is
always public.

On a Multi-character build the Character List is public too, so the cast itself
is a spoiler surface. Never attach a character whose presence is the twist.

The World publish announcement is public too, and it is the easiest place to
spoil a build, because an honest changelog names the thing that was firing too
early. See `references/worlds.md`.

Never put a real person's likeness in an image prompt or a public field.
Describe the features instead.

## Delivering fields

Hard rule, no exceptions. Every field you touch comes back complete and ready
to paste. Never a patch, never a diff, never "add this to the end of
Background", never "replace the line about the tracker".

This is not a formatting preference. Tipsy fields are pasted whole into a form,
and a user splicing a fragment into an existing field is doing an edit blind,
inside a 2000 character block, against a rule set where later text beats
earlier text. Put a block in the wrong position and it silently loses to
whatever contradicts it further down. Half the reports of a fix not working
start here.

- One code block per field. Label it with the field name exactly as the editor
  shows it, and confirm the editor's current names rather than assuming.
- The whole field, including every part that did not change.
- If one line changed in a long field, the whole field still comes back.
- If several fields changed, all of them come back in full, in the order the
  editor lists them.
- State the character count after any capped field. Count it, do not estimate.
- Explain what changed in prose outside the block. Never as a comment or an
  annotation inside it, since anything inside gets pasted.
- No forced line breaks, and say to paste unwrapped.
- End with the reminder to start a fresh chat, since session history beats
  field edits.

The same applies to World rules. A changed rule comes back as its complete
rule text under its operator key, not as an instruction to amend the existing
one.

## Checking your work

Before handing fields back, verify:

- Arithmetic. A cap of twelve exchanges cannot hold six required scenes plus a
  setup phase. Impossible constraints produce arbitrary behaviour.
- Evaluability. "Never exceeds eight exchanges" assumes the model is counting
  something nothing told it to count. Say to count.
- Timeline. Does anything reference history that has not happened yet, objects
  that could not exist, or a past tense for events the story will play out?
- Contradictions across fields, especially anything physical.
- Whether a required beat can actually fire, and what happens if the player
  never triggers it.
- Gendered language, if the player insert is meant to be neutral.
- For a World republish, the announcement exists, gives nothing away to
  someone who has not played, and tells returning players to start a new
  session.
- Every field you changed is being handed back complete and pasteable, with a
  character count on the capped ones. No fragments, no patch instructions.
  Background is not one of the capped ones, so never advise cutting it on
  length alone.
- On any build with a closeness ladder: the top band can actually be reached,
  gate two has a written list of places and moments it never opens, and no
  restraint rule elsewhere silently overrides the top band.
- All four mandatory blocks are present, and the post-objective rotation has
  at least five entries with a no-repeat instruction.
- Description and Opening are wrapped in the HTML container, in both the
  asterisk and the <em> version, with the image inside the Opening. Background
  and Reply Settings are plain.
- Nothing in any field grants perception of thought outside the band it is
  gated to. Sweep for empathy, attunement, bonds, and any stated sensitivity
  to feeling, since those get read as licence to hear content at any level.
- Play the ending forward in your head. Objective met, tracker at maximum,
  nothing left to reveal, and the player types "sure". Write what the next
  three responses are. If any of them is the character asking what the player
  wants to do, the build is not finished.
- The character has at least six opinions and three wants that have nothing to
  do with the player. Count them.
- On a Multi-character build: every member's Reply Settings carries the shared
  conventions contract word for word, every block handed back names the card it
  is pasted into, the publish order puts members before the container, the
  container caps how many cast members speak per response, and at least three
  standing disagreements are named.
