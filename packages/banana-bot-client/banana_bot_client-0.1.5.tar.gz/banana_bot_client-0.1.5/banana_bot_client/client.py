import json
import os
import random

import requests
from dotenv import load_dotenv
from loguru import logger
from retry import retry

load_dotenv()


class BananaAPIClient:
    USER_INFO_API = "https://interface.carv.io/banana/get_user_info"
    LOTTERY_INFO_API = "https://interface.carv.io/banana/get_lottery_info"
    DO_LOTTERY_API = "https://interface.carv.io/banana/do_lottery"
    CLAIM_LOTTERY_API = "https://interface.carv.io/banana/claim_lottery"
    QUEST_LIST_API = "https://interface.carv.io/banana/get_quest_list"
    ACHIEVE_QUEST_API = "https://interface.carv.io/banana/achieve_quest"
    CLAIM_QUEST_API = "https://interface.carv.io/banana/claim_quest"
    CLAIM_QUEST_LOTTERY_API = "https://interface.carv.io/banana/claim_quest_lottery"
    DO_CLICK_API = "https://interface.carv.io/banana/do_click"

    def __init__(self):
        self.tokens = self._get_tokens()

    def _get_tokens(self):
        try:
            with open("configs/config.json", "r") as file:
                tokens = json.load(file)
                for index, item in enumerate(tokens):
                    logger.info(f"Token {index + 1}: {item['token']}")
                logger.info(f"Total tokens: {len(tokens)}")
                return tokens
        except FileNotFoundError:
            logger.error("Token not found, please add token on configs/config.json")
            return None

    def _validate_tokens(self):
        valid_tokens = []
        for token in self.tokens:
            try:
                response = requests.get(
                    self.USER_INFO_API,
                    headers={"Authorization": f"Bearer {token['token']}"},
                )
                response.raise_for_status()
                valid_tokens.append(token)
            except requests.exceptions.RequestException as e:
                logger.error(f"Token not valid, response code: {e}")

        logger.info(f"Token valid: {len(valid_tokens)}")
        return valid_tokens

    def claim_lottery(self):
        tokens = self._validate_tokens()
        if not tokens:
            return

        for token in tokens:
            try:
                info = requests.get(
                    self.LOTTERY_INFO_API,
                    headers={"Authorization": f"Bearer {token['token']}"},
                )
                info.raise_for_status()
                data = info.json().get("data", {})
                remain_lottery = data.get("remain_lottery_count", 0)
                for _ in range(remain_lottery):
                    requests.post(
                        self.DO_LOTTERY_API,
                        headers={"Authorization": f"Bearer {token['token']}"},
                    )
                    logger.info("Lottery claimed successfully")
                if data.get("countdown_end"):
                    requests.post(
                        self.CLAIM_LOTTERY_API,
                        json={"claimLotteryType": 1},
                        headers={"Authorization": f"Bearer {token['token']}"},
                    )
                    logger.info("Farming claimed successfully")
                else:
                    logger.info("Farming countdown..")
            except requests.exceptions.RequestException as e:
                logger.error(e)

    def claim_mission(self):
        tokens = self._validate_tokens()
        if not tokens:
            return

        for token in tokens:
            try:
                info = requests.get(
                    self.QUEST_LIST_API,
                    headers={"Authorization": f"Bearer {token['token']}"},
                )
                info.raise_for_status()
                quest_data = info.json().get("data", {}).get("quest_list", [])
                mission_list = [q for q in quest_data if q.get("quest_id") != 10]
                mission_not_claimed = [
                    q for q in mission_list if not q.get("is_claimed")
                ]
                mission_not_completed = [
                    q for q in mission_list if not q.get("is_achieved")
                ]

                for mission in mission_not_completed:
                    requests.post(
                        self.ACHIEVE_QUEST_API,
                        json={"quest_id": mission.get("quest_id")},
                        headers={"Authorization": f"Bearer {token['token']}"},
                    )
                    logger.info(
                        f"Mission {mission.get('quest_name')} completed successfully"
                    )

                for mission in mission_not_claimed:
                    requests.post(
                        self.CLAIM_QUEST_API,
                        json={"quest_id": mission.get("quest_id")},
                        headers={"Authorization": f"Bearer {token['token']}"},
                    )
                    logger.info(
                        f"Mission {mission.get('quest_name')} claimed successfully"
                    )

                if not mission_not_claimed:
                    claim_lottery = requests.post(
                        self.CLAIM_QUEST_LOTTERY_API,
                        headers={"Authorization": f"Bearer {token['token']}"},
                    )
                    if claim_lottery.json().get("code") != 4404:
                        logger.info("Lottery claimed successfully")
                    else:
                        logger.info("No quest lottery left")

            except requests.exceptions.RequestException as e:
                logger.error(e)

    @retry(tries=5, delay=2, backoff=2)
    def _do_click(self, token):
        response = requests.post(
            self.DO_CLICK_API,
            json={"clickCount": random.randint(1, 10)},
            headers={"Authorization": f"Bearer {token['token']}"},
        )
        response.raise_for_status()
        return response

    def click_rewards(self):
        tokens = self._validate_tokens()
        if not tokens:
            return

        for token in tokens:
            try:
                info = requests.get(
                    self.USER_INFO_API,
                    headers={"Authorization": f"Bearer {token['token']}"},
                )
                info.raise_for_status()
                data = info.json().get("data", {})
                max_click = data.get("max_click_count", 0)
                today_click = data.get("today_click_count", 0)

                while today_click < max_click:
                    try:
                        self._do_click(token)
                        logger.info(f"Click successfully {today_click + 1}")
                        today_click += 1
                        if today_click == max_click:
                            logger.info(f"Click done {today_click}")
                            break
                    except requests.exceptions.RequestException as e:
                        logger.error(f"Click failed: {e}")
            except requests.exceptions.RequestException as e:
                logger.error(f"Message: {e}")
