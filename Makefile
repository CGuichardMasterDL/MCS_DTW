init: cleanvenv
	@bash scripts/venv.sh
	@bash scripts/update.sh

update:
	@bash scripts/update.sh

test:
	@bash scripts/test.sh

evaluate:
	-@bash scripts/evaluate.sh

build:
	@bash scripts/build.sh

package:
	@bash scripts/package.sh

install:
	@bash scripts/install.sh

uninstall:
	@bash scripts/uninstall.sh

cleanall: cleanout cleanvenv cleanpackage

cleanout:
	@rm -rf out/

cleanvenv:
	@rm -rf venv/

cleanpackage:
	@rm -rf build/ dist/ mcs_dtw.egg-info/

.PHONY: init update test evaluate build package install uninstall cleanall cleanout cleanvenv cleanpackage
