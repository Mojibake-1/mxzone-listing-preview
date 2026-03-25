---
name: amazon-listing-preview
description: Turn an Amazon ASIN plus real product photos into a complete Amazon image suite, image-generation prompt plan, and a previewable listing + A+ HTML page. Use when Antigravity/Codex needs to create Amazon main images, gallery images, A+ banners, listing mockups, or preview pages from ASIN data, storefront facts, and user-supplied product photos.
---

# Amazon Listing Preview — Best Seller Tier

Build an Amazon listing image set that matches the visual standard of Anker, LEVOIT, Tineco, Dyson, Shark, eufy, and Roborock Best Sellers. Every generated image must be **anchored to the user's real product photos** for visual consistency.

## Design DNA (Extracted from 10+ Top-Tier Best Sellers)

These are non-negotiable design principles derived from studying actual Best Seller listings:

### 1. Visual Anchor Consistency (最关键的一条)
- The **exact same product appearance** must be maintained across ALL images — gallery, A+, and infographics.
- Every generated image MUST reference the user's original product photos as the visual anchor.
- Lighting direction, material texture (microfiber fuzz, plastic housing color, filter mesh pattern), and product proportions must be **identical** in every frame.
- When generating images, ALWAYS pass the user's reference photos to the image generation tool so the AI can match the real product.

### 2. Text Overlay Rules (从Anker/LEVOIT/Tineco提炼)
- **2-4 word benefit labels** only — never paragraphs (e.g. "5x Longer Lifespan", "Smart iLoop Sensor", "Perfect for MacBook M4")
- **Clean sans-serif typography**: Inter, Montserrat, or Proxima Nova style
- **Floating callout lines**: thin pointer lines connecting labels to specific product features
- **Bold hierarchy**: Title (24-28pt Bold) → Subtitle (16-18pt Medium) → Fine print (10-12pt Regular)
- Brand color accent used sparingly — 1 accent color max per image

### 3. Gallery Narrative Flow (7-Slot Conversion Funnel)
The gallery is NOT random photos. It's a **story arc** designed to convert:
1. Trust (white BG main) → 2. Desire (hero benefit) → 3. Proof (real-world use) → 4. Differentiation (vs competition) → 5. Context (lifestyle) → 6. Detail (materials/tech) → 7. Confidence (package contents)

### 4. A+ Content Architecture (从Tineco/Roborock提炼)
- **Full-width cinematic hero banner** at the top — selling the "dream", not specs
- **Modular feature blocks**: 3-4 distinct benefit modules with consistent background colors
- **Product Comparison Table**: Cross-sell within brand family (essential for premium brands)
- **Interactive visual motifs**: Tineco uses red/blue circles for dirty/clean; LEVOIT uses cross-section layers; Anker uses size comparison with everyday objects
- **4-grid lifestyle feature section**: 4 equal boxes, each with a lifestyle photo + 2-word headline + 1-line description

## Workflow

1. **Collect minimum viable inputs.**
   Required:
   - ASIN (or product title if no ASIN)
   - Real product photos — front / side / top / packaging (at least 1, ideally 3+)
   Optional:
   - Brand / store name
   - Current title and bullets
   - Pack count, dimensions, materials, compatibility list
   - Banned claims or mandatory claims
   - Marketplace (US/UK/DE/JP etc.)

2. **Derive a fact sheet before writing any prompts.**
   - Pull only verifiable facts from the live listing, package photos, manuals, or user's notes.
   - Treat compatibility, dimensions, filtration percentages, certifications, and warranty claims as high-risk facts.
   - If a claim cannot be verified, omit it or label it as a visual design direction rather than product copy.
   - **Extract key visual attributes from the reference photos**: exact color (grey/white roller with dark speckles), shape (cylinder, rectangular filter housing), surface finish (fuzzy microfiber, pleated HEPA), connector style, brand markings.

3. **Build the shot plan.**
   - Use [references/shot-plan.md](references/shot-plan.md) for the canonical image slots, naming convention, and **per-slot prompt scaffolding**.
   - Keep gallery to 1 main + 6 support images unless user asks otherwise.
   - Keep A+ to 7 banners unless brand template requires another set.
   - For each slot, write the prompt following the **6-block prompt structure** defined in shot-plan.md.

4. **Generate images with the reference photo anchor.**
   - **CRITICAL**: For EVERY image generation call, pass the user's reference photo(s) as `ImagePaths` so the AI can visually match the real product.
   - Generate each image against an explicit slot objective, copy block, and filename.
   - The product in every generated image must visually match the reference photos — same colors, proportions, and textures.
   - Save output images with the exact filenames expected by the preview manifest.

5. **Render the preview page.**
   - Write a JSON manifest matching [references/manifest-schema.md](references/manifest-schema.md).
   - Run `python scripts/render_preview.py path/to/manifest.json`.
   - The script emits `preview.html` next to the manifest unless `--output` is provided.

6. **QA the result.**
   - Open the HTML locally and verify both desktop and mobile views.
   - **Visual consistency check**: Does the product look the same across all images? Same color, same proportions, same lighting angle?
   - Confirm the first gallery image is the pure-white main image.
   - Confirm all thumbnails switch correctly and all A+ banners load.
   - Remove any copy that looks like an unsupported medical, safety, or performance claim.
   - Compare against the reference photos — if the generated product doesn't match the real one, regenerate.

## Rules

- **NEVER generate images without referencing the user's original product photos.** This is the #1 failure mode.
- Do not invent product facts to make the design look better.
- Do not claim certifications, material specs, percentages, or compatibility coverage unless sourced.
- Amazon main image compliance: pure white background, product-only, no badges, no text overlays.
- Maintain visual consistency: same product geometry, lighting direction, accent colors, and copy tone across all images.
- Use the **"2-4 word benefit label" rule** — never put paragraphs on images.
- If the ASIN page cannot be accessed, fall back to user-provided facts and visible packaging text, then say that the output is based on fallback inputs.

## Output Contract

Produce these artifacts in the working folder for each product:

- Generated images named by slot: `00_Main_White_BG.png` through `06_Package_Contents.png`
- A+ banners named: `A+_01_Brand_Banner.png` through `A+_07_Box_And_Guarantee.png`
- `manifest.json` matching the schema reference
- `preview.html` rendered by `scripts/render_preview.py`
- Optional review screenshots for desktop and mobile

## Resource Map

- Slot definitions, prompt scaffolding, and Best Seller design patterns:
  [references/shot-plan.md](references/shot-plan.md)
- Manifest structure and example JSON:
  [references/manifest-schema.md](references/manifest-schema.md)
- Deterministic preview renderer:
  [scripts/render_preview.py](scripts/render_preview.py)
- HTML template used by the renderer:
  [assets/preview-template.html](assets/preview-template.html)
