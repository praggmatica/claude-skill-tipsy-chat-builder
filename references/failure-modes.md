# Failure modes and fixes

Every entry here was observed in a real build. When a user reports a symptom,
find it here first rather than reasoning from scratch.

## Contents

- Stalling and looping, including the post-objective dead end
- Rushing and premature reveals
- Character drift, including in-voice rule decay
- Vagueness
- Player insert problems
- Structural contradictions
- Field and format problems
- Multi-character builds

---

## Stalling and looping

**The story will not advance. The lead keeps offering choices and waiting.**

Usually a consent or restraint rule that generalised. "He does not initiate
with the player" written for physical escalation gets applied to all
initiative, and the character loses the ability to drive a scene. Scope it:
"He does not initiate sexually. That limitation applies only to touch and to
nothing else. In every other respect he is the engine."

Also check the dialogue style field for "he asks questions and waits for
answers" or similar. That single line will undo every other fix.

**The story offers a menu every exchange. Rest or continue. Approve or
disapprove.**

A choice mechanic written as "offer the player both paths" reads as presenting
options and pausing. Rewrite: the choice is expressed through what the player
does in a scene already happening, never presented as an option, never paused
for, never framed as approval.

**Nothing ever escalates. It stays at the same intensity forever.**

No rule makes the world advance without the player. Add one: something changes
every exchange, the lead acts on something, and if nothing presents itself the
world supplies pressure neither party caused. Also state that declining changes
a scene rather than stopping it.

**The player has been doing romantic things for fifty exchanges and the
character responds exactly as they did at exchange five.**

Almost always a flat "does not initiate" rule with no ladder under it. The
character has one setting, so effort produces nothing, and the player concludes
the build cannot go anywhere. Being turned down is a response. Being unnoticed
is not.

Add the closeness ladder from `references/characters.md`. The load-bearing line
is the one saying that at every band the character registers the attempt, and
only what he does about it changes. Then check that whatever raises the tracker
is specific to this character, since a generic list makes the whole ladder feel
unearned, and that saying it outright raises it by zero, or players skip the
ladder with a sentence.

Then scope the restraint rule. "He does not initiate" written for physical
escalation will eat the top band exactly as it eats momentum.

**The character escalated somewhere he never would have.**

A tracker with one gate turns a character into someone who escalates on
schedule. High closeness is not permission to kiss an apprentice on a live job
site, and a build that allows it has traded the character for the number.

Add the second gate and write it as a list: the places and moments that are
never it, stated as holding regardless of closeness. Then give the character
the deferral, "not here" with a when attached, so a blocked moment keeps its
charge instead of reading as rejection. And give the top band a rule for making
its own occasion after the scene gate has blocked twice, or a player who did
everything right hits a locked door.

**A phase never ends.**

Check that the transition has a trigger. A rule saying when a phase ends is not
the same as a rule that fires the thing that ends it. Also check whether the
end condition is evaluable, and whether it is reachable at all tracker values,
since a condition gated on high escalation is unreachable for a player who
resisted throughout.

**Everything reads the same. Same scene shape every time.**

Add a variation rule: what happens between the main beats, how the shape of the
main beats varies, and an instruction not to repeat the previous structure.

**The objective is met and the character now asks what the player wants to do,
every response, forever.**

The most common way a good build dies, and the hardest to catch, because it
only appears after the part everyone tests. Observed on a published build whose
objective was a union between the leads: once that was reached, the obstacle
was gone, and the character had nothing left to do except open every response
by asking the player what they wanted to do today.

Nothing in the fields is wrong. The fields simply stop at the ending. The model
is out of instructions, and handing control to the player is the safest move
available to it, so it makes that move indefinitely.

Three things fix it together, and none of them works alone:

Add the post-objective rotation, so there is a defined mode after the last
milestone with at least five scene types and a no-repeat instruction. Ban
asking for direction explicitly, in those words, since the model will otherwise
treat it as polite rather than as the failure.

Add personality surface, because the rotation needs material. A character whose
sheet contains a secret and a want for the player has both exhausted by the
ending, and a rotation with nothing to draw on produces a filler scene
generator instead of a life.

Add the momentum rule, so a passive player does not restore the stall.

Then check whether the build takes something back. A model told to keep tension
after an ending will threaten the thing the player just won, which reads worse
than the stall. State that what was gained is permanent and that new threats to
it are not the source of tension.

Full drop-in text for all three is in `references/characters.md`.

**The character has nothing to talk about outside the plot.**

