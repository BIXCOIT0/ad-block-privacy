# Privacy policy — PapaAnúncio

[Português](PRIVACY.md) | English

Updated November 8, 2026.

This policy describes the behavior of version 0.9.17, confirmed by the maintainer as the version published in the store and the project's current functional baseline, succeeding versions 0.9.14 and 0.9.16, which are now history. The Microsoft listing and installed version determine actual availability. Twitch header capture and token rewriting are disabled by default. Check the installed version at edge://extensions or chrome://extensions.

Public information about PapaAnúncio is available at https://github.com/BIXCOIT0/ad-block-privacy. Its purpose is to block ads and trackers and let users pause protection on individual websites. It requires no extension account and contains no browsing telemetry, analytics tools, advertising of its own or developer-operated backend. An optional support form is described below.

PapaAnúncio also uses the localized names AdChomper, ZampaAnuncios, 广告吞吞 and ऐडखाऊ. The interface follows the browser language through chrome.i18n, without a translation service, text uploads or a new stored preference. This policy remains available in Portuguese and English.

## Data used in the browser

The extension accesses the current page/frame URL and domain to determine which rules and selectors apply. The popup reads the active tab and the browser-provided matched-rule count. It does not maintain a browsing history.

The extension declares in its manifest the permissions declarativeNetRequest (applying the local network rules), declarativeNetRequestFeedback (reading observed rule actions for the counter), storage (keeping preferences and counters in the profile), scripting (registering local scripts and CSS), webNavigation (validating the source document and tab) and alarms (scheduling global pause resumption), plus the <all_urls> host permission (applying protection on any website). None of these permissions creates an account, telemetry or automatic data uploads.

Paused domains (disabledSites), compatibility settings (compatibilityDisabledSites), global pause (globalPaused and pausedUntil) and rule activation totals/status (ruleStatus and ruleStatusErrors) are stored in chrome.storage.local in the browser profile, together with the counters (counters) and the support grace-period data (installDate, donationPrompted and hasDonated, described below). Rule activation errors may include the browser API error message. The extension does not synchronize these values; the optional form below can send rule counts without complete preferences.

On supported websites, locally packaged scripts read and adapt page elements and player responses to attempt to remove advertising. The extension logic and filter lists used during browsing are included in the installed package. Filter lists are downloaded only by the developer during the project build.

## Cosmetic CSS and local messages

The cosmetic script collects tokens from DOM IDs, classes, tag names and attribute names. It sends these tokens only through chrome.runtime.sendMessage to the extension's own local service worker, which selects packaged filters and applies domain exceptions. These messages make no network requests. Received tokens are not logged or written to storage; temporary sets of already processed tokens in the page script prevent repeated work and are discarded when the context is destroyed. The worker also checks the URL/frame to validate the document and insert site-specific CSS; this does not create browsing history.

Cosmetic debugging, manually requested in the extension console, shows each frame's page origin, specific file and loaded selectors, held temporarily in the tab context. This does not confirm that a selector matched an element. These results are not automatically sent or persistently recorded; the user may view/copy the result locally.

## Onboarding page

Onboarding reads ruleStatus/globalPaused once. Its typed sequence presents local configuration; it does not run a security scan or activate rules. The image, system fonts and effects are local.

## Experimental Twitch module

The module may make additional requests directly to Twitch to obtain playback tokens and ad-free playlists. In its default anonymous mode, auxiliary token requests use credentials: omit and do not send cookies, Authorization or Client-Integrity. They may reuse the application's observed public Client-ID; session/device identifier capture is disabled by default. This does not make the connection anonymous to Twitch: Twitch still receives the IP address and the data needed for the request.

If capture is manually enabled, with allowSessionHeaders: false the fetch wrapper captures only client-id, client-session-id, client-version and x-device-id when available. The capture does not read Authorization or Client-Integrity; those values are not cached by the extension, forwarded over BroadcastChannel or stored by the worker. Auxiliary token requests use credentials: omit. If an anonymous token fails, the module does not try complete mode; without a safe backup, it preserves the original playlist. This refers to auxiliary requests, separate from normal page requests described below.

