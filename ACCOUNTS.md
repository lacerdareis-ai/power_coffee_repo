# The Power Coffee — Publishing Accounts

All platforms the Sales Motor posts to daily (except email, which is weekly on Mondays).

---

## Social Media

| Platform | Account | URL | Status |
|----------|---------|-----|--------|
| Instagram | @powercoffee.ofc | https://instagram.com/powercoffee.ofc | ✅ Active |
| X (Twitter) | @boosteddays | https://x.com/boosteddays | ✅ Active |
| LinkedIn | Leo Lacerda (@leolacerdaofc) | https://www.linkedin.com/in/leolacerdaofc/ | ✅ Active |
| Telegram | Better Days Power Coffee | https://t.me/betterdayspowercoffee | ✅ Active |

## Store & Blog

| Platform | Account | URL | Status |
|----------|---------|-----|--------|
| Shopify Blog | thepowercoffee.com | https://thepowercoffee.com/blogs | ✅ Active |
| Amazon | Power Coffee listing | https://a.co/d/09Gmr1Sq | ✅ Active |

## Email

| Type | Address | Frequency |
|------|---------|-----------|
| Newsletter (outbound) | email_list.txt (~343 contacts) | Every Monday |
| Daily report (internal) | lacerdareis@gmail.com | Every day 8am |

---

## ❓ One Thing Left — LinkedIn Person URN

Profile URL is set. The API also needs your internal LinkedIn person ID (`urn:li:person:XXXXXX`).

Once `LINKEDIN_ACCESS_TOKEN` is in `.env`, run this to fetch it automatically:
```bash
cd /Users/lacerdareis/power_coffee_bot/sales_motor
python3 -c "
from dotenv import load_dotenv; from pathlib import Path; import os, requests
load_dotenv(Path('.env'))
r = requests.get('https://api.linkedin.com/v2/me', headers={'Authorization': f'Bearer {os.environ[\"LINKEDIN_ACCESS_TOKEN\"]}'})
print(r.json().get('id'))
"
```
Then update `.env`:
```
LINKEDIN_PERSON_URN=urn:li:person:RESULT_FROM_ABOVE
```

---

*Last updated: May 10, 2026*