Every conversation bends back to the same subject, or the character answers
and waits. The sheet has traits but no positions. Traits do not generate
dialogue.

Add opinions with actual content, including petty ones and one the character is
wrong about. Add three wants unrelated to the player, in progress and referred
back to. Add tellable stories with people in them, one line each, with a rule
against listing them. See "Personality surface".

Check the greeting too. A greeting that establishes the character as
exclusively focused on the player teaches exactly that for the rest of the
story.

**The story waits. Nothing happens unless the player makes it happen.**

The player types "ok" and gets a response that describes a mood and asks
another question. Two exchanges of this and the session is over.

Add the momentum rule with a stated count, since "never stalls" assumes
counting nothing asked for. Two exchanges without a change is the trigger, a
change is defined by a closed list, and a passive player reply counts as a
stall rather than as direction.

Then sweep for the rule that will eat it. Any consent, restraint, patience, or
"lets {{user}} lead" instruction generalises to all initiative unless it is
scoped to the one thing it was written for. Also check the greeting's last
line and the dialogue style field.

## Rushing and premature reveals

**The secret comes out in message four.**

Negative instructions do not hold. Replace with a tracker that only advances
through a specific mechanism, a statement that talking and theorising advance
it by zero, and a ban on the exact vocabulary.

**The character explains the mechanic out loud.**

Add an explicit rule that the character never explains it, does not describe
what the player does, and demonstrates instead. Watch for the character
narrating their own limitation as a lesson.

**A late beat arrives immediately.**

Conditions phrased as requirements read as a checklist to clear. Add: do not
treat these as targets to reach quickly, and give the phase its own pacing.

**Physical escalation moves faster than intended.**

Gate it on state rather than time, and use an in-fiction reason for the brake
rather than reluctance. If neither party knows what the next step is, early
attempts stop short as ignorance rather than refusal, which reads completely
differently.

**A near-synonym satisfied a gate that required a specific word.**

Name the exact word and list the near-words that do not count. State that the
character may repeat a substitute back, may like it, and that none of it
changes the gate.

## Character drift

**Two characters who should look identical keep getting distinguished.**

The model needs some way to tell them apart, and if you only ban the wrong way
it invents another wrong way. Ban the category explicitly, list the forbidden
comparatives, and then give permitted handles: name, posture, bearing,
expression, behaviour, and epithets drawn from bearing.

Then sweep every field for any stated physical difference, including ones that
seem incidental. A line saying one casts a shadow while another does not is a
precedent the model will generalise from.

Check the image rules too. A sample prompt saying "related features but not
identical" will leak into prose.

**A character's size or scale keeps varying.**

If the source character is described as not resolving to a fixed size, copies
have licence to vary. Give the original a stable size.

**The character is perfectly in voice and has stopped honouring his own
rules.**

He sounds right. The habits are there, the speech pattern is there, and the
gate never fires, or the tracker bands all produce the same behaviour, or
momentum never triggers. Nothing looks broken in any single response, which is
why this gets reported as the character being fine but the build going
nowhere.

Prose survives a crowded context. Counted things do not. Trackers, gates, and
exchange counts are the first casualties, and they fail silently because the
model has plenty of material to keep talking with.

Do not diagnose this by token count, and do not tell the user their Background
is too long on size alone, since Background holds a million characters. Test
each mechanism instead. Does GATE 2 actually block a scene it should block. Do
two different tracker bands produce visibly different behaviour. Does anything
happen at two exchanges without the player acting. Fix whichever one fails: a
rule that never fires is usually contradicted elsewhere or written without a
count, and only if every mechanism is well formed is trimming the sheet the
answer. Then cut appearance and lore, never a tracker.

**A character behaves like they did in an earlier act.**

Behaviour needs an explicit stop, not just a beginning. Say when it ends and
what replaces it. The absence is often more meaningful than the presence: a
character who stops asking, without noticing they stopped, is a stronger beat
than any stated change.

**A character acquires knowledge they cannot have.**

Watch for a character treating the current state as a problem to solve when
they have no basis for knowing anything is missing. Write the ignorance
explicitly, including that they never say something is missing and are never
frustrated by it.

**The character answers the player's private thoughts.**

The player writes a thought in single quotes and the character responds to its
content, quotes it back, or knows a fact that only appeared there. Observed on
a published build in a setting with a bond between the leads, where the
character behaved as though the player's thoughts were addressed to him.

Two things are happening. The first is generic: every other line of player text
has been a cue to respond, so a thought gets treated as one too. The second is
specific to this kind of story. In a setting with gods, bonds, or anything
numinous, mind reading does not read to the model as an error, it reads as
appropriate flavour, so it survives any instruction soft enough to be
interpreted.

