# Images

## Platform requirements

At least 768 x 1360. Use the platform's upscale function on every upload. A
landscape image will be cropped on the card, so check the preview.

Only original or authorised images. No watermarks or other platforms' logos.
No real people's photos, and no real person's name in a prompt. Describe the
features instead, since unauthorised likenesses can limit public display.

Public images follow the rating regardless of what the chat contains: nothing
involving minors, no explicit nudity or sex acts, no excessive violence or
gore.

## Prompt syntax

Tipsy supports emphasis with parentheses and de-emphasis with brackets.
`((bright blue eyes))` weights a feature up, `[hat]` weights it down.

**There is no negative prompt field.** Not on Tipsy, not in Canva. Never hand a
user a separate negative prompt block, and never write "put X in the negative
prompt" as advice. Every exclusion has to live inside the one prompt, phrased
as something present rather than something absent.

## Writing exclusions without a negative prompt

Three techniques, in order of how reliably they hold.

**Describe the wanted state affirmatively.** This is the strongest by a wide
margin. "A plain white van with completely blank smooth panels" beats any
amount of "no lettering". The model has something to render instead of an
instruction to suppress, and rendering is what it does.

**Add one blanket clause at the end.** A closing sentence such as "every
surface in the frame is blank and unlettered, with no text, no numbers, no
signage, no brand logos, and no watermark" catches the surfaces you did not
think to name individually. Put it last, where it is read against everything
above it.

**Use the de-emphasis brackets, on Tipsy only.** `[background detail]` pushes
something down without removing it. This is the closest thing to a negative
the platform has, and it works on things you want less of rather than things
you want gone.

A bare "no X" on its own is the weakest form and sometimes summons X, so always
pair it with the affirmative version of the same instruction rather than using
it alone.

Two sliders when using a reference image. Face Mimic drives facial similarity.
Style Mimicry drives overall style. Both reduce the generator's freedom, and
pushing both high strangles it.

## Working with a reference image

A reference anchors composition as hard as it anchors face. This is the most
common surprise: attaching a portrait and asking for a different scene returns
the portrait's pose with a new background.

Keep Face Mimic high and Style Mimicry low, and describe only what the
reference does not already contain. Re-specifying features the reference shows
dilutes the match.

If composition will not budge, generate the composition without the reference
first, then regenerate with the reference at minimum style to bring the face
back.

**Model choice does more here than prompt wording.** Wherever the tool lets you
pick a model, GPT Image 2 is the best at holding an approved reference photo's
face and features while actually changing the pose. Most other models fail one
way or the other: they keep the face and hand back the reference's original
composition with a new background, or they take the new pose and drift the face
into someone else. Reach for it first on any greeting shot, alternate scene, or
second angle that has to look like the same person as the card.

That also makes the two-pass workaround above mostly unnecessary. Try the
single pass on GPT Image 2 before splitting the job, and keep the two-pass
route for tools that do not offer a model choice.

## Common problems

**The generator ignores emotion words.** Lead with the body. "Both hands
gripping his own hair, shoulders hunched to his ears, spine curved" produces
dread. The word "anxious" produces a neutral face.

**It fills empty space.** A void reads as an invitation for a starfield.
Describe the background as flat, featureless, and empty rather than as dark,
and name what the emptiness is made of, such as flat black with no texture and
no horizon line. Naming the wanted emptiness works where naming the unwanted
stars does not.

**It genders ambiguous figures.** If a figure must stay neutral, do not show
the body. Use a hand, or crop, or dissolve the figure into light.

**It blends two light colours into one.** If two distinct colours carry
meaning, emphasise both and state that they are distinct.

**It adds fantasy furniture.** Armour, swords, crowns, wings, halos, and
thrones appear unbidden in anything cosmic. Say what they are wearing and
standing in instead, in plain specific terms, and close with a clause stating
that they carry nothing and wear no armour, jewellery, or headpiece. The
description of the plain thing is what displaces the ornate one.

**Two figures that should be identical come out different.** State that it is
the same person rendered twice, with the same height, the same build, and the
same face, and say so as a positive claim. Then add a closing clause that the
two figures are indistinguishable from each other. Listing the comparatives you
do not want, taller, shorter, thinner, gives the model the vocabulary rather
than removing it.

## Image rules in Worlds

Each rule has a trigger, guidance, an aspect ratio, a size, a sample prompt,
and an optional reference.

Write the trigger as a specific story condition rather than a mood. Tie any
variation to a tracker value and describe what changes at each band, since one
sample prompt has to serve every firing.

Keep the guidance consistent with the character fields. A sample prompt
describing two characters as similar-but-different will contradict a rule
demanding they be identical, and it leaks into prose as well as art.

Some things are easier in code than in a diffusion model. Absence, emptiness,
a controlled gradient, and anything that must look identical every time are all
better handled by the code-generated option.
