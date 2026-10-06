# Állapotnapló

## Lokális orkesztrátor indult (2026-10-06 este)

- A felhős Pathlings- és Craterpult-sessionök leálltak; **mindkettőt ez a lokális orkesztrátor-session viszi tovább párhuzamosan** (háttér-agentekkel, külön Playwright-portokon: Pathlings 4391, Craterpult 4411). Lokális klónok: `C:\Claude projects\Pathlings`, `C:\Claude projects\Craterpult`.
- Swaplight: 1.0-jelölt, a tulajdonosi store-lépésekre vár; nincs aktív munka.
- Futó feladatok: **Craterpult** `t7.2-paywall` merge a main-re (M6-ütközések feloldása) → utána M8.
- **Munkamegosztás:** a Pathlingset (T2.1-től) egy külön lokális session viszi (cwd `C:\Claude projects\Pathlings`); az orkesztrátor nem pushol a Pathlings main-re, a dashboardot a Pathlings `docs/TASKS.md` + `HANDOFF.md` alapján szinkronizálja.
- Megjegyzés: az agent-definíciók (`.claude/agents/`) csak a branch checkoutja utáni új sessionben töltődnek be; addig `general-purpose` agent kapja a szerep-leírást.
- **Pathlings:** T2.1 Renderer kész (`aa00679`, 327 unit + 7 e2e zöld) → T2.2 Camera (Pathlings-session).
- **Craterpult:** T7.2 paywall a main-en (`73695ae`, 243 unit + 29 e2e). M8: store-szövegek/weboldal/checklisták kész (commitra vár), screenshot-generátor fut. Tulajdonosi teendő: `craterpult-site` repó + Pages, `craterpult.support@gmail.com` postafiók.
- Blastyard (#4) repó még nem létezik – a tulajdonosnak kell létrehoznia.

---

## Átadás lokális sessionnek (2026-10-06, felhős orkesztrátor leállt)

**Queue állása** (`queue.md`):
- #1 Swaplight – kész 1.0-jelölt (másik munkamenet). #2 Craterpult – folyamatban (másik munkamenet, ne nyúlj hozzá).
- **#3 Pathlings – aktív.** Repo: `DanielArpadfalvi/Pathlings`, ág `main` (utolsó commit `dc654bc`). Kész: terv, M0 (scaffold+CI), M1 (teljes mag-motor, T1.1–T1.7). 264 unit + 3 e2e zöld, CI zöld. Részletek és következő lépések: Pathlings `docs/HANDOFF.md`.
- #4–#12 – nem kezdődött el. Repót a session nem tud létrehozni (403) → a tulajdonos hozza létre a következőt (`queue.md` munkacímei szerint), mielőtt az aktuális projekt elkészül.

**Félkész munka / WIP-branchek:** nincs. Minden pusholva: Pathlings `main`, orchestrator `claude/upbeat-bohr-rofk9t`.

**Nyitott döntések / ismert hiányok:** a beépített pályák validálása még nincs a `npm run check`-ben (T5.1); a M1-ben hozott, PLAN.md-ben nem rögzített szimulációs szabályok listája a Pathlings HANDOFF-ban (golden hash-ekkel rögzítve).

**Következő lépések sorrendben:**
1. Pathlings T2.1 Renderer (`game-builder` agent).
2. T2.2 Camera + T2.3 Smart selection.
3. T2.4 HUD + controls + e2e végigjátszás a `tests/fixtures/levels` megoldásaival.
4. M2 `game-reviewer` kör, majd M3 → M4 … a `playbook/PIPELINE.md` szerint 1.0-ig.
5. Kellő időben kérd a tulajdonostól a `DanielArpadfalvi/Blastyard` repót (#4).

**Dashboard** (Projektfedélzet, https://claude.ai/artifact/94fw4py1eoxCoL7aozTVBQ): `ArtifactData`, kollekció `projects`, doc `pathlings`. Mindig `get` → `update` az `if_version`-nel. Feladat-lista szinkron: `python3 scripts/tasks2dash.py <pathlings>/docs/TASKS.md '<extra JSON>' > x.json`, majd `update` `file_path`-szal. Mezők: `playbook/DASHBOARD.md`.

**Lokális futtatás:** `npm ci`; egyszer `npx playwright install chromium` (lokálisan nincs `/opt/pw-browsers`); `npm run check` / `build` / `test:e2e`. A `.claude/agents/*.md` agent-definíciók lokálisan közvetlenül használhatók (`subagent_type: game-builder` stb.).

---

Legfrissebb bejegyzés felül. Minden bejegyzés: dátum · projekt · mi készült · mi a következő · mi blokkol.

## 2026-10-06
- **Pathlings:** repó létrehozva (tulajdonos), terv kész és pusholva (`docs/PLAN.md`, `docs/TASKS.md` M0–M10). Üzleti modell: 30 pálya + szerkesztő + kódok ingyen, teljes játék $2,99. M0 kész, M1 kész (T1.1–T1.7).
- Monetizációs kutatás kész (`docs/monetization-research-2026-10.md`) → stúdió-szintű modell a `CLAUDE.md`-ben.
- Repó-létrehozás a sessionből nem megy (403, az app-integráció nem kaphat ilyen jogot) → a tulajdonos hozza létre projektenként; a következő repót előre jelezni kell.
- Orchestrator repó létrehozva (agent-definíciók, pipeline, queue).
- **Pathlings (#3)** indul. Blokkoló: a session nem tud GitHub repót létrehozni (403) → a tulajdonos hozza létre a `DanielArpadfalvi/Pathlings` (és a többi) repót; addig helyi fejlesztés.
