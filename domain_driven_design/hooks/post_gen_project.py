import subprocess

PDM = "pdm"
UV = "uv"
dependency_manager = "{{cookiecutter.dependency_manager}}"


def install_python() -> None:
	subprocess.run(["pyenv", "install", "{{cookiecutter.python_version}}"], check=True)
	subprocess.run(["cd", "{{cookiecutter.project_slug}}"], check=True)
	subprocess.run(["pyenv", "local", "{{cookiecutter.python_version}}"], check=True)
	print("Python has been installed.")


def install_pdm() -> None:
	subprocess.run(["pip", "install", PDM], check=True)
	print(f"{PDM} has been installed.")


def install_uv() -> None:
	subprocess.run(["pip", "install", UV], check=True)
	print(f"{UV} has been installed.")


def main() -> None:
	install_python()

	if dependency_manager == PDM:
		install_pdm()
	elif dependency_manager == UV:
		install_uv()


if __name__ == "__main__":
	main()
