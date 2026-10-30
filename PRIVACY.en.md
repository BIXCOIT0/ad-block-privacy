# Privacy policy — PapaAnúncio

[Português](PRIVACY.md) | English

Updated October 30, 2026.

This policy describes version 0.9.3 prepared for store submission; this does not confirm store submission or publication. Twitch header capture and token rewriting are disabled by default. Check the installed version at edge://extensions or chrome://extensions.

Public information about PapaAnúncio is available at https://github.com/xdbixcoito-hub/ad-block-privacy. Its purpose is to block ads and trackers and let users pause protection on individual websites. It requires no extension account and contains no telemetry, analytics tools, advertising of its own or developer-operated backend.

PapaAnúncio also uses the localized names AdChomper, ZampaAnuncios, 广告吞吞 and ऐडखाऊ. The interface follows the browser language through chrome.i18n, without a translation service, text uploads or a new stored preference. Diagnostics show the localized name. This policy remains available in Portuguese and English.

## Data used in the browser

The extension accesses the current page/frame URL and domain to determine which rules and selectors apply. The popup reads the active tab and the browser-provided matched-rule count. It does not maintain a browsing history.

Paused domains (disabledSites) and rule activation totals/status (ruleStatus and ruleStatusErrors) are stored in chrome.storage.local in the browser profile. Rule activation errors may include the browser API error message. The extension does not synchronize these values or send them to the developer.

On supported websites, locally packaged scripts read and adapt page elements and player responses to attempt to remove advertising. The extension logic and filter lists used during browsing are included in the installed package. Filter lists are downloaded only by the developer during the project build.

## Cosmetic CSS and local messages

The cosmetic script collects tokens from DOM IDs, classes, tag names and attribute names. It sends these tokens only through chrome.runtime.sendMessage to the extension's own local service worker, which selects packaged filters and applies domain exceptions. These messages make no network requests. Received tokens are not logged or written to storage; temporary sets of already processed tokens in the page script prevent repeated work and are discarded when the context is destroyed. The worker also checks the URL/frame to validate the document and insert site-specific CSS; this does not create browsing history.

Cosmetic debugging, manually requested in the extension console, shows each frame's page origin, specific file and loaded selectors, held temporarily in the tab context. This does not confirm that a selector matched an element. These results are not automatically sent or persistently recorded; the user may view/copy the result locally. This debug feature is separate from the popup diagnostic preview described below.

## Optional diagnostics

The popup offers a local diagnostic preview, prepared only when its panel is expanded. It contains the version, API availability and rule counts, using explicitly selected fields. It excludes websites, history, URLs, error messages, headers, tokens and session data. Nothing is sent automatically. Clicking Copy diagnostics replaces the clipboard contents; you choose whether and where to share it. If automatic copying is unavailable, you can copy the selected text manually. Diagnostics are not saved in extension storage.

## Onboarding page

Onboarding reads ruleStatus/globalPaused once and, where the API exists, toolbar pinning status. Its typed sequence presents local configuration; it does not run a security scan or activate rules. The image, system fonts and effects are local.

## Experimental Twitch module

The module may make additional requests directly to Twitch to obtain playback tokens and ad-free playlists. In its default anonymous mode, auxiliary token requests use credentials: omit and do not send cookies, Authorization or Client-Integrity. They may reuse the application's observed public Client-ID; session/device identifier capture is disabled by default. This does not make the connection anonymous to Twitch: Twitch still receives the IP address and the data needed for the request.

If capture is manually enabled, with allowSessionHeaders: false the fetch wrapper captures only client-id, client-session-id, client-version and x-device-id when available. The capture does not read Authorization or Client-Integrity; those values are not cached by the extension, forwarded over BroadcastChannel or stored by the worker. Auxiliary token requests use credentials: omit. If an anonymous token fails, the module does not try complete mode; without a safe backup, it preserves the original playlist. This refers to auxiliary requests, separate from normal page requests described below.

In 0.9.3, headerCapture, adMute and tokenRewrite default to off; workerFilter, backup, playlistFilter and adMetrics default to on. The module transiently reads HLS playlists received through fetch and XHR in the page/worker to remove segments and metadata classified as ads, preserving the original when remaining media is unsafe. It may request a backup of up to 480p directly from Twitch during ads and returns to the original variant afterward. Media URLs and required backup tokens are held only in memory, not extension storage or requests to the developer. Normal page requests preserve their own headers and credentials: Authorization/Client-Integrity values are not extracted by the filter but may still be sent by the browser to Twitch as specified by the page. The previous token rewrite remains a disabled manual source option.

GQL observation (observePlayback=true) reads only the application's public Client-ID and the native live response signature to associate the channel with its Usher master. The original request and response are preserved. These fields are held in a private Map of up to 32 entries per context, valid for 60 seconds; expired entries are removed on the next access/observation or when the context closes. They are not placed in globals, sessionStorage, chrome.storage, logs or BroadcastChannel. The native token value is not retained. When the signature matches the same channel's Usher URL, the Client-ID may be reused in anonymous auxiliary requests to Twitch itself. This observation does not read Authorization/Client-Integrity; headerCapture remains disabled. This context is not shared between frames/workers. Missing, failed or expired observations fall back to the configured public Client-ID. This does not make requests anonymous to Twitch.

Isolated GQL operations named VideoAdTrack/AdReport may receive an empty local JSON response without sending those requests to Twitch. Mixed batches, unsupported formats and other metrics may still be sent. This does not guarantee preventing detection or all tracking. Metric request bodies are not logged. Filtering and synthetic XHR events can be detected by the site. There is no public proxy; effectiveness, quality and playback are not guaranteed.

