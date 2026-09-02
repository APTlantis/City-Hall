<h3>D:\ Drive — Development Environment Index</h3>
<p>D:\INDEX.md is the human-readable map of the D:\ development drive: it explains the drive&#39;s purpose, operating principles, root-level conventions, shared governance, infrastructure, reference material, and—later—its project areas.
<strong>Current scope:</strong>  This document covers the hidden foundation directories and the governed CTS, DRS, LDS, and WDS portfolio roots. Later root-directory groups remain intentionally deferred.</p>
<h4>Contents</h4>
<ol>
<li><a href="#1-purpose-of-the-drive">Purpose of the drive</a></li>
<li><a href="#2-operating-model-and-goals">Operating model and goals</a></li>
<li><a href="#3-root-level-contract">Root-level contract</a></li>
<li><a href="#4-central-documents">Central documents</a></li>
<li><a href="#5-central-concepts">Central concepts</a></li>
<li><a href="#6-hidden-foundation-directories">Hidden foundation directories</a></li>
<li><a href="#7-known-documentation-and-manifest-drift">Known documentation and manifest drift</a></li>
<li><a href="#8-dbasic--qb64-workshop-and-incubator"> — QB64 workshop and incubator</a></li>
<li><a href="#9-ddrs--desktop-application-portfolio"> — desktop application portfolio</a></li>
<li><a href="#10-dcts--command-tools-and-automation"> — command tools and automation</a></li>
<li><a href="#11-ddata--shared-datasets-and-source-snapshots"> — shared datasets and source snapshots</a></li>
<li><a href="#12-dwds--websites-and-web-applications"> — websites and web applications</a></li>
<li><a href="#13-scope-boundary">Scope boundary</a></li>
</ol>
<hr>
<h4>1. Purpose of the drive</h4>
<p>D:\ is a 2 TB Western Digital Blue SATA SSD used as the primary formal development and project-creation drive. Development can happen elsewhere on the computer, but work moves here when it needs a durable home, clearer structure, shared resources, governance, repeatable workflows, or a path toward becoming a maintained project.
The drive is therefore more than a collection of repositories. It is an operator-managed development environment containing:</p>
<ul>
<li>Governance standards and reusable project conventions.</li>
<li>Shared documentation, schemas, templates, styles, and reference assets.</li>
<li>Local service data, model caches, SDK archives, and tool runtimes.</li>
<li>Project workspaces and supporting datasets.</li>
<li>Release, provenance, integrity, evaluation, and preservation records.</li>
<li>Local copies of material that should remain usable without depending entirely on hosted services.
The structure is intentionally practical rather than purely taxonomic. Directories are grouped according to how they are used, maintained, recovered, and understood by the operator.</li>
</ul>
<hr>
<h4>2. Operating model and goals</h4>
<p>The drive is designed to make serious local work easier to start, understand, maintain, and recover.</p>
<h5>2.1 Primary goals</h5>
<ol>
<li><strong>Give formal work a stable home.</strong>  Projects that move beyond experiments should have an intentional location, identity, and lifecycle.</li>
<li><strong>Keep shared dependencies local.</strong>  Large caches, models, installers, documentation, and common resources should not be duplicated inside every project.</li>
<li><strong>Make context recoverable.</strong>  Manifests, READMEs, standards, release notes, and evaluation records should explain what a directory is and how it is meant to be used.</li>
<li><strong>Support repeatable delivery.</strong>  Build, validation, hashing, provenance, packaging, and release evidence belong to the workflow rather than being afterthoughts.</li>
<li><strong>Remain useful offline.</strong>  Important tools and references should continue to work when a hosted service, package registry, or upstream website is unavailable.</li>
<li><strong>Separate projects from supporting infrastructure.</strong>  Runtime data and caches belong in shared service areas; canonical standards belong in governance areas; reusable references belong in the library.</li>
<li><strong>Stay navigable by both people and agents.</strong>  A future operator or agent should be able to begin at this index, follow the manifests, and identify authoritative material before changing anything.</li>
</ol>
<h5>2.2 High-level layout</h5>
<pre><code class="language-text">D:\
├── AGENTS.md                        Drive-wide operational constitution
├── Development.manifest.toml        Machine-readable drive identity and root registry
├── INDEX.md                         Human-readable drive map
├── .city_hall\                      Standards workshop, sandbox, incubation, and promotion lineage
├── .dpw\                            Shared infrastructure, caches, models, and installers
├── .library\                        Canonical active standards, adopted governance docs, references, and media
├── .zoning\                         General intake and incubation for project and standard ideas
├── BASIC\                           QB64 tools, local runtimes, and early project ideas
├── DRS\                             Desktop applications governed by the DRS
├── CTS\                             Command tools, pipelines, generators, and utilities
├── DATA\                            Shared datasets, temporal snapshots, and source exports
├── WDS\                             Websites and web applications governed by WDS
└── ...                              Project and other directory groups documented later

</code></pre>
<p>The leading-dot directories form the drive&#39;s hidden foundation layer. They support work across projects but are not ordinary project workspaces themselves.</p>
<hr>
<h4>3. Root-level contract</h4>
<p>The root governance contract is:
| File | Role |
| ------ | ------ |
| D:\AGENTS.md | Short operational constitution defining precedence, inheritance, required records, naming, change safety, and release rules. |
| D:\Development.manifest.toml | Authoritative machine-readable identity, policy, standard registry, and governed-root registry for the development drive. Restored on 2026-08-20 from current physical roots and live entity manifests. |
| D:\INDEX.md | Primary human-readable overview and navigation document for the drive. |</p>
<p>Everything else should be grouped into a directory with a clear operational purpose. Reusable governance templates live under D:.library\aptlantis_core\Blanks, not loose at the drive root.</p>
<h5>3.1 Governance record contract</h5>
<p>The permanent entity-named convention is:</p>
<ul>
<li>Governed portfolio or container: AGENTS.md and [DirectoryName].manifest.toml.</li>
<li>Individual project or project group: AGENTS.md, [ProjectName].manifest.toml, and Project-README.md.</li>
<li>Optional ecosystem-facing documentation: README.md.
The manifest filename matches its containing directory exactly, preserving casing and punctuation. Superseded generic and duplicate manifests are preserved in dated City Hall migration archives rather than left beside the active record. Canonical active standards and adopted overview records resolve to D:.library\aptlantis_core; City Hall is the standards workshop and sandbox for incubation, experimentation, historical lineage, archive, review, and promotion. City Hall-only material is not copied into projects and does not govern active work until deliberately promoted or explicitly adopted by a governing standard.</li>
</ul>
<h5>3.2 Maintenance commands</h5>
<p>The WGS tooling is dry-run or read-only by default where mutation is possible:</p>
<pre><code class="language-powershell">python D:\.library\aptlantis_core\WGS\tools\workspace_inventory.py --workspace-root D:\
python D:\.library\aptlantis_core\WGS\tools\governance_scaffold.py --help
python D:\.library\aptlantis_core\WGS\tools\snapshot_root_governance.py --workspace-root D:\

</code></pre>
<p>The inventory command never rewrites manifests. Scaffolding requires --apply, refuses existing targets, creates entity-named records, and registers the child with its parent. The root snapshot is a hash-indexed recovery copy inside the City Hall Git repository; the drive-root files remain authoritative.</p>
<hr>
<h4>4. Central documents</h4>
<p>The maintained Aptlantis standards, templates, and adopted governance overview records live in D:.library\aptlantis_core. These are the canonical materials currently firm enough for active use.
| Document | Purpose | Location |
| ------ | ------ | ------ |
| Aptlantis Core README | Active standards-library front door and authority boundary. | D:.library\aptlantis_core\README.md |
| Aptlantis Core Map | Guided active-governance map and reading paths. | D:.library\aptlantis_core\WORKSHOP-MAP.md |
| City Hall Operational Case Study | Adopted governance evidence showing standards workflow in practice. | D:.library\aptlantis_core\City Hall Operational Case Study.md and D:.library\aptlantis_core\City Hall Operational Case Study.pdf |
| WGS | Workspace structure, manifests, lifecycle, inheritance, and agent orientation. | D:.library\aptlantis_core\WGS |
| PPS | Project mission, boundaries, constraints, risks, roadmap, success, and failure. | D:.library\aptlantis_core\PPS |
| DRS | Desktop build, verification, packaging, integrity, and release evidence. | D:.library\aptlantis_core\DRS |
| CTS | Command-line contracts, streams, structured output, compatibility, and safety. | D:.library\aptlantis_core\CTS |
| WDS | Website and web-application development and delivery. | D:.library\aptlantis_core\WDS |
| ARHS | Release hash manifests and distribution/signing provenance records for release artifacts. | D:.library\aptlantis_core\ARHS |
| AAMHS | Multi-hash integrity records and validation for preserved archives. | D:.library\aptlantis_core\AAMHS |
| SESM | Semantic metadata embedded in SVG assets. | D:.library\aptlantis_core\SESM |
| Blanks | Entity-named manifest and README templates. | D:.library\aptlantis_core\Blanks |</p>
<hr>
<h4>5. Central concepts</h4>
<p>Aptlantis work generally follows these principles:</p>
<ul>
<li><strong>Local-first by default</strong>  — useful without depending on hosted services.</li>
<li><strong>Metadata matters</strong>  — files, datasets, commands, and outputs should explain themselves.</li>
<li><strong>Operator-centered design</strong>  — tools should fit real workflows and expose trustworthy state.</li>
<li><strong>Integrity is a feature</strong>  — hashes, manifests, release notes, provenance, and verification belong to the product.</li>
<li><strong>Preservation over polish</strong>  — durable and recoverable artifacts matter more than trend-chasing.</li>
<li><strong>Repeatability wins</strong>  — pipelines, schemas, manifests, logs, and checklists turn one-off work into reusable systems.</li>
<li><strong>Small tools can be serious tools</strong>  — a focused utility can remove more friction than a much larger platform.</li>
<li><strong>Authority should be identifiable</strong>  — templates, archives, reference copies, and active standards must not be mistaken for one another.</li>
<li><strong>Context should survive handoff</strong>  — a project should remain understandable after time has passed or a different human or agent takes over.</li>
<li><strong>Shared infrastructure should stay shared</strong>  — caches, runtimes, models, and references should be centralized where that improves portability and reduces duplication.</li>
</ul>
<hr>
<h4>6. Hidden foundation directories</h4>
<h5>6.1 D:.city_hall - standards workshop and sandbox</h5>
<h6>Role</h6>
<p>D:.city_hall is the standards workshop and sandbox for Aptlantis. It holds incubation, experiments, historical evidence, archive, review, and promotion workflow for standards and governance material. Finished standards and adopted overview records used by active work live under D:.library\aptlantis_core.
City Hall remains useful for unfinished concepts, alternative structures, historical evidence, and framework ideas that have not been promoted into the canonical library. Active projects must not inherit rules from City Hall-only material unless a canonical standard explicitly adopts them.</p>
<h6>Start here</h6>
<ol>
<li>D:.library\aptlantis_core\README.md for active standards-library orientation</li>
<li>D:.library\aptlantis_core\WORKSHOP-MAP.md for adopted governance reading paths</li>
<li>D:.city_hall\CITY-HALL.manifest.toml</li>
<li>D:.city_hall\README.md</li>
<li>D:.city_hall\WORKSHOP-MAP.md</li>
<li>D:.city_hall\AGENTS.md</li>
<li>D:.city_hall\WGS\README.md for the workspace-governance lineage</li>
<li>D:.city_hall\SFDS\README.md for standard-suite development and promotion ideas</li>
<li>D:.city_hall\PPS\README.md for proposal-history comparison only; active PPS work uses the library suite</li>
</ol>
<h6>Standard and framework map</h6>





















































































