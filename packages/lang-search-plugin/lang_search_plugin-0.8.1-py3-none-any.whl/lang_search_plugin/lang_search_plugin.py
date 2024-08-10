import os
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import logging

logger = logging.getLogger("mkdocs.plugins.lang_search_plugin")

class LangSearchPlugin(BasePlugin):

    config_scheme = (
        ('default_language', config_options.Type(str, default='en')),
        ('languages', config_options.Type(list, default=['en'])),
        ('paths', config_options.Type(dict, default={})),
    )

    def on_pre_build(self, config):
        if 'search' in config['plugins']:
            logger.info("search found in plugins")



    def on_post_build(self, config):
        if 'search' in config['plugins']:
            logger.info("search found in plugins")


