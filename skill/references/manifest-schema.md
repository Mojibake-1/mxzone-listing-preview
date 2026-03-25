# Manifest Schema

Write `manifest.json` beside the generated images, then run:

```bash
python scripts/render_preview.py manifest.json
```

## Required Fields

```json
{
  "asin": "B07WRQ4JFZ",
  "marketplace_domain": "amazon.co.uk",
  "brand": "MXZONE",
  "product_title": "2 Pack Premium HEPA Post-Motor Filter Compatible with Dyson V7 V8 Absolute Animal Cordless Vacuum",
  "price": "11.91",
  "currency_symbol": "\u00A3",
  "gallery": [
    { "src": "00_Main_White_BG.png", "label": "Main", "alt": "Main image" }
  ],
  "aplus": [
    { "src": "A+_01_Brand_Banner.png", "alt": "Brand banner" }
  ]
}
```

## Supported Optional Fields

- `control_title` — Preview pane heading
- `search_query` — Search bar default text
- `brand_link_text` — "Visit the X Store"
- `rating` — Star rating number (e.g. "4.8")
- `rating_count` — e.g. "25,320 ratings"
- `delivery_note` — e.g. "FREE delivery"
- `breadcrumbs` — Category path array
- `about_items` — Bullet point list
- `aplus_heading` — e.g. "Product Description"
- `aplus_label` — e.g. "From the Manufacturer - A+ Content"
- `footer_note` — Preview disclaimer
- `footer_summary` — Image count summary
- `footer_meta` — Brand/ASIN/marketplace info
- `reference_photos` — Array of original product photo paths (for audit trail)
- `brand_accent_color` — Hex color for the brand (used in A+ and infographics)
- `compatible_models` — Array of verified compatible model names

## Full Example

```json
{
  "control_title": "iFloor3 Parts Listing Preview",
  "asin": "B0XXXXXXXXX",
  "marketplace_domain": "amazon.com",
  "brand": "GenericReplacement",
  "brand_link_text": "Visit the GenericReplacement Store",
  "brand_accent_color": "#0EA5E9",
  "search_query": "Tineco iFloor 3 replacement roller brush filter",
  "product_title": "Ifloor3 Roller Brush Replacement for Tineco iFloor 3 and Floor One S3 Cordless Wet Dry Vacuum Cleaner, 2 Brush Roller, 2 HEPA Filters",
  "rating": "4.8",
  "rating_count": "342 ratings",
  "price": "19.99",
  "currency_symbol": "$",
  "delivery_note": "FREE delivery",
  "breadcrumbs": [
    "Home & Kitchen",
    "Vacuums & Floor Care",
    "Vacuum Parts & Accessories",
    "Replacement Parts"
  ],
  "about_items": [
    "PERFECT COMPATIBILITY: Designed specifically for Tineco iFloor 3 and Floor One S3 Cordless Wet Dry Vacuum Cleaners.",
    "PREMIUM QUALITY MATERIAL: High-density microfiber roller brush with strong water absorption. HEPA filter captures fine particles.",
    "WASHABLE & REUSABLE: HEPA filter is fully washable. Air dry completely before reinstalling.",
    "VALUE PACK: Includes 2 Roller Brushes, 2 HEPA Filters, and 1 Cleaning Brush tool.",
    "SAFE ON SEALED FLOORS: Perfect for hardwood, tile, marble, and laminate without scratching."
  ],
  "compatible_models": [
    "Tineco iFloor 3",
    "Tineco Floor One S3"
  ],
  "reference_photos": [
    "original_product_photo.png"
  ],
  "gallery": [
    { "src": "00_Main_White_BG.png", "label": "Main", "alt": "Product main image - all components on white BG" },
    { "src": "01_Hero_Core_Benefit.png", "label": "Hero", "alt": "Hero benefit - 2-Pack value bundle" },
    { "src": "02_Use_Care_Process.png", "label": "Care", "alt": "3-step wash and reuse process" },
    { "src": "03_Compatibility_Or_Specs.png", "label": "Fit", "alt": "Compatible model verification" },
    { "src": "04_Lifestyle_Proof.png", "label": "Lifestyle", "alt": "Product cleaning hardwood floors" },
    { "src": "05_Materials_Or_Tech.png", "label": "Materials", "alt": "Dense microfiber and HEPA detail" },
    { "src": "06_Package_Contents.png", "label": "Kit", "alt": "Full kit flat-lay with quantities" }
  ],
  "aplus_heading": "Product Description",
  "aplus_label": "From the Manufacturer - A+ Content",
  "aplus": [
    { "src": "A+_01_Brand_Banner.png", "alt": "Cinematic brand lifestyle banner" },
    { "src": "A+_02_Perfect_Fit.png", "alt": "Perfect fit compatibility proof" },
    { "src": "A+_03_Feature_Deep_Dive.png", "alt": "Core technology deep dive" },
    { "src": "A+_04_How_To_Use.png", "alt": "3-step installation guide" },
    { "src": "A+_05_Durability_Or_Reuse.png", "alt": "Washable & durable proof" },
    { "src": "A+_06_Lifestyle_Value.png", "alt": "4-grid lifestyle benefits" },
    { "src": "A+_07_Box_And_Guarantee.png", "alt": "Package contents and guarantee" }
  ],
  "footer_note": "This is a preview simulation for internal review only."
}
```

## Notes

- Relative image paths are resolved relative to the manifest file.
- Absolute local paths are converted into paths that a local browser can load.
- The renderer uses the first gallery image as the main image.
- Keep the generated images and the rendered `preview.html` in the same deliverable folder.
- `reference_photos` is for audit trail only — not shown in the preview.
- `compatible_models` populates the compatibility section if the template supports it.
- `brand_accent_color` should be a curated hex color — avoid generic primaries.
