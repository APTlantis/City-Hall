# [AppName] — Data Migration Contract

**Migration:** v[FROM] schema → v[TO] schema
**Application release:** [AppName] v[X.Y.Z]
**Document status:** [Draft / Final]
**Date:** [YYYY-MM-DD]

This document defines the contract for migrating [AppName] data from schema version [FROM] to schema version [TO]. It must be written and reviewed before the release that introduces the schema change ships.

---

## Why This Migration Exists

[One paragraph: what changed in the data format and why. Link to the feature or fix that required the change.]

---

## Schema Versions

| Field | Previous (v[FROM]) | New (v[TO]) |
|-------|--------------------|-------------|
| Schema version identifier | `[FROM]` | `[TO]` |
| Storage format | [e.g. SQLite / JSON / binary] | [e.g. same / changed to ...] |
| Location | [e.g. %APPDATA%\AppName\data.db] | [e.g. same / moved to ...] |

### Changed Fields

| Field / Table | Change | Notes |
|---------------|--------|-------|
| [e.g. `records.created_at`] | [e.g. Added — ISO 8601 timestamp] | [e.g. Backfilled with file creation time for existing records] |
| [e.g. `vault.version`] | [e.g. Changed from integer to string] | [e.g. "1" becomes "1.0"] |
| [e.g. `settings.theme`] | [e.g. Removed] | [e.g. Replaced by `settings.appearance.theme`] |

### Unchanged Fields

[List fields that are preserved exactly — or state "All other fields are unchanged."]

---

## Migration Trigger

The migration runs when:

* [e.g. The application detects schema version [FROM] on startup]
* [e.g. The user explicitly runs `AppName.exe migrate`]
* [e.g. The installer upgrade runs the migration during install]

The application reads the schema version from: `[field name and location, e.g. the "version" field in the header of data.db]`

If the schema version is already `[TO]`, migration is skipped silently.

If the schema version is **higher than `[TO]`**, the application refuses to open the data and displays an error. Downgrade is not supported.

---

## Migration Steps

The migration is performed in this order:

1. **Pre-migration backup**
   * Copy `[data path]` to `[backup path, e.g. data.db.pre-vX.Y.Z.bak]` before any changes
   * If backup fails, abort migration
   * Backup is not deleted automatically — the user may remove it manually

2. **[Step name, e.g. Add created_at column]**
   * [Exact SQL, JSON transformation, or file operation]
   * [How existing records are handled: backfill value, null, default]

3. **[Step name]**
   * [...]

4. **Update schema version marker**
   * Write `[TO]` to `[field name and location]`

5. **Verify**
   * [What is checked after migration to confirm success]

---

## Rollback

**Is rollback supported?** [Yes / No]

[If yes:]
Rollback restores the pre-migration backup:
* Stop the application
* Delete `[data path]`
* Rename `[backup path]` to `[data path]`
* Install [AppName] v[FROM] (the previous release)

[If no:]
Rollback is not supported. The pre-migration backup (`[backup path]`) is preserved and can be used to restore data manually, but downgrading the application is not tested or recommended.

---

## Failure Behavior

| Failure Point | Behavior |
|---------------|---------|
| Backup fails before migration starts | Abort; leave data untouched; display error |
| Migration step fails mid-way | Roll back to backup; display error with backup path |
| Schema version unrecognized (too old) | Refuse to open; display migration instructions |
| Schema version too new | Refuse to open; display upgrade instructions |
| Backup file is missing at rollback time | Display error; do not overwrite current data |

The application does not silently ignore migration failures. Every failure surfaces a message with the backup path and next steps.

---

## Testing Requirements

Before shipping this release:

- [ ] Migration tested on a fresh install (no existing data) — no migration should run
- [ ] Migration tested on data at schema v[FROM] — migration completes successfully
- [ ] Migrated data passes format validation
- [ ] Rollback tested — restored backup opens correctly in [AppName] v[FROM]
- [ ] Migration tested on corrupted / partial data — fails safely without deleting backup
- [ ] Uninstall after migration — backup file behavior documented
- [ ] Test count recorded (must not have dropped from previous release)

---

## Operator Guidance

[What an operator should know before upgrading. What they should back up. Whether they need to do anything manually.]

* **Before upgrading:** [e.g. "No action required. The application backs up your data automatically during migration."]
* **After upgrading:** [e.g. "Verify your data is intact. The backup at [backup path] may be deleted once you are satisfied."]
* **If something goes wrong:** [e.g. "Do not delete the backup file. Contact [maintainer] before taking further action."]

---

## Change Log

| Version | Change | Date |
|---------|--------|------|
| v[X.Y.Z] | Initial document for v[FROM] → v[TO] migration | [YYYY-MM-DD] |
