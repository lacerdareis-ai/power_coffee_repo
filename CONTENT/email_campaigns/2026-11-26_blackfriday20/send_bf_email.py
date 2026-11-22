#!/usr/bin/env python3
"""Send the Black Friday 2026 PT-BR email (BLACKFRIDAY20) as one Resend broadcast.

    python3 send_bf_email.py --dry-run   # build everything, check images load, send nothing
    python3 send_bf_email.py             # send (only if email_override.json has "_code_confirmed": true)

It sends to the same Resend newsletter segment as the Saturday newsletter, with the same
offer_email.py template. It never sends twice: the broadcast ID is saved in sent.json next to this file.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
BOT = Path.home() / "power_coffee_bot/sales_motor"
sys.path.insert(0, str(BOT))
from dotenv import load_dotenv  # noqa: E402

load_dotenv(BOT / ".env")
import offer_email  # noqa: E402
import resend_broadcast as rb  # noqa: E402

DRY = "--dry-run" in sys.argv
SENT = HERE / "sent.json"
REPO = os.environ.get("GITHUB_REPO", "lacerdareis-ai/power_coffee_repo")


def cdn_url(name: str) -> str:
    f = HERE / name
    root = Path(subprocess.check_output(["git", "-C", str(HERE), "rev-parse", "--show-toplevel"], text=True).strip())
    sha = subprocess.check_output(["git", "-C", str(root), "log", "-1", "--format=%H", "--", str(f)], text=True).strip()
    if not sha:
        raise SystemExit(f"{name} is not committed and pushed, so it has no public URL")
    return f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/{f.relative_to(root)}"


def main():
    if SENT.exists():
        print(f"Already sent: {SENT.read_text().strip()}. Not sending again.")
        return
    cfg = json.loads((HERE / "email_override.json").read_text())
    if not DRY and cfg.get("_code_confirmed") is not True:
        print("HELD: BLACKFRIDAY20 isn't confirmed active in Shopify yet "
              "(set \"_code_confirmed\": true in email_override.json once it is). Nothing sent.")
        sys.exit(3)
    for name in cfg["images"].values():
        u = cdn_url(name)
        r = requests.get(u, timeout=30)
        if r.status_code != 200 or not r.headers.get("content-type", "").startswith("image/"):
            raise SystemExit(f"Image not loading ({r.status_code}): {u}")
    segment = os.environ.get("RESEND_NEWSLETTER_SEGMENT_ID", "").strip()
    if not segment:
        raise SystemExit("RESEND_NEWSLETTER_SEGMENT_ID missing in .env")
    postal = os.environ.get("MAILING_ADDRESS", "[SET MAILING_ADDRESS IN .env]")
    html = offer_email.build_html(cfg, cdn_url, rb.UNSUBSCRIBE_URL, postal)
    text = offer_email.build_text(cfg, rb.UNSUBSCRIBE_URL)
    if DRY:
        print(f"DRY RUN OK: '{cfg['subject']}', {len(html):,} bytes of HTML, images load, segment set. Nothing sent.")
        return
    bid = rb.send_broadcast(segment, rb._from_field(), cfg["subject"], html, text, name="Black Friday 2026 (PT)")
    SENT.write_text(json.dumps({"broadcast_id": bid}))
    print(f"SENT: Resend broadcast {bid}")


if __name__ == "__main__":
    main()
