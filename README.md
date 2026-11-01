# Frontend Component Skill

A Codex skill for frontend pages and components. It asks Codex to choose type sizes and spacing before writing code, use semantic HTML, and clean up animation effects on unmount.

[繁體中文](README.zh-TW.md) · [Installation](docs/installation.md) · [Prompt examples](docs/examples.md) · [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)

## What it does

| Area | Instructions |
| --- | --- |
| Typography | Choose a type scale, adjust tracking and line height, and limit text measure. |
| Spacing | Use a consistent base rhythm and distinguish section gaps from internal gaps. |
| Motion | Keep effects restrained and clean up canvas or animation work on unmount. |
| Accessibility | Use semantic elements, hide decorative layers from assistive technology, and provide visible focus styles. |
| Implementation | Follow the project’s naming and typing conventions, reuse installed libraries, and add dependencies only when authorized. |
| Output | Include a short usage comment and report the chosen type scale and spacing base. |

After generating a component, check it in your application at mobile and desktop widths, and test keyboard navigation.

## Quick start

1. Download and extract this repository, or clone it with Git.
2. Copy `.agents/skills/frontend-component/` into your project's `.agents/skills/` directory. Copy the **whole folder**, including `agents/` and `references/`.
3. Open Codex in that project and use the skill in a prompt:

```text
$frontend-component
Build an editorial homepage hero in src/components/EditorialHero.tsx.
Use a large left-aligned headline, a right-hand description and one CTA.
Use the project's existing stack. No animation or additional libraries.
```

Codex CLI and the IDE extension support `$frontend-component` mentions. Local skills are discovered automatically; restart Codex if the skill does not appear. See the [installation guide](docs/installation.md) for shell commands, user-level installation, and troubleshooting, and the [official skills documentation](https://learn.chatgpt.com/docs/build-skills) for host-specific behavior.

## Example prompt

Include the copy, layout, target file, framework, and any animation requirements. For example:

```text
$frontend-component
Create a full-screen editorial homepage using the existing React/TypeScript stack.

Content: “Field Notes” / “Essays on design and everyday work.” / CTA: “Read the latest issue”.
Layout: top navigation, oversized headline on the left, supporting copy and CTA
on the right, and a compact information bar at the bottom.
Style: dark brown background, off-white text, thin borders, no gradients.
Motion: none. Do not add dependencies.
Target: src/components/JournalHero.tsx.
```

More examples, including the original Traditional Chinese prompts, are in the [prompt guide](docs/examples.md). See the [design notes](.agents/skills/frontend-component/references/design-notes.md) for background.

## Project structure

```text
.agents/skills/frontend-component/
├── SKILL.md                 # Core skill instructions
├── agents/openai.yaml       # Display metadata and invocation policy
└── references/design-notes.md

docs/                       # Installation and prompt guides
.github/                    # Contribution templates and repository checks
scripts/validate.py         # Dependency-free repository validation
CONTRIBUTING.md              # Contribution and review expectations
LICENSE                     # MIT
```

## Development

The repository contains skill instructions and documentation, with no frontend app to build. To run the repository checks, use Python 3.9 or newer:

```bash
python3 scripts/validate.py
```

The script checks required files, local Markdown links, and the recorded `SKILL.md` checksum. See [Contributing](CONTRIBUTING.md) for review steps.

## Further reading

The author tested this skill with short and detailed prompts, with other skills disabled. Read the [comparison and conversation examples](https://leosplain.com/codex-frontend-skill-short-vs-detailed-prompt/).

## License

[MIT](LICENSE) © 2026 Leo.
