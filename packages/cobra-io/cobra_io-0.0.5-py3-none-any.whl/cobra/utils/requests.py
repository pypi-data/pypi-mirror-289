from requests_ratelimiter import LimiterSession


"""
Main session object to use when interacting with any part of the CoBRA API.

Features:
 - Rate limiting: <= 5 per second and <= 100 per minute
"""
session = LimiterSession(per_second=5, per_minute=100)
