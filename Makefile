setup-env:
	chmod +x ./tasks/install_dependencies.sh
	chmod +x ./tasks/install_dependencies_pdm.sh
	chmod +x ./tasks/install_dependencies_pip.sh
	./tasks/install_dependencies.sh $(method)

setup-folders:
	chmod +x ./tasks/setup_folders.sh
	./tasks/setup_folders.sh

setup:
	make setup-env method=$(method)
	make setup-folders