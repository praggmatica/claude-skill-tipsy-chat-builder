#!/usr/bin/env python3
"""
Validate Claude Agent Skill files (SKILL.md) anywhere in the repository.

Checks every SKILL.md against the Agent Skills format:
  - YAML frontmatter present and parseable
  - required fields: name, description
  - name: lowercase alphanumeric + hyphens, max 64 chars, matches parent directory
  - description: non-empty string, max 1024 chars
  - optional fields have the expected types
  - body is non-empty and relative file references resolve
  - warns when the body exceeds the recommended 500 lines

Exits non-zero when any error is found. Warnings never fail the build.
Output uses GitHub Actions workflow annotations.

@since 1.0.0
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print('::error::PyYAML is required. Install with: pip install pyyaml')
    sys.exit(1)

NAME_PATTERN = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
NAME_MAX_LENGTH = 64
DESCRIPTION_MAX_LENGTH = 1024
RECOMMENDED_MAX_BODY_LINES = 500
EXCLUDED_DIRS = {'.git', 'node_modules', 'vendor', 'dist', 'build', '.code-helper'}

# fields accepted by the agent skills spec and the claude code runtime
KNOWN_FIELDS = {
    'name': str,
    'description': str,
    'license': str,
    'version': str,
    'metadata': dict,
    'allowed-tools': (str, list),
    'argument-hint': str,
    'disable-model-invocation': bool,
    'user-invocable': bool,
    'model': str,
    'context': str,
    'agent': str,
    'compatibility': (str, dict),
}

MARKDOWN_LINK_PATTERN = re.compile(r'\[[^\]]*\]\(([^)#?\s]+)[^)]*\)')


def find_skill_files(root):
    """
    Locate every SKILL.md under the given root, skipping excluded directories.

    @since 1.0.0
    @param root Path repository root to scan
    @return list of Path objects, sorted for stable output
    """
    results = []
    for path in root.rglob('SKILL.md'):
        if not EXCLUDED_DIRS.intersection(part for part in path.parts):
            results.append(path)
    return sorted(results)


def split_frontmatter(text):
    """
    Split a SKILL.md document into its frontmatter and body.

    @since 1.0.0
    @param text str full file contents
    @return tuple (frontmatter_str or None, body_str)
    """
    if not text.startswith('---'):
        return None, text
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.DOTALL)
    if not match:
        return None, text
    return match.group(1), match.group(2)


def annotate(level, path, message):
    """
    Print a GitHub Actions annotation for the given file.

    @since 1.0.0
    @param level str 'error' or 'warning'
    @param path Path file the annotation applies to
    @param message str annotation text
    @return void
    """
    print(f'::{level} file={path}::{message}')


def validate_name(value, path, errors, warnings):
    """
    Validate the name field format, length, and directory match.

    @since 1.0.0
    @param value mixed frontmatter name value
    @param path Path SKILL.md being validated
    @param errors list collector for error messages
    @param warnings list collector for warning messages
    @return void
    """
    if not isinstance(value, str) or not value.strip():
        errors.append("'name' must be a non-empty string")
        return
    if len(value) > NAME_MAX_LENGTH:
        errors.append(f"'name' exceeds {NAME_MAX_LENGTH} characters ({len(value)})")
    if not NAME_PATTERN.match(value):
        errors.append(
            f"'name: {value}' is invalid — use lowercase letters, digits, and single hyphens "
            '(e.g. tipsy-chat-builder)'
        )
    parent = path.parent.name
    if path.parent != path.parent.parent and parent != value and parent not in ('', '.'):
        # skip the repo root, where the checkout directory name is not meaningful
        if (path.parent / '.git').exists() or str(path.parent) == '.':
            warnings.append(f"'name: {value}' does not match repository root directory — verify intentional")
        else:
            errors.append(f"'name: {value}' must match its directory name '{parent}'")


def validate_description(value, errors, warnings):
    """
    Validate the description field content and length.

    @since 1.0.0
    @param value mixed frontmatter description value
    @param errors list collector for error messages
    @param warnings list collector for warning messages
    @return void
    """
    if not isinstance(value, str) or not value.strip():
        errors.append("'description' must be a non-empty string")
        return
    if len(value) > DESCRIPTION_MAX_LENGTH:
        errors.append(f"'description' exceeds {DESCRIPTION_MAX_LENGTH} characters ({len(value)})")
    if len(value.strip()) < 20:
        warnings.append("'description' is very short — include what the skill does and when to use it")


def validate_optional_fields(frontmatter, errors, warnings):
    """
    Type-check optional frontmatter fields and flag unknown ones.

    @since 1.0.0
    @param frontmatter dict parsed frontmatter mapping
    @param errors list collector for error messages
    @param warnings list collector for warning messages
    @return void
    """
    for key, value in frontmatter.items():
        if key in ('name', 'description'):
            continue
        expected = KNOWN_FIELDS.get(key)
        if expected is None:
            warnings.append(f"unknown frontmatter field '{key}' — not part of the Agent Skills spec")
        elif not isinstance(value, expected):
            expected_names = (
                expected.__name__ if isinstance(expected, type)
                else ' or '.join(t.__name__ for t in expected)
            )
            errors.append(f"'{key}' must be of type {expected_names}, got {type(value).__name__}")


def validate_body(body, path, errors, warnings):
    """
    Validate the markdown body: non-empty, sane length, resolvable references.

    @since 1.0.0
    @param body str markdown content after the frontmatter
    @param path Path SKILL.md being validated
    @param errors list collector for error messages
    @param warnings list collector for warning messages
    @return void
    """
    if not body.strip():
        errors.append('body is empty — a skill needs instructions after the frontmatter')
        return
    line_count = body.count('\n') + 1
    if line_count > RECOMMENDED_MAX_BODY_LINES:
        warnings.append(
            f'body is {line_count} lines — keep SKILL.md under {RECOMMENDED_MAX_BODY_LINES} lines '
            'and move detail into referenced files'
        )
    for match in MARKDOWN_LINK_PATTERN.finditer(body):
        target = match.group(1)
        if '://' in target or target.startswith(('mailto:', 'data:', '/')):
            continue
        if not (path.parent / target).exists():
            errors.append(f"referenced file '{target}' does not exist relative to {path.parent}")


def validate_skill(path):
    """
    Run all checks against a single SKILL.md file.

    @since 1.0.0
    @param path Path SKILL.md to validate
    @return tuple (errors list, warnings list)
    """
    errors = []
    warnings = []
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return (['file is not valid UTF-8'], warnings)

    frontmatter_str, body = split_frontmatter(text)
    if frontmatter_str is None:
        errors.append("missing YAML frontmatter — file must start with '---'")
        return (errors, warnings)

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as exc:
        errors.append(f'frontmatter is not valid YAML: {exc}')
        return (errors, warnings)

    if not isinstance(frontmatter, dict):
        errors.append('frontmatter must be a YAML mapping of key: value pairs')
        return (errors, warnings)

    if 'name' not in frontmatter:
        errors.append("missing required field 'name'")
    else:
        validate_name(frontmatter['name'], path, errors, warnings)

    if 'description' not in frontmatter:
        errors.append("missing required field 'description'")
    else:
        validate_description(frontmatter['description'], errors, warnings)

    validate_optional_fields(frontmatter, errors, warnings)
    validate_body(body, path, errors, warnings)
    return (errors, warnings)


def main():
    """
    Entry point: validate every SKILL.md and report results.

    @since 1.0.0
    @return int process exit code
    """
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    skill_files = find_skill_files(root)

    if not skill_files:
        print('::notice::No SKILL.md files found — nothing to validate yet.')
        return 0

    total_errors = 0
    for path in skill_files:
        errors, warnings = validate_skill(path)
        rel = path.relative_to(root)
        for message in warnings:
            annotate('warning', rel, message)
        for message in errors:
            annotate('error', rel, message)
        status = 'FAIL' if errors else 'OK'
        print(f'[{status}] {rel} ({len(errors)} errors, {len(warnings)} warnings)')
        total_errors += len(errors)

    print(f'\nValidated {len(skill_files)} skill file(s), {total_errors} error(s).')
    return 1 if total_errors else 0


if __name__ == '__main__':
    sys.exit(main())
