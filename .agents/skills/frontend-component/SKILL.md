---
name: frontend-component
description: Build a frontend section that looks deliberately designed. Prioritize type contrast, spacing rhythm, and restrained motion over decorative defaults. Use when the user wants a new page or component that should not feel generated.
---

# Frontend Component

Build sections and components that feel intentionally designed rather than assembled from defaults.  
Decide type scale and spacing rhythm *before* writing markup. Prefer strong hierarchy and clear structure over decoration.

## Done criteria

### Project fit
- Use the project's existing framework, language, file naming, and component conventions.
- Place new files alongside similar components. Prefer clear English PascalCase names when that is the local convention.
- In TypeScript projects, type all props using the project's interface or type-alias style. Do not introduce implicit `any`.
- Do not add TypeScript or JSX to projects that do not already use them.

### Typography (decide first)
Choose a type scale before coding. Use one of these as a starting point, then adjust:

| Scale | Ratio | Example sizes (px) | Best for |
|-------|-------|--------------------|----------|
| Compact | 1.2 | 14 / 17 / 20 / 24 / 29 | Dense UI, dashboards |
| Editorial | 1.25 | 16 / 20 / 25 / 31 / 39 / 49 | Most content sections |
| Display | 1.333 | 16 / 21 / 28 / 37 / 50 / 67 | Heroes, landing sections |

Rules:
- One clearly dominant size for the primary heading or key message.
- Distinct secondary and tertiary levels (usually 2–3 steps below).
- Adjust tracking and line-height to the actual content length (tighter for short display type, looser for body).
- Set a maximum measure (`ch` or `max-width`) so lines do not run too long (typically 60–75 characters for body text).

### Spacing rhythm
Pick a single base unit and stick to it (recommended: **8px** or **4px** for denser interfaces).

Typical scale derived from an 8px base:
- 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96

Rules:
- Gaps *between* major blocks are larger than gaps *inside* a block.
- Prefer consistent vertical rhythm over arbitrary pixel values.
- Use the same spacing language for padding, margin, and gap.

### Motion
- Motion is optional. Use only what the request asks for.
- Limit to one primary entrance or loop unless the request explicitly names more.
- Canvas, particle, or animation work must be cleaned up on unmount (cancel frames, remove listeners, disconnect observers).
- Do not combine fade + slide + scale on the same element.
- Respect `prefers-reduced-motion`: provide a reduced or static alternative when motion is present.

### Accessibility
- Use semantic elements (`section`, `article`, `nav`, `header`, `footer`, `h1`–`h3`).
- Decorative layers (absolute backgrounds, canvas, purely visual shapes) must have `aria-hidden="true"`.
- Interactive elements need visible focus styles that meet contrast requirements.
- Ensure sufficient color contrast (aim for WCAG AA: 4.5:1 for normal text, 3:1 for large text).
- Maintain logical reading order on narrow viewports.
- Provide keyboard-accessible controls; do not rely on hover alone for critical actions.

### Implementation constraints
- Reuse libraries already present in the project.
- Add a new dependency only when the user explicitly requests or authorizes it.
- Avoid interchangeable “generated” defaults:
  - Do not center every block by default.
  - Do not apply the same border-radius and shadow to every container.
  - Gradients or soft glows are allowed only when the user asks for them or they already exist in the project's design system. A color palette alone does not authorize them.
  - Do not add decorative icons or shapes that carry no information.

### Documentation
- At the end of each new component file, add a 3–5 line usage comment (valid for the file type).
- When editing an existing component, update its usage comment if one exists; otherwise include the usage note in the reply.
- In the final reply, state the type scale and spacing base you chose.

## Steps

1. Extract visual intent, required content, file path, and any named libraries from the request. Inspect the project's framework, language, dependencies, and component conventions.
2. Choose a type scale (and specific sizes) and a spacing base *before* writing markup or styles.
3. Build the structure with semantic elements and the decided type and spacing values.
4. Add only the motion or canvas effect that was requested, including cleanup and a reduced-motion path.
5. Verify that any new dependencies were authorized and that decorative effects match the request or existing design system.
6. Add or update the usage comment (or include it in the reply if file comments are disallowed).
7. In the final message, report the type scale, spacing base, key assumptions, and any new dependencies or decorative effects.

## Output

- File path
- Type scale used (name or ratio + concrete sizes)
- Spacing base used
- Assumptions made
- One-line summary of any new dependencies and decorative effects, or confirmation that none were added

## Quick reference (common pitfalls)

| Avoid | Prefer |
|-------|--------|
| Everything centered | Asymmetric or edge-aligned composition when it serves the content |
| Uniform 8px radius + soft shadow on all cards | Varied treatment; radius and shadow used sparingly and purposefully |
| Multiple competing animations | One clear motion idea, or none |
| Long unbroken lines of body text | Constrained measure + comfortable line-height |
| Decorative icons with no function | Only icons that clarify or navigate |