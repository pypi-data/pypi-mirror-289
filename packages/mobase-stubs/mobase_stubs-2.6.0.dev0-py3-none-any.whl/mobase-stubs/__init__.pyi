from __future__ import annotations

__version__ = "2.6.0.dev0"

import abc
import os
from enum import Enum
from typing import (
    Callable,
    Dict,
    Iterator,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
    overload,
)

import PyQt6.QtCore
import PyQt6.QtGui
import PyQt6.QtWidgets

GameFeatureType = TypeVar("GameFeatureType")
MoVariant = None | bool | int | str | list[object] | dict[str, object]
INVALID_HANDLE_VALUE: int = ...

def getFileVersion(
    filepath: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo],
) -> str:
    """
    Retrieve the file version of the given executable.

    Args:
        filepath: Absolute path to the executable.

    Returns:
        The file version, or an empty string if the file version could not be retrieved.
    """
    ...

def getIconForExecutable(
    executable: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo],
) -> PyQt6.QtGui.QIcon:
    """
    Retrieve the icon of an executable. Currently this always extracts the biggest icon.

    Args:
        executable: Absolute path to the executable.

    Returns:
        The icon for this executable, if any.
    """
    ...

def getProductVersion(
    executable: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo],
) -> str:
    """
    Retrieve the product version of the given executable.

    Args:
        executable: Absolute path to the executable.

    Returns:
        The product version, or an empty string if the product version could not be retrieved.
    """
    ...

class EndorsedState(Enum):
    ENDORSED_FALSE = ...
    ENDORSED_TRUE = ...
    ENDORSED_UNKNOWN = ...
    ENDORSED_NEVER = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: EndorsedState, other: object) -> bool: ...
    def __ge__(self: EndorsedState, other: EndorsedState) -> bool: ...
    def __gt__(self: EndorsedState, other: EndorsedState) -> bool: ...
    def __int__(self: EndorsedState) -> int: ...
    def __le__(self: EndorsedState, other: EndorsedState) -> bool: ...
    def __lt__(self: EndorsedState, other: EndorsedState) -> bool: ...
    def __ne__(self: EndorsedState, other: object) -> bool: ...
    def __str__(self: EndorsedState) -> str: ...

class GuessQuality(Enum):
    """
    Describes how good the code considers a guess (i.e. for a mod name) this is used to
    determine if a name from another source should overwrite or not.
    """

    INVALID = ...
    FALLBACK = ...
    GOOD = ...
    META = ...
    PRESET = ...
    USER = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: GuessQuality, other: object) -> bool: ...
    def __int__(self: GuessQuality) -> int: ...
    def __ne__(self: GuessQuality, other: object) -> bool: ...
    def __str__(self: GuessQuality) -> str: ...

class InstallResult(Enum):
    SUCCESS = ...
    FAILED = ...
    CANCELED = ...
    MANUAL_REQUESTED = ...
    NOT_ATTEMPTED = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: InstallResult, other: object) -> bool: ...
    def __int__(self: InstallResult) -> int: ...
    def __ne__(self: InstallResult, other: object) -> bool: ...
    def __str__(self: InstallResult) -> str: ...

class LoadOrderMechanism(Enum):
    NONE = ...
    FILE_TIME = ...
    PLUGINS_TXT = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: LoadOrderMechanism, other: object) -> bool: ...
    def __int__(self: LoadOrderMechanism) -> int: ...
    def __ne__(self: LoadOrderMechanism, other: object) -> bool: ...
    def __str__(self: LoadOrderMechanism) -> str: ...

class ModState(Enum):
    EXISTS = ...
    ACTIVE = ...
    ESSENTIAL = ...
    EMPTY = ...
    ENDORSED = ...
    VALID = ...
    ALTERNATE = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __and__(self: ModState, other: ModState) -> ModState: ...
    def __eq__(self: ModState, other: object) -> bool: ...
    def __ge__(self: ModState, other: ModState) -> bool: ...
    def __gt__(self: ModState, other: ModState) -> bool: ...
    def __int__(self: ModState) -> int: ...
    def __invert__(self: ModState) -> ModState: ...
    def __le__(self: ModState, other: ModState) -> bool: ...
    def __lt__(self: ModState, other: ModState) -> bool: ...
    def __ne__(self: ModState, other: object) -> bool: ...
    def __or__(self: ModState, other: ModState) -> ModState: ...
    def __rand__(self: ModState, other: ModState) -> ModState: ...
    def __ror__(self: ModState, other: ModState) -> ModState: ...
    def __rxor__(self: ModState, other: ModState) -> ModState: ...
    def __str__(self: ModState) -> str: ...
    def __xor__(self: ModState, other: ModState) -> ModState: ...

class PluginState(Enum):
    MISSING = ...
    INACTIVE = ...
    ACTIVE = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __and__(self: PluginState, other: PluginState) -> PluginState: ...
    def __eq__(self: PluginState, other: object) -> bool: ...
    def __ge__(self: PluginState, other: PluginState) -> bool: ...
    def __gt__(self: PluginState, other: PluginState) -> bool: ...
    def __int__(self: PluginState) -> int: ...
    def __invert__(self: PluginState) -> PluginState: ...
    def __le__(self: PluginState, other: PluginState) -> bool: ...
    def __lt__(self: PluginState, other: PluginState) -> bool: ...
    def __ne__(self: PluginState, other: object) -> bool: ...
    def __or__(self: PluginState, other: PluginState) -> PluginState: ...
    def __rand__(self: PluginState, other: PluginState) -> PluginState: ...
    def __ror__(self: PluginState, other: PluginState) -> PluginState: ...
    def __rxor__(self: PluginState, other: PluginState) -> PluginState: ...
    def __str__(self: PluginState) -> str: ...
    def __xor__(self: PluginState, other: PluginState) -> PluginState: ...

class ProfileSetting(Enum):
    MODS = ...
    CONFIGURATION = ...
    SAVEGAMES = ...
    PREFER_DEFAULTS = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __and__(self: ProfileSetting, other: ProfileSetting) -> ProfileSetting: ...
    def __eq__(self: ProfileSetting, other: object) -> bool: ...
    def __ge__(self: ProfileSetting, other: ProfileSetting) -> bool: ...
    def __gt__(self: ProfileSetting, other: ProfileSetting) -> bool: ...
    def __int__(self: ProfileSetting) -> int: ...
    def __invert__(self: ProfileSetting) -> ProfileSetting: ...
    def __le__(self: ProfileSetting, other: ProfileSetting) -> bool: ...
    def __lt__(self: ProfileSetting, other: ProfileSetting) -> bool: ...
    def __ne__(self: ProfileSetting, other: object) -> bool: ...
    def __or__(self: ProfileSetting, other: ProfileSetting) -> ProfileSetting: ...
    def __rand__(self: ProfileSetting, other: ProfileSetting) -> ProfileSetting: ...
    def __ror__(self: ProfileSetting, other: ProfileSetting) -> ProfileSetting: ...
    def __rxor__(self: ProfileSetting, other: ProfileSetting) -> ProfileSetting: ...
    def __str__(self: ProfileSetting) -> str: ...
    def __xor__(self: ProfileSetting, other: ProfileSetting) -> ProfileSetting: ...

class ReleaseType(Enum):
    FINAL = ...
    CANDIDATE = ...
    BETA = ...
    ALPHA = ...
    PRE_ALPHA = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: ReleaseType, other: object) -> bool: ...
    def __int__(self: ReleaseType) -> int: ...
    def __ne__(self: ReleaseType, other: object) -> bool: ...
    def __str__(self: ReleaseType) -> str: ...

class SortMechanism(Enum):
    NONE = ...
    MLOX = ...
    BOSS = ...
    LOOT = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: SortMechanism, other: object) -> bool: ...
    def __int__(self: SortMechanism) -> int: ...
    def __ne__(self: SortMechanism, other: object) -> bool: ...
    def __str__(self: SortMechanism) -> str: ...

class TrackedState(Enum):
    TRACKED_FALSE = ...
    TRACKED_TRUE = ...
    TRACKED_UNKNOWN = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: TrackedState, other: object) -> bool: ...
    def __ge__(self: TrackedState, other: TrackedState) -> bool: ...
    def __gt__(self: TrackedState, other: TrackedState) -> bool: ...
    def __int__(self: TrackedState) -> int: ...
    def __le__(self: TrackedState, other: TrackedState) -> bool: ...
    def __lt__(self: TrackedState, other: TrackedState) -> bool: ...
    def __ne__(self: TrackedState, other: object) -> bool: ...
    def __str__(self: TrackedState) -> str: ...

class VersionScheme(Enum):
    DISCOVER = ...
    REGULAR = ...
    DECIMAL_MARK = ...
    NUMBERS_AND_LETTERS = ...
    DATE = ...
    LITERAL = ...

    @property
    def value(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __eq__(self: VersionScheme, other: object) -> bool: ...
    def __int__(self: VersionScheme) -> int: ...
    def __ne__(self: VersionScheme, other: object) -> bool: ...
    def __str__(self: VersionScheme) -> str: ...

class ExecutableForcedLoadSetting:
    def __init__(
        self: ExecutableForcedLoadSetting, process: str, library: str
    ) -> None: ...
    def enabled(self: ExecutableForcedLoadSetting) -> bool: ...
    def forced(self: ExecutableForcedLoadSetting) -> bool: ...
    def library(self: ExecutableForcedLoadSetting) -> str: ...
    def process(self: ExecutableForcedLoadSetting) -> str: ...
    def withEnabled(
        self: ExecutableForcedLoadSetting, enabled: bool
    ) -> ExecutableForcedLoadSetting: ...
    def withForced(
        self: ExecutableForcedLoadSetting, forced: bool
    ) -> ExecutableForcedLoadSetting: ...

class ExecutableInfo:
    def __init__(
        self: ExecutableInfo,
        title: str,
        binary: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo],
    ) -> None: ...
    def arguments(self: ExecutableInfo) -> Sequence[str]: ...
    def asCustom(self: ExecutableInfo) -> ExecutableInfo: ...
    def binary(self: ExecutableInfo) -> PyQt6.QtCore.QFileInfo: ...
    def isCustom(self: ExecutableInfo) -> bool: ...
    def isValid(self: ExecutableInfo) -> bool: ...
    def steamAppID(self: ExecutableInfo) -> str: ...
    def title(self: ExecutableInfo) -> str: ...
    def withArgument(self: ExecutableInfo, argument: str) -> ExecutableInfo: ...
    def withSteamAppId(self: ExecutableInfo, app_id: str) -> ExecutableInfo: ...
    def withWorkingDirectory(
        self: ExecutableInfo, directory: Union[str, os.PathLike[str], PyQt6.QtCore.QDir]
    ) -> ExecutableInfo: ...
    def workingDirectory(self: ExecutableInfo) -> PyQt6.QtCore.QDir: ...

class FileInfo:
    """
    Information about a virtualized file
    """

    @property
    def archive(self) -> str: ...
    @archive.setter
    def archive(self, arg0: str) -> None: ...
    @property
    def filePath(self) -> str: ...
    @filePath.setter
    def filePath(self, arg0: str) -> None: ...
    @property
    def origins(self) -> list[str]: ...
    @origins.setter
    def origins(self, arg0: list[str]) -> None: ...
    def __init__(self: FileInfo) -> None:
        """
        Creates an uninitialized FileInfo.
        """
        ...

