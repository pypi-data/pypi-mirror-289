"""Read a QR code from an image file."""

import os
import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from qread import __copyright__, __name__, __version__

os.environ["OPENCV_LOG_LEVEL"] = "OFF"
from cv2 import QRCodeDetector, error, imread
from cv2.typing import MatLike


def err(msg: str, retval: int = 1) -> None:
    """Print an error message to stderr and exit with a non-zero return value."""
    sys.stderr.write(f"{__name__}: error: {msg}\n")
    sys.exit(retval)


# Build CLI
parser: ArgumentParser = ArgumentParser(
    prog=__name__,
    description="Read a QR code from an image file.",
    add_help=False,
)
parser.add_argument(
    "-h",
    "--help",
    action="help",
    help="Show this help message and exit.",
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    help="Show version and exit.",
    version=f"{__name__} v{__version__} -- {__copyright__}",
)
parser.add_argument("filename", type=Path, help="Image file containing a QR code.")
args: Namespace = parser.parse_args()

# Try to read in the image file
image: MatLike = imread(args.filename)
if image is None:
    err(f"unable to read image file {args.filename}")

# Try to detect the QR code
data: str
points: MatLike
detector: QRCodeDetector = QRCodeDetector()
try:
    data, points, _ = detector.detectAndDecode(image)
except error as e:
    err(f"opencv error {e.err}")
if points is None:
    err("no qr codes detected")

# Finish
sys.stdout.write(f"{data}\n")
sys.exit()
