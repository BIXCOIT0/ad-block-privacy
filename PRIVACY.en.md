# Privacy policy — PapaAnúncio

[Português](PRIVACY.md) | English

Updated October 29, 2026.

PapaAnúncio is the browser extension from the AD-BLOCK project maintained at https://github.com/xdbixcoito-hub/AD-BLOCK. Its purpose is to block ads and trackers and let users pause protection on individual websites. It requires no extension account and contains no telemetry, analytics tools, advertising of its own or developer-operated backend.

## Data used in the browser

The extension accesses the current page/frame URL and domain to determine which rules and selectors apply. The popup reads the active tab and the browser-provided matched-rule count. It does not maintain a browsing history.

Paused domains (disabledSites) and rule activation totals/status (ruleStatus and ruleStatusErrors) are stored in chrome.storage.local in the browser profile. Rule activation errors may include the browser API error message. The extension does not synchronize these values or send them to the developer.

On supported websites, locally packaged scripts read and adapt page elements and player responses to attempt to remove advertising. The extension logic and filter lists used during browsing are included in the installed package. Filter lists are downloaded only by the developer during the project build.

## Experimental Twitch module

The module may make additional requests directly to Twitch to obtain playback tokens and ad-free playlists. In its default anonymous mode, token requests omit cookies, Authorization and Client-Integrity. They may reuse Twitch's Client-ID and session/device identifiers. This does not make the connection anonymous to Twitch: Twitch still receives the IP address and the data needed for the request.

If an anonymous token request fails, the module can retry once using the complete session headers made available by the Twitch page, including authorization/integrity headers when present. The extension keeps these values and tokens in memory for this purpose only. It does not write them to storage or files, send them to the developer or use third-party proxies. Playlists and segments are requested from Twitch and the media addresses it returns. Twitch's privacy policy continues to apply to these connections.

Twitch debugging is off by default. When manually enabled by the user, it writes diagnostics such as channel name, player type, segment counts and request duration to the local console. The code redacts token and header values in diagnostics. Logs are not sent automatically.

## Sharing and controls

We do not sell data or share it with advertisers or analytics services. The Twitch requests described above serve video playback only. GitHub help/privacy links are opened only when you choose to open them; GitHub's policies apply to that visit.

You can pause protection through the popup. The current tab reloads to apply the change. Reload other open tabs for that site as well to remove scripts that are already running. Uninstalling the extension removes its local profile storage. If you manually enabled debugging, remove its key with localStorage.removeItem('bloqueioPessoal_twitchDebug') in the Twitch console. That key belongs to the website's storage, outside extension storage.

Updates installed through the store are distributed by Microsoft Edge Add-ons and are subject to Microsoft's policies. The extension has no remote updater of its own.

## Contact

Privacy questions or requests: https://github.com/xdbixcoito-hub/ad-block-privacy/issues. Issues are public; do not post tokens, passwords, private URLs or personal information.