class FileTreeEntry:
    """
    Represent an entry in a file tree, either a file or a directory. This class
    inherited by IFileTree so that operations on entry are the same for a file or
    a directory.

    This class provides convenience methods to query information on the file, like its
    name or the its last modification time. It also provides a convenience astree() method
    that can be used to retrieve the tree corresponding to its entry in case the entry
    represent a directory.
    """

    class FileTypes(Enum):
        """
        Enumeration of the different file type or combinations.
        """

        FILE = ...
        DIRECTORY = ...
        FILE_OR_DIRECTORY = ...

        @property
        def value(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __and__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> FileTreeEntry.FileTypes: ...
        def __eq__(self: FileTreeEntry.FileTypes, other: object) -> bool: ...
        def __ge__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> bool: ...
        def __gt__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> bool: ...
        def __int__(self: FileTreeEntry.FileTypes) -> int: ...
        def __invert__(self: FileTreeEntry.FileTypes) -> FileTreeEntry.FileTypes: ...
        def __le__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> bool: ...
        def __lt__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> bool: ...
        def __ne__(self: FileTreeEntry.FileTypes, other: object) -> bool: ...
        def __or__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> FileTreeEntry.FileTypes: ...
        def __rand__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> FileTreeEntry.FileTypes: ...
        def __ror__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> FileTreeEntry.FileTypes: ...
        def __rxor__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> FileTreeEntry.FileTypes: ...
        def __str__(self: FileTreeEntry.FileTypes) -> str: ...
        def __xor__(
            self: FileTreeEntry.FileTypes, other: FileTreeEntry.FileTypes
        ) -> FileTreeEntry.FileTypes: ...

    DIRECTORY: FileTypes = ...
    FILE: FileTypes = ...
    FILE_OR_DIRECTORY: FileTypes = ...

    def __eq__(self: FileTreeEntry, other: object) -> bool: ...
    def detach(self: FileTreeEntry) -> bool:
        """
        Detach this entry from its parent tree.

        Returns:
            True if the entry was removed correctly, False otherwise.
        """
        ...
    def fileType(self: FileTreeEntry) -> FileTreeEntry.FileTypes:
        """
        Returns:
            The filetype of this entry.
        """
        ...
    @overload
    def hasSuffix(self: FileTreeEntry, suffixes: Sequence[str]) -> bool:
        """
        Check if this entry has one of the given suffixes.

        Args:
            suffixes: Suffixes to check.

        Returns:
            True if this entry is a file and has one of the given suffix.
        """
        ...
    @overload
    def hasSuffix(self: FileTreeEntry, suffix: str) -> bool:
        """
        Check if this entry has the given suffix.

        Args:
            suffix: Suffix to check.

        Returns:
            True if this entry is a file and has the given suffix.
        """
        ...
    def isDir(self: FileTreeEntry) -> bool:
        """
        Returns:
            True if this entry is a directory, False otherwise.
        """
        ...
    def isFile(self: FileTreeEntry) -> bool:
        """
        Returns:
            True if this entry is a file, False otherwise.
        """
        ...
    def moveTo(self: FileTreeEntry, tree: IFileTree) -> bool:
        """
        Move this entry to the given tree.

        Args:
            tree: The tree to move this entry to.

        Returns:
            True if the entry was moved correctly, False otherwise.
        """
        ...
    def name(self: FileTreeEntry) -> str:
        """
        Returns:
            The name of this entry.
        """
        ...
    def parent(self: FileTreeEntry) -> IFileTree | None:
        """
        Returns:
            The parent tree containing this entry, or a `None` if this entry is the root
        or the parent tree is unreachable.
        """
        ...
    def path(self: FileTreeEntry, sep: str = "\\") -> str:
        """
        Retrieve the path from this entry up to the root of the tree.

        This method propagate up the tree so is not constant complexity as
        the full path is never stored.

        Args:
            sep: The type of separator to use to create the path.

        Returns:
            The path from this entry to the root, including the name of this entry.
        """
        ...
    def pathFrom(self: FileTreeEntry, tree: IFileTree, sep: str = "\\") -> str:
        """
        Retrieve the path from the given tree to this entry.

        Args:
            tree: The tree to reach, must be a parent of this entry.
            sep: The type of separator to use to create the path.

        Returns:
            The path from the given tree to this entry, including the name of this entry, or
        an empty string if the given tree is not a parent of this entry.
        """
        ...
    def suffix(self: FileTreeEntry) -> str:
        """
        Retrieve the "last" extension of this entry.

        The "last" extension is everything after the last dot in the file name.

        Returns:
            The last extension of this entry, or an empty string if the file has no extension
        or is directory.
        """
        ...

class GameFeature(abc.ABC):
    """
    Base class for all game features, cannot be inherited, used only for typing
    purpose in Python.
    """

    ...

class GuessedString:
    """
    Represents a string that may be set from different places. Each time the value is
    changed a "quality" is specified to say how probable it is the value is the best choice.
    Only the best choice should be used in the end but alternatives can be queried. This
    class also allows a filter to be set. If a "guess" doesn't pass the filter, it is ignored.
    """

    @overload
    def __init__(self: GuessedString) -> None:
        """
        Creates a GuessedString with no associated value.
        """
        ...
    @overload
    def __init__(
        self: GuessedString, value: str, quality: GuessQuality = GuessQuality.USER
    ) -> None:
        """
        Creates a GuessedString with the given value and quality.

        Args:
            value: Initial value of the GuessedString.
            quality: Quality of the initial value.
        """
        ...
    def __str__(self: GuessedString) -> str: ...
    @overload
    def reset(self: GuessedString) -> GuessedString:
        """
        Reset this GuessedString to an invalid state.

        Returns:
            This GuessedString object.
        """
        ...
    @overload
    def reset(self: GuessedString, value: str, quality: GuessQuality) -> GuessedString:
        """
        Reset this GuessedString object with the given value and quality, only
        if the given quality is better than the current one.

        Args:
            value: New value for this GuessedString.
            quality: Quality of the new value.

        Returns:
            This GuessedString object.
        """
        ...
    @overload
    def reset(self: GuessedString, other: GuessedString) -> GuessedString:
        """
        Reset this GuessedString object by copying the given one, only
        if the given one has better quality.

        Args:
            other: The GuessedString to copy.

        Returns:
            This GuessedString object.
        """
        ...
    def setFilter(
        self: GuessedString, filter: Callable[[str], Union[str, bool]]
    ) -> None:
        """
        Set the filter for this GuessedString.

        The filter is applied on every `update()` and can reject the new value
        altogether or modify it (by returning a new value).

        Args:
            filter: The new filter.
        """
        ...
    @overload
    def update(self: GuessedString, value: str) -> GuessedString:
        """
        Update this GuessedString by adding the given value to the list of variants
        and setting the actual value without changing the current quality of this
        GuessedString.

        The GuessedString is only updated if the given value passes the filter.

        Args:
            value: The new value for this string.

        Returns:
            This GuessedString object.
        """
        ...
    @overload
    def update(self: GuessedString, value: str, quality: GuessQuality) -> GuessedString:
        """
        Update this GuessedString by adding a new variants with the given quality.

        If the specified quality is better than the current one, the actual value of
        the GuessedString is also updated.

        The GuessedString is only updated if the given value passes the filter.

        Args:
            value: The new variant to add.
            quality: The quality of the variant.

        Returns:
            This GuessedString object.
        """
        ...
    def variants(self: GuessedString) -> set[str]:
        """
        Returns:
            The list of variants for this GuessedString.
        """
        ...

class IDownloadManager:
    def downloadPath(self: IDownloadManager, id: int) -> str:
        """
        Retrieve the (absolute) path of the specified download.

        Args:
            id: ID of the download.

        Returns:
            The absolute path to the file corresponding to the given download. This file
        may not exist yet if the download is incomplete.
        """
        ...
    def onDownloadComplete(
        self: IDownloadManager, callback: Callable[[int], None]
    ) -> bool:
        """
        Installs a handler to be called when a download completes.

        Args:
            callback: The function to be called when a download complete. The parameter is the download ID.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onDownloadFailed(
        self: IDownloadManager, callback: Callable[[int], None]
    ) -> bool:
        """
        Installs a handler to be called when a download fails.

        Args:
            callback: The function to be called when a download fails. The parameter is the download ID.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onDownloadPaused(
        self: IDownloadManager, callback: Callable[[int], None]
    ) -> bool:
        """
        Installs a handler to be called when a download is paused.

        Args:
            callback: The function to be called when a download is paused. The parameter is the download ID.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onDownloadRemoved(
        self: IDownloadManager, callback: Callable[[int], None]
    ) -> bool:
        """
        Installs a handler to be called when a download is removed.

        Args:
            callback: The function to be called when a download is removed. The parameter is the download ID.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def startDownloadNexusFile(
        self: IDownloadManager, mod_id: int, file_id: int
    ) -> int:
        """
        Download a file from www.nexusmods.com/<game>. <game> is always the game
        currently being managed.

        Args:
            mod_id: ID of the mod to download the file from.
            file_id: ID of the file to download.

        Returns:
            An ID identifying the download.
        """
        ...
    def startDownloadURLs(self: IDownloadManager, urls: Sequence[str]) -> int:
        """
        Download a file by url.

        The list can contain alternative URLs to allow the download manager to switch
        in case of download problems

        Args:
            urls: List of urls to download from.

        Returns:
            An ID identifying the download.
        """
        ...

class IExtension:
    """
    Class representing a ModOrganizer2 extension.
    """

    ...

class IExtensionList:
    """
    Interface to access extensions.
    """

    def __getitem__(self: IExtensionList, index: Union[int, str]) -> IExtension:
        """
        Access the given item by identifier or index.

        Args:
            index: Index or identifier for the extension.

        Returns:
            The extension with the given identifier or at the given index.

        Raises:
            IndexError: if the requested extension does not exist.
        """
        ...
    def __len__(self: IExtensionList) -> int:
        """
        Retrieve the number of installed extensions.

        Returns:
            The number of installed extensions.
        """
        ...
    def enabled(self: IExtensionList, identifier: str) -> bool:
        """
        Check if the given extension is enabled.

        Args:
            identifier: Identifier of the extension to check.

        Returns:
            True if the extension is enabled, False otherwise.
        """
        ...
    def installed(self: IExtensionList, identifier: str) -> bool:
        """
        Check if the given extension is installed.

        Args:
            identifier: Identifier of the extension to check.

        Returns:
            True if the extension is installed, False otherwise.
        """
        ...

class IGameFeatures:
    """
    Interface for the game features, accessible through IOrganizer.gameFeatures().
    """

    def gameFeature(
        self: IGameFeatures, feature_type: Type[GameFeatureType]
    ) -> GameFeatureType:
        """
        Retrieve the given game feature, if one exists.

        Args:
            feature_type: The class of feature to retrieve.

        Returns:
            The game feature corresponding to the given type, or `None` if the feature is
        not available.
        """
        ...
    @overload
    def registerFeature(
        self: IGameFeatures,
        games: Sequence[str],
        feature: GameFeature,
        priority: int,
        replace: bool = False,
    ) -> bool:
        """
        Register game feature for the specified game.

        This method register a game feature to combine or replace with other features
        of the same kind. Some features are merged (e.g., ModDataContent,
        ModDataChecker), while other override previous features (e.g., SaveGameInfo).

        For features that can be combined, the priority argument indicates the order of
        priority (e.g., the order of the checks for ModDataChecker). For other features,
        the feature with the highest priority will be used. The features provided by the
        game plugin itself always have lowest priority.

        The feature is associated to the plugin that registers it, if the plugin is
        disabled, the feature will not be available.

        This function will return True if the feature was registered, even if the
        feature is not used du to its low priority.

        Args:
            games: Names of the game to enable the feature for.
            feature: Game feature to register.
            priority: Priority of the game feature. If the plugin registering the feature
                is a game plugin, this parameter is ignored.
            replace: If True, remove features of the same kind registered by the current plugin,
                otherwise add the feature alongside existing ones.

        Returns:
            True if the game feature was properly registered, False otherwise.
        """
        ...
    @overload
    def registerFeature(
        self: IGameFeatures,
        game: IPluginGame,
        feature: GameFeature,
        priority: int,
        replace: bool = False,
    ) -> bool:
        """
        Register game feature for the specified game.

        This method register a game feature to combine or replace with other features
        of the same kind. Some features are merged (e.g., ModDataContent,
        ModDataChecker), while other override previous features (e.g., SaveGameInfo).

        For features that can be combined, the priority argument indicates the order of
        priority (e.g., the order of the checks for ModDataChecker). For other features,
        the feature with the highest priority will be used. The features provided by the
        game plugin itself always have lowest priority.

        The feature is associated to the plugin that registers it, if the plugin is
        disabled, the feature will not be available.

        This function will return True if the feature was registered, even if the
        feature is not used du to its low priority.

        Args:
            game: Game to enable the feature for.
            feature: Game feature to register.
            priority: Priority of the game feature. If the plugin registering the feature
                is a game plugin, this parameter is ignored.
            replace: If True, remove features of the same kind registered by the current plugin,
                otherwise add the feature alongside existing ones.

        Returns:
            True if the game feature was properly registered, False otherwise.
        """
        ...
    @overload
    def registerFeature(
        self: IGameFeatures, feature: GameFeature, priority: int, replace: bool = False
    ) -> bool:
        """
        Register game feature for all games.

        This method register a game feature to combine or replace with other features
        of the same kind. Some features are merged (e.g., ModDataContent,
        ModDataChecker), while other override previous features (e.g., SaveGameInfo).

        For features that can be combined, the priority argument indicates the order of
        priority (e.g., the order of the checks for ModDataChecker). For other features,
        the feature with the highest priority will be used. The features provided by the
        game plugin itself always have lowest priority.

        The feature is associated to the plugin that registers it, if the plugin is
        disabled, the feature will not be available.

        This function will return True if the feature was registered, even if the
        feature is not used du to its low priority.

        Args:
            feature: Game feature to register.
            priority: Priority of the game feature. If the plugin registering the feature
                is a game plugin, this parameter is ignored.
            replace: If True, remove features of the same kind registered by the current plugin,
                otherwise add the feature alongside existing ones.

        Returns:
            True if the game feature was properly registered, False otherwise.
        """
        ...
    def unregisterFeature(self: IGameFeatures, feature: GameFeature) -> bool:
        """
        Unregister the given game feature.

        This function is safe to use even if the given feature was never registered.

        Args:
            feature: Feature to unregister.

        Returns:
            True if the feature was successfully unregistered, False otherwise.
        """
        ...
    def unregisterFeatures(
        self: IGameFeatures, feature_type: Type[GameFeatureType]
    ) -> int:
        """
        Unregister all features of the given type registered by the calling plugin.

        This function is safe to use even if the plugin has no feature of the given type
        register.

        Args:
            feature_type: The class of feature to unregister.

        Returns:
            The number of unregistered features.
        """
        ...

class IInstallationManager:
    def createFile(self: IInstallationManager, entry: FileTreeEntry) -> str:
        """
        Create a new file on the disk corresponding to the given entry.

        This method can be used by installer that needs to create files that are not in the original
        archive. At the end of the installation, if there are entries in the final tree that were used
        to create files, the corresponding files will be moved to the mod folder.

        Temporary files corresponding to created files are automatically cleaned up at the end of
        the installation.

        Args:
            entry: The entry for which a temporary file should be created.

        Returns:
            The path to the created file, or an empty string if the file could not be created.
        """
        ...
    def extractFile(
        self: IInstallationManager, entry: FileTreeEntry, silent: bool = False
    ) -> str:
        """
        Extract the specified file from the currently opened archive to a temporary
        location.

        This method cannot be used to extract directory.

        The call will fail with an exception if no archive is open (plugins deriving from
        IPluginInstallerSimple can rely on that, custom installers should not). The temporary
        file is automatically cleaned up after the installation. This call can be very slow
        if the archive is large and "solid".

        Args:
            entry: Entry corresponding to the file to extract.
            silent: If true, the dialog showing extraction progress will not be shown.

        Returns:
            The absolute path to the temporary file, or an empty string if the file was not extracted.
        """
        ...
    def extractFiles(
        self: IInstallationManager, entries: list[FileTreeEntry], silent: bool = False
    ) -> Sequence[str]:
        """
        Extract the specified files from the currently opened archive to a temporary
        location.

        This method cannot be used to extract directories.

        The call will fail with an exception if no archive is open (plugins deriving from
        IPluginInstallerSimple can rely on that, custom installers should not). The temporary
        files are automatically cleaned up after the installation. This call can be very slow
        if the archive is large and "solid".

        Args:
            entries: Entries corresponding to the files to extract.
            silent: If true, the dialog showing extraction progress will not be shown.

        Returns:
            A list containing absolute paths to the temporary files.
        """
        ...
    def getSupportedExtensions(self: IInstallationManager) -> Sequence[str]:
        """
        Returns:
            The extensions of archives supported by this installation manager.
        """
        ...
    def installArchive(
        self: IInstallationManager,
        mod_name: GuessedString,
        archive: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo],
        mod_id: int = 0,
    ) -> tuple[InstallResult, str, int]:
        """
        Install the given archive.

        Args:
            mod_name: Suggested name of the mod.
            archive: Path to the archive to install.
            mod_id: ID of the mod, if available.

        Returns:
            The result of the installation.
        """
        ...

class IModInterface:
    def absolutePath(self: IModInterface) -> str:
        """
        Returns:
            Absolute path to the mod to be used in file system operations.
        """
        ...
    def addCategory(self: IModInterface, name: str) -> None:
        """
        Assign a category to the mod. If the named category does not exist it is created.

        Args:
            name: Name of the new category to assign.
        """
        ...
    def addNexusCategory(self: IModInterface, category_id: int) -> None:
        """
        Set the category id from a nexus category id. Conversion to MO ID happens internally.

        If a mapping is not possible, the category is set to the default value.

        Args:
            category_id: The Nexus category ID.
        """
        ...
    def categories(self: IModInterface) -> Sequence[str]:
        """
        Returns:
            The list of categories this mod belongs to.
        """
        ...
    def clearPluginSettings(
        self: IModInterface, plugin_name: str
    ) -> dict[str, MoVariant]:
        """
        Remove all the settings of the specified plugin this mod.

        Args:
            plugin_name: Name of the plugin for which settings should be removed. This should always be `IPlugin.name()`
                unless you have a really good reason to access settings of another plugin.

        Returns:
            The old settings from the given plugin, as returned by `pluginSettings()`.
        """
        ...
    def color(self: IModInterface) -> PyQt6.QtGui.QColor:
        """
        Returns:
            The color of the 'Notes' column chosen by the user.
        """
        ...
    def comments(self: IModInterface) -> str:
        """
        Returns:
            The comments for this mod, if any.
        """
        ...
    def converted(self: IModInterface) -> bool:
        """
        Check if the mod was marked as converted by the user.

        When a mod is for a different game, a flag is shown to users to warn them, but
        they can mark mods as converted to remove this flag.

        Returns:
            True if this mod was marked as converted by the user.
        """
        ...
    def endorsedState(self: IModInterface) -> EndorsedState:
        """
        Returns:
            The endorsement state of this mod.
        """
        ...
    def fileTree(self: IModInterface) -> IFileTree:
        """
        Retrieve a file tree corresponding to the underlying disk content of this mod.

        The file tree should not be cached by plugins since it is already and updated when
        required.

        Returns:
            A file tree representing the content of this mod.
        """
        ...
    def gameName(self: IModInterface) -> str:
        """
        Retrieve the short name of the game associated with this mod. This may differ
        from the current game plugin (e.g. you can install a Skyrim LE game in a SSE
        installation).

        Returns:
            The name of the game associated with this mod.
        """
        ...
    def ignoredVersion(self: IModInterface) -> VersionInfo:
        """
        Returns:
            The ignored version of this mod (for update), or an invalid version if the user
        did not ignore version for this mod.
        """
        ...
    def installationFile(self: IModInterface) -> str:
        """
        Returns:
            The absolute path to the file that was used to install this mod.
        """
        ...
    def isBackup(self: IModInterface) -> bool:
        """
        Returns:
            True if this mod represents a backup.
        """
        ...
    def isForeign(self: IModInterface) -> bool:
        """
        Returns:
            True if this mod represents a foreign mod, not managed by MO2.
        """
        ...
    def isOverwrite(self: IModInterface) -> bool:
        """
        Returns:
            True if this mod represents the overwrite mod.
        """
        ...
    def isSeparator(self: IModInterface) -> bool:
        """
        Returns:
            True if this mod represents a separator.
        """
        ...
    def name(self: IModInterface) -> str:
        """
        Returns:
            The name of this mod.
        """
        ...
    def newestVersion(self: IModInterface) -> VersionInfo:
        """
        Returns:
            The newest version of this mod (as known by MO2). If this matches version(),
        then the mod is up-to-date.
        """
        ...
    def nexusId(self: IModInterface) -> int:
        """
        Returns:
            The Nexus ID of this mod.
        """
        ...
    def notes(self: IModInterface) -> str:
        """
        Returns:
            The notes for this mod, if any.
        """
        ...
    def pluginSetting(
        self: IModInterface, plugin_name: str, key: str, default: MoVariant = None
    ) -> MoVariant:
        """
        Retrieve the specified setting in this mod for a plugin.

        Args:
            plugin_name: Name of the plugin for which to retrieve a setting. This should always be `IPlugin.name()`
                unless you have a really good reason to access settings of another plugin.
            key: Identifier of the setting.
            default: The default value to return if the setting does not exist.

        Returns:
            The setting, if found, or the default value.
        """
        ...
    def pluginSettings(self: IModInterface, plugin_name: str) -> dict[str, MoVariant]:
        """
        Retrieve the settings in this mod for a plugin.

        Args:
            plugin_name: Name of the plugin for which to retrieve settings. This should always be `IPlugin.name()`
                unless you have a really good reason to access settings of another plugin.

        Returns:
            A map from setting key to value. The map is empty if there are not settings for this mod.
        """
        ...
    def primaryCategory(self: IModInterface) -> int:
        """
        Returns:
            The ID of the primary category of this mod.
        """
        ...
    def removeCategory(self: IModInterface, name: str) -> bool:
        """
        Unassign a category from this mod.

        Args:
            name: Name of the category to remove.

        Returns:
            True if the category was removed, False otherwise (e.g. if no such category
        was assigned).
        """
        ...
    def repository(self: IModInterface) -> str:
        """
        Returns:
            The name of the repository from which this mod was installed.
        """
        ...
    def setGameName(self: IModInterface, name: str) -> None:
        """
        Set the source game of this mod.

        Args:
            name: The new source game short name of this mod.
        """
        ...
    def setIsEndorsed(self: IModInterface, endorsed: bool) -> None:
        """
        Set endorsement state of the mod.

        Args:
            endorsed: New endorsement state of this mod.
        """
        ...
    def setNewestVersion(self: IModInterface, version: VersionInfo) -> None:
        """
        Set the latest known version of this mod.

        Args:
            version: The latest known version of this mod.
        """
        ...
    def setNexusID(self: IModInterface, nexus_id: int) -> None:
        """
        Set the Nexus ID of this mod.

        Args:
            nexus_id: Thew new Nexus ID of this mod.
        """
        ...
    def setPluginSetting(
        self: IModInterface, plugin_name: str, key: str, value: MoVariant
    ) -> bool:
        """
        Set the specified setting in this mod for a plugin.

        Args:
            plugin_name: Name of the plugin for which to retrieve a setting. This should always be `IPlugin.name()`
                unless you have a really good reason to access settings of another plugin.
            key: Identifier of the setting.
            value: New value for the setting to set.

        Returns:
            True if the setting was set correctly, False otherwise.
        """
        ...
    def setUrl(self: IModInterface, url: str) -> None:
        """
        Set the URL of this mod.

        Args:
            url: The URL of this mod.
        """
        ...
    def setVersion(self: IModInterface, version: VersionInfo) -> None:
        """
        Set the version of this mod.

        Args:
            version: The new version of this mod.
        """
        ...
    def trackedState(self: IModInterface) -> TrackedState:
        """
        Returns:
            The tracked state of this mod.
        """
        ...
    def url(self: IModInterface) -> str:
        """
        Returns:
            The URL of this mod, or an empty QString() if no URL is associated
        with this mod.
        """
        ...
    def validated(self: IModInterface) -> bool:
        """
        Check if the mod was marked as validated by the user.

        MO2 uses ModDataChecker to check the content of mods, but sometimes these fail, in
        which case mods are incorrectly marked as 'not containing valid games data'. Users can
        choose to mark these mods as valid to hide the warning / flag.

        Returns:
            True if th is mod was marked as containing valid game data.
        """
        ...
    def version(self: IModInterface) -> VersionInfo:
        """
        Returns:
            The current version of this mod.
        """
        ...

