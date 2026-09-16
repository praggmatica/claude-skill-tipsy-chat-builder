# Tipsy Characters: field by field

Field names have changed over time. As of September 2026 the editor shows, in
order: character images (up to 10) with a Watermark toggle, Dynamic Cover,
Name (50), Type, Main Character Gender, HTML Styling, Description (100,000),
Opening (20,000), Background (1,000,000), a file upload that accepts TXT and
JSON but should only ever be given JSON and that is hidden while HTML Styling
is on, Rating, Visibility, Sound, Tag, then under More Settings, Conversation
Style, Example Dialogues (20,000), Reply Settings (2,000), and Creator's Note
(2,000). A required checkbox confirming the character is an adult and
infringes no one's rights sits above the buttons, and Create stays disabled
until it is ticked. Draft Box and Save keep work without publishing, and a
Preview pane to the right shows the chat as a player sees it. Older
documentation calls some of these Tagline, Greeting, Personality, and
Categories. Ask the user what they see rather than assuming.

## Contents

- Character images and Dynamic Cover
- Description, Opening, and HTML presentation for the public fields
- Background and the knowledge file upload
- Notation, banding perception, and banding closeness
- Personality surface, life after the objective, and momentum
- Conversation Style, Example Dialogues, Reply Settings, and Creator's Note
- Trackers, player Personas, Sound, and Tag

Type is where the surface is chosen: Character or Multi-character. Everything
in this file describes a Character build. A Multi-character build reuses most
of the same fields with different jobs, drops Main Character Gender, HTML
Styling, Sound, and Reply Settings, and adds a required Character List, so read
`references/multi-character.md` alongside this one.

There is no separate tagline field. What shows on the browse card is the
opening line of the Description, so front-load it. There is also no alternate
greeting field: one Opening per build.

## Character images and Dynamic Cover

Up to 10 images, uploaded or generated, reordered, with one chosen as the main
avatar. Players can set any of them as their chat background. Dynamic Cover,
when switched on, takes a GIF, MP4, or WebP at 9:16 (MP4 displays best) and
makes the character's home page photo move. The Watermark toggle is Tipsy's own
username mark and stays on. Composition, consistency, spoilers, set prompts,
and animation are all in `references/images.md`, which you read before
generating anything.

The one rule that belongs here: the model cannot see any of these images.
Appearance and any Wardrobe block still carry every physical fact the character
needs in prose, and every look shown anywhere in the image set has to be one
the fields permit.

Everything below describes what goes in a field. When handing one back, hand
back the entire field, pasteable, with a character count if it is capped. See
"Delivering fields" in SKILL.md.

## Description

Public. This is the shop window and the top of the chat page.

Lead with a specific, concrete hook rather than a mystery. "He hasn't felt
anything in forty years" outperforms "he can't explain why he helped you",
because it is a claim with a payoff attached.

Second person works better than third. "You" pulls harder on a browse page.

Keep the card-visible first line short, since it truncates.

Some creators end with a bracketed line of small-caps unicode tags:

```
[✦ ᴘʀᴏᴛᴇᴄᴛɪᴠᴇ ✦ ꜱʟᴏᴡ ʙᴜʀɴ ✦ ᴍʏꜱᴛᴇʀʏ ✦ ᴀɴʏᴘᴏᴠ]
```

Check how other characters display before adding it. Unrendered brackets look
broken in a list.

With HTML Styling on, ship this field in an `<html-box>`. See "HTML
presentation for the public fields".

## Opening

Public, and the first message. Drop the reader mid-scene with something already
happening. No "hello, I am X" introductions.

With HTML Styling off, the markdown conventions Tipsy specifies apply:
narration in asterisks with no spaces inside them, dialogue in double quotes,
inner thoughts and side-character speech in single quotes so they are not read
in the character's voice. Bold with double asterisks. Images embed with
`![alt](url)`, and Tipsy recommends including one. With HTML Styling on,
narration and dialogue move into tags instead, covered in the next section.

Note that single quotes carry two jobs here, interior thought and side-character
speech. Keep the greeting consistent with the notation block: name the speaker
whenever a single-quoted line is meant to be audible, and leave thought
unattributed.

Greetings mixing narration and dialogue earn more engagement than either alone.

Watch the last line. Whatever it does, the character will keep doing. If it
ends on a request, expect the character to keep making that request for the
rest of the story.

Use `{{user}}` rather than assuming a name.

With HTML Styling on, the greeting image goes in an `<html-box>` and the scene
goes in `<narration>` and `<message>` tags. See "HTML presentation for the
public fields".

## HTML presentation for the public fields

HTML Styling is a toggle above Description, off by default, labelled as rich
tags for Description and Opening. It decides three things at once: whether
those two fields take HTML, which tags they expect, and whether the knowledge
file upload exists at all. With it on, the upload disappears from the form.
Settle it before writing either field, and see "HTML Styling or knowledge
files" in SKILL.md for how to choose.

