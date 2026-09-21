# Burabeeh workflow

A locally tested MiniMax H3 workflow for a fast preview followed by latent refinement, with the original preview audio reused in the final video. This is the owner’s selected working configuration, not a benchmark proving it is the best workflow for every machine or subject.

## Quick start

1. Install a compatible ComfyUI build and the H3 latent upscaler custom node. See the model and environment notes.
2. Put the six required model files in their documented folders. The exact locally adapted Turbo weight is required.
3. Open `workflows/Burabeeh workflow.json` in ComfyUI.
4. At node 100, upload your own reference. The saved example filename is `ep01_end_frame.png`; this personal project image is not bundled in the public backup.
5. Replace node 10’s example prompt for your own scene. Match identity, costume AND location to the reference.
6. Select node 48 and press **Ctrl+M** to mute final saving for a preview-only run. Check that its mode visibly changes. Do not bypass Save Video.
7. Click **Run** once. Wait for completion, then play the preview with sound.
8. Keep seed, models, prompt and reference unchanged. Select node 48 and press **Ctrl+M** again to enable it, then Run for refinement. Cache reuse is conditional; restarting or changing upstream inputs may regenerate the preview.
9. Find videos under `output/Burabeeh-workflow/`. Review the refined result with sound before using it.

**Default behavior:** both Save Video nodes are enabled, so a normal Run computes preview AND refinement. The graph itself has no automatic human-review pause.

## Tested settings

| Setting | Value |
|---|---|
| Preview | 864 × 480 |
| Length / playback | 158 frames / 24 fps, approximately 6.58 s |
| Preview sampling | res_multistep / simple / 8 steps / denoise 1.0 |
| Compatible Turbo strength | 0.70 |
| Final | 1376 × 768 |
| Refinement | 4 steps / simple / denoise 0.25 |
| Video tiled decode | 512 / 64 overlap / temporal 32 / temporal overlap 8 |
| Optional adapter nodes 3–5 | Bypassed; no optional weights required |

## Every node

### 1. Hybrid b25-49 — tutorial base

**Type:** `UNETLoader`. **Mode:** active.

Loads the MiniMax H3 hybrid b25 to 49 INT8 diffusion model. Keep weight dtype on default. This is the tested base; similarly named pruned reference or first-last-frame models are not interchangeable with this setup.


### 2. Attention backend

**Type:** `ModelAttentionBackend`. **Mode:** active.

Selects comfy kitchen attention for the loaded model. Keep this tested attention backend when reproducing the local setup. This node changes attention computation, not the story, reference image or video length.


### 3. Optional correction — BYPASSED

**Type:** `LoraLoaderModelOnly`. **Mode:** bypassed.

This optional correction adapter is bypassed. It passes the model through without loading the named weight. The file is not required. Leave it bypassed; enabling an unavailable adapter causes a missing-model error.


### 4. Optional Cinema / close shots — BYPASSED

**Type:** `LoraLoaderModelOnly`. **Mode:** bypassed.

This optional cinema adapter is also bypassed. Its strength value has no effect while bypassed. It is not part of the tested six-model configuration and is not needed to generate a preview or refined output.


### 5. Optional Film / wide shots — BYPASSED

**Type:** `LoraLoaderModelOnly`. **Mode:** bypassed.

The optional film adapter is bypassed too. Do not mistake the placeholder filename for a required download. Nodes three, four and five are reserved optional slots, not evidence that these adapters have been tested.


### 6. Hybrid Turbo — locally curve-adapted — 0.70

**Type:** `LoraLoaderModelOnly`. **Mode:** active.

Loads the locally curve-adapted Hybrid Turbo adapter at strength zero point seven. Use the exact compatible filename. The original unadapted adapter caused a shape mismatch. This conversion is specific to the hybrid base and is documented in the model notes.


### 7. H3 text encoder

**Type:** `CLIPLoader`. **Mode:** active.

Loads the MiniMax Qwen three vision-language text encoder, with type minimax and device default. It interprets the prompt and reference inputs. Keep it in the text encoders MiniMax folder and retain its exact filename.