class IModList:
    """
    Interface to the mod-list.

    All api functions in this interface work need the internal name of a mod to find a
    mod. For regular mods (mods the user installed) the display name (as shown to the user)
    and internal name are identical. For other mods (non-MO mods) there is currently no way
    to translate from display name to internal name because the display name might not me un-ambiguous.
    """

    def allMods(self: IModList) -> Sequence[str]:
        """
        Returns:
            A list containing the internal names of all installed mods.
        """
        ...
    def allModsByProfilePriority(
        self: IModList, profile: IProfile | None = None
    ) -> Sequence[str]:
        """
        Returns:
            The list of mod (names), sorted according to the current profile priorities.
        """
        ...
    def displayName(self: IModList, name: str) -> str:
        """
        Retrieve the display name of a mod from its internal name.

        If you received an internal name from the API (e.g. `IPluginList.origin`) then you should use
        that name to identify the mod in all other api calls but use this function to retrieve the name
        to show to the user.

        Args:
            name: Internal name of the mod.

        Returns:
            The display name of the given mod.
        """
        ...
    def getMod(self: IModList, name: str) -> IModInterface:
        """
        Retrieve an interface to a mod using its name.

        Args:
            name: Name of the mod to retrieve.

        Returns:
            An interface to the given mod, or `None` if there is no mod with this name.
        """
        ...
    def onModInstalled(
        self: IModList, callback: Callable[[IModInterface], None]
    ) -> bool:
        """
        Install a new handler to be called when a new mod is installed.

        Args:
            callback: The function to call when a mod is installed. The parameter of the function is the name of the
                newly installed mod.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onModMoved(self: IModList, callback: Callable[[str, int, int], None]) -> bool:
        """
        Install a handler to be called when a mod is moved.

        Args:
            callback: The function to call when a mod is moved. The first argument is the internal name of the
                mod, the second argument the old priority and the third argument the new priority.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onModRemoved(self: IModList, callback: Callable[[str], None]) -> bool:
        """
        Install a new handler to be called when a mod is removed.

        Args:
            callback: The function to call when a mod is removed. The parameter of the function is the name of the
                removed mod.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onModStateChanged(
        self: IModList, callback: Callable[[dict[str, ModState]], None]
    ) -> bool:
        """
        Install a handler to be called when mod states change (enabled/disabled, endorsed, ...).

        Args:
            callback: The function to call when the states of mod change. The argument is a map containing the
                mods whose states have changed. Keys are internal mod names and values are mod states.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def priority(self: IModList, name: str) -> int:
        """
        Retrieve the priority of a mod.

        Args:
            name: Internal name of the mod.

        Returns:
            The priority of the given mod.
        """
        ...
    def removeMod(self: IModList, mod: IModInterface) -> bool:
        """
        Remove a mod (from disc and from the UI).

        Args:
            mod: The mod to remove.

        Returns:
            True if the mod was removed, False otherwise.
        """
        ...
    def renameMod(self: IModList, mod: IModInterface, name: str) -> IModInterface:
        """
        Rename the given mod.

        This method usually invalidates the given mod so you should use the returned value
        after calling it instead of the passed value.

        Args:
            mod: The mod to rename.
            name: The new name of the mod.

        Returns:
            A valid reference to the given mod after renaming it.
        """
        ...
    @overload
    def setActive(self: IModList, names: Sequence[str], active: bool) -> int:
        """
        Enable or disable a list of mods.

        Calling this will cause MO to re-evaluate its virtual file system so this is
        a fairly expensive call.

        Args:
            names: Internal names of the mod to enable or disable.
            active: True to enable the mods, False to disable them.

        Returns:
            True on success, False otherwise.
        """
        ...
    @overload
    def setActive(self: IModList, name: str, active: bool) -> bool:
        """
        Enable or disable a mod.

        Calling this will cause MO to re-evaluate its virtual file system so this is
        a fairly expensive call.

        Args:
            name: Internal name of the mod to enable or disable.
            active: True to enable the mod, False to disable it.

        Returns:
            True on success, False otherwise.
        """
        ...
    def setPriority(self: IModList, name: str, priority: int) -> bool:
        """
        Change the priority of a mod.

        `priority` is the new priority after the move. Keep in mind that the mod disappears from its
        old location and all mods with higher priority than the moved mod decrease in priority by one.

        Args:
            name: Internal name of the mod.
            priority: The new priority of the mod.

        Returns:
            True if the priority was changed, False otherwise (if the name or priority were invalid).
        """
        ...
    def state(self: IModList, name: str) -> ModState:
        """
        Retrieve the state of a mod.

        Args:
            name: Internal name of the mod.

        Returns:
            The state of the given mod.
        """
        ...

class IOrganizer:
    """
    Interface to class that provides information about the running session
    of Mod Organizer to be used by plugins.
    """

    def basePath(self: IOrganizer) -> str:
        """
        Returns:
            The absolute path to the base directory of Mod Organizer.
        """
        ...
    def createMod(self: IOrganizer, name: GuessedString) -> IModInterface:
        """
        Create a new mod with the specified name.

        If a mod with the same name already exists, the user will be queried. If the user chooses
        to merge or replace, the call will succeed, otherwise the call will fail.

        Args:
            name: Name of the mod to create.

        Returns:
            An interface to the newly created mod that can be used to modify it, or `None` if the mod
        could not be created.
        """
        ...
    def createNexusBridge(self: IOrganizer) -> IModRepositoryBridge:
        """
        Create a new Nexus interface.

        Returns:
            The newly created Nexus interface.
        """
        ...
    def downloadManager(self: IOrganizer) -> IDownloadManager:
        """
        Returns:
            The interface to the download manager.
        """
        ...
    def downloadsPath(self: IOrganizer) -> str:
        """
        Returns:
            The absolute path to the download directory.
        """
        ...
    def extensionList(self: IOrganizer) -> IExtensionList:
        """
        Returns:
            The interface to the extension list.
        """
        ...
    def findFileInfos(
        self: IOrganizer,
        path: Union[str, os.PathLike[str], PyQt6.QtCore.QDir],
        filter: Callable[[FileInfo], bool],
    ) -> Sequence[FileInfo]:
        """
        Find files in the virtual directory matching the specified filter.

        Args:
            path: The path to search in (relative to the 'data' folder).
            filter: The function to use to filter files. Should return True for the files to keep.

        Returns:
            The list of `QFileInfo` corresponding to the matching files.
        """
        ...
    @overload
    def findFiles(
        self: IOrganizer,
        path: Union[str, os.PathLike[str], PyQt6.QtCore.QDir],
        filter: Callable[[str], bool],
    ) -> Sequence[str]:
        """
        Find files in the given folder that matches the given filter.

        Args:
            path: The path to search in (relative to the 'data' folder).
            filter: The function to use to filter files. Should return True for the files to keep.

        Returns:
            The list of matching files.
        """
        ...
    @overload
    def findFiles(
        self: IOrganizer,
        path: Union[str, os.PathLike[str], PyQt6.QtCore.QDir],
        patterns: Sequence[str],
    ) -> Sequence[str]:
        """
        Find files in the given folder that matches one of the given glob patterns.

        Args:
            path: The path to search in (relative to the 'data' folder).
            patterns: List of glob patterns to match against.

        Returns:
            The list of matching files.
        """
        ...
    @overload
    def findFiles(
        self: IOrganizer,
        path: Union[str, os.PathLike[str], PyQt6.QtCore.QDir],
        pattern: str,
    ) -> Sequence[str]:
        """
        Find files in the given folder that matches the given glob pattern.

        Args:
            path: The path to search in (relative to the 'data' folder).
            pattern: The glob pattern to use to filter files.

        Returns:
            The list of matching files.
        """
        ...
    def gameFeatures(self: IOrganizer) -> IGameFeatures:
        """
        Returns:
            The interface to the game features.
        """
        ...
    def getFileOrigins(self: IOrganizer, filename: str) -> Sequence[str]:
        """
        Retrieve the file origins for the specified file.

        The origins are listed with their internal name. The internal name of a mod can differ
        from the display name for disambiguation.

        Args:
            filename: Path to the file to retrieve origins for (relative to the 'data' folder).

        Returns:
            The list of origins that contain the specified file, sorted by their priority.
        """
        ...
    def getGame(self: IOrganizer, name: str) -> IPluginGame:
        """
        Retrieve the game plugin matching the given name.

        Args:
            name: Name of the game (short name).

        Returns:
            The plugin for the given game, or `None` if none was found.
        """
        ...
    @staticmethod
    def getPluginDataPath() -> str:
        """
        Returns:
            The directory for plugin data, typically plugins/data.
        """
        ...
    def installMod(
        self: IOrganizer,
        filename: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo],
        name_suggestion: str = "",
    ) -> IModInterface:
        """
        Install a mod archive at the specified location.

        Args:
            filename: Absolute filepath to the archive to install.
            name_suggestion: Suggested name for this mod. This can still be changed by the user.

        Returns:
            An interface to the new installed mod, or `None` if no installation took place (canceled or failure).
        """
        ...
    @overload
    def isPluginEnabled(self: IOrganizer, plugin: IPlugin) -> bool:
        """
        Check if a plugin is enabled.

        Args:
            plugin: The plugin to check.

        Returns:
            True if the plugin is enabled, False otherwise.
        """
        ...
    @overload
    def isPluginEnabled(self: IOrganizer, plugin: str) -> bool:
        """
        Check if a plugin is enabled.

        Args:
            plugin: The name of the plugin to check.

        Returns:
            True if the plugin is enabled, False otherwise.
        """
        ...
    def listDirectories(self: IOrganizer, directory: str) -> Sequence[str]:
        """
        Retrieve the list of (virtual) subdirectories in the given path.

        Args:
            directory: Path to the directory to list (relative to the 'data' folder).

        Returns:
            The list of directories in the given directory.
        """
        ...
    def managedGame(self: IOrganizer) -> IPluginGame:
        """
        Returns:
            The plugin corresponding to the current game.
        """
        ...
    def modDataChanged(self: IOrganizer, mod: IModInterface) -> None:
        """
        Notify the organizer that the given mod has changed.

        Args:
            mod: The mod that has changed.
        """
        ...
    def modList(self: IOrganizer) -> IModList:
        """
        Returns:
            The interface to the mod list.
        """
        ...
    def modsPath(self: IOrganizer) -> str:
        """
        Returns:
            The (absolute) path to the mods directory.
        """
        ...
    @overload
    def onAboutToRun(
        self: IOrganizer, callback: Callable[[str, PyQt6.QtCore.QDir, str], bool]
    ) -> bool:
        """
        Install a new handler to be called when an application is about to run.

        Multiple handlers can be installed. If any of the handler returns `False`, the
        application will not run.

        Args:
            callback: The function to call when an application is about to run. The function
                receives the absolute path to the application to run, the working directory
                for the run and a string containing the arguments passed to the executable.
                The function can return False to prevent the application from running.

        Returns:
            True if the handler was installed properly (there are currently no
        reasons for this to fail).
        """
        ...
    @overload
    def onAboutToRun(self: IOrganizer, callback: Callable[[str], bool]) -> bool:
        """
        Install a new handler to be called when an application is about to run.

        Multiple handlers can be installed. If any of the handler returns `False`, the
        application will not run.

        Args:
            callback: The function to call when an application is about to run. The parameter
                is the absolute path to the application to run. The function can return False
                to prevent the application from running.

        Returns:
            True if the handler was installed properly (there are currently no reasons for
        this to fail).
        """
        ...
    def onFinishedRun(self: IOrganizer, callback: Callable[[str, int], None]) -> bool:
        """
        Install a new handler to be called when an application has finished running.

        Args:
            callback: The function to call when an application has finished running. The first parameter is the absolute
                path to the application, and the second parameter is the exit code of the application.

        Returns:
            True if the handler was installed properly (there are currently no reasons for
        this to fail).
        """
        ...
    def onNextRefresh(
        self: IOrganizer,
        callback: Callable[[], None],
        immediate_if_possible: bool = True,
    ) -> bool:
        """
        Install a new handler to be called on the next refresh or immediately.

        Args:
            callback: Function to call on the next refresh (or immediately).
            immediate_if_possible: If True, immediately run the callback if no refresh is currently running.

        Returns:
            True if the handler was installed properly (there are currently no reasons for
        this to fail).
        """
        ...
    @overload
    def onPluginDisabled(self: IOrganizer, callback: Callable[[IPlugin], None]) -> None:
        """
        Install a new handler to be called when a plugin is disabled.

        Args:
            callback: The function to call when a plugin is disabled. The parameter is the plugin being disabled.
        """
        ...
    @overload
    def onPluginDisabled(
        self: IOrganizer, name: str, callback: Callable[[], None]
    ) -> None:
        """
        Install a new handler to be called when the given plugin is disabled.

        Args:
            name: Name of the plugin to watch.
            callback: The function to call when the plugin is disabled.
        """
        ...
    @overload
    def onPluginEnabled(self: IOrganizer, callback: Callable[[IPlugin], None]) -> None:
        """
        Install a new handler to be called when a plugin is enabled.

        Args:
            callback: The function to call when a plugin is enabled. The parameter is the plugin being enabled.
        """
        ...
    @overload
    def onPluginEnabled(
        self: IOrganizer, name: str, callback: Callable[[], None]
    ) -> None:
        """
        Install a new handler to be called when the given plugin is enabled.

        Args:
            name: Name of the plugin to watch.
            callback: The function to call when the plugin is enabled.
        """
        ...
    def onPluginSettingChanged(
        self: IOrganizer, callback: Callable[[str, str, MoVariant, MoVariant], None]
    ) -> bool:
        """
        Install a new handler to be called when a plugin setting is changed.

        Args:
            callback: The function to call when a plugin setting is changed. The parameters are: The name of the plugin, the
                name of the setting, the old value (or `None` if the setting did not exist before) and the new value
                of the setting (or `None` if the setting has been removed).

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onProfileChanged(
        self: IOrganizer, callback: Callable[[IProfile, IProfile], None]
    ) -> bool:
        """
        Install a new handler to be called when the current profile is changed.

        The function is called when the profile is changed but some operations related to
        the profile might not be finished when this is called (e.g., the virtual file system
        might not be up-to-date).

        Args:
            callback: The function to call when the current profile is changed. The first parameter is the old profile (can
                be `None`, e.g. at startup), and the second parameter is the new profile (cannot be `None`).

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onProfileCreated(
        self: IOrganizer, callback: Callable[[IProfile], None]
    ) -> bool:
        """
        Install a new handler to be called when a new profile is created.

        Args:
            callback: The function to call when a new profile is created. The parameter is the new profile (can be
                a temporary object and should not be stored).

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onProfileRemoved(self: IOrganizer, callback: Callable[[str], None]) -> bool:
        """
        Install a new handler to be called when a profile is remove.

        The callbacks are called after the profile has been removed so the profile is not accessible
        anymore.

        Args:
            callback: The function to call when a profile is remove. The parameter is the name of the profile that was
                removed.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onProfileRenamed(
        self: IOrganizer, callback: Callable[[IProfile, str, str], None]
    ) -> bool:
        """
        Install a new handler to be called when a profile is renamed.

        Args:
            callback: The function to call when a profile is renamed. The first parameter is the profile being renamed,
                the second parameter the previous name and the third parameter the new name.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onUserInterfaceInitialized(
        self: IOrganizer, callback: Callable[[PyQt6.QtWidgets.QMainWindow], None]
    ) -> bool:
        """
        Install a new handler to be called when the UI has been fully initialized.

        Args:
            callback: The function to call when the user-interface has been fully initialized. The parameter is the main
                window of the application (`QMainWindow`).

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def overwritePath(self: IOrganizer) -> str:
        """
        Returns:
            The (absolute) path to the overwrite directory.
        """
        ...
    def persistent(
        self: IOrganizer, plugin_name: str, key: str, default: MoVariant = None
    ) -> MoVariant:
        """
        Retrieve the specified persistent value for a plugin.

        A persistent is an arbitrary value that the plugin can set and retrieve that is persistently stored
        by the main application. There is no UI for the user to change this value but they can directly access
        the storage

        Args:
            plugin_name: Name of the plugin for which to retrieve the value. This should always be `IPlugin.name()` unless you have a
                really good reason to access data of another mod AND if you can verify that plugin is actually installed.
            key: Identifier of the setting.
            default: Default value to return if the key is not set (yet).

        Returns:
            The value corresponding to the given persistent setting, or `def` is the key is not found.
        """
        ...
    def pluginDataPath(self: IOrganizer) -> str:
        """
        Retrieve the path to a directory where plugin data should be stored.

        For python plugins, it is recommended to use a dedicated folder (per plugin) if you need to
        store data (resources, or multiple python files).

        Returns:
            Path to a directory where plugin data should be stored.
        """
        ...
    def pluginList(self: IOrganizer) -> IPluginList:
        """
        Returns:
            The plugin list interface.
        """
        ...
    def pluginSetting(self: IOrganizer, plugin_name: str, key: str) -> MoVariant:
        """
        Retrieve settings of plugins.

        Args:
            plugin_name: Name of the plugin to retrieve the setting for.
            key: Name of the setting to retrieve the value for.

        Returns:
            The value of the setting.
        """
        ...
    def profile(self: IOrganizer) -> IProfile:
        """
        Returns:
            The interface to the current profile.
        """
        ...
    def profileName(self: IOrganizer) -> str:
        """
        Returns:
            The name of the current profile, or an empty string if no profile has been loaded (yet).
        """
        ...
    def profilePath(self: IOrganizer) -> str:
        """
        Returns:
            The absolute path to the active profile or an empty string if no profile has been loaded (yet).
        """
        ...
    def refresh(self: IOrganizer, save_changes: bool = True) -> None:
        """
        Refresh the internal mods file structure from disk. This includes the mod list, the plugin
        list, data tab and other smaller things like problems button (same as pressing F5).

        The main part of the refresh of the mods file structure, mod list and plugin list is done
        asynchronously, so you should not expect them to be up-to-date when this function returns.

        Args:
            save_changes: If True, the relevant profile information is saved first (enabled mods and order of mods).
        """
        ...
    def resolvePath(
        self: IOrganizer, filename: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo]
    ) -> str:
        """
        Resolves a path relative to the virtual data directory to its absolute real path.

        Args:
            filename: Path to resolve.

        Returns:
            The absolute real path, or an empty string if the path was not found.
        """
        ...
    def setPersistent(
        self: IOrganizer,
        plugin_name: str,
        key: str,
        value: MoVariant,
        sync: bool = True,
    ) -> None:
        """
        Set the specified persistent value for a plugin.

        This does not update the in-memory value for this setting, see `setPluginSetting()` for this.

        Args:
            plugin_name: Name of the plugin for which to change a value. This should always be `IPlugin.name()` unless you have a
                really good reason to access data of another mod AND if you can verify that plugin is actually installed.
            key: Identifier of the setting.
            value: New value for the setting.
            sync: If True, the storage is immediately written to disc. This costs performance but is safer against data loss.
        """
        ...
    def setPluginSetting(
        self: IOrganizer, plugin_name: str, key: str, value: MoVariant
    ) -> None:
        """
        Set the specified setting for a plugin.

        This automatically notify handlers register with `onPluginSettingChanged`, so you do not have to do it yourself.

        Args:
            plugin_name: Name of the plugin for which to change a value. This should always be `IPlugin.name()` unless you have a
                really good reason to access data of another mod AND if you can verify that plugin is actually installed.
            key: Identifier of the setting.
            value: New value for the setting.
        """
        ...
    def startApplication(
        self: IOrganizer,
        executable: Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo],
        args: Sequence[str] = [],
        cwd: Union[str, os.PathLike[str], PyQt6.QtCore.QDir] = "",
        profile: str = "",
        forcedCustomOverwrite: str = "",
        ignoreCustomOverwrite: bool = False,
    ) -> int:
        """
        Starts an application with virtual filesystem active.

        Args:
            executable: Name or path of the executable. If this is only a filename, it will only work if it has been configured
                in MO as an executable. If it is a relative path it is expected to be relative to the game directory.
            args: Arguments to pass to the executable. If the list is empty, and `executable` refers to a configured executable,
                the configured arguments are used.
            cwd: The working directory for the executable. If this is empty, the path to the executable is used unless `executable`
                referred to a configured MO executable, in which case the configured cwd is used.
            profile: Profile to use. If this is empty (the default) the current profile is used.
            forcedCustomOverwrite: The mod to set as the custom overwrite, regardless of what the profile has configured.
            ignoreCustomOverwrite: Set to true to ignore the profile's configured custom overwrite.

        Returns:
            The handle to the started application, or 0 if the application failed to start.
        """
        ...
    def version(self: IOrganizer) -> Version:
        """
        Returns:
            The running version of Mod Organizer.
        """
        ...
    def virtualFileTree(self: IOrganizer) -> IFileTree:
        """
        Retrieve a IFileTree object representing the virtual file tree.

        Returns:
            An IFileTree representing the virtual file tree.
        """
        ...
    def waitForApplication(
        self: IOrganizer, handle: int, refresh: bool = True
    ) -> tuple[bool, int]:
        """
        Wait for the application corresponding to the given handle to finish.

        This will always show the lock overlay, regardless of whether the
        user has disabled locking in the setting, so use this with care.
        Note that the lock overlay will always allow the user to unlock, in
        which case this will return False.

        Args:
            handle: Handle of the application to wait for (as returned by `startApplication()`).
            refresh: Whether ModOrganizer should refresh after the process completed or not.

        Returns:
            A tuple `(result, exitcode)`, where `result` is a boolean indicating if the application
        completed successfully, and `exitcode` is the exit code of the application.
        """
        ...

