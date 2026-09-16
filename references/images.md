# Images

This file assumes Magic Hour (magichour.ai) for stills and video, since that is
where the build art gets made. Tipsy's own generator is covered briefly near
the end for creators who use it. Tool menus change often, so when a label here
does not match what the user sees, trust their screen and ask.

## Contents

- Platform requirements, the image set, and watermarks
- Magic Hour: which tool for which job
- The prompt shape, choosing an art style, attractiveness, composition, and
  exclusions
- Working from the approved card, and editing an approved image
- Prompts for the rest of the set: rules, the set prompt shape, and image types
- Common problems
- Dynamic Cover: step by step, the motion prompt shape, checks, and a worked
  example
- Images generated in chat, and Tipsy's built-in generator
- Image rules in Worlds

## Platform requirements

At least 768 x 1360, portrait, 9:16. Use Tipsy's upscale function on every
upload. A landscape image will be cropped on the card, so check the preview.

Only original or authorised images. No watermarks or logos from other
platforms. No real people's photos, and no real person's name in a prompt.
Describe the features instead, since unauthorised likenesses can limit public
display.

Public images follow the rating regardless of what the chat contains: nothing
involving minors, no explicit nudity or sex acts, no excessive violence or
gore. Keep the card clothed enough to pass review even on a Limitless build. A
shirtless card was flagged for nudity on a Limitless build, and the replacement
kept his jeans on.

## The image set

Since the September 2 2026 update, a character holds up to 10 images, uploaded
or generated, which the creator can reorder and from which one is chosen as the
main avatar. Players can also pick any of them as a chat background. That
second use changes what the extra images are for.

**The main avatar is the card.** Everything about card art applies to it, and
it is the image the Dynamic Cover is animated from.

**Include a face closeup, ideally as the main avatar.** Tipsy shows the
character as a small circular avatar in places such as the card preview, and a
three-quarter or full-length shot shrinks the face to almost nothing there.
Creator experience suggests wide primary images also cause trouble with Tipsy
picking up the avatar at all. The rule until that is better understood: make
the main avatar a closeup of the face, or at minimum make sure at least one
image in the set is. Get it by moving the camera close when generating, never
by cropping a wider image (see "Composition and camera"). A clear, front-lit
closeup is also the best reference for generating the rest of the set.

**The rest are backgrounds first.** In chat, the image sits behind a header and
gradient across the top and message bubbles and the input bar across the
bottom, in a 9:16 frame. A face placed low in the frame gets covered by the
conversation. Keep faces and the point of interest in the upper middle, keep
the lower third quiet enough that text over it stays legible, and generate at
9:16 rather than cropping something wider.

**Vary the scene, never the person.** The point of the set is different looks,
scenes, and sides of the character. Rotate location, time of day, wardrobe, and
mood. Never the face, build, tattoos, piercings, or anything Appearance states.
Every image has to read as the same person, so generate the set from the
approved card as reference. See "Working from the approved card".

**Every image is public and every image is a spoiler surface.** All ten are
browsable. No image of a secret form, the reveal, a later-act location, or the
cast member who is the twist, however good it looks.

**The model cannot see any of them.** A background of him in a suit does not
tell the character he owns a suit. If a look appears anywhere in the set, make
sure Appearance or a Wardrobe block permits it. If an image contradicts the
fields, change the image, not the fields.

**The cap is not a target.** Four strong images that hold the face beat ten
that drift. Every weak image is one a player may pick and sit with for a whole
chat. Prompts and image types for filling the set are under "Prompts for the
rest of the set".

**The Opening image is separate.** The greeting image embedded in the Opening
still needs to be a scene shot of its own. Reusing the avatar there wastes the
first screen of every chat.

## Watermarks

Two different watermarks matter here, and they are easy to confuse.

**Tipsy's Watermark toggle** sits beside the image counter and defaults to on.
Its tooltip says it marks character images with the creator's username to
protect the work, and that switching it off removes the protection. Leave it
on. The review standards prohibit watermarks and logos from other platforms,
not Tipsy's own.

**Magic Hour's export watermark** is the one that gets a card rejected, and
this is confirmed: two cards were rejected in review for watermarks on art
exported before the creator was on a paid plan. Magic Hour says export
watermarks vary by tool and plan, with paid subscriptions and credit packs
exporting without them. Check every export at full size, corners included,
before it goes anywhere near Tipsy, and remove any mark that is there. The
other marks that fail review arrive the same way: an editing app's logo, a
stock overlay, or lettering on a surface that reads as a brand.

