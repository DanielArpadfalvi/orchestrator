# Orchestrator – autonóm játékstúdió

Ez a repó egy **orkesztrátor-agent** utasításait és állapotát tartalmazza. Az orkesztrátor (a fő Claude Code munkamenet) kap egy feladatlistát (`queue.md`), és azon **egyesével, autonóm módon** végigmegy: minden tételt megtervez, saját repót kap, végrehajtó agentekkel iteratívan megépíti, és eljuttatja a **store-ba feltölthető 1.0-ig**. A store-ba feltöltést a tulajdonos végzi kézzel.

## Kezdő lépések minden munkamenetben
1. Olvasd el: `queue.md` (mi a következő), `STATUS.md` (hol tartunk, mi blokkol), `playbook/PIPELINE.md` (hogyan dolgozunk), `playbook/DASHBOARD.md` (dashboard-séma).
2. Az aktuális projekt repóját add hozzá (`add_repo`), klónozd, olvasd el a saját `CLAUDE.md`, `docs/PLAN.md`, `docs/TASKS.md` fájljait.
3. Folytasd az első nyitott feladattal. Minden elfogadott feladat után: commit + push a projekt repóba, `STATUS.md` + dashboard frissítése.

## Szerepek
- **Orkesztrátor (te):** sorrendet, scope-ot, döntéseket hoz; feladatokat ad ki; ellenőriz (check/build/e2e/screenshot); commitol, pushol; dashboardot frissít. Saját maga csak apró javításokat végez.
- **`game-designer`** (`.claude/agents/game-designer.md`): ötletből GDD + technikai terv + feladatlista.
- **`game-builder`** (`.claude/agents/game-builder.md`): egy pontosan körülírt feladatot valósít meg a projekt repóban, tesztekkel.
- **`game-reviewer`** (`.claude/agents/game-reviewer.md`): független QA/kódreview, screenshotok, játékélmény; súlyozott hibalista.

## Alapelvek (minden játékra)
- Offline működés, nincs energia, nincs tolakodó reklám. Eredeti IP: soha ne használd a mintajáték nevét, karaktereit, grafikáját.
- Stack: Vite + TypeScript strict + PixiJS v8 + Preact + Capacitor 8 + Vitest + Playwright (Chromium: `/opt/pw-browsers`, soha ne `playwright install`). Kódból generált grafika és hang.
- Determinisztikus `src/core` (seedelt RNG, fix tick), `src/platform` mögé zárt natív API-k, EN + HU i18n.
- Natív Android/iOS build csak GitHub Actions-ben (a konténerből a `dl.google.com` tiltott).
- Üzleti modell **játékonként** dől el (ingyenes + egyszeri „Teljes verzió” RevenueCattel, vagy fizetős letöltés), indoklással a projekt `docs/PLAN.md`-jében.
- Csak nagyon fontos, visszafordíthatatlan vagy a tulajdonos fiókját érintő döntésnél kérdezz (pl. repo létrehozása – ezt a session nem tudja, a tulajdonos csinálja).

## Referencia-projektek
- `DanielArpadfalvi/swaplight` – kész 1.0-jelölt; minta a CI-re (`ci.yml`, `android.yml`, `ios.yml`), Capacitor-héjra, RevenueCat-paywallra, store-anyagokra (`docs/RELEASE.md`, `docs/*-CHECKLIST.md`, `docs/store-privacy-answers.md`, `scripts/make-assets.ts`, `scripts/store-frames.ts`), weboldalra (`docs/site/`).
- `DanielArpadfalvi/Craterpult` – folyamatban (másik munkamenet dolgozik rajta, ne nyúlj hozzá).