class IPlugin(abc.ABC):
    """
    Base class for all plugins.
    """

    def __init__(self: IPlugin) -> None: ...
    def enabledByDefault(self: IPlugin) -> bool:
        """
        Check whether this plugin should be enabled by default.

        Returns:
            True if this plugin should be enabled by default, False otherwise.
        """
        ...
    @abc.abstractmethod
    def init(self: IPlugin, organizer: IOrganizer) -> bool:
        """
        Initialize this plugin.

        Note that this function may never be called if no `IOrganizer` is available
        at that time, such as when creating the first instance in MO.

        Plugins will probably want to store the organizer pointer. It is guaranteed
        to be valid as long as the plugin is loaded.

        These functions may be called before `init()`:

          - `name()`
          - see `IPluginGame` for more.

        Args:
            organizer: The main organizer interface.

        Returns:
            True if the plugin was initialized correctly, False otherwise.
        """
        ...
    def localizedName(self: IPlugin) -> str:
        """
        Retrieve the localized name of the plugin.

        Unlike `name()`, this method can (and should!) return a localized name for the plugin.
        This method returns name() by default.

        Returns:
            The localized name of the plugin.
        """
        ...
    @abc.abstractmethod
    def name(self: IPlugin) -> str:
        """
        Retrieve the name of the plugin.

        The name of the plugin is used for internal storage purpose so it should not change,
        and it should be static. In particular, you should not use a localized string (`tr()`)
        for the plugin name.

        In the future, we will provide a way to localized plugin names using a distinct method,
        such as `localizedName()`.

        Returns:
            The name of the plugin.
        """
        ...
    def requirements(self: IPlugin) -> list[IPluginRequirement]:
        """
        Retrieve the requirements for this plugin.

        This method is called right after `init()` and the ownership the requirements is

        Returns:
            The list of requirements for this plugin.
        """
        ...
    @abc.abstractmethod
    def settingGroups(self: IPlugin) -> Sequence[SettingGroup]:
        """
        Returns:
            A list of setting groups for this plugin.
        """
        ...
    @abc.abstractmethod
    def settings(self: IPlugin) -> Sequence[Setting]:
        """
        Returns:
            A list of settings for this plugin.
        """
        ...

class IPluginList:
    """
    Primary interface to the list of plugins.
    """

    def hasLightExtension(self: IPluginList, name: str) -> bool:
        """
        Determine if a plugin has a .esl extension.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            True if the given file has a .esl extension, False otherwise or if the
        file does not exist.
        """
        ...
    def hasMasterExtension(self: IPluginList, name: str) -> bool:
        """
        Determine if a plugin has a .esm extension.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            True if the given file has a .esm extension, False otherwise or if the
        file does not exist.
        """
        ...
    def hasNoRecords(self: IPluginList, name: str) -> bool:
        """
        Determine if a plugin has no records.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            True if the given file plugin contains no records, False if it does OR if the
        file does not exist.
        """
        ...
    def isLightFlagged(self: IPluginList, name: str) -> bool:
        """
        Determine if a plugin is flagged as light.

        In gamebryo games, a master file will usually have a .esl file extension but
        technically an esp can be flagged as light.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            True if the given plugin is a light plugin, False otherwise or if the
        file does not exist.
        """
        ...
    def isMasterFlagged(self: IPluginList, name: str) -> bool:
        """
        Determine if a plugin is flagged as mater, i.e., a library, reference by
        other plugins.

        In gamebryo games, a master file will usually have a .esm file extension but
        technically an esp can be flagged as master and an esm might not be.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            True if the given plugin is a master plugin, False otherwise or if the
        file does not exist.
        """
        ...
    def isMediumFlagged(self: IPluginList, name: str) -> bool:
        """
        Determine if a plugin is flagged as medium.

        This plugin flag was added in Starfield and signifies plugin records that
        update existing records

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            True if the given plugin is a medium plugin, False otherwise or if the
        file does not exist.
        """
        ...
    def loadOrder(self: IPluginList, name: str) -> int:
        """
        Retrieve the load order of a plugin.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            The load order of the plugin (the order in which the game loads it). If all plugins are enabled this
        is the same as the priority but disabled plugins will have a load order of -1. This also returns -1
        if the plugin does not exist.
        """
        ...
    def masters(self: IPluginList, name: str) -> Sequence[str]:
        """
        Retrieve the list of masters required for a plugin.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            The list of masters for the plugin (filenames with extension, no path).
        """
        ...
    def onPluginMoved(
        self: IPluginList, callback: Callable[[str, int, int], None]
    ) -> bool:
        """
        Install a new handler to be called when a plugin is moved.

        Args:
            callback: The function to call when a plugin is moved. The first parameter is the plugin name, the
                second the old priority of the plugin and the third one the new priority.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onPluginStateChanged(
        self: IPluginList, callback: Callable[[dict[str, PluginState]], None]
    ) -> bool:
        """
        Install a new handler to be called when plugin states change.

        Args:
            callback: The function to call when a plugin states change. The parameter is a map from plugin names to new
                plugin states for the plugin whose states have changed.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def onRefreshed(self: IPluginList, callback: Callable[[], None]) -> bool:
        """
        Install a new handler to be called when the list of plugins is refreshed.

        Args:
            callback: The function to call when the list of plugins is refreshed.

        Returns:
            True if the handler was installed properly (there are currently no reasons for this to fail).
        """
        ...
    def origin(self: IPluginList, name: str) -> str:
        """
        Retrieve the origin of a plugin. This is either the (internal) name of a mod, `"overwrite"` or `"data"`.

        The internal name of a mod can differ from the display name for disambiguation.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            The name of the origin of the plugin, or an empty string if the plugin does not exist.
        """
        ...
    def pluginNames(self: IPluginList) -> Sequence[str]:
        """
        Returns:
            The list of all plugin names.
        """
        ...
    def priority(self: IPluginList, name: str) -> int:
        """
        Retrieve the priority of a plugin.

        The higher the priority, the more important.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            The priority of the given plugin, or -1 if the plugin does not exist.
        """
        ...
    def setLoadOrder(self: IPluginList, loadorder: Sequence[str]) -> None:
        """
        Set the load order.

        Plugins not included in the list will be placed at highest priority in the order they
        were before.

        Args:
            loadorder: The new load order, specified by the list of plugin names, sorted.
        """
        ...
    def setPriority(self: IPluginList, name: str, priority: int) -> bool:
        """
        Change the priority of a plugin.

        Args:
            name: Filename of the plugin (without path but with file extension).
            priority: New priority of the plugin.

        Returns:
            True on success, False if the priority change was not possible. This is usually because
        one of the parameters is invalid. The function returns true even if the plugin was not moved
        at the specified priority (e.g. when trying to move a non-master plugin before a master one).
        """
        ...
    def setState(self: IPluginList, name: str, state: PluginState) -> None:
        """
        Set the state of a plugin.

        Args:
            name: Filename of the plugin (without path but with file extension).
            state: New state of the plugin (`INACTIVE` or `ACTIVE`).
        """
        ...
    def state(self: IPluginList, name: str) -> PluginState:
        """
        Retrieve the state of a plugin.

        Args:
            name: Filename of the plugin (without path but with file extension).

        Returns:
            The state of the plugin.
        """
        ...

class IPluginRequirement:
    """
    Class representing requirements for plugins.
    """

    class Problem:
        """
        Class representing a problem found by a requirement.
        """

        def __init__(
            self: IPluginRequirement.Problem,
            short_description: str,
            long_description: str = "",
        ) -> None:
            """
            Args:
                short_description: Short description of the problem.
                long_description: Long description of the problem.
            """
            ...
        def longDescription(self: IPluginRequirement.Problem) -> str:
            """
            Returns:
                A long description of the problem.
            """
            ...
        def shortDescription(self: IPluginRequirement.Problem) -> str:
            """
            Returns:
                A short description of the problem.
            """
            ...

    def check(
        self: IPluginRequirement, organizer: IOrganizer
    ) -> Optional[IPluginRequirement.Problem]:
        """
        Check if the requirement is met, and return a problem if not.

        Args:
            organizer: The IOrganizer instance.

        Returns:
            The problem found if the requirement is not met, otherwise None.
        """
        ...

class IProfile:
    """
    Interface to interact with Mod Organizer 2 profiles.
    """

    def absoluteIniFilePath(self: IProfile, inifile: str) -> str:
        """
        Retrieve the absolute file path to the corresponding INI file for this profile.

        If iniFile does not correspond to a file in the list of INI files for the
        current game (as returned by IPluginGame::iniFiles), the path to the global
        file will be returned (if iniFile is absolute, iniFile is returned, otherwise
        the path is assumed relative to the game documents directory).

        Args:
            inifile: INI file to retrieve a path for. This can either be the name of a file or a path to the
                absolute file outside of the profile.

        Returns:
            The absolute path for the given INI file for this profile.
        """
        ...
    def absolutePath(self: IProfile) -> str:
        """
        Returns:
            The absolute path to the profile folder.
        """
        ...
    def invalidationActive(self: IProfile) -> tuple[bool, bool]:
        """
        Returns:
            True if automatic archive invalidation is enabled for this profile, False otherwise.
        """
        ...
    def localSavesEnabled(self: IProfile) -> bool:
        """
        Returns:
            True if profile-specific saves are enabled for this profile, False otherwise.
        """
        ...
    def localSettingsEnabled(self: IProfile) -> bool:
        """
        Returns:
            True if profile-specific game settings are enabled for this profile, False otherwise.
        """
        ...
    def name(self: IProfile) -> str:
        """
        Returns:
            The name of this profile.
        """
        ...

class ISaveGame:
    """
    Base class for information about what is in a save game.
    """

    def __init__(self: ISaveGame) -> None: ...
    def allFiles(
        self: ISaveGame,
    ) -> Sequence[Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo]]:
        """
        Returns:
            The list of all files related to this save.
        """
        ...
    def getCreationTime(self: ISaveGame) -> PyQt6.QtCore.QDateTime:
        """
        Retrieve the creation time of the save.

        The creation time of a save is not always the same as the creation time of
        the file containing the save.

        Returns:
            The creation time of the save.
        """
        ...
    def getFilepath(
        self: ISaveGame,
    ) -> Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo]:
        """
        Returns:
            The path name to the (main) file or folder for the save.
        """
        ...
    def getName(self: ISaveGame) -> str:
        """
        Returns:
            The name of this save, for display purpose.
        """
        ...
    def getSaveGroupIdentifier(self: ISaveGame) -> str:
        """
        Retrieve the name of the group this files belong to.

        The name can be used to identify sets of saves to transfer between profiles. For
        RPG games, this is usually the name of a character.

        Returns:
            The group identifier for this save game.
        """
        ...

