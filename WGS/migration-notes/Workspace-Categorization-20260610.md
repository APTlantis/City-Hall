# Workspace Categorization 20260610

## Summary

Created the numbered category structure under DRS, CTS, WDS, and DATA, then moved clear project/data roots into those categories. Ambiguous top-level service/cache roots were not moved.

## Moves

| Source | Target | Result | Reason |
| --- | --- | --- | --- |
| `D:\100-DRS\110-ARCHIVAL` | `D:\100-DRS\130-ARCHIVAL` | moved | Renumber archival category to avoid collision with 110-CRYPTO. |
| `D:\100-DRS\ChromeArchivalPlugin` | `D:\100-DRS\130-ARCHIVAL\ChromeArchivalPlugin` | moved | Archival desktop project. |
| `D:\100-DRS\AptlantisConsole` | `D:\100-DRS\140-TAURI\AptlantisConsole` | moved | Tauri or webview desktop application. |
| `D:\100-DRS\DataVisualizer` | `D:\100-DRS\140-TAURI\DataVisualizer` | moved | Tauri or webview desktop application. |
| `D:\100-DRS\Structra` | `D:\100-DRS\140-TAURI\Structra` | moved | Tauri or webview desktop application. |
| `D:\100-DRS\Tauri-IT` | `D:\100-DRS\140-TAURI\Tauri-IT` | moved | Tauri or webview desktop application. |
| `D:\100-DRS\Tauri-Visualizers` | `D:\100-DRS\140-TAURI\Tauri-Visualizers` | moved | Tauri or webview desktop application. |
| `D:\100-DRS\Hubris` | `D:\100-DRS\140-TAURI\Hubris` | moved | Tauri or webview desktop application. |
| `D:\100-DRS\QB-7Zip` | `D:\100-DRS\150-QB\QB-7Zip` | moved | QB-related desktop utility project. |
| `D:\100-DRS\QB-Veracrypt` | `D:\100-DRS\150-QB\QB-Veracrypt` | moved | QB-related desktop utility project. |
| `D:\100-DRS\QB-Winget` | `D:\100-DRS\150-QB\QB-Winget` | moved | QB-related desktop utility project. |
| `D:\100-DRS\ClipboardFilter` | `D:\100-DRS\160-UTILITIES\ClipboardFilter` | moved | General desktop utility project. |
| `D:\100-DRS\CommandWizard` | `D:\100-DRS\160-UTILITIES\CommandWizard` | moved | General desktop utility project. |
| `D:\100-DRS\ProjectTracking` | `D:\100-DRS\160-UTILITIES\ProjectTracking` | moved | General desktop utility project. |
| `D:\100-DRS\WinTrim` | `D:\100-DRS\160-UTILITIES\WinTrim` | moved | General desktop utility project. |
| `D:\100-DRS\WSL` | `D:\100-DRS\160-UTILITIES\WSL` | moved | General desktop utility project. |
| `D:\200-CTS\appstream_to_jsonl` | `D:\200-CTS\210-CONVERSION\appstream_to_jsonl` | moved | Conversion or transformation command tool. |
| `D:\200-CTS\ConversionTools` | `D:\200-CTS\210-CONVERSION\ConversionTools` | moved | Conversion or transformation command tool. |
| `D:\200-CTS\LangThemeGenerator` | `D:\200-CTS\210-CONVERSION\LangThemeGenerator` | moved | Conversion or transformation command tool. |
| `D:\200-CTS\CloneCratesio` | `D:\200-CTS\220-API\CloneCratesio` | moved | API acquisition or reference toolkit command project. |
| `D:\200-CTS\GithubAcquisition` | `D:\200-CTS\220-API\GithubAcquisition` | moved | API acquisition or reference toolkit command project. |
| `D:\200-CTS\FH-RefToolkit` | `D:\200-CTS\220-API\FH-RefToolkit` | moved | API acquisition or reference toolkit command project. |
| `D:\200-CTS\ArchiveHasher` | `D:\200-CTS\230-HASHING\ArchiveHasher` | moved | Hashing/integrity command tool. |
| `D:\200-CTS\ReleaseHasher` | `D:\200-CTS\230-HASHING\ReleaseHasher` | moved | Hashing/integrity command tool. |
| `D:\200-CTS\DatasetPipelines` | `D:\200-CTS\240-DATA-PIPELINES\DatasetPipelines` | moved | Dataset/training pipeline command project. |
| `D:\200-CTS\Training` | `D:\200-CTS\240-DATA-PIPELINES\Training` | moved | Dataset/training pipeline command project. |
| `D:\200-CTS\AnalyzeProjects` | `D:\200-CTS\250-DOCS-SCRIPTING\AnalyzeProjects` | moved | Documentation, analysis, or scripting command project. |
| `D:\200-CTS\PythonDocs` | `D:\200-CTS\250-DOCS-SCRIPTING\PythonDocs` | moved | Documentation, analysis, or scripting command project. |
| `D:\200-CTS\ScriptWriters` | `D:\200-CTS\250-DOCS-SCRIPTING\ScriptWriters` | moved | Documentation, analysis, or scripting command project. |
| `D:\200-CTS\Llama` | `D:\200-CTS\260-LLM\Llama` | moved | LLM-related command tooling. |
| `D:\200-CTS\AptlantisLogos` | `D:\200-CTS\270-MEDIA\AptlantisLogos` | moved | Media generation or asset command tooling. |
| `D:\200-CTS\EpicVideos` | `D:\200-CTS\270-MEDIA\EpicVideos` | moved | Media generation or asset command tooling. |
| `D:\300-WDS\aptlantis_net` | `D:\300-WDS\310-aptlantis.net\aptlantis_net` | moved | Canonical aptlantis.net website project. |
| `D:\300-WDS\aptlantis_studio` | `D:\300-WDS\320-aptlantis.studio\aptlantis_studio` | moved | Canonical aptlantis.studio website project. |
| `D:\300-WDS\aptlantis` | `D:\300-WDS\330-TEMPLATE\aptlantis` | moved | Template or starter web project. |
| `D:\300-WDS\AAMHS` | `D:\300-WDS\340-SITES\AAMHS` | moved | Additional website project. |
| `D:\300-WDS\LinuxGenealogy` | `D:\300-WDS\340-SITES\LinuxGenealogy` | moved | Additional website project. |
| `D:\300-WDS\webserver` | `D:\300-WDS\390-SERVER\webserver` | moved | Website server infrastructure project. |
| `D:\980-DATA\cratesio` | `D:\980-DATA\981-CRATESIO\cratesio` | moved | Crates.io data asset. |
| `D:\980-DATA\nodejs` | `D:\980-DATA\982-NODEJS\nodejs` | moved | Node.js data asset. |
| `D:\980-DATA\winget` | `D:\980-DATA\983-WINGET\winget` | moved | Winget data asset. |
| `D:\980-DATA\WingetExport` | `D:\980-DATA\983-WINGET\WingetExport` | moved | Winget data asset. |

## Follow-Up

- Review generated entity-named project manifests for project-specific metadata.
- Decide whether any remaining service roots such as `.hf` and `.ollama` should be redirected into DPW after application-level verification.