<table><thead><tr><th>Folder</th><th>Name</th><th>Current role</th></tr></thead><tbody><tr><td>AADR</td><td>Application as Data Representation Standard</td><td>Describes application-as-data records, component maps, relationships, schemas, compatibility, and validation limits.</td></tr><tr><td>AAMHS</td><td>Aptlantis Archive Multi-Hash Standard</td><td>Defines integrity records and validation procedures for preserved archives.</td></tr><tr><td>AAS</td><td>Aptlantis Analysis Standard</td><td>Defines analysis manifests, evaluation records, metrics, comparisons, and interpretation boundaries.</td></tr><tr><td>ARHS</td><td>APTlantis Release Hashing Standard</td><td>Active copy promoted to D:.library\aptlantis_core\ARHS; defines release hash manifests with SHA256, BLAKE3-256, KT128, distribution channel, and signing/provenance evidence.</td></tr><tr><td>ATS</td><td>Agent Task Standard</td><td>Defines replayable task records, handoffs, validation summaries, blockers, and agent-work context.</td></tr><tr><td>CTS</td><td>Command Tool Standard</td><td>Defines CLI contracts, streams, structured output, exit codes, compatibility, and safety for command tools.</td></tr><tr><td>DDS</td><td>Dataset Development Standard</td><td>Defines dataset provenance, licensing, splits, validation, integrity, schemas, and release readiness.</td></tr><tr><td>DRS</td><td>Desktop Application Release Standard</td><td>Reference suite for desktop release notes, manifests, artifacts, hashes, verification, and release evidence.</td></tr><tr><td>NeonInk</td><td>NeonInk</td><td>Defines semantic color, themes, UI language, visual intent, and SESM-aligned visual metadata.</td></tr><tr><td>PPS</td><td>Project Proposal Standard</td><td>Defines project mission, boundaries, constraints, risks, roadmap, success, and failure before broad implementation.</td></tr><tr><td>SESM</td><td>SVG Embedded Semantic Metadata</td><td>Defines portable semantic metadata embedded in SVG assets, including safe use, privacy, validation, and tooling.</td></tr><tr><td>SFDS</td><td>Standards Framework Development Standard</td><td>Governs how standards are structured, validated, versioned, adopted, and preserved.</td></tr><tr><td>SIS</td><td>Service and Infrastructure Standard</td><td>Governs local services, daemons, APIs, health checks, ports, logs, resource bounds, and recovery.</td></tr><tr><td>WDS</td><td>Website Development Standard</td><td>Governs websites and web apps, including manifests, deployment, accessibility, routes, rollback, and monitoring.</td></tr><tr><td>WGS</td><td>Workspace Governance Standard</td><td>Acts as the workspace constitution for roots, manifests, lifecycle, services, responsibilities, and agent orientation.</td></tr></tbody></table>
<p>These entries describe the City Hall experiment, not the active standards registry. Many contain specifications, changelogs, adoption guidance, validation checklists, examples, templates, schemas, or preserved references worth consulting selectively.</p>
<h6>Reference routing</h6>
<p>Use the canonical suite under D:.library\aptlantis_core when it owns the question:</p>
<ul>
<li><strong>Where does this live, and how is it registered?</strong>  → WGS</li>
<li><strong>Why should this project exist?</strong>  → PPS</li>
<li><strong>What kind of supported deliverable is shipping?</strong>  → DRS, CTS, or WDS</li>
<li><strong>What release hash manifest is needed?</strong>  → ARHS</li>
<li><strong>What archive integrity record is needed?</strong>  → AAMHS</li>
<li><strong>How should visual meaning or embedded metadata work?</strong>  → NeonInk or SESM
City Hall-only suites remain non-governing references or candidates until they are deliberately completed and promoted into aptlantis_core.</li>
</ul>
<h6>Repository and workspace metadata</h6>
<ul>
<li>The directory is a Git working tree and includes .git, .gitignore, and .gitattributes.</li>
<li>IDE metadata is present under .idea.</li>
<li>The City Hall README identifies git@github.com:APTlantis/CityHall.git as the repository for that reference framework.</li>
<li>City Hall is a governance/reference area; ordinary project creation should not happen directly inside it.</li>
</ul>
<hr>
<h5>6.2 D:.dpw — shared infrastructure and caches</h5>
<h6>Role</h6>
<p>D:.dpw is the drive&#39;s “Public Works” area: shared local infrastructure that supports development but is not itself the main project collection. It centralizes large or machine-managed data so that the development environment is more portable and project workspaces remain cleaner.
The directory should generally be treated as service state, caches, installers, and tool-managed storage. Contents may be large, frequently updated, or unsafe to reorganize while the owning application is running.</p>
<h6>Resource map</h6>








































<table><thead><tr><th>Path</th><th>Purpose</th><th>Operational notes</th></tr></thead><tbody><tr><td>D:.dpw\HF</td><td>Hugging Face local cache and authentication state.</td><td>Contains local Hub/cache material and may include sensitive authentication state. Token-bearing files must not be published, indexed into documentation, or copied into repositories.</td></tr><tr><td>D:.dpw\JetBrains</td><td>Local storage for JetBrains IDE installations or managed application data.</td><td>Tool-managed runtime/application data. Preserve product-specific layout unless a supported JetBrains relocation or cleanup workflow is being used.</td></tr><tr><td>D:.dpw\Ollama</td><td>Ollama model store.</td><td>Contains content-addressed blobs and model manifests. Back up blobs and manifests together; neither side alone fully describes the installed model set.</td></tr></tbody></table>
<h6>Management rules</h6>
<ul>
<li>Do not treat cache presence as proof that a dependency is permanently available; record important model or package identities elsewhere when reproducibility matters.</li>
<li>Do not commit credentials, tokens, machine IDs, or private cache metadata.</li>
<li>Stop the owning application before manually moving application-managed storage.</li>
<li>Prefer supported relocation/export mechanisms for Docker Desktop, model managers, and IDEs.</li>
<li>Preserve paired content/manifest structures together.</li>
<li>Projects may consume resources here, but source code and project-specific release artifacts should live in their governed project directories.</li>
</ul>
<hr>
<h5>6.3 D:.library - shared reference and active standards library</h5>
<h6>Role</h6>
<p>D:.library is the shared knowledge and reference layer for the drive. It contains reusable Aptlantis documents, active standards, adopted governance overview records, documentation sites, selected Git clones, and reference media. Unlike .dpw, which is primarily tool/service state, .library contains material intended to be read, reused, compared, cited, or incorporated into documentation workflows.</p>
<h6>Resource map</h6>













































<table><thead><tr><th>Path</th><th>Purpose</th><th>Current contents</th></tr></thead><tbody><tr><td>D:.library\aptlantis_core</td><td>Canonical Aptlantis active standards, schemas, templates, visual-language material, and adopted governance overview records.</td><td>Active suites include AAMHS, ARHS, CTS, DRS, LDS, PPS, SESM, WDS, WGS, blue.slate, and Blanks; adopted overview records include README.md, WORKSHOP-MAP.md, City Hall Operational Case Study.md, and City Hall Operational Case Study.pdf.</td></tr><tr><td>D:.library\docusaurus</td><td>Local Docusaurus documentation publishing workspace.</td><td>Documentation site workspaces and supporting assets. Keep generated output distinguishable from authored source.</td></tr><tr><td>D:.library\ghclones</td><td>Selected local Git repository clones used for source study or reuse.</td><td>Reference/source checkouts. A clone is not automatically an Aptlantis project or canonical upstream.</td></tr><tr><td>D:.library\youtube</td><td>Optional local storage for YouTube-related reference media.</td><td>Reference media area; provenance and retention should be reviewed before reuse.</td></tr></tbody></table>
<h6>Docusaurus sites</h6>





