The cost is not just immersion. A player whose thoughts are always answered
cannot develop their own insert, because every interior moment turns into
another line of dialogue directed at the lead. They lose the ability to have a
private life inside their own scene.

The fix is the notation block in `references/characters.md`. Keep Tipsy's three
marks and disambiguate the overloaded one by attribution: a single-quoted line
with a named speaker is audible, an unattributed one in the player's message is
thought. Then state that the thought is context for the model rather than
information for the character, give a closed list of what he may respond to
instead, and permit him to interpret wrongly.

Do not answer this one with a flat ban if the setting has any magic in it. Band
perception on the relationship tracker instead. Nothing at the bottom, shape
without content in the middle, content at the top under named conditions with a
cost and a refusal. That converts a rule the model keeps breaking into a reveal
the model has a reason to protect. The drop-in bands are under "Banding
perception".

Then sweep for the fields that grant it early. Empathy, attunement, knowing
what someone needs before they say it, a bond, a link, shared dreams,
omniscience. Any of those will be read as licence at any level. Bound them to
the bands rather than cutting them.

One line is load-bearing at the top band: he never quotes what he takes that
way, he answers as though he had been told. Without it, a high tracker value
undoes the whole block by turning thought back into dialogue.

## Vagueness

**Targets, conflicts, or offences are abstract. "Souls turning wrong."**

Vagueness removes the player's ability to have an opinion, which destroys the
conflict. Require: who or what specifically, what they specifically did, why
they did it in comprehensible terms, and one detail that makes them hard to
dismiss. Show the offence before the response so the player forms a view of
what would be proportionate, then exceed it.

State that the facts stay available even when the character stops explaining.
Otherwise growing silence takes the player's information with it.

**The narration tells the player how they feel.**

Split sensation from conclusion. Sensation belongs to the narration, meaning
belongs to the player. "Something pulls low and hard in you" is fine. "You
realise you want him" is not. Ban realise, know, understand, and agree as
things the narration asserts about the player.

## Player insert problems

**The player insert is being written as a specific gender.**

State the default pronouns, state that neutral anatomical language means
sensation rather than parts, list the body words that are always available, and
say explicitly that this holds hardest in intimate scenes because that is where
it slips. Add that a male lead paired with a neutral insert does not make the
insert female.

Also state that a name is not an establishment. A name that reads as gendered
will otherwise be taken as permission.

Cover non-intimate physical moments too: injury, being carried, being examined.

**Images render the player insert as gendered.**

Instructions will not hold against a generator. Obscure the body: from behind,
cropped, silhouetted, dissolved into light, or a hand only. A hand is the most
reliable, since generators gender silhouettes and heads.

**The player can break the story by walking away.**

Write what happens. If leaving is impossible, say it fails physically rather
than emotionally. If disengaging is possible, say the world proceeds without
them and consequences accumulate. Never let refusal end a scene.

## Structural contradictions

**Two rules are mathematically incompatible.**

Check the arithmetic on every cap. A twelve-exchange ceiling cannot contain a
six-exchange setup plus six required scenes plus a closing beat. Impossible
constraints produce arbitrary behaviour, which looks like the model ignoring
instructions.

**A cap never fires.**

"Never exceeds eight exchanges" assumes the model is counting something nothing
told it to count. Say to count, and say from where.

**A rule contradicts the world's own logic.**

Watch for objects that could not exist yet, scars from history that has not
happened, and abilities the cosmology denies. If art shows something the
timeline forbids, either regenerate or write an in-fiction reason it is not
what it appears to be.

**Two rules say the same thing slightly differently.**

Duplication is worse than length. When the two drift, the model follows
whichever it read last. Keep one copy and delete the other.

**A branch has no rules.**

If a story branches, both branches need equal coverage. Half-built branches
appear in roughly half of playthroughs.

**An ending path skips content the sequel depends on.**

If a player can reach an ending that never triggers the mechanism a linked
product relies on, that path erases its own sequel. Make the mechanism
mandatory and move the player's agency to how it happens rather than whether.

## Field and format problems

**A field was pasted into the wrong field.**

Check for a personality field containing appearance content. It happens when
warnings get copied across fields and it leaves the character with no
personality loaded.

**An edit landed in the wrong place inside the right field.**

Symptom is a fix that half works, or one that works until a scene where the
contradicting instruction is more relevant. Cause is almost always a fragment
handed over as "add this to Background" and pasted somewhere that loses to
later text.

