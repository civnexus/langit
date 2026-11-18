# Mount Paradise

A seven-page architectural concept website for a proposed mountain community in Trawas, East Java.

Live site: https://civnexus.github.io/langit/

## Edit and preview

The site is dependency-free HTML, CSS and JavaScript. Open `index.html` directly, or run `python3 -m http.server 8765` from this directory and visit http://localhost:8765.

Page content is maintained in `scripts/pages.py`, with shared templates in `scripts/build.py`. After changing it, run `python3 scripts/build.py`. Styles and interactions are in `styles.css` and `site.js`. Commit the generated HTML alongside source changes. GitHub Pages serves the root of `main`.

## Artwork

The user-approved cinematic image and original watercolor are preserved as `assets/signature-lodge.jpg` and `assets/original-watercolor.jpg`. The actual villa photograph and the earlier repetitive community watercolor have been removed from the published assets. Original artwork uses the built-in Imagegen tool. The approved cinematic exterior, interior and evening images are retained. New additions are `landscape.jpg`, `terrace.jpg`, `dining.jpg` and `forest-style.jpg`. See `ART-DIRECTION.md` for the prompt set. All assets are local; no stock image services or external scripts are used.

Renderings and the watercolor community layout are conceptual. They do not establish surveyed boundaries, guaranteed views, plot counts, floor plans, approved amenities or completed construction. Phase 1 is the existing built pilot. Phase 2 covers 10 hectares. Phase 3 is a future expansion opportunity of 20+ hectares.

## Verification

Local links and asset paths checked across all six pages. Round-two browser review checked desktop lodge layouts and a 390px-wide mobile phase timeline. Local validation checked every page/asset link, all nine retained/new artwork placements and removal of retired image references and old phase labels. A full device/browser matrix has not been tested.

## Expanded lodge collection

`lodge-tiers.html` adds Retreat, Family, Reserve and Estate concepts. Content is in `scripts/tiers.py`; original lodge styles remain in place. Four new built-in Imagegen artworks and prompts are in `assets/` and `TIER-PROMPTS.md`. Tiers describe proposed space and amenities, not fixed pricing or approved specifications. Desktop and 390px mobile layouts were reviewed.
