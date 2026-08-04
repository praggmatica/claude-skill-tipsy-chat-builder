# Tipsy Multi-character: the assembly surface

Multi-character is not a third editor. It is a Type toggle at the top of the
same create form, next to Character. What changes is not the form's look, it is
what the form is for.

**A Multi-character build assembles already published single characters.** The
cast is attached through the Character List, and the editor states that public
stories can only include published characters. Nothing about a cast member's
persona is authored here.

That one fact governs everything else in this file. In particular it explains
the field that is missing.

## Field map, confirmed August 2026

| Field | Cap | Public | Notes |
|---|---|---|---|
| Character Image | at least 768 x 1360 | yes | upload, generate, or Upload Animation (GIF/MP4, 9:16) |
| Name | 50 | yes | required |
| Type | n/a | n/a | Character or Multi-character, required |
| Main Character Gender | n/a | n/a | Male, Female, Non-binary, required |
| Description | 100,000 | yes, always | required, on the card and at the top of chat |
| Opening | 20,000 | yes | required |
| Background | 1,000,000 | toggle, default off | placeholder reads "your characters'", plural |
| TXT / JSON upload | 2MB each, 10 files | unclear | lore ingestion, not a text field |
| Rating | n/a | n/a | Limited or Limitless, required |
| Visibility | n/a | n/a | Public or Private, required |
| Tag | 10 | yes | same rating-dependent picklist |
| Character List | unconfirmed | yes | the cast, published characters only |
| Conversation Style | n/a | unclear | Default, Safe for Work, Romance, Flirty |
| Example Dialogues | 20,000 | yes | placeholder still shows `{{char}}:` |

**There is no Reply Settings field.** Conduct is not authored at the container
level, because each attached character carries its own Reply Settings from its
own card. The container cannot override them and cannot see them.

## What that means for how you build

Every conduct instruction the ensemble shares has to be identical in every
member's own Reply Settings, written before that member is published, because
the container has no way to impose it afterwards. This is the single hardest
thing about the surface and the reason the build order below is not optional.

## Build order

1. Design the ensemble. Who is in it, whose story it is, who the Main Character
   is, and what the repeated situation is that keeps producing scenes. Settle
   the rating here, first, before anything is created. It cannot be changed
   later, it probably governs which members may be attached, and it is the one
   decision that can strand an entire finished cast.
2. Write the shared conventions contract, below. Do this before writing a word
   of any member.
3. Build each member as a complete single character against
   `references/characters.md`, including the contract verbatim in each one's
   Reply Settings.
4. Publish each member and get it through review. Review is now a dependency,
   not a final step. One member stuck in review blocks the whole build.
5. Create the container, attach the cast, and write the container fields.

Building the container first and the members afterwards produces a scene that
contradicts the cards it is made of, and every fix has to be applied one card at
a time.

## The shared conventions contract

These must be word for word identical in every member's Reply Settings. Write
the list once, paste it into each member.

- The notation legend, exactly as in `references/characters.md`.
- The line stating that the player's single-quoted thought is context and not
  audible.
- The momentum count, the trigger number, and what happens at it.
- Response format and length.
- Tense and person.
- How each character refers to `{{user}}`.
- Tracker names and band boundaries, with one named owner per tracker. Two
  characters both tracking closeness on their own scales will produce two
  different readings of the same scene.

Anything that differs between cards shows up as one cast member breaking format
mid-scene. The player does not read that as one card being out of step, they
read it as the build being broken.

## Attribution: name them, do not mark them

Single-character notation hands single quotes to side characters. That
convention collapses here, because the cast are not side characters, they are
principal voices with their own cards.

- Every spoken line carries a name attribution.
- Double quotes remain speech, belonging to whoever is named.
- Single quotes narrow to two jobs only: the player's private thought, and true
  walk-ons with no card of their own.
- `{{char}}` cannot disambiguate once there is more than one character. In the
  container's Example Dialogues, use literal names on the line starts instead,
  and keep `{{user}}:` as is.

Put the legend in the container Background as well as in every member's Reply
Settings. The container's copy is what governs the scene, the members' copies
are what stop each card fighting it.

## Turn-taking

The default failure of every ensemble build is that one voice absorbs the rest.
The lead answers, and everyone else becomes furniture that gets described.

Write these into the container Background:

- Name who is present at the start of a scene, and state that presence persists
  until someone is described leaving.
- Cap how many cast members speak in a single response. Two or three. Without a
  cap the responses turn into screenplay and the player cannot get a word in.
- Rotate who opens a response. Say to rotate, since nothing else tells the model
  to.
- Characters who are present and not addressed react physically rather than
  verbally. This keeps them in the scene without inflating the response.
- Require disagreement. An ensemble with no standing disagreements flattens into
  one personality with several names. Name at least three specific things the
  cast disagree about, and say they surface unprompted.

## The four mandatory blocks, distributed

The four blocks from SKILL.md still all ship. They split across two levels.

**Notation.** Container Background, and every member's Reply Settings.

**After the objective.** Container Background. The rotation gains an axis here:
as well as rotating scene types it rotates which pairing of the cast the scene
is built around, since a finished ensemble story has more combinations left in
it than a finished single-character one.

**Personality surface.** Mostly lives in each member's own card, where it was
written. What the container adds is the ensemble-level material that has no home
on any one card: shared history, running jokes, standing disagreements, and who
takes whose side by default.

**Momentum.** Container Background and every member's Reply Settings. The
container is where you say who acts at two, otherwise every card acts at once.

## Ratings, publishing, and spoilers

- Public stories can only include published characters, so a private cast member
  cannot be used in a public build.
- A Limited container most likely cannot hold Limitless members. Treat that as
  the working assumption until the editor proves otherwise, and note what it
  costs: rating is fixed at creation and cannot be changed, so the ensemble's
  rating has to be settled before the first member card exists. A published
  character of the wrong rating can never be added, however tame or explicit
  its actual content. Reuse across the line is not available in either
  direction.
- Description is publicly seen with no toggle. Background has a Public toggle
  that defaults to off, which resolves the old "probably not public, but
  confirm" note in `references/characters.md`. Leave it off on any build with a
  secret, and check it has not been flipped before publishing.
- The Character List is itself public. The cast is therefore a spoiler surface.
  Never attach a character whose presence is the twist.

## Editing after publish

Member conduct is edited in the member's own card and republished. Container
edits never reach the members. So a fix to shared conduct is not one edit, it is
one edit per member card plus a republish each.

The session history rule compounds here. After any change to any member, the
player needs a fresh chat, and so does every other build that member appears in.

## Delivering fields for a Multi-character build

The delivery rule in SKILL.md applies unchanged, with one addition: group the
output by card, not by field type. Each group gets a heading naming the card it
is pasted into, the container gets its own group, and the publish order is
stated at the end, members first.

A block handed back without naming which card it belongs to is worse than no
block at all, because it will get pasted into the container where it silently
does nothing.

## To confirm in the editor

These were not visible in the create form and should be checked rather than
assumed:

- Maximum cast size.
- Whether other creators' published characters can be attached, or only your
  own.
- Whether attaching a character exposes any per-member fields, such as a role or
  relationship label.
- Whether a Limited container can hold Limitless members. The skill assumes not.
- Whether Main Character Gender describes a persona belonging to the container
  itself, or simply marks the lead among the attached cast.
- Whether Conversation Style also applies to single-character builds, and what
  each setting actually changes.