Magic Hour also states that free-plan outputs are for personal, non-commercial
use, and that commercial rights come with paid subscriptions rather than credit
packs. A public build that earns is safest made on a subscription. Tell the
user this once rather than deciding for them.

Whether Tipsy's username mark is burned into the stored file is unconfirmed.
Keep local originals of every image, and never use a copy saved back off Tipsy
as a start frame or a reference in Magic Hour.

## Magic Hour: which tool for which job

- **AI Image Generator, model GPT Image 2,** for the card, the image set, and
  the greeting image. Strict prompt adherence, natural-language prompts, and an
  image upload for working from the approved card. Aspect ratio 9:16. Choose 2K
  or 4K where the plan allows, so the upload clears Tipsy's 768 x 1360 floor
  with room to spare, and check the pixel dimensions of the download before
  uploading.
- **No style preset,** whatever the look. Presets such as Character, OC, or
  Dark Fantasy pull a photoreal prompt toward illustration, and on an
  illustrated build they impose their own house style over the one described.
  Leave the preset empty and let the prompt carry the look. See "Choosing an
  art style".
- **AI Image Editor** for fixing an approved image rather than rerolling it:
  removing lettering or a logo, changing clothing, moving the subject into a
  new scene. See "Editing an approved image".
- **Image to Video, model Kling 2.5,** for the Dynamic Cover. It supports 9:16,
  720p and 1080p, and up to 10 seconds in Magic Hour. Kling 3.0 is available
  for longer or multi-shot clips, which a cover does not need. See "Dynamic
  Cover".
- **AI Characters,** Magic Hour's reusable character feature, promises
  consistency across generations. It is untested for this workflow. Do not
  recommend it over the reference-image method below until the user has tried
  it on a build.

## The prompt shape

GPT Image 2 reads natural language. Write one dense block in this order. For a
first generation with no reference, use labelled sections for the person so
nothing gets dropped:

```
[Shot type and crop], [subject], [pose], [expression].
Face: [shape, jaw, brow, eyes and eye colour, nose, mouth, skin tone, facial hair].
Build: [height as a number, frame, musculature, where the weight sits].
Tattoos: [placement and style, left or right stated].
Piercings: [placement, metal].
Wearing: [each garment, colour, fit, how it sits on the body].
Makeup: [if any].
[Setting, with the props that give it character].
[Camera: lens, camera height, tilt, and where the viewer is standing].
[Lighting: source, direction, height, colour, and what it rakes across].
[Camera character: what kind of photograph this is].
[Palette: four or five colours].
Natural skin texture, visible pores, no beauty retouching or skin smoothing. Sharp focus on the eyes.
[Blanket clause: every surface blank and unlettered, naming the specific surfaces in frame].
[Wearing-not clause: the jewellery, layers, and accessories the subject does not have on].
Vertical portrait orientation, at least 768 by 1360.
```

For a new pose or scene from an approved image, the shape changes. See "Working
from the approved card".
Notes on the lines that do the most work:

**Height as a number.** A number holds where "tall" drifts. Raising a stated
height to six foot six was one of the three changes that finally locked a card
that had failed repeatedly.

**The camera-character line.** One line saying what kind of photograph this is
sets the register of the whole image. "A middle-of-the-night phone photograph"
supplies privacy and intimacy that no amount of lighting description does, and
it reconciles a warm lamp with a candid feel.

**Pin every tattoo and piercing to a side and a place.** Placement still drifts,
such as a chest piece rendering higher and running onto the throat, so once an
image is approved, update Appearance to where things actually landed.

**Say where the viewer is.** A lens, a camera height, and a position together
decide how the character relates to the person looking. "Camera set low at the
level of the tabletop and tilted slightly upward from the seat across from him,
so that he stands over the viewer's position" makes the viewer a participant in
the scene rather than a photographer outside it.

**Put the body under load.** A hand planted with weight on it, a shirt pulling
across the shoulders as he leans, a hand caught in the act of turning
something. Physical strain and mid-action verbs are what keep a pose from
reading as posed.

**Make legibility impossible, not forbidden.** Pages angled away from the
camera so nothing on them is legible, screens dark and empty. Give the model a
reason the text cannot be seen, then back it with the blanket clause.