The allowSessionHeaders flag exists only in source code for development, defaults to false and has no interface or chrome.storage setting. Manually changing it to true, also enabling headerCapture to capture headers, and reloading allows these headers to be captured and permits complete-mode requests using credentials: same-origin (or complete mode directly if backupAnonymous is false). In that development mode, values and tokens remain in memory and may be sent in auxiliary requests to Twitch itself, not to the developer. Playlists and segments are still requested from Twitch and its returned media addresses. Twitch's privacy policy applies to those connections; no third-party proxy is used.

Twitch debugging is off by default. When manually enabled by the user, it writes diagnostics such as channel name, player type, segment counts and request duration to the local console. With session access disabled, GQL diagnostics include status only, not response bodies or errors messages. In the development session mode, diagnostics retain redaction of tokens and known header values. Logs are not sent automatically.

## Global pause, counters and activity

Global pause stores globalPaused (state) and pausedUntil (resume time or null) in chrome.storage.local. The alarms permission schedules resumption while the popup is closed; browser suspension may delay an alarm. Startup checks expired pauses. disabledSites remains independent from global pause.

counters stores total, today and day (local date). These are rule actions observed by queries when opening the popup, not a complete count of ads or unique requests. Repeated observations are deduplicated with temporary tab/rule/time markers in storage.session (matchWatermarks, up to 1,000 tabs). Unobserved events, API limits, timestamp ties and restarts can affect counts. Today resets by local date; the accumulated value stays in the profile.

storage.session also holds activity: only the three latest confirmed pause/resume actions, with an action code and timestamp, without domains or URLs. The browser clears session data at session end; nothing is sent to the developer. Voluntary diagnostics still exports only explicitly permitted fields.

Pausing changes network rules immediately and removes registrations for future navigations. Scripts/CSS already running in other tabs need another load; popup actions reload only the current tab. Alarm resumption attempts to reload only the active HTTP/HTTPS tab.

## Visual update and local notifications

“Threats neutralized” is a visual label for observed rule actions, not a security assessment. There is no malware scan or confirmation of threats. In an unpacked installation, when the browser provides onRuleMatchedDebug, the worker checks local block rules and sends only tabId and a count to the extension UI. The code does not read event URLs or headers. tabLiveCounts and liveRequestKeys are temporary storage.session values, limited to the latest 128 tabs and up to 256 request/rule keys per tab; they are cleared on tab closure or session end. These are browser-generated IDs, not Twitch credentials.

Store installations do not provide that immediate event. The popup queries getMatchedRules on opening and every 35 seconds while visible, backing off on errors or quota limits. These queries also update Today/Total. There is no periodic query with the popup closed and nothing is sent to developer servers. Network blocking works without the counter being open.

## Local anti-adblock resources — 0.9.3

This version includes original minimal advertising/analytics API stubs and packaged empty responses. When enabled for a validated domain, browser redirect rules replace configured scripts/GET test requests with local files without sending those requests to advertising servers. The GPT/IMA profile is enabled for www.xfilme.net and subsbr.net after owner confirmation, including five control sites without problems. On www.baixetorrentshd.org, a profile replaces the configured adsbygoogle script/probes and keeps only specific baits off screen with minimum dimensions and opacity 1; real ads outside those selectors are not revealed. The owner confirmed that the warning was resolved and navigation worked. Redirects are restricted to configured resources and domains; this does not represent general website coverage. Unmatched requests remain subject to other rules and normal browser behavior.

Stub files declared in web_accessible_resources use use_dynamic_url: true and are restricted to the origins declared in the manifest (local test origins, www.xfilme.net, subsbr.net and www.baixetorrentshd.org). Dynamic URLs do not guarantee hiding the extension: allowed websites may, in theory, probe or observe accessible resources and substitution effects. The Chromium 111 schema accepts this option; its effective behavior has not been verified here on minimum Chrome/Edge versions. There is no attempt to bypass Edge Tracking Prevention or server-side blocker verification.

Local domain profiles may apply offscreen CSS for simple, specific bait selectors validated per profile, constant flags, property read/write interruption, timer suppression by literal text and local responses to configured fetch calls. These are specific interventions: stubs do not implement full SDKs and may be incompatible with unvalidated websites. They do not affect the YouTube/Twitch modules. Profile installation failures should not interrupt the page; explicitly configured property interruptions are intentional and may interrupt detector code accessing those properties.

Anti-adblock debugging is manually requested in the service worker console using antiAdblockDebug(tabId). It queries frames at that moment and shows reported stubs, bait effects, scriptlet actions and setup time, without storage or network transmission. MAIN-world reports can be forged by the page; debugging is not security evidence. Temporary state ends when the document reloads/closes. There is no remote code, developer-side collection, new dependency or new API permission.

## Sharing and controls

We do not sell data or share it with advertisers or analytics services. The Twitch requests described above serve video playback only. GitHub help/privacy links are opened only when you choose to open them; GitHub's policies apply to that visit.

You can pause protection through the popup. The current tab reloads to apply the change. Reload other open tabs for that site as well to remove scripts that are already running. Uninstalling the extension removes its local profile storage. If you manually enabled debugging, remove its key with localStorage.removeItem('bloqueioPessoal_twitchDebug') in the Twitch console. That key belongs to the website's storage, outside extension storage.

Updates installed through the store are distributed by Microsoft Edge Add-ons and are subject to Microsoft's policies. The extension has no remote updater of its own.

## Contact

Privacy questions or requests: https://github.com/xdbixcoito-hub/ad-block-privacy/issues. Issues are public; do not post tokens, passwords, private URLs or personal information.
