"""签到脚本的单元测试。用假的 HTTP 会话返回预设响应, 不访问网络。

运行: python -m unittest -v
"""

import datetime
import logging
import os
import sys
import types
import unittest
from unittest import mock
from urllib.parse import urlparse

try:
    import pypushdeer  # noqa: F401
except ImportError:  # 本地没装 pypushdeer 时用替身, 测试不会真正推送
    sys.modules["pypushdeer"] = types.SimpleNamespace(PushDeer=mock.MagicMock())

import checkin
from checkin import Checker, Config

# Actions 中未配置的 secret 会以空字符串传入
EMPTY_ENV = {"GLADOS_COOKIES": "", "PUSHDEER_SENDKEY": "", "GLADOS_EXCHANGE_PLAN": "", "GLADOS_VERBOSE": ""}


def setUpModule():
    # 测试时不输出签到日志
    logging.getLogger().setLevel(logging.CRITICAL + 1)


class FakeResponse:
    def __init__(self, payload=None, status_code=200, text=""):
        self.status_code = status_code
        self.ok = status_code < 400
        self.payload = payload
        self.text = text

    def json(self):
        return self.payload


# 真实服务器对不属于该域名 (或已失效) 的 Cookie 的响应
NO_PERMISSION = FakeResponse({"code": -2, "message": "No permission"})


class FakeSession:
    """按 (Cookie, 域名, 路径) 返回预设响应, 没有预设的请求返回 No permission。记录所有请求。"""

    def __init__(self, routes):
        self.routes = routes
        self.headers = {}
        self.calls = []
        self.last_post_data = None

    def _respond(self, url, headers):
        parsed = urlparse(url)
        key = (headers["cookie"], parsed.netloc, parsed.path)
        self.calls.append(key)
        return self.routes.get(key, NO_PERMISSION)

    def get(self, url, headers, timeout):
        return self._respond(url, headers)

    def post(self, url, headers, data, timeout):
        self.last_post_data = data
        return self._respond(url, headers)

    def close(self):
        pass


def account(cookie, domain, checkin_code=1, points="179.0000000000000000"):
    """只属于 domain 的账号。checkin_code: 0 签到成功, 1 今天已签到过"""
    return {
        (cookie, domain, "/api/user/checkin"): FakeResponse({"code": checkin_code, "message": "ok", "points": 1 if checkin_code == 0 else 0}),
        (cookie, domain, "/api/user/status"): FakeResponse({"code": 0, "data": {"leftDays": "30.5"}}),
        (cookie, domain, "/api/user/points"): FakeResponse({"code": 0, "points": points}),
        (cookie, domain, "/api/user/exchange"): FakeResponse({"code": 0, "message": "ok"}),
    }


def run_checkin(routes, cookies, **env):
    session = FakeSession(routes)
    environ = dict(EMPTY_ENV, GLADOS_COOKIES="&".join(cookies), **env)
    with mock.patch.dict(os.environ, environ), \
            mock.patch.object(checkin.requests, "Session", return_value=session), \
            mock.patch.object(checkin.time, "sleep") as sleep:
        checker = Checker(Config())
        checker.checkin_all()
    return checker, session, sleep


def requested_paths(session, domain):
    return [path for _, netloc, path in session.calls if netloc == domain]


