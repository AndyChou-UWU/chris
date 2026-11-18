# 陳威倫 1 號｜學生代表候選人

以 Flet 製作的繁體中文競選介紹頁，並整合使用 `@mlc-ai/web-llm` 的瀏覽器端 AI 政見小幫手。
WebLLM 聊天介面使用原生 HTML、CSS、JavaScript 與 Vite 建置，透過 WebGPU 在訪客的瀏覽器本機推論。

候選人影片中提到的三項政見：

- 健康水果點心
- 購買文具或書籍贈送 200 點購物點數
- 增加戶外課程

## 環境需求

- Python 與專案虛擬環境
- Node.js 22.12 以上版本
- 支援 WebGPU 的新版 Chrome 或 Edge，以及相容的 GPU
- 首次下載模型時需要網路

## 建置與啟動

在此資料夾開啟 PowerShell，先安裝前端套件並建置 WebLLM 頁面：

```powershell
& npm.cmd install
& npm.cmd run build
```

接著啟動 Flet 網站：

```powershell
py -m venv .venv # 僅在尚未建立 .venv 時執行
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

網站首頁的「開啟瀏覽器 AI 聊天」按鈕會連至 `assets/webllm` 建置出的頁面。也可以在開發時執行 `& npm.cmd run dev`，直接預覽 WebLLM 聊天介面。

## WebLLM 模型與資料

預設模型為 `Qwen2.5-1.5B-Instruct-q4f16_1-MLC`。第一次載入會從模型來源下載約 1–2 GB 的模型檔，頁面會顯示載入進度；WebLLM 會快取模型，以便之後重用。聊天推論在瀏覽器端 WebGPU 執行，不會送到 Ollama 或其他推論 API。

使用者的對話僅保留在目前頁面的記憶體中；重新載入頁面會清除對話。模型檔的首次下載仍需要網路。瀏覽器若不支援 WebGPU，頁面會提示訪客更換支援的瀏覽器或裝置。

## 專案結構

```text
網頁/
├── main.py                 # Flet 候選人介紹頁
├── assets/
│   ├── campaign.mp4        # 競選影片
│   ├── candidate.jpg       # 候選人圖片
│   └── webllm/             # Vite 建置產物，由 Flet 網站提供
├── webllm/
│   ├── index.html
│   └── src/
│       ├── main.js         # WebGPU 檢查、進度、串流對話與多輪上下文
│       ├── style.css
│       └── worker.js       # WebLLM Web Worker
├── package.json
├── vite.config.js
└── requirements.txt
```
