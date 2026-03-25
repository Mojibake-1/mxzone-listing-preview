from __future__ import annotations

import argparse
import json
import html
from pathlib import Path
from typing import Any


DEFAULT_TEMPLATE_NAME = "preview-template.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render an Amazon listing preview HTML file from a manifest.json file."
    )
    parser.add_argument("manifest", help="Path to the JSON manifest.")
    parser.add_argument(
        "--template",
        help="Optional path to the HTML template. Defaults to the bundled template.",
    )
    parser.add_argument(
        "--output",
        help="Optional output HTML path. Defaults to preview.html beside the manifest.",
    )
    return parser.parse_args()


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8-sig")
    except FileNotFoundError as exc:
        raise SystemExit(f"Manifest not found: {path}") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Manifest is not valid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise SystemExit("Manifest root must be a JSON object.")
    return data


def require_field(data: dict[str, Any], field: str) -> Any:
    value = data.get(field)
    if value in (None, "", []):
        raise SystemExit(f"Manifest field '{field}' is required.")
    return value


def normalize_image_entries(
    items: Any, manifest_path: Path, output_path: Path
) -> list[dict[str, str]]:
    if not isinstance(items, list) or not items:
        raise SystemExit("Image collections must be non-empty arrays.")

    normalized: list[dict[str, str]] = []
    for index, item in enumerate(items):
        if isinstance(item, str):
            src_value = item
            label = f"Image {index + 1}"
            alt = label
        elif isinstance(item, dict):
            src_value = item.get("src")
            label = item.get("label") or f"Image {index + 1}"
            alt = item.get("alt") or label
        else:
            raise SystemExit("Each image entry must be a string or object.")

        if not src_value:
            raise SystemExit("Each image entry must include a non-empty 'src'.")

        normalized.append(
            {
                "src": make_browser_path(src_value, manifest_path, output_path),
                "label": str(label),
                "alt": str(alt),
            }
        )
    return normalized


def make_browser_path(raw_value: str, manifest_path: Path, output_path: Path) -> str:
    if raw_value.startswith(("http://", "https://", "data:")):
        return raw_value

    source_path = Path(raw_value)
    if not source_path.is_absolute():
        source_path = (manifest_path.parent / source_path).resolve()

    try:
        relative = source_path.relative_to(output_path.parent)
        return relative.as_posix()
    except ValueError:
        try:
            return source_path.relative_to(output_path.parent.resolve()).as_posix()
        except ValueError:
            try:
                return source_path.resolve().relative_to(output_path.parent.resolve()).as_posix()
            except ValueError:
                try:
                    return source_path.resolve().relative_to(output_path.parent).as_posix()
                except ValueError:
                    try:
                        return source_path.resolve().relative_to(manifest_path.parent.resolve()).as_posix()
                    except ValueError:
                        try:
                            return source_path.resolve().relative_to(manifest_path.parent).as_posix()
                        except ValueError:
                            return source_path.resolve().as_uri()


def render_breadcrumbs(breadcrumbs: Any) -> str:
    if not isinstance(breadcrumbs, list) or not breadcrumbs:
        return "<b>Product Detail</b>"

    escaped = [html.escape(str(part)) for part in breadcrumbs]
    if len(escaped) == 1:
        return f"<b>{escaped[0]}</b>"
    return " &rsaquo; ".join(escaped[:-1] + [f"<b>{escaped[-1]}</b>"])


def render_bullets(items: Any) -> str:
    if not isinstance(items, list) or not items:
        return "<li>Verified product highlights will appear here.</li>"
    return "\n".join(
        f"<li>{html.escape(str(item))}</li>" for item in items if str(item).strip()
    )


def render_thumbnails(gallery: list[dict[str, str]]) -> str:
    blocks: list[str] = []
    for index, item in enumerate(gallery):
        active_class = " active" if index == 0 else ""
        blocks.append(
            f"<div class=\"thumb{active_class}\" onclick=\"switchImage({index})\">"
            f"<img src=\"{html.escape(item['src'])}\" alt=\"{html.escape(item['alt'])}\" loading=\"lazy\">"
            "</div>"
        )
    return "\n".join(blocks)


