# WGS Suite Map

## Suite Layer

WGS is indexed by `WGS.manifest.toml`, `README.md`, and `Workspace Governance Standard.md`.

```mermaid
flowchart TB
    Suite["WGS standard suite"]
    Manifest["WGS.manifest.toml"]
    Readme["README.md"]
    Spec["Workspace Governance Standard.md"]

    Suite --> Manifest
    Suite --> Readme
    Suite --> Spec
```

## Adopter Layer

Workspace adopters use the manifest templates in `templates/`: workspace, directory, project, and standard manifests.

```mermaid
flowchart LR
    Workspace["Workspace"]
    Directory["Directory"]
    Project["Project"]
    Standard["Standard"]
    Templates["templates/"]

    Templates --> Workspace
    Templates --> Directory
    Templates --> Project
    Templates --> Standard
```

## Validation Layer

Validate workspace health with `Validation-Checklist.md`, `Workspace-Inventory.md`, `Target-Directory-Map.md`, and `Agent-Startup-Procedure.md`.

```mermaid
flowchart LR
    Inventory["Workspace-Inventory.md"]
    Target["Target-Directory-Map.md"]
    Startup["Agent-Startup-Procedure.md"]
    Checklist["Validation-Checklist.md"]
    Health["Workspace health judgment"]

    Inventory --> Checklist
    Target --> Checklist
    Startup --> Checklist
    Checklist --> Health
```