### 8. Video VAE — installed FP16

**Type:** `VAELoader`. **Mode:** active.

Loads the H3 video VAE in FP16. The VAE converts between image pixels and the compressed visual representation used by the model. Both preview and final video decoding use this video VAE.


### 9. Audio VAE

**Type:** `VAELoader`. **Mode:** active.

Loads the H3 audio VAE in FP32. This handles the sound representation. It is separate from the video VAE and is required for native speech and ambience. Do not substitute an LTX audio VAE.


### 10. 1. EDIT YOUR PROMPT

**Type:** `PrimitiveStringMultiline`. **Mode:** active.

Write the shot here. Describe the person, correct location, one bounded action, camera, light and style under integrated multimodal description. Under overall soundscape specify exact short dialogue and ambience. A connected prompt overrides the duplicate text shown inside the conditioning node.


### 11. Preview width

**Type:** `PrimitiveInt`. **Mode:** active.

Preview width is 864 pixels. Width and height control the first sampling stage. Start at this tested size on the 24 gigabyte GPU; raising resolution increases memory and runtime. Change width and height together to maintain the intended composition.


### 12. Preview height

**Type:** `PrimitiveInt`. **Mode:** active.

Preview height is 480 pixels. The preview is a slightly wider than sixteen by nine working frame. The final dimensions differ slightly in aspect ratio, so inspect framing after refinement rather than assuming an identical crop.


### 13. 158 frames — 6.58 seconds at 24 fps

**Type:** `PrimitiveInt`. **Mode:** active.

The clip contains 158 frames. At 24 frames per second this is about 6.58 seconds. Keep this tested length for your first run. Generated duration does not guarantee that a long spoken line will fit.


### 14. Final width — change with final height

**Type:** `PrimitiveInt`. **Mode:** active.

Final width is 1376 pixels. This value feeds the latent upscaler. It does not change preview resolution. Refinement increases detail after the first generation; it cannot reliably repair a wrong face, location or action.


### 15. Final height

**Type:** `PrimitiveInt`. **Mode:** active.

Final height is 768 pixels. Use it with final width 1376 for the tested refinement. Larger output dimensions can exceed available memory. Keep the initial settings until a complete preview and refinement have succeeded.


### 20. Reference-guided H3 — Episode 1 image CONNECTED

**Type:** `MiniMaxH3ReferenceToVideo`. **Mode:** active.

Reference-to-video conditioning combines the prompt, image reference, both VAEs, dimensions and frame count. Reference image zero is connected. The output provides positive conditioning and the starting audio-video latent. A reference can influence the entire background, not just a face.


### 21. KEEP FIXED after choosing a preview

**Type:** `RandomNoise`. **Mode:** active.

The random seed is fixed. Keeping the seed, prompt, references and model settings unchanged makes comparisons more controlled. Changing the seed selects a different starting noise pattern. Lock it after selecting a useful preview.


### 22. Preview guidance

**Type:** `BasicGuider`. **Mode:** active.

Basic guidance combines the model and positive conditioning for preview sampling. It has no editable guidance slider in this graph. A disabled-looking properties row can simply mean there are no editable widgets; it does not mean the graph node is muted.


### 23. Sampler — tutorial res_multistep

**Type:** `KSamplerSelect`. **Mode:** active.

Selects the res multistep sampler. The preview and refinement share this sampler. Keep the tested sampler when checking reproducibility. Changing it changes the sampling process and requires a fresh quality check.


### 24. 8-step preview / full denoise

**Type:** `BasicScheduler`. **Mode:** active.

The preview scheduler uses simple scheduling, eight steps and full denoise of one. It builds the noise schedule for the first generation. The compatible Turbo adapter makes this short schedule practical in the tested configuration.


### 25. 3. GENERATE PREVIEW

**Type:** `SamplerCustomAdvanced`. **Mode:** active.

The advanced sampler creates the preview audio-video latent from noise, guidance, sampler, schedule and initial latent. This is the expensive first sampling stage. Watch progress and errors in the job queue; do not submit duplicate jobs while one is running.


