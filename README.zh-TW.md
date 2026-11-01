# Frontend Component Skill

給 Codex 使用的前端 Skill，適用於網頁與元件製作。要求 Codex 在寫程式前先決定字級與間距，使用語意化 HTML，並在元件卸載時清除動畫效果。

[English](README.md) · [安裝指南](docs/installation.md) · [提示詞範例](docs/examples.md) · [貢獻指南](CONTRIBUTING.md) · [MIT 授權](LICENSE)

## 功能

| 項目 | 要求 |
| --- | --- |
| 字型 | 先決定各層級字體大小，調整字距與行高，限制文字行長。 |
| 間距 | 使用同一套間距基準，區塊之間的距離大於區塊內部。 |
| 動效 | 限制動畫數量，卸載時清除 canvas 或動畫相關工作。 |
| 可存取性 | 使用語意標籤、隱藏純裝飾層，並提供可見的焦點樣式。 |
| 實作 | 沿用專案命名與型別慣例，使用現有套件，新增依賴需經使用者同意。 |
| 輸出 | 附上簡短使用註解，說明採用的字級與間距基準。 |

元件產出後，請在實際應用中檢查手機與桌面版面，並測試鍵盤操作。

## 快速開始

1. 下載並解壓縮這個儲存庫，或使用 Git 複製。
2. 將 `.agents/skills/frontend-component/` 放進目標專案的 `.agents/skills/`。請複製**整個資料夾**，包含 `agents/` 與 `references/`。
3. 在目標專案開啟 Codex，輸入：

```text
$frontend-component
請在 src/components/EditorialHero.tsx 做一個雜誌風格的首頁主視覺。
左側放大標題，右側放說明與一個 CTA。
沿用專案現有技術，不要動畫，也不要新增函式庫。
```

Codex CLI 與 IDE 擴充功能支援用 `$frontend-component` 呼叫。本機 Skill 會自動被偵測；如果沒有出現，可重新啟動 Codex。[安裝指南](docs/installation.md) 包含終端機指令、使用者層級安裝與排查步驟；各介面的行為請參考 [官方技能文件](https://learn.chatgpt.com/docs/build-skills)。

## 提示詞範例

請寫出實際文案、版面、檔案路徑、使用的框架，以及是否需要動畫。例如：

```text
$frontend-component
沿用專案現有 React/TypeScript，製作全螢幕雜誌風格首頁。

文案：「設計筆記」／「記錄設計與日常工作的文章」／CTA：「閱讀最新一期」。
版面：頂部導覽、左側超大主標、右側說明與 CTA、底部精簡資訊列。
樣式：深棕色背景、米白色文字、細線分隔，不要漸層。
動效：不需要。不要新增依賴。
目標：src/components/JournalHero.tsx。
```

[提示詞指南](docs/examples.md) 收錄更多範例，包括原始的中文提示詞。[設計筆記](.agents/skills/frontend-component/references/design-notes.md) 說明這個 Skill 背後的考量。

## 專案結構

```text
.agents/skills/frontend-component/
├── SKILL.md                 # Skill 核心指示
├── agents/openai.yaml       # 顯示資訊與呼叫設定
└── references/design-notes.md

docs/                       # 安裝與提示詞指南
.github/                    # 協作範本與儲存庫檢查
scripts/validate.py         # 不需第三方套件的檢查程式
CONTRIBUTING.md              # 貢獻與審查說明
LICENSE                     # MIT
```

## 維護與檢查

本專案包含 Skill 指示與文件，沒有需要建置的前端應用。使用 Python 3.9 以上版本執行檢查：

```bash
python3 scripts/validate.py
```

檢查程式會確認必要檔案、Markdown 內的本機連結，以及`SKILL.md` 的校驗碼。其他檢查步驟請見[貢獻指南](CONTRIBUTING.md)。

## 延伸閱讀

作者關閉其他 Skill，分別用短提示詞與詳細提示詞測試本 Skill，記錄在[實測對照與對話範例](https://leosplain.com/codex-frontend-skill-short-vs-detailed-prompt/)。

## 授權

[MIT](LICENSE) © 2026 Leo。
