import pytest
from crimson.file_loader import collect_files, reconstruct_folder_structure, generate_file_contents


@pytest.fixture
def sample_directory(tmp_path):
    # 샘플 디렉토리 구조 생성
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir1" / "file1.txt").write_text("content1")
    (tmp_path / "dir2").mkdir()
    (tmp_path / "dir2" / "file2.py").write_text("content2")
    (tmp_path / "file3.jpg").write_text("content3")
    return tmp_path


@pytest.fixture
def sample_out_directory(tmp_path):
    # 샘플 디렉토리 구조 생성
    (tmp_path / "dir1%file1.txt").write_text("content1")
    (tmp_path / "dir2%file2.py").write_text("content2")
    (tmp_path / "file3.jpg").write_text("content3")
    return tmp_path


def get_new_path(tmp_path, relative_path="dir1/file1.txt"):
    new_path = str(tmp_path / relative_path).replace("/", "%")
    return new_path


def test_collect_files(sample_directory, tmp_path):
    out_dir = tmp_path / "output"
    collect_files(
        str(sample_directory),
        str(out_dir),
        includes=["\.txt$", "\.py$"],
        excludes=["dir2"],
    )

    assert (out_dir / get_new_path(tmp_path, "dir1/file1.txt")).exists()
    assert not (out_dir / get_new_path(tmp_path, "dir2%file2.py")).exists()
    assert not (out_dir / get_new_path(tmp_path, "file3.jpg")).exists()


def test_collect_files_with_path_editor(sample_directory, tmp_path):
    out_dir = tmp_path / "output"

    def path_editor(path):
        return path.replace("dir1", "new_dir1")

    collect_files(
        str(sample_directory),
        str(out_dir),
        post_path_editor=path_editor,
    )

    assert (out_dir / get_new_path(tmp_path, "new_dir1%file1.txt")).exists()


def test_collect_files_overwrite(sample_directory, tmp_path):
    out_dir = tmp_path / "output"
    out_dir.mkdir()
    (out_dir / "existing_file.txt").write_text("old content")

    assert (out_dir / "existing_file.txt").exists()

    collect_files(str(sample_directory), str(out_dir), overwrite=True)

    assert not (out_dir / "existing_file.txt").exists()


def test_reconstruct_folder_structure(sample_directory, tmp_path):
    intermediate_dir = tmp_path / "intermediate"
    collect_files(str(sample_directory), str(intermediate_dir))

    out_dir = tmp_path / "output"
    reconstruct_folder_structure(str(intermediate_dir), str(out_dir))

    assert (out_dir / tmp_path / "dir1" / "file1.txt").exists()
    assert (out_dir / tmp_path / "dir2" / "file2.py").exists()
    assert (out_dir / tmp_path / "file3.jpg").exists()


def test_reconstruct_folder_structure_with_path_editor(sample_directory, tmp_path):
    intermediate_dir = tmp_path / "intermediate"
    collect_files(str(sample_directory), str(intermediate_dir))

    out_dir = tmp_path / "output"

    def path_editor(path):
        return path.replace(str(tmp_path).replace("/", "%"), "")

    reconstruct_folder_structure(
        str(intermediate_dir), str(out_dir), path_editor=path_editor
    )

    assert (out_dir / "dir1" / "file1.txt").exists()


def test_reconstruct_folder_structure_overwrite(sample_directory, tmp_path):
    intermediate_dir = tmp_path / "intermediate"
    collect_files(str(sample_directory), str(intermediate_dir))

    out_dir = tmp_path / "output"
    out_dir.mkdir()
    (out_dir / "existing_file.txt").write_text("old content")

    assert (out_dir / "existing_file.txt").exists()

    reconstruct_folder_structure(str(intermediate_dir), str(out_dir), overwrite=True)

    assert not (out_dir / "existing_file.txt").exists()


def test_generate_file_contents(sample_directory):
    file_contents = generate_file_contents(
        str(sample_directory),
        includes=["\.txt$", "\.py$"],
        excludes=["dir2"],
    )

    assert len(file_contents) == 1
    assert file_contents[0][0].endswith("dir1%file1.txt")
    assert file_contents[0][1] == b"content1"


def test_generate_file_contents_with_path_editor(sample_directory):
    def path_editor(path):
        return path.replace("dir1", "new_dir1")

    file_contents = generate_file_contents(
        str(sample_directory),
        post_path_editor=path_editor,
    )

    assert any(content[0].endswith("new_dir1%file1.txt") for content in file_contents)


def test_generate_file_contents_all_files(sample_directory):
    file_contents = generate_file_contents(str(sample_directory))

    assert len(file_contents) == 3
    file_names = [content[0] for content in file_contents]
    assert any("dir1%file1.txt" in name for name in file_names)
    assert any("dir2%file2.py" in name for name in file_names)
    assert any("file3.jpg" in name for name in file_names)


def test_generate_file_contents_binary_content(sample_directory):
    # 바이너리 파일 생성
    binary_file = sample_directory / "binary_file.bin"
    binary_file.write_bytes(b'\x00\x01\x02\x03')

    file_contents = generate_file_contents(str(sample_directory), includes=[r"\.bin$"])

    assert len(file_contents) == 1
    assert file_contents[0][0].endswith("binary_file.bin")
    assert file_contents[0][1] == b'\x00\x01\x02\x03'
