# 🌐 AI Power Tools Explorer - Hosted Python Website

A production-ready, cloud-deployable Python website built to run directly on web hosting platforms (**Render**, **Railway**, **Vercel**, **PythonAnywhere**, **Heroku**, **Docker**, or **VPS**) without any desktop scripts or batch files.

---

## 🚀 Instant Deployment Options (No Batch Files)

### 1. Render (Recommended - Free Tier)
1. Push this repository to GitHub or GitLab.
2. Sign in to [render.com](https://render.com) and click **New Web Service**.
3. Select your repository.
4. Render automatically detects `render.yaml` or you can enter:
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn wsgi:app --bind 0.0.0.0:$PORT`
5. Click **Create Web Service**. Your website is live in seconds with HTTPS!

---

### 2. Railway
1. Go to [railway.app](https://railway.app) and create a **New Project**.
2. Select **Deploy from GitHub repo**.
3. Railway automatically reads the included `Procfile` and launches `wsgi:app`.

---

### 3. Vercel (Serverless Python)
1. Install Vercel CLI (`npm i -g vercel`) or import your repo in the Vercel dashboard.
2. The included `vercel.json` and `api/index.py` configure the serverless function automatically.
3. Run `vercel --prod` to deploy.

---

### 4. PythonAnywhere / cPanel (Shared Hosting)
1. In your **Web** tab, choose **Manual Configuration** (Python 3.12).
2. Edit the **WSGI configuration file** to point to `wsgi.py`:
   ```python
   import sys
   path = '/home/yourusername/aitoolpython'
   if path not in sys.path:
       sys.path.append(path)

   from wsgi import application
   ```
3. Click **Reload**.

---

### 5. Docker / Google Cloud Run / AWS ECS
```bash
# Build the container
docker build -t ai-tools-web .

# Run the container
docker run -p 5000:5000 ai-tools-web
```

---

### 6. Standard Web Server / Linux VPS
On any remote Linux/Ubuntu/Debian server:
```bash
# Using Gunicorn (Production)
pip install -r requirements.txt
gunicorn wsgi:app --bind 0.0.0.0:8000

# Or using Python directly:
python app.py
```
*(The server automatically reads the `PORT` environment variable from your host and binds to `0.0.0.0`).*

---

## 🛠️ The 9 Featured AI Tools

| # | Tool Name | Primary Category | Official URL | YouTube Embed ID |
|---|---|---|---|---|
| **1** | **Google NotebookLM** | Research & Knowledge Synthesis | [notebooklm.google.com](https://notebooklm.google.com/) | `uSVBfyHBiDU` |
| **2** | **Google Stitch** | AI UI/UX Design & Prototyping | [stitch.withgoogle.com](https://stitch.withgoogle.com/) | `o6Gr7X9erF8` |
| **3** | **Google AI Studio** | Developer LLM & Gemini API | [aistudio.google.com](https://aistudio.google.com/) | `AcNOi-PUTL4` |
| **4** | **Wispr Flow** | Context-Aware Voice Dictation | [wisprflow.ai](https://wisprflow.ai/) | `x6XJIbRksgI` |
| **5** | **Claude AI** | Conversational AI & Reasoning | [claude.ai](https://claude.ai/) | `r2vYObllqJU` |
| **6** | **Julius AI** | Data Science & Python Analytics | [julius.ai](https://julius.ai/) | `pzf0ZtgX0fs` |
| **7** | **Higgsfield AI** | Cinematic AI Video & World Models | [higgsfield.ai](https://higgsfield.ai/) | `3W1VhiKLNp4` |
| **8** | **Claude Skills** | Agentic Skills & Reusable Workflows | [claude.com/skills](https://claude.com/skills) | `w7_yWjYyxjE` |
| **9** | **ElevenLabs** | AI Voice Synthesis & Cloning | [elevenlabs.io](https://elevenlabs.io/) | `yDTbAxJ3sKI` |

---

## 📁 Repository Structure

```
aitoolpython/
├── app.py           # Core WSGI web application & route handler
├── wsgi.py          # Standard WSGI entry point (Gunicorn/Passenger)
├── index.html       # Responsive multi-tab UI with YouTube embeds
├── tools_data.py    # Python module containing full tool metadata
├── tools.json       # JSON data store
├── Procfile         # Heroku / Render / Railway process declaration
├── requirements.txt # Gunicorn production server requirements
├── runtime.txt      # Python 3.12 runtime specification
├── render.yaml      # Render blueprint configuration
├── vercel.json      # Vercel serverless routing configuration
├── api/index.py     # Vercel serverless function bridge
├── Dockerfile       # Container definition for Cloud Run / AWS
└── test_app.py      # Automated test suite (11/11 tests passing)
```

---

## 🧪 Testing

Run the automated test suite verifying data consistency and WSGI routing:
```bash
python -m unittest test_app.py
```
