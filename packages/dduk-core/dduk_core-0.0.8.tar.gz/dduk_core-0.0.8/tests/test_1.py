#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os
import unittest
# from src import dduk
# from dduk import utils # dduk 못알아먹음.
# from ..src.dduk.utils import strutil # 상대 접근 실패.
# from src.dduk.utils import strutil # 성공.
# import src.dduk.utils.strutil # 성공.
from src.dduk.core.repository import Repository # 성공.



#--------------------------------------------------------------------------------
# 테스트 매니저.
#--------------------------------------------------------------------------------
class TestsManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	value : str


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.value = "VALUE!!"


	#--------------------------------------------------------------------------------
	# 출력.
	#--------------------------------------------------------------------------------
	def Print(self) -> None:
		builtins.print(f"TestsManaager.Print(\"{self.value}\")")


#--------------------------------------------------------------------------------
# 유닛테스트.
#--------------------------------------------------------------------------------
class Test_1(unittest.TestCase):
	#--------------------------------------------------------------------------------
	# 유닛테스트.
	#--------------------------------------------------------------------------------
	def test_Main(self):
		# 성공.
		# timestamp = src.dduk.utils.strutil.GetTimestampString()
		# builtins.print(timestamp)

		# 성공.
		# timestamp = strutil.GetTimestampString()
		# builtins.print("tests.test_1.Test_1.test_Main()")
		# builtins.print(timestamp)

		testsManager : TestsManager = Repository.Get(TestsManager)
		testsManager.Print()
