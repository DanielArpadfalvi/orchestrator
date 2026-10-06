# Dashboard – Projektfedélzet

Artifact: https://claude.ai/artifact/94fw4py1eoxCoL7aozTVBQ
Írás: `ArtifactData` tool, kollekció `projects`, dokumentum-azonosító = projekt id (kisbetűs munkacím, pl. `pathlings`).
Mindig olvasd be előbb (`get`), és a kapott `version`-t add át `if_version`-ként (új dokumentumnál ne).

## Séma (a meglévő `swaplight` / `craterpult` dokumentumok mintájára)
```json
{
  "name": "Pathlings",
  "tagline": "Egy mondat magyarul.",
  "repo": "DanielArpadfalvi/Pathlings",
  "state": "planning | active | release-ready | paused",
  "order": 2,            // swaplight=1, craterpult=0; új projektek 2, 3, …
  "accent": "#7dff6a",
  "accent2": "#4fc3ff",
  "milestones": [
    { "code": "M0", "title": "Foundation", "tasks": [ { "id": "T0.1", "title": "Scaffold", "done": true } ] }
  ],
  "agents": [ { "id": "m1", "label": "M1 mag-szimuláció", "status": "running | done | failed" } ],
  "lastCommit": { "sha": "abc1234", "message": "…", "at": "2026-10-06T15:00:00Z" },
  "needsInput": [ { "id": "repo", "question": "Mit kell a tulajdonosnak tennie", "since": "2026-10-06T15:00:00Z" } ],
  "updatedAt": "2026-10-06T15:00:00Z"
}
```
A `milestones` a projekt `docs/TASKS.md`-jének tükre; minden elfogadott feladat után frissítsd.
