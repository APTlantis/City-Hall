"""Fail closed on missing or pending release-stage evidence."""
from datetime import date
from pathlib import Path
import tomllib

STAGES = ('build-package', 'install-upgrade', 'runtime', 'migration', 'integrity')


def check_evidence(root, manifest):
    errors = []
    root = root.resolve()
    rel = manifest.get('release', {}).get('verified', {}).get('stage_evidence', '')
    try:
        record = (root / rel).resolve()
        if not rel or not record.is_relative_to(root):
            return ['release.verified.stage_evidence must name a project-local TOML record']
        evidence = tomllib.loads(record.read_text(encoding='utf-8'))
        if evidence.get('version') != manifest.get('release', {}).get('version'):
            errors.append('stage evidence version does not match release.version')
        artifact = manifest.get('release', {}).get('installer', {})
        if not artifact.get('sha256') or evidence.get('artifact_sha256', '').lower() != artifact['sha256'].lower():
            errors.append('stage evidence must bind the exact installer SHA256')
        stages = evidence.get('stages', {})
        for name in STAGES:
            stage = stages.get(name, {})
            status = stage.get('status')
            if status == 'not-applicable' and name == 'migration':
                if not stage.get('reason') or not stage.get('reviewer'):
                    errors.append('migration waiver requires reason and reviewer')
            elif status != 'pass':
                errors.append(f'{name}: stage must pass (observed {status!r})')
            try:
                date.fromisoformat(stage.get('date', ''))
            except (ValueError, TypeError):
                errors.append(f'{name}: ISO date required')
            log = (root / stage.get('log', '')).resolve()
            if not log.is_relative_to(root) or not log.is_file() or not log.stat().st_size:
                errors.append(f'{name}: nonempty project-local evidence log required')
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        errors.append(f'invalid release-stage evidence: {exc}')
    return errors
