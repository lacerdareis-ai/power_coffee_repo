# Archived month folders

Content months older than the live working window. Moved here 2026-08-15.

**Why it is safe to move these:** nothing in the pipeline scans `*_content`
directories. Every script resolves a folder from a date
(`d.strftime("%b%Y").lower() + "_content"`), so only the current and upcoming
days are ever touched. Analytics looks back 30 days through the Shopify API,
not the filesystem.

**Already-published content is unaffected.** Instagram/Meta fetch images through
SHA-pinned jsDelivr URLs, which resolve against a specific commit and are
immutable — moving a file today cannot break a post from June.

**To restore a month:** move the folder back up one level. That is all; no code
changes are required.

| Folder | Archived | Note |
|---|---|---|
| `may2026_content` | 2026-08-15 | 289M |
| `jun2026_content` | 2026-08-15 | 1.6G — holds the oversized source videos |