### 26. Separate picture and sound

**Type:** `LTXVSeparateAVLatent`. **Mode:** active.

Separates the generated audio-video latent into picture and sound branches. Despite the LTX name, this utility is used here for the compatible combined latent structure. It does not load an LTX diffusion model.


### 27. Preview picture — tiled decode

**Type:** `VAEDecodeTiled`. **Mode:** active.

Tiled video decoding turns the preview visual latent into frames while limiting decoding memory. The tested settings are tile size 512, overlap 64, temporal size 32 and temporal overlap eight. Keep them for the first test.


### 28. Preview sound — reused for final output

**Type:** `VAEDecodeAudio`. **Mode:** active.

Decodes the preview audio latent into a waveform with the H3 audio VAE. The final output deliberately reuses this stage-one audio. Listen for missing words, repeated dialogue, cut-off endings and unwanted extra voices.


### 29. Preview with original audio

**Type:** `CreateVideo`. **Mode:** active.

Combines the decoded preview frames and sound at 24 frames per second. Keep the frame rate consistent with the intended duration. This creates a video object; the following Save Video node writes the actual file.


### 30. PREVIEW — review motion + sound first

**Type:** `SaveVideo`. **Mode:** active.

Saves the preview with the Burabeeh workflow preview prefix. Review the entire clip with sound before accepting it. Check character identity, room, hands, props and motion. A playable file or matching transcription alone is not full quality approval.


### 40. 4. Upscale VIDEO latent only

**Type:** `MinimaxH3LatentUpscaler3D`. **Mode:** active.

Upscales only the visual latent using the dedicated H3 three-dimensional latent upscaler. The target is 1376 by 768, with temporal chunk 32, CUDA and BF16. The audio branch is kept separate so picture enhancement does not replace the preview dialogue.


### 41. Rejoin untouched audio latent

**Type:** `LTXVConcatAVLatent`. **Mode:** active.

Recombines the enlarged visual latent and original audio latent before refinement. The name is another audio-video utility, not an LTX model dependency. Keep the two branches connected in the supplied order.


### 42. Refinement guidance — same prompt/references

**Type:** `BasicGuider`. **Mode:** active.

Creates refinement guidance from the same model and positive conditioning. The prompt and references must stay consistent with the selected preview. Changing the story between stages defeats the purpose of refining a selected take.


### 43. 4-step refinement / denoise 0.25

**Type:** `BasicScheduler`. **Mode:** active.

The refinement schedule uses simple scheduling, four steps and denoise zero point two five. It makes a smaller change than full-denoise generation. Raising denoise can change identity, composition and action, so treat changes as new experiments.


### 44. 5. REFINE THE SELECTED PREVIEW

**Type:** `SamplerCustomAdvanced`. **Mode:** active.

Runs the second advanced sampler on the enlarged combined latent. It uses the fixed noise source, refinement guidance, shared sampler and four-step schedule. This stage is a real generation pass, not ordinary image resizing.


### 45. Refined video latent

**Type:** `LTXVSeparateAVLatent`. **Mode:** active.

Separates the refined combined latent again. Only its visual result is used for final picture decoding. The final video uses audio decoded from the first stage, which is why the connection from node 28 must remain intact.


### 46. Final picture — tiled decode

**Type:** `VAEDecodeTiled`. **Mode:** active.

Decodes the refined visual latent into the final frames with the video VAE. It uses the same tested tiled decoding settings. If decoding runs out of memory, first return to the tested resolution and close competing GPU jobs.


### 47. Final picture + stage-one audio

**Type:** `CreateVideo`. **Mode:** active.

Combines final frames with the original stage-one audio at 24 frames per second. This is the important sound-preservation connection: enhanced picture from node 46, original decoded sound from node 28.


### 48. FINAL — refinement output (enabled)

**Type:** `SaveVideo`. **Mode:** active.

Saves the refined video with the Burabeeh workflow refined prefix. This output is enabled in the supplied workflow. Run therefore generates both stages unless you mute this output first. The old disabled label was misleading and has been corrected.


### 100. ENABLED — Sherlock identity + Episode 1 end frame

