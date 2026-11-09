# Mascot Pose Library — Register 2

Final style locked 2026-09-26: **vintage retro screen-print** — thick navy-blue
(`#1B3A6B`-ish, sample the actual files rather than trust this hex) ink
outline, cream/off-white flat fill, navy halftone dot-pattern shading on one
side, distressed grain texture, solid navy lightning-bolt steam, bold navy
"THE POWER COFFEE" wordmark, **no face** (matches the reference exactly — no
eyes, no mouth). This replaced an earlier flat-vector-with-face draft after
Leo's direct correction with a reference image; that draft is in
`_flat_v1_archive/`, kept for history only, not for use.

**Generation notes for next time:**
- Made with Higgsfield `gpt_image_2_5`, `image_references` role, two inputs:
  the style reference poster + the real flat logo (`high_energy_guy.png`) for
  proportions/wordmark fidelity. Editing a real reference beats blind
  text-to-image for keeping the wordmark and proportions exact.
- **The model bakes a soft glow/halo into "transparent background" requests**
  when the reference has a dark background — confirmed by direct pixel
  sampling: alpha=0 pixels still carried non-zero navy RGB, plus a ~150-200px
  low-alpha gradient band around the character. Explicit "no glow/no halo/no
  gradient, hard die-cut edges" prompting reduced it but did not eliminate
  it. **Fix: threshold the alpha channel after generation** (anything below
  ~60 → 0, above ~200 → 255, zero the RGB wherever alpha hits 0) — see the
  one-off script used this session; worth turning into a small reusable
  script if this style gets used often. Always test-composite onto a light
  background before calling a "transparent" asset done — the halo was
  invisible on black and obvious on cream.
- All 5 share one face treatment (none) and one shading direction (halftone
  on the left third) — check both before accepting a new pose into this set.

| File | Pose | Suggested use |
|---|---|---|
| `pose_fistpump.png` | Both hands up, triumphant | Win/success moments — order confirmation, streak callouts |
| `pose_skeptical.png` | Hands on hips, head tilted | Reels calling out excuses, myth-busting hooks |
| `pose_pointing.png` | Pointing forward, mid-stride | PDP guarantee callout, discount code signature |
| `pose_armscrossed.png` | Arms crossed, standing tall | Confidence/authority beats, comparison graphics |
| `pose_shouting.png` | Cupped hand, calling out | Announcements, launches, restock moments |

Use the flat logo (`high_energy_guy.png` / `high_energy_guy_whitecolor.png`)
for tiny placements (packaging sticker, favicon-scale) where fine halftone
texture wouldn't survive the size. Use these poses for anything where the
retro poster look is the point but a full illustrated poster isn't worth
building from scratch each time.

**Cutout versions (2026-09-27):** `pose_pointing_cutout.png` and
`pose_armscrossed_cutout.png` are the same art, bbox-trimmed to the actual
character (no dead transparent padding — the source files are 2048x2048
canvases with the character only filling ~1320x1891 of that). Re-verified
alpha-clean first (no halo, confirmed via pixel sampling — see fix notes
above, already applied to the full set before this). Made for the "Fuel
Check" carousel format so the mascot drops onto a photo background at a
predictable size without runtime cropping. Trim the other three poses the
same way if they get reused over a photo.
