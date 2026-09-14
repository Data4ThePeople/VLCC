# Hero image prompts: Turns out oil is close to $150, in real life, not on your screen

Target: 1680x1080 landscape. Generate wide (16:9 or 3:2); the crop is done with
`~/.claude/d4tp-process/hero fit`. Keep the ship's bow and stern inside the
middle 80% of the frame so the crop does not clip it. No text, no logos, no
flags, no visible ship name.

## Prompt 1

A very large crude carrier, a supertanker over 1,000 feet long, made entirely
of polished solid gold, sailing across open ocean. The ship has the true
proportions of a VLCC: a long, low, flat hull sitting deep in the water,
fully loaded, with the white superstructure and bridge replaced by gold at
the stern, a single funnel, and a deck covered in gold pipework, catwalks and
manifolds. Every surface is gold, from the anchor to the bridge windows.
Late-afternoon sun low on the horizon lights the hull from the side, so the
gold reflects warm highlights and the water shows a long golden reflection.
Deep blue-green sea with small whitecaps and a broad wake behind the ship.
Photorealistic, shot from a helicopter at a three-quarter angle slightly
above the waterline, wide-angle lens, the ship filling about two thirds of
the frame with open sea and a clear sky around it. High detail, sharp focus,
no text, no watermark, no people.

## Prompt 2 (variant)

Cinematic aerial photograph of a supertanker cast in solid gold crossing the
ocean alone, seen from directly abeam so the entire length of the hull runs
across the frame. The ship is a real VLCC: a low, wide hull fully loaded and
riding deep, stern superstructure, deck pipes, gold from bow to stern with a
brushed-metal finish rather than a mirror finish. Overcast morning light,
grey-blue sea with gentle swell, a soft glint along the deck edge. The gold
is the only warm color in the picture. Photorealistic, 35mm, high detail,
no text, no watermark, no people.

## Prompt 3 (variant, closer)

Photorealistic close view of the bow of a gold supertanker cutting through
dark blue ocean, spray breaking white against a hull of solid gold, the rest
of the ship receding into the distance along the frame. A tanker's bulbous
bow and anchor pockets, all gold, with fine hull plating and weld seams
visible. Strong directional sunlight, deep shadow on the far side of the
hull. Wide-angle, low camera just above the water, sharp focus, no text, no
watermark, no people.

## Notes for generating

- The most common failure is a container ship or a cruise ship in gold. If
  the result has stacked boxes, many windows or a tall white superstructure,
  add "oil tanker, no containers, no cranes, flat deck with pipes" and
  regenerate.
- Ask for the ship well inside the frame. A bow or stern touching the edge
  cannot be fixed by the crop.
- A brushed finish (Prompt 2) reads as gold at thumbnail size; a mirror
  finish can read as yellow chrome.

## Chosen

File: images/supertanker-rates-hero-source.jpg (Gemini, from Prompt 1; cropped center to images/supertanker-rates-hero-1680x1080.png)
Alt (under 500 characters): A supertanker made entirely of polished gold sails across a deep blue ocean in low afternoon sun, seen from above at a three-quarter angle. The long, low hull rides deep in the water, with gold pipework across the deck and a gold bridge and funnel at the stern. Whitecaps break at the bow and a golden reflection spreads across the water beside the hull under a clear sky.
