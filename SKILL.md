---
name: app-store-naming
description: Research, generate, validate, and optimize App Store app names, subtitles, and keyword strategy. Use when the user wants to name or rename an iOS/iPadOS/macOS app, check whether a candidate name appears usable, compare naming options, or optimize naming for ASO, brand, localization, scope, and App Store metadata compliance.
---

# App Store Naming

## Purpose

Create App Store names that are not merely catchy, but practical to ship.

The workflow must balance:

- App Store name availability and collision risk
- ASO relevance and search intent
- Brand distinctiveness and memorability
- Product clarity
- Future product scope
- Localization and pronunciation
- Trademark / third-party brand risk
- App Review metadata compliance
- Coordination between app name, subtitle, and keyword field

The user's explicit instructions take precedence over this skill.

## Core principle

Do not treat naming as a pure brainstorming task.

Use this sequence:

`understand product -> research market -> generate candidates -> hard-filter -> live-check -> ASO optimize -> rank -> provide final metadata set -> state what still requires App Store Connect/legal verification`

Never claim that a name is definitively available merely because no public App Store result was found.

## Official constraints to enforce

Read `references/apple-rules.md` before doing final validation.

At minimum enforce:

- App Store app name: 2–30 characters.
- Subtitle: no more than 30 characters.
- Keywords field: up to 100 bytes.
- Use a unique app name and accurate keywords.
- Do not stuff metadata with trademarked terms, popular app names, pricing information, or irrelevant phrases.
- Subtitle must not reference other apps or make unverifiable product claims.
- The App Store can search by app name, subtitle, keywords, and company/developer name.
- Do not waste keyword-field bytes by needlessly repeating app-name/company-name terms.

If Apple changes these rules, current official Apple documentation overrides this skill.

## Inputs

Use information already provided by the user. Do not ask again for facts already known.

Useful inputs include:

- Product category and core job-to-be-done
- Current feature set
- Likely future scope
- Primary market / storefront
- Primary language and planned localizations
- Target users
- Existing brand/company/product names
- Competitor/reference apps
- Monetization model if it affects positioning
- Desired tone: brand-like, descriptive, technical, playful, premium, etc.
- Existing candidate names, if any

If some inputs are missing, make reasonable assumptions and label them. Do not block a naming task for nonessential missing details.

## Modes

Infer the mode from the request.

### CREATE
Generate a new App Store naming system from scratch.

### EVALUATE
Evaluate one or more names supplied by the user.

### RENAME
Replace an existing name while preserving product recognition where useful.

### VERIFY
Focus on current public collision checks, metadata constraints, and risk.

### LOCALIZE
Create or evaluate localized names for multiple storefront languages.

## Workflow

### 1. Build the naming brief

Condense the product into five statements:

1. `Core job`: what the user primarily comes to the app to do.
2. `Primary search intent`: what a likely user may type into App Store search.
3. `Brand promise`: the product impression the name should create.
4. `Scope boundary`: what the app may expand into over the next 1–3 years.
5. `Naming constraints`: market, language, tone, forbidden terms, existing brand constraints.

Correct faulty premises before naming. Example: if the user says the app is “only for New Concept English” but also says it will later contain other language-learning materials, do not anchor the brand permanently to “New Concept”.

### 2. Research current market when live tools are available

For App Store naming, current verification materially improves accuracy. Use live web/search/browser tools when available.

Research:

- Exact candidate names on the target App Store storefront
- Close spelling / phonetic variants
- Major apps in the same category
- Common category wording used in current App Store names/subtitles
- Existing brands/companies/products with the same or confusingly similar name
- Obvious trademark conflicts using authoritative trademark databases when practical

Prefer primary sources for hard rules and authoritative registries for trademark facts.

For public App Store collision checks, search both exact and normalized variants. Example queries:

- `site:apps.apple.com "Candidate Name"`
- `site:apps.apple.com/cn/app "候选名"`
- `"Candidate Name" app`
- `"Candidate Name" software`

When a target market is specified, prioritize that storefront and language.

Do not equate “no search result” with final name availability.

### 3. Create candidate families

Generate candidates from multiple strategies rather than one naming style.

Candidate families:

- `Brand-first`: short invented or distinctive brand name
- `Brand + descriptor`: distinctive brand plus a category/function cue
- `Descriptive`: immediately understandable search-intent name
- `Semantic`: word with a meaningful association to the product outcome
- `Compound`: two simple words with a clear product association
- `Localized`: language-native name rather than literal translation

For China-first products, consider both Chinese discovery behavior and a brand that remains usable internationally. Do not force pinyin/English if Chinese wording is materially clearer; do not force Chinese if future global expansion makes the name brittle.

Generate broadly first, then filter. Do not dump the raw brainstorming list on the user unless requested.

### 4. Hard-filter candidates

Reject or heavily penalize candidates that:

- exceed Apple metadata limits
- are already clearly occupied in the relevant localization/storefront
- are confusingly close to a major competitor or third-party brand
- depend on another app/company/trademark for ASO
- imply functionality the app does not provide
- include unverifiable superlatives such as “Best”, “No.1”, “Official” without basis
- include prices or irrelevant search terms
- are too generic to build a defensible brand
- are difficult to type, pronounce, remember, or distinguish verbally
- create a false scope ceiling for a product likely to expand
- become awkward or misleading after localization

Availability and serious trademark conflicts are gates, not merely small score deductions.

### 5. Evaluate ASO as a metadata system

Do not optimize the app name in isolation.

Treat these as a coordinated system:

`App Name + Subtitle + Keyword Field + Developer Name`

Use the app name for the strongest combination of brand and high-value intent. Use the subtitle to clarify the use case and cover adjacent intent. Use the keyword field for useful non-duplicative terms.

Avoid blindly repeating the same token across name, subtitle, and keywords.

If no trustworthy keyword-volume data is available, do not invent search volumes. Label search-demand judgments as qualitative estimates based on market/category evidence.

### 6. Score surviving candidates

Read `references/scoring-rubric.md`.

Use the rubric to compare candidates consistently, but do not let a numeric score override a hard legal/availability/compliance gate.

Score out of 100:

- ASO relevance & search intent: 25
- Brand distinctiveness: 20
- Product clarity: 15
- Memorability / pronunciation / typing: 10
- Future extensibility: 10
- Competitive uniqueness: 10
- Localization robustness: 5
- App Store presentation fit: 5

Also show separately:

- `Public collision`: Clear / Possible conflict / Conflict / Not checked
- `Trademark risk`: Low / Medium / High / Not checked
- `ASC final availability`: Confirmed only if actually verified in App Store Connect; otherwise `Requires ASC verification`

### 7. Build final metadata combinations

For the top candidates, create a complete set:

- App name
- Subtitle
- Keyword strategy (not necessarily a final 100-byte string unless asked)
- Optional short Home Screen display name if a shorter in-app label is useful
- Localized version(s) when relevant

Run `scripts/validate_metadata.py` when code execution is available.

### 8. Final verification ladder

Use this confidence ladder exactly:

#### Level A — Public conflict scan
No obvious exact/near collision found in public App Store/web searches.

#### Level B — Brand/trademark screen
No obvious conflict found in relevant brand/trademark research. This is not legal clearance.

#### Level C — App Store Connect availability
The name is actually accepted in the intended App Store Connect localization/app record workflow. This is the operational availability check.

Do not label a candidate “available” without Level C. Before Level C, say `publicly appears clear` or `no obvious public collision found`.

If the user has not performed Level C, end with the exact candidate(s) they should try first in App Store Connect.

## Output format

Default to a decisive report, not a giant brainstorm list.

### A. Naming brief
A compact 3–6 line summary of the naming strategy and any corrected assumptions.

### B. Candidate matrix
Normally show 6–10 finalists.

Columns:

| Candidate | Strategy | ASO fit | Brand fit | Scope fit | Public collision | Risk | Score |

Use short evidence-based notes, not vague praise.

### C. Top 3 metadata sets
For each:

- `App name:`
- `Subtitle:`
- `ASO angle:`
- `Why it works:`
- `Main risk:`
- `Availability status:`

### D. Recommendation
Give:

- `Recommended`: one primary choice
- `Backup 1`
- `Backup 2`

State why the primary choice is preferred. If live availability is unverified, make the recommendation conditional on ASC acceptance.

### E. Before creating the App Store record
Provide the minimal final checks still required, especially App Store Connect name acceptance and any unresolved trademark issue.

## Evidence discipline

Explicitly distinguish:

- `Confirmed`: Apple rules, live search findings, registry records
- `Inferred`: memorability, brand feel, qualitative ASO intent
- `Unverified`: App Store Connect reservation status, legal trademark clearance, unavailable keyword-volume data

Never fabricate:

- App Store search volume
- download estimates
- keyword difficulty
- trademark registration status
- App Store Connect availability

## Special handling: Chinese market

When the primary market is mainland China:

- Test whether the name is natural when spoken aloud in Chinese.
- Prefer short, memorable names that users can type without unusual characters.
- Check whether a Chinese name is too generic to own mentally or commercially.
- Consider a compact brand name plus a descriptive subtitle rather than turning the entire app name into keyword stuffing.
- Check whether the name survives expansion beyond a single textbook/course/provider when the product roadmap is broader.
- If an English brand is used, check likely Chinese pronunciation, transliteration ambiguity, and whether users can recall the spelling.

## Special handling: existing candidate supplied by user

Do not immediately praise it.

First test:

1. Is the product premise behind the name still correct?
2. Is it within metadata limits?
3. Does it collide with existing apps/brands?
4. Is it unnecessarily narrow?
5. Does it waste the app-name field on low-value words?
6. Does the subtitle compensate for brand ambiguity?
7. Is there a better brand/ASO division across fields?

Then provide a verdict and alternatives.

## References

- `references/apple-rules.md`
- `references/scoring-rubric.md`
- `references/availability-check.md`
- `references/aso-framework.md`
- `templates/naming-report.md`