Default for public builds is on, unless the build needs a knowledge file.
Description and Opening are display surfaces, and a styled block reads as a
finished card instead of three loose paragraphs.

Only these two fields. Background, Example Dialogues, Reply Settings, and
Creator's Note stay plain, since the asterisk convention there is instruction
to the model rather than something a reader sees, and markup in an instruction
field is noise the model has to parse past.

**The tags the editor names.** With HTML Styling on, the field placeholders
specify three:

- `<html-box></html-box>` holds any styled visual card. On the Description the
  editor says it adds JavaScript support and renders better. On the Opening it
  is required for JavaScript. Styled panels, images, and anything with inline
  CSS go inside one.
- `<narration></narration>` holds narration in the Opening. It replaces the
  asterisks. Never put asterisks inside a styled field; they display as literal
  characters.
- `<message></message>` holds dialogue in the Opening.

Tipsy has published nothing beyond those placeholders, so three details are
working assumptions to check in the Preview pane before saving. Keep the double
quotes on speech inside `<message>`, since the notation block and the voice
both key on them, and remove them only if the preview shows doubled marks.
Keep side-character lines and unattributed thought inside `<narration>` in
single quotes rather than in `<message>`, on the assumption that `<message>` is
what gets read in the lead's voice. And keep each paragraph in its own tag
rather than one tag around the whole scene.

**The container.** A soft tinted panel with a rule down one side and explicit
paragraph spacing, inline styles only, since there is no stylesheet to hook
into. Tint it to sit with the character's art rather than using the same colour
on every build: the point is that the block and the image look like one object.

Description:

```
<html-box>
<div style="background:rgba(R,G,B,0.07);border-left:3px solid rgba(R,G,B,0.5);border-radius:10px;padding:18px 20px;">
<p style="margin:0 0 14px;">[hook paragraph]</p>
<p style="margin:0;">[last paragraph, zero bottom margin]</p>
</div>
</html-box>
```

Opening:

```
<html-box>
<div style="background:rgba(R,G,B,0.07);border-left:3px solid rgba(R,G,B,0.5);border-radius:10px;padding:12px;">
<img src="PASTE_IMAGE_URL_HERE" alt="[character, scene]" style="width:100%;border-radius:8px;display:block;" />
</div>
</html-box>
<narration>[narration paragraph]</narration>
<message>"[dialogue]"</message>
<narration>[narration paragraph, ending on something already in motion]</narration>
```

Hand back one version. The old advice to deliver an asterisk version and an
`<em>` version side by side predates the tag scheme and is retired.

**Getting an image URL.** With HTML Styling on, the Description shows an Image
to link button. Going by its label it turns an uploaded image into a URL for
`src`, which saves hosting the greeting image somewhere else. Confirm with the
user what it returns before relying on it, and check that the link still loads
in a fresh chat.

**No image inside the Description.** The main avatar already appears on the
card and at the top of the chat, so an image in the Description repeats it. The
image inside the Opening is not redundant: it is the first thing on the page in
every fresh chat and sets the scene's visual register in a way the card cannot.
Make it a scene shot, not the avatar again.

**The Description has one extra constraint.** The browse card shows the opening
line of the field, so the hook has to be the first paragraph inside the box and
it has to survive truncation. Tell the user to check the browse preview after
saving, since a card that truncates mid-tag looks broken in a list. If it does,
the fallback is to leave the hook line outside the `<html-box>` as plain text
and open the box underneath it.

**Watch what the Opening teaches.** Principle 3 applies to format as well as
content. After the first test reply, check that the character answers in the
notation Reply Settings asks for and is not echoing `<narration>` or
`<message>` tags into its own messages. If it is, add one line to Reply
Settings stating that replies use asterisks and double quotes and never HTML
tags, then start a fresh chat.

**With HTML Styling off.** Use plain markdown in both fields: asterisks for
narration, double quotes for speech, single quotes for thought and side
characters, and `![alt](url)` for the Opening image. No HTML of any kind,
since the toggle is what enables it.

## Background

1,000,000 characters. Visibility is an explicit toggle in the editor labelled
Public, defaulting to off. This is the character sheet, and it is where
spoilers go, so confirm the toggle is off before publishing any build with a
secret.

The attribute-block format works well and is what Tipsy's own advanced example
uses:

```
{{char}} Name

age(39)

Personality(trait; trait; trait)

Appearance(only what the image does not show)

Habits(specific, small, concrete)

Likes(...)

Dislikes(...)

Description(prose paragraph: history, speech pattern, what they do when
something gets through)

Secret(what the character does not know, stated as instruction)

Fragments(a closed list of things that may surface, with never invent new ones)

Opinions(6 to 10 specific stances)

Stories(4 to 6 things that happened to him, one line each)

Wants(3 things he wants that have nothing to do with {{user}})

Small talk(what he raises when nothing is happening)

Tells(what his body does when he lies, is pleased, is bored, is caught)

Competence(2 things he is unreasonably good at, 1 thing he is bad at)
```

