# Privacy policy — PapaAnúncio

[Português](PRIVACY.md) | English

Updated October 29, 2026.

This policy describes version 0.7.3, submitted for review. In the previously published version 0.7.1, a failed anonymous token could trigger an attempt using complete session headers (including Authorization and Client-Integrity when available), held in memory and sent only to Twitch itself. This attempt is disabled by default in 0.7.3. Check the installed version at edge://extensions or chrome://extensions.

PapaAnúncio is the browser extension from the AD-BLOCK project maintained at https://github.com/xdbixcoito-hub/AD-BLOCK. Its purpose is to block ads and trackers and let users pause protection on individual websites. It requires no extension account and contains no telemetry, analytics tools, advertising of its own or developer-operated backend.

## Data used in the browser

The extension accesses the current page/frame URL and domain to determine which rules and selectors apply. The popup reads the active tab and the browser-provided matched-rule count. It does not maintain a browsing history.

Paused domains (disabledSites) and rule activation totals/status (ruleStatus and ruleStatusErrors) are stored in chrome.storage.local in the browser profile. Rule activation errors may include the browser API error message. The extension does not synchronize these values or send them to the developer.

On supported websites, locally packaged scripts read and adapt page elements and player responses to attempt to remove advertising. The extension logic and filter lists used during browsing are included in the installed package. Filter lists are downloaded only by the developer during the project build.

## Experimental Twitch module

The module may make additional requests directly to Twitch to obtain playback tokens and ad-free playlists. In its default anonymous mode, token requests omit cookies, Authorization and Client-Integrity. They may reuse Twitch's Client-ID and session/device identifiers. This does not make the connection anonymous to Twitch: Twitch still receives the IP address and the data needed for the request.

In the distributed configuration (allowSessionHeaders: false), the fetch wrapper captures only client-id, client-session-id, client-version and x-device-id when available. The capture does not read Authorization or Client-Integrity; those values are not cached by the extension, forwarded over BroadcastChannel or stored by the worker. Auxiliary token requests use credentials: omit. If an anonymous token fails, the module does not try complete mode; without a safe backup, it preserves the original playlist. This does not modify authenticated requests normally made by the Twitch page itself.

The allowSessionHeaders flag exists only in source code for development, defaults to false and has no interface or chrome.storage setting. Manually changing it to true and reloading allows these headers to be captured again and permits complete-mode requests using credentials: same-origin (or complete mode directly if backupAnonymous is false). In that development mode, values and tokens remain in memory and may be sent in auxiliary requests to Twitch itself, not to the developer. Playlists and segments are still requested from Twitch and its returned media addresses. Twitch's privacy policy applies to those connections; no third-party proxy is used.

Twitch debugging is off by default. When manually enabled by the user, it writes diagnostics such as channel name, player type, segment counts and request duration to the local console. With session access disabled, GQL diagnostics include status only, not response bodies or errors messages. In the development session mode, diagnostics retain redaction of tokens and known header values. Logs are not sent automatically.

## Sharing and controls

We do not sell data or share it with advertisers or analytics services. The Twitch requests described above serve video playback only. GitHub help/privacy links are opened only when you choose to open them; GitHub's policies apply to that visit.

You can pause protection through the popup. The current tab reloads to apply the change. Reload other open tabs for that site as well to remove scripts that are already running. Uninstalling the extension removes its local profile storage. If you manually enabled debugging, remove its key with localStorage.removeItem('bloqueioPessoal_twitchDebug') in the Twitch console. That key belongs to the website's storage, outside extension storage.

Updates installed through the store are distributed by Microsoft Edge Add-ons and are subject to Microsoft's policies. The extension has no remote updater of its own.

## Contact

Privacy questions or requests: https://github.com/xdbixcoito-hub/ad-block-privacy/issues. Issues are public; do not post tokens, passwords, private URLs or personal information.
