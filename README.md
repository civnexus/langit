# Mount Paradise

Destination website for stays, gatherings, private residences, wellness and the 800 Club in Trawas, East Java.

Live: https://langit-three.vercel.app/
Intended custom domain: MountParadiseJava.com
Repository: https://github.com/civnexus/langit

## Build and preview

Dependency-free static HTML, CSS and JavaScript. Run `python3 scripts/build.py`, then `python3 scripts/check.py`. Preview with `python3 -m http.server 8765`.

Shared templates: scripts/build.py. Destination content: scripts/destination.py. The retained private residence collection comes from scripts/pages.py and scripts/tiers.py. Legacy clubhouse content is overridden by destination.py. Commit sources and generated pages together.

19 pages, including Home, Stay, Gather, Corporate Retreats, Weddings, Residences, Main Lodge, Wellness, 800 Club, Discover, Arvorest Woods, Botanical Gardens, Land, Mountain Living and private lodge collection/detail pages. Old clubhouse.html and vision.html URLs retain updated content with canonical links to their new equivalents.

## Enquiries and domain

Direct email links only, to info@mountparadisejava.com. No forms or lead database. Separate subject lines for stays, gatherings, ownership and membership.

After connecting the custom domain, run `SITE_URL=https://mountparadisejava.com python3 scripts/build.py` and republish. Until then canonical URLs, sitemap and share images use the working Vercel host. The domain connection and mailbox setup are separate tasks. OG/Twitter metadata uses a 1200x630 JPEG of the approved Main Lodge.

## Content direction

See DESTINATION-DIRECTION.md for architecture, planting references, named tree locations, Arvorest Woods and the arboretum vision. Arvorest uses intentional photo placeholders pending confirmed imagery. Existing residential Garden Lodge name does not apply to the Main Lodge.

Long-term 40–50 hectare scale is an ambition. Existing development and future facilities are differentiated in the copy. No unsupported water chemistry or health claims.