**No weighting syntax.** Parentheses and brackets are Tipsy generator syntax.
In GPT Image 2 they are just punctuation.

## Choosing an art style

Settle photoreal or illustrated before the first generation, because it decides
the wording of every prompt in the set and cannot be changed later without
regenerating everything.

**Photoreal** suits contemporary and grounded builds, and it is what the prompt
shape above is written for: real skin texture, real light, a camera-character
line.

**Illustrated** suits fantasy, historical, and supernatural builds, where a
photoreal render of an impossible feature can land somewhere between silly and
unpleasant. Name the style precisely rather than saying "anime" or "stylised",
since a bare style word returns the most generic version of it. Say what the
linework, shading, colour, and level of detail are doing, and say which parts
of the photoreal shape still apply: the lighting description and the camera
position still work, while "natural skin texture, visible pores" does not.

Whichever is chosen, use it for every image in the set, the Opening image, and
the Dynamic Cover. A set that mixes registers reads as several different
characters even when the face is consistent.

Style words do not excuse the rules above. An illustrated character still has
to be extremely attractive, still needs the face high in the frame, and is
still held to the rating. Illustration is not a route around review, since the
standards apply to what the image depicts.
## Making the character attractive

These are fantasy cards. The lead has to be extremely attractive, and a render
that is realistic but plain is a failed render, not a stylistic choice.

**Ask for conventional.** "Extremely conventionally attractive" outperforms
"strikingly handsome", which pulls toward editorial and model faces rather than
broad appeal. Add the build word the character needs, such as muscular, in the
same sentence.

**Never stack imperfections to get realism.** Overhead light, forehead shine, a
blemish, chapped lips, patchy stubble, flattened hair, asymmetry, and loose
washed-out clothing, all at once, produced a render the creator called
horrifically ugly. The same failure happens with anti-lookalike features: a
broken nose, a heavy brow, weathered skin, and deep folds together read as
unattractive rather than distinctive.

**Get realism from everything except the face and the light.** Real room
clutter, real fabric texture, natural grain, and no colour gels or cinema rim
light make an image feel like a photograph. Light the face with soft window
daylight at face height, never overhead.

**Cinematic lighting reads fake on a candid build.** Rim light, a dark set, and
a hot practical make a photo look staged. If the fiction says the image is
something he sent, light it like something he could have taken.

**Expressions overshoot.** "Too happy to be there" is a real rejection reason.
A closed-mouth smirk beat a toothy grin. Name the expression a notch milder
than the target, and lead with what the body does, since emotion words alone
produce a neutral face.

**Lock what rendered.** Once an image is approved, details will differ from the
prompt: a tattoo sits higher, hair comes out a shade off. Update Appearance to
match the approved art rather than chasing the prompt, so the fields and every
later image agree.

## Composition and camera

**Camera height changes status.** A camera low at hip level tilted up makes a
character read dominant. A full-length standing shot at conversational distance
makes the same man read short and unimposing.

**Motion reads better than posing.** A subject caught mid-step toward the
camera, or doing something with their hands, looks candid. A braced or held
pose reads stiff in stills and worse once animated.

**Clothing changes proportions.** An untucked, blousy shirt halves the leg
line. Say how each garment sits on the body.

**Never crop for a bigger face.** A tight crop of an approved image killed its
depth, which came from the setting receding behind the subject and the full
width of the shoulders. To get the face bigger, move the camera closer and turn
the body about twenty degrees so one shoulder is nearer the lens.

**Looking away from the lens can be the point.** A character looking at a phone
rather than the camera, in a build where the player is on the other end of that
phone, puts the viewer in the image.

## Writing exclusions

Write every exclusion inside the main prompt, phrased as something present
rather than something absent. Tipsy's generator and Canva have no negative
prompt field, and GPT Image 2 works from one natural-language prompt, so a
separate negative prompt block is never the answer. Never hand the user one.

**Describe the wanted state affirmatively.** This is the strongest method by a
wide margin. "A plain white van with completely blank smooth panels" beats any
amount of "no lettering". The model has something to render instead of an
instruction to suppress.

**Add one blanket clause at the end.** A closing sentence such as "every
surface in the frame is blank and unlettered, with no text, no numbers, no
signage, no brand logos, and no watermark" catches the surfaces you did not
name. Put it last, where it is read against everything above it.

