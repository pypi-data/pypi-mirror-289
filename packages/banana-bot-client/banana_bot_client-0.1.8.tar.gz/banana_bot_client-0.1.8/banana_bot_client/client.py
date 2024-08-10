import requests

from .constants import (
    ACHIEVE_QUEST_API,
    BANANA_LIST_API,
    CLAIM_LOTTERY_API,
    CLAIM_QUEST_API,
    CLAIM_QUEST_LOTTERY_API,
    DO_CLICK_API,
    DO_LOTTERY_API,
    EQUIP_BANANA_API,
    LOTTERY_INFO_API,
    QUEST_LIST_API,
    USER_INFO_API,
)
from .exceptions import ClaimIncompleteQuestError, UnknownBananaRequestError
from .models import (
    BananaListModel,
    ClaimQuestModel,
    ClickRewardModel,
    DoLotteryModel,
    LotteryInfoModel,
    QuestListModel,
    UserInfoModel,
)


class BananaBotClient:
    def __init__(self, token: str):
        self.token = token

    @property
    def default_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def _make_request(
        self, method: str, url: str, headers=None, proxies=None, **kwargs
    ):
        """
        expected proxies: https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module
        """
        request_headers = self.default_headers.copy()
        if headers:
            request_headers.update(headers)

        response = requests.request(
            method,
            url,
            headers=request_headers,
            proxies=proxies,
            timeout=20,
            **kwargs,
        )
        response.raise_for_status()
        response_json = response.json()
        # TODO: expend the error handling
        if response_json["code"] != 0 or response_json["msg"] != "Success":
            if response_json["code"] == 4404:
                raise ClaimIncompleteQuestError(response_json["msg"])
            code = response_json["code"]
            msg = response_json["msg"]
            raise UnknownBananaRequestError(f"code: {code}, msg: {msg}")
        return response_json["data"]

    def get_lottery_info(self, headers=None, proxies=None) -> LotteryInfoModel:
        data = self._make_request(
            "GET", LOTTERY_INFO_API, headers=headers, proxies=proxies
        )
        return LotteryInfoModel(**data)

    def do_lottery(self, headers=None, proxies=None) -> DoLotteryModel:
        """
        claim a banana once the countdown is done
        """
        data = self._make_request(
            "POST", DO_LOTTERY_API, headers=headers, proxies=proxies
        )
        return DoLotteryModel(**data)

    def claim_lottery(self, headers=None, proxies=None) -> None:
        """
        harvest and reveal a banana
        """
        _ = self._make_request(
            "POST",
            CLAIM_LOTTERY_API,
            headers=headers,
            proxies=proxies,
            json={"claimLotteryType": 1},
        )
        return None  # Since the response data is None, just return None

    def get_quest_list(self, headers=None, proxies=None) -> QuestListModel:
        data = self._make_request(
            "GET", QUEST_LIST_API, headers=headers, proxies=proxies
        )
        return QuestListModel(**data)

    def achieve_quest(self, quest_id: int, headers=None, proxies=None) -> None:
        """
        complete a request
        """
        _ = self._make_request(
            "POST",
            ACHIEVE_QUEST_API,
            headers=headers,
            proxies=proxies,
            json={"quest_id": quest_id},
        )
        return None  # Since the response data is None, just return None

    def claim_quest(self, quest_id: int, headers=None, proxies=None) -> ClaimQuestModel:
        """
        claim rewards for a completed quest
        """
        data = self._make_request(
            "POST",
            CLAIM_QUEST_API,
            headers=headers,
            proxies=proxies,
            json={"quest_id": quest_id},
        )
        return ClaimQuestModel(**data)

    def claim_quest_lottery(self, headers=None, proxies=None) -> None:
        """
        claim additional banana for every completed 3 quests
        """
        _ = self._make_request(
            "POST", CLAIM_QUEST_LOTTERY_API, headers=headers, proxies=proxies
        )
        return None  # Since the response data is None, just return None

    def click(self, click_count: int, headers=None, proxies=None) -> ClickRewardModel:
        data = self._make_request(
            "POST",
            DO_CLICK_API,
            headers=headers,
            proxies=proxies,
            json={"clickCount": click_count},
        )
        return ClickRewardModel(**data)

    def get_user_info(self, headers=None, proxies=None) -> UserInfoModel:
        data = self._make_request(
            "GET", USER_INFO_API, headers=headers, proxies=proxies
        )
        return UserInfoModel(**data)

    def get_banana_list(self, headers=None, proxies=None) -> BananaListModel:
        data = self._make_request(
            "GET", BANANA_LIST_API, headers=headers, proxies=proxies
        )
        return BananaListModel(**data)

    def equip_banana(self, banana_id: int, headers=None, proxies=None) -> None:
        _ = self._make_request(
            "POST",
            EQUIP_BANANA_API,
            headers=headers,
            proxies=proxies,
            json={"bananaId": banana_id},
        )
        return None
