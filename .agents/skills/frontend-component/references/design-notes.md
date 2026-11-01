# Design Principles

This skill is built around a few practical observations from real frontend work with coding agents:

1. Models default to safe, interchangeable layouts when constraints are weak.
2. Explicit type scale and spacing rhythm reduce that tendency more effectively than a long list of “don’ts”.
3. Canvas and animation effects are frequently left running; requiring cleanup is low-cost and high-value.
4. Asking the model to report the decisions it made (type scale, spacing base) makes later edits easier.

## When the skill helps most

- Magazine-style or editorial landing sections
- Hero areas with strong typography
- Pages that should feel designed rather than assembled from common component patterns
- Tasks where you want the model to avoid adding unrequested libraries or decorative defaults

## When to write a longer prompt anyway

The skill sets structural and quality rules. The prompt should still carry:

- The actual copy (especially if it must be in a specific language)
- Required sections (nav, hero split, footer, CTA)
- Visual temperature (warm vs cool) and any named effects
- Exact constraints such as “no GSAP” or “use canvas particles”

A short prompt plus this skill can still produce a complete page. A detailed prompt usually produces a page closer to what you intended.

## Related write-up

See the comparison of a short prompt vs a detailed prompt using this skill:

https://leosplain.com/codex-skill-prompt-vs-no-prompt-frontend/
