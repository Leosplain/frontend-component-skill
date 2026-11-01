# Prompt examples / 提示詞範例

These are prompts to try, not screenshots or measured results. Replace paths and content with your project's actual values. The skill's [core instructions](../.agents/skills/frontend-component/SKILL.md) remain the source of truth.

以下是可嘗試的提示詞，不是成果截圖或測試數據。請依專案替換路徑與文案；規則以 [Skill 原文](../.agents/skills/frontend-component/SKILL.md)為準。

## 1. Explore a direction / 探索方向

The original short prompt leaves copy, structure, and many implementation choices open:

原始短提示詞將文案、結構及較多實作決策交給代理：

```text
$frontend-component
幫我做一個雜誌風的大字首頁，背景要像星空。
```

## 2. Control the layout / 控制版面

The original detailed prompt adds sections, alignment, and a specific effect:

原始詳細提示詞補上區塊、對齊方式與明確效果：

```text
$frontend-component
請做一個雜誌風格的全螢幕首頁，但必須像可實際使用的網頁。

- 頂部導覽列
- 左側超大中文主標題
- 右側說明文字 + 細線按鈕
- 底部資訊列
- 深色溫馨夜空 + canvas 動態粒子星星
- 不要全部居中
- 不需要 GSAP
```

For a project task, also add the actual text, destination path, and existing framework. If you request animation, specify a reduced-motion fallback and confirm that effects are cleaned up when the component unmounts.

實際專案請再補上文案、目的路徑與既有框架。有動效時，可明確要求降低動態效果偏好的替代呈現，並確認元件卸載時會清除效果。

## 3. A bounded implementation / 明確的實作範圍

```text
$frontend-component
Create src/components/JournalHero.tsx using the project's existing React,
TypeScript and styling conventions.

Headline: “Ideas after dark.”
Description: “A journal for curious minds.”
CTA: “Read the journal”, linking to /journal.

Use an editorial layout: oversized left-aligned headline, supporting copy
on the right, top navigation and a compact information bar at the bottom.
Use a warm dark palette, fine rules and no gradients. No animation.
Keep the reading order clear on narrow screens. Include visible focus styles.
Do not add dependencies. Report the chosen type scale and spacing base.
```

## Review the result / 檢查結果

Use the skill's done criteria as a review aid: check type hierarchy, spacing rhythm, semantic structure, focus styles, effect cleanup when applicable, and the usage comment. Also inspect mobile widths and verify that links and buttons work in the real application.

依照 Skill 的完成條件檢查字型層級、間距節奏、語意結構、焦點樣式、適用時的效果清理，以及使用註解；也應檢查手機寬度與實際應用中的連結、按鈕功能。
