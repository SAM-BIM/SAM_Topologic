# SAM_Topologic retirement notice - Q4 (2026-10-12)

Status: implemented on `docs/retirement-notice-q4`; owner review required. Not merged.
Base: `sow/2026-Q4` at `fca7ad19579fd5eea47303ea38176d139140dc51`.
PR: the live PR for this branch in `SAM-BIM/SAM_Topologic` (its number is not committed here).
Tested content SHA: `ce2edb1b9208fad608be7412f3d0a818038d41fe` (changes only README.md).
Final PR head and hosted check results: recorded in the live PR description. A record cannot contain its own commit SHA, so this file is the only change after the tested SHA.

## Change

Adds a retirement notice to the top of `README.md` on the active quarter branch. The repository is deprecated in favour of SAM_OCCT and is being archived on the owner's authorization (2026-10-12). A matching `master` notice is a separate PR (`master` requires a reviewing approval).

Evidence (see the PR description and `ARCHIVE_CANDIDATES_ASSESSMENT_2026-10-12.md`, machine-local): SAM_Deploy b1e6329 and d4e1d98 / SAM_Deploy#33 removed the submodule and every build entry because SAM_OCCT replaced it; SAM_Revit and SAM_Revit_UI CI comments say the same; no current build, project, workflow or submodule references remain.

## Validation

Local documentation checks only: `git diff --check` exit=0 at the tested SHA; changed files: README.md; `PROJECT_PROGRESS.md` untouched on this branch; README stays LF without BOM. Reproduce: `git diff --check <base> <tested>` and `git diff --name-only <base> <tested>`; the tested-to-final list contains only this record. Hosted checks are reported in the PR description, not asserted here.

## Remaining decisions and next step

Merge needs owner approval and passing final-head checks. After merge: a docs-only `[skip ci]` closeout in `PROJECT_PROGRESS.md` recording the deprecation, then guarded cleanup of `docs/retirement-notice-q4`; archiving follows the `master` notice.