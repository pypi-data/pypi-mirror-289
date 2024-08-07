import gzip
import hashlib
import shutil
import sys
import tarfile
import time
import zipfile
from pathlib import Path

import build.util
import pytest

from scikit_build_core._compat.importlib.metadata import PathDistribution
from scikit_build_core.build import (
    _file_processor,
    build_sdist,
    build_wheel,
    prepare_metadata_for_build_wheel,
)

ENTRYPOINTS = """\
[one.two]
three = four

[console_scripts]
something = other

[gui_scripts]
guithing = a.b:c
"""
METADATA = """\
Metadata-Version: 2.1
Name: CMake.Example
Version: 0.0.1
Requires-Python: >=3.7
Provides-Extra: test
Requires-Dist: pytest>=6.0; extra == "test"
"""

mark_hashes_different = pytest.mark.xfail(
    sys.platform.startswith(("win", "cygwin")),
    reason="hashes differ on Windows",
    strict=False,
)


def compute_uncompressed_hash(inp: Path) -> str:
    with gzip.open(inp, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


@pytest.mark.usefixtures("package_simple_pyproject_ext")
def test_pep517_sdist():
    dist = Path("dist")
    out = build_sdist("dist")

    (sdist,) = dist.iterdir()
    assert sdist.name == "cmake_example-0.0.1.tar.gz"
    assert sdist == dist / out

    with tarfile.open(sdist) as f:
        file_names = set(f.getnames())
        assert file_names == {
            f"cmake_example-0.0.1/{x}"
            for x in (
                "CMakeLists.txt",
                "pyproject.toml",
                "src/main.cpp",
                "PKG-INFO",
                "LICENSE",
            )
        }
        pkg_info = f.extractfile("cmake_example-0.0.1/PKG-INFO")
        assert pkg_info
        pkg_info_contents = pkg_info.read().decode()
        assert pkg_info_contents == METADATA


@mark_hashes_different
def test_pep517_sdist_hash(monkeypatch, package_simple_pyproject_ext):
    # Unset SOURCE_DATE_EPOCH in order to guarantee the hash match
    monkeypatch.delenv("SOURCE_DATE_EPOCH", raising=False)
    dist = Path("dist")
    out = build_sdist("dist")
    sdist = dist / out
    hash = compute_uncompressed_hash(sdist)
    assert hash == package_simple_pyproject_ext.sdist_hash
    mode = sdist.stat().st_mode
    assert mode == 33188
    with gzip.open(sdist, "rb") as f:
        f.read()
        assert f.mtime == 1667997441


@pytest.mark.usefixtures("package_simple_pyproject_ext")
def test_pep517_sdist_time_hash():
    dist = Path("dist")

    out = build_sdist("dist")
    sdist = dist / out
    hash1 = hashlib.sha256(sdist.read_bytes()).hexdigest()

    time.sleep(2)
    Path("src/main.cpp").touch()

    if Path("dist").is_dir():
        shutil.rmtree("dist")

    out = build_sdist(str(dist))
    sdist = dist / out

    hash2 = hashlib.sha256(sdist.read_bytes()).hexdigest()

    assert hash1 == hash2


@pytest.mark.usefixtures("package_simple_pyproject_ext")
def test_pep517_sdist_time_hash_nonreproducable():
    dist = Path("dist")

    out = build_sdist("dist", {"sdist.reproducible": "false"})
    sdist = dist / out
    hash1 = hashlib.sha256(sdist.read_bytes()).hexdigest()

    time.sleep(2)

    if Path("dist").is_dir():
        shutil.rmtree("dist")

    out = build_sdist(str(dist))
    sdist = dist / out

    hash2 = hashlib.sha256(sdist.read_bytes()).hexdigest()

    assert hash1 != hash2


@mark_hashes_different
@pytest.mark.parametrize("reverse_order", [False, True])
def test_pep517_sdist_time_hash_set_epoch(
    monkeypatch, reverse_order, package_simple_pyproject_ext
):
    dist = Path("dist")
    monkeypatch.setenv(
        "SOURCE_DATE_EPOCH", package_simple_pyproject_ext.source_date_epoch
    )

    _each_unignored_file = _file_processor.each_unignored_file

    def each_unignored_file_ordered(*args, **kwargs):
        return sorted(_each_unignored_file(*args, **kwargs), reverse=reverse_order)

    monkeypatch.setattr(
        _file_processor, "each_unignored_file", each_unignored_file_ordered
    )

    out = build_sdist(str(dist), {"sdist.reproducible": "true"})
    sdist = dist / out
    hash = compute_uncompressed_hash(sdist)
    assert hash == package_simple_pyproject_ext.sdist_dated_hash


@pytest.mark.compile()
@pytest.mark.configure()
@pytest.mark.usefixtures("package_simple_pyproject_script_with_flags")
@pytest.mark.parametrize(
    ("env_var", "setting"),
    [
        ("CMAKE_ARGS", '-DCMAKE_C_FLAGS="-DFOO=1 -DBAR="'),
        ("SKBUILD_CMAKE_ARGS", "-DCMAKE_C_FLAGS=-DFOO=1 -DBAR="),
    ],
)
def test_passing_cxx_flags(monkeypatch, env_var, setting):
    # Note: This is sensitive to the types of quotes for SKBUILD_CMAKE_ARGS
    monkeypatch.setenv(env_var, setting)
    build_wheel("dist", {"cmake.targets": ["cmake_example"]})  # Could leave empty
    (wheel,) = Path("dist").glob("cmake_example-0.0.1-py3-none-*.whl")
    with zipfile.ZipFile(wheel) as f:
        file_names = set(f.namelist())

    ext = ".exe" if sys.platform.startswith(("win", "cygwin")) else ""

    assert file_names == {
        "cmake_example-0.0.1.dist-info/RECORD",
        "cmake_example-0.0.1.dist-info/WHEEL",
        f"cmake_example-0.0.1.data/scripts/cmake_example{ext}",
        "cmake_example-0.0.1.dist-info/METADATA",
        "cmake_example-0.0.1.dist-info/licenses/LICENSE",
    }


@pytest.mark.compile()
@pytest.mark.configure()
@pytest.mark.usefixtures("package_simple_pyproject_ext")
def test_pep517_wheel(virtualenv):
    dist = Path("dist")
    out = build_wheel("dist", {"cmake.targets": ["cmake_example"]})  # Could leave empty
    (wheel,) = dist.glob("cmake_example-0.0.1-*.whl")
    assert wheel == dist / out

    with zipfile.ZipFile(wheel) as zf:
        file_paths = {Path(p) for p in zf.namelist()}
        file_names = {p.parts[0] for p in file_paths}

        with zf.open("cmake_example-0.0.1.dist-info/METADATA") as f:
            metadata = f.read().decode("utf-8")

        with zf.open("cmake_example-0.0.1.dist-info/entry_points.txt") as f:
            entry_points = f.read().decode("utf-8")

    assert Path("cmake_example-0.0.1.dist-info/licenses/LICENSE") in file_paths

    assert len(file_names) == 2
    assert "cmake_example-0.0.1.dist-info" in file_names
    file_names.remove("cmake_example-0.0.1.dist-info")
    (so_file,) = file_names

    assert so_file.startswith("cmake_example")
    print("SOFILE:", so_file)

    print(entry_points == ENTRYPOINTS)
    assert 'Requires-Dist: pytest>=6.0; extra == "test"' in metadata
    assert "Metadata-Version: 2.1" in metadata
    assert "Name: CMake.Example" in metadata
    assert "Version: 0.0.1" in metadata
    assert "Requires-Python: >=3.7" in metadata
    assert "Provides-Extra: test" in metadata

    virtualenv.install(wheel)

    version = virtualenv.execute(
        "import cmake_example; print(cmake_example.__version__)",
    )
    assert version.strip() == "0.0.1"

    add = virtualenv.execute(
        "import cmake_example; print(cmake_example.add(1, 2))",
    )
    assert add.strip() == "3"


@pytest.mark.compile()
@pytest.mark.configure()
@pytest.mark.usefixtures("package_simple_pyproject_source_dir")
def test_pep517_wheel_source_dir(virtualenv):
    dist = Path("dist")
    out = build_wheel("dist", config_settings={"skbuild.wheel.build-tag": "1foo"})
    (wheel,) = dist.glob("cmake_example-0.0.1-*.whl")
    assert wheel == dist / out

    with zipfile.ZipFile(wheel) as zf:
        file_paths = {Path(p) for p in zf.namelist()}
        file_names = {p.parts[0] for p in file_paths}

        with zf.open("cmake_example-0.0.1.dist-info/METADATA") as f:
            metadata = f.read().decode("utf-8")

        with zf.open("cmake_example-0.0.1.dist-info/WHEEL") as f:
            wheel_metadata = f.read().decode("utf-8")

        with zf.open("cmake_example-0.0.1.dist-info/entry_points.txt") as f:
            entry_points = f.read().decode("utf-8")

    assert Path("cmake_example-0.0.1.dist-info/licenses/LICENSE") in file_paths

    assert len(file_names) == 2
    assert "cmake_example-0.0.1.dist-info" in file_names
    file_names.remove("cmake_example-0.0.1.dist-info")
    (so_file,) = file_names

    assert so_file.startswith("cmake_example")
    print("SOFILE:", so_file)

    print(entry_points == ENTRYPOINTS)
    assert 'Requires-Dist: pytest>=6.0; extra == "test"' in metadata
    assert "Metadata-Version: 2.1" in metadata
    assert "Name: CMake.Example" in metadata
    assert "Version: 0.0.1" in metadata
    assert "Requires-Python: >=3.7" in metadata
    assert "Provides-Extra: test" in metadata

    assert "Build: 1foo" in wheel_metadata
    assert "Wheel-Version: 1.0" in wheel_metadata
    assert "Generator: scikit-build" in wheel_metadata
    assert "Root-Is-Purelib: false" in wheel_metadata

    virtualenv.install(wheel)

    version = virtualenv.execute(
        "import cmake_example; print(cmake_example.__version__)",
    )
    assert version.strip() == "0.0.1"

    add = virtualenv.execute(
        "import cmake_example; print(cmake_example.add(1, 2))",
    )
    assert add.strip() == "3"


@pytest.mark.skip(reason="Doesn't work yet")
@pytest.mark.compile()
@pytest.mark.configure()
def test_pep517_wheel_time_hash(monkeypatch):
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "12345")
    dist = Path("dist")
    out = build_wheel("dist")
    wheel = dist / out
    hash1 = hashlib.sha256(wheel.read_bytes()).hexdigest()

    time.sleep(2)
    Path("src/main.cpp").touch()

    if Path("dist").is_dir():
        shutil.rmtree("dist")

    out = build_wheel(str(dist))
    wheel = dist / out

    hash2 = hashlib.sha256(wheel.read_bytes()).hexdigest()

    assert hash1 == hash2


