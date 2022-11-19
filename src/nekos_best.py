from os import getcwd
from time import time
from pathlib import Path
from requests import get

class NekosBest:
	def __init__(self) -> None:
		self.api = "https://nekos.best/api/v2"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def save_file(
			self,
			content: bytes,
			location: str = getcwd()) -> bool:
		with open(
			Path(location).joinpath(f"{time() * 1000}.jpg"),
		mode="wb+",
		) as file:
			file.write(content)
			file.close()
		return True

	def get_endpoints(self) -> dict:
		return get(
			f"{self.api}/endpoints",
			headers=self.headers).json()
	
	def get_random_image(
			self,
			category: str,
			amount: int = 1) -> dict:
		return get(
			f"{self.api}/{category}?amount={amount}",
			headers=self.headers).json()
	
	def search_for_phrase(
			self,
			query: str,
			category: str,
			amount: int = 1) -> dict:
		return get(
			f"{self.api}/search?query={query}&type={type}&category={category}&amount={amount}",
			headers=self.headers).json()
			
	def get_file(
			self,
			category: str,
			file_name: str,
			format: str) -> bool:
		return self.save_file(get(
			f"{self.api}/{category}/{file_name}.{format}",
			headers=self.headers).content)