class MO2Exception:
    """
    Base class for MO2 exception.
    """

    ...

class Mapping:
    @property
    def createTarget(self) -> bool: ...
    @createTarget.setter
    def createTarget(self, arg0: bool) -> None: ...
    @property
    def destination(self) -> str: ...
    @destination.setter
    def destination(self, arg0: str) -> None: ...
    @property
    def isDirectory(self) -> bool: ...
    @isDirectory.setter
    def isDirectory(self, arg0: bool) -> None: ...
    @property
    def source(self) -> str: ...
    @source.setter
    def source(self, arg0: str) -> None: ...
    @overload
    def __init__(self: Mapping) -> None:
        """
        Creates an empty Mapping.
        """
        ...
    @overload
    def __init__(
        self: Mapping,
        source: str,
        destination: str,
        is_directory: bool,
        create_target: bool = False,
    ) -> None:
        """
        Creates a Mapping with the given parameters.

        Args:
            source: The source of this mapping (absolute path), i.e. the path to the actual file.
            destination: Destination of this mapping (absolute path), i.e. the path in the virtual file system.
            is_directory: True if this mapping corresponds to a directory, False otherwise.
            create_target: True if file creation (including move or copy) should be redirected to source.
        """
        ...
    def __str__(self: Mapping) -> str: ...

class ModRepositoryFileInfo:
    @property
    def categoryID(self) -> int: ...
    @categoryID.setter
    def categoryID(self, arg0: int) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, arg0: str) -> None: ...
    @property
    def fileCategory(self) -> int: ...
    @fileCategory.setter
    def fileCategory(self, arg0: int) -> None: ...
    @property
    def fileID(self) -> int: ...
    @fileID.setter
    def fileID(self, arg0: int) -> None: ...
    @property
    def fileName(self) -> str: ...
    @fileName.setter
    def fileName(self, arg0: str) -> None: ...
    @property
    def fileSize(self) -> int: ...
    @fileSize.setter
    def fileSize(self, arg0: int) -> None: ...
    @property
    def fileTime(self) -> PyQt6.QtCore.QDateTime: ...
    @fileTime.setter
    def fileTime(self, arg0: PyQt6.QtCore.QDateTime) -> None: ...
    @property
    def gameName(self) -> str: ...
    @gameName.setter
    def gameName(self, arg0: str) -> None: ...
    @property
    def modID(self) -> int: ...
    @modID.setter
    def modID(self, arg0: int) -> None: ...
    @property
    def modName(self) -> str: ...
    @modName.setter
    def modName(self, arg0: str) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, arg0: str) -> None: ...
    @property
    def newestVersion(self) -> VersionInfo: ...
    @newestVersion.setter
    def newestVersion(self, arg0: VersionInfo) -> None: ...
    @property
    def repository(self) -> str: ...
    @repository.setter
    def repository(self, arg0: str) -> None: ...
    @property
    def uri(self) -> str: ...
    @uri.setter
    def uri(self, arg0: str) -> None: ...
    @property
    def userData(self) -> MoVariant: ...
    @userData.setter
    def userData(self, arg0: MoVariant) -> None: ...
    @property
    def version(self) -> VersionInfo: ...
    @version.setter
    def version(self, arg0: VersionInfo) -> None: ...
    @overload
    def __init__(self: ModRepositoryFileInfo, other: ModRepositoryFileInfo) -> None: ...
    @overload
    def __init__(
        self: ModRepositoryFileInfo,
        game_name: str = "",
        mod_id: int = 0,
        file_id: int = 0,
    ) -> None: ...
    def __str__(self: ModRepositoryFileInfo) -> str: ...
    @staticmethod
    def createFromJson(data: str) -> ModRepositoryFileInfo: ...

class PluginRequirementFactory:
    @staticmethod
    def basic(
        checker: Callable[[IOrganizer], bool], description: str
    ) -> IPluginRequirement:
        """
        Create a basic requirement.

        Args:
            checker: The callable to use to check if the requirement is met. Should return True
                if the requirement is met, False otherwise.
            description: The description of the problem, when the requirement is not met.

        Returns:
            The constructed requirement.
        """
        ...
    @staticmethod
    def diagnose(diagnose: IPluginDiagnose) -> IPluginRequirement:
        """
        Construct a requirement from a diagnose plugin.

        If the wrapped diagnose plugin reports a problem, the requirement fails
        and the associated message is the one from the diagnose plugin (or the
        list of messages if multiple problems were reported).

        Args:
            diagnose: The diagnose plugin to wrap in this requirement.

        Returns:
            The constructed requirement.
        """
        ...
    @overload
    @staticmethod
    def gameDependency(games: Sequence[str]) -> IPluginRequirement:
        """
        Create a new game dependency requirement.

        The requirement is met when the managed game is one of the specified game.

        Args:
            games: The names of the required games.

        Returns:
            The constructed requirement.
        """
        ...
    @overload
    @staticmethod
    def gameDependency(game: str) -> IPluginRequirement:
        """
        Create a new game dependency requirement.

        The requirement is met when the managed game is the specified game.

        Args:
            game: The name of the required game.

        Returns:
            The constructed requirement.
        """
        ...
    @overload
    @staticmethod
    def pluginDependency(plugins: Sequence[str]) -> IPluginRequirement:
        """
        Create a new plugin dependency requirement.

        The requirement is met when one of the specified plugins is enabled.

        Args:
            plugins: The name of the plugins.

        Returns:
            The constructed requirement.
        """
        ...
    @overload
    @staticmethod
    def pluginDependency(plugin: str) -> IPluginRequirement:
        """
        Create a new plugin dependency requirement.

        The requirement is met when the specified plugin is enabled.

        Args:
            plugin: The name of the plugin that must be enabled.

        Returns:
            The constructed requirement.
        """
        ...