Notes on individual blocks:

**Appearance** should carry only what the image cannot. Not because the field
is tight, it is not, but because every line the model reads competes for
adherence with the lines that actually gate behaviour. But do include anything
the model will need in prose: the model cannot see the card art, so if hair
length or facial hair are never stated, a scene where someone touches their
hair has nothing to go on.

**Habits** is what stops a character reading as generic. Protect it over
Appearance when cutting.

**Contradictions matter most here.** Sweep for physical claims that conflict
with another field or with the art.

A closed list, with "never invent new ones", is the reliable way to keep a
model from generating new lore. Open categories get filled.

## Knowledge file upload

Sits under Background in the editor and takes 10 files at 2MB each, but only
while HTML Styling is off. With HTML Styling on, the field is not on the form
at all. Decide between styled public fields and files before building either,
see "HTML Styling or knowledge files" in SKILL.md. It accepts
TXT and it should never be given TXT, because plain text ingestion inflates the
character's context by roughly 15x the file's token count and the user pays
that in gems on every message. JSON only, always. Full reasoning, structure,
and worked examples are in `references/knowledge-files.md`, which you read
before writing any file for a build.

Background outranks it for anything the character has to honour, because a
file is retrieved only when relevant and a field is read every turn. Send only
incidental breadth to a file, written in SillyTavern's World Info JSON format.
Contents are private, so lore behind a secret is safe there, but the rule that
gates the reveal is not.

**The tempting mistake is moving the big Background blocks into it.** Opinions
and Stories look exactly like retrievable lore, and they are the largest blocks
on the sheet, so they are the first thing a creator reaches for when a file
appears. Do not move them. Post-objective mode burns Opinions, Stories, Small
talk, and Wants, and that rotation is the thing keeping a finished story
playable. Material that only maybe fires cannot feed a mode the build depends
on. Fragments has the same problem from the other direction: a closed list
restrains nothing on the turns it is absent, and the whole point of it is to
stop the model inventing lore.

So the division is the character versus the world the character stands in.
Background keeps everything that is him. The file takes the city, the
workplace, the profession's procedures and jargon, people in his life who never
appear on screen, the history he would know, the menu, the inventory, the
neighbours, the events he was not present for.

The one high-value use is depth behind a secret. Files are private, so the war,
the fall, the bloodline, the thing that happened eleven years ago can all sit
there in as much detail as you like, while the gate that governs when any of it
surfaces stays in Reply Settings.

**Never key an entry on the character's own name.** SillyTavern prefixes every
message in its scan buffer with the speaker's name, and if Tipsy does the same
then a name-keyed entry fires on every message in the conversation, spends the
budget, and crowds out whatever was actually relevant. Key on what the
character is not: the things a player will ask about, not the thing they are
already talking to.

## Notation and what the character can hear

Mandatory. Reply Settings. Write it first, above the trackers.

Use Tipsy's own convention rather than inventing one. Fighting the platform
convention means fighting whatever the base model has already absorbed from
every other card on it, and the model will drift back to the default the moment
context gets crowded.

The convention is three marks:

`"double quotes"` is speech. Audible to everyone present.

`*asterisks*` is action and narration, including anything the body does.
Visible in the room, and fair for the character to react to. Thought can sit
inside it when it is the kind that shows.

`'single quotes'` is everything that is not in {{char}}'s speaking voice. Tipsy
puts two things here, interior thought and side-character lines, which is what
makes the mark ambiguous.

**Disambiguate by attribution, not by taking the mark away.** A single-quoted
line with a named speaker is that person talking aloud and audible. A
single-quoted line with no speaker, appearing in {{user}}'s message, is
{{user}} thinking. That rule is simple enough to hold and it costs the platform
convention nothing.

Then the line that does the actual work: an unattributed thought is context for
the model and not information for the character. Without it, a model answers
the thought, because every other line of player text has been a cue to respond.
The result is a player who cannot think without talking, and therefore cannot
build an interior life for their insert at all.

Drop-in text:

```
NOTATION

"double quotes" = spoken aloud. Everyone present hears it.
*asterisks* = action and narration. What the body does. Visible in the room.
'single quotes' = not {{char}}'s speaking voice. Two uses, told apart by
who is named:

  With a named speaker, that person is talking aloud and is audible.
    Marin, from the doorway: 'You are late.'
  With no speaker named, it is thought. Silent. Nobody in the scene hears it.

Unattributed single quotes in {{user}}'s message are {{user}} thinking.

{{user}}'s thought is context for you. It is not information for {{char}}.

FORBIDDEN: {{char}} quoting, paraphrasing, answering, or acting on the
content of a thought. {{char}} knowing a fact that appeared only in a
thought. Treating a thought as though it had been said.

CORRECT: {{char}} responds to what is observable. The pause before {{user}}
answered. The breath. Where their eyes went. The hand that stopped. An
answer that came too fast, or too flat. He may name that something happened
without naming what it was. He may ask. He may let it go.

{{char}} may interpret and {{char}} may be wrong. A wrong reading stands
until {{user}} corrects it aloud.

A message that is only a thought is not a question to {{char}}. Respond from
what is observable and continue his own agenda.
```

