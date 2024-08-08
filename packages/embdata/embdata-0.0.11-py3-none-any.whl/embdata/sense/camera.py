from pydantic import Field

from embdata.ndarray import NumpyArray
from embdata.sample import Sample


class Intrinsics(Sample):
    """Model for Camera Intrinsic Parameters."""

    focal_length_x: float = 0.0
    focal_length_y: float = 0.0
    optical_center_x: float = 0.0
    optical_center_y: float = 0.0


class Extrinsics(Sample):
    """Model for Camera Extrinsic Parameters."""

    rotation_matrix: NumpyArray[3, 3, float] = Field(
        default_factory=lambda: [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
        description="Rotation matrix from world to camera coordinate system",
    )
    translation_vector: NumpyArray[3, float] = Field(
        default_factory=lambda: [0.0, 0.0, 0.0],
        description="Translation vector from world to camera coordinate system",
    )


class Distortion(Sample):
    """Model for Camera Distortion Parameters."""

    k1: float = 0.0
    k2: float = 0.0
    p1: float = 0.0
    p2: float = 0.0
    k3: float = 0.0


class CameraParams(Sample):
    """Model for Camera Parameters."""

    intrinsic: Intrinsics = Field(default_factory=Intrinsics, description="Intrinsic parameters of the camera")
    distortion: Distortion = Field(default_factory=Distortion, description="Distortion parameters of the camera")
    extrinsic: Extrinsics = Field(default_factory=Extrinsics, description="Extrinsic parameters of the camera")
    depth_scale: float = 1.0
