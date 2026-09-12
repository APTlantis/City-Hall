# The SVG Panels In Neon Ink - Actual Content

> **NIPC alignment note:** These SVG/XML examples preserve generated and mockup-era colors such as `#00E5FF`. Treat those values as legacy artifact evidence. New generated SVGs should embed NIPC-compatible `theme` metadata and use current NIPC tokens unless deliberately preserving an existing artifact.

## related-datasets.svg

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="312" height="238" viewBox="0 0 312 238" fill="none">
    <metadata id="sesm"><![CDATA[
{
  "artifact": {
    "artifact_id": "rust-code-corpus-related-datasets",
    "build_profile": "phase2",
    "kind": "compiled-svg",
    "output_path": "public/svg/panels/related-datasets.svg",
    "source_id": "rust-code-corpus",
    "source_path": "data/datasets/rust-code-corpus.json",
    "source_type": "dataset_manifest",
    "template_id": "related-datasets",
    "template_path": "templates/svg/panels/related-datasets.svg.tera"
  },
  "asset": {
    "description": "Related dataset links for Rust Code Corpus.",
    "ecosystem": "rust",
    "id": "rust-code-corpus-related-datasets",
    "role": "navigation-card",
    "tags": [
      "rust",
      "code",
      "source",
      "functions",
      "structs",
      "impl",
      "ownership",
      "lifetime",
      "traits",
      "macros",
      "crates",
      "docs"
    ],
    "title": "Related Datasets"
  },
  "crawl": {
    "canonical_group": "datasets",
    "discover_paths": [
      "public/index.html"
    ],
    "indexable": true
  },
  "llm": {
    "intended_interpretation": "Treat this SVG as a semantic navigation-card artifact for Rust Code Corpus.",
    "interpretation_hints": [
      "Use the canonical HTML page for full context.",
      "Do not treat this SVG as decorative only."
    ],
    "summary": "Related dataset links for Rust Code Corpus."
  },
  "provenance": {
    "build_id": "phase2-local",
    "generated": true,
    "generator": {
      "name": "aptlantis-artifact-compiler",
      "version": "0.1.0"
    },
    "input_records": [
      "rust-code-corpus",
      "neon-ink",
      "rust-code-corpus-page"
    ],
    "reproducible": true
  },
  "sesm_version": "0.3.0",
  "theme": {
    "accent": "#00E5FF",
    "id": "neon-ink",
    "name": "Neon Ink",
    "semantic_roles": {
      "blue": "license",
      "cyan": "structure",
      "green": "complete",
      "orange": "code-heat",
      "pink": "attention",
      "violet": "process"
    }
  },
  "ui": {
    "component_type": "related-dataset-list",
    "dimensions": "intrinsic-svg-viewbox",
    "preferred_layout": "artifact-panel",
    "preferred_regions": [
      "related-datasets"
    ],
    "responsive_behavior": "preserve-aspect-ratio"
  }
}
  ]]></metadata>
  <rect x=".5" y=".5" width="311" height="237" rx="5.5" fill="#050A12" stroke="#0D4152"/>
  <text x="186" y="15" fill="#5B8795" opacity=".42" font-family="Cascadia Mono, monospace" font-size="8" letter-spacing="1.1">DATASET / LINKS</text>
  <text x="18" y="30" fill="#00E5FF" font-family="Cascadia Mono, monospace" font-size="14">RELATED DATASETS</text>
  <g font-family="Cascadia Mono, monospace">
    <g transform="translate(18 52)">
      <rect width="34" height="34" fill="#081320" stroke="#00AFC7"/>
      <circle cx="17" cy="17" r="12" fill="#1A3850" stroke="#6BA7D9"/><text x="17" y="23" text-anchor="middle" fill="#D7ECFF" font-size="18" font-family="Georgia, serif">R</text>
      <text x="46" y="13" fill="#D7D0C7" font-size="12">Rust Documentation Corpus</text>
      <rect x="46" y="20" width="34" height="14" fill="#0C1830" stroke="#00AFC7"/><text x="51" y="31" fill="#00E5FF" font-size="9">CODE</text>
      <rect x="86" y="20" width="34" height="14" fill="#2A1405" stroke="#FF7A18"/><text x="91" y="31" fill="#FF7A18" font-size="9">RUST</text>
      <rect x="126" y="20" width="36" height="14" fill="#1B0F26" stroke="#B554FF"/><text x="131" y="31" fill="#B554FF" font-size="9">DOCS</text>
    </g>
    <g transform="translate(18 94)">
      <rect width="34" height="34" fill="#171708" stroke="#B9B21E"/>
      <circle cx="17" cy="17" r="12" fill="#22220A" stroke="#D6D231"/><text x="17" y="22" text-anchor="middle" fill="#D6D231" font-size="15">⚙</text>
      <text x="46" y="13" fill="#D7D0C7" font-size="12">Crates.io Metadata</text>
      <rect x="46" y="20" width="38" height="14" fill="#162014" stroke="#72896A"/><text x="51" y="31" fill="#A9C59D" font-size="9">TOOLS</text>
      <rect x="90" y="20" width="34" height="14" fill="#132615" stroke="#50E060"/><text x="95" y="31" fill="#50E060" font-size="9">RUST</text>
      <rect x="130" y="20" width="34" height="14" fill="#102314" stroke="#50E060"/><text x="135" y="31" fill="#50E060" font-size="9">META</text>
    </g>
    <g transform="translate(18 136)">
      <rect width="34" height="34" fill="#220811" stroke="#FF2E96"/>
      <path d="M17 7L29 28H5L17 7Z" fill="#250813" stroke="#FF2E96"/><text x="17" y="24" text-anchor="middle" fill="#FF2E96" font-size="16">!</text>
      <text x="46" y="13" fill="#D7D0C7" font-size="12">Rust Error Messages</text>
      <rect x="46" y="20" width="34" height="14" fill="#0C1830" stroke="#00AFC7"/><text x="51" y="31" fill="#00E5FF" font-size="9">CODE</text>
      <rect x="86" y="20" width="34" height="14" fill="#2A1405" stroke="#FF7A18"/><text x="91" y="31" fill="#FF7A18" font-size="9">RUST</text>
      <rect x="126" y="20" width="48" height="14" fill="#25102D" stroke="#B554FF"/><text x="131" y="31" fill="#B554FF" font-size="9">ERRORS</text>
    </g>
    <g transform="translate(18 178)">
      <rect width="34" height="34" fill="#180A22" stroke="#B554FF"/>
      <rect x="10" y="8" width="15" height="20" fill="#180A22" stroke="#B554FF"/><path d="M14 12H22M14 17H22M14 22H20" stroke="#B554FF"/>
      <text x="46" y="13" fill="#D7D0C7" font-size="12">Rust Book Instruct</text>
      <rect x="46" y="20" width="30" height="14" fill="#1B0F26" stroke="#B554FF"/><text x="51" y="31" fill="#B554FF" font-size="9">RPG</text>
      <rect x="82" y="20" width="54" height="14" fill="#1B0F26" stroke="#B554FF"/><text x="87" y="31" fill="#B554FF" font-size="9">NARRATIVE</text>
      <rect x="142" y="20" width="54" height="14" fill="#1B0F26" stroke="#B554FF"/><text x="147" y="31" fill="#B554FF" font-size="9">TUTORIAL</text>
    </g>
  </g>
  <text x="18" y="228" fill="#00E5FF" font-family="Cascadia Mono, monospace" font-size="12">VIEW ALL RELATED →</text>