**Type:** `LoadImage`. **Mode:** active.

Load the reference image here and keep its image output connected to reference image zero. Use a reference that already matches the intended location. A portrait taken in another room can pull that room into the result. For a new scene, use a coherent character-and-location reference.



## Troubleshooting and review

- **Missing model:** compare the exact folder and filename to the model manifest. The three bypassed adapter placeholders do not need files.
- **Turbo shape mismatch:** the unadapted source adapter is not a replacement for the curve-compatible file. See the reproduction caveat in MODEL-NOTES.md.
- **Missing image:** upload a reference through node 100 and choose it in the node. Merely copying a file while the browser is open may leave its dropdown stale.
- **Wrong room or face:** repair the reference before spending another refinement pass. Separate unrelated location cues; one coherent character-in-location still worked better for the corrected crime-scene takes.
- **Repeated or missing dialogue:** shorten the line, render a new take, and listen. Automatic transcription can help but cannot verify voice quality.
- **Out of memory:** use the tested dimensions, one GPU job at a time, and tiled decode. Avoid simultaneous workloads on another ComfyUI server.
- **No speedup on refinement:** input changes or restarting the server can invalidate upstream cache. There is no permanent saved-latent loader in this graph.
- **Muted versus no widgets:** a grey properties row with no editable parameters does not prove the underlying graph node is muted. Inspect node mode.

## What was actually verified

This workflow family previously completed local preview and refinement jobs on an RTX 3090 24 GB. The user accepted the opening preview. Later episode takes exposed location and dialogue problems; successful execution is not artistic approval. The tutorial captures actual node screens. It does not present bypassed adapters as executed or claim every generated take is usable. The original episode videos were subsequently selected for deletion.

## Backup scope

The backup contains the graph, reference/API instructions, complete node documentation, captured node screens and the narrated tutorial. It excludes model weights, credentials, personal reference image files and historical episode footage. Downloaded model licenses continue to apply.

See [the exact connection map](CONNECTIONS.md) for every linked input.

## Recorded run demonstration

The accompanying screen walkthrough shows node 48 being muted, the preview being queued, the active sampler, preview completion, node 48 being re-enabled, and refinement using the cached preview. The first fresh preview took 404.72 seconds after memory cleanup. This is one measured run, not a general speed promise.

## Screen-by-screen run demonstration

### Run step 1 — mute the final output

Here is the real preview-only switch. Click the title of node 48 to select it, then press Control M. The node becomes translucent. Its title is just a label, so the word enabled does not update automatically. The actual mute state determines whether final saving runs.



### Run step 2 — submit one preview

Click the blue Run button once. ComfyUI queues the preview and loads the required models. The final output was muted for this run. After clearing the memory cache, model initialization can take substantially longer than a warm run. Do not click Run repeatedly.



### Run step 3 — watch the job queue

Open the active job counter to watch progress. The current node and progress percentage appear at the top. Older entries may refer to deleted files and show unavailable media. That does not mean the current job failed. Wait for the current job to complete before deciding what to do next.



### Run step 4 — preview complete

The preview has now finished successfully. This cold-cache demonstration took about 405 seconds on the local RTX 3090. The output contains 158 frames at 864 by 480 with audio. Completion verifies execution; you still need to play and review the scene before accepting it for a film.



### Run step 5 — enable refinement

Select node 48 again and press Control M to unmute it. Keep the seed, prompt, reference, dimensions and model settings unchanged. The supplied workflow has both outputs enabled by default. This manual mute and unmute sequence creates a deliberate review step.



### Run step 6 — reuse the preview

Click Run again. In this demonstration, the job jumps directly to the latent upscaler because the preview is still cached. It then runs the four-step refinement and final decoding. This is conditional caching, not a saved preview file being loaded back into the model.



### Run step 7 — final output verified

Refinement has completed successfully. The final file has 158 frames at 1376 by 768. This pass took about 271 seconds. Both files decoded correctly, and their decoded audio samples were identical. These checks prove execution and sound preservation, while identity, motion and delivery still require a viewing and listening review.



