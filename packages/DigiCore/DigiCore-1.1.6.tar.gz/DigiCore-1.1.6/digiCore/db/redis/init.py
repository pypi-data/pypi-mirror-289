# _*_ coding: utf-8 _*_
# @Time : 2024/7/31
# @Author : 杨洋
# @Email ： yangyang@doocn.com
# @File : DigiCore
# @Desc :

from typing import Optional

from loguru import logger
from redis import ConnectionPool, StrictRedis

from digiCore.db.config import REDIS_SERVER, REDIS_PORT, REDIS_PWD


class RedisConnectionPool():

    def __init__(self,
                 host: Optional[str] = REDIS_SERVER,
                 port: Optional[int] = REDIS_PORT,
                 password: Optional[str] = REDIS_PWD,
                 db: Optional[int] = 5):
        self.__pool__ = ConnectionPool(host=host,
                                       port=port,
                                       password=password,
                                       db=db,
                                       max_connections=100)

    def __call__(self):
        return StrictRedis(connection_pool=self.__pool__)

    def __enter__(self):
        self.redis_conn = self()
        return self.redis_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 在这里确保连接被正确释放
        if exc_type is not None:
            # 如果有异常发生，记录错误信息
            logger.error(f"Error: {exc_type}, {exc_val}")

        # 关闭连接
        try:
            self.redis_conn.connection_pool.disconnect()
        except Exception as e:
            logger.error(f"Failed to disconnect from Redis: {e}")