<table><thead><tr><th>Path</th><th>Role</th></tr></thead><tbody><tr><td>D:.library\docusaurus\docs.aptlantis.studio</td><td>Docusaurus site for Aptlantis projects and standards documentation. Includes source docs, static assets, generated .docusaurus state, and a built site.</td></tr><tr><td>D:.library\docusaurus\docs.localhost</td><td>Docusaurus site for personal and miscellaneous local project documentation. It has the same basic source/build layout as the Aptlantis site.</td></tr><tr><td>D:.library\docusaurus\refactor-refs</td><td>Visual and project reference material used while refactoring documentation, including project screenshots, SVG/logo assets, style references, and grouped source material.</td></tr></tbody></table>
<p>Both site directories currently include package.json, package-lock.json, and pnpm-lock.yaml. Before installing or updating dependencies, choose the intended package manager deliberately and avoid casually regenerating both lockfile families.</p>
<h6>Library usage rules</h6>
<ul>
<li>Treat aptlantis_core as canonical for active suites and adopted governance overview records; treat .city_hall as the workshop and sandbox whose unpromoted material is non-governing. D:\Development.manifest.toml is the restored machine-readable root registry.</li>
<li>Treat ghclones as reference/source checkouts unless a separate manifest identifies a clone as governed work.</li>
<li>Keep generated Docusaurus output (build, .docusaurus) distinguishable from authored source (docs, src, static).</li>
<li>Preserve source attribution and licensing when material moves from a clone, screenshot collection, video, or other external reference into a project.</li>
<li>Avoid placing credentials, private tokens, or uncontrolled binaries in the library.</li>
</ul>
<hr>
<h5>6.4 D:.zoning - general intake and incubation</h5>
<h6>Role</h6>
<p>D:.zoning is the general intake and incubation area for Aptlantis project and standard ideas before PPS/WGS onboarding, standard assignment, promotion, and relocation. Material here is candidate or intake material by default. It does not govern active projects and must not replace promoted standards under D:.library\aptlantis_core unless City Hall records a promotion decision or a governing standard explicitly adopts it.</p>
<h6>Current children</h6>
<table><thead><tr><th>Path</th><th>Role</th><th>Current status</th></tr></thead><tbody><tr><td>D:.zoning\Aegis</td><td>Legacy candidate project group containing Aegis-CPP and Aegis-Rust material.</td><td>Has direct intake records; future project name is Pridwen, with Rust-first/Tauri-possible redesign preferred over promoting the C++ code directly.</td></tr><tr><td>D:.zoning\AptDiskwright</td><td>Windows desktop storage-planning prototype.</td><td>Ledger status is promote-candidate; user supplied Disk Poet as intended/alternate name; manifest paths still need zoning/current-location reconciliation.</td></tr><tr><td>D:.zoning\CloneCratesGUI</td><td>Tauri desktop operator console for CloneCratesio.</td><td>Ledger status is promote-candidate; user notes DRS, but the 2026-08-22 queue pass observed the zoning copy and no matching DRS child by name.</td></tr><tr><td>D:.zoning\Ops-Control-Surface</td><td>Tauri/React local project-board prototype.</td><td>Has direct intake records; ledger status is merge-review because D:\DRS\Ops Control Surface also exists.</td></tr><tr><td>D:.zoning\WingettingQB64</td><td>QB64/Winget idea preserved as a reconciliation record.</td><td>Ledger status is archive-review; intended target is D:\DRS\drs_holding once the holding convention exists.</td></tr><tr><td>D:.zoning\WinTrim</td><td>Windows trimming and configuration project.</td><td>Ledger status is promote-candidate; source artifacts and project/tooling scope need separation.</td></tr><tr><td>D:.zoning\WSL</td><td>WSL distribution experiment project group.</td><td>Ledger status is needs-investigation; intended target is DRS as WSL Distros, but large artifacts and active distro work need inventory.</td></tr></tbody></table>
<h6>Recently promoted out</h6>
<table><thead><tr><th>Former path</th><th>Destination</th><th>Promotion note</th></tr></thead><tbody><tr><td>D:.zoning\Theme-Preview</td><td>D:\DRS\Theme-Preview</td><td>Promoted to DRS on 2026-08-11 after WGS/PPS/DRS onboarding as a release-prep Tauri desktop application.</td></tr><tr><td>D:.zoning\ReactComponentLibrary</td><td>D:\LDS\ReactComponentLibrary</td><td>Moved to LDS on 2026-07-29 after PPS/WGS/LDS onboarding.</td></tr></tbody></table>
<p>The 2026-08-22 hidden-foundation inventory is recorded at D:.library\aptlantis_core\WGS\Hidden-Foundation-Inventory-2026-08-22.md. The current zoning ledger is D:.zoning\Intake-Ledger-2026-08-22.md, with the first incoming-project queue at D:.zoning\Incoming-Project-Queue-2026-08-22.md.</p>
<h6>Promotion rule</h6>
<p>Promotion or relocation requires classification, appropriate PPS/WGS records, applicable delivery-standard assignment, and parent-record updates. Standards and design systems require City Hall review before they govern active work, and adopted material should land under D:.library\aptlantis_core.</p>
<hr>
<h4>7. Known documentation and manifest drift</h4>
<p>The July 7–8 governance rollout established D:\AGENTS.md, D:\Development.manifest.toml, entity-named manifests, portfolio/root instructions, project/group records, holding rules, and repeatable scaffold/inventory tooling. The July 8 authority migration promoted the firm standards and templates into D:.library\aptlantis_core. On 2026-08-20, adopted overview records were also promoted into D:.library\aptlantis_core: README.md, WORKSHOP-MAP.md, and City Hall Operational Case Study.pdf.
The drift below describes historical evidence or remaining project-specific verification work. Superseded live manifests were moved to D:.city_hall\WGS\migration-notes\Legacy-Live-Manifests-20260708.
The following discrepancies were observed during the July 7, 2026 documentation pass. They are recorded here so that navigation remains honest; this pass does not silently rewrite the individual manifests.
| Area | Observed drift | Recommended correction |
| ------ | ------ | ------ |
| D:.city_hall | The broad framework contains unfinished suites, experiments, historical internal paths, and promotion lineage. | Retain it as the standards workshop and sandbox; promote only deliberately completed standards and adopted overview records into D:.library\aptlantis_core. |
| D:.dpw | Earlier root and child records retained D:\015-DPW paths and incomplete inventories. | Resolved to current cleaned-up shape on 2026-08-22: .dpw.manifest.toml registers HF, JetBrains, and Ollama. Removed runtime/cache registrations remain historical gaps. |
| D:.library | The former root record described an unrelated DocHub project at E:/DocHub. | Resolved: .library.manifest.toml now classifies the four current reference collections; the old record is archived. |
| Removed SonarScanner runtime | The former .sonar directory and root registration described a locally installed scanner that was not used. | Resolved: the runtime was deleted and active root documentation and manifests no longer register it. |
| Root documentation | Earlier notes described loose manifest templates at the drive root, and D:\Development.manifest.toml was referenced by root instructions but absent during the 2026-08-11 Theme-Preview onboarding pass. | Active blanks live under D:.library\aptlantis_core\Blanks. D:\Development.manifest.toml was restored on 2026-08-20 from current physical roots and live entity manifests, and updated on 2026-08-22 to register .zoning again. Follow-up inventory still reports child-list drift in several visible portfolio manifests. |
| D:\BASIC | Earlier root and child manifests retained former paths. | Resolved structurally: BASIC.manifest.toml and child entity manifests now use current paths; prior records are archived. Project execution evidence remains incremental. |
| D:\DRS | Earlier manifests described D:\100-DRS and the former numbered taxonomy. | Resolved structurally for the current direct children. DRS.manifest.toml now points Windows GUI release work toward MSIX/Microsoft Store distribution, with project release evidence remaining project-specific. |
| DRS project manifests | Several manifests retain former paths under D:\100-DRS, and some generated records report placeholder 0.0.0 versions and zero completion despite substantial source trees. | Review each manifest against its current project documentation and built artifacts before using it for portfolio reporting. |
| D:\DRS\WSL | clearlinux\PROCESS.md and other build material still cite former D:\100-DRS\160-UTILITIES\WSL paths. The requested aptlantis child is not currently present on disk. | Update process paths when the workspaces settle; add aptlantis only when an actual directory or governed record exists. |
| D:\CTS | Earlier manifests recorded D:\200-CTS and the former numbered taxonomy. | Resolved structurally: CTS.manifest.toml registers current direct projects, groups, Llama, utilities, and holding. |
| CTS project manifests | Several generated manifests retain former D:\200-CTS... locations or placeholder versions/completion values that disagree with substantial current implementations and READMEs. | Reconcile each manifest with current source, documentation, tests, and release artifacts before portfolio reporting. |
| D:\DATA | Earlier root and child manifests retained former paths. | Resolved structurally: DATA.manifest.toml registers current datasets, Winget group, and root ISO artifact; dataset provenance verification remains incremental. |
| DATA documentation | The crates.io and Node.js dataset manifests point to nonexistent root-level README.md/PROJECT.md files and report placeholder 0.0.0/0% metadata despite large, documented outputs. | Make the snapshot/output READMEs authoritative or add dataset-root orientation documents, then align manifest state with reproducible evidence. |
| D:\DATA\winget | Earlier duplicate directory/dataset records retained numbered paths and a phantom child. | Resolved structurally: winget.manifest.toml is the sole local entity authority and registers WingetExport as its child project. |</p>
<p>Until these records are normalized, the physical paths documented in this index reflect the observed July 7, 2026 layout, while the embedded historical manifest values remain evidence of the earlier numbered-directory organization.</p>
<hr>
<h4>8. D:\BASIC — QB64 workshop and incubator</h4>
<h5>8.1 Role</h5>
<p>D:\BASIC is the drive&#39;s QB64 and QuickBASIC-oriented workshop. It combines local development-tool copies with a small group of QB64 application ideas and experiments. Most of the project concepts are in an initial planning or scaffolding phase; QB-Winget is the clear functional exception.
The directory is deliberately lighter-weight than D:\DRS. It is a place to preserve the language toolchain, explore compact desktop utilities, and develop ideas far enough to decide whether they should mature into governed releases.</p>
<h5>8.2 Directory map</h5>













































<table><thead><tr><th>Path</th><th>Classification</th><th>Purpose and current state</th></tr></thead><tbody><tr><td>D:\BASIC\Inform</td><td>Local development tool/reference</td><td>Local copy of  <strong>InForm</strong> , a WYSIWYG GUI designer and event-driven UI engine for QB64. Its designer exports a .frm form definition and a .bas program file where application event logic is added. A Windows UiEditor.exe, source tree, setup scripts, README, license, and manifest are present.</td></tr><tr><td>D:\BASIC\QB64</td><td>Local language/runtime reference</td><td>Local copy of the original QB64 ecosystem. The visible root contains a nested qb64 distribution plus QB64.manifest.toml. Keep it as tool/reference material rather than treating it as an Aptlantis-authored project.</td></tr><tr><td>D:\BASIC\QB64PE</td><td>Local language/runtime reference</td><td>Local copy of  <strong>QB64 Phoenix Edition</strong> , the maintained QB64 offshoot that retains QB4.5/QBasic compatibility and compiles native Windows, Linux, and macOS binaries. The directory includes qb64pe.exe, compiler/source internals, settings, licenses, build files, and a local manifest.</td></tr><tr><td>D:\BASIC\QB-Winget</td><td>Functional QB64 application</td><td>Retro-styled QB64 GUI wrapper for Windows Package Manager. It supports package discovery, installation, list handling, and package-management workflows. The repository contains source/form files, an InForm integration, a compiled WingettingQB64.exe, assets, documentation, captured command output, an evaluation record, and a project manifest.</td></tr><tr><td>D:\BASIC\QB-Veracrypt</td><td>Pending application concept</td><td>Intended to explore a QB64 front end for encryption/VeraCrypt workflows, conceptually similar to the Winget wrapper. At present it contains a project manifest and VeraCrypt-master.zip; it is not yet a working QB64 application.</td></tr><tr><td>D:\BASIC\QB-7Zip</td><td>Pending application concept/reference</td><td>Intended to explore a QB64 front end for compression/7-Zip workflows. The current 7-zip child is a Maven-based source tree rather than a QB64 application or a simple 7-Zip binary bundle, so the project premise and dependency source should be reviewed before implementation.</td></tr><tr><td>D:\BASIC\BASIC.manifest.toml</td><td>Canonical root governance record</td><td>Registers all current children, classifies Inform/QB64/QB64PE as external sources, and classifies the three QB utility directories as projects.</td></tr></tbody></table>
<h5>8.3 QB-Winget — working reference project</h5>
<p>QB-Winget demonstrates the practical shape that the other QB utility ideas could eventually take:</p>
<ul>
<li>QB64/BASIC source and InForm-generated UI definitions.</li>
<li>A compiled Windows executable for direct testing.</li>
<li>A project manifest and README describing identity, dependencies, capabilities, and status.</li>
<li>Captured Winget search/install output for integration development.</li>
<li>Saved package lists and supporting assets.</li>
<li>A Git repository linked to <a href="https://github.com/APTlantis/WingettingQB64">APTlantis/WingettingQB64</a>.
Its current manifest identifies version 1.0.0, active development, approximately 75% completion, and mostly stable behavior. Those values should be reverified before the next formal release rather than treated as an automatic release claim.</li>
</ul>
<h5>8.4 Toolchain relationships</h5>
<pre><code class="language-text">QB64 / QB64PE
    └── compile BASIC source into native applications

InForm
    └── design event-driven QB64 interfaces and generate .frm + .bas files

