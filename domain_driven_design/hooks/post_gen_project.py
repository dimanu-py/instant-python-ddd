import subprocess

PDM = "pdm"
UV = "uv"
YES = ["yes", "y"]

dependency_manager = "{{cookiecutter.dependency_manager}}"
default_dependencies = "{{cookiecutter.install_default_dependencies}}"


def install_python() -> None:
	subprocess.run(["pyenv", "install", "{{cookiecutter.python_version}}"], check=True)
	subprocess.run(["pyenv", "local", "{{cookiecutter.python_version}}"], check=True)
	print("Python has been installed.")


def install_pdm() -> None:
	subprocess.run(["pip", "install", PDM], check=True)
	print(f"{PDM} has been installed.")


def install_uv() -> None:
	subprocess.run(["pip", "install", UV], check=True)
	print(f"{UV} has been installed.")


def install_default_dependencies() -> None:
	print("""Default dependencies to be installed:
	- coverage
	- doublex
	- doublex-expects
	- pytest
	- pytest-watch
	- pytest-xdist
	- ruff
	- mypy
	""")
	subprocess.run(["make", "install"], check=True)


def ask_for_additional_dependencies() -> None:
	while True:
		continue_asking = input("Do you want to install additional dependencies? [yes/no]")

		if continue_asking in YES:
			subprocess.run(["make", "add-dep"], check=True)
		else:
			break


def main() -> None:
	install_python()

	if dependency_manager == PDM:
		install_pdm()
	elif dependency_manager == UV:
		install_uv()

	if default_dependencies in YES:
		install_default_dependencies()
	ask_for_additional_dependencies()


if __name__ == "__main__":
	main()