**Permit the props the clause would strip.** A blanket no-text clause also
removes ledgers, books, and paperwork, which are what give an office or a study
its character. Ask for them affirmatively as "cloth-bound ledgers with blank,
unlettered spines".

A bare "no X" on its own is the weakest form and sometimes summons X, so always
pair it with the affirmative version.

## Working from the approved card

A reference anchors composition as hard as it anchors face. Attaching a
portrait and asking for a different scene often returns the portrait's pose
with a new background.

**GPT Image 2 is the model to use for this.** It is the best found so far at
holding an approved photo's face and features while actually changing the pose.
Other models fail one way or the other: they keep the face and the original
composition, or they take the new pose and drift the face into someone else.

**Call the reference with @.** In Magic Hour, upload the approved image and
start the prompt with @ and the reference's name, such as `@character-name`. Then
refer to the subject as "the same man from the reference image" rather than
describing him from scratch.

**Say "the same" for everything that carries over.** The same table, the same
room, the same shirt, the same watch, the same lighting. Each "same" is an
explicit instruction to keep that element, and each element described without
it is licence to change. Then spend the detail on what is new: the pose, the
crop, the camera position, and the action.

**Same scene, keep the light. New scene, release it.** When the pose changes
but the room does not, restate the lighting as "the same lighting" and describe
it, since the light is part of what makes it the same room. When the character
moves into a different scene, do the opposite and release lighting and shadow,
or the subject looks pasted in. See "Editing an approved image".

**The reference face has to be large and clearly lit.** A small, shadowed face,
such as an over-the-shoulder shot, gives the model nothing to hold, and it
invents hair and features. Use the most front-facing, evenly lit approved image
as the reference even when a different image is the one being matched in mood.

**Restate the face in words when the reference is weak.** With a clear
reference, "the same man" is enough, as the worked example below shows. With a
small or shadowed reference, put the full Face, Build, Tattoos, and Piercings
sections back in as the safety net.

**Do not regenerate the approved image to improve it.** Rerolling the card off
itself for a closer or better-angled version produced a slightly different
person each time. Once the card is approved it is locked. Generate new poses
and scenes from it, not new versions of it.

**If composition will not budge,** generate the composition first without the
reference, then regenerate with the approved card attached to bring the face
back.

A worked example that moved an approved card into a new pose in the same room:

```
@character-name Photorealistic three quarter length portrait of the same man from the reference image, now standing at the head of the same dark conference table in the same operations room at night, cropped from mid-thigh up, shot on an 85mm lens with the camera set low at the level of the tabletop and tilted slightly upward from the seat across from him, so that he stands over the viewer's position. He leans forward slightly with his weight on one hand planted flat on the table beside an open manila folder, his other hand caught in the act of turning the folder to face the camera, head up, chin level, eyes straight into the lens with a steady direct gaze, closed lips, the composed look of a man about to say something he has decided to say. Wearing the same white dress shirt with the sleeves rolled to just below the elbow and the same dark navy tie hanging loosened and off-centre, the shirt pulling across his shoulders and back as he leans on the planted arm, the same plain steel watch with the face on the inside of the wrist, the same dark navy trousers, the suit jacket still discarded over the back of the chair beside him. On the table, the open folder holds plain pale pages angled away from the camera so that nothing on them is legible, and the two glasses from before stand near his planted hand, one full and one half empty. Behind him the same wall of dark standby screens throwing faint cool blue light, the head chair pushed back behind him, the room otherwise empty. The same lighting: a single hard warm key low and from the right raking across his jaw, throat and forearms, the cool blue rim from the screens tracing his shoulder and hair, deep shadow in the corners, the white shirt reading as textured cotton rather than flat white. Steel blue, navy, white and warm gold palette. Natural skin texture, visible pores, no beauty retouching or skin smoothing. Sharp focus on the eyes. Every surface in the frame is blank and unlettered, with all screens dark and empty, the folder pages blank and illegible, no text, no numbers, no insignia or badges, no signage, no brand logos and no watermark. He wears no jacket on his body, no lanyard, no rings, no necklace and no earrings. Vertical portrait orientation, at least 768 by 1360.
```

What it does, line by line: the @ reference and "the same man" carry identity;
the crop, lens, camera height, and viewer position set the new composition; the
planted hand, the pulling shirt, and the folder caught mid-turn put the body
under load; every carried-over garment and prop is named with "the same"; the
new props are made illegible by their angle; the lighting is restated because
the room is the same; and the prompt closes on the skin line, the eyes, the
blanket clause naming the specific surfaces in frame, the wearing-not clause,
and the orientation.
## Editing an approved image

