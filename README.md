# Simple Pipeline for Asynchronous Task Scheduling in Python 

## 📖 Table of Contents
- [Simple Pipeline for Asynchronous Task Scheduling in Python](#simple-pipeline-for-asynchronous-task-scheduling-in-python)
  - [📖 Table of Contents](#-table-of-contents)
  - [😄 TL;DR: What is this at all?](#-tldr-what-is-this-at-all)
  - [💢 Background knowledge](#-background-knowledge)
    - [🎡 What is async tasks?](#-what-is-async-tasks)
    - [💭 Why we need them (Use Cases)?](#-why-we-need-them-use-cases)
  - [🎨 Architecture of the pipeline](#-architecture-of-the-pipeline)
  - [🧵 Installation and Usage](#-installation-and-usage)
  - [💎 How the things go (aka. Results)?](#-how-the-things-go-aka-results)
  - [📘 References](#-references)
  - [🎈 Author & Feedback/Contrubitons](#-author--feedbackcontrubitons)

---

## 😄 TL;DR: What is this at all?
TBA

## 💢 Background knowledge
TBA

### 🎡 What is async tasks?
TBA

### 💭 Why we need them (Use Cases)?
TBA

**Here are the some cases:**

<details>
    <summary>Case Study 1</summary>
    <p>Case Study 1</p>
</details>

<details>
    <summary>Case Study 2</summary>
    <p>Case Study 2</p>
</details>

---

## 🎨 Architecture of the pipeline
TBA with images

## 🧵 Installation and Usage
TBA with prompts

## 💎 How the things go (aka. Results)?
TBA with images

```
    # Redis
    redis-server --port 6380 --slaveof 127.0.0.1 6379

    # In the project folder for Flask UI
    celery worker -A flask_ui.celery_client -E --pool=solo -l info

    flower -A flask_ui.celery_client

    python flask_ui.py

    # In the project folder for REST-API
    celery worker -A flask_api.celery_client -E --pool=solo -l info

    flower -A flask_api.celery_client

    python flask_api.py
```

## 📘 References
TBA as bullet points with numbers

## 🎈 Author & Feedback/Contrubitons
TBA