class Setting:
    """
    Class to hold the user-configurable parameters an extension or plugin accepts.
    The purpose of this class is only to inform the application what settings to offer
    to the user, it does not hold the actual value.
    """

    @property
    def default_value(self) -> MoVariant: ...
    @property
    def description(self) -> str: ...
    @property
    def group(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def title(self) -> str: ...
    @overload
    def __init__(
        self: Setting, name: str, title: str, description: str, default_value: MoVariant
    ) -> None:
        """
        Args:
            name: Name of the setting (for internal usage).
            title: Name of the setting (for display).
            description: Description of the setting.
            default_value: Default value of the setting.
        """
        ...
    @overload
    def __init__(
        self: Setting,
        name: str,
        title: str,
        description: str,
        group: str,
        default_value: MoVariant,
    ) -> None:
        """
        Args:
            name: Name of the setting (for internal usage).
            title: Name of the setting (for display).
            description: Description of the setting.
            group: Name of the group of the setting.
            default_value: Default value of the setting.
        """
        ...

class SettingGroup:
    """
    Class representing a group of setting. The class only describes the group, it
    does not hold the settings.
    """

    @property
    def description(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def title(self) -> str: ...
    def __init__(self: SettingGroup, name: str, title: str, description: str) -> None:
        """
        Args:
            name: Name of the group (for internal usage, in particular in Setting).
            title: Name of the group (for display).
            description: Description of the group.
        """
        ...

class Version:
    """
    Represents a version.
    """

    class FormatMode(Enum):
        FORCE_SUBPATCH = ...
        NO_SEPARATOR = ...
        SHORT_ALPHA_BETA = ...
        NO_METADATA = ...
        CONDENSED = ...

        @property
        def value(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __eq__(self: Version.FormatMode, other: object) -> bool: ...
        def __ge__(self: Version.FormatMode, other: Version.FormatMode) -> bool: ...
        def __gt__(self: Version.FormatMode, other: Version.FormatMode) -> bool: ...
        def __int__(self: Version.FormatMode) -> int: ...
        def __le__(self: Version.FormatMode, other: Version.FormatMode) -> bool: ...
        def __lt__(self: Version.FormatMode, other: Version.FormatMode) -> bool: ...
        def __ne__(self: Version.FormatMode, other: object) -> bool: ...
        def __str__(self: Version.FormatMode) -> str: ...

    class ParseMode(Enum):
        SEMVER = ...
        MO2 = ...

        @property
        def value(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __eq__(self: Version.ParseMode, other: object) -> bool: ...
        def __int__(self: Version.ParseMode) -> int: ...
        def __ne__(self: Version.ParseMode, other: object) -> bool: ...
        def __str__(self: Version.ParseMode) -> str: ...

    class ReleaseType(Enum):
        DEVELOPMENT = ...
        ALPHA = ...
        BETA = ...
        RELEASE_CANDIDATE = ...

        @property
        def value(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __eq__(self: Version.ReleaseType, other: object) -> bool: ...
        def __int__(self: Version.ReleaseType) -> int: ...
        def __ne__(self: Version.ReleaseType, other: object) -> bool: ...
        def __str__(self: Version.ReleaseType) -> str: ...

    ALPHA: ReleaseType = ...
    BETA: ReleaseType = ...
    CONDENSED: FormatMode = ...
    DEVELOPMENT: ReleaseType = ...
    FORCE_SUBPATCH: FormatMode = ...
    NO_METADATA: FormatMode = ...
    NO_SEPARATOR: FormatMode = ...
    RELEASE_CANDIDATE: ReleaseType = ...
    SHORT_ALPHA_BETA: FormatMode = ...

    @property
    def build_metadata(self) -> str: ...
    @property
    def major(self) -> int: ...
    @property
    def minor(self) -> int: ...
    @property
    def patch(self) -> int: ...
    @property
    def prereleases(self) -> Sequence[ReleaseType | str]: ...
    @property
    def subpatch(self) -> int: ...
    @overload
    def __init__(
        self: Version, major: int, minor: int, patch: int, metadata: str = ""
    ) -> None: ...
    @overload
    def __init__(
        self: Version,
        major: int,
        minor: int,
        patch: int,
        subpatch: int,
        metadata: str = "",
    ) -> None: ...
    @overload
    def __init__(
        self: Version,
        major: int,
        minor: int,
        patch: int,
        type: Version.ReleaseType,
        metadata: str = "",
    ) -> None: ...
    @overload
    def __init__(
        self: Version,
        major: int,
        minor: int,
        patch: int,
        subpatch: int,
        type: Version.ReleaseType,
        metadata: str = "",
    ) -> None: ...
    @overload
    def __init__(
        self: Version,
        major: int,
        minor: int,
        patch: int,
        type: Version.ReleaseType,
        prerelease: int,
        metadata: str = "",
    ) -> None: ...
    @overload
    def __init__(
        self: Version,
        major: int,
        minor: int,
        patch: int,
        subpatch: int,
        type: Version.ReleaseType,
        prerelease: int,
        metadata: str = "",
    ) -> None: ...
    @overload
    def __init__(
        self: Version,
        major: int,
        minor: int,
        patch: int,
        subpatch: int,
        prereleases: list[Union[int, Version.ReleaseType]],
        metadata: str = "",
    ) -> None: ...
    def __eq__(self: Version, other: object) -> bool: ...
    def __ge__(self: Version, arg0: Version) -> bool: ...
    def __gt__(self: Version, arg0: Version) -> bool: ...
    def __le__(self: Version, arg0: Version) -> bool: ...
    def __lt__(self: Version, arg0: Version) -> bool: ...
    def __ne__(self: Version, other: object) -> bool: ...
    def __str__(self: Version, arg0: Version.FormatMode) -> str: ...
    def isPreRelease(self: Version) -> bool:
        """
        Check if this version contains pre-releases components.

        Returns:
            True if this version contains pre-releases components, False otherwise.
        """
        ...
    @staticmethod
    def parse(value: str, mode: Version.ParseMode = ParseMode.SEMVER) -> Version:
        """
        Parse a version from a string.

        Args:
            value: String to parse.
            mode: Mode to use to parse the string.

        Returns:
            The version parsed from the given string.

        Raises:
            InvalidVersionException: if the given string is invalid.
        """
        ...
    def string(self: Version, mode: Version.FormatMode = 14) -> str:
        """
        Create a user-readably representation of this version.

        Args:
            mode: Mode to use to create the string.

        Returns:
            A string representing this version.
        """
        ...

class VersionInfo:
    """
    Represents the version of a mod or plugin.
    """

    @overload
    def __init__(self: VersionInfo) -> None:
        """
        Construct an invalid VersionInfo.
        """
        ...
    @overload
    def __init__(
        self: VersionInfo, value: str, scheme: VersionScheme = VersionScheme.DISCOVER
    ) -> None:
        """
        Construct a VersionInfo by parsing the given string according to the given scheme.

        Args:
            value: String to parse.
            scheme: Scheme to use to parse the string.
        """
        ...
    @overload
    def __init__(
        self: VersionInfo,
        major: int,
        minor: int,
        subminor: int,
        subsubminor: int,
        release_type: ReleaseType = ReleaseType.FINAL,
    ) -> None:
        """
        Construct a VersionInfo using the given elements.

        Args:
            major: Major version.
            minor: Minor version.
            subminor: Subminor version.
            subsubminor: Subsubminor version.
            release_type: Type of release.
        """
        ...
    @overload
    def __init__(
        self: VersionInfo,
        major: int,
        minor: int,
        subminor: int,
        release_type: ReleaseType = ReleaseType.FINAL,
    ) -> None:
        """
        Construct a VersionInfo using the given elements.

        Args:
            major: Major version.
            minor: Minor version.
            subminor: Subminor version.
            release_type: Type of release.
        """
        ...
    def __eq__(self: VersionInfo, other: object) -> bool: ...
    def __ge__(self: VersionInfo, arg0: VersionInfo) -> bool: ...
    def __gt__(self: VersionInfo, arg0: VersionInfo) -> bool: ...
    def __le__(self: VersionInfo, arg0: VersionInfo) -> bool: ...
    def __lt__(self: VersionInfo, arg0: VersionInfo) -> bool: ...
    def __ne__(self: VersionInfo, other: object) -> bool: ...
    def __str__(self: VersionInfo) -> str:
        """
        Returns:
            See `canonicalString()`.
        """
        ...
    def canonicalString(self: VersionInfo) -> str:
        """
        Returns:
            A canonical string representing this version, that can be stored and then parsed using the parse() method.
        """
        ...
    def clear(self: VersionInfo) -> None:
        """
        Resets this VersionInfo to an invalid version.
        """
        ...
    def displayString(self: VersionInfo, forced_segments: int = 2) -> str:
        """
        Args:
            forced_segments: The number of version segments to display even if the version is 0. 1 is major, 2 is major
                and minor, etc. The only implemented ranges are (-inf,2] for major/minor, [3] for major/minor/subminor,
                and [4,inf) for major/minor/subminor/subsubminor. This only versions with a regular scheme.

        Returns:
            A string for display to the user. The returned string may not contain enough information to reconstruct this version info.
        """
        ...
    def isValid(self: VersionInfo) -> bool:
        """
        Returns:
            True if this VersionInfo is valid, False otherwise.
        """
        ...
    def parse(
        self: VersionInfo,
        value: str,
        scheme: VersionScheme = VersionScheme.DISCOVER,
        is_manual: bool = False,
    ) -> None:
        """
        Update this VersionInfo by parsing the given string using the given scheme.

        Args:
            value: String to parse.
            scheme: Scheme to use to parse the string.
            is_manual: True if the given string should be treated as user input.
        """
        ...
    def scheme(self: VersionInfo) -> VersionScheme:
        """
        Returns:
            The version scheme in effect for this VersionInfo.
        """
        ...

class BSAInvalidation(GameFeature):
    def __init__(self: BSAInvalidation) -> None: ...
    @abc.abstractmethod
    def activate(self: BSAInvalidation, profile: IProfile) -> None: ...
    @abc.abstractmethod
    def deactivate(self: BSAInvalidation, profile: IProfile) -> None: ...
    @abc.abstractmethod
    def isInvalidationBSA(self: BSAInvalidation, name: str) -> bool: ...

class DataArchives(GameFeature):
    def __init__(self: DataArchives) -> None: ...
    @abc.abstractmethod
    def addArchive(
        self: DataArchives, profile: IProfile, index: int, name: str
    ) -> None:
        """
        Add an archive to the archive list.

        Args:
            profile: Profile to add the archive to.
            index: Index to insert before. Use 0 for the beginning of the list or INT_MAX for
                the end of the list).
            name: Name of the archive to add.
        """
        ...
    @abc.abstractmethod
    def archives(self: DataArchives, profile: IProfile) -> Sequence[str]:
        """
        Retrieve the list of archives in the given profile.

        Args:
            profile: Profile to retrieve archives from.

        Returns:
            The list of archives in the given profile.
        """
        ...
    @abc.abstractmethod
    def removeArchive(self: DataArchives, profile: IProfile, name: str) -> None:
        """
        Remove the given archive from the given profile.

        Args:
            profile: Profile to remove the archive from.
            name: Name of the archive to remove.
        """
        ...
    @abc.abstractmethod
    def vanillaArchives(self: DataArchives) -> Sequence[str]:
        """
        Retrieve the list of vanilla archives.

        Vanilla archives are archive files that are shipped with the original
        game.

        Returns:
            The list of vanilla archives.
        """
        ...

class GamePlugins(GameFeature):
    def __init__(self: GamePlugins) -> None: ...
    @abc.abstractmethod
    def getLoadOrder(self: GamePlugins) -> Sequence[str]: ...
    @abc.abstractmethod
    def lightPluginsAreSupported(self: GamePlugins) -> bool:
        """
        Returns:
            True if light plugins are supported, False otherwise.
        """
        ...
    @abc.abstractmethod
    def mediumPluginsAreSupported(self: GamePlugins) -> bool:
        """
        Returns:
            True if medium plugins are supported, False otherwise.
        """
        ...
    @abc.abstractmethod
    def readPluginLists(self: GamePlugins, plugin_list: IPluginList) -> None: ...
    @abc.abstractmethod
    def writePluginLists(self: GamePlugins, plugin_list: IPluginList) -> None: ...

class IFileTree(FileTreeEntry):
    """
    Interface to classes that provides way to visualize and alter file trees. The tree
    may not correspond to an actual file tree on the disk (e.g., inside an archive,
    from a QTree Widget, ...).

    Read-only operations on the tree are thread-safe, even when the tree has not been populated
    yet.

    In order to prevent wrong usage of the tree, implementing classes may throw
    UnsupportedOperationException if an operation is not supported. By default, all operations
    are supported, but some may not make sense in many situations.

    The goal of this is not reflect the change made to a IFileTree to the disk, but child
    classes may override relevant methods to do so.

    The tree is built upon FileTreeEntry. A given tree holds shared pointers to its entries
    while each entry holds a weak pointer to its parent, this means that the descending link
    are strong (shared pointers) but the uplink are weak.

    Accessing the parent is always done by locking the weak pointer so that returned pointer
    or either null or valid. This structure implies that as long as the initial root lives,
    entry should not be destroyed, unless the entry are detached from the root and no shared
    pointers are kept.

    However, it is not guarantee that one can go up the tree from a single node entry. If the
    root node is destroyed, it will not be possible to go up the tree, even if we still have
    a valid shared pointer.
    """

    class InsertPolicy(Enum):
        FAIL_IF_EXISTS = ...
        REPLACE = ...
        MERGE = ...

        @property
        def value(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __eq__(self: IFileTree.InsertPolicy, other: object) -> bool: ...
        def __int__(self: IFileTree.InsertPolicy) -> int: ...
        def __ne__(self: IFileTree.InsertPolicy, other: object) -> bool: ...
        def __str__(self: IFileTree.InsertPolicy) -> str: ...

    class WalkReturn(Enum):
        """
        Enumeration that can be returned by the callback for the `walk()` method to stop the
        walking operation early.
        """

        CONTINUE = ...
        STOP = ...
        SKIP = ...

        @property
        def value(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __eq__(self: IFileTree.WalkReturn, other: object) -> bool: ...
        def __int__(self: IFileTree.WalkReturn) -> int: ...
        def __ne__(self: IFileTree.WalkReturn, other: object) -> bool: ...
        def __str__(self: IFileTree.WalkReturn) -> str: ...

    CONTINUE: WalkReturn = ...
    FAIL_IF_EXISTS: InsertPolicy = ...
    MERGE: InsertPolicy = ...
    REPLACE: InsertPolicy = ...
    SKIP: WalkReturn = ...
    STOP: WalkReturn = ...

    def __bool__(self: IFileTree) -> bool:
        """
        Returns:
            True if this tree is not empty, False otherwise.
        """
        ...
    def __getitem__(self: IFileTree, index: int) -> FileTreeEntry:
        """
        Retrieve the entry at the given index in this tree.

        Args:
            index: Index of the entry to retrieve, must be less than the size.

        Returns:
            The entry at the given index.

        Raises:
            IndexError: If the given index is not in range for this tree.
        """
        ...
    def __iter__(self: IFileTree) -> Iterator[FileTreeEntry]:
        """
        Retrieves an iterator for entries directly under this tree.

        This method does not recurse into subtrees, see `walk()` for this.

        Returns:
            An iterator object that can be used to iterate over entries in this tree.
        """
        ...
    def __len__(self: IFileTree) -> int:
        """
        Returns:
            The number of entries directly under this tree.
        """
        ...
    def addDirectory(self: IFileTree, path: str) -> IFileTree:
        """
        Create a new directory tree under this tree.

        This method will create missing folders in the given path and will
        not fail if the directory already exists but will fail if the given
        path contains "." or "..".
        This method invalidates iterators to this tree and all the subtrees
        present in the given path.

        Args:
            path: Path to the directory to create.

        Returns:
            An IFileTree corresponding to the created directory.

        Raises:
            RuntimeError: If the directory could not be created.
        """
        ...
    def addFile(
        self: IFileTree, path: str, replace_if_exists: bool = False
    ) -> FileTreeEntry:
        """
        Create a new file directly under this tree.

        This method will fail if the file already exists and `replace_if_exists` is `False`.
        This method invalidates iterators to this tree and all the subtrees present in the
        given path.

        Args:
            path: Path to the file to create.
            replace_if_exists: If True and an entry already exists at the given location, it will be replaced by
                a new entry. This will replace both files and directories.

        Returns:
            A FileTreeEntry corresponding to the created file.

        Raises:
            RuntimeError: If the file could not be created.
        """
        ...
    def clear(self: IFileTree) -> bool:
        """
        Delete (detach) all the entries from this tree.

        This method will go through the entries in this tree and stop at the first
        entry that cannot be deleted, this means that the tree can be partially cleared.

        Returns:
            True if all entries have been detached, False otherwise.
        """
        ...
    def copy(
        self: IFileTree,
        entry: FileTreeEntry,
        path: str = "",
        insert_policy: IFileTree.InsertPolicy = InsertPolicy.FAIL_IF_EXISTS,
    ) -> FileTreeEntry:
        """
        Move the given entry to the given path under this tree.

        The entry must not be a parent tree of this tree. This method can also be used
        to rename entries.

        If the insert policy if FAIL_IF_EXISTS, the call will fail if an entry
        at the same location already exists. If the policy is REPLACE, an existing
        entry will be replaced. If MERGE, the entry will be merged with the existing
        one (if the entry is a file, and a file exists, the file will be replaced).

        This method invalidates iterator to this tree, to the parent tree of the given
        entry, and to subtrees of this tree if the insert policy is MERGE.

        Args:
            entry: Entry to copy.
            path: The path to copy the entry to. If the path ends with / or \\, the entry will
                be copied in the corresponding directory instead of replacing it. If the
                given path is empty (`""`), the entry is copied directly under this tree.
            insert_policy: Policy to use to resolve conflicts.

        Returns:
            The new entry (copy of the specified entry).

        Raises:
            RuntimeError: If the entry could not be copied.
        """
        ...
    def createOrphanTree(self: IFileTree, name: str = "") -> IFileTree:
        """
        Create a new orphan empty tree.

        Args:
            name: Name of the tree.

        Returns:
            A new tree without any parent.
        """
        ...
    def exists(
        self: IFileTree,
        path: str,
        type: FileTreeEntry.FileTypes = FileTreeEntry.FileTypes.FILE_OR_DIRECTORY,
    ) -> bool:
        """
        Check if the given entry exists.

        Args:
            path: Path to the entry, separated by / or \\.
            type: The type of the entry to check.

        Returns:
            True if the entry was found, False otherwise.
        """
        ...
    def find(
        self: IFileTree,
        path: str,
        type: FileTreeEntry.FileTypes = FileTreeEntry.FileTypes.FILE_OR_DIRECTORY,
    ) -> IFileTree | FileTreeEntry | None:
        """
        Retrieve the given entry.

        If no entry exists at the given path, or if the entry is not of the right
        type, `None` is returned.

        Args:
            path: Path to the entry, separated by / or \\.
            type: The type of the entry to check.

        Returns:
            The entry at the given location, or `None` if the entry was not found or
        was not of the correct type.
        """
        ...
    def insert(
        self: IFileTree,
        entry: FileTreeEntry,
        policy: IFileTree.InsertPolicy = InsertPolicy.FAIL_IF_EXISTS,
    ) -> bool:
        """
        Insert the given entry in this tree, removing it from its
        previous parent.

        The entry must not be this tree or a parent entry of this tree.

          - If the insert policy if `FAIL_IF_EXISTS`, the call will fail if an entry
            with the same name already exists.
          - If the policy is `REPLACE`, an existing entry will be replaced by the given entry.
          - If the policy is `MERGE`:

            - If there is no entry with the same name, the new entry is inserted.
            - If there is an entry with the same name:

              - If both entries are files, the old file is replaced by the given entry.
              - If both entries are directories, a merge is performed as if using merge().
              - Otherwise the insertion fails (two entries with different types).

        This method invalidates iterator to this tree, to the parent tree of the given
        entry, and to subtrees of this tree if the insert policy is MERGE.

        Args:
            entry: Entry to insert.
            policy: Policy to use to resolve conflicts.

        Returns:
            True if the entry was insert, False otherwise.
        """
        ...
    def merge(
        self: IFileTree, other: IFileTree, overwrites: bool = False
    ) -> Union[dict[FileTreeEntry, FileTreeEntry], int]:
        """
        Merge the given tree with this tree, i.e., insert all entries
        of the given tree into this tree.

        The tree must not be this tree or a parent entry of this tree. Files present in both tree
        will be replaced by files in the given tree. After a merge, the source tree will be
        empty but still attached to its parent.

        If `overwrites` is `True`, a map from overridden files to new files will be returned.

        Note that the merge process makes no distinction between files and directories
        when merging: if a directory is present in this tree and a file from source
        is in conflict with it, the tree will be removed and the file inserted; if a file
        is in this tree and a directory from source is in conflict with it, the file will
        be replaced with the directory.

        This method invalidates iterators to this tree, all the subtrees under this tree
        present in the given path, and all the subtrees of the given source.

        Args:
            other: Tree to merge.
            overwrites: If True, a mapping from overridden files to new files will be returned.

        Returns:
            If `overwrites` is True, a mapping from overridden files to new files, otherwise
        the number of overwritten entries.

        Raises:
            RuntimeError: If the merge failed.
        """
        ...
    def move(
        self: IFileTree,
        entry: FileTreeEntry,
        path: str,
        policy: IFileTree.InsertPolicy = InsertPolicy.FAIL_IF_EXISTS,
    ) -> bool:
        """
        Move the given entry to the given path under this tree.

        The entry must not be a parent tree of this tree. This method can also be used
        to rename entries.

        If the insert policy if FAIL_IF_EXISTS, the call will fail if an entry
        at the same location already exists. If the policy is REPLACE, an existing
        entry will be replaced. If MERGE, the entry will be merged with the existing
        one (if the entry is a file, and a file exists, the file will be replaced).

        This method invalidates iterator to this tree, to the parent tree of the given
        entry, and to subtrees of this tree if the insert policy is MERGE.

        Args:
            entry: Entry to move.
            path: The path to move the entry to. If the path ends with / or \\, the entry will
                be inserted in the corresponding directory instead of replacing it. If the
                given path is empty (`""`), this is equivalent to `insert()`.
            policy: Policy to use to resolve conflicts.

        Returns:
            True if the entry was moved correctly, False otherwise.
        """
        ...
    def pathTo(self: IFileTree, entry: FileTreeEntry, sep: str = "\\") -> str:
        """
        Retrieve the path from this tree to the given entry.

        Args:
            entry: The entry to reach, must be in this tree.
            sep: The type of separator to use to create the path.

        Returns:
            The path from this tree to the given entry, including the name of the entry, or
        an empty string if the given entry was not found under this tree.
        """
        ...
    @overload
    def remove(self: IFileTree, name: str) -> bool:
        """
        Delete the entry with the given name.

        This method does not recurse into subtrees, so the entry should be
        accessible directly from this tree.

        Args:
            name: Name of the entry to delete.

        Returns:
            True if the entry was deleted, False otherwise.
        """
        ...
    @overload
    def remove(self: IFileTree, entry: FileTreeEntry) -> bool:
        """
        Delete the given entry.

        Args:
            entry: Entry to delete. The entry must belongs to this tree (and not to a subtree).

        Returns:
            True if the entry was deleted, False otherwise.
        """
        ...
    def removeAll(self: IFileTree, names: Sequence[str]) -> int:
        """
        Delete the entries with the given names from the tree.

        This method does not recurse into subtrees, so only entries accessible
        directly from this tree will be removed. This method invalidates iterators.

        Args:
            names: Names of the entries to delete.

        Returns:
            The number of deleted entry.
        """
        ...
    def removeIf(self: IFileTree, filter: Callable[[FileTreeEntry], bool]) -> int:
        """
        Delete entries matching the given predicate from the tree.

        This method does not recurse into subtrees, so only entries accessible
        directly from this tree will be removed. This method invalidates iterators.

        Args:
            filter: Predicate that should return true for entries to delete.

        Returns:
            The number of deleted entry.
        """
        ...
    def walk(
        self: IFileTree,
        callback: Callable[[str, FileTreeEntry], IFileTree.WalkReturn],
        sep: str = "\\",
    ) -> None:
        """
        Walk this tree, calling the given function for each entry in it.

        The given callback will be called with two parameters: the path from this tree to the given entry
        (with a trailing separator, not including the entry name), and the actual entry. The method returns
        a `WalkReturn` object to indicates what to do.

        Args:
            callback: Method to call for each entry in the tree.
            sep: Type of separator to use to construct the path.
        """
        ...

class IModRepositoryBridge(PyQt6.QtCore.QObject):
    descriptionAvailable: PyQt6.QtCore.pyqtSignal = ...
    filesAvailable: PyQt6.QtCore.pyqtSignal = ...
    fileInfoAvailable: PyQt6.QtCore.pyqtSignal = ...
    downloadURLsAvailable: PyQt6.QtCore.pyqtSignal = ...
    endorsementsAvailable: PyQt6.QtCore.pyqtSignal = ...
    endorsementToggled: PyQt6.QtCore.pyqtSignal = ...
    trackedModsAvailable: PyQt6.QtCore.pyqtSignal = ...
    trackingToggled: PyQt6.QtCore.pyqtSignal = ...
    requestFailed: PyQt6.QtCore.pyqtSignal = ...

    def __getattr__(self: IModRepositoryBridge, arg0: str) -> object: ...
    def _object(self: IModRepositoryBridge) -> PyQt6.QtCore.QObject:
        """
        Returns:
            The underlying `QObject` for the bridge.
        """
        ...
    def requestDescription(
        self: IModRepositoryBridge, game_name: str, mod_id: int, user_data: MoVariant
    ) -> None:
        """
        Request description of a mod.

        Args:
            game_name: Name of the game containing the mod.
            mod_id: Nexus ID of the mod.
            user_data: User data to be returned with the result.
        """
        ...
    def requestDownloadURL(
        self: IModRepositoryBridge,
        game_name: str,
        mod_id: int,
        file_id: int,
        user_data: MoVariant,
    ) -> None:
        """
        Request download URL for mod file.0

        Args:
            game_name: Name of the game containing the mod.
            mod_id: Nexus ID of the mod.
            file_id: ID of the file for which a URL should be returned.
            user_data: User data to be returned with the result.
        """
        ...
    def requestFileInfo(
        self: IModRepositoryBridge,
        game_name: str,
        mod_id: int,
        file_id: int,
        user_data: MoVariant,
    ) -> None:
        """
        Args:
            game_name: Name of the game containing the mod.
            mod_id: Nexus ID of the mod.
            file_id: ID of the file for which information is requested.
            user_data: User data to be returned with the result.
        """
        ...
    def requestFiles(
        self: IModRepositoryBridge, game_name: str, mod_id: int, user_data: MoVariant
    ) -> None:
        """
        Request the list of files belonging to a mod.

        Args:
            game_name: Name of the game containing the mod.
            mod_id: Nexus ID of the mod.
            user_data: User data to be returned with the result.
        """
        ...
    def requestToggleEndorsement(
        self: IModRepositoryBridge,
        game_name: str,
        mod_id: int,
        mod_version: str,
        endorse: bool,
        user_data: MoVariant,
    ) -> None:
        """
        Args:
            game_name: Name of the game containing the mod.
            mod_id: Nexus ID of the mod.
            mod_version: Version of the mod.
            endorse:
            user_data: User data to be returned with the result.
        """
        ...

class IPluginDiagnose(IPlugin):
    """
    Plugins that create problem reports to be displayed in the UI.

    This can be used to report problems related to the same plugin (which implements further
    interfaces) or as a stand-alone diagnosis tool.
    """

    def __init__(self: IPluginDiagnose) -> None: ...
    def _invalidate(self: IPluginDiagnose) -> None:
        """
        Invalidate the problems corresponding to this plugin.
        """
        ...
    @abc.abstractmethod
    def activeProblems(self: IPluginDiagnose) -> list[int]:
        """
        Retrieve the list of active problems found by this plugin.

        This method returns a list of problem IDs, that are then used when calling other methods
        such as `shortDescription()` or `hasGuidedFix()`.

        Returns:
            The list of active problems for this plugin.
        """
        ...
    @abc.abstractmethod
    def fullDescription(self: IPluginDiagnose, key: int) -> str:
        """
        Retrieve the full description of the problem corresponding to the given key.

        Args:
            key: ID of the problem.

        Returns:
            The full description of the problem.

        Raises:
            IndexError: If the key is not valid.
        """
        ...
    @abc.abstractmethod
    def hasGuidedFix(self: IPluginDiagnose, key: int) -> bool:
        """
        Check if the problem corresponding to the given key has a guided fix.

        Args:
            key: ID of the problem.

        Returns:
            True if there is a guided fix for the problem, False otherwise.

        Raises:
            IndexError: If the key is not valid.
        """
        ...
    @abc.abstractmethod
    def shortDescription(self: IPluginDiagnose, key: int) -> str:
        """
        Retrieve the short description of the problem corresponding to the given key.

        Args:
            key: ID of the problem.

        Returns:
            The short description of the problem.

        Raises:
            IndexError: If the key is not valid.
        """
        ...
    @abc.abstractmethod
    def startGuidedFix(self: IPluginDiagnose, key: int) -> None:
        """
        Starts a guided fix for the problem corresponding to the given key.

        This method should throw `ValueError` if there is no guided fix for the corresponding
        problem.

        Args:
            key: ID of the problem.

        Raises:
            IndexError: If the key is not valid.
            ValueError: If there is no guided fix for this problem.
        """
        ...

class IPluginFileMapper(IPlugin):
    """
    Plugins that adds virtual file links.
    """

    def __init__(self: IPluginFileMapper) -> None: ...
    @abc.abstractmethod
    def mappings(self: IPluginFileMapper) -> list[Mapping]:
        """
        Returns:
            Mapping for the virtual file system (VFS).
        """
        ...

class IPluginGame(IPlugin):
    """
    Base classes for game plugins.

    Each game requires a specific game plugin. These plugins were initially designed for
    Bethesda games, so a lot of methods and attributes are irrelevant for other games. If
    you wish to write a plugin for a much simpler game, please consider the `basic_games`
    plugin: https://github.com/ModOrganizer2/modorganizer-basic_games
    """

    def __init__(self: IPluginGame) -> None: ...
    def CCPlugins(self: IPluginGame) -> Sequence[str]:
        """
        Returns:
            The current list of active Creation Club plugins.
        """
        ...
    def DLCPlugins(self: IPluginGame) -> Sequence[str]:
        """
        Returns:
            The list of esp/esm files that are part of known DLCs.
        """
        ...
    @abc.abstractmethod
    def binaryName(self: IPluginGame) -> str:
        """
        Returns:
            The name of the default executable to run (relative to the game folder).
        """
        ...
    @abc.abstractmethod
    def dataDirectory(self: IPluginGame) -> PyQt6.QtCore.QDir:
        """
        Returns:
            The path to the directory containing data (absolute path).
        """
        ...
    @abc.abstractmethod
    def detectGame(self: IPluginGame) -> None:
        """
        Detect the game.

        This method is the first called for game plugins (before `init()`). The following
        methods should work properly after the call to `detectGame()` (and before `init()`):

          - gameName()
          - isInstalled()
          - gameIcon()
          - gameDirectory()
          - dataDirectory()
          - gameVariants()
          - looksValid()

        See `IPlugin.init()` for more.
        """
        ...
    def displayGameName(self: IPluginGame) -> str:
        """
        Returns:
            The name of the game to user for display, default to gameName().
        """
        ...
    @abc.abstractmethod
    def documentsDirectory(self: IPluginGame) -> PyQt6.QtCore.QDir:
        """
        Returns:
            The directory of the documents folder where configuration files and such for this game reside.
        """
        ...
    def enabledPlugins(self: IPluginGame) -> Sequence[str]:
        """
        Returns:
            A list of plugins enabled by the game but not in a strict load order.
        """
        ...
    @abc.abstractmethod
    def executableForcedLoads(
        self: IPluginGame,
    ) -> Sequence[ExecutableForcedLoadSetting]:
        """
        Returns:
            A list of automatically discovered libraries that can be force loaded with executables.
        """
        ...
    def executables(self: IPluginGame) -> Sequence[ExecutableInfo]:
        """
        Returns:
            A list of automatically discovered executables of the game itself and tools surrounding it.
        """
        ...
    @abc.abstractmethod
    def gameDirectory(self: IPluginGame) -> PyQt6.QtCore.QDir:
        """
        Returns:
            The directory containing the game installation.
        """
        ...
    @abc.abstractmethod
    def gameIcon(self: IPluginGame) -> PyQt6.QtGui.QIcon:
        """
        Returns:
            The icon representing the game.
        """
        ...
    @abc.abstractmethod
    def gameName(self: IPluginGame) -> str:
        """
        Returns:
            The name of the game (for internal usage).
        """
        ...
    def gameNexusName(self: IPluginGame) -> str:
        """
        Returns:
            The name of the game identifier for Nexus.
        """
        ...
    @abc.abstractmethod
    def gameShortName(self: IPluginGame) -> str:
        """
        Returns:
            The short name of the game.
        """
        ...
    def gameVariants(self: IPluginGame) -> Sequence[str]:
        """
        Retrieve the list of variants for this game.

        If there are multiple variants of a game (and the variants make a difference to the
        plugin), like a regular one and a GOTY-edition, the plugin can return a list of them
        and the user gets to chose which one he owns.

        Returns:
            The list of variants of the game.
        """
        ...
    @abc.abstractmethod
    def gameVersion(self: IPluginGame) -> str:
        """
        Returns:
            The version of the game.
        """
        ...
    @abc.abstractmethod
    def getLauncherName(self: IPluginGame) -> str:
        """
        Returns:
            The name of the launcher executable to run (relative to the game folder), or an
        empty string if there is no launcher.
        """
        ...
    @abc.abstractmethod
    def getSupportURL(self: IPluginGame) -> str:
        """
        Returns:
            An URL for the support page of this game.
        """
        ...
    def iniFiles(self: IPluginGame) -> Sequence[str]:
        """
        Returns:
            The list of INI files this game uses. The first file in the list should be the
        'main' INI file.
        """
        ...
    @abc.abstractmethod
    def initializeProfile(
        self: IPluginGame, directory: PyQt6.QtCore.QDir, settings: ProfileSetting
    ) -> None:
        """
        Initialize a profile for this game.

        The MO app does not yet support virtualizing only specific aspects but plugins should be written
        with this future functionality in mind.

        This function will be used to initially create a profile, potentially to repair it or upgrade/downgrade
        it so the implementations have to gracefully handle the case that the directory already contains files.

        Args:
            directory: The directory where the profile is to be initialized.
            settings: The parameters for how the profile should be initialized.
        """
        ...
    @abc.abstractmethod
    def isInstalled(self: IPluginGame) -> bool:
        """
        Returns:
            True if this game has been discovered as installed, False otherwise.
        """
        ...
    @abc.abstractmethod
    def listSaves(self: IPluginGame, folder: PyQt6.QtCore.QDir) -> list[ISaveGame]:
        """
        List saves in the given directory.

        Args:
            folder: The folder to list saves from.

        Returns:
            The list of game saves in the given folder.
        """
        ...
    def loadOrderMechanism(self: IPluginGame) -> LoadOrderMechanism:
        """
        Returns:
            The load order mechanism used by this game.
        """
        ...
    @abc.abstractmethod
    def looksValid(self: IPluginGame, directory: PyQt6.QtCore.QDir) -> bool:
        """
        Check if the given directory looks like a valid game installation.

        Args:
            directory: Directory to check.

        Returns:
            True if the directory looks like a valid installation of this game, False otherwise.
        """
        ...
    def lootGameName(self: IPluginGame) -> str:
        """
        Returns:
            The game name to use when calling LOOT from MO2, default to gameShortName().
        """
        ...
    @abc.abstractmethod
    def nexusGameID(self: IPluginGame) -> int:
        """
        Retrieve the Nexus game ID for this game.

        Example: For Skyrim, the Nexus game ID is 110.

        Returns:
            The Nexus game ID for this game.
        """
        ...
    def nexusModOrganizerID(self: IPluginGame) -> int:
        """
        Retrieve the Nexus mod ID of Mod Organizer for this game.

        Example: For Skyrim SE, the mod ID of MO2 is 6194. You can find the mod ID in the URL:
          https://www.nexusmods.com/skyrimspecialedition/mods/6194

        Returns:
            The Nexus mod ID of Mod Organizer for this game.
        """
        ...
    def primaryPlugins(self: IPluginGame) -> Sequence[str]:
        """
        Returns:
            The list of plugins that are part of the game and not considered optional.
        """
        ...
    def primarySources(self: IPluginGame) -> Sequence[str]:
        """
        Retrieve primary alternative 'short' names for this game.

        This is used to determine if a Nexus (or other) download source should be considered
        as a primary source for the game so that it is not flagged as an alternative one.

        Returns:
            The list of primary alternative 'short' names for this game, or an empty list.
        """
        ...
    @abc.abstractmethod
    def savesDirectory(self: IPluginGame) -> PyQt6.QtCore.QDir:
        """
        Returns:
            The directory where save games are stored.
        """
        ...
    def secondaryDataDirectories(self: IPluginGame) -> Dict[str, PyQt6.QtCore.QDir]:
        """
        Retrieve the list of secondary data directories. Each directories should be
        assigned a unique name that differs from "data" which is the name of the main
        data directory returned by dataDirectory().

        Returns:
            A mapping from unique name to secondary data directories.
        """
        ...
    @abc.abstractmethod
    def setGamePath(self: IPluginGame, path: str) -> None:
        """
        Set the path to the managed game.

        This is called during instance creation if the game is not auto-detected and the user has
        to specify the installation location. This is not called if the game has been auto-detected,
        so `isInstalled()` should call this.

        Args:
            path: Path to the game installation.
        """
        ...
    @abc.abstractmethod
    def setGameVariant(self: IPluginGame, variant: str) -> None:
        """
        Set the game variant.

        If there are multiple variants of game (as returned by `gameVariants()`), this will be
        called on start with the user-selected game variant.

        Args:
            variant: The game variant selected by the user.
        """
        ...
    def sortMechanism(self: IPluginGame) -> SortMechanism:
        """
        Returns:
            The sort mechanism for this game.
        """
        ...
    def steamAPPId(self: IPluginGame) -> str:
        """
        Retrieve the Steam app ID for this game.

        If the game is not available on Steam, this should return an empty string.

        If a game is available in multiple versions, those might have different app ids. The plugin
        should try to return the right one

        Returns:
            The Steam app ID for this game. Should be empty for games not available on steam.
        """
        ...
    @abc.abstractmethod
    def validShortNames(self: IPluginGame) -> Sequence[str]:
        """
        Retrieve the valid 'short' names for this game.

        This is used to determine if a Nexus download is valid for the current game since not all
        game variants have their own nexus pages and others can handle downloads from other nexus
        game pages and should be allowed to do so (e.g., you can install some Skyrim LE mod even
        when using Skyrim SE).

        The short name should be considered the primary handler for a directly supported game
        for purposes of auto-launching an instance.

        Returns:
            The list of valid short names for this game.
        """
        ...

class IPluginInstaller(IPlugin):
    """
    This is the top-level class for installer. Actual installers should inherit either:

      - `IPluginInstallerSimple` if the installer can work directly with the archive. This is what
        most installers use.
      - `IPluginInstallerCustom` if the installer needs to perform custom operations. This is only
        used by the external NCC installer and the OMOD installer.
    """

    def _manager(self: IPluginInstaller) -> IInstallationManager:
        """
        Returns:
            The installation manager.
        """
        ...
    def _parentWidget(self: IPluginInstaller) -> PyQt6.QtWidgets.QWidget:
        """
        Returns:
            The parent widget.
        """
        ...
    @abc.abstractmethod
    def isArchiveSupported(self: IPluginInstaller, tree: IFileTree) -> bool:
        """
        Check if the given file tree corresponds to a supported archive for this installer.

        Args:
            tree: The tree representing the content of the archive.

        Returns:
            True if this installer can handle the archive, False otherwise.
        """
        ...
    @abc.abstractmethod
    def isManualInstaller(self: IPluginInstaller) -> bool:
        """
        Check if this installer is a manual installer.

        Returns:
            True if this installer is a manual installer, False otherwise.
        """
        ...
    def onInstallationEnd(
        self: IPluginInstaller, result: InstallResult, new_mod: IModInterface
    ) -> None:
        """
        Method calls at the end of the installation process. This method is only called once
        per installation process, even for recursive installations (e.g. with the bundle installer).

        Args:
            result: The result of the installation.
            new_mod: If the installation succeeded (result is RESULT_SUCCESS), contains the newly
                installed mod, otherwise it contains a null pointer.
        """
        ...
    def onInstallationStart(
        self: IPluginInstaller,
        archive: str,
        reinstallation: bool,
        current_mod: IModInterface,
    ) -> None:
        """
        Method calls at the start of the installation process, before any other methods.
        This method is only called once per installation process, even for recursive
        installations (e.g. with the bundle installer).

        If `reinstallation` is true, then the given mod is the mod being reinstalled (the one
        selected by the user). If `reinstallation` is false and `currentMod` is not null, then
        it corresponds to a mod MO2 thinks corresponds to the archive (e.g. based on matching Nexus ID
        or name).

        The default implementation does nothing.

        Args:
            archive: Path to the archive that is going to be installed.
            reinstallation: True if this is a reinstallation, False otherwise.
            current_mod: A currently installed mod corresponding to the archive being installed, or None
                if there is no such mod.
        """
        ...
    @abc.abstractmethod
    def priority(self: IPluginInstaller) -> int:
        """
        Retrieve the priority of this installer.

        If multiple installers are able to handle an archive, the one with the highest priority wins.

        Returns:
            The priority of this installer.
        """
        ...
    def setInstallationManager(
        self: IPluginInstaller, manager: IInstallationManager
    ) -> None:
        """
        Set the installation manager for this installer.

        Python plugins usually do not need to re-implement this and can directly access the installation
        manager using `_manager()`.

        Args:
            manager: The installation manager.
        """
        ...
    def setParentWidget(
        self: IPluginInstaller, parent: PyQt6.QtWidgets.QWidget
    ) -> None:
        """
        Set the parent widget for this installer.

        Python plugins usually do not need to re-implement this and can directly access the parent
        widget using `_parentWidget()` once the UI has been initialized.

        Args:
            parent: The parent widget.
        """
        ...

class IPluginModPage(IPlugin):
    def __init__(self: IPluginModPage) -> None: ...
    def _parentWidget(self: IPluginModPage) -> PyQt6.QtWidgets.QWidget:
        """
        Returns:
            The parent widget.
        """
        ...
    @abc.abstractmethod
    def displayName(self: IPluginModPage) -> str:
        """
        Returns:
            The name of the page as displayed in the UI.
        """
        ...
    @abc.abstractmethod
    def handlesDownload(
        self: IPluginModPage,
        page_url: PyQt6.QtCore.QUrl,
        download_url: PyQt6.QtCore.QUrl,
        fileinfo: ModRepositoryFileInfo,
    ) -> bool:
        """
        Check if the plugin handles the specified download.

        Args:
            page_url: URL of the page that contains the download link.
            download_url: The download URL.
            fileinfo: Not usable in python.

        Returns:
            True if this plugin wants to handle the specified download, False otherwise.
        """
        ...
    @abc.abstractmethod
    def icon(self: IPluginModPage) -> PyQt6.QtGui.QIcon:
        """
        Returns:
            The icon to display with the page.
        """
        ...
    @abc.abstractmethod
    def pageURL(self: IPluginModPage) -> PyQt6.QtCore.QUrl:
        """
        Returns:
            The URL to open when the user wants to visit this mod page.
        """
        ...
    def setParentWidget(self: IPluginModPage, parent: PyQt6.QtWidgets.QWidget) -> None:
        """
        Set the parent widget for this mod page.

        Python plugins usually do not need to re-implement this and can directly access the parent
        widget using `_parentWidget()` once the UI has been initialized.

        Args:
            parent: The parent widget.
        """
        ...
    @abc.abstractmethod
    def useIntegratedBrowser(self: IPluginModPage) -> bool:
        """
        Indicates if the page should be displayed in the integrated browser.

        Unless the page provides a special means of starting downloads (like the nxm:// url schema
        on nexus),  it will not be possible to handle downloads unless the integrated browser is used!

        Returns:
            True if the page should be opened in the integrated browser, False otherwise.
        """
        ...

class IPluginPreview(IPlugin):
    """
    These plugins add support for previewing files in the data pane. Right now all image formats supported
    by qt are implemented (including dds) but no audio files and no 3d mesh formats.
    """

    def __init__(self: IPluginPreview) -> None: ...
    @abc.abstractmethod
    def genDataPreview(
        self: IPluginPreview,
        file_data: PyQt6.QtCore.QByteArray,
        filename: str,
        max_size: PyQt6.QtCore.QSize,
    ) -> PyQt6.QtWidgets.QWidget:
        """
        Generate a preview widget from in-memory data.

        Args:
            file_data: In-memory data to preview.
            filename: Name of the file the data comes from.
            max_size: Maximum size of the generated widget.

        Returns:
            The widget showing a preview of the in-memory data.
        """
        ...
    @abc.abstractmethod
    def genFilePreview(
        self: IPluginPreview, filename: str, max_size: PyQt6.QtCore.QSize
    ) -> PyQt6.QtWidgets.QWidget:
        """
        Generate a preview widget for the specified file.

        Args:
            filename: Path to the file to preview.
            max_size: Maximum size of the generated widget.

        Returns:
            The widget showing a preview of the file.
        """
        ...
    @abc.abstractmethod
    def supportedExtensions(self: IPluginPreview) -> set[str]:
        """
        Returns:
            The list of file extensions that are supported by this preview plugin.
        """
        ...
    @abc.abstractmethod
    def supportsArchives(self: IPluginPreview) -> bool:
        """
        Check if this preview plugin supports preview from in-memory data.

        Returns:
            True if the plugin supports preview from raw data, False otherwise.
        """
        ...

class IPluginTool(IPlugin):
    """
    This is the simplest of plugin interfaces. Such plugins simply place an icon inside the tools sub-menu
    and get invoked when the user clicks it. They are expected to have a user interface of some sort. These
    are almost like independent applications except they can access all Mod Organizer interfaces like querying
    and modifying the current profile, mod list, load order, use MO to install mods and so on. A tool plugin
    can (and should!) integrate its UI as a window inside MO and thus doesn't have to initialize a windows
    application itself.
    """

    def __init__(self: IPluginTool) -> None: ...
    def _parentWidget(self: IPluginTool) -> PyQt6.QtWidgets.QWidget:
        """
        Returns:
            The parent widget.
        """
        ...
    @abc.abstractmethod
    def display(self: IPluginTool) -> None:
        """
        Called when the user starts the tool.
        """
        ...
    @abc.abstractmethod
    def displayName(self: IPluginTool) -> str:
        """
        Returns:
            The display name for this tool, as shown in the tool menu.
        """
        ...
    @abc.abstractmethod
    def icon(self: IPluginTool) -> PyQt6.QtGui.QIcon:
        """
        Returns:
            The icon for this tool, or a default-constructed QICon().
        """
        ...
    def setParentWidget(self: IPluginTool, parent: PyQt6.QtWidgets.QWidget) -> None:
        """
        Set the parent widget for this tool.

        Python plugins usually do not need to re-implement this and can directly access the parent
        widget using `_parentWidget()` once the UI has been initialized.

        Args:
            parent: The parent widget.
        """
        ...
    @abc.abstractmethod
    def tooltip(self: IPluginTool) -> str:
        """
        Returns:
            The tooltip for this tool.
        """
        ...

class ISaveGameInfoWidget(PyQt6.QtWidgets.QWidget):
    """
    Base class for a save game info widget.
    """

    def __init__(
        self: ISaveGameInfoWidget, parent: PyQt6.QtWidgets.QWidget | None = None
    ) -> None:
        """
        Args:
            parent: Parent widget.
        """
        ...
    def __getattr__(self: ISaveGameInfoWidget, arg0: str) -> object: ...
    def _widget(self: ISaveGameInfoWidget) -> PyQt6.QtWidgets.QWidget:
        """
        Returns:
            The underlying `QWidget`.
        """
        ...
    @abc.abstractmethod
    def setSave(self: ISaveGameInfoWidget, save: ISaveGame) -> None:
        """
        Set the save file to display in this widget.

        Args:
            save: The save to display in the widget
        """
        ...

class IncompatibilityException(MO2Exception): ...
class InvalidNXMLinkException(MO2Exception): ...
class InvalidVersionException(MO2Exception): ...

class LocalSavegames(GameFeature):
    def __init__(self: LocalSavegames) -> None: ...
    @abc.abstractmethod
    def mappings(
        self: LocalSavegames, profile_save_dir: PyQt6.QtCore.QDir
    ) -> list[Mapping]: ...
    @abc.abstractmethod
    def prepareProfile(self: LocalSavegames, profile: IProfile) -> bool: ...

class ModDataChecker(GameFeature):
    """
    Game feature that is used to check the content of a data tree.
    """

    class CheckReturn(Enum):
        INVALID = ...
        FIXABLE = ...
        VALID = ...

        @property
        def value(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __eq__(self: ModDataChecker.CheckReturn, other: object) -> bool: ...
        def __int__(self: ModDataChecker.CheckReturn) -> int: ...
        def __ne__(self: ModDataChecker.CheckReturn, other: object) -> bool: ...
        def __str__(self: ModDataChecker.CheckReturn) -> str: ...

    FIXABLE: CheckReturn = ...
    INVALID: CheckReturn = ...
    VALID: CheckReturn = ...

    def __init__(self: ModDataChecker) -> None: ...
    @abc.abstractmethod
    def dataLooksValid(
        self: ModDataChecker, filetree: IFileTree
    ) -> ModDataChecker.CheckReturn:
        """
        Check that the given filetree represent a valid mod layout, or can be easily
        fixed.

        This method is mainly used during installation (to find which installer should
        be used or to recurse into multi-level archives), or to quickly indicates to a
        user if a mod looks valid.

        This method does not have to be exact, it only has to indicate if the given tree
        looks like a valid mod or not by quickly checking the structure (heavy operations
        should be avoided).

        If the tree can be fixed by the `fix()` method, this method should return `FIXABLE`.
        `FIXABLE` should only be returned when it is guaranteed that `fix()` can fix the tree.

        Args:
            filetree: The tree starting at the root of the "data" folder.

        Returns:
            Whether the tree is invalid, fixable or valid.
        """
        ...
    def fix(self: ModDataChecker, filetree: IFileTree) -> IFileTree | None:
        """
        Try to fix the given tree.

        This method is used during installation to try to fix invalid archives and will only be
        called if dataLooksValid returned `FIXABLE`.

        Args:
            filetree: The tree to try to fix. Can be modified during the process.

        Returns:
            The fixed tree, or a null pointer if the tree could not be fixed.
        """
        ...

class ModDataContent(GameFeature):
    """
    The ModDataContent feature is used (when available) to indicate to users the content
    of mods in the "Content" column.

    The feature exposes a list of possible content types, each associated with an ID, a name
    and an icon. The icon is the path to either:

      - A Qt resource or;
      - A file on the disk.

    In order to facilitate the implementation, MO2 already provides a set of icons that can
    be used. Those icons are all under ``:/MO/gui/content`` (e.g. ``:/MO/gui/content/plugin`` or ``:/MO/gui/content/music`` `).

    The list of available icons is:

      - ``plugin``: |plugin-icon|
      - ``skyproc``: |skyproc-icon|
      - ``texture``: |texture-icon|
      - ``music``: |music-icon|
      - ``sound``: |sound-icon|
      - ``interface``: |interface-icon|
      - ``skse``: |skse-icon|
      - ``script``: |script-icon|
      - ``mesh``: |mesh-icon|
      - ``string``: |string-icon|
      - ``bsa``: |bsa-icon|
      - ``menu``: |menu-icon|
      - ``inifile``: |inifile-icon|
      - ``modgroup``: |modgroup-icon|

    .. |plugin-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/jigsaw-piece.png
    .. |skyproc-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/hand-of-god.png
    .. |texture-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/empty-chessboard.png
    .. |music-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/double-quaver.png
    .. |sound-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/lyre.png
    .. |interface-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/usable.png
    .. |skse-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/checkbox-tree.png
    .. |script-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/tinker.png
    .. |mesh-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/breastplate.png
    .. |string-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/conversation.png
    .. |bsa-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/locked-chest.png
    .. |menu-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/config.png
    .. |inifile-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/feather-and-scroll.png
    .. |modgroup-icon| image:: https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/resources/contents/xedit.png
    """

    class Content:
        @property
        def icon(self) -> str: ...
        @property
        def id(self) -> int: ...
        @property
        def name(self) -> str: ...
        def __init__(
            self: ModDataContent.Content,
            id: int,
            name: str,
            icon: str,
            filter_only: bool = False,
        ) -> None:
            """
            Args:
                id: ID of this content.
                name: Name of this content.
                icon: Path to the icon for this content. Can be either a path
                    to an image on the disk, or to a resource. Can be an empty string if filterOnly
                    is true.
                filter_only: Indicates if the content should only be show in the filter
                    criteria and not in the actual Content column.
            """
            ...
        def isOnlyForFilter(self: ModDataContent.Content) -> bool:
            """
            Returns:
                True if this content is only meant to be used as a filter criteria.
            """
            ...

    def __init__(self: ModDataContent) -> None: ...
    @abc.abstractmethod
    def getAllContents(self: ModDataContent) -> list[ModDataContent.Content]:
        """
        Returns:
            The list of all possible contents for the corresponding game.
        """
        ...
    @abc.abstractmethod
    def getContentsFor(self: ModDataContent, filetree: IFileTree) -> list[int]:
        """
        Retrieve the list of contents in the given tree.

        Args:
            filetree: The tree corresponding to the mod to retrieve contents for.

        Returns:
            The IDs of the content in the given tree.
        """
        ...

class SaveGameInfo(GameFeature):
    """
    Feature to get hold of stuff to do with save games.
    """

    def __init__(self: SaveGameInfo) -> None: ...
    @abc.abstractmethod
    def getMissingAssets(
        self: SaveGameInfo, save: ISaveGame
    ) -> Dict[str, Sequence[str]]:
        """
        Retrieve missing assets from the save.

        Args:
            save: The save to find missing assets for.

        Returns:
            A collection of missing assets and the modules that can supply those assets.
        """
        ...
    @abc.abstractmethod
    def getSaveGameWidget(
        self: SaveGameInfo, parent: PyQt6.QtWidgets.QWidget
    ) -> ISaveGameInfoWidget | None:
        """
        Retrieve a widget to display over the save game list.

        This method is allowed to return `None` in case no widget has been implemented.

        Args:
            parent: The parent widget.

        Returns:
            A SaveGameInfoWidget to display information about save game.
        """
        ...

class ScriptExtender(GameFeature):
    def __init__(self: ScriptExtender) -> None: ...
    @abc.abstractmethod
    def binaryName(self: ScriptExtender) -> str:
        """
        Returns:
            The name of the script extender binary.
        """
        ...
    @abc.abstractmethod
    def getArch(self: ScriptExtender) -> int:
        """
        Returns:
            The CPU platform of the extender.
        """
        ...
    @abc.abstractmethod
    def getExtenderVersion(self: ScriptExtender) -> str:
        """
        Returns:
            The version of the script extender.
        """
        ...
    @abc.abstractmethod
    def isInstalled(self: ScriptExtender) -> bool:
        """
        Returns:
            True if the script extender is installed, False otherwise.
        """
        ...
    @abc.abstractmethod
    def loaderName(self: ScriptExtender) -> str:
        """
        Returns:
            The loader to use to ensure the game runs with the script extender.
        """
        ...
    @abc.abstractmethod
    def loaderPath(
        self: ScriptExtender,
    ) -> Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo]:
        """
        Returns:
            The full path to the script extender loader.
        """
        ...
    @abc.abstractmethod
    def pluginPath(
        self: ScriptExtender,
    ) -> Union[str, os.PathLike[str], PyQt6.QtCore.QDir]:
        """
        Returns:
            The script extender plugin path, relative to the data folder.
        """
        ...
    @abc.abstractmethod
    def savegameExtension(self: ScriptExtender) -> str:
        """
        Retrieve the extension of script extender save files.

        Returns:
            The extension of script extender save files (e.g. "skse").
        """
        ...

class UnmanagedMods(GameFeature):
    def __init__(self: UnmanagedMods) -> None: ...
    @abc.abstractmethod
    def displayName(self: UnmanagedMods, mod_name: str) -> str:
        """
        Retrieve the display name of a given mod.

        Args:
            mod_name: Internal name of the mod.

        Returns:
            The display name of the mod.
        """
        ...
    @abc.abstractmethod
    def mods(self: UnmanagedMods, official_only: bool) -> Sequence[str]:
        """
        Retrieve the list of unmanaged mods for the corresponding game.

        Args:
            official_only: Retrieve only unmanaged official mods.

        Returns:
            The list of unmanaged mods (internal names).
        """
        ...
    @abc.abstractmethod
    def referenceFile(
        self: UnmanagedMods, mod_name: str
    ) -> Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo]:
        """
        Retrieve the reference file for the requested mod.

        Example: For Bethesda games, the reference file may be the main
        plugin (esp or esm) for the game or a DLCs.

        Args:
            mod_name: Internal name of the mod.

        Returns:
            The reference file (absolute path) for the requested mod.
        """
        ...
    @abc.abstractmethod
    def secondaryFiles(
        self: UnmanagedMods, mod_name: str
    ) -> Sequence[Union[str, os.PathLike[str], PyQt6.QtCore.QFileInfo]]:
        """
        Retrieve the secondary files for the requested mod.

        Example: For Bethesda games, the secondary files may be the archives
        corresponding to the reference file.

        Args:
            mod_name: Internal name of the mod.

        Returns:
            The secondary files (absolute paths) for the request mod.
        """
        ...

class IPluginInstallerCustom(IPluginInstaller):
    """
    Custom installer for mods. Custom installers receive the archive name and have to go
    from there. They have to be able to extract the archive themselves.

    Example of such installers are the external NCC installer or the OMOD installer.
    """

    def __init__(self: IPluginInstallerCustom) -> None: ...
    @abc.abstractmethod
    def install(
        self: IPluginInstallerCustom,
        mod_name: GuessedString,
        game_name: str,
        archive_name: str,
        version: str,
        nexus_id: int,
    ) -> InstallResult:
        """
        Install the given archive.

        The mod needs to be created by calling `IOrganizer.createMod` first.

        Args:
            mod_name: Name of the mod to install. As an input parameter this is the suggested name
                (e.g. from meta data) The installer may change this parameter to rename the mod).
            game_name: Name of the game for which the mod is installed.
            archive_name: Name of the archive to install.
            version: Version of the mod. May be empty if the version is not yet known. The plugin is responsible
                for setting the version on the created mod.
            nexus_id: ID of the mod or -1 if unknown. The plugin is responsible for setting the mod ID for the
                created mod.

        Returns:
            The result of the installation process.
        """
        ...
    @overload
    @abc.abstractmethod
    def isArchiveSupported(self: IPluginInstaller, tree: IFileTree) -> bool:
        """
        Check if the given file tree corresponds to a supported archive for this installer.

        Args:
            tree: The tree representing the content of the archive.

        Returns:
            True if this installer can handle the archive, False otherwise.
        """
        ...
    @overload
    @abc.abstractmethod
    def isArchiveSupported(self: IPluginInstallerCustom, archive_name: str) -> bool:
        """
        Check if the given file is a supported archive for this installer.

        Args:
            archive_name: Name of the archive.

        Returns:
            True if this installer can handle the archive, False otherwise.
        """
        ...
    @abc.abstractmethod
    def supportedExtensions(self: IPluginInstallerCustom) -> set[str]:
        """
        Returns:
            A list of file extensions that this installer can handle.
        """
        ...

class IPluginInstallerSimple(IPluginInstaller):
    """
    Simple installer for mods. Simple installers only deal with an in-memory structure
    representing the archive and can modify what to install and where by editing this structure.
    Actually extracting the archive is handled by the manager.
    """

    def __init__(self: IPluginInstallerSimple) -> None: ...
    @abc.abstractmethod
    def install(
        self: IPluginInstallerSimple,
        name: GuessedString,
        tree: IFileTree,
        version: str,
        nexus_id: int,
    ) -> Union[InstallResult, IFileTree, tuple[InstallResult, IFileTree, str, int]]:
        """
        Install a mod from an archive filetree.

        The installer can modify the given tree and use the manager to extract or create new
        files.

        This method returns different type of objects depending on the actual result of the
        installation. The C++ bindings for this method always returns a tuple (result, tree,
        version, id).

        Args:
            name: Name of the mod to install. As an input parameter this is the suggested name
                (e.g. from meta data) The installer may change this parameter to rename the mod).
            tree: In-memory representation of the archive content.
            version: Version of the mod, or an empty string is unknown.
            nexus_id: ID of the mod, or -1 if unknown.

        Returns:
            In case of failure, the result of the installation, otherwise the modified tree or
        a tuple (result, tree, version, id) containing the result of the installation, the
        modified tree, the new version and the new ID. The tuple can be returned even if the
        installation did not succeed.
        """
        ...
