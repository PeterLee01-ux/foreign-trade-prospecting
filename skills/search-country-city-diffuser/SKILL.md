---
name: search-country-city-diffuser
description: Find and organize lawful B2B prospects for scent diffusers, aromatherapy diffusers, fragrance products, and adjacent commercial scenting use cases by country, city, population band, street cluster, and target industry. Use when Codex is asked to change the target country or city, search diffuser-related companies, collect public websites/emails/phones, remove generic contacts and public-service numbers, deduplicate records, or export a country/city prospect list to JSON, CSV, and Excel.
---

# Search Country City Diffuser

Build reproducible country- and city-level prospect lists for diffuser and commercial scenting outreach.

## Workflow

1. Confirm or infer:
   - ISO 3166-1 alpha-2 country code.
   - Population range; default to 10,000–250,000.
   - Explicit large-city exceptions such as Dubai.
   - Country calling code and public-service/toll-free prefixes.
   - Overture Maps release.
2. Read [methodology.md](references/methodology.md) before changing keywords, industries, contact filters, city matching, or completeness claims.
3. Check the current Overture release and country telephone rules using authoritative sources. Do not silently reuse another country's prefixes.
4. Install dependencies:

   ```bash
   python -m pip install -r scripts/requirements.txt
   ```

5. Run the collector. Repeat `--include-city` and `--public-prefix` as needed:

   ```bash
   python scripts/search_diffuser_leads.py \
     --country AE \
     --country-name "United Arab Emirates" \
     --dial-code 971 \
     --public-prefix 800 --public-prefix 400 --public-prefix 600 \
     --include-city Dubai \
     --release 2026-06-17.0 \
     --output-dir outputs/uae-diffuser
   ```

6. Inspect `quality_report.json`. Require zero duplicate IDs, duplicate business keys, generic emails, public-service numbers, missing required fields, and non-exception cities outside the population range.
7. Render or open the Excel workbook and visually inspect every worksheet before delivery.
8. State the source release, collection date, record count, exceptions, filters, and limitations in the handoff.

## Non-negotiable rules

- Use only lawfully accessible public or licensed data.
- Treat public-source and syntax checks as `not SMTP verified`.
- Do not send messages, test mailboxes, or perform SMTP probing without separate authorization and a lawful basis.
- Exclude generic role accounts and country-specific public-service/toll-free numbers.
- Match a named locality only by GeoNames name/alias. Use nearest-city matching only when locality is blank.
- Deduplicate by source record ID and normalized company + city + region.
- Never describe the result as a national business registry or every company in the country. Say “all records matching the stated filters in the cited source release.”
- Honor opt-outs and applicable privacy, electronic marketing, platform, and data-license rules.

## Outputs

The script produces:

- `qualified_leads.json`
- `qualified_leads.csv`
- `quality_report.json`
- `country_city_diffuser_leads.xlsx`

The workbook contains project notes, lead details, city/street clusters, industry/region statistics, and rules.

## Self-test

Run before first use or after modifying the script:

```bash
python scripts/search_diffuser_leads.py --self-test
```
