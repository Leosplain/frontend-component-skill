# Contributing

Focused documentation fixes, clearer examples, and reproducible issue reports are welcome. English and Traditional Chinese are both welcome in issues and pull requests.

## Scope

This repository packages an instruction-only frontend skill. Keep changes small and relevant to installation, usage, documentation, or repository maintenance. Keep the English and Traditional Chinese READMEs aligned.

For changes to `.agents/skills/frontend-component/SKILL.md`, explain the rule being changed and the use case it addresses. Keep related documentation aligned. After reviewing the instruction changes, update `scripts/skill.sha256` to record the new file bytes; include both changes in the same pull request.

## Before opening a pull request

1. Explain the problem and the resulting behavior or documentation improvement.
2. Check that examples use real project constraints without presenting invented results as evidence.
3. Run `python3 scripts/validate.py` with Python 3.9 or newer.
4. Preview changed Markdown on GitHub and check tables, code blocks, and language links.
5. If installation instructions changed, try them in a disposable project and confirm that existing installations are not overwritten.

No package installation is needed for repository checks. GitHub Actions runs the same validator for pushes and pull requests. Validation covers file presence, local Markdown link targets, and the recorded skill checksum; generated UI still requires manual review.

## Reporting an issue

Include the Codex interface and version if available, installation scope, expected behavior, actual behavior, and the smallest relevant prompt or reproduction steps. Remove private project content before attaching examples. For layout issues, include the target framework and viewport dimensions.

## 繁體中文摘要

歡迎提交文件修正、提示詞範例與可重現的問題回報；Issue 與 PR 可使用中文或英文。請同步維護雙語 README，並執行 `python3 scripts/validate.py`。

修改 `SKILL.md` 時，請說明調整的規則與使用情境，並同步相關文件。檢查指示內容後，更新 `scripts/skill.sha256`，與內容修改一起提交。安裝指令若有修改，請在暫存專案驗證；介面產出仍需人工檢查。
