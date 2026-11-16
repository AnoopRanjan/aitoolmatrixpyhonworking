"""
Tools Data Store - AI Tools Directory
======================================
Comprehensive details, single-paragraph operational overviews, and YouTube tutorial IDs
for all 9 cutting-edge AI platforms.
"""

TOOLS_DATA = [
    {
        "id": "notebooklm",
        "name": "Google NotebookLM",
        "url": "https://notebooklm.google.com/",
        "category": "Research & Knowledge Synthesis",
        "tagline": "Personalized AI research notebook grounded strictly in your curated sources",
        "youtube_id": "uSVBfyHBiDU",
        "youtube_title": "Google NotebookLM Tutorial: The Ultimate AI Research & Study Tool",
        "badge_color": "#4285F4",
        "gradient": "linear-gradient(135deg, #1a73e8, #4285f4)",
        "pricing": "Free (with Google Account)",
        "developer": "Google Labs",
        "description": "Google NotebookLM is a personalized AI research assistant and note-taking environment grounded strictly in your curated source documents—including PDFs, Google Docs, text files, web links, and YouTube video transcripts—powered by Google's Gemini multimodal models. It works by creating a private knowledge base where every answer, summary, and analytical insight is tied to verifiable inline citations from your uploaded materials, virtually eliminating artificial hallucinations. It empowers students, researchers, and knowledge workers to effortlessly synthesize complex multi-document archives, generate comprehensive study guides and FAQs, and create realistic, dual-host conversational 'Audio Overviews' (AI podcasts) that turn dense technical reading into engaging, digestible discussions.",
        "key_features": [
            "Source-Grounded AI: Strictly limits answers to your uploaded materials with exact citation anchors.",
            "Multi-Source Ingestion: Accepts PDFs, Google Docs, Slides, Copied Text, Web URLs, and YouTube videos.",
            "Audio Overviews: Generates lively, human-sounding dual-host podcast discussions summarizing your documents.",
            "Instant Synthesis: Auto-generates study guides, briefing documents, FAQs, timelines, and outlines.",
            "Gemini 1.5 Integration: Handles massive source libraries with long-context reasoning capabilities."
        ],
        "how_it_helps": [
            "Converts hundreds of pages of research papers or reports into clear synthesized takeaways in seconds.",
            "Guarantees factual accuracy through clickable inline citations linked directly to your source text.",
            "Offers an auditory learning mode by turning complex reading into conversational podcast summaries.",
            "Eliminates hours of manual outlining, note summarizing, and study-guide compilation."
        ]
    },
    {
        "id": "stitch",
        "name": "Google Stitch",
        "url": "https://stitch.withgoogle.com/",
        "category": "AI-Native UI/UX & Frontend Prototyping",
        "tagline": "AI design canvas that translates natural language and vibes into interactive UI mockups and code",
        "youtube_id": "o6Gr7X9erF8",
        "youtube_title": "Google Stitch Tutorial for Beginners: Create AI UI Designs Step by Step",
        "badge_color": "#0F9D58",
        "gradient": "linear-gradient(135deg, #0f9d58, #34a853)",
        "pricing": "Free / Experimental Preview",
        "developer": "Google Labs",
        "description": "Google Stitch is an experimental, AI-native design canvas developed by Google Labs that translates natural language prompts, sketches, interface screenshots, and web URLs into high-fidelity user interface layouts and developer-ready frontend code. It operates through an interactive 'vibe design' workspace featuring an autonomous design agent, multi-screen storyboard capabilities, and real-time design critiques that allow creators to direct layouts, adjust styles, and iterate on themes using text or voice instructions. It can help UI/UX designers, developers, and product managers rapidly bridge the gap between creative ideation and functional product development by generating clean mobile and web UI screens, interactive prototypes, and production-ready code exports in minutes instead of days.",
        "key_features": [
            "AI-Native Design Canvas: Freeform workspace combining text prompts, images, screenshots, and live previews.",
            "Vibe Design Workflow: Direct visual styles, color palettes, typography, and mood using conversational language.",
            "Multi-Screen App Flows: Rapidly generates connected user journeys from onboarding to settings screens.",
            "Developer Code Export: Produces clean, standards-compliant HTML, Tailwind CSS, and frontend component code.",
            "Interactive Voice Critiques: Speak design feedback aloud to adjust component padding, contrast, and alignment."
        ],
        "how_it_helps": [
            "Allows non-designers to prototype professional-grade app and web interfaces without learning Figma.",
            "Drastically accelerates concept ideation for software startups and product teams by generating visual mockups in seconds.",
            "Exports usable frontend starter code directly, minimizing handoff friction between design and engineering.",
            "Facilitates rapid client presentations and user testing with fully realized, multi-screen prototypes."
        ]
    },
    {
        "id": "aistudio",
        "name": "Google AI Studio",
        "url": "https://aistudio.google.com/",
        "category": "Developer Playground & LLM Prototyping",
        "tagline": "Fastest prototyping environment to build with Gemini models, system prompts, and multimodal APIs",
        "youtube_id": "AcNOi-PUTL4",
        "youtube_title": "Google AI Studio: Complete Real-Time AI, Screen Sharing & App Building Guide",
        "badge_color": "#EA4335",
        "gradient": "linear-gradient(135deg, #ea4335, #ff5722)",
        "pricing": "Generous Free Tier + Pay-As-You-Go API",
        "developer": "Google DeepMind & Google Cloud",
        "description": "Google AI Studio is a rapid prototyping and experimentation web platform designed for developers and creators to interact with, evaluate, and fine-tune Google's state-of-the-art Gemini multimodal models and Gemma open models. It operates by offering a playground with system instructions, temperature and safety control sliders, multimodal token inputs (supporting code, images, audio, long-context video, and real-time screen streaming), structured JSON schema generation, and function calling. It helps developers, AI engineers, and makers quickly test complex prompts, prototype functional web and mobile applications with massive 1M+ token context windows, compare model latency and reasoning across Gemini 1.5 Pro and Flash, and instantly export production-ready code in Python, JavaScript, cURL, or REST API keys.",
        "key_features": [
            "Massive Context Window: Ingests up to 2 million tokens of video, audio, PDFs, and full source code repositories.",
            "Real-Time Multimodal Streaming: Interactive audio-video screen sharing for live software guidance and voice chat.",
            "Structured JSON Outputs: Enforces strict schema adhering responses ideal for automated database and API pipelines.",
            "Function Calling & Tools: Connects LLM logic to custom REST APIs, Python code execution, and web search grounding.",
            "One-Click Code Export: Generates ready-to-run client code snippets in Python, JavaScript, cURL, and REST."
        ],
        "how_it_helps": [
            "Enables instant prototyping and testing of complex AI agent logic without spinning up local infrastructure.",
            "Allows comprehensive document and video analysis by uploading entire hour-long video lectures or books in one prompt.",
            "Provides immediate API key generation to transition prototypes into live production applications.",
            "Significantly cuts token and operational costs by comparing Flash vs. Pro model trade-offs before deployment."
        ]
    },
    {
        "id": "wisprflow",
        "name": "Wispr Flow",
        "url": "https://wisprflow.ai/",
        "category": "Voice-to-Text & Context-Aware Dictation",
        "tagline": "AI speech-to-text dictation that removes filler words, formats thoughts, and types 3x faster anywhere",
        "youtube_id": "x6XJIbRksgI",
        "youtube_title": "Wispr Flow: The Next-Generation AI Voice Dictation & Workflow Multiplier",
        "badge_color": "#6366F1",
        "gradient": "linear-gradient(135deg, #4f46e5, #6366f1)",
        "pricing": "Freemium / Monthly Subscription ($12-$15/mo)",
        "developer": "Wispr AI",
        "description": "Wispr Flow is a cross-platform, system-wide AI dictation application for macOS, Windows, iOS, and Android that transforms natural, unedited human speech into clean, professionally formatted, and context-aware written text across any software application. Rather than simply transcribing phonetics like traditional speech recognition engines, Wispr Flow passes spoken audio through contextual language models that automatically filter out vocal filler words ('um', 'uh', 'like'), fix mid-sentence thought changes, apply intelligent punctuation and paragraphing, and adapt style based on whether you are writing an email, Slack chat, or code prompt. It dramatically boosts productivity by enabling users to speak naturally at over 150 words per minute into tools like Notion, Gmail, Cursor, or WhatsApp, supported by customizable technical dictionaries, voice shortcuts, and meeting notetaking capabilities.",
        "key_features": [
            "Universal OS Integration: Runs system-wide via a global hotkey across any desktop or mobile input field.",
            "Intelligent Speech Polishing: Automatically strips stuttering, vocal filler words, and corrects mid-sentence rewording.",
            "Context-Adaptive Formatting: Structures sentences into clean paragraphs, bulleted lists, or technical code blocks.",
            "Personalized Technical Dictionary: Learns developer terminology, acronyms, and colleague names with 100% accuracy.",
            "100+ Languages & Multilingual Mixing: Fluently captures natural multilingual speech patterns and regional dialects."
        ],
        "how_it_helps": [
            "Replaces tedious manual typing with natural speech, multiplying writing throughput to 120-180 words per minute.",
            "Eliminates keyboard strain and repetitive strain injuries (RSI) for developers, writers, and knowledge workers.",
            "Allows users to think out loud naturally without worrying about messy drafts or phonetic transcription errors.",
            "Works instantly in any text box across all favorite tools without requiring browser extensions or plugins."
        ]
    },
    {
        "id": "claude",
        "name": "Claude AI",
        "url": "https://claude.ai/",
        "category": "Conversational AI & Complex Reasoning",
        "tagline": "Anthropic's premier AI assistant renowned for nuanced writing, complex reasoning, and live Artifacts",
        "youtube_id": "r2vYObllqJU",
        "youtube_title": "Claude AI Tutorial for Beginners: Master Claude 3.5 & Live Artifacts",
        "badge_color": "#D97706",
        "gradient": "linear-gradient(135deg, #d97706, #f59e0b)",
        "pricing": "Free Tier / Pro ($20/mo) / Team Plans",
        "developer": "Anthropic",
        "description": "Claude.ai is Anthropic's flagship conversational artificial intelligence assistant powered by the Claude 3.5 model family (Sonnet, Haiku, and Opus), engineered with constitutional AI principles to prioritize deep reasoning, safety, nuanced communication, and exceptional coding performance. It functions through a clean interactive interface featuring Claude Artifacts—a dedicated side-by-side workspace that renders interactive HTML/React applications, SVG diagrams, Markdown documents, and code snippets in real time alongside your dialogue. Claude helps researchers, software engineers, and writers tackle heavy analytical workloads, debug complex multi-file codebases, draft sophisticated technical and creative prose, process massive document contexts up to 200,000 tokens, and automate knowledge retrieval across custom Project repositories.",
        "key_features": [
            "Interactive Artifacts: Live execution window that renders interactive React apps, SVGs, code, and dashboards.",
            "Industry-Leading Coding & Reasoning: Superior benchmarks in code generation, logic puzzles, and architecture review.",
            "200K Context Window: Ingests extensive codebases, full-length books, and voluminous legal documents in single chats.",
            "Claude Projects: Organized team workspaces with persistent custom instructions and uploaded knowledge bases.",
            "Constitutional AI Safety: Carefully aligned to provide reliable, nuanced, helpful, and non-hallucinatory output."
        ],
        "how_it_helps": [
            "Delivers best-in-class programming assistance, turning natural language prompts into working full-stack apps.",
            "Provides articulate, natural-sounding prose that reads like high-caliber human writing rather than robotic text.",
            "Allows live visual testing of UI components, charts, and interactive games without leaving the chat window.",
            "Enables persistent project management where team members collaborate with a unified context and documentation base."
        ]
    },
    {
        "id": "julius",
        "name": "Julius AI",
        "url": "https://julius.ai/",
        "category": "Data Science & Computational Analysis",
        "tagline": "AI data scientist that transforms spreadsheets, SQL, and CSVs into Python code, charts, and insights",
        "youtube_id": "pzf0ZtgX0fs",
        "youtube_title": "Julius AI for Data Analysis: Full Tutorial & Practical Workflow",
        "badge_color": "#8B5CF6",
        "gradient": "linear-gradient(135deg, #7c3aed, #8b5cf6)",
        "pricing": "Freemium / Monthly Subscription ($20/mo)",
        "developer": "Julius AI",
        "description": "Julius AI is an intelligent data analysis and computational assistant that converts natural language business inquiries into executable Python and R scripts to clean, process, analyze, and visualize complex datasets in real time. It works by allowing users to upload structured and unstructured files—such as Excel spreadsheets (.xlsx), CSVs, Google Sheets, databases, and PDFs—and conversational prompts to generate dynamic interactive charts, execute linear regressions, forecast time-series trends, and detect statistical anomalies while providing full code transparency. It serves data analysts, finance professionals, researchers, and non-technical business users by eliminating formula friction, automating routine data hygiene tasks, and delivering presentation-grade charts and executive summaries in seconds.",
        "key_features": [
            "Conversational Data Science: Ask plain-English questions to analyze tables without writing VLOOKUP or SQL queries.",
            "Python/R Execution Engine: Automatically writes and runs sandboxed pandas, numpy, and scikit-learn code behind the scenes.",
            "Publication-Ready Visualizations: Generates interactive heatmaps, scatter plots, trend lines, and downloadable charts.",
            "Predictive Modeling & Regressions: Builds machine learning forecasts, statistical significance tests, and anomaly detection.",
            "Multi-File & Database Connectors: Ingests Excel workbooks, Google Sheets, PostgreSQL, and multi-tab financial reports."
        ],
        "how_it_helps": [
            "Democratizes advanced data science for non-coders who want powerful Python analysis directly from raw Excel sheets.",
            "Saves hours spent manually cleaning missing values, standardizing dates, and reconciling disparate table structures.",
            "Generates presentation-ready visual reports and exportable cleaned spreadsheets with one simple instruction.",
            "Provides full transparency by revealing the underlying Python code so analysts can inspect and verify calculations."
        ]
    },
    {
        "id": "higgsfield",
        "name": "Higgsfield AI",
        "url": "https://higgsfield.ai/",
        "category": "Cinematic AI Video Generation & World Models",
        "tagline": "Director-level AI video creation suite with camera controls, character consistency, and high-def realism",
        "youtube_id": "3W1VhiKLNp4",
        "youtube_title": "Master Higgsfield AI: Cinematic Video Generation & Studio Controls",
        "badge_color": "#EC4899",
        "gradient": "linear-gradient(135deg, #db2777, #ec4899)",
        "pricing": "Tiered Credit Plans / Subscriptions",
        "developer": "Higgsfield AI",
        "description": "Higgsfield AI is a creative video generation and world-modeling platform built specifically for directors, animators, and digital content creators who require granular, scene-by-scene cinematic control over generative video. It functions through an advanced suite containing Cinema Studio, Shorts Studio, and models like Seedance, enabling creators to direct virtual cameras with specific panning, zooming, and tilting movements, define lighting and genre aesthetics, and generate extended video clips with native high-definition resolution and synced audio. It empowers filmmakers and marketing teams to produce high-impact visual storytelling while solving generative video's biggest hurdle: maintaining character and scene consistency across multiple sequential camera takes through multi-image reference pipelines.",
        "key_features": [
            "Cinema Studio Director Controls: Configure focal length, camera motion (pan, tilt, crane, dolly), and cinematic lighting.",
            "Seedance Extended Video Models: Generates up to 30-second continuous cinematic takes in native 1080p resolution.",
            "Multi-Reference Character Consistency: Upload multiple reference angles to keep character appearance stable across cuts.",
            "Shorts Studio: Tailored generative workflows for high-engagement vertical videos on TikTok, Reels, and Shorts.",
            "Stylistic Transformations (Genjutsu): Re-render scenes into anime, cyberpunk, watercolor, or 3D Pixar animation styles."
        ],
        "how_it_helps": [
            "Empowers indie filmmakers, creators, and advertising agencies to produce high-budget cinematic visuals on minimal budgets.",
            "Eliminates random video hallucinations by providing precise virtual camera movement and lighting presets.",
            "Solves character drift across scenes, allowing multi-scene narratives and commercial storylines with a consistent actor.",
            "Accelerates storyboarding, pitch decks, and commercial video creation from weeks of CGI production into minutes."
        ]
    },
    {
        "id": "claude-skills",
        "name": "Claude Skills",
        "url": "https://claude.com/skills",
        "category": "Agentic Framework & Reusable Domain Skills",
        "tagline": "Modular, repeatable instruction packages that endow Claude with specialized workflows and tool powers",
        "youtube_id": "w7_yWjYyxjE",
        "youtube_title": "Claude Skills & Projects: Automating Advanced Agent Workflows",
        "badge_color": "#10B981",
        "gradient": "linear-gradient(135deg, #059669, #10b981)",
        "pricing": "Included with Claude.ai / Claude Code ecosystem",
        "developer": "Anthropic",
        "description": "Claude Skills is Anthropic's modular extensibility framework designed for Claude.ai, Claude Code, and agentic workflows to endow the AI with specialized, repeatable domain competencies and standardized operational procedures. It operates using an open standard centered around structured SKILL.md instruction packages and progressive disclosure, wherein Claude loads minimal YAML metadata at startup and dynamically pulls in full execution rules, helper scripts, and corporate guidelines only when relevant user prompts are detected. It can help engineering teams, enterprises, and individual developers standardize software architectures, enforce brand tone and compliance rules, automate multi-step document pipelines (like PowerPoint, Excel, or Word generation), and connect seamlessly with external APIs via the Model Context Protocol (MCP) without polluting prompt context windows.",
        "key_features": [
            "Modular SKILL.md Architecture: Encapsulate domain rules, file templates, validation scripts, and step-by-step guides.",
            "Progressive Disclosure: Keeps tokens lean by advertising lightweight summaries and loading full details only on demand.",
            "Open Standard Portability: Compatible across Claude Code, Claude.ai, Cursor, Gemini CLI, and modern coding agents.",
            "Model Context Protocol (MCP) Synergy: Bridges standardized agent workflows with external live tools and enterprise databases.",
            "Custom Enterprise Workflows: Standardize corporate code reviews, financial reporting templates, and style enforcement."
        ],
        "how_it_helps": [
            "Prevents repetitive prompt engineering by packaging complex organizational instructions into one reusable skill.",
            "Maintains low latency and cheap token usage by only loading instructions when the relevant task is actually triggered.",
            "Enforces strict architectural consistency and code standards across large engineering teams automatically.",
            "Empowers non-technical team members to run complex multi-stage tasks reliably with pre-tuned domain workflows."
        ]
    },
    {
        "id": "elevenlabs",
        "name": "ElevenLabs",
        "url": "https://elevenlabs.io/",
        "category": "Generative AI Voice Synthesis & Audio AI",
        "tagline": "Industry-leading hyper-realistic text-to-speech, instant voice cloning, and multilingual video dubbing",
        "youtube_id": "yDTbAxJ3sKI",
        "youtube_title": "ElevenLabs AI Voice Tutorial: Complete Text-to-Speech & Voice Cloning Guide",
        "badge_color": "#0284C7",
        "gradient": "linear-gradient(135deg, #0284c7, #38bdf8)",
        "pricing": "Free Tier / Starter ($5/mo) / Creator ($22/mo) / Enterprise",
        "developer": "ElevenLabs",
        "description": "ElevenLabs is a generative voice technology and audio AI platform that delivers industry-leading text-to-speech synthesis, instant voice cloning, and emotional speech generation with human-like cadence, nuance, and intonation across dozens of languages. It operates using deep learning generative audio architectures that analyze script punctuation and linguistic context to control pitch, pacing, and emotional expression, accompanied by tools like Voice Design, Voice Isolator, and Studio for timeline-based audio creation. It helps content creators, game developers, audiobook publishers, and businesses produce studio-grade voiceovers, clone authentic digital vocal replicas from small audio samples, translate and dub videos into international languages while preserving original speaker characteristics, and build conversational voice agents.",
        "key_features": [
            "Hyper-Realistic Text-to-Speech: Uncanny human cadence, natural breathing, emotional inflection, and contextual pacing.",
            "Instant & Professional Voice Cloning: Replicate any voice with studio accuracy using as little as one minute of clean audio.",
            "Multilingual AI Dubbing: Automatically translates and redubs videos into 30+ languages matching the speaker's vocal timbre.",
            "Voice Isolator & Audio Cleanup: Strips extreme background noise, reverb, and chatter to produce crisp podcast-quality vocals.",
            "Conversational Voice AI Agents: Ultra-low latency voice models powering real-time interactive customer service and gaming NPCs."
        ],
        "how_it_helps": [
            "Enables video creators, podcasters, and educators to produce high-end voiceovers without expensive microphones or voice actors.",
            "Localizes YouTube videos and corporate training media worldwide by dubbing content into dozens of languages effortlessly.",
            "Allows authors and publishers to transform written books into full-length audiobooks with multi-character voice casting.",
            "Saves hours of audio post-production by removing studio background noise and repairing flawed vocal recordings instantly."
        ]
    }
]
