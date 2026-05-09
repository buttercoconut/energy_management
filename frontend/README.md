# Energy Management Frontend

This is a lightweight Vue 3 application that consumes the FastAPI backend exposed by the
`energy_management` project.  It provides two main views:

* **Dashboard** – shows real‑time energy consumption data.
* **Report** – displays a summary report of daily consumption.

The project uses Vite as the build tool and includes the following key dependencies:

* `vue` – the core framework.
* `vue-router` – routing between the two views.
* `axios` – HTTP client for calling the backend API.
* `chart.js` + `vue-chartjs` – optional charting library (not used in the minimal
  example but ready for future enhancements).

## Getting Started

```bash
# Install dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build
```

The application expects the backend to be reachable at the URL specified by the
`VUE_APP_API_BASE_URL` environment variable.  By default it falls back to
`http://localhost:8000`.

## Project Structure

```
frontend/
├─ src/
│  ├─ api/          # API wrapper around axios
│  ├─ components/   # Reusable Vue components
│  ├─ views/        # Page components used by the router
│  ├─ router/       # Vue Router configuration
│  ├─ main.js       # Application entry point
│  └─ App.vue       # Root component
├─ package.json
└─ README.md
```
