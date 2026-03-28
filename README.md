## 進行状態

現在3段階で実装中。

1. mistral-ocrでmd化
2. mdを成形 `./cleanup_ocr.py`
3. llmで文脈を通して処理

汎用化への道

- gemini
  並列に処理させるために、tmuxで管理？
- scriptの合成
  変換 → 成形を行う
- llmで校正させると余計なものが挟まる可能性？
  pdf → script → md → script → md-v1 → gemini → improve script　
  このように決定論的な修正スクリプトを既存のものと新たにllmによって発見されたものに分けることによって
