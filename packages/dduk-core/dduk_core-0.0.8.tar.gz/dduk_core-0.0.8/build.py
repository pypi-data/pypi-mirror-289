#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
import builtins
import os
import setuptools
import dotenv


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
UTF8 : str = "utf-8"
READ : str = "r"
SRC : str = "src"
READMEMD : str = "README.md"
CONSOLESCRIPTS : str = "console_scripts"
CLASSIFIER_1 : str = "Programming Language :: Python :: 3"
CLASSIFIER_2 : str = "License :: OSI Approved :: MIT License"
CLASSIFIER_3 : str = "Operating System :: OS Independent"


#--------------------------------------------------------------------------------
# 환경 변수 파일 기반 변수 목록. (.ENV)
#--------------------------------------------------------------------------------
dotenv.load_dotenv(override = True)
NAME = os.getenv("NAME")
VERSION = os.getenv("VERSION")
AUTHOR = os.getenv("AUTHOR")
AUTHOR_EMAIL = os.getenv("AUTHOR_EMAIL")
DESCRIPTION = os.getenv("DESCRIPTION")
LONG_DESCRIPTION_CONTENT_TYPE = os.getenv("LONG_DESCRIPTION_CONTENT_TYPE")
URL = os.getenv("URL")
PYTHON_REQUIRES = os.getenv("PYTHON_REQUIRES")
builtins.print(f"NAME: {NAME}")
builtins.print(f"VERSION: {VERSION}")


#--------------------------------------------------------------------------------
# 휠 라이브러리 빌드. (.WHL)
#--------------------------------------------------------------------------------
setuptools.setup(
	name = NAME,
	version = VERSION,
	author = AUTHOR,
	author_email = AUTHOR_EMAIL,
	description = DESCRIPTION,
	long_description = open(file = READMEMD, mode = READ, encoding = UTF8).read(),
	long_description_content_type = LONG_DESCRIPTION_CONTENT_TYPE,
	url = URL,
	packages = setuptools.find_packages(where = SRC),
	include_package_data = True,
	package_dir = { "": SRC },
	package_data = {
		"": [
			"res/*"
		],
	},
	scripts = [

	],
	entry_points = {
		CONSOLESCRIPTS: [
			# "dduk-core=dduk.core.commands:Command"
		]
	},
    install_requires = [
	],
	classifiers = [
		CLASSIFIER_1,
		CLASSIFIER_2,
		CLASSIFIER_3,
	],
	python_requires = PYTHON_REQUIRES
)