QB-Winget
    └── working example of a QB64/InForm Windows utility

QB-Veracrypt and QB-7Zip
    └── early concepts that may follow the same wrapper pattern

</code></pre>
<h5>8.5 Working rules</h5>
<ul>
<li>Preserve Inform, QB64, and QB64PE as identifiable upstream tool/reference copies; do not imply Aptlantis authorship.</li>
<li>Keep generated forms and the hand-edited application logic distinguishable so InForm regeneration does not overwrite custom work.</li>
<li>Do not describe QB-Veracrypt or QB-7Zip as functional until a runnable implementation and verification evidence exist.</li>
<li>Treat encryption and archive operations as potentially destructive: preview inputs/outputs, avoid silent overwrites, and make command execution visible.</li>
<li>Verify the provenance, license, and intended role of the current Maven tree under QB-7Zip\7-zip before building against it.</li>
<li>Move a project into the release discipline of D:\DRS when it is expected to ship as a maintained desktop application.</li>
</ul>
<hr>
<h4>9. D:\DRS — desktop application portfolio</h4>
<h5>9.1 Role and governing standard</h5>
<p>D:\DRS is the portfolio root for desktop applications governed by the  <strong>Desktop Application Release Standard (DRS)</strong> . Projects may be Windows-specific or cross-platform underneath, but they are grouped here because their intended deliverable is a desktop application, desktop package, or desktop-operated system. Public Windows GUI releases now default to MSIX submitted through the Microsoft Store, with self-signed MSIX reserved for development/sideload evidence and documented direct MSI/EXE distribution treated as an exception.
The active root governance files are:
| File | Role |
| ------ | ------ |
| D:\DRS\AGENTS.md | Portfolio-specific operational rules inheriting the drive constitution. |
| D:\DRS\DRS.manifest.toml | Canonical directory record for current direct children and release-policy orientation. |
| D:\DRS\Windows-GUI-MSIX-Store-Workflow.md | Portfolio workflow for `winapp`, `msstore`, MSIX development packages, Store submission, and signing boundaries. |
| D:.library\aptlantis_core\DRS | Canonical Desktop Application Release Standard suite. |</p>
<p>Canonical DRS guidance resolves to D:.library\aptlantis_core\DRS through the manifest and Markdown links. City Hall and portfolio-local copies are not authoritative.
The standard&#39;s core posture is that a release is a verifiable bundle of understanding, artifact, and evidence—not merely a compiled file. In practical terms:</p>
<ul>
<li>The release note is the human promise.</li>
<li>The manifest is the machine-readable record.</li>
<li>The artifact hash binds the promise and record to the actual build.</li>
<li>Destructive behavior must be detected and explained before mutation.</li>
<li>Documentation and verification evidence ship with the release.</li>
<li>A passing build alone does not establish release readiness.</li>
</ul>
<h5>9.2 Active portfolio map</h5>






































































<table><thead><tr><th>Project</th><th>Purpose</th><th>Current evidence and posture</th></tr></thead><tbody><tr><td>AptlantisConsole</td><td>Local-first DevOps/operator console combining a Next.js interface with a Tauri 2 Windows shell.</td><td>Version 1.0.8 is documented. Live areas include Docker, Git, system monitoring, MongoDB, DuckDB, networking, SSH/FTP, Winget, editor tools, terminals, settings, screenshots, and a command builder. docs\CurrentAndPlannedFeatures.md is the detailed live/partial/planned feature ledger.</td></tr><tr><td>Chat</td><td><strong>ChatArchive</strong> , a local-first desktop archive for exported AI conversations.</td><td>Tauri 2 + React reader with a Rust OpenAI importer, SQLite state, filesystem-backed normalized conversations and assets, structured search, artifact explorers, and Markdown export. It handles both single and sharded OpenAI conversation exports. Its README states that the Phase 2 release gate remains blocked on a clean-baseline Windows installer lifecycle rerun despite other major checks passing.</td></tr><tr><td>ChromeArchivalPlugin</td><td>Chrome/Chromium extension tailored to the operator&#39;s page-capture and archival workflow.</td><td>Captures page/link lists, metadata, JSON-LD, readable Markdown, full-page content, screenshots, and paginated PDFs into local download structures. It combines familiar archival capabilities in one preferred workflow rather than claiming a novel category of browser extension.</td></tr><tr><td>ClipboardFilter</td><td>Local clipboard extraction, embedding, indexing, and lookup pipeline.</td><td>Uses staged 1-Input, 2-Embed, 3-Database, and 4-Lookup areas, Python processing scripts, DuckDB, local embeddings/Ollama, and a web lookup UI. The manifest describes version 2.0.0, mostly-stable status, and an atomic-entry TOML processing model.</td></tr><tr><td>CommandWizard</td><td>Schema-driven WinUI desktop application for constructing CLI commands through a guided interface.</td><td>Release v1.0.0 is locally packaged as a signed MSIX. The release record reports a successful Release build, 11/11 tests, a valid local signature, successful installation, and launch. Its development certificate is suitable for local/trusted testing—not public trust.</td></tr><tr><td>DataVisualizers</td><td>Early Tauri/React/TypeScript data-visualization workspace.</td><td>The source tree and Tauri structure exist, but the README is still the starter template and the generated manifest reports placeholder 0.0.0/0% metadata. Treat it as experimental until its actual mission and supported formats are documented.</td></tr><tr><td>Filing Cabinet</td><td>Local-first Windows desktop vault for retaining, cataloging, previewing, verifying, and recovering technical artifacts.</td><td>Version 0.1.1 is the active governed line. The first Microsoft Store identity is reserved as Filing Cabinet with package identity Aptlantis.FilingCabinet and Store ID 9N29X9KR70R3. Aptlantis.FilingCabinet_0.1.1.0_x64.msix has been accepted by Partner Center package validation and has ARHS hash evidence plus detached PGP/SLH-DSA manifest signatures. Public release still requires any remaining certification/publication steps and verification of the Microsoft Store-signed distributed package; historical WiX/MSI evidence remains local/direct-distribution evidence rather than the default public release path.</td></tr><tr><td>AptDiskwright</td><td>Safety-first Windows disk planning and migration application.</td><td>First full PPS adoption: a .NET/WPF client with a privileged native C++ engine boundary, durable plan/evidence records, authenticated named-pipe protocol, and a “Plan first. Execute second. Record everything.” rule. Physical-disk mutation and live migration remain disabled pending disposable-VHD and bootable-VM qualification.</td></tr><tr><td>Structra</td><td>Interactive structure and layout visualization tool for architectures and organizational systems.</td><td>React/Tauri workspace with export support, docs, evaluation record, and a manifest identifying version 1.0.0, mostly-stable status, and roughly 85% completion. Verify those generated status fields before release reporting.</td></tr><tr><td>Tauri-IT</td><td>Desktop packaging/adaptation of the upstream  <strong>IT-Tools</strong>  web application.</td><td>Not an original Aptlantis application concept. It is a local Tauri 2 desktop bundle of <a href="https://github.com/CorentinTh/it-tools">CorentinTh/it-tools</a>, retained because many of its developer and IT utilities are useful without repeatedly starting a web development server. Preserve upstream license and attribution.</td></tr><tr><td>Theme-Preview</td><td>Local-first Tauri desktop laboratory for deterministic UI component, theme-token, and reusable component-group previews from TOML metadata.</td><td>Promoted from zoning on 2026-08-11 with WGS/PPS/DRS records. Current posture is release-prep: `npm run verify` passed from D:\DRS\Theme-Preview on 2026-08-11, but artifact hashes, install/uninstall behavior, docs inclusion, and signing remain pending before release claims.</td></tr><tr><td>WinTrim</td><td>Long-running Windows environment and installation-curation research project.</td><td>Originated in deliberate NTLite-based Windows ISO customization with a strong emphasis on understanding and documenting each removal instead of trusting opaque debloat scripts. Current material includes a large annotated removal manifest, component-removal documentation, machine/config data, a documentation architecture, and a Windows 11 ISO. The planned revival should focus on transparent desired state, evidence, and reproducibility.</td></tr><tr><td>WSL</td><td>Workspace for adapting Linux distributions into locally packaged WSL environments.</td><td>Contains active/recent distro experiments, rootfs artifacts, ISOs, MSIX packaging scripts, launchers, logos, inventories, and process notes. This area is artifact-heavy and currently less normalized than the other DRS projects. See the dedicated map below.</td></tr></tbody></table>
<h5>9.3 Project detail and read-first documents</h5>
<h6>AptlantisConsole</h6>
<p>Read in this order:</p>
<ol>
<li>D:\DRS\AptlantisConsole\AptlantisConsole.manifest.toml</li>
<li>D:\DRS\AptlantisConsole\README.md</li>
<li>D:\DRS\AptlantisConsole\docs\CurrentAndPlannedFeatures.md</li>
<li>D:\DRS\AptlantisConsole\AptlantisConsoleVersionMilestoneTimeline.md
The feature ledger is especially important because it separates live behavior from partial areas, known gaps, proposals, and planned work across each operator-console surface.</li>
</ol>
<h6>ChatArchive</h6>
<p>Start with D:\DRS\Chat\README.md, then consult docs\Phase2-QA-Report.md for the current release gate. The README is unusually specific about importer compatibility, local storage, artifacts, tests, privacy, and limitations; it should remain the primary orientation document until a project manifest is added.</p>
<h6>ClipboardFilter</h6>
<pre><code class="language-text">1-Input      Raw clipboard/export inputs
2-Embed      Extracted entries and embedding-stage material
3-Database   DuckDB-backed indexed corpus
4-Lookup     Query/interaction layer
└── web      Web UI for searching and interacting with the database
scripts      Extraction, ingestion, and embedding utilities

