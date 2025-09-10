# Giga Maps API — Dashboard Documentation

This repository contains the OpenAPI 3.1 specification (`openapi.yaml`) for the Giga Maps API. The goal is to provide documentation that can be embedded directly into the Giga Maps dashboard as a section in the sidebar navigation.

---

## How to Include Documentation in the Dashboard

1. Add a **Documentation** link in your dashboard sidebar navigation.

   * For example, in React:

   ```jsx
   <nav>
     <ul>
       <li><a href="/dashboard">Dashboard</a></li>
       <li><a href="/docs">API Documentation</a></li>
     </ul>
   </nav>
   ```

2. Create a `/docs` route or page in your site to serve the API docs.

---

## Serving the OpenAPI YAML

You can render the `openapi.yaml` file in the dashboard using tools like **Swagger UI** or **Redoc**.

### Option A — Swagger UI React

Install:

```bash
npm install swagger-ui-react swagger-ui
```

Create a docs page:

```jsx
import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";

export default function Docs() {
  return <SwaggerUI url="/openapi.yaml" />;
}
```

Place `openapi.yaml` in your `public/` folder so it’s served at `/openapi.yaml`.

### Option B — Redoc

Install:

```bash
npm install redoc
```

Create a docs page:

```jsx
import { RedocStandalone } from "redoc";

export default function Docs() {
  return <RedocStandalone specUrl="/openapi.yaml" />;
}
```

---

## Python Websites

If your dashboard is served by a Python backend, you can still embed docs.

### Option A — Redoc with Flask

```python
from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)

@app.route("/docs")
def docs():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
      <title>API Docs</title>
      <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
    </head>
    <body>
      <redoc spec-url='/openapi.yaml'></redoc>
    </body>
    </html>
    ''')

@app.route('/openapi.yaml')
def spec():
    return send_from_directory('.', 'openapi.yaml')
```

### Option B — Swagger UI with Flask

```python
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/docs")
def docs():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
      <title>API Docs</title>
      <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css">
    </head>
    <body>
      <div id="swagger"></div>
      <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
      <script>
        SwaggerUIBundle({ url: '/openapi.yaml', dom_id: '#swagger' });
      </script>
    </body>
    </html>
    ''')
```

---

## Recommended Setup

* Place `openapi.yaml` in the `public/` (JS) or project root (Python) so it’s served at `/openapi.yaml`.
* Add a `/docs` route that embeds Swagger UI or Redoc.
* Add **API Documentation** to your dashboard sidebar.

---

## Example Sidebar Item

* Dashboard
* Schools
* Connectivity
* **API Documentation** ← links to `/docs`

---

## Support

* Website: [https://giga.global](https://giga.global)
* Email: [gigabcn@unicef.org](mailto:gigabcn@unicef.org)

---

## Add API Docs to the Dashboard Sidebar

Goal: show the OpenAPI docs inside your dashboard with a sidebar link.

### Structure

* Sidebar link: “Documentation” → `/docs`
* Page at `/docs` renders Swagger UI or Redoc
* `openapi.yaml` served locally from `/openapi.yaml`

### JavaScript (Next.js 13+ App Router)

1. Expose the spec

```ts
// app/openapi.yaml/route.ts
import { NextResponse } from "next/server";
import fs from "node:fs";
import path from "node:path";

export async function GET() {
  const file = fs.readFileSync(path.join(process.cwd(), "openapi.yaml"), "utf8");
  return new NextResponse(file, {
    headers: { "Content-Type": "application/yaml" }
  });
}
```

2. Add the docs page (Redoc via script)

```tsx
// app/docs/page.tsx
export default function DocsPage() {
  return (
    <html>
      <head>
        <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
      </head>
      <body>
        <redoc spec-url="/openapi.yaml"></redoc>
      </body>
    </html>
  );
}
```

3. Or use Swagger UI (React)

```bash
npm i swagger-ui-react
```

```tsx
// app/docs/page.tsx
"use client";
import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";

export default function DocsPage() {
  return <SwaggerUI url="/openapi.yaml" docExpansion="list" tryItOutEnabled />;
}
```

4. Sidebar link example

```tsx
// components/Sidebar.tsx
export function Sidebar() {
  return (
    <nav>
      <a href="/">Dashboard</a>
      <a href="/docs">Documentation</a>
    </nav>
  );
}
```

### Python (FastAPI or Flask dashboard)

1. Serve the spec

```python
# FastAPI
from fastapi import FastAPI, Response
app = FastAPI()

@app.get("/openapi.yaml")
def spec():
    with open("openapi.yaml", "r", encoding="utf-8") as f:
        return Response(f.read(), media_type="application/yaml")
```

```python
# Flask
from flask import Flask, Response
app = Flask(__name__)

@app.get("/openapi.yaml")
def spec():
    return Response(open("openapi.yaml").read(), mimetype="application/yaml")
```

2. Docs route with Redoc (no build step)

```python
# FastAPI
from fastapi.responses import HTMLResponse

@app.get("/docs", response_class=HTMLResponse)
def docs():
    return """
<!doctype html>
<html>
  <head>
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
  </head>
  <body>
    <redoc spec-url="/openapi.yaml"></redoc>
  </body>
</html>
"""
```

```python
# Flask
@app.get("/docs")
def docs():
    return """
<!doctype html>
<html>
  <head>
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
  </head>
  <body>
    <redoc spec-url="/openapi.yaml"></redoc>
  </body>
</html>
"""
```

3. Optional: Bundle static docs

```bash
npx redoc-cli bundle openapi.yaml -o public/docs/index.html
```

Then link the sidebar to `/docs/index.html`.

### Tips

* Keep `openapi.yaml` at repo root.
* Gate access behind your dashboard auth if needed.
* Use Redoc for clean reading. Use Swagger UI if you want "Try it out".
* Add `/docs` to the sidebar like any other route.
