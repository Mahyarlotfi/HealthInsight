# Development Workflow

This document defines the standard workflow for developing HealthInsight.

The workflow should be followed at the end of each development phase and before creating a Git commit.

---

# 1. Complete Phase Tasks

Before committing:

- Verify all planned tasks for the phase are completed.
- Review the phase checklist in `roadmap.md`.
- Confirm the implementation matches the project goals.

---

# 2. Update Documentation

Review and update documentation if needed:

- `README.md`
- `docs/roadmap.md`
- `docs/features.md`
- `docs/user-flow.md`
- `docs/database-design.md`
- `docs/architecture.md`

Documentation must reflect the current project state.

---

# 3. Check Project Structure

Verify:

- Folder structure is correct.
- No unnecessary files exist.
- Temporary files are removed.
- Required files are present.

Example:

```bash
tree
```

---

# 4. Git Review Before Commit

Check current changes:

```bash
git status
```

Review changes:

```bash
git diff
```

Check modified files carefully:

- Confirm only expected files are changed.
- Check for accidental changes.
- Check file names and structure.
- Remove unnecessary files.

---

# 5. Code Quality Check

## Black

Black is an automatic Python code formatter.

### Purpose

- Keep code style consistent.
- Automatically format Python files.
- Reduce formatting discussions during development.

### Run

```bash
black .
```

### After running Black

- Review changed files.
- Include formatting changes in the commit if they are intentional.

---

## isort

isort automatically sorts Python imports.

### Purpose

- Keep imports organized.
- Maintain consistent import order.
- Improve code readability.

### Run

```bash
isort .
---

## Pylint

Pylint is a Python code quality checker.

### Purpose

- Detect programming errors.
- Identify code smells.
- Check coding standards.
- Improve maintainability.

### Run

```bash
pylint src/
```

### Review

- Errors must be fixed.
- Important warnings should be addressed.
- Minor warnings can be reviewed and documented if intentional.

---

## Code Quality Rules

Before committing code:

- Run Black for formatting.
- Run Pylint for quality checks.
- Fix important issues.
- Review all automatic changes.
- Commit only after code quality checks are complete.

# 6. Testing

Run project tests:

```bash
pytest
```

Verify:

- All tests pass.
- No errors remain.
- New features have appropriate tests.

---

# 7. Final Review

Confirm:

- [ ] Code works correctly.
- [ ] Tests pass.
- [ ] Documentation is updated.
- [ ] No temporary files exist.
- [ ] No sensitive information is included.
- [ ] Git status shows only intended changes.

---

# 8. Commit

Create a meaningful commit message:

```bash
git add <files>

git commit -m "Complete phase 1 planning documentation"
```

Examples:

```text
Add database design documentation

Update project roadmap

Implement medication model

Fix validation errors
```

---

# 9. Push to GitHub

After successful commit:

```bash
git push
```

Verify the repository on GitHub.

---

# Phase Completion Checklist

Before marking a phase as completed:

- [ ] All phase tasks are finished.
- [ ] Code has been reviewed.
- [ ] Documentation is updated.
- [ ] Tests are passing.
- [ ] Changes are committed.
- [ ] Changes are pushed to GitHub.
- [ ] Roadmap status is updated.
- [ ] No passwords, API keys, or private data are included.

Only after completing this checklist, the phase status can be changed to **Completed**.