</code></pre>
<p>Key scripts currently include embed.py, extract_checked.py, extract_raw.py, and ingest.py. Inputs, generated/intermediate records, the authoritative database, and the lookup interface should remain clearly separated.</p>
<h6>CommandWizard</h6>
<p>D:\DRS\CommandWizard\RELEASE-v1.0.0.md is the clearest release summary. It records the local MSIX path, certificate posture, install flow, validation commands, and verified results. The repository also contains the WinUI project, tests, schemas, packaging scripts, assets, and built output.</p>
<h6>AptDiskwright</h6>
<p>Read AptDiskwright-Project-Proposal.md first, then AptDiskwright-Architecture-v1.md, AptDiskwright.manifest.toml, and README.md. The key trust boundary is explicit: the current native service performs an authenticated handoff and recorded safe stop, but it does  <strong>not</strong>  silently fall back to DiskPart, PowerShell mutation, or physical-disk writes.</p>
<h6>Structra</h6>
<p>Read README.md, Structra.manifest.toml, and Structra-AI-EVALUATION.json together. The README describes intent and capabilities; the manifest provides structured status; the evaluation is analytical evidence and may age independently of the code.</p>
<h6>Theme Preview</h6>
<p>Read Theme-Preview.manifest.toml, Project-README.md, README.md, Theme-Preview.md, docs\Project-Proposal.md, and docs\Theme-Preview - Release Checklist.md. The project is a Tauri 2 desktop preview studio whose TOML metadata is source of truth for components, themes, and groups. Existing build and preview artifacts are preserved, and `npm run verify` passed after promotion on 2026-08-11. Release readiness remains blocked until artifact hashes, installer lifecycle checks, docs inclusion, and signing status are recorded.</p>
<h6>WinTrim</h6>
<p>The most useful current records are:</p>
<ul>
<li>COMPONENTS_REMOVED.md — detailed removal knowledge.</li>
<li>RemovalManifest_Annotated.xml — structured annotated removal record.</li>
<li>DOCUMENTATION_ARCHITECTURE.md — plan for standalone toolkit/GUI documentation and a unified booklet.</li>
<li>PHASE1_CLEANUP_SUMMARY.md — completed cleanup and next documentation work.</li>
<li>README-Rules.md — local documentation conventions.
Because the directory contains a multi-gigabyte Windows ISO, redistribution, licensing, provenance, and hash handling must be deliberate. The ISO should not be mistaken for an ordinary source artifact.</li>
</ul>
<h5>9.4 WSL workspace</h5>
<h6>Purpose</h6>
<p>D:\DRS\WSL is a rapid-development workshop for converting, adapting, validating, and packaging Linux distributions for WSL. Some children are complete enough to include signed local MSIX packages and launchers; others are only source media, extracted payloads, rootfs archives, or planning documents.
The area also contains large shared source artifacts at its root. These include Clear Linux and Nitrux ISOs, Clear Linux archives, a raw disk, Debian Wheezy package indexes, logos, and a very large Clear Linux bundle archive. These files should be inventoried and hashed before deduplication or relocation.</p>
<h6>Distro/workspace map</h6>

















































<table><thead><tr><th>Path</th><th>Current on-disk state</th></tr></thead><tbody><tr><td>WSL\antix</td><td>antiX 26 Core ISO plus a substantial antiX-WSL.md process/planning document.</td></tr><tr><td>WSL\brunson</td><td>BrunsonLabs-WSL.md planning/process document; no packaged rootfs is visible at the top level.</td></tr><tr><td>WSL\cbpp</td><td>CrunchBang++ ISO, assets, AppX manifest, launcher, local development certificate, and MSIX build script.</td></tr><tr><td>WSL\clear-43540-live-server</td><td>Extracted Clear Linux live-server ISO layout with EFI, images, bootloader, kernel, and loader trees.</td></tr><tr><td>WSL\clearlinux</td><td>The most heavily documented Clear Linux experiment: frozen baselines, inventory outputs, smoke-test and swupd records, a large WSL rootfs tar, and PROCESS.md. The work explores not only import but the practical limits of maintaining Clear Linux as a WSL-oriented fork/environment.</td></tr><tr><td>WSL\crunchbang</td><td>CrunchBang ISO, rootfs tar, local MSIX releases, launcher, packaging script, overrides, and detailed investigation notes. CRUNCHBANG_APT_CASE_STUDY.md distinguishes the fixed missing apt command from deeper vintage Debian/Wheezy instability.</td></tr><tr><td>WSL\feren</td><td>Feren OS image/rootfs material, Windows launcher, AppX manifest, build script, local certificate, and README.</td></tr><tr><td>WSL\nitrux</td><td>Nitrux ISO only at present; no local packaging or process document is visible at the top level.</td></tr><tr><td>WSL\peppermint</td><td>Peppermint OS ISO, multiple rootfs tar iterations, local MSIX builds, launcher, manifests, assets, staging data, and packaging script. This is a built-artifact workspace, not merely a distro note.</td></tr><tr><td>WSL\solus</td><td>A solus-rootfs.tar artifact is present. Additional process documentation is not visible in the current top level and should be restored or linked if it lives elsewhere.</td></tr></tbody></table>
<p>The requested D:\DRS\WSL\aptlantis directory is not currently present and is therefore not documented as an existing workspace.</p>
<h6>WSL handling rules</h6>
<ul>
<li>Verify the real image chain for each distro; ISO layouts and package managers differ materially.</li>
<li>Do not assume every rootfs is Debian/Ubuntu-based or that apt is available.</li>
<li>Extract Linux filesystems on a filesystem that preserves permissions, links, devices, and metadata; NTFS-mounted extraction can break hardlinks and modes.</li>
<li>Keep source media, extracted rootfs, normalized tar, staged package, signed package, and verification evidence distinguishable.</li>
<li>Record hashes for large source and release artifacts.</li>
<li>Treat local .pfx development certificates as sensitive release infrastructure; do not publish private-key material.</li>
<li>Test imports under a distinct disposable WSL name before replacing a working distro.</li>
<li>Preserve a known-good baseline before experimental pruning or package-manager changes.</li>
<li>Document whether a distro is a proof of import, a maintained WSL adaptation, or an intended fork; these are very different maintenance commitments.</li>
</ul>
<h5>9.5 drs_holding — excluded and dormant work</h5>
<p>D:\DRS\drs_holding is the quarantine/incubator area for ideas, starts, dormant projects, and incomplete work that should not appear in normal project evaluations or active-portfolio reporting.
| Path | Current role |
| ------ | ------ |
| drs_holding\Aegis | Holds former Aegis material for review. The intended future project name is Pridwen, and the C++ code should be treated as reference/prototype material unless explicitly revived. |
| drs_holding\Hubris | Contains an Aptlantis Hubris concept document, concept art, NeonInk reference, manifest, and a nested implementation tree. The generated manifest&#39;s “active” label should not override its holding-area classification. |
| drs_holding\ProjectTracking | Early project/tool tracking material plus a generated manifest retaining an older path. |
| drs_holding\Tauri-Visualizers | Experimental Tauri visualization bundle containing Mermaid and JSONCrack-related material, source, dependencies, build output, and a minimal README. |</p>
<p>Rules for the holding area:</p>
<ul>
<li>Exclude it from default evaluations, release dashboards, and active-project counts.</li>
<li>Do not infer abandonment; “holding” means intentionally outside the active reporting surface.</li>
<li>A project should leave holding only after its identity, purpose, current state, documentation, and destination are reviewed.</li>
<li>Update generated manifests when promotion occurs; moving a directory alone does not make its old status/path metadata true.</li>
</ul>
<h5>9.6 Portfolio-level maintenance rules</h5>
<ul>
<li>Read the project-specific manifest and current README before broad changes.</li>
<li>Apply the DRS release gates in proportion to the artifact and its risk.</li>
<li>Keep source, generated output, installer/package artifacts, and verification evidence distinct.</li>
<li>Never report a project as release-ready solely because it builds.</li>
<li>Preserve upstream attribution and license boundaries for adapted third-party projects such as IT-Tools.</li>
<li>Treat disk-management, encryption, OS-image, WSL-rootfs, and installer work as elevated-risk operations requiring explicit verification.</li>
<li>Exclude drs_holding from ordinary active-portfolio analysis.</li>
<li>Reconcile project docs, manifests, versions, and actual artifacts before publishing portfolio metrics.</li>
</ul>
<hr>
<h4>10. D:\CTS — command tools and automation</h4>
<h5>10.1 Role and governing standard</h5>
<p>D:\CTS is the portfolio root for command-line tools, automation utilities, generators, data-processing pipelines, and other operator-facing programs governed primarily by the  <strong>Command Tool Standard (CTS)</strong> .
CTS exists to make command behavior dependable for both people and automation. It governs command contracts, help and version output, stdout/stderr behavior, structured output, exit codes, pipeline integration, destructive-operation safeguards, compatibility, and release verification. It does not replace the standards governing workspace placement, project intent, datasets, websites, or desktop packaging.
The current root governance files are:
| File | Role |
| ------ | ------ |
| D:\CTS\AGENTS.md | Portfolio-specific command-tool rules inheriting the drive constitution. |
| D:\CTS\CTS.manifest.toml | Canonical current-path manifest registering direct projects, project groups, Llama, utilities, and the holding area. |
| D:.library\aptlantis_core\CTS | Canonical Command Tool Standard suite. |</p>
<p>Canonical CTS guidance resolves to D:.library\aptlantis_core\CTS through the manifest and Markdown links. City Hall and portfolio-local copies are not authoritative.</p>
<h5>10.2 CTS operating contract</h5>
<p>A CTS-governed tool should make the following behavior explicit before its public command surface is considered stable:</p>
<ul>
<li>Command purpose and invocation pattern.</li>
<li>Required and optional inputs.</li>
<li>Normal stdout and diagnostic stderr behavior.</li>
<li>Machine-readable output mode and stable fields.</li>
<li>Documented exit codes.</li>
<li>Human and automation examples.</li>
<li>Stability level for commands, flags, and output fields.</li>
<li>Preview, confirmation, recovery, or --dry-run behavior for destructive actions.</li>
<li>Accurate --help and --version output.
CTS uses these default exit-code bands:
| Code | Meaning |
| ------ | ------ |
| 0 | Success. |
| 1 | General failure. |
| 2 | Invalid command usage or arguments. |
| 3 | Input file, path, or resource missing. |
| 4 | Validation failed. |
| 5 | External dependency unavailable. |
| 10+ | Tool-specific failure documented in the command contract. |</li>
</ul>
<p>Normal data belongs on stdout; warnings, progress, diagnostics, and errors belong on stderr. A JSON mode must not mix prose progress into its stdout payload. A stable command is one that a script can invoke, parse, and respond to without reading prose logs.</p>
<h5>10.3 Active portfolio map</h5>























































