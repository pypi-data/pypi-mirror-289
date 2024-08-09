# coding=utf-8
import datetime
import logging

from autojob.job_tool import job_before

logger = logging.getLogger(__name__)


@job_before
def job_test(*args):
    # 应用启动时，job自动扫描会自动读取下面这行文档描述，当做job的描述，不写的话则默认为job的路径
    """This is a timed task for testing"""
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(now + '__This is a timed task for testing:' + args[0])