In version 0.9.17, headerCapture, adMute and tokenRewrite default to off; workerFilter, backup, playlistFilter, adMetrics and observePlayback default to on; backupAnonymous defaults to on and allowSessionHeaders defaults to off. The module transiently reads HLS playlists received through fetch and XHR in the page/worker to remove segments and metadata classified as ads, preserving the original when remaining media is unsafe. It may request a backup of up to 480p directly from Twitch during ads and returns to the original variant afterward. Media URLs and required backup tokens are held only in memory, not extension storage or requests to the developer. Normal page requests preserve their own headers and credentials: Authorization/Client-Integrity values are not extracted by the filter but may still be sent by the browser to Twitch as specified by the page. The previous token rewrite remains a disabled manual source option.

GQL observation (observePlayback=true) reads only the application's public Client-ID and the native live response signature to associate the channel with its Usher master. The original request and response are preserved. These fields are held in a private Map of up to 32 entries per context, valid for 60 seconds; expired entries are removed on the next access/observation or when the context closes. They are not placed in globals, sessionStorage, chrome.storage, logs or BroadcastChannel. The native token value is not retained. When the signature matches the same channel's Usher URL, the Client-ID may be reused in anonymous auxiliary requests to Twitch itself. This observation does not read Authorization/Client-Integrity; headerCapture remains disabled. This context is not shared between frames/workers. Missing, failed or expired observations fall back to the configured public Client-ID. This does not make requests anonymous to Twitch.

Isolated GQL operations named VideoAdTrack/AdReport may receive an empty local JSON response without sending those requests to Twitch. Mixed batches, unsupported formats and other metrics may still be sent. This does not guarantee preventing detection or all tracking. Metric request bodies are not logged. Filtering and synthetic XHR events can be detected by the site. There is no public proxy; effectiveness, quality and playback are not guaranteed.

The allowSessionHeaders flag exists only in source code for development, defaults to false and has no interface or chrome.storage setting. Manually changing it to true, also enabling headerCapture to capture headers, and reloading allows these headers to be captured and permits complete-mode requests using credentials: same-origin (or complete mode directly if backupAnonymous is false). In that development mode, values and tokens remain in memory and may be sent in auxiliary requests to Twitch itself, not to the developer. Playlists and segments are still requested from Twitch and its returned media addresses. Twitch's privacy policy applies to those connections; no third-party proxy is used.

Twitch debugging is off by default. When manually enabled by the user, it writes diagnostics such as channel name, player type, segment counts and request duration to the local console. With session access disabled, GQL diagnostics include status only, not response bodies or errors messages. In the development session mode, diagnostics retain redaction of tokens and known header values. Logs are not sent automatically.

## Global pause, counters and activity

Global pause stores globalPaused (state) and pausedUntil (resume time or null) in chrome.storage.local. The alarms permission schedules resumption while the popup is closed; browser suspension may delay an alarm. Startup checks expired pauses. disabledSites remains independent from global pause.

counters stores total, today, day (local date) and days, a local map limited to seven dates: today and the previous six local days. These are rule actions observed by queries when opening the popup, not a complete count of ads or unique requests. Repeated observations are deduplicated with temporary tab/rule/time markers in storage.session (matchWatermarks, up to 1,000 tabs). Unobserved events, API limits, timestamp ties and restarts can affect counts. Today resets by local date; the accumulated value stays in the profile. No dates are invented for legacy totals without daily history.

storage.session also holds pageObservedCounts: up to eight documents per tab and up to 128 tabs, with document IDs, timestamps/time origins and counts for navigation and history restoration (BFCache). Closing the tab removes its entry. This state supports the displayed counter and contains neither URLs nor a permanent browsing history. A temporary pendingMatchBatch allows interrupted counter writes to recover without duplication.

storage.session also holds activity: only the three latest confirmed pause/resume actions, with an action code and timestamp, without domains or URLs. The browser clears session data at session end; nothing is sent to the developer.

Pausing changes network rules immediately and removes registrations for future navigations. Scripts/CSS already running in other tabs need another load; popup actions reload only the current tab. Alarm resumption attempts to reload only the active HTTP/HTTPS tab.

## Visual update and local notifications

“Threats neutralized” is a visual label for observed rule actions, not a security assessment. There is no malware scan or confirmation of threats. In an unpacked installation, when the browser provides onRuleMatchedDebug, the worker checks local block rules and sends only tabId and a count to the extension UI. The code does not read event URLs or headers. tabLiveCounts and liveRequestKeys are temporary storage.session values, limited to the latest 128 tabs and up to 256 request/rule keys per tab; they are cleared on tab closure or session end. These are browser-generated IDs, not Twitch credentials.

