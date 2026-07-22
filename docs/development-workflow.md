# Development Workflow

This document defines the standard development workflow for **HealthInsight**.

Follow this workflow before creating every Git commit.

---

# 1. Complete Phase Tasks

Before committing:

- Verify all planned tasks for the current phase are completed.
- Review the corresponding checklist in `roadmap.md`.
- Ensure the implementation matches the project goals.

---

# 2. Update Documentation

Review and update documentation when necessary:

- `README.md`
- `docs/roadmap.md`
- `docs/features.md`
- `docs/user-flow.md`
- `docs/database-design.md`
- `docs/architecture.md`

Documentation should always reflect the current project state.

---

# 3. Check Project Structure

Verify that:

- Folder structure is correct.
- No temporary files exist.
- No unnecessary files are included.
- Required project files are present.

Example:

```bash
tree
```

---

# 4. Review Git Changes

Check repository status:

```bash
git status
```

Review modifications:

```bash
git diff
```

Verify that:

- Only intended files are modified.
- No accidental changes exist.
- No generated or temporary files are included.

---

# 5. Code Quality

## Ruff

Ruff is responsible for:

- Linting
- Import sorting
- Automatic fixes

Run:

```bash
ruff check . --fix
```

Review any automatic fixes before committing.

---

## Ruff Formatter

Format the project:

```bash
ruff format .
```

Review formatting changes before committing.

---

# 6. Testing

Run the complete test suite:

```bash
pytest
```

Verify that:

- All tests pass.
- No unexpected failures remain.
- New functionality includes appropriate tests.

---

# 7. Final Documentation Review

Before committing, verify whether any documentation requires updates:

- `README.md`
- `docs/roadmap.md`
- `docs/features.md`
- `docs/database-design.md`
- `docs/architecture.md`

---

# 8. Final Review

Confirm the following:

- [ ] Feature is complete.
- [ ] Ruff passes without errors.
- [ ] Project is correctly formatted.
- [ ] All tests pass.
- [ ] Documentation is updated if necessary.
- [ ] No temporary files remain.
- [ ] No sensitive information is included.
- [ ] Git status contains only intended changes.

---

# 9. Commit

Stage the required files:

```bash
git add <files>
```

Create a meaningful commit message:

```bash
git commit -m "feat(repository): implement MedicationRepository"
```

Examples:

```text
feat(repository): implement MedicationRepository
fix(database): resolve relationship loading issue
refactor(models): simplify validation logic
test(repository): add MedicationRepository tests
docs: update development workflow
build: add pyproject configuration
```

---

# 10. Push to GitHub

Push the changes:

```bash
git push
```

Verify the repository on GitHub after the push.

---

# Phase Completion Checklist

Before marking a phase as completed:

- [ ] All planned tasks are finished.
- [ ] Code has been reviewed.
- [ ] Ruff passes successfully.
- [ ] Project formatting is clean.
- [ ] All tests pass.
- [ ] Documentation is updated.
- [ ] Changes are committed.
- [ ] Changes are pushed to GitHub.
- [ ] Roadmap status is updated.
- [ ] No passwords, API keys, or private data are included.

Only after completing this checklist should the phase status be changed to **Completed**.
