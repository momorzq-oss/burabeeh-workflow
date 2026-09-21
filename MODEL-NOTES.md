# Models and reproducibility

Six model files are required; MODEL-MANIFEST.json records exact filenames, lengths and previously verified base/Turbo hashes. Other hashes are explicitly unmeasured. Place paths relative to your ComfyUI models directory or an extra-model-paths root. Do not rename unrelated weights to satisfy a dropdown.

## Sources

- Hybrid base: https://huggingface.co/smhfacct/Minimax-H3-fl2va-ref2va-hybrid-models/tree/a36feb17fbd1f20ff4bdd509ccd07e2b7b585a38
- Original Turbo adapter source: https://huggingface.co/TenStrip/MinimaxH3-Turbo_Shenanigans/tree/7b0cb70261a47dfb7b660999a0545163f20a8d14
- H3 latent upscaler: https://huggingface.co/LBH-123-AI/Minimax_h3_latent_Upscaler
- Upscaler custom node: https://github.com/LBH-123-AI/Comfyui_Minimax_h3_latent_Upscaler at `d7c01b9011f2e8439493f6c02c29995a27df276f`.

The encoder and both VAEs are available from [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3). MODEL-MANIFEST.json includes revision-pinned publisher links and publisher hashes. These are source metadata, not a fresh local hash verification. Preserve the MiniMax subfolders shown in the local paths. No weights are redistributed here.

## Critical Turbo compatibility caveat

The required `lightx2v_hybrid-4to8step-Turbo_r48_b25_curve_compatible.safetensors` is a LOCAL conversion, not the upstream download filename. The unadapted upstream adapter produced an AdaLN shape mismatch with this base. The conversion projects 51 AdaLN modules into the exact base curve coordinates, preserves the affine bias and drops no modules. Local sampled numerical checks passed; visual equivalence to the tutorial is not established.

`adapt_turbo.py` reproduces the conversion using the upstream helper implementation from https://github.com/Jalen-Brunson/ComfyUI-MiniMax-H3-PDD-Acc at `311a65dd53832d8a5f8177a9d5fb923c09e35a90`. This is an offline conversion dependency, NOT PDD acceleration in the running graph. Install that helper repository including its basis assets, then run the script with `--models` and `--helper`. You need the original source adapter to regenerate the converted weight. It was removed during local cleanup, but can be downloaded again from the pinned source above.

## Recorded local environment

- Windows; NVIDIA RTX 3090, 24 GB VRAM.
- ComfyUI commit `ace9172e95038ac25015c419713aa7755f739034`.
- Current graph requires ComfyUI H3 core nodes, comfy kitchen attention, and the H3 latent upscaler extension. Utilities with LTX in their names do not require an LTX diffusion model.
- Prior runtime repair recorded PyTorch 2.14.0+cu130 and Triton Windows 3.8.0.post28. See ENVIRONMENT.json for the currently measured package versions.
- The tested server uses 4 GB reserved VRAM and disables live latent previews. Run one GPU job at a time.

## Backup limits

This repository restores the workflow and its instructions. It is not a complete offline model backup. Keep a separate private copy of the six model files if offline disaster recovery is required. Model weights retain their original licenses. Public example screenshots contain the illustrated reference visible on the canvas, but the standalone personal reference source image is not distributed.

## Restore checklist

1. Restore the JSON into the ComfyUI user workflows folder or open it through the UI.
2. Restore or download the six model files using MODEL-MANIFEST.json. Rebuild the locally converted Turbo adapter if you did not retain it.
3. Install the pinned latent upscaler extension and compatible ComfyUI runtime; restart ComfyUI.
4. Upload a reference in node 100, replace the prompt, and check all required loaders.
5. Use the preview-only steps in the tutorial before trying the full output.

Example conversion command after cloning the helper repository and obtaining the upstream source adapter:

```powershell
python adapt_turbo.py --models "D:/ComfyUI/models" --helper "D:/ComfyUI/custom_nodes/ComfyUI-MiniMax-H3-PDD-Acc"
```

The converter requires torch and safetensors in that Python environment, plus the helper repository’s own requirements and matching basis files. It was adapted from the locally used converter; the parameterized distribution script is syntax-checked, not independently rerun after the source weight was deleted.
