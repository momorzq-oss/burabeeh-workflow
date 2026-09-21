# Connection map

Each row names the upstream node feeding a connected input. This is extracted from the saved UI workflow.

| Node | Input | Source node / output slot |
|---|---|---|
| 2 | `model` | 1 / 0 |
| 3 | `model` | 2 / 0 |
| 4 | `model` | 3 / 0 |
| 5 | `model` | 4 / 0 |
| 6 | `model` | 5 / 0 |
| 20 | `clip` | 7 / 0 |
| 20 | `vae` | 8 / 0 |
| 20 | `audio_vae` | 9 / 0 |
| 20 | `ref_images.ref_image_0` | 100 / 0 |
| 20 | `prompt` | 10 / 0 |
| 20 | `width` | 11 / 0 |
| 20 | `height` | 12 / 0 |
| 20 | `length` | 13 / 0 |
| 22 | `model` | 6 / 0 |
| 22 | `conditioning` | 20 / 0 |
| 24 | `model` | 6 / 0 |
| 25 | `noise` | 21 / 0 |
| 25 | `guider` | 22 / 0 |
| 25 | `sampler` | 23 / 0 |
| 25 | `sigmas` | 24 / 0 |
| 25 | `latent_image` | 20 / 1 |
| 26 | `av_latent` | 25 / 0 |
| 27 | `samples` | 26 / 0 |
| 27 | `vae` | 8 / 0 |
| 28 | `samples` | 26 / 1 |
| 28 | `vae` | 9 / 0 |
| 29 | `images` | 27 / 0 |
| 29 | `audio` | 28 / 0 |
| 30 | `video` | 29 / 0 |
| 40 | `latent` | 26 / 0 |
| 40 | `mode.width` | 14 / 0 |
| 40 | `mode.height` | 15 / 0 |
| 41 | `video_latent` | 40 / 0 |
| 41 | `audio_latent` | 26 / 1 |
| 42 | `model` | 6 / 0 |
| 42 | `conditioning` | 20 / 0 |
| 43 | `model` | 6 / 0 |
| 44 | `noise` | 21 / 0 |
| 44 | `guider` | 42 / 0 |
| 44 | `sampler` | 23 / 0 |
| 44 | `sigmas` | 43 / 0 |
| 44 | `latent_image` | 41 / 0 |
| 45 | `av_latent` | 44 / 0 |
| 46 | `samples` | 45 / 0 |
| 46 | `vae` | 8 / 0 |
| 47 | `images` | 46 / 0 |
| 47 | `audio` | 28 / 0 |
| 48 | `video` | 47 / 0 |