<table><thead><tr><th>Project</th><th>Purpose</th><th>Current evidence and posture</th></tr></thead><tbody><tr><td>AnalyzeProjects</td><td>AI-assisted multi-project assessment and classification tool.</td><td>Python implementation that samples project trees, filters generated/dependency content, sends structured prompts to an Ollama-compatible model endpoint, validates JSON results, and produces per-project summaries plus aggregate statistics. It supports local or cloud-hosted models, configurable concurrency, retry/backoff, context limits, and recent-result skipping.</td></tr><tr><td>AptlantisLogos</td><td>Centralized visual-asset generation pipeline.</td><td>Converts AI-generated source PNG logos into standardized PNG, ICO, and SVG derivatives, extracts 16-color palettes with ImageMagick/Pillow-based tooling, emits metadata, and builds a local HTML palette/logo atlas. Its palettes directly feed LangThemeGenerator.</td></tr><tr><td>CloneCratesio</td><td>High-performance crates.io mirroring and metadata pipeline.</td><td>Go command tools with a Python orchestration wrapper. Downloads .crate archives from a local crates.io index, supports loose and rolling tar.zst storage, writes JSONL/sidecar metadata, restores bundles, and exposes Prometheus/pprof telemetry. The README records a June 11, 2026 full-registry run with 2,490,647 successes and zero final errors.</td></tr><tr><td>ConversionTools</td><td>Small, opinionated local media-conversion suite.</td><td>Groups Rust/FFmpeg audio and video converters with a CPU-oriented Python Whisper transcription utility. Input conventions and common settings are intentionally preselected for the operator&#39;s usual workflows.</td></tr><tr><td>DatasetPipelines</td><td>Emerging home for repeatable dataset-production pipelines.</td><td>Introduces a formal Rust-oriented pipeline model in which the dataset, provenance, validation, training splits, model metadata, reports, and reusable pipeline are all products. Current children are Winget and TinyLlama-HolyC; their implementation maturity differs.</td></tr><tr><td>FH-RefToolkit</td><td>Flathub catalog/ref acquisition toolkit.</td><td>Python tools for AppStream parsing, catalog querying, list generation, and .flatpakref download. It works, but its documentation, structure, command contracts, and generated status records lag behind the current quality bar and should be revisited before being presented as a current production example.</td></tr><tr><td>LangThemeGenerator</td><td>Palette-to-theme generator linked to AptlantisLogos.</td><td>Converts 16-color ecosystem palettes into themes for VS Code, Notepad++, JetBrains IDEs, and terminals. Includes generated theme trees, palette inputs, documentation, screenshots such as project_images\jb-zig.png, and a manifest. Generated themes have also been exposed through the main website for download.</td></tr><tr><td>Llama</td><td>HolyC dataset-generation and model-preparation project group.</td><td>Contains the Rust create-dataset producer and Python-oriented layer-one workspace with substantial JSONL corpora. Governance now identifies the children explicitly; provenance, regeneration, schemas, hashes, and training boundaries remain the next verification priorities.</td></tr><tr><td>UTILITIES</td><td>Collection of narrowly scoped supporting command tools.</td><td>Contains seven small converters, mappers, metadata processors, and search/copy tools. These should remain separately understandable even though they share one portfolio directory.</td></tr></tbody></table>
<h5>10.4 AnalyzeProjects</h5>
<h6>Purpose</h6>
<p>D:\CTS\AnalyzeProjects is a project-intelligence tool for quickly extracting useful metadata from many local codebases. It is used for classification, sorting, progress assessment, missing-piece discovery, next-step suggestions, and creative upgrade ideas.
Its model connection is Ollama-compatible, which permits the same workflow to use either:</p>
<ul>
<li>A local model hosted through Ollama.</li>
<li>A cloud-hosted model exposed through an Ollama-compatible endpoint.
Cloud models are often preferred for speed and stronger project inference, while local models remain useful when privacy, offline operation, or cost control is more important.</li>
</ul>
<h6>Processing model</h6>
<pre><code class="language-text">Configured project roots
    ↓
File filtering and bounded sampling
    ↓
Structured project-analysis prompt
    ↓
Local or cloud Ollama-compatible model
    ↓
JSON validation and retry handling
    ↓
Per-project JSON + aggregate Markdown/statistics

</code></pre>
<p>The current implementation includes configurable roots, explicit standalone projects, directory exclusions, file/character limits, three-worker concurrency by default, exponential retry behavior, seven-day result skipping, progress logging, and schema validation.</p>
<h6>Read first and security</h6>
<ol>
<li>D:\CTS\AnalyzeProjects\README.md</li>
<li>D:\CTS\AnalyzeProjects\config.toml</li>
<li>D:\CTS\AnalyzeProjects\Summarizer.py</li>
<li>D:\CTS\AnalyzeProjects\PromptTemplate.py</li>
<li>D:\CTS\AnalyzeProjects\ModelClient.py
The local Git remote identifies <a href="https://github.com/APTlantis/AnalyzeProjects">APTlantis/AnalyzeProjects</a> as the upstream repository.
Model API keys must not be committed. Prefer environment variables or another secret store, and remember that selecting a cloud model sends sampled project content outside the machine. Sensitive repositories require an explicit privacy decision before analysis.</li>
</ol>
<h5>10.5 AptlantisLogos and LangThemeGenerator</h5>
<p>These projects form one connected visual pipeline:</p>
<pre><code class="language-text">Programming-language or ecosystem concept
    ↓
AI-generated Aptlantis source PNG
    ↓
AptlantisLogos
    ├── normalized PNG derivatives
    ├── ICO assets
    ├── SVG assets
    ├── extracted color palettes
    ├── logos.json metadata
    └── local HTML atlas / palette board
              ↓
       LangThemeGenerator
              ├── VS Code themes
              ├── Notepad++ themes
              ├── JetBrains themes
              └── terminal themes

</code></pre>
<p>The source logo is inspired by a programming language&#39;s syntax or ecosystem identity, but its colors are not necessarily that language&#39;s official brand colors. They may reflect the image model&#39;s composition and should be labeled as Aptlantis interpretations rather than official language branding.
AptlantisLogos currently contains separate png, ico, svg, palettes, themes, and scripts trees plus logos.json and a large generated palette-atlas.html. The atlas is a local static board and generated artifact; its approximately 258 MB size makes regeneration and source/derived separation important.
LangThemeGenerator consumes the palette layer through generate_theme.py and produces multiple IDE/terminal theme families. Its README currently describes “one palette → 5 IDE themes.” Read README.md, LangThemeGenerator.manifest.toml, palettes, and project_images before changing mappings or published output.
Repositories:</p>
<ul>
<li><a href="https://github.com/APTlantis/AptlantisLogos">APTlantis/AptlantisLogos</a></li>
<li>The local LangThemeGenerator directory did not expose a Git remote during this audit; confirm its canonical publishing location before documenting one.</li>
</ul>
<h5>10.6 CloneCratesio</h5>
<p>D:\CTS\CloneCratesio is a production-oriented crates.io mirror system built for large captures, offline Rust development, archival work, and metadata analysis.</p>
<h6>Architecture</h6>





































<table><thead><tr><th>Component</th><th>Role</th></tr></thead><tbody><tr><td>Clone-Index.py</td><td>Outer orchestration layer around the compiled command tools and local index workflow.</td></tr><tr><td>cmd\download-crates</td><td>Concurrent crate downloader with retries, integrity behavior, loose/bundle storage modes, progress, and telemetry.</td></tr><tr><td>cmd\generate-sidecars</td><td>Generates per-crate JSON or aggregated JSONL sidecar metadata.</td></tr><tr><td>cmd\extract-bundles</td><td>Restores rolling bundle contents into the standard crates.io shard layout.</td></tr><tr><td>internal</td><td>Shared Go implementation packages.</td></tr><tr><td>docs</td><td>Architecture, quick-start, release, air-gap, metrics, and operational evidence.</td></tr><tr><td>testdata</td><td>Bounded fixtures for validation and development.</td></tr></tbody></table>
<p>The README identifies v1.1.0 as the current documented release and shows the actual large-scale run evidence near the top. Its root manifest still reports 1.0.0, so release reporting should use the README/release document and reconcile the manifest before the next publish action.
Read first:</p>
<ol>
<li>D:\CTS\CloneCratesio\README.md</li>
<li>D:\CTS\CloneCratesio\docs\Architecture.md</li>
<li>D:\CTS\CloneCratesio\docs\Quickstart-Windows.md</li>
<li>D:\CTS\CloneCratesio\docs\RELEASE-v1.1.0.md</li>
<li>D:\CTS\CloneCratesio\CloneCratesio.manifest.toml
Repository: <a href="https://github.com/APTlantis/Clone-Cratesio">APTlantis/Clone-Cratesio</a></li>
</ol>
<h5>10.7 ConversionTools</h5>
<p>D:\CTS\ConversionTools groups three task-focused local media tools:
| Path | Implementation | Role |
| ------ | ------ | ------ |
| ConversionTools\VideoToMP4 | Rust + FFmpeg | Converts common video inputs to MP4 using the operator&#39;s usual input and output conventions. Contains a Cargo project, source, built target tree, and help text. |
| ConversionTools\Audio | Rust + FFmpeg | Performs common audio conversion work through a small compiled Rust wrapper. Contains an independent Cargo project and target tree. |
| ConversionTools\CPU-Whisper | Python + Whisper | CPU-oriented local transcription using small/base/tiny Whisper-class models. Contains main.py and a minimal requirements file. |
| ConversionTools\in | Shared input staging | Convenience location for source media. Inputs should not be confused with source code or durable release artifacts. |</p>
<p>The suite is intentionally opinionated: it avoids repeatedly reconstructing FFmpeg and transcription commands for common local jobs. That convenience should still be backed by visible input/output paths, overwrite behavior, dependency checks, and meaningful exit codes.
Repository: <a href="https://github.com/APTlantis/SimpleConversionTools">APTlantis/SimpleConversionTools</a></p>
<h5>10.8 DatasetPipelines</h5>
<h6>Purpose</h6>
<p>D:\CTS\DatasetPipelines is a newer effort to replace one-off, project-attached dataset generation with reusable and inspectable pipelines. The governing idea in Aptlantis Rust Pipeline Template.md is that a dataset should never simply appear as train.jsonl; it should ship with evidence explaining source material, transformations, exclusions, rules, structure, intended model objective, and quality checks.
The target pipeline stack is:</p>
<pre><code class="language-text">Source material
    ↓
Rust pipeline
    ↓
Normalized corpus
    ↓
High-signal dataset
    ↓
Training splits
    ↓
Model/fine-tune metadata
    ↓
Evaluation and validation reports
    ↓
Published dataset bundle

</code></pre>
<h6>Current children</h6>

















