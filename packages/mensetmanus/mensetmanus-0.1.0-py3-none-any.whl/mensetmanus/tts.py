import os
import sys
import typing
import pathlib
import tempfile

import torch

# Prevent triggering notice from https://github.com/DynamicTimeWarping/dtw-python/blob/51b2bb8e29d74cd5027d857bcb4ad6c7a2952d86/dtw/__init__.py#L32
if hasattr(sys, "ps1"):
    sys.ps1 = ""
else:
    sys.flags.interactive = False
from .thirdparty.OpenVoice.openvoice import api as ov_api
from .thirdparty.OpenVoice.openvoice import se_extractor as ov_se_extractor
from .thirdparty.MeloTTS.melo import api as melo_api


def download_unidic():
    """Download unidic data from S3."""
    os.system("python -m unidic download")


class VoiceCloner:
    """An object representing a Voice Cloning Pipeline."""

    def __init__(
        self,
        checkpoint_dir: pathlib.Path,
        device: str = "cuda:0" if torch.cuda.is_available() else "cpu",
        speaker: typing.Literal["EN-US"] = "EN-US",
    ):
        self.speaker_id = speaker
        self.speaker = melo_api.TTS(language=speaker.split("-")[0], device=device)
        self.converter = ov_api.ToneColorConverter(
            checkpoint_dir / "converter" / "config.json", device=device
        )
        self.converter.load_ckpt(checkpoint_dir / "converter" / "checkpoint.pth")
        self.embedding = torch.load(
            checkpoint_dir / "base_speakers" / "ses" / f"{speaker}.pth",
            map_location=device,
        )
        self.references = {}

    def add_reference_embedding(self, name: str, audio_path: pathlib.Path):
        """Add a reference voice to this voice cloner."""
        with tempfile.TemporaryDirectory() as tdir:
            embedding, _ = ov_se_extractor.get_se(
                audio_path=audio_path.as_posix(),
                target_dir=tdir,
                vc_model=self.converter,
                vad=False,
            )
        self.references[name] = embedding

    def speak(
        self,
        text: str,
        output: pathlib.Path,
        reference: str,
        base_audio: typing.Optional[pathlib.Path] = None,
        speed: int = 1,
    ):
        """Use this voice to speak."""
        with tempfile.NamedTemporaryFile(suffix=".wav") as base_temp:
            base_audio = (
                base_audio if base_audio is not None else pathlib.Path(base_temp.name)
            )
            self.speaker.tts_to_file(
                text,
                speaker_id=self.speaker.hps.data.spk2id[self.speaker_id],
                output_path=base_audio.as_posix(),
                speed=speed,
            )
            self.converter.convert(
                audio_src_path=base_audio,
                src_se=self.embedding,
                tgt_se=self.references[reference],
                output_path=output.as_posix(),
                message="@MyShell",
            )