@pytest.mark.usefixtures("package_simple_pyproject_ext")
def test_prepare_metdata_for_build_wheel():
    metadata = build.util.project_wheel_metadata(str(Path.cwd()), isolated=False)
    answer = {
        "Metadata-Version": "2.1",
        "Name": "CMake.Example",
        "Version": "0.0.1",
        "Requires-Python": ">=3.7",
        "Provides-Extra": "test",
        "Requires-Dist": 'pytest>=6.0; extra == "test"',
    }

    for k, b in answer.items():
        assert metadata.get(k, None) == b

    assert len(metadata) == len(answer)


@pytest.mark.usefixtures("package_simple_pyproject_ext")
def test_prepare_metdata_for_build_wheel_by_hand(tmp_path):
    mddir = tmp_path / "dist"
    mddir.mkdir()
    out = prepare_metadata_for_build_wheel(str(mddir), {})
    print("Metadata dir:", (mddir / out).resolve())
    metadata = PathDistribution(mddir / out).metadata
    answer = {
        "Metadata-Version": "2.1",
        "Name": "CMake.Example",
        "Version": "0.0.1",
        "Requires-Python": ">=3.7",
        "Provides-Extra": "test",
        "Requires-Dist": 'pytest>=6.0; extra == "test"',
    }

    for k, b in answer.items():
        assert metadata.get(k, None) == b

    assert len(metadata) == len(answer)