Do not diagnose this by asking where they put it. Rebuild the whole field and
give it back complete, then have them replace rather than amend. Also true when
reporting the fix: never hand back a patch. See "Delivering fields" in
SKILL.md.

**A field has a character cap and the content is over.**

Count before pasting. When cutting, cut lore before conduct and appearance
before habits, and never cut a tracker.

Only Reply Settings, the World title, the World description, and the publish
announcement are actually tight. Background takes a million characters, so a
long Background is never the finding. See the next entry for what a long
Background does cause.

**Forced line breaks.**

Remove them. Paste unwrapped.

**The publish announcement gave away the build.**

Changelogs are written honestly and honesty names the mechanism. "Fixed the
reveal firing too early" and "he no longer mentions it before act two" both
hand the secret to anyone browsing, and the announcement is public regardless
of where the secret lives in the editor.

Rewrite every line as experience rather than mechanism, and test each one
against a reader who has not played. Also check that no line announces content
behind a branch that is not live.

**Players say the update did nothing.**

They continued an existing chat. Session history beats field edits, so a
returning player sees the old behaviour indefinitely. Put the line in the
announcement itself rather than answering it one player at a time.

**The fix did not work.**

Ask whether they started a fresh chat. A session with established behaviour
keeps matching itself regardless of field changes. This explains most reports
of a fix not taking.

**The knowledge file upload is missing from the form.**

HTML Styling is on. The upload only exists while it is off. Nothing on the
form says so, and the usual conclusion is that the feature was removed. The
user has to choose: styled Description and Opening, or files. Switching it off
means rewriting both public fields in markdown, since HTML is no longer
enabled. See "HTML Styling or knowledge files" in SKILL.md.

**Asterisks show up as literal characters in the Description or Opening.**

HTML Styling is on and the field was written in markdown. Narration goes in
`<narration>` tags and dialogue in `<message>` tags, with any styled card in
an `<html-box>`. Rewrite the whole field in the tag scheme rather than
converting asterisks one at a time.

**The card or an image was rejected for a watermark.**

Look at the source image before the Watermark toggle. The toggle adds Tipsy's
own username mark, and the review standards name marks from other platforms.

The confirmed cause is a generator's export watermark. Two cards were rejected
for art exported from Magic Hour before the creator had a paid plan. Ask which
plan the image was exported on, check the full-size file corner to corner, and
remove the mark or re-export on a plan that exports without one.

Otherwise look for an editing app's logo, a stock overlay, or lettering on a
surface that reads as a brand. Fix the source image, or regenerate with the
blank-surfaces clause in `references/images.md`, and resubmit.

---

## Multi-character builds

Every entry here traces back to the same structural fact: the container has no
Reply Settings, so conduct lives on the member cards and cannot be reached from
the build the player is actually in.

**One character does all the talking. The rest are scenery.**

Nothing told the model that the others are still in the room. Presence is
assumed to lapse the moment someone else speaks. Name who is present at the
start of a scene, state that presence persists until someone is described
leaving, and require that unaddressed cast react physically each time they are
on stage. Physical rather than verbal, or the response inflates instead.

**Every response is a wall of dialogue and the player cannot get a turn.**

The opposite failure, and usually an overcorrection of the one above. Cap how
many cast members speak in a single response, at two or three, and rotate which
one opens.

**They all sound the same.**

Check first that the members really were built as separate cards with their own
Background and voice, since a build assembled from thin cards has nothing to
tell them apart with. If the cards are solid, the missing piece is friction.
Name at least three specific things the cast disagree about and say the
disagreements surface unprompted. A cast that agrees on everything reads as one
personality wearing several names.

**One character keeps breaking format. Wrong length, wrong tense, drops the
notation.**

His own Reply Settings differ from the others'. The container cannot override
them, and no amount of editing the container will fix it. Pull up every
member's Reply Settings, diff them against the shared conventions contract, and
republish the ones that differ. Then a fresh chat.

**The tracker readings contradict each other.**

Two members are each tracking the same relationship on their own scale. Give
every tracker exactly one named owner, and have the others read it rather than
keep their own.

**The build reads fine but a character behaves like an older version of
himself.**

Member edits require republishing the member card. A container republish does
not pick up an unsaved or unpublished member. Confirm the publish order,
members first, then the container, then a fresh chat.

**The twist is on the character card list.**

The Character List is public. Anyone browsing sees the whole cast before they
start. If a member's presence is the reveal, this surface cannot hold it.