</svg>
```

## dataset-header.svg

```xml<svg xmlns="http://www.w3.org/2000/svg" width="946" height="350" viewBox="0 0 946 350" fill="none">
    <metadata id="sesm"><![CDATA[
{
  "artifact": {
    "artifact_id": "rust-code-corpus-dataset-header",
    "build_profile": "phase2",
    "kind": "compiled-svg",
    "output_path": "public/svg/panels/dataset-header.svg",
    "source_id": "rust-code-corpus",
    "source_path": "data/datasets/rust-code-corpus.json",
    "source_type": "dataset_manifest",
    "template_id": "dataset-header",
    "template_path": "templates/svg/panels/dataset-header.svg.tera"
  },
  "asset": {
    "description": "Primary dataset identity panel for the Rust Code Corpus page.",
    "ecosystem": "rust",
    "id": "rust-code-corpus-dataset-header",
    "role": "dataset-header",
    "tags": [
      "rust",
      "code",
      "source",
      "functions",
      "structs",
      "impl",
      "ownership",
      "lifetime",
      "traits",
      "macros",
      "crates",
      "docs"
    ],
    "title": "Rust Code Corpus"
  },
  "crawl": {
    "canonical_group": "datasets",
    "discover_paths": [
      "public/index.html"
    ],
    "indexable": true
  },
  "llm": {
    "intended_interpretation": "Treat this SVG as a semantic dataset-header artifact for Rust Code Corpus.",
    "interpretation_hints": [
      "Use the canonical HTML page for full context.",
      "Do not treat this SVG as decorative only."
    ],
    "summary": "Header artifact summarizing the Rust Code Corpus dataset."
  },
  "provenance": {
    "build_id": "phase2-local",
    "generated": true,
    "generator": {
      "name": "aptlantis-artifact-compiler",
      "version": "0.1.0"
    },
    "input_records": [
      "rust-code-corpus",
      "neon-ink",
      "rust-code-corpus-page"
    ],
    "reproducible": true
  },
  "sesm_version": "0.3.0",
  "theme": {
    "accent": "#00E5FF",
    "id": "neon-ink",
    "name": "Neon Ink",
    "semantic_roles": {
      "blue": "license",
      "cyan": "structure",
      "green": "complete",
      "orange": "code-heat",
      "pink": "attention",
      "violet": "process"
    }
  },
  "ui": {
    "component_type": "dataset-hero-panel",
    "dimensions": "intrinsic-svg-viewbox",
    "preferred_layout": "artifact-panel",
    "preferred_regions": [
      "dataset-header"
    ],
    "responsive_behavior": "preserve-aspect-ratio"
  }
}
  ]]></metadata>
  <defs>
    <pattern id="dots" width="8" height="8" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="1" fill="#193341"/>
    </pattern>
    <filter id="cyanGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" flood-color="#00E5FF"/>
    </filter>
    <linearGradient id="panelGrad" x1="0" x2="0" y1="0" y2="350">
      <stop stop-color="#091522"/>
      <stop offset="1" stop-color="#03070D"/>
    </linearGradient>
    <radialGradient id="statusLiveGrad" cx="48%" cy="18%" r="78%">
      <stop offset="0" stop-color="#00E5FF" stop-opacity=".18"/>
      <stop offset=".42" stop-color="#102440" stop-opacity=".18"/>
      <stop offset="1" stop-color="#070A12" stop-opacity="0"/>
    </radialGradient>
    <filter id="activeGlow" x="-60%" y="-80%" width="220%" height="260%">
      <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#00E5FF" flood-opacity=".72"/>
    </filter>
  </defs>

  <rect x="0.5" y="0.5" width="945" height="349" rx="5.5" fill="url(#panelGrad)" stroke="#0D4152"/>
  <path d="M9 18V8H19M927 8H937V18M19 342H9V332M937 332V342H927" stroke="#00E5FF" opacity=".65"/>
  <text x="838" y="17" fill="#5B8795" opacity=".48" font-family="Cascadia Mono, monospace" font-size="8" letter-spacing="1.2">DATASET / HEADER</text>
  <text x="34" y="31" fill="#B554FF" font-family="Cascadia Mono, monospace" font-size="13">DATASETS</text>
  <text x="114" y="31" fill="#B554FF" font-family="Cascadia Mono, monospace" font-size="14">&gt;</text>
  <text x="140" y="31" fill="#00E5FF" font-family="Cascadia Mono, monospace" font-size="13">CODE</text>
  <text x="196" y="31" fill="#B554FF" font-family="Cascadia Mono, monospace" font-size="14">&gt;</text>
  <text x="222" y="31" fill="#50E060" font-family="Cascadia Mono, monospace" font-size="13">RUST CODE CORPUS</text>

  <g transform="translate(34 56)">
    <rect x="0" y="0" width="166" height="174" fill="#05080D" stroke="#FF7A18"/>
    <rect x="6" y="6" width="154" height="152" fill="url(#dots)" opacity=".85"/>
    <circle cx="83" cy="86" r="66" fill="#F26A16"/>
    <circle cx="83" cy="86" r="55" fill="#03070D"/>
    <circle cx="83" cy="86" r="43" fill="#F26A16"/>
    <text x="83" y="112" text-anchor="middle" fill="#03070D" font-family="Arial Black, Impact, sans-serif" font-size="88">R</text>
    <g fill="#03070D">
      <circle cx="83" cy="29" r="6"/><circle cx="83" cy="143" r="6"/><circle cx="26" cy="86" r="6"/><circle cx="140" cy="86" r="6"/>
      <circle cx="43" cy="46" r="5"/><circle cx="124" cy="46" r="5"/><circle cx="43" cy="126" r="5"/><circle cx="124" cy="126" r="5"/>
    </g>
    <text x="123" y="166" fill="#FF7A18" font-family="Cascadia Mono, monospace" font-size="10">v1.2.0</text>
  </g>

  <text x="222" y="88" fill="#F2EDE6" font-family="Arial Narrow, Bahnschrift Condensed, sans-serif" font-size="38" font-weight="700" letter-spacing="4">RUST CODE CORPUS</text>
  <g font-family="Cascadia Mono, monospace" font-size="12">
    <rect x="222" y="106" width="48" height="24" fill="none" stroke="#00E5FF"/>
    <text x="235" y="122" fill="#00E5FF">CODE</text>
    <rect x="282" y="106" width="48" height="24" fill="none" stroke="#FF7A18"/>
    <text x="292" y="122" fill="#FF7A18">RUST</text>
    <rect x="342" y="106" width="74" height="24" fill="none" stroke="#B554FF"/>
    <text x="354" y="122" fill="#B554FF">TRAINING</text>
    <rect x="428" y="106" width="96" height="24" fill="none" stroke="#B554FF"/>
    <text x="441" y="122" fill="#B554FF">INSTRUCTION</text>
  </g>
  <text x="222" y="162" fill="#D7D0C7" font-family="Cascadia Mono, monospace" font-size="14">
    <tspan x="222" dy="0">A high-quality corpus of Rust source code, documentation,</tspan>
    <tspan x="222" dy="22">examples, and crate metadata prepared for small-model</tspan>
    <tspan x="222" dy="22">fine tuning and code understanding.</tspan>
  </text>

  <line x1="222" y1="242" x2="720" y2="242" stroke="#17202B"/>
  <g font-family="Cascadia Mono, monospace">
    <g transform="translate(34 258)"><text fill="#00E5FF" font-size="22">▤</text><text x="32" y="10" fill="#908F93" font-size="10">RECORDS</text><text x="32" y="29" fill="#FFFFFF" font-size="14">532,104</text></g>
    <g transform="translate(154 258)"><text fill="#00E5FF" font-size="22">⬡</text><text x="32" y="10" fill="#908F93" font-size="10">TOKENS</text><text x="32" y="29" fill="#FFFFFF" font-size="14">18.7B</text></g>
    <g transform="translate(274 258)"><text fill="#B554FF" font-size="22">▱</text><text x="32" y="10" fill="#908F93" font-size="10">SIZE</text><text x="32" y="27" fill="#F2EDE6" font-size="12">7.2 GB</text></g>
    <g transform="translate(394 258)"><text fill="#6B8CFF" font-size="22">◇</text><text x="32" y="10" fill="#908F93" font-size="10">LICENSE</text><text x="32" y="27" fill="#F2EDE6" font-size="12">MIT</text></g>
    <g transform="translate(514 258)"><text fill="#B554FF" font-size="22">▣</text><text x="32" y="10" fill="#908F93" font-size="10">CREATED</text><text x="32" y="27" fill="#F2EDE6" font-size="12">Apr 12, 2025</text></g>
    <g transform="translate(654 258)"><text fill="#B554FF" font-size="22">✥</text><text x="32" y="10" fill="#908F93" font-size="10">UPDATED</text><text x="32" y="27" fill="#F2EDE6" font-size="12">May 18, 2025</text></g>
  </g>
  <g font-family="Cascadia Mono, monospace" font-size="12">
    <rect x="34" y="310" width="122" height="34" fill="rgba(0,229,255,.06)" stroke="#00E5FF"/>
    <text x="49" y="331" fill="#00E5FF">DOWNLOAD  ↓</text>
    <rect x="170" y="310" width="174" height="34" fill="rgba(181,84,255,.05)" stroke="#B554FF"/>
    <text x="187" y="331" fill="#B554FF">&lt;/&gt; VIEW SAMPLES  →</text>
    <rect x="358" y="310" width="194" height="34" fill="rgba(181,84,255,.05)" stroke="#B554FF"/>
    <text x="374" y="331" fill="#B554FF">&gt;_ LAUNCH PIPELINE ...</text>
    <rect x="566" y="310" width="124" height="34" fill="rgba(181,84,255,.05)" stroke="#B554FF"/>
    <text x="582" y="331" fill="#F2EDE6">☆ STAR</text><text x="650" y="331" fill="#F2EDE6">142</text>
  </g>

  <g transform="translate(740 20)">
    <rect x="0" y="0" width="194" height="300" rx="3" fill="#070A12" stroke="#B554FF"/>
    <rect x="1" y="1" width="192" height="298" rx="3" fill="url(#statusLiveGrad)"/>
    <path d="M8 14V6H16M178 6H186V14M16 294H8V286M186 286V294H178" stroke="#B554FF" opacity=".5"/>
    <text x="18" y="29" fill="#BEB8B3" font-family="Cascadia Mono, monospace" font-size="11">STATUS</text>
    <rect x="18" y="42" width="72" height="24" fill="rgba(0,229,255,.14)" stroke="#00E5FF" filter="url(#activeGlow)"/>
    <circle cx="28" cy="54" r="4" fill="#00E5FF" filter="url(#activeGlow)"/>
    <text x="40" y="58" fill="#6EF5FF" font-family="Cascadia Mono, monospace" font-size="12">ACTIVE</text>
    <text x="18" y="94" fill="#A7A09A" font-family="Cascadia Mono, monospace" font-size="11">QUALITY SCORE</text>
    <text x="18" y="131" fill="#10F0FF" font-family="Cascadia Mono, monospace" font-size="31">96</text>
    <text x="58" y="128" fill="#F2EDE6" font-family="Cascadia Mono, monospace" font-size="15">/100</text>
    <rect x="18" y="144" width="160" height="6" fill="#102734" stroke="#164253"/>
    <rect x="18" y="144" width="148" height="6" fill="#00E5FF"/>
    <text x="18" y="177" fill="#A7A09A" font-family="Cascadia Mono, monospace" font-size="11">VERIFIED</text>
    <text x="18" y="194" fill="#D7D0C7" font-family="Cascadia Mono, monospace" font-size="12">May 18, 2025</text>
    <text x="18" y="222" fill="#A7A09A" font-family="Cascadia Mono, monospace" font-size="11">LAST PIPELINE RUN</text>
    <text x="18" y="239" fill="#D7D0C7" font-family="Cascadia Mono, monospace" font-size="12">2 hours ago</text>
    <rect x="18" y="257" width="152" height="34" fill="rgba(0,229,255,.05)" stroke="#00E5FF"/>
    <text x="36" y="279" fill="#00E5FF" font-family="Cascadia Mono, monospace" font-size="12">VIEW REPORT  →</text>
  </g>
</svg>
```
