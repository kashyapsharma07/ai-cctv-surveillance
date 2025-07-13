import streamlit as st
import os
import sys

# Add the app directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

# Import and run the existing portfolio app
import portfolio_app 