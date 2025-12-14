# Building the Addon

## Quick Build

To create an installable `.ankiaddon` file:

```bash
python3 build_addon.py
```

This will create a timestamped file like `backfill-anki-yomitan_20251214_122907.ankiaddon`

## Installing the Addon

1. Open Anki
2. Go to **Tools → Add-ons**
3. Click **"Install from file..."**
4. Select the generated `.ankiaddon` file
5. Restart Anki