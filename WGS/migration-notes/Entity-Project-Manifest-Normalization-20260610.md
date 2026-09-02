# Entity Project Manifest Normalization 20260610

## Summary

Normalized live project manifests so governed projects use entity-named files in their project roots, while the generic v2.4 template remains available only as the reusable schema/default pattern.

## Batch Scope

The following live project-root manifest files were normalized in this pass:

| Source | Target | Mode | Reason | Safety |
| --- | --- | --- | --- | --- |
| `D:\020-LIBRARY\020-LIBRARY.manifest.toml` | `D:\020-LIBRARY\DocHub.manifest.toml` | renamed in place | Preserve DocHub as an entity-named project record. | Safe, no root move |
| `D:\100-DRS\110-CRYPTO\Aegis\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\Aegis.manifest.toml` | archived duplicate | Entity-named `Aegis.manifest.toml` already existed as the live project record. | Safe, live manifest preserved |
| `D:\100-DRS\120-STORAGE\FileCabinet\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\FileCabinet.project.manifest.toml` | archived duplicate | Entity-named `FileCabinet.manifest.toml` already existed as the live project record. | Safe, live manifest preserved |
| `D:\100-DRS\130-ARCHIVAL\ChromeArchivalPlugin\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\ChromeArchivalPlugin.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\100-DRS\140-TAURI\AptlantisConsole\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\AptlantisConsole.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\100-DRS\140-TAURI\Structra\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\Structra.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\100-DRS\140-TAURI\Tauri-IT\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\Tauri-IT.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\100-DRS\150-QB\QB-Winget\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\QB-Winget.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\100-DRS\160-UTILITIES\ClipboardFilter\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\ClipboardFilter.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\100-DRS\160-UTILITIES\CommandWizard\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\CommandWizard.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\100-DRS\160-UTILITIES\WinTrim\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\WinTrim.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\210-CONVERSION\ConversionTools\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\ConversionTools.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\210-CONVERSION\LangThemeGenerator\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\LangThemeGenerator.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\220-API\CloneCratesio\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\CloneCratesio.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\230-HASHING\ArchiveHasher\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\ArchiveHasher.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\230-HASHING\ReleaseHasher\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\ReleaseHasher.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\240-DATA-PIPELINES\DatasetPipelines\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\DatasetPipelines.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\240-DATA-PIPELINES\Training\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\Training.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\250-DOCS-SCRIPTING\AnalyzeProjects\project.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\AnalyzeProjects.manifest.toml` | archived duplicate | Entity-named `AnalyzeProjects.manifest.toml` already existed as the live project record. | Safe, live manifest preserved |
| `D:\200-CTS\250-DOCS-SCRIPTING\PythonDocs\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\PythonDocs.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\250-DOCS-SCRIPTING\ScriptWriters\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\ScriptWriters.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\260-LLM\Llama\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\Llama.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\270-MEDIA\AptlantisLogos\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\AptlantisLogos.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\200-CTS\270-MEDIA\EpicVideos\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\EpicVideos.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |
| `D:\300-WDS\340-SITES\AAMHS\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\AAMHS.manifest.toml` | archived duplicate | Entity-named `AAMHS.manifest.toml` already existed as the live project record. | Safe, live manifest preserved |
| `D:\300-WDS\340-SITES\LinuxGenealogy\PROJECT.manifest.toml` | `D:\010-CITY-HALL\WGS\migration-notes\Legacy-Project-Manifests\LinuxGenealogy.manifest.toml` | archived duplicate | Entity-named live manifest already existed or was maintained separately. | Safe, live manifest preserved |

## Verification

- Live project roots no longer contain `PROJECT.manifest.toml` or `project.manifest.toml`.
- `D:\020-LIBRARY` now exposes `DocHub.manifest.toml` as the project record beside `DIRECTORY.manifest.toml`.
- Legacy manifest evidence remains available under `WGS\migration-notes\Legacy-Project-Manifests\`.