The AI Image Editor changes an image by instruction. The shape of the
instruction decides whether the result looks real.

**Preserve identity, release everything else.** List what must stay the same:
face, features, skin tone, hair, build, tattoos, piercings, jewellery, and
clothing. Then explicitly release lighting, stance, body angle, and shadow so
the subject is relit by the new scene.

**Never lock the lighting in a scene change.** Locking pose, gaze, and the
existing lighting made the subject look pasted in, because they kept the old
scene's light in the new room.

**Small fixes go the same way.** To remove lettering from a van or a logo from
a shirt, name the surface and describe it as blank, and state that nothing else
in the image changes.

## Prompts for the rest of the set

The card is one image of ten. The rest exist to show different looks, scenes,
and sides of the character, and every one of them doubles as a chat background
a player may sit with for a whole conversation. This section is how to fill the
set without the face drifting.

### Rules for every image in the set

- **Reference the approved card every time.** Never use another set image as
  the reference for the next one. Rerolling an approved image off itself
  produced a slightly different person each time, and chaining set images off
  each other invites the same drift to compound.
- **Pick the images from Background, not from imagination.** Every location,
  garment, and prop should be one the fields already establish or permit. The
  model cannot see the set, so an image of something the character denies is a
  contradiction the player watches.
- **Release the light in a new scene.** Keep "the same lighting" only when the
  room is the same room. A new scene with the card's lighting looks pasted in.
- **Compose for a background.** Face in the upper half, the lower third quiet,
  since the message bubbles and input bar cover the bottom of the frame.
- **Nothing from a later act.** Every image is public. If the location or look
  belongs to a reveal, it waits.
- **Stop when the character is covered.** Ten is a cap, not a quota. A weak
  image is worse than a missing one.

After each approved image, update Appearance or Wardrobe for anything that
rendered differently or anything new it shows.

### The set prompt shape

For any new scene built from the card. It is the first-generation shape with
identity carried by the reference, the light released, and a composition line
added for chat backgrounds:

```
@[card-reference-name] Photorealistic [shot type and crop] of the same man from the reference image, now [location, time of day], [pose with the body under load or caught mid-action], [expression, named a notch milder than the target].
His face, features, skin tone, hair, build, tattoos and piercings remain identical to the reference image, with [each visible tattoo and piercing, side and place].
Wearing [every garment in this image, new or carried over, colour, fit, how it sits on the body].
[Setting, with the props that give it character, every one named].
[Camera: lens, camera height, tilt, and where the viewer is].
[Lighting for this scene: source, direction, height, colour, and what it rakes across], lit by this scene rather than the reference image.
His face sits in the upper half of the frame, and the lower third of the frame is [a quiet, low-detail surface: floorboards, a tabletop, bedsheets, pavement].
[Camera character: what kind of photograph this is]. [Palette: four or five colours].
Natural skin texture, visible pores, no beauty retouching or skin smoothing. Sharp focus on the eyes.
Every surface in the frame is blank and unlettered, with [the specific surfaces in this scene], no text, no numbers, no signage, no brand logos and no watermark.
[Wearing-not clause: anything from the card that must not carry over, plus jewellery and layers he does not have on].
Vertical portrait orientation, at least 768 by 1360.
```

Swap "man" for whatever the reference shows.

For a new pose in the card's own scene, use the "the same" method and the
worked example under "Working from the approved card" instead.

### Image types to choose from

Pick the ones the character's Background supports. What changes in each prompt:

- **Close quarters.** The viewer is within arm's reach: across a small table,
  the next seat, a doorway. Camera at seated eye level on a 50mm lens, a warm
  practical light nearby. Keep it within the rating and within what the public
  card would pass, since every image in the set is browsable.
- **Face closeup.** Required if the main avatar is not already one. Head and
  shoulders with the face filling most of the frame, camera close at eye level
  rather than a crop, soft light at face height, eyes to the lens. It serves
  the avatar and the reference first and a chat background second, so the
  lower-third rule can give way here.
- **Home ground.** His own space, off duty. Put one of his wants from the
  personality surface in the room as a physical object, such as the record
  collection, the half-restored bike, the plants he keeps alive. This is the
  image that makes him a person rather than a role.
