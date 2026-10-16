# ZeroOne: CallIt HW5

CallIt gives a private group one shared record of its predictions and results. The main promise is: "Being right is better when your group remembers."

## Public pages

| Page | Audience and main value | URL |
|---|---|---|
| Homepage | Groups that want a shared prediction record | [call-it.app](https://call-it.app/) |
| Friends | Friend groups that want to remember who called it | [Friends page](https://call-it.app/for/friends) |
| Sports | Recurring sports groups that want to collect picks in one place | [Sports page](https://call-it.app/for/sports) |
| Agreements | Groups that want to keep the original terms clear over time | [Agreements page](https://call-it.app/for/agreements) |

Each page has a waitlist signup action. A saved signup leads to the [thank-you page](https://call-it.app/thanks). The pages use the shared CallIt style guide, Lucide icons, and credited photos and films. The separate [web app](https://app.call-it.app/) is the implementation for the HW6 MVP.

## Deliverables

- [Demand strategy](demand_strategy.md): named traffic owner, two research communities, three published promotional items with their tagged destinations, and a blog plan.
- [MVP definition](mvp_doc.md): core flow, scope, manual steps, stack, and named delivery responsibilities.
- [Landing-page evidence mapping](landing-page-alignment.md): each audience and value proposition traced to HW4.
- [Analytics Academy status](analytics-academy.md): the course start confirmation still needed from the team.

Emily owns traffic and content. Yuval owns analytics setup. Charles owns submission integration. The demand strategy records the actual link placement: Rednote has a copyable tagged URL; Instagram points to its tagged profile link; LinkedIn has a clickable tagged link. These placements are visible for the instructor to assess.

## Analytics and submission status

The analytics guide records GA4 on the marketing pages, a `sign_up` event from the thank-you page, and first-touch UTM storage. Marking `sign_up` as a GA4 key event remains unconfirmed. Campaign labels in the demand strategy are lowercase.

Read-only checks on October 16, 2026: all four public pages and `/thanks` returned HTTP 200. Each page loaded a bundle containing GA4 ID `G-HPKQ2CBQT7` and the `sign_up` event code. This checks the deployed code, not GA4 event receipt or the key-event setting. Earlier signup and browser checks are recorded in the team's bulletin.

The class submission is [draft PR #42](https://github.com/kenxle/columbia-startup-studio-fall-2026/pull/42), in `teams/zeroone/hw5-pages-demand-mvp/`. It contains this README, the demand strategy, the MVP definition, the evidence mapping, and the Academy status note. After the account confirmations below are recorded, mark the PR ready and paste its URL into Courseworks. The slides set the HW5 deadline at the start of class on October 16, 2026, at 1:10 PM America/New_York.

Remaining account actions:

- **Yuval (@Yuval-Gerber):** confirm that `sign_up` is a GA4 key event and record the result.
- **Charles (@ZhangchengCharles):** collect the team's Analytics Academy 101 and 102 start confirmations and update `analytics-academy.md` with the names and dates.
- **Charles (@ZhangchengCharles):** after the confirmations are recorded, mark PR #42 ready and paste its link into Courseworks.

These actions are pending.

## Sources

- [Class 5 slides](https://github.com/et2921/CallIt/blob/90e6cfd/homework/hw-5/ref/class-5-slides.pdf), pages 85-90.
- [Style guide](https://github.com/et2921/CallIt/blob/90e6cfd/landing-pages/docs/style_guide.md) and [media credits](https://github.com/et2921/CallIt/blob/90e6cfd/docs/design/media-credits.md).
- [Analytics guide](https://github.com/et2921/CallIt/blob/90e6cfd/docs/ANALYTICS.md).

Source: [CallIt HW5 snapshot](https://github.com/et2921/CallIt/blob/90e6cfd/homework/hw-5/README.md).