Store installations do not provide that immediate event. The popup queries getMatchedRules on opening and every 35 seconds while visible, backing off on errors or quota limits. These queries also update Today/Total. There is no periodic query with the popup closed and nothing is sent to developer servers. Network blocking works without the counter being open.

## Local anti-adblock resources

This version includes original minimal advertising/analytics API stubs and packaged empty responses. When enabled for a validated domain, browser redirect rules replace configured scripts/GET test requests with local files without sending those requests to advertising servers. The GPT/IMA profile is enabled for www.xfilme.net, www.xfilme.org, formadeganhardinheiro.net, melhoresreceitas.blog and subsbr.net after owner confirmation, including five control sites without problems. On www.baixetorrent.org, www.baixetorrentshd.org and www.baixetorrentshd.com, the same profile replaces the configured adsbygoogle script/probes and keeps only specific baits off screen with minimum dimensions and opacity 1; real ads outside those selectors are not revealed. On planetadosfilmes.com, the profile replaces the configured adsbygoogle script with the local stub, without baits. The owner confirmed that the warning was resolved and navigation worked on www.baixetorrentshd.org. The coverage for www.baixetorrent.org and www.baixetorrentshd.com shares the same profile as .org and was verified in the project's synthetic tests; this does not claim validation in every real-world scenario. Redirects are restricted to configured resources and domains; this does not represent general website coverage. Unmatched requests remain subject to other rules and normal browser behavior.

Stub files declared in web_accessible_resources use use_dynamic_url: true and are restricted to the origins declared in the manifest (local test origins, www.xfilme.net, www.xfilme.org, formadeganhardinheiro.net, melhoresreceitas.blog, subsbr.net, www.baixetorrentshd.org, www.baixetorrent.org, www.baixetorrentshd.com and planetadosfilmes.com). Dynamic URLs do not guarantee hiding the extension: allowed websites may, in theory, probe or observe accessible resources and substitution effects. The Chromium 111 schema accepts this option; its effective behavior has not been verified here on minimum Chrome/Edge versions. There is no attempt to bypass Edge Tracking Prevention or server-side blocker verification.

Local domain profiles may apply offscreen CSS for simple, specific bait selectors validated per profile, constant flags, property read/write interruption, timer suppression by literal text and local responses to configured fetch calls. These are specific interventions: stubs do not implement full SDKs and may be incompatible with unvalidated websites. They do not affect the YouTube/Twitch modules. Profile installation failures should not interrupt the page; explicitly configured property interruptions are intentional and may interrupt detector code accessing those properties.

Anti-adblock debugging is manually requested in the service worker console using antiAdblockDebug(tabId). It queries frames and up to 500 observed rule records for that tab at that moment, showing reported stubs, bait effects, scriptlet actions and a summary of blocking rules, without request URLs, storage or network transmission. MAIN-world reports can be forged by the page; debugging is not security evidence. Temporary state ends when the document reloads/closes. There is no remote code, developer-side collection, new dependency or new API permission.

Compatibility adjustments run internally on eligible HTTP/HTTPS pages, excluding YouTube/Twitch. The dedicated popup control was removed in 0.9.8 at the owner’s request. In addition to the three specific profiles, a general layer covers one synthetic bait signature and two exact image probes. Adjustments remain enabled by default; legacy compatibilityDisabledSites preferences stay local and are preserved. Global or site pause suspends these adjustments. Scripts/CSS already installed may require a tab reload to disappear. Local domain exceptions can cover subdomains.


The general layer uses two GET redirects exclusively for image requests to the configured Google paths with a numeric _dns_ parameter and no other parameters. The response is a packaged transparent 1×1 SVG image without scripts or external content. Actual advertising scripts, fetch/XHR, POST and other trackers do not receive this general exception. General CSS targets only an empty div with the abd-ext-bait- ID prefix and all five expected detector classes, keeping it off screen. It does not blindly remove warning dialogs or unlock server-side content.

Only antiadblock/probes/empty.svg becomes accessible to all HTTP/HTTPS origins, with use_dynamic_url:true. This expansion may allow more websites to probe for the extension; dynamic URLs do not guarantee hiding it. JavaScript stubs remain restricted to profile domains. Pauses and the local compatibility preference suspend corresponding interventions. Coverage depends on recognized patterns, without guarantees for every site or detector version.


## Black Box and optional support form