- **Off duty.** The same person in the casual end of his Wardrobe, somewhere
  ordinary. The contrast with the card's clothing is the point, so describe
  every garment and keep tattoos and piercings pinned.
- **Opening scene.** The place and moment the Opening starts in, so a player
  can chat over the scene they walked into. Match the Opening's time of day,
  weather, and what he is doing.
- **Out in the world.** A location the story visits early: the bar, the venue,
  the street outside. Other people and signage are more for the model to get
  wrong, so empty the room or push others out of focus, and name every sign
  surface as blank.
- **Unguarded.** Alone, doing something ordinary, not looking at the lens.
  Three-quarter profile rather than the back of the head, so the face stays
  large enough to read as him. Camera further back, the viewer as someone who
  has just walked in.
- **Weather and daylight.** An exterior in daylight, rain, or snow, when the
  card is an interior or a night shot. A change of light reads as a different
  day in a way a change of pose alone does not.
- **Work.** His hands occupied with the actual tools of his role. Permit the
  props the blanket clause would strip, as blank-spined ledgers, blank screens,
  unlabelled equipment.

Event tags on Tipsy rotate. An image made for a current event belongs in the
set only if the setting and clothing are ones the character could plausibly be
in without the event, since the image will outlive it.

## Common problems

**The generator refuses the prompt outright.** A generic guidelines message
usually means something in the prompt read as an attempt to reproduce a real
person, or as a minor, rather than anything explicit. The usual triggers are a
dense stack of specific facial measurements, a named real person, an age or a
youthful descriptor sitting near revealing clothing, or a combination of
garments that reads younger than intended. Do not argue with it by rewording
one adjective. Strip the prompt to a plain version that certainly passes, then
add the blocks back one at a time until it fails, which identifies the trigger
in a few generations rather than a few dozen. Loosen facial specifics before
loosening clothing, since identity is the more common cause.

**The generator ignores emotion words.** Lead with the body. "Both hands
gripping his own hair, shoulders hunched to his ears, spine curved" produces
dread. The word "anxious" produces a neutral face.

**It fills empty space.** A void reads as an invitation for a starfield.
Describe the background as flat, featureless, and empty rather than as dark,
and name what the emptiness is made of, such as flat black with no texture and
no horizon line.

**It genders ambiguous figures.** If a figure must stay neutral, do not show
the body. Use a hand, or crop, or dissolve the figure into light.

**It blends two light colours into one.** If two distinct colours carry
meaning, name both and state that they are distinct.

**It adds fantasy furniture.** Armour, swords, crowns, wings, halos, and
thrones appear unbidden in anything cosmic. Say what they are wearing and
standing in instead, in plain specific terms, and close with a clause stating
that they carry nothing and wear no armour, jewellery, or headpiece.

**Two figures that should be identical come out different.** State that it is
the same person rendered twice, with the same height, build, and face, as a
positive claim. Then add a closing clause that the two figures are
indistinguishable. Listing the comparatives you do not want, taller, shorter,
thinner, gives the model the vocabulary rather than removing it.

**Tattoos do not render.** Describe coverage as dense and continuous from wrist
to shoulder rather than as individual pieces, and make sure the clothing
exposes the skin they sit on.

## Dynamic Cover

A toggle under the image set on Tipsy, off by default. When on, it takes a GIF,
MP4, or WebP, and the editor asks for a high-resolution GIF or MP4 at 9:16. It
makes the character's home page photo move, so the cover is the animated
version of the card. Upload MP4: creator testing found it displays better on
Tipsy than GIF, so there is no reason to convert.

### Step by step

1. **Pick the source.** The local original of the approved main avatar, never a
   copy saved back off Tipsy. A card whose subject is caught mid-action
   animates best, because the clip can finish a motion the photograph already
   started instead of inventing one. If the main avatar is a tight face
   closeup, expect more rerolls, since close faces drift in animation (see
   the checks below).
2. **Open Image to Video in Magic Hour** and choose Kling 2.5.
3. **Upload the card as the start frame only.** Leave the end frame empty.
   Pinning the card as both start and end frame produced a completely still
   clip.
4. **Set 9:16, 1080p, and 5 seconds.** At 10 seconds the model padded the clip
   with invented micro-motion, including the mouth parting. Audio is irrelevant
   to a cover.