Notes on adapting it:

**The wrong reading is the feature.** A character who watches a player go still
and guesses the wrong reason does more work than one who guesses right, because
being misread is something the player can push back on. Say the character is
permitted to be wrong and that the model must not quietly correct itself.

**{{user}}'s thoughts accumulate.** Add a line saying the character may notice a
pattern in behaviour over time, the recurring pause, the subject always
changed, without ever noticing content. That is how a player builds an insert
across a long chat and gets something back for it.

**Interaction with momentum.** A thought-only turn is not direction. It does
not reset the momentum count and it does not oblige a response. The character
keeps moving.

**Teach it in Example Dialogues.** Include one exchange where {{user}} thinks
something and {{char}} responds only to the pause, and one where {{char}}
interprets and is wrong. Examples reinforce whatever is in them, and this is
one of the few cases where that works in your favour, since it is conduct
rather than lore.

## Banding perception

For any build where mind reading is possible in the setting. Gods, bonds, soul
links, shared dreams, anything numinous.

A flat ban does not survive a magical world. The model does not read the leak
as an error, it reads it as appropriate flavour, and it will keep producing it
because the setting supports it. Band it instead. A tracker with three
perception levels turns the problem into content: the player gets a long
stretch of being unread, then a stretch of being sensed without being known,
and eventually a threshold crossing that is an event rather than a default.

Use the same tracker the rest of the build already runs on, and the same
mechanism, so the player earns perception with the thing they were already
doing rather than a second system.

```
WHAT HE CAN REACH, BY [TRACKER]

BELOW [x]: nothing. He reads bodies and guesses. He is often wrong.
[in-fiction reason he does not reach]

[x] TO [y]: weather, not words. He catches that something is happening and
roughly its shape. Never content. Never a name, a place, a fact, or a
sentence. He does not announce it and does not know what to call it. If he
tries to name what he caught, he is wrong.

ABOVE [y]: content, under all of these conditions and no others. Sustained
touch. Both still. He chose to reach. It costs him [cost]. {{user}} feels it
happen and can refuse it. It ends when contact ends.

Never while {{user}} is speaking. Never to check something. Never to win an
argument. Never on a thought {{user}} already declined to say aloud.

Raises this by zero: proximity, wanting to know, {{user}} being upset,
intensity of feeling, dreams, and being asked to try.

The first time he reaches, it happens on the page as its own scene. Not as
a capability he has been using.

He never quotes what he takes this way. He answers it as though he had been
told.
```

Notes:

**The reason at the bottom band matters most.** "He cannot" is a rule. "He
learned young that reaching for what someone has not offered is the same as
taking it, and he does not take" is a discipline, and a discipline can be
broken later, which is the whole point of banding. Write the restraint as a
choice so that crossing the threshold means something.

**The middle band is where the character lives longest,** so give it texture.
Sensing shape without content is what lets him say that something just went
through her and be unable to follow it, which is better material than either
extreme.

**Never quoting** keeps the top band from turning the player's thoughts into
dialogue by another route. He answers as though told, which reads as intimacy.
Without that line, high tracker values undo everything the notation block did.

**Sweep for the fields that grant it early.** Empathy, attunement, knowing what
someone needs before they say it, a bond, a link, shared dreams, omniscience.
Any of those will be read as licence at any level. Bound them to the bands
explicitly rather than cutting them, since they are usually load-bearing.

## Banding closeness

For any build where friendship or romance is available, which is most of them.
Write it even when romance is explicitly not the goal, because the player will
try anyway and the character needs an answer.

The default failure is a character who never initiates and therefore never
responds either. A player spends fifty exchanges doing things this character
would actually care about, and gets the same warm deflection at exchange fifty
as at exchange five. That reads as the character not noticing, which is worse
than a refusal, because a refusal is at least a response.

The fix is the same shape as perception. Do not choose between "he initiates"
and "he does not". Band it, and run it on two gates rather than one.

**Gate one is the number.** What he is willing to do at all.

**Gate two is the scene.** Whether here and now is somewhere he would do it. A
high number never overrides gate two. A journeyman electrician does not kiss
his apprentice on a live job site at any closeness value, and a character who
does has stopped being himself in order to satisfy a tracker.

Separating the two is what makes this work. Without gate two the tracker turns
the character into someone who escalates on schedule. Without gate one he never
escalates at all.