The Black Box uses a restricted technical format (technical-codes-v1): console.error and console.warn from extension code, HTTP/HTTPS pages and MAIN modules are observed after the scripts are injected, and exceptions, unhandled rejections and resource/media failures may also produce events. Page console.log is not intercepted. Messages and objects are inspected transiently to recognize codes from a fixed list, then discarded; they are not stored or sent as free-form text. Unrecognized errors become a generic category. Names, email addresses, phone numbers, cookies, tokens, form contents, URLs, channel/video names and full stacks are not copied. File names must be known packaged extension files; page errors do not retain their paths. Type, timestamp, category, technical source and bounded line/column numbers may remain. It keeps up to 50 recent entries in chrome.storage.session, under blackboxLogs.

The service worker combines records in chrome.storage.session under blackboxLogs, with centralized writing and no storage.local for these logs. This is not a permanent history: the browser discards the session when it ends or the extension reloads. Each component also has bounded local memory. Page content is not copied; only the technical codes of events are kept, as described above. Isolated content scripts ignore external errors without a proven extension origin. The module does not retrospectively read the Console. Original console functions and existing error handlers continue to work.

Optional diagnostics may also include build: a SHA-256 identity of the packaged extension content. It identifies the code package, not a user or device. This field is not sent without authorized diagnostics. When the preview is reviewed, submission uses that same diagnostic snapshot; unchecking and checking the attachment again allows a new snapshot.

History remains limited to 50 entries in storage.session. Page capture and the context bridge have rate and size limits. A small MAIN history already converted to codes allows the isolated receiver to connect; no original message text crosses that bridge. Page events are unauthenticated and may be forged: they are diagnostic clues, not proof of origin or security. Internal retry IDs are not exported. Records from older versions are converted to the restricted format when read by the new recorder; fields are validated again before preview and submission. Already-open pages must be reloaded to use the updated scripts.

Report a Problem is a dedicated page. Attach diagnostic data automatically is unchecked by default, but sending only happens after clicking Send Report; unchecking excludes diagnostics and logs from the request. Optional data includes version, API availability, rule counts and console_logs. If no records exist, the field states that no errors were detected in the session. A preview is available before sending. Unchecking attachments does not delete or stop local session recording.

This package is configured to send HTTPS POST to Web3Forms for delivery to the developer. This service receives typed text, selected attachments and normal connection data such as IP; its policies and configured retention apply. Free text can contain information the user chooses to write. When the form is opened from the popup, the source tab’s hostname is prefilled in Problem website. This visible field can be edited or cleared; if left filled, it is sent as site only when Send Report is clicked, independently of log attachments. Only the hostname is sent, without path, port, query parameters or fragment. The form can also be opened directly and filled manually. The report does not add browsing history, the full tab URL, complete preferences, headers or session tokens. Automatic records use only fixed technical codes, but the free text you type and the reported hostname may still contain information you do not wish to share. Review the preview and do not send secrets. Reports are not sent in the background, periodically or automatically.

In version 0.9.17, Web3Forms remains configured using the public form key supplied by the maintainer. Its policy is https://web3forms.com/privacy. Requests omit cookies and referrers; logs and diagnostics are formatted JSON text. The dedicated page replaces the old Gmail panel, which remains removed.

Attaching diagnostics remains optional and initially unchecked. Preview and submission use the same snapshot; no diagnostics are transmitted without clicking Send report. Restricting automatic attachments does not anonymize the text the user types, the optional hostname they choose to submit or normal connection data received by Web3Forms, such as IP addresses. The provider policy still applies. Without configuring the optional integration below, Web3Forms remains the only reporting destination. The interface may also show today and the previous six days using a local map bounded to seven dates, without inventing dates for undated legacy totals.

### Optional private GitHub integration

The maintainer can configure the extension to also record reports in a private GitHub repository through a Cloudflare Workers service. It is disabled by default and requires hosting and server-side credentials. When enabled, the form discloses these destinations before submission. After email delivery through Web3Forms is confirmed, the same description, optional hostname and authorized attachments are forwarded through Cloudflare to the private repository. The GitHub token is not included in the extension, and the server verifies that the repository is private before creating an issue. People and integrations authorized in the repository can access reports; these are not public issues.

