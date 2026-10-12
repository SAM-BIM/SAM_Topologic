# Project Progress - SAM_Topologic (2026-Q4)

## Q4 retirement notice and deprecation closeout (final) - 2026-10-12

- SAM-BIM/SAM_Topologic#13 merged as `1d78e99be165ea268319cd8872b680eb822ce808` (merge commit pinned to approved head `1a3d414eca6a0748666fc5f612e1839c1c28add0`; base `sow/2026-Q4` `fca7ad19579fd5eea47303ea38176d139140dc51`; validated content `ce2edb1b9208fad608be7412f3d0a818038d41fe`). Owner-authorized 2026-10-12.
- Docs only: README.md, plus the record `docs/Agent-Continuity-RetirementNotice-Q4.md`. The README now carries a retirement notice. SAM_Topologic is deprecated and replaced by SAM_OCCT: SAM_Deploy b1e6329 (2026-07-28) and d4e1d98 / SAM_Deploy#33 (2026-08-02) removed its submodule and every build entry, and SAM_Revit / SAM_Revit_UI CI comments record that SAM_OCCT replaced it; no current build, project, workflow or submodule references it. Preserved on purpose: SAM_Revit_UI's post-build deletion of stale Topologic DLLs (upgrade cleanup), all branches (master, sow/2026-Q3, this branch) and local checkouts/worktrees. No product code, build, workflow, dependency pin, gitlink or tool changed.
- Validation: local documentation checks and commands are in `docs/Agent-Continuity-RetirementNotice-Q4.md` (`git diff --check`, file scope, LF, no BOM). Hosted checks at the approved head: build success (run 38285798336); spdx success (run 38285798187). Dependency selection: dependency clones in the build log: SAM @ sow/2026-Q4.
- Cleanup: remote docs/retirement-notice-q4 deleted with an expected-SHA lease on 1a3d414eca6a0748666fc5f612e1839c1c28add0 after confirming it is contained in sow/2026-Q4 and no open PR uses it as head or base; the local branch and its worktree are preserved (worktree in use). Other branches, worktrees and the frozen quarters were not touched.
- Remaining gaps: no agent-client behaviour or token benchmark has been run.
- Exact next step: archive the repository (authorized 2026-10-12) once the matching `master` README notice PR is merged by an approving reviewer (`master` requires one review). This is the final Q4 closeout: an archived repository accepts no further commits, so the archive result is recorded in the owner's machine-local workspace checkpoint and the SAM rollout/assessment notes. To revive, unarchive and make a new owner decision.

## Q4 AGENTS.md progress-file correction closeout - 2026-10-12

- SAM-BIM/SAM_Topologic#11 merged as `149ac5008a26e6a3c19689a21efa91248df145e1` (merge commit pinned to approved head `c463bf6e14443d5727ffce33973b4f0b270c3488`; base `sow/2026-Q4` `428de5dc9719dba5486e9fdb0c7033ad0788d62c`; validated content `e1e3458084c7b0013d2612b220942c08417d9019`). Owner-approved 2026-10-12.
- Docs only: AGENTS.md, plus the record `docs/Agent-Continuity-ProgressFile-Fix-Q4.md`. `AGENTS.md` now reads the existing `PROJECT_PROGRESS.md` (step 2 and the continuity paragraph) instead of claiming the file is missing and asking for bootstrap approval; the branch-creation history is kept and notes the progress file was created on 2026-10-12. No product code, build, workflow, dependency pin or tool changed; this closeout is the only `PROJECT_PROGRESS.md` change in this task.
- Validation: local documentation checks and commands are in `docs/Agent-Continuity-ProgressFile-Fix-Q4.md` (each replaced passage matched exactly once, no stale phrasing left, `git diff --check`, LF, no BOM). Hosted checks at the approved head: build success (run 38282371908); spdx success (run 38282371904). Dependency selection: dependency clones in the build log: SAM @ sow/2026-Q4.
- Cleanup: remote docs/agent-instructions-progress-file-fix-q4 deleted with an expected-SHA lease on c463bf6e14443d5727ffce33973b4f0b270c3488 after confirming it is contained in sow/2026-Q4 and no open PR uses it as head or base; the local branch and its worktree are preserved (worktree in use). Other branches, worktrees and the frozen quarters were not touched.
- Remaining gaps: no agent-client behaviour or token benchmark has been run.
- Exact next step: continue from the shared `AGENTS.md` and this file; the owner sets Q4 priorities for this repository.

## Q4 agent instructions rollout closeout - 2026-10-12

- SAM-BIM/SAM_Topologic#10 merged as `8839d525b75e507e028a962c527ffe0e435a4120` (merge commit pinned to approved head `517282ba63afc50b002abcf17ae5f0f4fbaf49ef`; base `sow/2026-Q4` `d75653c9a0efcfbd667247acc715b80ab7e7d9bb`; validated content `baea9f60e3160d4178811f2b0bdd584538df90c0`). Owner-authorized 2026-10-12 after an independent review (`AGENT_ROLLOUT_REVIEW_2026-10-12.md`, local to the owner's workspace, not committed).
- Docs only: AGENTS.md, CLAUDE.md, plus the rollout record `docs/Agent-Continuity-Rollout-Q4.md`. No product code, build, workflow, dependency pin or tool changed; this closeout is the only `PROJECT_PROGRESS.md` change.
- This closeout creates `PROJECT_PROGRESS.md` for this repository (owner-authorized 2026-10-12 as a post-merge docs-only `[skip ci]` commit; no other file changed). Earlier Q4 work (the merged icon migration, merge `d75653c`) predates this file and is recorded in Git history and the closed PR.
- Validation: local documentation checks and commands are in `docs/Agent-Continuity-Rollout-Q4.md` (`git diff --check`, file scope, UTF-8/LF/no BOM, import). Hosted checks at the approved head: build success (run 38257893668); spdx success (run 38257893932). Dependency selection: dependency clones in the build log: SAM @ sow/2026-Q4.
- Cleanup: remote docs/agent-instructions-rollout-q4 deleted with an expected-SHA lease on 517282ba63afc50b002abcf17ae5f0f4fbaf49ef after confirming it is contained in sow/2026-Q4 and no open PR uses it as head or base; the local branch and its worktree are preserved (worktree in use). Other branches, worktrees and the frozen quarters were not touched.
- Remaining gaps: no agent-client behaviour or token benchmark has been run.
- Exact next step: Owner sets Q4 priorities for this repository and records them here; start each task from `AGENTS.md` and this file, with feature branches and owner-reviewed PRs.

## Branch

`sow/2026-Q4` - created 2026-10-11 directly from `master` (see `AGENTS.md` Branch context). Frozen Q3 record: `sow/2026-Q3` (not modified).