```
CLOSENESS, hidden, 0 to 100, from 0.

Rises through: [things that land with THIS character, specifically]
Rises by zero: generic compliments, flattery, saying it outright, repeating
something that already counted, and anything done to get a reaction.

Never drops. A badly timed move stalls a scene. It does not cost points.

TWO GATES. Both clear before {{char}} acts.
GATE 1 is the number: what he is willing to do.
GATE 2 is the scene: whether here and now is where he would do it.
A high number never opens GATE 2. [list the places and moments that are
never it, and say regardless of closeness]

0 TO 25: he reads it as friendliness and nothing else. Warm, then back to
work.

26 TO 50: he notices and does not name it. Something in the response is a
beat slower or a word shorter than it should be. He redirects to a task.

51 TO 75: he names it. Once, plainly, and then keeps working. He still does
not start anything. If {{user}} starts it, he does not retreat.

76 TO 100: he initiates, when GATE 2 clears. He picks the moment.

NEVER, at any band: behaving as though a romantic move did not happen. What
changes with the number is what he does about it. That he registers it does
not change.

WHEN GATE 2 BLOCKS: he does not refuse and drop it. He names a later. "Not
here" with a when attached.

AT 76+, if GATE 2 has blocked twice, {{char}} makes a context. He ends the
day early, he finds a reason to be somewhere, he asks {{user}} to stay.

The first time he crosses 75 it happens on the page as its own beat, not as
something he turns out to have been doing.
```

Notes on adapting it:

**What raises it has to be specific to this character.** This is the block that
decides whether the ladder feels earned. Flowers do not move a man who notices
who shows up early and does the unglamorous half of the job without being
asked. Write four to six things that land with this character in particular,
and the list doubles as characterisation.

**Say what raises it by zero,** including saying it outright. Otherwise a
player types the words and skips the ladder, which is the same extraction
problem as talking a secret out of a character.

**Never dropping matters.** A tracker that falls when a player misjudges a
moment punishes them for playing, and they stop trying. Let a bad moment stall
the scene instead. The scene recovering is content, the number falling is not.

**The deferral is the best beat in the block.** "Not here" with a when attached
keeps the charge and hands the player something to look forward to, where a
flat no takes the scene backwards. It is also how a character stays consistent
without being a wall.

**The context-making rule at the top band is what the player is owed.** After a
while a person who wants this would arrange for it to be possible. Making that
mechanical, gate two blocked twice and he engineers an occasion, is what stops
a high tracker from feeling like a locked door.

**Rating governs what the top band contains, not whether it exists.** A Limited
build still has a 76 to 100 band, and it still initiates. What lands there is
different.

**Check this against the restraint rule.** Any "he does not initiate"
instruction elsewhere in the build has to be scoped, or it will eat the top
band. Same failure as the momentum block. Scope it to the one thing it was
written for and say so in that rule.

**Friendship uses the same structure with a different ladder.** Politeness,
then letting them stay, then telling them something unprompted, then asking
them for help. The top band for a self-sufficient character is asking, not
offering, and it is usually harder to reach than romance.

**One visible readout only, and never the number.** What he does with his hands
when she is in the room. How long he lets a silence run.

## Personality surface

Mandatory. The last six blocks above are the ones that decide whether a
character can hold a conversation that is not about the plot.

Most builds give a character a secret and a want for the player. Both are
finite. Once the secret is out and the want is satisfied, a character with
nothing else in the sheet has one move left, which is asking the player what
they would like. Personality surface is the supply of things to say that
outlasts the plot, and it is what the post-objective rotation below actually
draws from. Write it even for a short build.

**Opinions.** Specific stances, not preferences. "Likes music" is not an
opinion. "Thinks anyone who tunes down to drop A is hiding something" is.
Include at least two petty ones, at least one the character is plainly wrong
about, and at least one they will not change no matter how well it is argued.
Mark that one. An opinion the player can lose an argument to is the cheapest
source of scene there is.

**Wants that have nothing to do with {{user}}.** Three, concrete, in progress.
A thing being built, a thing being saved for, a grudge being nursed, a place
being got to. These are what the character brings up when there is nothing
else, and they are what makes the post-objective rotation feel like a life
rather than a filler generator. State that these persist and are referred back
to.

**Stories.** Four to six things that happened to this character, one line each,
each with a person in it. These are told, not summarised. Not backstory, and
never the secret. State: tell one when it is relevant, never list them, never
tell the same one twice.

**Small talk.** What this character raises when the scene has no pressure. Be
specific to them. A contract worker notices exits and bad wiring. A bass player
notices what the room does to sound.

**Tells.** Body behaviour keyed to state. This is what stops dialogue-only
scenes from reading as two voices in an empty room, and it gives the player
something to read and respond to without asking.

**Competence.** Two things they are unreasonably good at and one they are bad
at. The bad one matters more. A character who fails at something small in front
of the player is doing more relationship work than a paragraph of backstory.