def render_aplus(aplus_items: list[dict[str, str]]) -> str:
    return "\n".join(
        f"<img src=\"{html.escape(item['src'])}\" alt=\"{html.escape(item['alt'])}\" loading=\"lazy\">"
        for item in aplus_items
    )


def fill_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace(f"__{key}__", value)
    return rendered


def main() -> None:
    args = parse_args()
    manifest_path = Path(args.manifest).resolve()
    output_path = Path(args.output).resolve() if args.output else manifest_path.with_name("preview.html")
    template_path = (
        Path(args.template).resolve()
        if args.template
        else Path(__file__).resolve().parent.parent / "assets" / DEFAULT_TEMPLATE_NAME
    )

    data = load_manifest(manifest_path)

    gallery = normalize_image_entries(require_field(data, "gallery"), manifest_path, output_path)
    aplus_items = normalize_image_entries(require_field(data, "aplus"), manifest_path, output_path)

    brand = str(require_field(data, "brand"))
    title = str(require_field(data, "product_title"))
    marketplace_domain = str(require_field(data, "marketplace_domain"))
    marketplace_suffix = marketplace_domain.replace("amazon.", "", 1) if marketplace_domain.startswith("amazon.") else marketplace_domain

    price = str(require_field(data, "price"))
    currency_symbol = str(require_field(data, "currency_symbol"))

    rating = html.escape(str(data.get("rating", "4.6")))
    rating_count = html.escape(str(data.get("rating_count", "Customer reviews")))
    delivery_note = html.escape(str(data.get("delivery_note", "See delivery options")))
    search_query = html.escape(str(data.get("search_query", title)))
    brand_link_text = html.escape(str(data.get("brand_link_text", f"Visit the {brand} Store")))
    control_title = html.escape(str(data.get("control_title", f"{brand} Listing Preview")))
    aplus_heading = html.escape(str(data.get("aplus_heading", "Product Description")))
    aplus_label = html.escape(str(data.get("aplus_label", "From the Manufacturer - A+ Content")))

    footer_note = html.escape(
        str(data.get("footer_note", "This is a preview simulation for internal review only."))
    )
    footer_summary = html.escape(
        str(
            data.get(
                "footer_summary",
                f"Product images: {len(gallery)} gallery images + {len(aplus_items)} A+ banners",
            )
        )
    )
    footer_meta = html.escape(
        str(data.get("footer_meta", f"{brand} - {data.get('asin', 'NO-ASIN')} - {marketplace_domain}"))
    )

    try:
        template = template_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise SystemExit(f"Template not found: {template_path}") from exc

    replacements = {
        "PAGE_TITLE": html.escape(f"{brand} Listing Preview - {marketplace_domain}"),
        "CONTROL_TITLE": control_title,
        "MARKETPLACE_SUFFIX": html.escape(marketplace_suffix),
        "SEARCH_QUERY": search_query,
        "BREADCRUMBS_HTML": render_breadcrumbs(data.get("breadcrumbs")),
        "MAIN_IMAGE_SRC": html.escape(gallery[0]["src"]),
        "MAIN_IMAGE_ALT": html.escape(gallery[0]["alt"]),
        "THUMBNAILS_HTML": render_thumbnails(gallery),
        "BRAND_LINK_TEXT": brand_link_text,
        "PRODUCT_TITLE": html.escape(title),
        "RATING": rating,
        "RATING_COUNT": rating_count,
        "CURRENCY_SYMBOL": html.escape(currency_symbol),
        "PRICE": html.escape(price),
        "DELIVERY_NOTE": delivery_note,
        "BULLET_ITEMS_HTML": render_bullets(data.get("about_items")),
        "APLUS_HEADING": aplus_heading,
        "APLUS_LABEL": aplus_label,
        "APLUS_HTML": render_aplus(aplus_items),
        "FOOTER_NOTE": footer_note,
        "FOOTER_SUMMARY": footer_summary,
        "FOOTER_META": footer_meta,
        "GALLERY_DATA_JSON": json.dumps(gallery, ensure_ascii=False),
    }

    rendered = fill_template(template, replacements)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"Rendered preview: {output_path}")


if __name__ == "__main__":
    main()
