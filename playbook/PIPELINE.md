# Pipeline – egy játék útja ötlettől 1.0-ig

Egyszerre egy projekt aktív. Minden fázis végén: commit + push a projekt repóba, `STATUS.md` bejegyzés, dashboard-frissítés (`playbook/DASHBOARD.md`).

## F0 – Kiválasztás & repo
- A `queue.md` első nem kész tétele. Munkacím: eredeti, nem védjegy, rövid, store-kereshető.
- Repo: `DanielArpadfalvi/<Munkacím>` (publikus – a macOS-runner percei publikus repóban ingyenesek). A session **nem tud repót létrehozni** → ha nincs meg, kérd a tulajdonostól, és addig dolgozz helyben (`/home/user/<munkacím>`), push később.
- Dashboard-szinkron: `python3 scripts/tasks2dash.py <projekt>/docs/TASKS.md > x.json`, majd `ArtifactData update` `file_path`-szal.
- Dashboard-dokumentum létrehozása `projects/<id>` alatt (`state: "planning"`).

## F1 – Tervezés (`game-designer` agent)
Kimenet a projekt repóban: `CLAUDE.md` (Swaplight/Craterpult mintájára), `README.md`, `docs/PLAN.md` (magyar GDD + technikai terv + üzleti modell + kockázatok), `docs/TASKS.md` (M0…M9 mérföldkövek, feladatonként elfogadási feltételekkel).
Az orkesztrátor átnézi: scope reális-e (1.0 = egy kis csapat kb. 10–15 iterációja), van-e egyértelmű „fun core”, mi kerül 1.1-re.

## F2 – Alapozás (M0)
Scaffold + CI (`ci.yml`; az `android.yml`/`ios.yml` a mobil héjnál). Elfogadás: `npm run check`, `npm run build`, `npm run test:e2e` zöld.

## F3 – Iteratív építés (M1 → M7)
Ciklus feladatonként:
1. **Kiadás:** `game-builder` agent pontos specifikációval (fájlok, AC, mit NE érintsen). Párhuzamosan csak egymást nem fedő fájlkörre; közös fájloknál `isolation: worktree`.
2. **Ellenőrzés (orkesztrátor):** diff-átnézés, `npm run check`, `npm run build`, releváns e2e, screenshotok megnézése (Playwright, 1× DPR, render loop megállítva).
3. **Elfogadás:** `docs/TASKS.md` pipálás, commit (explicit útvonalak), push, dashboard.
4. Mérföldkövenként `game-reviewer` agent: játékélmény + kód + UX; a P0/P1 hibák új feladatként visszamennek a listára.
Haladási sorrend: mag-szimuláció (determinisztikus, tesztelt) → játszható prototípus → játékélmény (hang, effektek, haptika) → tartalom/módok → meta & UI (menü, mentés, beállítások, EN/HU) → mobil héj (Capacitor, ikon/splash kódból, natív CI) → monetizáció.

## F4 – Kiadás-előkészítés (M8–M9)
- Store-szövegek EN/HU, screenshot-generátor (`npm run store:screens`), ikon/feature graphic, adatvédelmi szöveg + támogatási oldal, korhatár- és adatbiztonsági válaszok, `docs/RELEASE.md`, `docs/PLAY-STORE-CHECKLIST.md`, `docs/APP-STORE-CHECKLIST.md` (Swaplight mintájára).
- Teljes QA-kör (`game-reviewer`), egyensúly, teljesítmény (60 FPS célként, alsó kategóriás Android is).
- Verzió: `package.json` 1.0.0, Android `versionName 1.0.0` / `versionCode 1`, iOS `MARKETING_VERSION 1.0.0`. Git tag `v1.0.0`. CI zöld (web + Android + iOS unsigned).

## F5 – Lezárás
- `docs/HANDOFF.md`: mi kész, mi vár a tulajdonosra (secretek, store-fiók lépések), 1.1-ötletek.
- `queue.md`: `[x]`, dashboard `state: "release-ready"`, `needsInput`-ba a tulajdonosi teendők.
- Következő tétel a listáról.

## Szabályok
- Agentnek mindig: olvassa el a projekt `CLAUDE.md`-jét, ne commitoljon (ha nem kérted), ne futtasson `playwright install`-t, egyedi Playwright-portot használjon, ha más agent is futhat.
- „Flake” nem gyökérok; hibát nem tesztkikapcsolással javítunk.
- Ha valami a tulajdonosra vár (repo, secret, fiók), azt a dashboard `needsInput` mezőjébe és a `STATUS.md`-be írd, és dolgozz tovább azon, ami nem függ tőle.
