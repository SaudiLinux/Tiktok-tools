#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok Tools Configuration
Author: SayerLinux
"""

# Default settings
DEFAULT_VIDEOS_LIMIT = 10
OUTPUT_DIRECTORY = "./results"
TIMEOUT_SECONDS = 10
MAX_RETRIES = 3

# User-Agent strings for different browsers
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
]

# API endpoints (for reference)
TIKTOK_WEB_URL = "https://www.tiktok.com/@{}"
TIKTOK_API_BASE = "https://api.tiktokv.com/"

# Color settings
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'RESET': '\033[0m'
}

# File formats
SUPPORTED_FORMATS = ['json', 'csv', 'txt']

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FILE = "tiktok_tools.log"