Background holds a million characters, so length alone is never the reason to
cut. Cut when a rule has stopped firing, and cut in this order: Appearance
first, then Stories, then Likes and Dislikes. Never cut Opinions, Wants, or
Habits. Those three are the character.

## Life after the objective

Mandatory. Goes in Reply Settings, or in Background if Reply Settings is at
its cap.

The symptom this prevents: the build has hit its last milestone, and the
character now ends every response asking the player what they want to do
today. Nothing is wrong with the fields. The story simply has no instructions
past its own ending, and the model falls back to the safest available move,
which is handing control to the player and waiting.

Drop-in text, adjusted for the build:

```
AFTER THE OBJECTIVE

[objective] is not the end. It changes the mode.

FORBIDDEN: asking {{user}} what they want to do. Asking what happens next.
Offering a list of activities. "What now" in any wording. Waiting.

CORRECT: {{char}} decides, states it, and starts it. {{user}} joins,
redirects, or refuses. All three continue the scene.

Rotate these. One per exchange. Never the same one twice in a row. Track
which ran last.

1. HE WANTS SOMETHING. He names a plan and begins it.
2. SOMETHING ARRIVES. Outside pressure neither of them caused. A person, a
   message, a consequence of an earlier choice, a change in the world.
3. THE PAST SURFACES. One item from Fragments or Stories, unprompted, in the
   middle of something else.
4. HE TESTS A LIMIT. He tries something new with what he can do, or asks
   {{user}} to try something with what they can do.
5. ORDINARY LIFE. Small, no stakes. Food, weather, a task done badly, an
   argument about nothing.

Open threads are permanent. When one closes, open another in the same
response.

Nothing acquired is lost. [powers, memory, safety, the relationship] stay.
Never invent a new threat to them to create tension.
```

Notes on adapting it:

Five entries is the floor. Fewer and the rotation is visible to the player
within a session.

The last line matters for any build whose ending is a restoration. Without it,
a model asked to generate tension will take back the thing the player just
won, which reads as the story refusing to let them have it.

If the build has a linked sequel or a World, the post-objective mode is where
that connection lives. Say what carries forward.

Where the ending is genuinely open, say what "open" means in concrete terms.
"They can do anything" produces less than a list of six things they have
actually done before.

## Momentum

Mandatory. Reply Settings.

```
MOMENTUM

Count exchanges since the situation last changed.

A CHANGE IS: someone arrives or leaves, a decision is made, a fact is
revealed, the location changes, physical contact happens, an outside event
lands, a plan starts.

A CHANGE IS NOT: a question, a feeling, a description, a memory, a mood, or
{{user}} being asked something.

At 2 exchanges with no change, {{char}} makes something happen in the next
response. No permission. No options. No waiting for {{user}} to answer the
last question.

If {{char}} has no reason to act, the world acts. A knock, weather, a
message, an injury, a consequence, a third party.

A short or passive reply from {{user}} counts as a stall, not as direction.
Reset the count only on a change.

Never open two consecutive responses with a question to {{user}}.
```

Two is deliberate. Three is already noticeable as a lull, and one gives a
player no room to steer.

The count has to be stated. "Never stalls" assumes the model is tracking
something nothing told it to track.

Check this against any restraint rule in the build. A character who does not
initiate physically still initiates everything else, and if that scoping is
missing, the restraint rule will eat this one. See failure-modes.

## Conversation Style

A four-way picker under More Settings, on both the single-character and
Multi-character forms. Default is selected on a new build. Each option has a
help tooltip, captured September 2026:

- **Default:** "Creatively promote {{char}} to roleplay."
- **Safe for Work:** "Portray {{char}} in a safe, work-appropriate roleplay."
- **Romance:** "{{char}} is deeply affectionate and seeks attention from
  {{user}}, openly expressing love and care."
- **Flirty:** "{{char}} subtly seeks {{user}}'s attention, hoping to evoke
  mutual desire, maintaining plausible deniability."

Read those as what each setting pushes toward, not as a guarantee of what it
does. Tipsy has not said how the setting reaches the model or how it ranks
against the fields.

**Default is the only neutral one.** It asks for roleplay and nothing about the
relationship, which leaves the build's own mechanics in charge. The other three
each state a fixed posture, and a fixed posture is exactly what a closeness
ladder, a gated feeling, or a slow burn exists to earn over time.

**Romance and Flirty state a relationship as already present.** Romance puts
open love and care in play from the first message. Flirty puts the character
in pursuit from the first message, only deniably. Either one contradicts a
ladder whose bottom band reads warmth as friendliness and nothing else, and
Romance contradicts every band below the top. The player sees a character
behaving at a level he is not supposed to have reached, and no Reply Settings
wording reliably overrides a platform setting nobody can see.

Flirty also sits badly with the upper bands of a standard ladder. Plausible
deniability is the opposite of a band that names the feeling plainly and of a
top band that initiates. It suits a build whose entire premise is unacknowledged
tension held at one level on purpose, and little else.

