#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import sys
import os


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
EMPTY : str = ""
NONE : str = "NONE"
COMMA : str = ","
SLASH : str = "/"
BACKSLASH : str = "\\"
COLON : str = ":"
SPACE : str = " "
DEBUG : str = "DEBUG"


#--------------------------------------------------------------------------------
# 프로젝트 생성.
#--------------------------------------------------------------------------------
def CreateProject(rootPath : str) -> None:
	builtins.print("dduk.application.command.CreateProject()")


#--------------------------------------------------------------------------------
# 명령어 스크립트 생성.
#--------------------------------------------------------------------------------
def CreateCommandScript(rootPath : str) -> None:
	builtins.print("dduk.application.command.CreateCommandScript()")


#--------------------------------------------------------------------------------
# 명령어 스크립트 제거.
#--------------------------------------------------------------------------------
def DestroyCommandScript(rootPath : str) -> None:
	builtins.print("dduk.application.command.DestroyCommandScript()")


#--------------------------------------------------------------------------------
# 실행 함수.
#--------------------------------------------------------------------------------
def Main() -> None:
	rootPath = os.getcwd()
	rootPath = rootPath.replace(BACKSLASH, SLASH)

	if sys.argv:
		command = sys.argv[0]
		command = command.lower()
		if command == "project":
			# builtins.print(f"{rootPath}/.git")
			builtins.print(f"{rootPath}/.vscode")
			builtins.print(f"{rootPath}/.vscode/launch.json")
			builtins.print(f"{rootPath}/.vscode/settings.json")
			builtins.print(f"{rootPath}/.vscode/tasks.json")
			# builtins.print(f"{rootPath}/.venv")
			builtins.print(f"{rootPath}/build")
			builtins.print(f"{rootPath}/docs")
			builtins.print(f"{rootPath}/hints")
			builtins.print(f"{rootPath}/hooks")
			builtins.print(f"{rootPath}/libs")
			builtins.print(f"{rootPath}/logs")
			builtins.print(f"{rootPath}/res")
			builtins.print(f"{rootPath}/src")
			builtins.print(f"{rootPath}/tests")
			builtins.print(f"{rootPath}/workspace")
			builtins.print(f"{rootPath}/.gitignore")
			builtins.print(f"{rootPath}/requirements.txt")
		elif command == "bat":
			builtins.print(f"{rootPath}/build.bat")
			builtins.print(f"{rootPath}/environment.bat")
			builtins.print(f"{rootPath}/package.bat")
			builtins.print(f"{rootPath}/run.bat")
			builtins.print(f"{rootPath}/service.bat")
			builtins.print(f"{rootPath}/variable.bat")
			builtins.print(f"{rootPath}/venv.bat")
		elif command == "sh":
			builtins.print(f"{rootPath}/build.sh")
			builtins.print(f"{rootPath}/environment.sh")
			builtins.print(f"{rootPath}/package.sh")
			builtins.print(f"{rootPath}/run.sh")
			builtins.print(f"{rootPath}/service.sh")
			builtins.print(f"{rootPath}/variable.sh")
			builtins.print(f"{rootPath}/venv.sh")
		else:
			builtins.print(f"잘못된 명령어: {command}, 오류: 1")
	else:
		builtins.print("Usage: dduk-application \{project|bat|sh\}")
		builtins.print("dduk-application project: 현재 경로를 루트로 삼아 프로젝트 템플릿 생성.")
		builtins.print("dduk-application bat: 현재 경로를 루트로 삼아 프로젝트 배치파일 생성. (Windows)")
		builtins.print("dduk-application sh: 현재 경로를 루트로 삼아 프로젝트 쉘스크립트 생성. (Linux/MacOS)")