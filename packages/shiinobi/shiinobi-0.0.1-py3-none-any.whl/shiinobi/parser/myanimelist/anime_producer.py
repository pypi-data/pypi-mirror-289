import datetime
from typing import TypedDict

from dateutil import parser
from shiinobi.decorators.return_error_decorator import return_on_error

from shiinobi.mixins.base import BaseClientWithHelper

__all__ = ["AnimeProducerParser"]


class ProducerDictionary(TypedDict):
    mal_id: str
    name: str
    name_japanese: str
    established: datetime.datetime
    about: str


class AnimeProducerParser(BaseClientWithHelper):
    def __init__(self, html: str):
        super().__init__()

        self.parser = self.get_parser(html)

    @property
    @return_on_error("")
    def get_producer_url(self):
        return self.parser.css_first('meta[property="og:url"]').attributes["content"]

    @property
    @return_on_error("")
    def get_producer_id(self) -> str:
        return self.regex_helper.get_id_from_url(self.get_producer_url)

    @property
    @return_on_error("")
    def get_producer_name(self) -> str:
        node = self.parser.css_first(".title-name")
        return self.string_helper.cleanse(node.text())

    @property
    @return_on_error("")
    def get_producer_japanese_name(self) -> str:
        node = self.parser.select("span").text_contains("Japanese:")
        return self.string_helper.cleanse(node.matches[0].next.text())

    @property
    @return_on_error("")
    def get_producer_synonym(self) -> str:
        node = self.parser.select("span").text_contains("Synonyms:")
        return self.string_helper.cleanse(node.matches[0].next.text())

    @property
    @return_on_error("")
    def get_producter_establish_date(self) -> datetime.datetime:
        node = self.parser.select("span").text_contains("Established:")
        string_date = self.string_helper.cleanse(node.matches[0].next.text())
        actual_date = parser.parse(string_date)
        return actual_date

    @property
    @return_on_error("")
    def get_producer_about(self) -> str:
        text = self.parser.css_first(
            "#content > div:nth-of-type(1) div.spaceit_pad > span:not(.dark_text)"
        ).text()
        cleaned_text = self.regex_helper.remove_multiple_newline(text)
        return cleaned_text

    def build_dictionary(self) -> ProducerDictionary:
        dictionary: ProducerDictionary = {
            "mal_id": self.get_producer_id,
            "name": self.get_producer_name,
            "name_japanese": self.get_producer_japanese_name,
            "synonyms": self.get_producer_synonym,
            "established": self.get_producter_establish_date,
            "about": self.get_producer_about,
        }
        return dictionary