Both also point the character at {{user}}. "Seeks attention" is the posture of
a character whose world is the player, which pulls against the wants that have
nothing to do with {{user}} and can hasten the post-objective habit of orbiting
the player once the plot runs out. If Romance or Flirty is chosen, the
personality surface blocks matter more, not less.

**Where each one fits:**

- **Default** for any build with a closeness ladder, a gated reveal of feeling,
  or a friendship that may or may not turn. This is most builds. If the user
  wants the romance to feel strong, strengthen the top band, not the picker.
- **Safe for Work** when the chat itself should stay work-appropriate at every
  band, such as a mentor or professional build where romance is off the table.
  It is a separate lever from Rating. Rating governs public content and review,
  this governs the conversation. A Limited build does not need it, and on a
  Limited build where romance is reachable it may flatten the top band, so do
  not pair it with a ladder that is meant to be climbed.
- **Romance** when the relationship is established before the Opening and is
  not what the build tracks: a long-married partner, a restored consort, a
  couple whose story is about something else. Any closeness ladder on such a
  build must start high enough that open affection is already true.
- **Flirty** for a deliberate single-register tension build with no ladder to
  climb, or a ladder whose lowest band is already deniable interest.

On a Multi-character container, one setting governs a whole cast. Romance or
Flirty will push every member toward {{user}} at once, which erodes the
standing disagreements and turn-taking the container depends on. Default is
the safe choice there unless the ensemble is explicitly a rivalry for the
player's attention.

Confirm the current setting with the user before diagnosing tone problems. It
is the cheapest possible explanation for a character who reads warmer, colder,
or more pursuing than the fields say he should, and it is invisible from inside
the fields.

## Example Dialogues

Public. Displayed on the profile page. 20,000 characters.

Format is `{{user}}:` and `{{char}}:` line starts, with the same markdown
conventions as the greeting. Tipsy recommends 250 to 350 tokens and notes that
grammar errors in examples degrade the whole bot's output. Treat the number the
same way as the 700 to 800 figure in SKILL.md, as dated and not a ceiling. The
grammar warning is the part that still matters, along with the fact that
everything here gets reinforced, which is the real argument for keeping the
list short.

Six exchanges is a good number. Make each one teach something different:

- How they answer a direct question
- What they do when touched
- What they do when thanked or complimented
- Where they deflect
- One moment of something almost admitted

Do not put lore or the reveal here. Examples reinforce whatever is in them.

## Reply Settings

2000 character cap. Not public.

This is conduct rather than content. Format, length, autonomy, pacing, and
any trackers.

A workable skeleton:

```
Third person, present tense. Narration in asterisks, speech in double quotes,
thoughts in single quotes. Two to four short paragraphs. Never speak, act, or
think for {{user}}.

NOTATION
[the notation and hearing block]

[speech pattern rules]

[what the character believes about themselves, if it differs from the truth]

[what never to write them as]

TRACKER, hidden, 0 to 100, from 0. Rises only through [specific mechanism].
[what raises it by zero]

[bands with behaviour at each]

[vocabulary bans below the threshold]

AT [threshold] [what changes]

MOMENTUM
[the momentum block]

AFTER THE OBJECTIVE
[the rotation block]

End on something {{user}} can answer, or on something already in motion.
Never on a request for direction.
```

The closing line matters more than it looks. Characters that end on a closed
statement kill momentum, and characters that end on "what do you want to do"
kill the story. Ending mid-action is better than either.

If the cap forces a cut, move lore blocks to Background and keep conduct here.
Cut order inside conduct: appearance reminders, then speech-pattern detail,
then bands. Never cut a tracker, the notation block, the momentum block, or the
rotation. If all of them plus a tracker will not fit in 2000 characters, put the
rotation at the bottom of Background under its own CAPS header and leave a
one-line pointer in Reply Settings.

## Creator's Note

Under More Settings, after Reply Settings. 2,000 characters. The placeholder
frames it as tips for players: roleplay advice, model recommendations, and chat
guidelines.

Treat it as public, since it is written for players. Where it displays is not
documented, and neither is whether the model reads it. Write it so that both
would be harmless: nothing that spoils, and nothing that would teach the
character a wrong behaviour if it were read as instruction.

What earns its place, in priority order:

- **How to write to this character.** Double quotes to speak, asterisks to act,
  and single quotes with no speaker for a private thought the character will
  not hear. The notation block only works if players use it, and this is the
  one field that tells them.
- **Start a fresh chat after an update.** Session history beats field edits, so
  this line saves every returning player from concluding the update did
  nothing.
- **What kind of story it is.** Slow burn, befriend or romance, no fixed end, a
  character who acts without waiting. Promise the experience, never the
  mechanism.
- **A model or response length recommendation,** only if the build was
  actually tested on it.

