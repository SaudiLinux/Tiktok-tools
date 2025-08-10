#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example usage of TikTok Tools
Author: SayerLinux
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the tool class
exec(open('tiktok-tools.py').read())

def example_usage():
    """Example of how to use TikTok Tools programmatically"""
    
    # Initialize the tool
    tool = TikTokTools()
    
    # Display banner
    tool.display_banner()
    
    # Example target (you can change this)
    target = "example_user"  # Replace with actual username
    
    print(f"[*] Running example analysis for: @{target}")
    print("[*] Note: This is a demo - replace 'example_user' with real username")
    
    # This would work with real username
    # user_data = tool.get_user_info(target)
    # if user_data:
    #     tool.display_user_info(user_data)
    #     videos = tool.get_videos_info(target, limit=5)
    #     tool.display_videos_info(videos)
    #     tool.save_results(target, user_data, videos)

if __name__ == "__main__":
    example_usage()