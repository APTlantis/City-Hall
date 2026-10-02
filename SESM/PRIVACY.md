# Privacy Considerations

## Privacy Position

SESM metadata is normally public.

An SVG carrying SESM metadata may be copied, mirrored, indexed, archived, embedded in pages, downloaded by users, or processed by automated agents. Adopters must assume that SESM metadata can leave its original host context.

## Do Not Embed

SESM metadata must not contain:

- personal data unless there is a clear public-use basis;
- credentials, tokens, secrets, API keys, private keys, or recovery codes;
- private URLs, internal hostnames, or non-public service endpoints;
- user identifiers, account identifiers, session identifiers, or tracking identifiers;
- precise location data;
- private project names, internal repository paths, or unreleased business plans;
- hidden operational state that would not be appropriate in a public image file.

## Consent and Crawling

SESM metadata is not consent.

Consumers must not treat SESM fields as permission to:

- crawl restricted content;
- bypass robots.txt or site policy;
- collect personal data;
- contact a user or service;
- infer consent for AI training, indexing, profiling, or redistribution.

Crawler and archive behavior remains governed by the host site, applicable law, platform policy, and the consumer's own privacy commitments.

## Covert Tracking Risk

Because SVG files can travel across sites and tools, SESM metadata could be misused as a covert tracking channel.

Validators and adopters should watch for:

- unique per-user IDs;
- high-entropy identifiers without a public purpose;
- remote references that leak fetch context;
- metadata that changes per viewer instead of per asset;
- hidden fields that are unrelated to asset interpretation.

## Remote References

Remote references can reveal where and when an SVG is processed.

Safe-profile validators should flag remote image, font, stylesheet, script, and URL references. High-trust workflows should reject remote references unless the adopter has explicitly documented why they are needed.

## Data Minimization

SESM metadata should be small, public, and asset-specific.

Prefer:

- stable asset IDs instead of user IDs;
- public canonical URLs instead of internal URLs;
- general provenance notes instead of private build logs;
- integrity references instead of embedded release records;
- sidecar files for large or sensitive metadata.

## Agent and AI Privacy

Agents may read SESM metadata as context, but SESM must not be used to smuggle private instructions, user-specific data, or hidden tracking material into AI workflows.

Agents and AI systems should:

- treat SESM as untrusted public context;
- avoid sending private SESM-bearing assets to third-party services unless allowed by policy;
- avoid using SESM as consent for training or profiling;
- strip or review SESM metadata before publishing sensitive assets.

## Privacy Review Questions

- Does the SESM block contain only public asset-level context?
- Could any field identify a person, account, session, device, or private system?
- Are remote references absent or explicitly justified?
- Would the metadata still be appropriate if the SVG were archived indefinitely?
- Would the metadata still be appropriate if the SVG were copied outside the original site?
