---
name: comtrade-fragrance-query
description: Query UN Comtrade fragrance equipment, commercial scent machines, perfumes, room-fragrance refills, industrial fragrance compounds, and related trade data from only a country name, then deliver a structured Excel workbook. Use when the user says ComTrade_skills, asks to query a country's fragrance trade, or wants country-level fragrance industry customs data without reporter codes or HS codes.
---

# ComTrade fragrance query

## Workflow

1. Accept one required input: country name in Chinese or English, or ISO2/ISO3 code.
2. Do not ask for reporter code, HS code, period, or flow unless the user explicitly wants overrides.
3. Require `COMTRADE_API_KEY` in the environment. Never print it, store it in a workbook, or place it in a URL.
4. Run:

```powershell
python scripts/query_fragrance_trade.py "<country>" --output-dir "<workspace>/work/comtrade_<safe_country>"
```

5. Read `manifest.json`, `trade_data.csv`, `query_log.csv`, and [references/codebook.md](references/codebook.md).
6. Use the `spreadsheets` skill to create one `.xlsx` in the active task's `outputs/` directory with sheets for summary, trade data, HS scope, and query log.
7. Add `usd_per_kg = primaryValue / netWgt`, blank when weight is missing or zero.
8. Cite official source URLs inside the workbook. Render and verify every sheet before export.

## Fixed defaults

- Query the five most recently completed calendar years.
- Query both imports (`M`) and exports (`X`).
- Use partner `0` (World).
- Query each HS6 separately for an auditable product boundary.
- Include all fixed codes in the codebook even when some return no rows.
- Treat equipment results as a broad market proxy because headings contain non-fragrance machinery.

## Overrides

Only when explicitly requested, pass:

```powershell
python scripts/query_fragrance_trade.py "France" --years 2022,2023,2024 --flows M --partner 156 --output-dir "..."
```

## Failure handling

- If the country is ambiguous, show the closest reporter candidates and ask for one choice.
- If the key is missing, ask the user to set `COMTRADE_API_KEY`; never request it in chat.
- On `401`, report invalid/revoked key. On `403`, report permission. On `429`, retry with exponential backoff.
- Keep successful partial results and disclose failures in the query log.

## Classification warning

Use this workflow for market research, not binding customs classification. Actual codes depend on product construction and importing-country tariff extensions.