class CheckinTest(unittest.TestCase):
    def test_cookie_of_first_domain_does_not_try_other_domains(self):
        checker, session, _ = run_checkin(account("c1", "glados.cloud"), ["c1"])

        self.assertEqual(requested_paths(session, "railgun.info"), [])
        title, content, log_content = checker.format_results()
        self.assertEqual(title, "GLaDOS 签到, 成功0, 失败0, 重复1")
        self.assertEqual(content, "#1 [glados.cloud] P:0 剩余:30 天 总积分:179 积分 | 重复签到 | 未兑换: 积分不足 (179/500)")
        # 未开启 GLADOS_VERBOSE 时日志中不显示天数和积分
        self.assertEqual(log_content, "#1 [glados.cloud] 重复签到")
        self.assertEqual(checker.get_failed_cookies(), [])

    def test_rejection_by_other_domain_is_not_counted_as_failure(self):
        checker, session, _ = run_checkin(account("c1", "railgun.info", checkin_code=0), ["c1"])

        # 被拒绝的域名上只尝试签到, 不再查询和兑换
        self.assertEqual(requested_paths(session, "glados.cloud"), ["/api/user/checkin"])
        title, content, _ = checker.format_results()
        self.assertEqual(title, "GLaDOS 签到, 成功1, 失败0, 重复0")
        self.assertEqual(content, "#1 [railgun.info] P:1 剩余:30 天 总积分:179 积分 | 签到成功 | 未兑换: 积分不足 (179/500)")
        self.assertEqual(checker.get_failed_cookies(), [])

    def test_cookie_rejected_by_every_domain_fails(self):
        checker, _, _ = run_checkin({}, ["expired"])

        title, content, log_content = checker.format_results()
        self.assertEqual(title, "GLaDOS 签到, 成功0, 失败1, 重复0")
        expected = "#1 [glados.cloud] 签到失败: No permission\n#1 [railgun.info] 签到失败: No permission"
        self.assertEqual(content, expected)
        self.assertEqual(log_content, expected)
        self.assertEqual(checker.get_failed_cookies(), [1])
        self.assertEqual(checker.get_failure_causes(1), (False, True))

    def test_each_cookie_is_counted_once(self):
        routes = {**account("c1", "glados.cloud", checkin_code=0), **account("c3", "railgun.info")}
        checker, _, _ = run_checkin(routes, ["c1", "expired", "c3"])

        title, _, _ = checker.format_results()
        self.assertEqual(title, "GLaDOS 签到, 成功1, 失败1, 重复1")
        self.assertEqual(checker.get_failed_cookies(), [2])

    def test_server_error_is_retried_then_reported_as_request_error(self):
        bad_gateway = FakeResponse(status_code=502, text="<html><head><title>502 Bad Gateway</title></head></html>")
        checker, session, sleep = run_checkin({("c1", "glados.cloud", "/api/user/checkin"): bad_gateway}, ["c1"])

        self.assertEqual(requested_paths(session, "glados.cloud"), ["/api/user/checkin"] * 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [10, 30])
        # glados.cloud 请求出错, railgun.info 拒绝了 Cookie
        self.assertEqual(checker.get_failure_causes(1), (True, True))

    def test_exchange_when_points_are_enough(self):
        routes = account("c1", "glados.cloud", points="120.0000000000000000")
        checker, session, _ = run_checkin(routes, ["c1"], GLADOS_EXCHANGE_PLAN="plan100")

        self.assertEqual(session.last_post_data, {"planType": "plan100"})
        self.assertEqual(checker.results[0].exchange, "兑换成功: plan100")

    def test_no_exchange_request_when_points_are_not_enough(self):
        checker, session, _ = run_checkin(account("c1", "glados.cloud", points="499"), ["c1"])

        self.assertNotIn("/api/user/exchange", requested_paths(session, "glados.cloud"))
        self.assertEqual(checker.results[0].exchange, "未兑换: 积分不足 (499/500)")

    def test_exchange_is_still_tried_when_points_are_unknown(self):
        routes = account("c1", "glados.cloud")
        routes[("c1", "glados.cloud", "/api/user/points")] = FakeResponse(status_code=403, text="Forbidden")
        checker, session, _ = run_checkin(routes, ["c1"])

        self.assertIn("/api/user/exchange", requested_paths(session, "glados.cloud"))
        self.assertEqual(checker.results[0].exchange, "兑换成功: plan500")


class ConfigTest(unittest.TestCase):
    def load(self, **env):
        with mock.patch.dict(os.environ, dict(EMPTY_ENV, **env)), \
                mock.patch.object(checkin.logger, "warning") as warning:
            config = Config()
        return config, "\n".join(str(call.args[0]) for call in warning.call_args_list)

    def test_empty_verbose_secret_is_treated_as_unset(self):
        config, warnings = self.load(GLADOS_COOKIES="c1")

        self.assertFalse(config.verbose)
        self.assertNotIn("GLADOS_VERBOSE", warnings)

    def test_verbose_secret(self):
        config, _ = self.load(GLADOS_COOKIES="c1", GLADOS_VERBOSE=" True ")

        self.assertTrue(config.verbose)

    def test_cookies_are_split_and_trimmed(self):
        config, _ = self.load(GLADOS_COOKIES=" c1 & c2 &")

        self.assertEqual(config.cookies_list, ["c1", "c2"])


class MainTest(unittest.TestCase):
    def run_main(self):
        with self.assertRaises(SystemExit) as exit_info:
            checkin.main()
        return exit_info.exception.code

    def test_successful_checkin_exits_normally(self):
        session = FakeSession(account("c1", "glados.cloud", checkin_code=0))
        with mock.patch.dict(os.environ, dict(EMPTY_ENV, GLADOS_COOKIES="c1")), \
                mock.patch.object(checkin.requests, "Session", return_value=session):
            self.assertEqual(self.run_main(), 0)

    def test_expired_cookie_exits_with_error(self):
        with mock.patch.dict(os.environ, dict(EMPTY_ENV, GLADOS_COOKIES="expired")), \
                mock.patch.object(checkin.requests, "Session", return_value=FakeSession({})):
            self.assertEqual(self.run_main(), 1)

    def test_no_valid_cookie_exits_with_error(self):
        with mock.patch.dict(os.environ, dict(EMPTY_ENV, GLADOS_COOKIES=" & ")):
            self.assertEqual(self.run_main(), 1)

    def test_unexpected_error_exits_with_error_instead_of_crashing(self):
        with mock.patch.object(checkin, "Config", side_effect=RuntimeError("boom")):
            self.assertEqual(self.run_main(), 1)


class LoggingTest(unittest.TestCase):
    def test_log_time_is_beijing_time(self):
        formatter = logging.getLogger().handlers[0].formatter
        record = logging.makeLogRecord({"msg": "hi", "levelname": "INFO"})
        record.created = datetime.datetime(2026, 11, 3, 16, 30, tzinfo=datetime.timezone.utc).timestamp()

        # UTC 16:30 是北京时间第二天 0:30
        self.assertEqual(formatter.format(record), "2026-11-04 00:30:00 - INFO - hi")


if __name__ == "__main__":
    unittest.main()
