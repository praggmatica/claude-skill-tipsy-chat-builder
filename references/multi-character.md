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

## Field map, confirmed September 2026

Captured with the Type toggle set to Multi-character. The form is not the
Character form with one field missing. Four things a single character has are
absent here: Main Character Gender, HTML Styling, Sound, and Reply Settings.
One thing is added: the Character List.

| Field | Cap | Public | Notes |
|---|---|---|---|
| Character images | 10 images, at least 768 x 1360 | yes | upload or generate, reorder, choose main avatar, Watermark toggle default on, see `references/images.md` |
| Dynamic Cover | GIF, MP4, or WebP, 9:16 | yes | toggle, default off, upload MP4 |
| Name | 50 | yes | required |
| Type | n/a | n/a | Character or Multi-character, required |
| Description | 100,000 | yes, always | required, markdown only, on the card and at the top of chat |
| Opening | 20,000 | yes | required, markdown only, placeholder asks for quotes and asterisks |
| Background | 1,000,000 | toggle, default off | placeholder reads "your characters'", plural |
| File upload | 2MB each, 10 files | no, private | always on the form here, JSON only, never TXT, retrieved only when relevant, see `references/knowledge-files.md` |
| Rating | n/a | n/a | Limited or Limitless, required |
| Visibility | n/a | n/a | Public or Private, required |
| Tag | 10 | yes | same rating-dependent picklist, rotating event slot |
| Character List | at least 2, maximum unconfirmed | yes | required, published characters only for public stories, editor warns that more characters cost more |
| Conversation Style | n/a | unclear | Default, Safe for Work, Romance, Flirty |
| Example Dialogues | 20,000 | yes | placeholder still shows `{{char}}:` |
| Creator's Note | 2,000 | treat as yes | tips for players, see `references/characters.md` |

The Preview pane shows a browse card rather than a chat, so the Opening cannot
be checked there. Check it in a test chat after publishing privately.

**No HTML Styling.** Description and Opening are plain markdown on a container:
asterisks for narration, double quotes for speech, `![alt](url)` for images.
The HTML presentation rules in `references/characters.md` do not apply, and
neither does the choice between styled fields and knowledge files. A container
always has its upload field. That makes the container the natural home for an
ensemble's world file.

**No Sound.** The container has no voice of its own. Whether each member's
voice, set on its own card, plays in the ensemble scene is untested.

**No Main Character Gender.** The container does not declare a lead. If the
story has one, say so in the container Background.

**The Character List warns about cost.** The editor reminds creators that too
many characters affect both experience and cost. Every member is a full card in
context, so each one added raises what every player pays per message. Two to
four is the sensible range until a build proves it needs more, and it matches
the two-or-three-speakers cap under "Turn-taking".

**There is no Reply Settings field.** Conduct is not authored at the container
level, because each attached character carries its own Reply Settings from its
own card. The container cannot override them and cannot see them.

## What that means for how you build

Every conduct instruction the ensemble shares has to be identical in every
member's own Reply Settings, written before that member is published, because
the container has no way to impose it afterwards. This is the single hardest
thing about the surface and the reason the build order below is not optional.

## Build order

1. Design the ensemble. Who is in it, whose story it is, who leads it if
   anyone does, and what the repeated situation is that keeps producing scenes. Settle
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

**Voice may complicate this.** Tipsy's guide says double-quoted text is read
in the main character's voice. The container has no Sound field, and nobody has
confirmed whether members' own voices follow them into the scene or whether one
voice reads every quoted line. Keep a name attribution on every spoken line
regardless, and if any member has a voice set, tell the user to listen to a
two-speaker exchange in a test chat before publishing.

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

## Knowledge files across a cast

Files reintroduce the problem the missing Reply Settings field creates, in a
field the shared conventions contract does not cover.

Every member is a published single character that may carry its own files, and
the container has an upload field of its own. **Nobody has confirmed whether a
member's files reach the ensemble scene, or whether the container's files do.**
Both unknowns bite:

- If member files travel, a four member cast carrying four world files means
  four overlapping key sets firing at once, several near-identical entries
  about the same place competing for one budget, and any drift between
  members' versions of shared lore surfacing as the cast contradicting each
  other about their own world.
- If member files do not travel, lore a member depends on silently vanishes in
  the ensemble, and that member behaves differently there than it does solo.
  That is the conventions-contract bug again, in a place the contract cannot
  reach.

### Test it, it takes ten minutes

Two tests, because there are two unknowns. Run both before designing around
either.

**Does a member's file travel?** Publish a throwaway single character carrying
one file with one entry, keyed on an invented token no model could guess, whose
content states a checkable fact. Attach it to a two member container and put no
file on the container. Fresh chat, then ask out of character about the token. A
correct answer means member files travel.

**Does the container's file reach the scene at all?** Same setup inverted. The
file goes on the container only, no files on any member, invented token again,
fresh chat, ask. A correct answer means container files work, which is the more
fundamental of the two and worth confirming before relying on the container as
the canonical home.

### Placement until the results are in

The rule turns on whether the cast members are also meant to be chatted with
solo, so settle that at ensemble design time along with the rating.

**Cast assembled only, never played solo.** World file on the container, no
files on any member. This is correct whichever way the first test lands, so it
needs no result, and it is the reason to prefer a purpose-built cast when the
choice is open.

**Members also played solo.** Give each member the slice of the world its own
solo build actually needs, give the container the full world file, and make any
entry that appears in more than one place byte identical. If container files
work and member files do not travel, this is exactly right and the duplication
costs nothing, because the two copies never coexist. If member files do travel,
the cost is limited to the overlapping entries only, which is why the slices
should be as small as each solo build tolerates.

Either way, author one canonical world file and cut member slices from it.
Never write a member's file separately, because separately authored lore drifts
and drift is the failure that reads as the cast arguing about their own world.

### Keys across cards

The within-file collision sweep in `references/knowledge-files.md` becomes a
cross-card sweep here. Two members keying the same word is invisible from
inside either file and only shows up in play. List every key across every card
at once. Where two cards legitimately need the same word, the entries behind it
should be the same entry.

### Editing compounds

A shared world file changing is not one re-upload, it is one per card that
carries it, plus a republish each, plus the fresh chat rule for every build any
of those members appears in. Whether Tipsy replaces a file of the same name or
requires deleting the old one first is unconfirmed, so tell the user to check
rather than assuming the upload overwrites.

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

These were not visible in the Multi-character form in September 2026 and
should be checked rather than assumed:

- Maximum cast size.
- Whether other creators' published characters can be attached, or only your
  own.
- Whether attaching a character exposes any per-member fields, such as a role or
  relationship label.
- Whether a Limited container can hold Limitless members. The skill assumes not.
- Whether Conversation Style on a container applies its posture to every
  member, and which wins when a member's own card was published with a
  different setting. The tooltip for each option is captured in
  `references/characters.md`.
- Whether a member's voice, set under Sound on its own card, plays in the
  ensemble scene, and whose voice reads a quoted line if not.
- Whether a member's extra images become chat background options inside the
  ensemble.
- Whether a member's knowledge files reach the ensemble scene, and whether the
  container's own files do. Both are testable in ten minutes, see above.
- Whether uploading a file of the same name replaces the previous one or
  requires deleting it first.
- Whether review reads file contents. They are private to players, which is not
  the same as being outside the rating. Until this is answered, do not treat a
  private file as a safe harbour for content the build's rating does not
  allow.