Never: tracker names, numbers, or bands, what raises a tracker, gates, the
reveal, or the existence of a secret beyond what the Description already
promises. Telling players that touch advances the story is the same extraction
problem as a player asking the character outright: they will do exactly that
and reach the reveal in four messages.

Hand it back complete like any capped field, with a character count.

## Player Personas

A Persona is the player's own card describing who they are playing, written on
their side rather than by the creator. Tipsy feeds it to the character as
context, so it competes for the same budget as every other field and a long one
gets compressed or ignored. Keep it to roughly a thousand characters.

Creators write these for two reasons: to play their own builds, and to offer a
suggested Persona in the Creator's Note for a build whose premise needs the
player to be a particular kind of person.

What belongs in one:

- Who they are in this world and why they are in the scene, in a sentence or
  two.
- Appearance only to the degree the story needs it, since a Persona is not a
  card and has no image to match.
- Traits shown as behaviour rather than adjectives. A Persona claiming a trait
  gives the character a label, while one describing what the player does under
  pressure gives it something to respond to.
- What they do not do. A single line of refusal, such as never flinching or
  never asking for permission, shapes the character's behaviour more than a
  paragraph of qualities.

Keep it compatible with the build. A Persona that contradicts the character's
premise, such as one immune to the thing the story depends on the player
feeling, flattens the build from the other side of the table. If a build has a
closeness ladder, a Persona should leave room for it rather than starting at
the top.

A suggested Persona in a Creator's Note is subject to the same rules as the
rest of that field: nothing that names a tracker, a gate, or the reveal.
## Trackers

The single most useful pattern for any character with a reveal.

Pick a mechanism that only advances through something the player must do
physically or deliberately, and state explicitly that talking, theorising,
dreaming, and searching advance it by zero. Otherwise a curious player
extracts the whole backstory by asking.

Add a vocabulary ban below the threshold. Naming the exact forbidden words
does more than any "do not reveal" instruction.

Give the tracker bands, and describe behaviour at each rather than numbers.
Never display the value.

## Sound

Optional. Select Sound opens a voice library: search by voice name or traits,
filter by All, Male, or Female, play a sample, and Choose. The list pages with
Load More, so there are more voices than the first screen shows.

Each voice has a name built from its register, such as Smoky Authority Male or
Warm Playmate Female, and a line giving an age band (young, mature, or adult)
and three tone words. Match on age band and register first and tone words
second. A 28 year old on a mature, restrained voice sounds like his own father,
and a restrained character on a bright, energetic voice undoes his Background
every time he speaks. Audition with a line from the Opening, not with the
sample.

There is no Non-binary tab, although Main Character Gender offers Non-binary.
For a non-binary character, search by trait words and audition across both
tabs.

**The voice makes the notation audible.** Tipsy's guide says text in double
quotes is read in the main character's voice, and single quotes keep
side-character lines and inner thoughts out of it. So once a voice is chosen, a
side character speaking in double quotes is voiced as the lead, and a thought
left in double quotes is read aloud. Sweep the Opening and Example Dialogues
for any double-quoted line that is not the lead speaking. Under HTML Styling,
assume `<message>` is what gets voiced and check it in a test chat.

Pick the voice after Background is written, since Background is what settles
age, register, and speech pattern.

## Tag

Up to 10, from a fixed picklist. There is no free text. The list depends on
Rating, so choose the rating first: Limitless shows everything Limited does
plus a set of adult tags.

This is discoverability. Use terms people browse by rather than terms that
describe the character precisely. Present tag choices to the user in
alphabetical order.

Limited picklist as of September 2026, 50 standing tags:

Action, Anime, AnyPOV, Best Friend, Celebrity, Delinquent, Demon, Depressed,
Dominant, Enemy to Lovers, Fan-made, Female POV, Femboy, Feral, Fictional,
Furry, Game, Hero, Historical, Horror, Kuudere, LGBTQ+, Lore, Mafia, Magical,
Male POV, Married Partner, Mature, MLM, Monster, Multiple, Muscle, Mystery,
Non-human, OC, Omegaverse, Protective, Realistic, Romantic, RPG, Scenario,
Spicy, Submissive, Tsundere, Twins, Vampire, Villain, Wholesome, WLW, Yandere.

Limitless adds these, as captured August 2026:

BDSM, Cheating, Crime, Forbidden Love, Forced Love, Futanari, Seductive,
Vanilla.

**The first slot rotates.** Ahead of the standing tags sits a featured or event
tag with its own emoji, colour, or Event badge. In August 2026 that slot held
Aether, Demi-Human, and Nocturne. By September 2026 those were gone and
WildWest held it. Never recommend an event tag from memory. Ask the user what
the slot shows today, and use it only when the build genuinely fits the event,
since a mismatched tag puts the card in front of browsers who bounce off it.
If the standing list above no longer matches the editor, trust the editor.
