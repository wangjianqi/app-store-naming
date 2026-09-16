# Availability and collision-check procedure

## Goal

Reduce naming risk without pretending public search can reserve a name.

## Level A — Public App Store collision scan

For every serious finalist:

1. Search exact name in the target storefront/language.
2. Search punctuation/spacing variants.
3. Search singular/plural and obvious spelling variants.
4. Search phonetic/transliteration variants when relevant.
5. Search same-category apps with similar leading brand words.

Example web queries:

- `site:apps.apple.com "Exact Name"`
- `site:apps.apple.com/cn/app "中文名称"`
- `site:apps.apple.com/jp/app "候補名"`
- `"Exact Name" iPhone app`
- `"Exact Name" software`

Classify:

- `Clear`: no obvious exact/near collision found
- `Possible conflict`: similar app/brand exists
- `Conflict`: exact or strongly confusing collision exists
- `Not checked`: live search unavailable

Do not call `Clear` “available”.

## Level B — Brand and trademark screen

Search:

- general web
- company/product directories when relevant
- WIPO Global Brand Database for international screening
- CNIPA resources for China when available/appropriate
- USPTO for US-focused launches when appropriate
- other target-country official registries where material

This is a risk screen, not legal advice or legal clearance.

Classify:

- Low: no obvious relevant conflict found
- Medium: similar mark/brand exists or category overlap is unclear
- High: same/similar brand in software/adjacent relevant class or strong market recognition
- Not checked

## Level C — App Store Connect operational check

Final operational availability requires the intended app name/localization to be accepted by App Store Connect.

If the model/tool can access App Store Connect, do not create or submit an app record without explicit user authorization. A non-mutating availability checker may be used if one exists.

If the user checks manually, give the exact finalists in priority order to try.

## Important caveats

- A dormant/unlisted/not-public app may still affect naming availability.
- A public search result can lag or be region-dependent.
- App Store availability does not equal trademark safety.
- Trademark registration absence does not guarantee freedom to use a brand.
