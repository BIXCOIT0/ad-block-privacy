# Help — AdChomper

[Português](SUPPORT.md) · [Home](README.md) · [Privacy](PRIVACY.en.md)

## Install and check the version

1. Install from the [official Edge Add-ons listing](https://microsoftedge.microsoft.com/addons/detail/papaan%C3%BAncio/dkhdokbphfkndloeabmdpniaedpmnahl).
2. Open the Edge extensions menu and select AdChomper. Its Portuguese name is PapaAnúncio.
3. Check the version at `edge://extensions`. Type this address into the browser address bar. If an update is available, use the Edge controls.

The published version reported by the owner and current functional baseline is 0.9.17, succeeding versions 0.9.14 and 0.9.16. This guide describes the controls of version 0.9.17 and does not require third-party code.

## Pause and resume

- **Current site:** open the popup on the desired tab and use the round power button. Check the displayed domain and protection state. Use the same button to resume.
- **All sites:** select **Pause all** and choose 15 minutes, 1 hour or until you resume manually. Use **Resume all** to reactivate protection before the time expires.
- A global pause takes precedence over the per-site control. Check both states if protection does not resume.
- Reload the page after changing protection to test the new state. Browser internal pages, the store and other restricted pages may not allow the extension to operate.

## A site stopped working or detected the blocker

1. Note the domain, extension and Edge versions, and what you were trying to do.
2. Pause protection only on that site and reload the page. Compare the result. Resume protection after the test if desired.
3. If the problem continues, check your connection and whether another blocking or privacy extension interferes. Change one thing at a time and restore your preferences afterward.
4. Report the steps and comparison result. A detection message does not establish that this extension caused it.

Clearing all browser data is not a standard troubleshooting step: it can sign you out and delete preferences. Do not provide passwords or disable browser protections to obtain support.

## YouTube and Twitch

If you see an ad, black screen, playback lag or quality drop, say whether it happened when opening the video/stream, during playback, or after switching videos/channels. For Twitch, include the public channel and approximate time with time zone when possible. Describe whether the ad disappeared on its own and whether pausing protection changed the behavior.

Blocking depends on changes to these services and may not remove every ad. The Twitch module is experimental and may temporarily lower video quality. Avoiding blocker detection is not guaranteed.

## Understand the count

The popup number represents rule actions observed by the browser. One rule can act multiple times; this is not an exact count of ads or threats. The tab count and daily/overall totals cover different scopes. A loading or unavailable indicator does not mean protection is off; also check the protection state.

## Report with privacy

1. Open **Report a problem** from the affected tab's popup.
2. Check the site field. It sends only the domain; you can correct or clear it. Do not put private URLs in the report text.
3. Describe the steps, expected and observed behavior, version and browser. You can send a report without diagnostics.
4. If you choose to attach diagnostics, open **Review diagnostic data** and inspect the contents. The optional attachment uses only permitted technical codes and fields: up to 50 recent records in a restricted technical format and the optional technical snapshot of the source tab since loading with the current scripts, without storing original console text or objects; unknown errors appear as a generic category, and earlier console history or every internal browser message is not recovered. If there is anything in the preview you do not want to share, uncheck the attachment and describe the issue without those data. The free text you type and the optional hostname still require your review.
5. Clicking **Send report** sends the selected content through Web3Forms for delivery to the developer. If sending fails, check your connection and try again; you do not need to publish the logs.

Records are temporary and captured during the session; they do not retroactively recover the site's entire console. Read the [privacy policy](PRIVACY.en.md) before sending.

You can also open a [public issue](https://github.com/BIXCOIT0/ad-block-privacy/issues). **Everything posted there is public.** Use only a public domain, fictitious data and minimal steps; do not attach diagnostics, cookies, tokens, passwords, authentication headers, personal data or screenshots showing private information. If unsure, use the form without an attachment.

## Security vulnerabilities

Privately report suspected vulnerabilities to **marcoantonioarantes02@gmail.com**. Do not publicly disclose details of an unpatched flaw. Include the version, impact and minimal steps using fictitious data, without credentials or other people's data. This contact does not establish a response deadline or bounty program.

## Optional support

The [Pix support page](https://bixcoit0.github.io/apoio-AD-BLOCK/) is voluntary. Payment is not required to use the extension or submit reports. Check the recipient in your banking app before confirming any transfer.
