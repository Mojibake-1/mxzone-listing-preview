# Shot Plan — Best Seller Tier

This shot plan is derived from studying 10+ Amazon Best Seller listings from Anker, LEVOIT, Tineco, Dyson, Shark, eufy, and Roborock. Every slot has a specific conversion purpose.

## Required Inputs

- ASIN or product title
- Marketplace / storefront
- **Real product photos** (the visual anchor — this is non-negotiable)
- Verified product facts

## The Golden Rule

> **Every generated image MUST visually match the user's reference photos.**
> Pass the user's photos as `ImagePaths` to the image generation tool for EVERY call.
> The product's color, texture, shape, and proportions must be identical across all slots.

## Gallery Slots (7-Slot Conversion Funnel)

### 1. `00_Main_White_BG.png` — THE ANCHOR
**Objective**: Compliant main image that establishes the product's visual identity.
**Composition**:
- Product on pure white (#FFFFFF) background
- 15° angled view to show depth and profile (NOT flat-on — learned from Anker/Dyson)
- Photorealistic with soft contact shadow
- Show ALL items in the pack (e.g., 2 rollers + 2 filters + 1 brush tool)
- NO text, NO badges, NO logos, NO borders
- Product fills 85% of the frame
**Reference adherence**: Must match the exact color, texture, and shape of the user's photos.

### 2. `01_Hero_Core_Benefit.png` — DESIRE
**Objective**: First persuasive graphic showing the strongest verified benefit.
**Best Seller patterns observed**:
- Anker: "Perfect for MacBook M4 & New iPhone" + product in use context + spec callout (70W / 35min)
- LEVOIT: "5x Longer Lifespan, More Cost-Effective" + genuine vs generic comparison
- Tineco: "Vacuum & wash all at once" + 6 types of mess being cleaned
**Composition**:
- Product render + bold 2-4 word benefit headline
- 1 key spec number in large font (e.g., "2-Pack", "HEPA Filtration", "5x Lifespan")
- Subtle gradient or lifestyle background (NOT plain white)
- Brand accent color used for headline
**Text overlay rule**: MAX 8 words total. Title (3-4 words bold) + subtitle (4 words regular).

### 3. `02_Use_Care_Process.png` — PROOF
**Objective**: Show usage flow, installation, wash/replace, or care workflow.
**Best Seller patterns observed**:
- Tineco: 3-step self-cleaning cycle with numbered steps
- LEVOIT: Side-by-side genuine vs generic filter with lifespan callout
- Shark: Anti-tangle brush close-up during use
**Composition**:
- 2-3 step sequence layout (Step 1 → Step 2 → Result)
- Real product appearance in each step — same colors and textures
- Numbered circles or arrow flow indicators
- Minimal text: step labels only (e.g., "Remove", "Rinse", "Air Dry")

### 4. `03_Compatibility_Or_Specs.png` — DIFFERENTIATION
**Objective**: Model fit chart, compatibility confirmation, or technical spec comparison.
**Best Seller patterns observed**:
- Dyson: Official "fits these models" with product image + model list
- LEVOIT: "100% Genuine" seal with cross-section showing 3-layer filtration
- Roborock: Suction power comparison with large numbers (8000Pa)
**Composition**:
- Clean "check your model" layout with specific model names/numbers
- OR side-by-side "This product vs. Others" comparison
- Use icons (✓/✗) for compatibility, NOT dense text
- Product render must match the reference photos

### 5. `04_Lifestyle_Proof.png` — CONTEXT
**Objective**: Product in a believable, aspirational home environment.
**Best Seller patterns observed**:
- Tineco: Product cleaning hardwood floors in a modern kitchen with labeled mess types
- Shark: Vacuum in a bright, open living room
- Roborock: Robot navigating furniture with smart obstacle avoidance
**Composition**:
- High-end, clean environment matching the product category
- Product is the hero of the scene — prominent, in-use
- Warm, natural lighting — NOT stock-photo sterile
- NO text overlays on lifestyle shots (let the image speak)

### 6. `05_Materials_Or_Tech.png` — DETAIL
**Objective**: Cross-section, exploded view, material close-up, or engineering detail.
**Best Seller patterns observed**:
- LEVOIT: 3-layer filter cross-section (Pre-filter → HEPA → Carbon)
- Anker: GaN chip internal view showing size advantage
- Roborock: Anti-tangle brush mechanism close-up
**Composition**:
- Macro close-up of the key material or technology
- Floating callout lines pointing to specific components
- 2-3 word labels for each component (e.g., "Dense Microfiber", "HEPA Layer", "ABS Housing")
- Semi-transparent background or gradient to highlight the product

### 7. `06_Package_Contents.png` — CONFIDENCE
**Objective**: What's in the box — the "unboxing verification" shot.
**Best Seller patterns observed**:
- eufy: Top-down flat-lay of all components with count labels
- Shark: Organized grid with accessory names
- Tineco: Everything laid out with quantity numbers
**Composition**:
- Top-down flat-lay arrangement on neutral background
- Each item labeled with name and quantity (e.g., "×2 Roller Brush", "×2 HEPA Filter", "×1 Cleaning Tool")
- Clean, organized grid layout — NOT scattered
- All items must match the reference photos

## A+ Slots (7-Banner Brand Experience)

### 1. `A+_01_Brand_Banner.png`
**Goal**: Full-width cinematic hero — sell the "dream", not specs.
**Pattern**: Tineco uses sweeping hardwood floor + product silhouette; Roborock uses dark premium tech aesthetic.
**Composition**: Wide panoramic lifestyle + brand name + 1-line tagline.

### 2. `A+_02_Perfect_Fit.png`
**Goal**: Compatibility or fit explanation with visual proof.
**Pattern**: LEVOIT "100% Genuine" seal; Dyson "designed for V7/V8" with product fit.
**Composition**: Product + host device together, showing physical fit. Model list below.

### 3. `A+_03_Feature_Deep_Dive.png`
**Goal**: The main technology or product advantage — the ONE thing that makes this better.
**Pattern**: Tineco "iLoop Smart Sensor" with red→blue transition; Roborock "8000Pa HyperForce Suction" with large number.
**Composition**: Product hero shot + 1 large benefit number/word + supporting visual proof.

### 4. `A+_04_How_To_Use.png`
**Goal**: Install / use / maintain flow — remove buyer anxiety.
**Pattern**: Step-by-step with numbered circles.
**Composition**: 3-4 step horizontal sequence, each step with a photo and 2-word label.

### 5. `A+_05_Durability_Or_Reuse.png`
**Goal**: Material quality, longevity, or washable/reusable story.
**Pattern**: LEVOIT "5x Longer Lifespan" comparison; Tineco "Self-Cleaning System" feature callout.
**Composition**: Before/after or comparison layout showing durability advantage.

### 6. `A+_06_Lifestyle_Value.png`
**Goal**: Emotional home outcome — family, pets, clean floors.
**Pattern**: Tineco 4-grid ("Cordless & Long Runtime", "Bigger Tanks", "Lightweight", "Water Recovery Rate Over 90%").
**Composition**: 4-grid layout with lifestyle photos + 2-3 word headline + 1-line supporting text each.

### 7. `A+_07_Box_And_Guarantee.png`
**Goal**: Package contents visual + service promise + closing CTA.
**Pattern**: eufy/Shark clean flat-lay with "30-Day Guarantee" badge.
**Composition**: Flat-lay of all items + satisfaction/warranty badge + "Questions? Contact us" CTA.

## 6-Block Prompt Structure (For Each Image)

When generating each image, build the prompt in this precise order:

### Block 1: Product Fact Anchor
```
Product: [exact description from reference photos]
Appearance: [color, texture, shape, dimensions from the reference photos]
Components: [list what's visible]
```

### Block 2: Visual Reference Anchor
```
CRITICAL: This image must visually match the attached reference photos.
Preserve the exact: silhouette, connector geometry, surface finish (e.g., fuzzy grey/white microfiber
with dark speckles), housing color (dark grey ABS plastic), brand markings, and proportions.
```

### Block 3: Slot Objective
```
This is [Slot Name]. The purpose is to [conversion goal].
The viewer should feel [desired emotion/action].
```

### Block 4: Composition Instructions
```
Camera angle: [specific angle]
Crop: [framing]
Background: [specific BG]
Lighting: [direction, temperature]
Text zones: [placement and content — MAX 8 words]
```

### Block 5: Copy Guardrails
```
Approved claims: [only verified facts]
Banned claims: [anything unverified]
Text overlay limit: [2-4 word headlines only]
```

### Block 6: Output Specs
```
Filename: [exact filename]
Aspect ratio: [1:1 for gallery, 970×600 for A+]
Compliance: [main image = pure white, no text; others = minimal text]
```

## Claim Safety

- Do not state filtration percentages, health outcomes, or certifications unless verified.
- Do not claim compatibility with model families unless the ASIN page or packaging confirms them.
- Do not show accessories or quantity that are not in the box.
- If the raw photos reveal a physical limitation, preserve it instead of beautifying it away.
- Use "Compatible with" instead of "Designed for" unless the product is genuine OEM.