<table><thead><tr><th>Path</th><th>Current state</th></tr></thead><tbody><tr><td>DatasetPipelines\Winget</td><td>Existing Winget-manifest conversion work being drawn toward the formal pipeline model. The current directory is mixed Go/Python rather than a completed Rust pipeline and includes a compiled converter plus a roughly 533 MB winget_manifests-6.1.jsonl artifact. Treat this as migration/prototype work, not proof that the Rust pipeline standard is already complete.</td></tr><tr><td>DatasetPipelines\TinyLlama-HolyC</td><td>Rust/Cargo pipeline workspace with src, build output, transcripts, and both aptlantis.pipeline.toml and aptlantis.dataset.toml. This more closely reflects the intended repeatable pipeline shape.</td></tr></tbody></table>
<p>The root DatasetPipelines.manifest.toml describes an active 0.1.0 framework at roughly 75% completion, but those generated status fields should be reviewed alongside actual pipeline validation and reproducibility.</p>
<h5>10.9 FH-RefToolkit</h5>
<p>D:\CTS\FH-RefToolkit is the current home of the Flathub reference toolkit. Its working purpose is to:</p>
<ul>
<li>Parse Flathub AppStream/catalog data.</li>
<li>Query application metadata.</li>
<li>Generate lists of Flatpak references.</li>
<li>Download .flatpakref files for deployment or package-management workflows.</li>
<li>Support both packaged Python code and standalone scripts.
The directory contains src, StandAloneScripts, build output, Download.py, Query.py, a Dockerfile, Python project metadata, and two manifests: FH-RefToolkit.manifest.toml for the current container and FlathubRefs.manifest.toml for the underlying project identity.
Its current README still presents a polished “production/95%” FlathubRefs snapshot while the container manifest describes an experimental 0.0.0 command tool. This contradiction is exactly why the project needs a deliberate revisit: establish the canonical name, command surface, packaging model, tests, current Flathub API assumptions, and release evidence before updating status.</li>
</ul>
<h5>10.10 UTILITIES</h5>
<p>D:\CTS\UTILITIES collects narrow tools that are useful enough to preserve but do not need a large top-level project presence.
| Utility | Purpose and current shape |
| ------ | ------ |
| appstream_to_jsonl | Python converter for AppStream XML/catalog data into JSONL/Flatpak-ref-oriented records. Includes source and generated data, schema, README, and manifests. The checked-in XML and JSONL outputs are data artifacts and should be versioned intentionally. |
| dir_mapper | Directory/ecosystem mapping and graph-visualization experiments. Includes Python conversion, large graph JSON, DOT/SVG output, Linux genealogy datasets, crates data, and local HTML force-graph viewers. |
| extract_winget_manifests | Python iterations for converting Winget YAML manifests into JSON/JSONL, with conversion status, help text, and encoder tests. Overlaps materially with DatasetPipelines\Winget and should eventually have a documented source-of-truth relationship. |
| JSON-JSONL | Small Go converter between JSON and JSONL-oriented records, with sample crate and package-manifest inputs and a compiled executable. |
| platform_views | Rust-based generated/static platform view project with site, src, build output, and project manifest. Its exact supported views and command contract need deeper documentation. |
| search_and_copy | Minimal Go search-and-copy utility with source, module file, and help text. |
| svg_metadata | Python tool for applying or managing structured SVG metadata using an asset schema, override file, and sample assets. It should stay aligned with SESM expectations where applicable. |</p>
<p>Utility rules:</p>
<ul>
<li>Each tool should have its own help text or README, explicit inputs/outputs, and failure behavior.</li>
<li>Generated datasets and compiled binaries should be distinguishable from source.</li>
<li>Overlapping tools should name the authoritative implementation and migration path.</li>
<li>A utility that gains a stable external command contract can be promoted into a first-class CTS project without changing the meaning of its existing commands casually.</li>
</ul>
<h5>10.11 cts_holding — excluded and dormant work</h5>
<p>D:\CTS\cts_holding is the non-active reporting area for projects that should not appear in ordinary CTS evaluations, portfolio counts, or release dashboards.
| Path | Current role |
| ------ | ------ |
| cts_holding\EpicVideos | Media-production pipeline with Python package structure, tests, examples, output, and a manifest. Although its manifest calls it active/mostly stable, its physical holding classification is authoritative for portfolio inclusion. |
| cts_holding\GithubAcquisition | PowerShell-based ecosystem/repository acquisition work with workflow, schema, examples, and generated manifests. Retains an older D:\200-CTS manifest path. |
| cts_holding\PythonDocs | Preserved Python documentation project/material, including python-complete-6-1, README, and manifests. Currently concept-classified. |
| cts_holding\Training | Training/dataset experiments including RustForSmallModels and RustTrainingGemma4. Its manifest describes a completed Rust Corpus Forge dataset tool, but holding placement means it is excluded from current active reporting until reviewed. |
| cts_holding\ScriptWriters | Local LLM podcast/script generation system using Ollama and XTTS, with Python package code, tests, configuration, CPU/CUDA requirements, outputs, and a generated production-status manifest. It remains intentionally outside the active CTS surface. |</p>
<p>EpicVideos was listed separately in the planning notes, but the intended holding location is cts_holding\EpicVideos; it is documented only as held work.
Holding rules mirror drs_holding:</p>
<ul>
<li>Physical holding placement excludes a project from default evaluations even when an older manifest says active or production.</li>
<li>Holding does not mean abandoned; it means intentionally outside the current active portfolio.</li>
<li>Promotion requires a review of purpose, source state, documentation, command contract, tests, manifest, destination, and release posture.</li>
<li>Generated completion percentages do not override operator classification.</li>
</ul>
<h5>10.12 Portfolio relationships and maintenance rules</h5>
<p>The main CTS relationships are:</p>
<pre><code class="language-text">AptlantisLogos palettes ───────→ LangThemeGenerator themes

Winget source manifests ───────→ extract_winget_manifests
                         └──────→ DatasetPipelines\Winget

Flathub AppStream data ────────→ FH-RefToolkit
                         └──────→ UTILITIES\appstream_to_jsonl

Local project trees ───────────→ AnalyzeProjects evaluations

crates.io index ───────────────→ CloneCratesio mirror + metadata

</code></pre>
<p>Portfolio rules:</p>
<ul>
<li>Treat the Command Tool Standard as the command-behavior authority.</li>
<li>Read the project README, manifest, help output, and examples before changing a public command.</li>
<li>Verify generated status/completion fields against real tests and artifacts.</li>
<li>Keep model/API credentials out of repositories and document when source material is sent to a cloud model.</li>
<li>Preserve upstream attribution, data licensing, and source provenance.</li>
<li>Record reproducible inputs, transformations, validations, and outputs for dataset pipelines.</li>
<li>Avoid mixing human progress text into machine-readable stdout.</li>
<li>Require previews or explicit confirmation for destructive copy, overwrite, publish, delete, or mutation commands.</li>
<li>Exclude cts_holding from active portfolio reporting.</li>
<li>Keep large generated assets and datasets reproducible where practical; do not let a 258 MB HTML atlas or 533 MB JSONL file become the only surviving form of its source data.</li>
</ul>
<hr>
<h4>11. D:\DATA — shared datasets and source snapshots</h4>
<h5>11.1 Role and governance</h5>
<p>D:\DATA is the drive&#39;s shared dataset and source-snapshot store. It separates durable, reusable data products from the command tools and pipelines that produce, transform, validate, or consume them.
The distinction matters:</p>
<ul>
<li>D:\CTS contains executable pipelines and tooling.</li>
<li>D:\DATA contains their large data inputs, temporal snapshots, processed outputs, and reusable reference exports.</li>
<li>A dataset is not considered reproducible merely because its output files exist; its source, transformation, schema, statistics, dates, and validation evidence must remain identifiable.
D:\DATA\DATA.manifest.toml is the canonical root record. It establishes DDS as primary, registers the three current children, classifies crates.io and node.js as datasets and winget as a project group, and records the root ISO as an artifact.</li>
</ul>
<h5>11.2 Root map</h5>



































<table><thead><tr><th>Path</th><th>Role</th><th>Current contents</th></tr></thead><tbody><tr><td>D:\DATA\crates.io</td><td>Temporal crates.io ecosystem datasets.</td><td>January through April 2026 snapshots containing document-level and version-level JSONL, Parquet, source dumps, README documentation, and build statistics.</td></tr><tr><td>D:\DATA\node.js</td><td>Processed Node.js API documentation dataset.</td><td>A single output tree containing document-level and granular JSONL, granular Parquet, README documentation, and statistics.</td></tr><tr><td>D:\DATA\winget</td><td>Windows Package Manager catalog/reference snapshots.</td><td>Three large dated JSON exports, a local copy of Winget Export, and both directory- and dataset-level manifests.</td></tr><tr><td>D:\DATA\Win11_25H2_English_x64.iso</td><td>Uncategorized source artifact.</td><td>A 7,736,125,440-byte Windows 11 ISO currently stored directly at the DATA root. Its intended dataset/project relationship is not documented and should be reviewed.</td></tr><tr><td>D:\DATA\DATA.manifest.toml</td><td>Canonical root governance record.</td><td>Current-path APTlantis Entity Manifest v2.4 record with registered classifications and explicit verification gaps.</td></tr></tbody></table>
<h5>11.3 crates.io temporal datasets</h5>
<h6>Purpose</h6>
<p>D:\DATA\crates.io preserves monthly views of the evolving Rust package ecosystem. The datasets are derived from crates.io index data and retain both normal and yanked releases. That makes them useful for:</p>
<ul>
<li>Supply-chain and dependency analysis.</li>
<li>Ecosystem growth and evolution studies.</li>
<li>Resolver and version-history research.</li>
<li>Yanked-version and security-oriented analysis.</li>
<li>Retrieval, model-training, and code-intelligence experiments.</li>
<li>Reproducible comparison of the registry at different points in time.
The root cratesio.manifest.toml classifies the material as a DDS-governed data project but still points to the former D:\980-DATA\981-CRATESIO\cratesio location and nonexistent root documentation files.</li>
</ul>
<h6>Data views</h6>
<p>Each documented snapshot provides two complementary logical views:
| View | Unit | Intended use |
| ------ | ------ | ------ |
| <strong>Documents / macro</strong> | One record per crate, aggregating its release history. | Package lifecycle, maintenance, ecosystem context, and broader model context. |
| <strong>Granular / micro</strong> | One record per crate version. | Dependency resolution, version-specific analysis, feature/checksum inspection, yanked-release research, and fine-grained retrieval. |</p>
<p>The granular data is supplied as JSONL for streaming workflows and as Parquet for efficient columnar filtering and analytical queries. Document records preserve the full version history in a crate-level representation.</p>
<h6>Snapshot inventory</h6>













































<table><thead><tr><th>Snapshot</th><th>Source/build date</th><th>Unique crates</th><th>Versions</th><th>Yanked versions</th><th>Principal files</th></tr></thead><tbody><tr><td>jan-2026</td><td>Statistics generated February 5, 2026 from crates-1-29.26.jsonl.</td><td>222,152</td><td>1,934,833</td><td>92,972</td><td>crates_documents.jsonl, crates_granular.jsonl, crates_granular.parquet</td></tr><tr><td>feb-2026</td><td>February 14 source snapshot; statistics generated March 22, 2026.</td><td>227,133</td><td>1,980,440</td><td>93,534</td><td>Cratesio.2-14-26.jsonl, documents/granular JSONL, granular Parquet</td></tr><tr><td>mar-2026</td><td>March 15 source snapshot; statistics generated March 22, 2026.</td><td>238,012</td><td>2,071,078</td><td>95,933</td><td>Cratesio.03-15-26.jsonl, documents/granular JSONL, granular Parquet</td></tr><tr><td>apr-2026</td><td>April 17, 2026 snapshot/build.</td><td>254,393</td><td>2,211,049</td><td>98,778</td><td>crates_04-17-26.jsonl, dated documents/granular JSONL, dated Parquet</td></tr></tbody></table>
<p>The April statistics report a 4.47% yanked-version share. Directory names represent the intended temporal snapshot, while each STATS.md records the actual generation time and source filename; both should be retained because processing can occur after the source month.</p>
<h6>Snapshot files and storage posture</h6>
<p>Individual JSONL files are large—roughly 3.7 GB to 5.0 GB each—while the Parquet files are hundreds of megabytes. These should be treated as dataset artifacts rather than ordinary source files.
Each snapshot currently includes:</p>
<ul>
<li>A README describing provenance, methodology, schema, and intended use.</li>
<li>STATS.md with exact record counts and source/build information.</li>
<li>A crate-level documents JSONL view.</li>
<li>A version-level granular JSONL view.</li>
<li>A granular Parquet view.</li>
<li>For February through April, a dated/raw or precursor JSONL source artifact in the same snapshot directory.
January also contains a .git directory. That makes it the only monthly snapshot currently carrying repository metadata and should be a deliberate choice rather than an accidental difference between snapshots.</li>
</ul>
<h6>Relationship to CTS tooling</h6>
<p>The datasets are closely related to D:\CTS\CloneCratesio and the emerging dataset-pipeline work:</p>
<pre><code class="language-text">crates.io index / mirror metadata
    ↓