5. **Write the motion prompt** in the shape below.
6. **Review the render** against the checks below before spending credits on
   anything else.
7. **Check the export** full size for a Magic Hour watermark. See "Watermarks".
8. **Upload on Tipsy.** Switch Dynamic Cover on, upload the MP4 exactly as
   Magic Hour exported it, save, and look at the character's home page to see
   the cover playing. It loops, restarting from the first frame.

### The motion prompt shape

```
Animate this photograph as a short cinematic clip with one deliberate movement.
[Mouth lock: lips closed in the first frame and for the entire clip, listing no parting, no speech, no smile opening, no jaw movement.]
The clip begins from complete stillness matching the photograph exactly: [the pose as it is in the image, limb by limb, and where the eyes are].
Beat one: [finish the motion the photograph is caught in, small and unhurried].
Beat two: [the eyes arrive at the lens and something registers, in fractions: a slight narrowing, a brow rising a fraction].
Beat three: [the one large movement, slow, saying where each limb goes and the exact position it ends in].
The clip ends held in that position, completely still, [eyes, lips], for the final several frames.
Throughout: [face and features identical to the photograph, naming eyes, nose, mouth, jaw, and facial hair, including as the face grows larger in frame]; [where the gaze stays and its one permitted exception]; [expression ceiling: composed, with at most the faintest (named micro-expression) in the final hold].
[Clothing moves only as the body moves: what sways and comes to rest, what shifts, what stays put, nothing comes loose or unbuttons.]
The camera is locked off on a tripod, no pan, no tilt, no zoom, no push in, no parallax, no handheld shake; all approach toward the viewer comes from the body moving, not the camera.
[Background: each screen, prop, and liquid named, stays exactly where it is, with nothing appearing on any surface at any point.]
Photorealistic throughout, natural skin texture retained, no smoothing, no stylisation, no added glow, no lens flares, no particles and no smoke.
Every surface stays blank and unlettered, with no text, no numbers, no signage, no logos and no watermark appearing anywhere.
Vertical portrait orientation matching the source image, at least 768 by 1360, five seconds.
```

Why each part is there:

- **The mouth lock comes second, before any movement.** The mouth parting on
  its own is a failure already seen in padded clips, so the prompt closes that
  door before it describes anything else, and states it for the whole clip
  rather than for a moment.
- **Start from the photograph exactly.** Restating the pose as the image shows
  it anchors the first frame to the card, so the still and the motion read as
  one image.
- **Three beats, one movement.** Each beat continues the one before: finish a
  small motion, let the eyes arrive and react, then make the one large move. It
  is still a single arc, just written in the order it happens.
- **Expressions in fractions.** A slight narrowing, a brow rising a fraction,
  at most the faintest asymmetry. Expression words overshoot in animation, as
  when an unimpressed look became a glower, so the prompt names the smallest
  version and sets a ceiling.
- **Identity locked as the face grows.** Movement toward the camera enlarges
  the face, and close faces are where drift happens. Naming each feature and
  saying it holds "as his face grows larger in frame" addresses the exact
  moment it would slip.
- **All approach comes from the body.** Ruling out every camera move leaves him
  as the only thing coming closer, so the background has no reason to shift,
  and the lean toward the lens still gives the sense of approach.
- **Everything else in frame is told to stay.** Screens, props, the jacket,
  even the liquid in a glass. Anything not named is left to the model's
  judgement.
- **End on a held still frame.** Several frames of complete stillness make the
  movement read as finished and intentional rather than cut off. The cover
  loops, and a hard restart back to the first frame is fine, so there is no
  need to match the last frame to the first or engineer a seamless wrap.

### Checks before accepting a render

- The lips never part and the jaw never moves.
- The face in the final hold is the same person as the card, feature for
  feature.
- The expression stayed within its ceiling.
- The camera did not move and the background did not warp.
- No text, glow, or artefacts appeared on any screen or surface.
- Clothing moved with the body and nothing came undone.
- The last frames are genuinely still.

A render that fails one check is rejected, not kept for being mostly good. The
cover is the first moving thing every visitor to the character's page sees.

**Close faces drift.** On a tightly framed card, animation rolls drifted the
face, pushed an unimpressed look into a glower, and ballooned the hair into
curls. The identity lock and the fractional expressions in the shape above are
written against exactly that.

### Worked example

This rendered well against the approved card of a man reclined in a chair with
one hand at his loosened tie:

```
Animate this photograph as a short cinematic clip with one deliberate movement. His lips are closed in the first frame and remain fully closed for the entire clip, with no parting, no speech, no smile opening and no jaw movement at any point. The clip begins from complete stillness matching the photograph exactly: he is reclined in the chair, one forearm on the armrest, the other hand at his loosened tie, eyes toward the lens. Beat one: his hand at the collar finishes the motion it is caught in, drawing the tie a final centimetre looser in one small unhurried tug, his eyes dropping briefly toward his own hand as he does it. Beat two: his eyes lift back up to the lens and stop there, and something registers, a slight narrowing of the eyes, one brow rising a fraction, the stillness of a man who has just become aware he is being watched and finds it interesting rather than alarming. Beat three: he leans slowly forward out of the recline, his shoulders and head coming toward the camera, the hand at his tie lowering to rest on his thigh as he moves, his other forearm sliding forward along the armrest to take his weight, until he is sitting forward with his forearms low, chin dipping slightly so that he is looking at the lens from just under his brow, closer now, attentive and intrigued. The clip ends held in that leaned-forward position, completely still, eyes steady on the lens, lips closed, for the final several frames. Throughout: his face and features remain identical to the photograph with no change to the shape of his eyes, nose, mouth, jaw or stubble as his face grows larger in frame, his gaze stays on the lens except for the brief drop to his hand in beat one, and his expression stays composed, with at most the faintest closed-lip asymmetry at one corner in the final hold. His clothing moves only as the body moves: the tie sways naturally with the lean and comes to rest, the shirt shifts across his shoulders, the sleeves stay at the same place on his forearms, nothing comes loose or unbuttons. The camera is locked off on a tripod, no pan, no tilt, no zoom, no push in, no parallax, no handheld shake; all approach toward the viewer comes from his body moving, not the camera. Behind him the wall of screens stays dark and empty with nothing appearing on them at any point, the faint cool blue glow steady, the jacket on the chair unmoving, and on the table the glasses and folder stay exactly where they are with the liquid still. Photorealistic throughout, natural skin texture retained, no smoothing, no stylisation, no added glow, no lens flares, no particles and no smoke. Every surface stays blank and unlettered, with no text, no numbers, no signage, no logos and no watermark appearing anywhere. Vertical portrait orientation matching the source image, at least 768 by 1360, five seconds.
```

### File size

Tipsy publishes no size limit for the cover, and none has been hit with
ordinary exports. Keep the file average: a 5 second 1080p MP4 exactly as Magic
Hour exports it. Do not upscale to 4K, lengthen the clip, or re-encode at a
higher bitrate to chase quality. If an upload is ever refused, file size is the
first thing to check.

The cover is public and held to the rating like everything else here.

## Images generated in chat

Tipsy's in-chat image generation takes its lead from the card. A shirtless card
produces shirtless in-chat images long after the scene has moved on, because
the card anchors composition. The fix is a WARDROBE block in Background listing
default clothing and a closed list of when anything else is permitted, and a
card that shows the default look.

## Tipsy's built-in generator

For creators generating inside Tipsy instead:

- **Emphasis and de-emphasis.** `((bright blue eyes))` weights a feature up and
  `[hat]` weights it down. De-emphasis reduces something rather than removing
  it, so it is not a substitute for the affirmative methods above.
- **Face Mimic and Style Mimicry.** Two sliders when using a reference image.
  Face Mimic drives facial similarity, Style Mimicry drives overall style. Keep
  Face Mimic high and Style Mimicry low, and describe only what the reference
  does not already show. Pushing both high strangles the generator.
- **Artistic styles and AI Optimize** exist in the generator. Leave styles off
  for photoreal work, for the same reason as Magic Hour's presets.

## Image rules in Worlds

Each rule has a trigger, guidance, an aspect ratio, a size, a sample prompt,
and an optional reference.

Write the trigger as a specific story condition rather than a mood. Tie any
variation to a tracker value and describe what changes at each band, since one
sample prompt has to serve every firing.

Keep the guidance consistent with the character fields. A sample prompt
describing two characters as similar-but-different will contradict a rule
demanding they be identical, and it leaks into prose as well as art.

Some things are easier in code than in a diffusion model. Absence, emptiness, a
controlled gradient, and anything that must look identical every time are all
better handled by the code-generated option.
