# Installation / 安裝指南

## Choose a scope / 選擇安裝範圍

| Scope / 範圍 | Destination / 目的位置 | Use / 用途 |
| --- | --- | --- |
| Project / 專案 | `<your-project>/.agents/skills/frontend-component/` | Share the skill with that repository / 隨專案共用 |
| User / 使用者 | `~/.agents/skills/frontend-component/` | Make it available across your local projects / 供本機多個專案使用 |

The source folder in this repository is `.agents/skills/frontend-component/`. Install that folder, not the entire repository. Read its [instructions](../.agents/skills/frontend-component/SKILL.md) before installation.

來源是本儲存庫中的 `.agents/skills/frontend-component/`。請安裝這個資料夾，而非整個儲存庫；安裝前可先閱讀[指示內容](../.agents/skills/frontend-component/SKILL.md)。

## Project installation / 專案安裝

Run the following in this repository's root on macOS or Linux. Replace `/absolute/path/to/your-project` with the actual target project path. The commands stop if the target project does not exist or if the skill is already installed.

在本儲存庫根目錄執行以下 macOS / Linux 指令，先將路徑換成實際目標專案。目標專案不存在或已安裝同名 Skill 時，指令會停止。

```bash
PROJECT_DIR="/absolute/path/to/your-project"
if [ ! -d "$PROJECT_DIR" ]; then
  echo "Project directory does not exist: $PROJECT_DIR"
elif [ -e "$PROJECT_DIR/.agents/skills/frontend-component" ]; then
  echo "Skill already exists. Review the existing copy before updating."
else
  mkdir -p "$PROJECT_DIR/.agents/skills"
  cp -R .agents/skills/frontend-component "$PROJECT_DIR/.agents/skills/"
fi
```

On Windows, use File Explorer to copy the entire `frontend-component` folder to the same relative destination in your project.

Windows 使用者可透過檔案總管，將完整的 `frontend-component` 資料夾複製到專案內相同的相對位置。

## User installation / 使用者安裝

Run from this repository's root on macOS or Linux:

在本儲存庫根目錄執行（macOS / Linux）：

```bash
if [ -e "$HOME/.agents/skills/frontend-component" ]; then
  echo "Skill already exists. Review the existing copy before updating."
else
  mkdir -p "$HOME/.agents/skills"
  cp -R .agents/skills/frontend-component "$HOME/.agents/skills/"
fi
```

## Verify and invoke / 確認與呼叫

The installed folder should contain all three files:

安裝後應保留以下三個檔案：

```text
frontend-component/
├── SKILL.md
├── agents/openai.yaml
└── references/design-notes.md
```

Open the target project in Codex. In the CLI or IDE extension, mention `$frontend-component` in your prompt or select it through `/skills`. Codex detects local skill changes automatically; restart if it does not appear. Avoid installing multiple copies with the same name across scopes, since they can both appear in selectors.

在 Codex 開啟目標專案。CLI 或 IDE 擴充功能可在提示詞中輸入 `$frontend-component`，或使用 `/skills` 選取。本機變更會自動被偵測；若沒有出現，可重新啟動。請避免在不同範圍重複安裝同名 Skill，以免選單出現多個項目。

## Troubleshooting / 排查

- **Not listed:** Check the exact folder path and uppercase `SKILL.md` filename. Make sure the target project is open, then restart Codex if needed.
- **Nested folder:** `frontend-component/frontend-component/SKILL.md` is one level too deep; move the inner folder to the skill destination.
- **Different results:** Include actual copy, layout, stack, and motion requirements. Review generated output; instructions do not guarantee compliance.

- **沒有出現：** 檢查路徑與大寫的 `SKILL.md` 檔名，確認開啟的是目標專案，再視需要重新啟動 Codex。
- **多包了一層：** `frontend-component/frontend-component/SKILL.md` 過深，應將內層資料夾放到安裝位置。
- **結果不符預期：** 補充文案、版面、技術與動效需求，並人工檢查產出；指示並不保證每次完全遵循。

## Update or remove / 更新與移除

For an update, compare the installed copy with the new source, back up local edits, then replace the installed folder. To uninstall, remove only the installed `frontend-component` folder using your file manager. Leave other skills in place.

更新前請比對新舊內容並備份本機修改，再替換已安裝的資料夾。移除時，可用檔案管理員刪除已安裝的 `frontend-component` 資料夾，保留其他 Skill。

Reference: [Official OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills). These instructions describe local folder installation; this repository is not a packaged plugin.

參考：[OpenAI 官方技能文件](https://learn.chatgpt.com/docs/build-skills)。此處說明本機資料夾安裝，本儲存庫並非已封裝的 Plugin。