CloneCratesio acquisition and sidecar tools
    ↓
dataset transformation / flattening
    ↓
D:\DATA\crates.io\&lt;monthly snapshot&gt;
    ├── documents JSONL
    ├── granular JSONL
    ├── granular Parquet
    ├── README
    └── STATS.md

</code></pre>
<p>The monthly READMEs reference earlier processing locations such as src/process_crates.py and scripts/cmd. Those scripts are not present inside the current snapshot roots, so the canonical pipeline repository and exact command/version used for each build should be linked explicitly during normalization.</p>
<h5>11.4 node.js API dataset</h5>
<h6>Purpose</h6>
<p>D:\DATA\node.js\output contains a structured dataset derived from the official Node.js API documentation JSON. It flattens a large hierarchical documentation source into two model- and analysis-friendly views:
| File | Unit and purpose | Size |
| ------ | ------ | ------ |
| nodejs_documents.jsonl | Module-level records preserving high-level API context and nested content. | 723,690,415 bytes |
| nodejs_granular.jsonl | Individual functions, properties, events, and other API items for retrieval or instruction-oriented work. | 694,821,483 bytes |
| nodejs_granular.parquet | Columnar form of the granular dataset for DuckDB/Pandas-style filtering and analysis. | 153,811,230 bytes |
| README.md | Provenance, methodology, schemas, and use cases. | Documentation |
| STATS.md | Build date, source path, counts, and output inventory. | Documentation |</p>
<p>The February 2, 2026 statistics record:</p>
<ul>
<li>26,883 module/document records.</li>
<li>570,380 granular function/property/event records.
The document view supports broad conceptual association—for example, keeping related fs APIs together—while the granular view supports retrieval of a specific method, property, signature, or event. Parquet enables analytical questions such as filtering by stability classification or comparing API shapes across modules.</li>
</ul>
<h6>Provenance gaps</h6>
<p>output\README.md records the original source as datasets/raw/nodejs.all.json and the processor as src/process_nodejs.py, but neither the raw source nor the processor is present under the current D:\DATA\node.js root. The statistics also retain an older source path, d:/Projects/Datasets/raw/nodejs.all.json.
To make the dataset independently reproducible, the root should eventually identify:</p>
<ul>
<li>Exact Node.js documentation version or commit.</li>
<li>Source URL and acquisition date.</li>
<li>Source checksum.</li>
<li>Canonical processor repository and version.</li>
<li>Transformation command/configuration.</li>
<li>Schema version and validation results.</li>
<li>Licensing and redistribution terms for derived documentation data.</li>
</ul>
<h5>11.5 winget catalog data</h5>
<h6>Purpose</h6>
<p>D:\DATA\winget holds dated Windows Package Manager catalog exports plus a local copy of a third-party browsing/export interface. The data is useful for package discovery, manifest inspection, catalog analysis, list generation, ingestion experiments, and feeding Winget-oriented tools or datasets.</p>
<h6>Snapshot inventory</h6>





























<table><thead><tr><th>File</th><th>Date encoded in name</th><th>Contents</th><th>Size</th></tr></thead><tbody><tr><td>winget.all-2-23-26.json</td><td>February 23, 2026</td><td>Full package/version/installer-oriented records, including identifiers, versions, installer types, commands, dependencies, release dates, and installer metadata.</td><td>512,771,579 bytes</td></tr><tr><td>winget.locale-en-US-2-18-26.json</td><td>February 18, 2026</td><td>English (United States) package locale metadata such as identifiers, package names, publishers, authors, URLs, licenses, descriptions, and related fields.</td><td>192,555,051 bytes</td></tr><tr><td>winget.locale-en-US-2-23-26.json</td><td>February 23, 2026</td><td>Later English locale snapshot in the same general record family.</td><td>192,229,285 bytes</td></tr></tbody></table>
<p>These are JSON arrays rather than JSONL streams. Because each file is hundreds of megabytes, consumers should prefer streaming parsers or conversion to JSONL/Parquet instead of loading the entire array into memory without bounds.
The February 18 and February 23 locale files provide a natural temporal comparison, but the root currently has no README.md, STATS.md, checksums, record counts, acquisition commands, or schema note explaining exactly how the exports were generated.</p>
<h6>WingetExport</h6>
<p>D:\DATA\winget\WingetExport is a local clone of <a href="https://github.com/4lrick/winget-export">4lrick/winget-export</a>. The Git remote confirms that upstream identity.
The project provides a browser interface for:</p>
<ul>
<li>Searching the Winget package catalog.</li>
<li>Selecting and reordering packages.</li>
<li>Exporting selections as Winget JSON, PowerShell, or a command line.</li>
<li>Importing the generated JSON through winget import.</li>
<li>Rebuilding its local data\index.json package index.
It is useful as an upstream reference and operator convenience for grabbing package identifiers, export manifests, and installation lists. It is not an Aptlantis-authored project, and its MIT license and upstream attribution should remain intact.
The clone contains a static frontend, source, local data, a server component, assets, package metadata, a pnpm lockfile, and a GitHub Actions workflow that can update the package index. Its local WingetExport.manifest.toml is a generated Aptlantis inventory record, not an assertion of authorship or a replacement for the upstream project metadata.</li>
</ul>
<h6>Relationships to local tools</h6>
<pre><code class="language-text">Winget catalog/export data
    ├──→ D:\BASIC\QB-Winget
    ├──→ D:\DRS\AptlantisConsole Winget surface
    ├──→ D:\CTS\DatasetPipelines\Winget
    ├──→ D:\CTS\UTILITIES\extract_winget_manifests
    └──→ D:\DATA\winget\WingetExport

</code></pre>
<p>These consumers have different goals. The raw DATA snapshots should remain immutable inputs; transformations, UI-specific indexes, saved package lists, and generated training records should be written to distinct outputs with their own provenance.</p>
<h5>11.6 Data lifecycle and handling rules</h5>
<h6>Snapshot identity</h6>
<p>Every durable dataset snapshot should record:</p>
<ul>
<li>Canonical dataset name and schema version.</li>
<li>Source system, URL/repository, and source version or commit.</li>
<li>Acquisition date and transformation date.</li>
<li>Exact input filename and checksum.</li>
<li>Pipeline/tool version and invocation.</li>
<li>Record counts, validation results, and known exclusions.</li>
<li>Output filenames, sizes, and SHA-256 hashes.</li>
<li>License, redistribution constraints, and attribution.</li>
<li>Relationship to earlier and later snapshots.</li>
</ul>
<h6>Immutability and regeneration</h6>
<ul>
<li>Treat dated snapshots as immutable once published or consumed by downstream work.</li>
<li>Corrections should produce a clearly labeled replacement/revision rather than silently mutating a dated artifact.</li>
<li>Keep generated data reproducible from an identified source plus an identified pipeline version.</li>
<li>Do not rely on directory timestamps as dataset acquisition dates; preserve explicit dates in manifests and statistics.</li>
<li>Use streaming tools for multi-gigabyte JSON/JSONL data.</li>
<li>Prefer Parquet for repeated analytical filtering while retaining JSONL where portability and streaming matter.</li>
<li>Keep raw/source, normalized, granular, document-level, split, validation, and packaged outputs distinguishable.</li>
</ul>
<h6>Storage and integrity</h6>
<ul>
<li>Large data files should have recorded hashes; filenames and byte sizes alone do not establish identity.</li>
<li>Avoid copying multi-gigabyte snapshots casually between projects. Consumers should reference the shared DATA location or use a documented derived-data workflow.</li>
<li>A Git repository is not automatically appropriate for multi-gigabyte generated outputs; use a deliberate large-artifact or dataset publication strategy.</li>
<li>Verify available disk space before regeneration because pipelines may temporarily require source, intermediate, and final forms simultaneously.</li>
<li>Preserve README and statistics files with their matching snapshot.</li>
<li>Do not delete an older snapshot merely because a newer month exists; temporal comparison is part of the value.</li>
</ul>
<h5>11.7 Root ISO review item</h5>
<p>D:\DATA\Win11_25H2_English_x64.iso is not part of the crates.io, Node.js, or Winget datasets. A file with the same name and byte length was observed under D:\DRS\WinTrim, but matching name and size are not enough to prove identical content.
Before moving or deduplicating either copy:</p>
<ol>
<li>Compute and compare SHA-256 hashes.</li>
<li>Decide which project or source-media archive owns the canonical copy.</li>
<li>Update WinTrim documentation/configuration if its expected path changes.</li>
<li>Preserve licensing and redistribution boundaries.</li>
<li>Use a reference/link or documented shared-source relationship if both workflows need the same ISO.
No hash comparison or file relocation was performed during this documentation pass.</li>
</ol>
<hr>
<h4>12. D:\WDS — websites and web applications</h4>
<p>D:\WDS is the governed portfolio for websites and web applications. Its canonical standard is D:.library\aptlantis_core\WDS.
The active governance records are D:\WDS\AGENTS.md and D:\WDS\WDS.manifest.toml. Every active direct child is registered and has AGENTS.md, an entity-named manifest, and Project-README.md. .wds_holding is registered and excluded from active reporting.
| Project | Classification | Current shape |
| ------ | ------ | ------ |
| aptlantis-one | Project | Vite-based web application with client, server, public assets, and shared styling. |
| aptlantis-two | Project group | Contains independently governed aptlantis and webserver children. |
| linux-genealogy | Project | Linux genealogy web/data project with maintained data, reference material, and generated visualization output. |
| portfolio-website | Project | Next.js portfolio website with routes, components, data, hooks, styles, and public assets. |</p>
<p>The governance rollout establishes structure and authority, but each project still carries an explicit project-specific verification gap for current build, deployment, version, and lifecycle claims.</p>
<hr>
<h4>13. Scope boundary</h4>
<p>This document currently covers:</p>
<ol>
<li>The purpose, operating model, root contract, central documents, and central principles of D:.</li>
<li>The hidden foundation directories: .city_hall, .data, .dpw, .library, .pnpm-store, and .zoning.</li>
<li>The QB64 workshop and incubator at D:\BASIC.</li>
<li>The governed desktop-application portfolio at D:\DRS, including its WSL workshop and drs_holding area.</li>
<li>The command-tool portfolio at D:\CTS, including dataset pipelines, small utilities, and cts_holding.</li>
<li>The shared dataset store at D:\DATA, including crates.io temporal snapshots, Node.js API outputs, Winget catalog exports, and the uncategorized root ISO review item.</li>
<li>The website and web-application portfolio at D:\WDS, including the nested aptlantis-two project group.
No later root-directory group is documented yet. The next pass should begin from the next explicitly selected section rather than pulling unrelated directories into this one.</li>
</ol>




