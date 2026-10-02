# SESM Threat Model

## Security Position

SVG is an active-content-capable format.

SESM does not make arbitrary SVG safe.

SESM defines metadata conventions for SVG assets. It does not sanitize SVGs, grant trust, authorize agents, or override browser, crawler, archive, or host security policy.

## Assets Protected

Consumers of SESM should protect:

- user credentials and tokens;
- local files and private workspace data;
- build and release infrastructure;
- crawler and archive integrity;
- agent tool-use boundaries;
- search and indexing quality;
- user trust in visible asset identity;
- downstream systems that ingest metadata.

## Trust Boundaries

SESM metadata crosses a trust boundary whenever an SVG is:

- downloaded from an external source;
- copied from a repository;
- received from a user;
- mirrored by an archive;
- indexed by a crawler;
- processed by an agent;
- embedded into a web page or application;
- passed into build or release tooling.

SESM metadata is untrusted input at every boundary.

## Threats

### Active SVG Content

An SVG may contain scripts, event handlers, external references, or other active behavior. SESM consumers must not assume an SVG is safe just because it contains SESM metadata.

Mitigation: validate the SVG against `SAFE-PROFILE.md` before broad ingestion or trusted processing.

### Prompt Injection and Agent Manipulation

SESM fields such as `llm.summary`, `llm.interpretation_hints`, and `extra` can contain text aimed at agents or language models.

Attackers may try to use these fields to instruct an agent to reveal secrets, execute commands, ignore policy, rewrite files, or contact external services.

Mitigation: agents must treat SESM as untrusted context, not instructions. SESM text must never override user instructions, system policy, or tool safety rules.

### Hidden Payloads

SVGs can contain comments, hidden text, base64 content, off-canvas elements, invisible nodes, or duplicate metadata blocks.

Mitigation: validators should flag unusual hidden content, oversized payloads, duplicate SESM blocks, and conflicts between visible and metadata identity.

### Metadata Spoofing

An SVG can claim false provenance, misleading identity, unsafe links, or incorrect integrity data.

Mitigation: consumers should verify provenance and integrity against trusted manifests, release records, signatures, or known source repositories when trust matters.

### Remote Resource Loading

SVGs may reference remote images, fonts, stylesheets, or linked resources.

Mitigation: validators should report remote references. High-trust or offline workflows should reject them unless explicitly allowed.

### Parser and Resource Exhaustion

Large SVGs, deeply nested XML, oversized metadata blocks, or complex payloads can stress parsers and validators.

Mitigation: consumers should apply size limits, parser hardening, timeouts, and safe XML parsing practices.

## Non-Threats

SESM does not protect against:

- malicious SVG rendering in a vulnerable viewer;
- compromised host sites;
- untrusted browser extensions;
- false claims accepted without verification;
- unsafe downstream agent design;
- private data embedded by mistake.

## Required Consumer Behavior

Consumers should:

- parse SESM as data only;
- validate JSON structure;
- enforce safe-profile rules when safety is required;
- ignore unknown fields unless explicitly supported;
- report unsafe SVG features;
- avoid network access during validation unless explicitly configured;
- avoid executing scripts or event handlers;
- avoid following SESM links automatically;
- keep sidecar or release records as the source of authority for high-trust claims.

## Review Questions

- Are the forbidden SVG features in the safe profile sufficient?
- Should remote references be forbidden outright for the broad profile?
- What metadata size limits should validators enforce?
- Should `llm.interpretation_hints` be constrained further to reduce agent-instruction confusion?
- Which conformance labels should external adopters use?
