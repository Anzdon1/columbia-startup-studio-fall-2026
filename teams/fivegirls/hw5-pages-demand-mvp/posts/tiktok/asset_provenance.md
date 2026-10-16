# Video asset provenance

Created October 16, 2026, for the Five Girls HW5 organic-social draft. No asset is evidence of a real inspected restroom or a posted campaign.

| Asset | Source and treatment |
| --- | --- |
| `assets/nyc-illustration.png` | New image generated with the built-in ImageGen tool. Used as an illustrative opening backdrop with a visible “AI-generated illustration” label. No existing venue photo or testimonial was supplied. The original generated raster is preserved in this folder. |
| `assets/finder-mobile.png` | Anonymous screenshot of `https://nyc.imfinethanku.me/find/`, captured October 16, 2026, at 06:49 UTC / 02:49 New York time. Public Map view, default city collection, no sign-in, no geolocation permission, and no data writes. Captured `.finder-map-panel` at a 390 × 844 CSS-pixel browser viewport with 2× pixel density; the asset preserves its visible map attribution. |
| `assets/brand-lockup.png`, `assets/brand-mark.png` | Existing approved Restroom Ready R-tile identity, copied from the product repository's `brand/logo/lockup.png` and `brand/logo/favicon_512.png`. No logo redraw. |
| Map tiles | OpenStreetMap contributors, shown through the public app's Leaflet view. Attribution retained on the capture. [OpenStreetMap copyright and licence](https://www.openstreetmap.org/copyright). |
| Narration | macOS `say`, Samantha synthetic voice, 174 words per minute. Original project script, not a real speaker or customer quotation. |
| Typography | System Helvetica and SF Mono used as the style guide's sans-serif and monospace fallbacks. No font binaries redistributed. |
| Layout, text animation, cover, storyboard | Project-authored composition using Pillow and FFmpeg. White cards, #EEF2F3 background, #1E2A30 ink, #56666E supporting text, and #2B59C3 brand accent follow the retained checklist direction. |
| Music / third-party video | None. |

## Image-generation prompt

> Use case: ads-marketing. Asset type: opening backdrop for a 9:16 vertical mobile video about Restroom Ready NYC, a restroom discovery website. Generate a polished editorial illustration, not a photograph: New York sidewalk at a cross street, generic brownstone facades, distant midtown towers and simple street geometry, with a single small anonymous person walking. Calm precise linework, slightly textured architectural paper illustration, blue #2B59C3 accents, pale blue-gray #EEF2F3, white, ink #1E2A30, generous clear pale sky and negative space across the top half and central upper area for separately typeset titles. Buildings and street occupy the bottom third. Portrait composition 9:16. No text, no letters, no street names, no signage, no restroom interior, no brand marks, no interface mockup, no logos, no map pins, no photorealistic claims. This is an illustrative NYC mood scene, not an inspected location or evidence of a restroom.

## Reproduction

`render_video.py` renders frames from the included assets and generates the voiceover on macOS. It requires Python with Pillow, the listed system fonts, `say`, and an FFmpeg build with libx264 and AAC. Set `FFMPEG_BIN` to an installed FFmpeg path, or install `imageio-ffmpeg` in the active Python environment. The original render used a temporary encoder dependency, with no system-wide installation. It does not contact Firebase or publish anything.

The final MP4 was fully decoded after rendering; dimension, duration, frame-rate, and audio checks are recorded in `video-metadata.json`. First, middle, and ending frames were visually inspected. No ffprobe binary was installed; stream metadata and full decode were checked with the FFmpeg binary instead.