Cloudflare processes the body and connection metadata under its policy (https://www.cloudflare.com/privacypolicy/). The code transiently uses the IP address to derive an HMAC key for rate limiting, without copying it into the issue or receipt. This key is pseudonymous. Receipts in KV storage contain only a random per-report ID, repository association and normalized-content hash, expiring after 24 hours. The code does not log bodies or credentials, and the configuration disables application observability. Account settings and provider policies also apply. Issues are retained according to repository administration until deleted; there is no automatic issue deletion period. GitHub policy: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement.

If email arrives but GitHub fails, the form reports partial delivery. Retrying with unchanged fields on the same page attempts GitHub only. Closing or reloading loses this state; network failures and concurrency can still produce duplicates. This integration does not anonymize typed text or the chosen hostname and does not submit reports without a button click. Preparing it does not mean it is enabled: in version 0.9.17 it is disabled by default.

### Optional source-tab technical snapshot

When Report a problem is opened from the popup, the form can request a technical snapshot of the source tab after the user authorizes diagnostic attachments and opens the preview or submits. The internal tab ID is used only to locate that page and is not transmitted to the provider. The worker checks hostname and document identity before/after; a closed tab or changed document produces an unavailable status. Other tabs are not scanned and there is no periodic capture.

The snapshot contains fixed fields: document loading/visibility state; player/ad presence and markers; whether media is paused, ended, seeking, muted, near its beginning, has finite duration or has a source; bounded playback rate and numeric state/error codes; limited counts of Skip controls, ad elements, known detector/notices, baits and recognized advertising frames. Page text, titles or video names, form values, cookies, tokens, site storage, full URLs and media origins are not read/sent. Browser family and major version are included without the full user agent.

Protection flags, a matching profile and extension-module registration flags may accompany the snapshot. On YouTube, the module exposes its revision and the latest local transport sample: initial-filter and response counts, transport/processing durations in milliseconds, buffered byte count and the technical decision code. MAIN/DOM data can be forged by the site; they are clues, not authenticated evidence. When the API permits, the snapshot contains up to 30 rule ID/ruleset pairs observed only in the source tab during the last minute, without request URLs or individual request times. Quota or unavailable APIs produce an explicit status. Preview and submission share the same snapshot, which the user can refresh. Console errors are not required for an advertising problem to exist.

## Sharing and controls

We do not sell data or share it with advertisers or analytics services. The Twitch requests described above serve video playback only. GitHub help/privacy links are opened only when you choose to open them; GitHub's policies apply to that visit.

You can pause protection through the popup. The current tab reloads to apply the change. Reload other open tabs for that site as well to remove scripts that are already running. Uninstalling the extension removes its local profile storage. If you manually enabled debugging, remove its key with localStorage.removeItem('bloqueioPessoal_twitchDebug') in the Twitch console. That key belongs to the website's storage, outside extension storage.

Updates installed through the store are distributed by Microsoft Edge Add-ons and are subject to Microsoft's policies. The extension has no remote updater of its own.

## Contact

Privacy questions or requests: https://github.com/BIXCOIT0/ad-block-privacy/issues. Issues are public; do not post tokens, passwords, private URLs or personal information.

## YouTube and donations

In version 0.9.17, the old YouTube recovery monitor and automatic reloads were removed: there is no 15-second stalled-video monitor, no bypassCache reload and no youtubeRecoveryAttempts control. The YouTube module only filters known advertising descriptors in initial player data and recognized get_watch responses, within the browser. It does not clear site data and does not control Play, pause, position, speed, volume or Media Session. This processing does not send those data to the developer or create a video history.

installDate and donationPrompted are stored in extension storage.local for the seven-day grace period and dismissing the support request. Legacy settings, including hasDonated, are preserved. Clicking Pix opens https://bixcoit0.github.io/apoio-AD-BLOCK/ under that destination's policies. Opening the page does not verify or confirm a payment.

## Version history and limits

Version 0.9.14 kept textual Black Box records and used the YouTube recovery monitor. Candidate 0.9.16 introduced the restricted technical format (technical-codes-v1) with up to 50 entries in chrome.storage.session (blackboxLogs), pageObservedCounts with up to eight documents per tab and up to 128 tabs, the temporary pendingMatchBatch and the build field with the package SHA-256 hash; report delivery remains through Web3Forms. Version 0.9.17, published in the store, incorporates those changes and removes the recovery monitor and automatic reloads.

This policy describes the behavior of 0.9.17; earlier versions are history. Nothing here guarantees blocking every ad or avoiding blocker detection: YouTube and Twitch behavior may change with those services, and the Twitch module is experimental.
