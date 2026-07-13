# Methodology and decision rules

## Sources

- Use GeoNames country dumps for populated-place names, aliases, coordinates, administrative codes, and population.
- Use Overture Maps Places for public business names, categories, addresses, websites, emails, phones, coordinates, operating status, and source IDs.
- Record exact source URLs, release identifiers, and collection dates in every output.
- Recheck current releases and schemas before a production run.

## Product keywords

Core terms:

- Scent Diffuser
- Aromatherapy Diffuser
- Ultrasonic Diffuser
- Essential Oil Diffuser
- Fragrance Diffuser

Derived terms:

- LED Light Aromatherapy
- Ceramic Fragrance Diffuser
- Ultrasonic Aroma Diffuser
- Portable Air Freshener
- Wooden Scent Dispenser

Use direct keyword matches to prioritize records, not as the only inclusion path. Many valid buyers are hotels, property managers, spas, designers, retailers, and wholesalers whose names do not contain diffuser terms.

## Priority industries

Standardize source categories into:

- Hospitality
- Hotels
- Real Estate
- Property Management
- Retail
- Luxury Goods
- Wellness
- Spa
- Interior Design
- Architecture
- Facilities Services
- Commercial Design
- Beauty
- Lifestyle
- Import/Export
- Wholesale

The bundled script queries categories that Overture currently exposes and maps them to the closest standard industry. Review the mapping when Overture changes its taxonomy.

## City selection

- Default population: 10,000–250,000.
- Add a city outside the band only when the user names it explicitly; record it as an exception.
- Resolve a nonblank locality by normalized GeoNames name or alternate name.
- If locality is blank, allow nearest eligible city within the configured distance, default 20 km.
- Do not reassign a named large city to a nearby small city.
- Use `--bbox` to override derived bounds for countries crossing the antimeridian or with unusual overseas territories.

## Contact filtering

Require a company name, street address, website, syntactically valid email, and phone.

Exclude generic or placeholder local parts such as:

`info`, `sale`, `sales`, `contact`, `hello`, `support`, `admin`, `office`, `service`, `customer.service`, `help`, `enquiry`, `inquiry`, `mail`, `marketing`, `reservations`, `booking`, `orders`, `noreply`, `none`.

Normalize the country calling code before checking public-service/toll-free prefixes. Obtain prefixes from an authoritative national numbering source. Do not assume 800/400/600 applies globally.

## Deduplication

Apply both:

1. Source ID uniqueness.
2. Unicode-normalized company + matched city + administrative code uniqueness.

Keep the higher-confidence record when input order is not already confidence-ranked.

## Validation and claims

The quality report must show:

- Total remote candidates.
- Final qualified records.
- Unique IDs and business keys.
- Duplicate counts.
- Generic-email count.
- Public-number count.
- Missing-required-field count.
- Non-exception population violations.
- Counts by city, industry, and region.

“Valid email” means public-source plus syntax filtering unless a separate authorized verifier was used. Never label it SMTP verified by implication.

Use the phrase: “all records matching the stated filters in the cited public-data release.”
