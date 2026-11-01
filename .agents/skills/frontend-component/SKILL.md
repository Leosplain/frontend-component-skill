---
name: frontend-component
description: Build a frontend section that looks deliberately designed. Prioritize type contrast, spacing rhythm, and restrained motion over decorative defaults. Use when the user wants a new page or component that should not feel generated.
---

# Frontend Component

## Done criteria
- Use the project's existing framework, language, file naming, and component conventions. Place new files alongside similar components; use clear English PascalCase component names where that convention applies
- In TypeScript projects, type all props using the project's interface or type alias convention; do not introduce implicit any. Do not add TypeScript or JSX to projects that do not use them
- Typography is decided first:
  - One dominant size for the primary text, with clear secondary and tertiary levels
  - Tracking and line-height are adjusted to the actual content length, not left at framework defaults
  - Max-width is set in ch or a fixed measure so lines do not run too long
- Spacing follows a single rhythm (for example 8px or 12px base). Gaps between major blocks are larger than gaps inside a block
- Motion is optional and limited:
  - Only one primary entrance or loop unless the request names more
  - Canvas or particle effects must be cleaned up on unmount
  - No simultaneous fade + slide + scale on the same element
- Accessibility:
  - Semantic tags (section, article, h1–h3)
  - Decorative layers (canvas, absolute backgrounds) carry aria-hidden="true"
  - Interactive elements have visible focus styles
- Reuse libraries already available in the project. Add a new dependency only when the user explicitly requests or authorizes it
- Avoid outputs that look interchangeable with other generated pages:
  - Do not center every block by default
  - Do not apply the same border-radius and shadow to every container
  - Add gradients or soft glows only when the user asks for those effects or they are part of the project's established design system. A specified palette alone does not authorize these effects
  - Do not add decorative icons or shapes that carry no information
- At the end of each new component file, add a 3–5 line usage comment using valid comment syntax for that file type. When editing an existing component, update its existing usage comment or include the usage note in the reply if file comments conflict with project conventions
- In the reply, state the type scale and spacing base you chose

## Steps
1. Extract from the request: visual intent, required content, and any named libraries or file path. Check the project's framework, language, dependencies, and component conventions
2. Choose a type scale and spacing base before writing the component or markup
3. Build the structure with semantic elements and the decided type styles
4. Add only the motion or canvas effect that was asked for; write the cleanup
5. Verify any new dependencies were authorized and decorative effects follow the request or the established design system
6. Add or update the usage comment, or provide the usage note in the reply as described above
7. In the final message, note the type scale, spacing base, and any assumption

## Output
- File path
- Type scale and spacing base used
- Assumptions
- One-line summary of any new dependencies and decorative effects added, or confirmation that none were added
