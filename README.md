# Burabeeh workflow

The owner’s selected working MiniMax H3 preview-and-refine workflow for local ComfyUI.

- [Full illustrated tutorial](TUTORIAL.md) — all 36 nodes and run instructions.
- [Workflow](Burabeeh%20workflow.json)
- [Model and environment notes](MODEL-NOTES.md)
- [Narrated screen walkthrough](Burabeeh-workflow-tutorial.mp4)

Defaults: 864×480 preview, 158 frames at 24 fps, 8-step compatible Turbo sampling; 1376×768 refinement, 4 steps at denoise 0.25; original preview audio retained. Both outputs are enabled by default.

Tested locally on RTX 3090 24 GB. “Working” describes execution evidence, not flawless motion, identity or speech. Model weights and personal reference images are not included.

## Credits

Built on ComfyUI, MiniMax H3, the LBH H3 latent upscaler, the TenStrip Turbo adapter and the compatibility helper documented in MODEL-NOTES.md. Workflow direction was based on [the supplied tutorial](https://youtu.be/tmw2QOFaaPI). Burabeeh is the name of this configured workflow and tutorial package; upstream projects and weights retain their own ownership and licenses.

## Download the complete backup

- [Workflow + illustrated documentation ZIP](Burabeeh-workflow-backup.zip)
- [Illustrated offline tutorial — download and open in your browser](Burabeeh-workflow-tutorial.html)
- [Video chapter timings](VIDEO-CHAPTERS.md)
- [Exact connection map](CONNECTIONS.md)

The video is stored separately from the ZIP to stay within upload limits. The local full archive includes everything.

The approximately 14-minute tutorial uses real ComfyUI screen captures with zoom transitions, held readable node close-ups and synthesized narration. It includes all 36 nodes and a fresh preview/refinement run. Rendering waits are edited out.

Fresh run checks: preview 864×480, final 1376×768, both 158 frames at 24 fps, decoded audio identical. See VALIDATION.json for scope and hashes. Model weights are not included.
