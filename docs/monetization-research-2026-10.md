# IAP-modell piackutatás – max. játékosszám, min. elriasztás (2026-10)

Cél: offline, reklám- és energiamentes indie mobiljátékok (iOS + Android) **minél több játékoshoz** juttatása IAP-alapú modellel.
Módszer: webes keresés + oldalletöltés. Jelölés: **[K]** = az oldal nem volt letölthető (proxy blokkolta: pocketgamer.biz, toucharcade.com, pockettactics.com, mobilegamer.biz, shatteredpixel.com, engadget.com, reddit.com), az adat a keresési kivonatból származik. A Reddit közvetlenül nem volt elérhető, a hangulatot más fórumok/sajtó alapján foglaltam össze.

## 1. Modellek összevetése

| Modell | Letöltés / elérés | Konverzió / bevétel | Értékelés-kockázat | Forrás |
|---|---|---|---|---|
| Fizetős letöltés | A letöltések 96%-a F2P-é 2025-ben; a prémium szegmens niche marad | Csak fizetők játszanak; a $10→$40 áremelés után a RE2 iOS havi vásárlói ~9 500-ról 175-re estek (ugyanakkor ott free+unlock volt, az árrugalmasságot mutatja) | Alacsony (aki fizetett, elkötelezett) | [gamedev.net / AppMagic](https://gamedev.net/news/premium-mobile-games-are-back-with-releases-up-77-in-2025-r4367/), [VGC](https://www.videogameschronicle.com/news/resident-evil-2-remake-has-sold-fewer-than-10000-copies-on-ios-estimates-suggest/) |
| Ingyenes + egyszeri feloldás (free-to-try) | Ingyenes listában jelenik meg, minden piacon letölthető | Ball x Pit: ~670 ezer Android-letöltés, 4,8★ (7,5 ezer értékelés) $9,99-es feloldással | Közepes: Peglin (első harmad ingyen, $8,99) Androidon 3,41★, iOS-en 4,1★ | [AppBrain – Ball x Pit](https://www.appbrain.com/app/ball-x-pit/com.devolverdigital.ballxpit), [Peglin App Store](https://apps.apple.com/us/app/peglin/id6446336622) [K] |
| Ingyenes + opcionális IAP (kozmetika / tip jar / tartalomcsomag) | Shattered PD: 5M+ letöltés; Mindustry: 5M+ Androidon (9,3M össz.); Polytopia: 25M letöltés | Kevesen fizetnek, de nincs kapu; a Polytopia „sok játékos, kevés bevétel/fő” stratégiával is nyereséges | Legalacsonyabb | [Fandom – SPD](https://pixeldungeon.fandom.com/wiki/Shattered_Pixel_Dungeon) [K], [AppBrain – Mindustry](https://www.appbrain.com/app/mindustry/io.anuke.mindustry) [K], [Wikipedia – Polytopia](https://en.wikipedia.org/wiki/The_Battle_of_Polytopia) [K] |
| Teljesen ingyenes | Max. elérés | Nincs bevétel | Nincs | – |

Általános adatok:
- Google Playen az appok ~97%-a ingyenes ([BankMyCell](https://www.bankmycell.com/blog/number-of-google-play-store-apps/) [K]); „$0,99-nél is nagyon nehéz letöltést szerezni, ingyen könnyű” ([ScienceDirect, letöltési tényezők](https://www.sciencedirect.com/science/article/pii/S0148296320306536) [K]).
- Az IAP-konverzió saját árrugalmassága −1 és −4 között van, azaz az ár csökkentése arányában több vásárlót hoz ([ScienceDirect, 2023](https://www.sciencedirect.com/science/article/pii/S0167718723000279) [K]).
- Freemium jellegű termékeknél jellemzően 2–5% fizet ([Crazy Egg](https://www.crazyegg.com/blog/free-to-paid-conversion-rate/) [K]). Ez SaaS-alapú benchmark, játékokra csak irányadó.
- Prémium reneszánsz: 2025-ben +77% prémium mobilmegjelenés (~750 db), de a letöltések 96%-a F2P ([gamedev.net / AppMagic](https://gamedev.net/news/premium-mobile-games-are-back-with-releases-up-77-in-2025-r4367/) [K]).
- Google Play Game Trials (2025): a fizetős játékok percekig–1 óráig kipróbálhatók, és a haladás megmarad ([Google blog](https://blog.google/products-and-platforms/platforms/google-play/google-play-paid-games-updates/) [K]). A platform maga is a kipróbálás felé tolja a prémiumot.

## 2. Mit utálnak és mit fogadnak el a játékosok

| Utált | Bizonyíték | Elfogadott | Bizonyíték |
|---|---|---|---|
| Kényszerített reklám (a #1 panasz, ~46–47%) | [AppFollow](https://appfollow.io/blog/mobile-game-monetization) [K] | Egyszeri feloldás, világosan kommunikálva | Ball x Pit értékelései kiemelik: „truly free (no ads) chance to demo… straightforward way to purchase” ([App Store reviews](https://apps.apple.com/us/app/ball-x-pit/id6738703497?see-all=reviews&platform=iphone) [K]) |
| Pay-to-win | [AppFollow](https://appfollow.io/blog/mobile-game-monetization) [K], [Polytopia CEO](https://www.pocketgamer.biz/aggressive-mobile-game-monetisation-pushes-loyal-players-to-churn-says-battle-of-polytopia-ceo/) [K] | Nem fogyó (non-consumable) DLC, költéskorlát (Polytopia max. $35) | [Wikipedia – Polytopia](https://en.wikipedia.org/wiki/The_Battle_of_Polytopia) [K] |
| Fogyóeszköz / prémium valuta, korlátlan költés („túl drága lesz, a hű játékos lemorzsolódik”) | [Polytopia CEO, pocketgamer.biz](https://www.pocketgamer.biz/aggressive-mobile-game-monetisation-pushes-loyal-players-to-churn-says-battle-of-polytopia-ceo/) [K] | Kozmetikai supporter-csomag | SPD: $5/$20 supporter tier, csak kozmetika ([Fandom](https://pixeldungeon.fandom.com/wiki/Shattered_Pixel_Dungeon) [K]) |
| Előre nem jelzett paywall („nothing locked”, aztán zárva) | itch.io-kommentek ([1](https://itch.io/post/14976437), [2](https://itch.io/post/4792302)) [K] | Előre deklarált, hogy mi ingyenes | Peglin: „unlimited access to the first third” ([App Store](https://apps.apple.com/us/app/peglin/id6446336622)) [K] |
| Energia / várakozás | Ugyanabba a kategóriába esik, mint a fizetős gyorsítás; külön 2024-es %-os adatot nem találtam | Kipróbálás → teljes játék (shareware-logika); a legtöbben viszont csak az ingyenes részt játsszák | [AnandTech fórum](https://forums.anandtech.com/threads/android-users-free-app-with-ads-upgrade-to-pro-version-or-full-version-at-99.2431773/post-37410047) [K] |

## 3. Esettanulmányok

| Játék | Modell (mobil) | Ár | Játékos/letöltés | Tanulság | Forrás |
|---|---|---|---|---|---|
| Polytopia | Ingyenes, 4 törzs ingyen, többi non-consumable | $0,99–2,99/törzs, max. $35 | 25M letöltés | Ingyenes mag + kozmetikai/tartalmi DLC = legnagyobb elérés | [Wikipedia](https://en.wikipedia.org/wiki/The_Battle_of_Polytopia), [pocketgamer.biz](https://www.pocketgamer.biz/the-battle-of-polytopia-surpasses-25m-downloads-on-mobile/) [K] |
| Shattered Pixel Dungeon | 100% ingyenes, supporter IAP (kozmetika); iOS-en/Steamen fizetős | $5–20 tip | 5M+ (Android) | Az iOS-megjelenés háromszorozta a támogatók számát ([SPD 2021](https://shatteredpixel.com/blog/shattered-pixel-dungeon-in-2021.html) [K]) | [Fandom](https://pixeldungeon.fandom.com/wiki/Shattered_Pixel_Dungeon) [K] |
| Mindustry | Android ingyen, iOS $1,99, Steam fizetős | $0 / $1,99 | 5M+ Android, 9,3M össz. | Az ingyenes platform viszi a tömeget | [Mindustry FAQ](https://mindustrygame.github.io/wiki/faq/), [Wikipedia](https://en.wikipedia.org/wiki/Mindustry) [K] |
| Alto's Adventure | iOS $2,99 prémium; Android ingyenes + reklám | – | Android 36,5M → 50M+ | Ingyenes = nagyságrenddel több játékos | [Cult of Mac](https://www.cultofmac.com/news/altos-adventure-goes-free-on-android-stays-premium-on-ios), [Google Play](https://play.google.com/store/apps/details?id=com.noodlecake.altosadventure) [K] |
| Monument Valley | Prémium $3,99 | – | 26M letöltésből 21M ingyenes akció idején; Androidon csak 5% fizetett | Az ingyenesség sokszorozza a játékosszámot | [Game Developer](https://www.gamedeveloper.com/business/-i-monument-valley-i-revenues-top-14-million-two-years-after-launch), [GamesBeat](https://gamesbeat.com/monument-valley-developer-only-5-of-android-installs-were-paid-for/) [K] |
| Threes | $1,99 prémium → 21 nap múlva ingyenes klónok (2048) → Threes Free | – | A klónok vitték a tömeget; a free verzióval napi bevétel 2× | Fizetős puzzle-t ingyenes klón leelőz | [TechCrunch](https://techcrunch.com/2014/03/24/clones-clones-everywhere-1024-2048-and-other-copies-of-popular-paid-game-threes-fill-the-app-stores), [Game Developer](https://www.gamedeveloper.com/business/-i-threes-i-devs-double-daily-income-with-free-version) [K] |
| Pocket City | Külön „Free” (reklámos) + fizetős app | $2,99 | Free 1M+, Paid 1M+ | Két külön app: az ingyenes kb. annyi letöltést hoz, mint a fizetős | [Google Play Free](https://play.google.com/store/apps/details?id=com.codebrewgames.pocketcity&hl=en_NZ&gl=US) [K] |
| Ball x Pit (2026) | Free-to-try, 1. szint ingyen, nincs reklám | $9,99 | ~670 ezer (Android), 4,8★ | Jól kommunikált free trial-nál nincs „demó”-harag | [Gematsu](https://www.gematsu.com/2026/03/ball-x-pit-now-available-for-ios-android), [AppBrain](https://www.appbrain.com/app/ball-x-pit/com.devolverdigital.ballxpit) [K] |
| Peglin | Free-to-try, első harmad ingyen | $8,99 | ~720 ezer (Android) | Android 3,41★ vs. iOS 4,1★: a magas feloldási ár miatt rosszabb értékelések | [AppBrain](https://www.appbrain.com/app/peglin-a-pachinko-roguelike/com.RedNexusGamesInc.Peglin) [K] |
| Balatro | Prémium + Apple Arcade | $9,99 | 3,1M mobil, $21,3M | Prémium csak erős márkával skálázódik | [gamedev.net](https://gamedev.net/news/premium-mobile-games-are-back-with-releases-up-77-in-2025-r4367/) [K] |
| Slay the Spire / Dicey Dungeons / Wilmot's Warehouse / Mini Metro | Prémium | $9,99 / $4,99 / $4,99 / ~$0,99–4 | StS 1M+ Android; Mini Metro 1M+ Android (össz. ~1,4M eladás, minden platformon) | Kiváló játékok, de „csak” 1M körüli mobil elérés | [AppBrain StS](https://www.appbrain.com/app/slay-the-spire-mobile/com.creative.slay), [TouchArcade Dicey](https://toucharcade.com/2022/07/07/dicey-dungeons-mobile-download-out-now-ios-android-price-reunion-dlc-steam-switch-xbox/), [TouchArcade Wilmot](https://toucharcade.com/2020/05/21/wilmots-warehouse-finji-out-now-ios-puzzle-sorting/), [PCGamesInsider](https://www.pcgamesinsider.biz/news/67489/mini-metro-has-actually-sold-close-to-14m-copies/) [K] |
| BombSquad (party) | Ingyenes + „Pro” feloldás $2,99 + jegyek | $2,99 | 50M+ (Android) | A party játéknál az ingyenes belépés a döntő, mert minden résztvevőnek telepítenie kell | [AppBrain](https://www.appbrain.com/app/bombsquad/net.froemling.bombsquad) [K] |

Az összkép egyértelmű: az ingyenes belépésű címek (Polytopia, Alto Android, BombSquad, SPD, Mindustry) **5–50M** letöltést érnek el, a hasonlóan jó prémium indie-k jellemzően **~1M** körül vannak mobilon (nagyságrendi különbség).

## 4. Próbaidő mérete, szabályok, árazás

**Mekkora legyen az ingyenes rész?** Piaci gyakorlat: Ball x Pit = 1. szint, Peglin = első harmad, Deep Rock Galactic: Survivor = 2 biom, Polytopia = 4 törzs, korlátlan ideig ([comicbook.com](https://comicbook.com/gaming/news/one-of-2025s-most-addictive-new-indie-games-releases-for-mobile-and-its-free-to-try/), [Google Play Game Trials: 60 perc](https://www.pocketgamer.biz/google-play-rolls-out-game-trials-so-players-can-try-full-paid-games-before-purchasing/) [K]). Akkor nem érzik „demónak”, ha (a) az ingyenes rész önmagában lezárt, újrajátszható élmény, (b) a store-leírás első sorában és a játékban is előre szerepel, mi ingyenes, (c) a feloldás egyszeri, minden jövőbeli frissítéssel együtt (Peglin-szöveg).

| Szabály / tényező | Lényeg | Forrás |
|---|---|---|
| Apple 2.2 | „Demos, betas, trial versions” nem kerülhetnek a store-ba, ezért teljes appként kell kiadni IAP-feloldással, és a „Lite/Demo” név kerülendő | [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) |
| Apple 3.1.1 időalapú trial | $0-s non-consumable IAP „XX-day Trial” névvel; előre közölni kell a hosszt, a lezáródó tartalmat és az árat | [indiespark](https://indiespark.org/business/free-trial-app-store/), [MacStories](https://www.macstories.net/linked/apple-clarifies-app-review-guidelines-to-promote-free-trial-options/) [K] |
| Restore Purchases | Non-consumable IAP esetén kötelező gomb (különben elutasítják) | [Apple IAP](https://developer.apple.com/in-app-purchase/), [vp0](https://vp0.com/blogs/restore-purchases-button-missing-rejection-fix) [K] |
| Családi megosztás | Apple: non-consumable IAP megosztható (a fejlesztő kapcsolja be); Google Play Family Library: IAP nem osztható, csak a fizetős app | [Adapty](https://adapty.io/blog/app-purchases-family-sharing/), [Google One Help](https://support.google.com/googleone/answer/7007852?hl=en-GB) [K] |
| Regionális árazás | Apple: 900 árpont ($0,29-tól), automatikus kiegyenlítés 175 storefrontra; Google: helyi ajánlások (pl. $2,99 → ₹199 Indiában, −24%) | [Apple Newsroom](https://www.apple.com/newsroom/2022/12/apple-announces-biggest-upgrade-to-app-store-pricing-adding-700-new-price-points/), [mirava](https://www.mirava.io/blog/how-does-localized-pricing-work-in-google-play) [K] |
| Fizetős app elérhetősége | Google Playen fizetős app nem minden országban vásárolható, ingyenes igen | [Google Play Help](https://support.google.com/googleplay/answer/143779?hl=en) [K] |
| Alacsony ár | $1,99→$0,99 árcsökkentés után a Zombieville USA 2 nap alatt a #10. helyről a #5.-re lépett; RE2: $10 vs. $40 = ~54× több vásárló | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0148296320306536), [VGC](https://www.videogameschronicle.com/news/resident-evil-2-remake-has-sold-fewer-than-10000-copies-on-ios-estimates-suggest/) [K] |

## 5. „Data Not Collected” / reklámmentesség hatása

- Az Apple privacy label bevezetése után az iOS-appok heti letöltései átlagosan **−14%**-kal, bevételük −15%-kal estek, erősebben az adatgyűjtő appoknál ([Bian–Ma–Tang, FMG/LSE](https://www.fmg.ac.uk/publications/discussion-papers/supply-and-demand-data-privacy-evidence-mobile-apps) [K]).
- Ha a **fizetős** app azt jelzi, hogy nem gyűjt adatot, a rangja (és a kereslet) **nő**; hosszabb távon az adatot nem gyűjtő appok keresletet nyernek ([Garg & Telang, SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4588747) [K]).
- 1 505 fős kísérlet: a cross-app tracking címke drasztikusan csökkenti a telepítési hajlandóságot ([arXiv/NSF](https://par.nsf.gov/biblio/10581517) [K]). A „Data not collected” label tehát szerény, de mérhető előny; a hatás inkább a hátrány elkerülése, mint növekedési motor. Fontos: Firebase/Crashlytics vagy reklám-SDK nélkül legyen valóban igaz (a „no data” appok 80%-a mégis tartalmazott trackert, [arXiv 2204.03556](https://arxiv.org/pdf/2204.03556) [K]).
- A reklámmentesség („No ads”) a kulcsüzenet: a reklám a #1 panasz ([AppFollow](https://appfollow.io/blog/mobile-game-monetization) [K]), és a Ball x Pit-értékelések is kifejezetten ezt dicsérik.

## 6. Ajánlás (cél: maximális játékosszám, minimális elriasztás)

**Alapmodell: „Ingyenes, teljes értékű mag + egyszeri, nem fogyó feloldás + opcionális supporter/kozmetika”.** Mindig ingyenes letöltés (a fizetős letöltés nagyságrenddel kevesebb játékost jelent, ld. 3. fejezet), nincs reklám, nincs fogyó IAP, nincs valuta, nincs energia, összes költés limitálva (Polytopia-elv).

| Játéktípus | Mi ingyenes | Fizetős (non-consumable) | Ár (USD, regionálisan lejjebb) |
|---|---|---|---|
| **Party (Bomberman-szerű, helyi multi)** | **A teljes alapjáték**, összes mód, min. 4–6 pálya; minden résztvevő ingyen tud csatlakozni | Pályacsomagok, karakterskinek, „Supporter” | $0,99–1,99 / csomag; supporter $2,99 |
| **Tartalomintenzív puzzle / Lemmings-szerű** | Az első ~25–30% (pl. 1–2 világ, 30–40 pálya) + napi/végtelen mód, ha van | „Teljes játék” egyszeri feloldás + későbbi pályacsomagok | $2,99 (max. $3,99) |
| **Roguelite** | Teljes run-ciklus 1–2 karakterrel/biommal, korlátlan ideig (Peglin/DRG-minta) | Teljes feloldás (összes karakter/biom) | $2,99–4,99 |
| **Artillery (Worms/Pocket Tanks-szerű)** | Teljes játék alap fegyverkészlettel, helyi multi | Fegyvercsomagok (csak oldalirányú, nem P2W), skinek | $0,99–1,99 / csomag |
| **Menedzsment-szim (Pocket City-szerű)** | Teljes kampány első része / 1–2 térkép, mentéssel | Sandbox, további térképek/scenariók | $2,99–3,99 |
| **Kicsi, egymechanikás puzzle** | 100% ingyenes | Csak tip jar / kozmetika (SPD-minta) | $1,99 / $4,99 / $9,99 tier |

Kötelező elemek: store-leírás első sora: „Ingyenes kipróbálás – X pálya ingyen, a teljes játék egyszeri Y $-os vásárlás, reklám és adatgyűjtés nélkül”; az ingyenes rész végén ne zárjon ki, maradjon újrajátszható; Restore Purchases gomb; Family Sharing bekapcsolva iOS-en; Apple/Google regionális árajánlás elfogadása (vagy kézi lejjebb vitele a feltörekvő piacokon); „Data Not Collected” label (analitika-SDK nélkül).
