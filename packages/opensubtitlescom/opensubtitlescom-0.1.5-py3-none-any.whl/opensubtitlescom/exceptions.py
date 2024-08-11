"""
Copyright (c) 2023 Omer Duskin.

This file is part of Opensubtitles API wrapper.

Opensubtitles API is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by the Massachusetts
Institute of Technology.

For full details, please see the LICENSE file located in the root
directory of this project.
"""


class OpenSubtitlesException(Exception):
    """Custom exception class for the OpenSubtitles wrapper."""

    def __init__(self, message: str):
        """
        Initialize the custom exception.

        :param message: exception message.
        """
        self.message = message


class OpenSubtitlesFileException(Exception):
    """Custom exception class for files operations in OpenSubtitles wrapper."""

    def __init__(self, message: str):
        """
        Initialize the custom exception.

        :param message: exception message.
        """
        self.message = message
