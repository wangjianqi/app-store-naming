# ASO naming framework

## Principle

App Store naming is a constrained allocation problem.

Use each metadata field for the job it is best at:

- `Name`: brand + strongest high-value intent
- `Subtitle`: clarify use case + adjacent intent
- `Keywords`: useful non-duplicative search terms
- `Developer/company name`: already contributes to search; do not waste keyword bytes repeating it

## Brand vs descriptive balance

### Brand-first

Example pattern:

`LumaNote`

Strengths:

- distinctive
- scalable
- strong brand ownership

Weakness:

- may need subtitle to explain the product

### Brand + descriptor

Example pattern:

`LumaNote: Voice Notes`

Strengths:

- balances brand and discovery
- gives search context immediately

Weakness:

- consumes name characters quickly

### Pure descriptive

Example pattern:

`Voice Note Recorder`

Strengths:

- immediate clarity

Weaknesses:

- weak ownership
- high collision/genericity risk
- hard to differentiate

Default preference for most commercial apps: distinctive brand + carefully chosen descriptive support in the name or subtitle.

## Avoid keyword stuffing

Bad pattern:

`Scanner PDF Scan OCR Document AI`

Problems:

- reads unnaturally
- can create metadata-review risk
- weak brand memory
- burns scarce characters

Prefer a coherent name plus subtitle/keywords.

## Search intent hierarchy

Classify candidate terms:

1. `Core intent`: what the user is explicitly trying to do
2. `Category`: the general product category
3. `Feature`: a specific capability
4. `Outcome`: what the user wants to achieve
5. `Audience`: a specific user segment
6. `Brand`: distinctive identifier

Put core intent ahead of incidental features.

## Evidence rule

When there is no trusted ASO database/tool:

- do not invent keyword volume
- do not invent difficulty scores
- use qualitative labels such as `highly relevant`, `category-generic`, `niche intent`, `brand-only`
- explain the evidence behind the judgment

## Scope test

Ask:

> If the product expands according to the current roadmap, will this name become inaccurate or embarrassing?

A name can be excellent for current ASO and still be strategically wrong if it permanently anchors the product to a narrow source, course, language, or temporary feature.
