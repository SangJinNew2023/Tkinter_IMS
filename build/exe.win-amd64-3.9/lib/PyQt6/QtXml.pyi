# The PEP 484 type hints stub file for the QtXml module.
#
# Generated by SIP 6.7.10
#
# Copyright (c) 2023 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]


class QDomImplementation(PyQt6.sip.simplewrapper):

    class InvalidDataPolicy(enum.Enum):
        AcceptInvalidChars = ... # type: QDomImplementation.InvalidDataPolicy
        DropInvalidChars = ... # type: QDomImplementation.InvalidDataPolicy
        ReturnNullNode = ... # type: QDomImplementation.InvalidDataPolicy

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomImplementation') -> None: ...

    def isNull(self) -> bool: ...
    @staticmethod
    def setInvalidDataPolicy(policy: 'QDomImplementation.InvalidDataPolicy') -> None: ...
    @staticmethod
    def invalidDataPolicy() -> 'QDomImplementation.InvalidDataPolicy': ...
    def createDocument(self, nsURI: typing.Optional[str], qName: typing.Optional[str], doctype: 'QDomDocumentType') -> 'QDomDocument': ...
    def createDocumentType(self, qName: typing.Optional[str], publicId: typing.Optional[str], systemId: typing.Optional[str]) -> 'QDomDocumentType': ...
    def hasFeature(self, feature: typing.Optional[str], version: typing.Optional[str]) -> bool: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomNode(PyQt6.sip.simplewrapper):

    class EncodingPolicy(enum.Enum):
        EncodingFromDocument = ... # type: QDomNode.EncodingPolicy
        EncodingFromTextStream = ... # type: QDomNode.EncodingPolicy

    class NodeType(enum.Enum):
        ElementNode = ... # type: QDomNode.NodeType
        AttributeNode = ... # type: QDomNode.NodeType
        TextNode = ... # type: QDomNode.NodeType
        CDATASectionNode = ... # type: QDomNode.NodeType
        EntityReferenceNode = ... # type: QDomNode.NodeType
        EntityNode = ... # type: QDomNode.NodeType
        ProcessingInstructionNode = ... # type: QDomNode.NodeType
        CommentNode = ... # type: QDomNode.NodeType
        DocumentNode = ... # type: QDomNode.NodeType
        DocumentTypeNode = ... # type: QDomNode.NodeType
        DocumentFragmentNode = ... # type: QDomNode.NodeType
        NotationNode = ... # type: QDomNode.NodeType
        BaseNode = ... # type: QDomNode.NodeType
        CharacterDataNode = ... # type: QDomNode.NodeType

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNode') -> None: ...

    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...
    def nextSiblingElement(self, taName: typing.Optional[str] = ..., namespaceURI: typing.Optional[str] = ...) -> 'QDomElement': ...
    def previousSiblingElement(self, tagName: typing.Optional[str] = ..., namespaceURI: typing.Optional[str] = ...) -> 'QDomElement': ...
    def lastChildElement(self, tagName: typing.Optional[str] = ..., namespaceURI: typing.Optional[str] = ...) -> 'QDomElement': ...
    def firstChildElement(self, tagName: typing.Optional[str] = ..., namespaceURI: typing.Optional[str] = ...) -> 'QDomElement': ...
    def save(self, a0: QtCore.QTextStream, a1: int, a2: 'QDomNode.EncodingPolicy' = ...) -> None: ...
    def toComment(self) -> 'QDomComment': ...
    def toCharacterData(self) -> 'QDomCharacterData': ...
    def toProcessingInstruction(self) -> 'QDomProcessingInstruction': ...
    def toNotation(self) -> 'QDomNotation': ...
    def toEntity(self) -> 'QDomEntity': ...
    def toText(self) -> 'QDomText': ...
    def toEntityReference(self) -> 'QDomEntityReference': ...
    def toElement(self) -> 'QDomElement': ...
    def toDocumentType(self) -> 'QDomDocumentType': ...
    def toDocument(self) -> 'QDomDocument': ...
    def toDocumentFragment(self) -> 'QDomDocumentFragment': ...
    def toCDATASection(self) -> 'QDomCDATASection': ...
    def toAttr(self) -> 'QDomAttr': ...
    def clear(self) -> None: ...
    def isNull(self) -> bool: ...
    def namedItem(self, name: typing.Optional[str]) -> 'QDomNode': ...
    def isComment(self) -> bool: ...
    def isCharacterData(self) -> bool: ...
    def isProcessingInstruction(self) -> bool: ...
    def isNotation(self) -> bool: ...
    def isEntity(self) -> bool: ...
    def isText(self) -> bool: ...
    def isEntityReference(self) -> bool: ...
    def isElement(self) -> bool: ...
    def isDocumentType(self) -> bool: ...
    def isDocument(self) -> bool: ...
    def isDocumentFragment(self) -> bool: ...
    def isCDATASection(self) -> bool: ...
    def isAttr(self) -> bool: ...
    def setPrefix(self, pre: typing.Optional[str]) -> None: ...
    def prefix(self) -> str: ...
    def setNodeValue(self, a0: typing.Optional[str]) -> None: ...
    def nodeValue(self) -> str: ...
    def hasAttributes(self) -> bool: ...
    def localName(self) -> str: ...
    def namespaceURI(self) -> str: ...
    def ownerDocument(self) -> 'QDomDocument': ...
    def attributes(self) -> 'QDomNamedNodeMap': ...
    def nextSibling(self) -> 'QDomNode': ...
    def previousSibling(self) -> 'QDomNode': ...
    def lastChild(self) -> 'QDomNode': ...
    def firstChild(self) -> 'QDomNode': ...
    def childNodes(self) -> 'QDomNodeList': ...
    def parentNode(self) -> 'QDomNode': ...
    def nodeType(self) -> 'QDomNode.NodeType': ...
    def nodeName(self) -> str: ...
    def isSupported(self, feature: typing.Optional[str], version: typing.Optional[str]) -> bool: ...
    def normalize(self) -> None: ...
    def cloneNode(self, deep: bool = ...) -> 'QDomNode': ...
    def hasChildNodes(self) -> bool: ...
    def appendChild(self, newChild: 'QDomNode') -> 'QDomNode': ...
    def removeChild(self, oldChild: 'QDomNode') -> 'QDomNode': ...
    def replaceChild(self, newChild: 'QDomNode', oldChild: 'QDomNode') -> 'QDomNode': ...
    def insertAfter(self, newChild: 'QDomNode', refChild: 'QDomNode') -> 'QDomNode': ...
    def insertBefore(self, newChild: 'QDomNode', refChild: 'QDomNode') -> 'QDomNode': ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomNodeList(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNodeList') -> None: ...

    def isEmpty(self) -> bool: ...
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def length(self) -> int: ...
    def at(self, index: int) -> QDomNode: ...
    def item(self, index: int) -> QDomNode: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomDocumentType(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocumentType') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def internalSubset(self) -> str: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...
    def notations(self) -> 'QDomNamedNodeMap': ...
    def entities(self) -> 'QDomNamedNodeMap': ...
    def name(self) -> str: ...


class QDomDocument(QDomNode):

    class ParseOption(enum.Enum):
        Default = ... # type: QDomDocument.ParseOption
        UseNamespaceProcessing = ... # type: QDomDocument.ParseOption
        PreserveSpacingOnlyNodes = ... # type: QDomDocument.ParseOption

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: typing.Optional[str]) -> None: ...
    @typing.overload
    def __init__(self, doctype: QDomDocumentType) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocument') -> None: ...

    def toByteArray(self, indent: int = ...) -> QtCore.QByteArray: ...
    def toString(self, indent: int = ...) -> str: ...
    @typing.overload
    def setContent(self, reader: typing.Optional[QtCore.QXmlStreamReader], options: 'QDomDocument.ParseOption' = ...) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, device: typing.Optional[QtCore.QIODevice], options: 'QDomDocument.ParseOption' = ...) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray, memoryview, typing.Optional[str]], options: 'QDomDocument.ParseOption' = ...) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, text: typing.Union[QtCore.QByteArray, bytes, bytearray, memoryview], namespaceProcessing: bool) -> typing.Tuple[bool, typing.Optional[str], typing.Optional[int], typing.Optional[int]]: ...
    @typing.overload
    def setContent(self, text: typing.Optional[str], namespaceProcessing: bool) -> typing.Tuple[bool, typing.Optional[str], typing.Optional[int], typing.Optional[int]]: ...
    @typing.overload
    def setContent(self, dev: typing.Optional[QtCore.QIODevice], namespaceProcessing: bool) -> typing.Tuple[bool, typing.Optional[str], typing.Optional[int], typing.Optional[int]]: ...
    @typing.overload
    def setContent(self, reader: typing.Optional[QtCore.QXmlStreamReader], namespaceProcessing: bool) -> typing.Tuple[bool, typing.Optional[str], typing.Optional[int], typing.Optional[int]]: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def documentElement(self) -> 'QDomElement': ...
    def implementation(self) -> QDomImplementation: ...
    def doctype(self) -> QDomDocumentType: ...
    def elementById(self, elementId: typing.Optional[str]) -> 'QDomElement': ...
    def elementsByTagNameNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str]) -> QDomNodeList: ...
    def createAttributeNS(self, nsURI: typing.Optional[str], qName: typing.Optional[str]) -> 'QDomAttr': ...
    def createElementNS(self, nsURI: typing.Optional[str], qName: typing.Optional[str]) -> 'QDomElement': ...
    def importNode(self, importedNode: QDomNode, deep: bool) -> QDomNode: ...
    def elementsByTagName(self, tagname: typing.Optional[str]) -> QDomNodeList: ...
    def createEntityReference(self, name: typing.Optional[str]) -> 'QDomEntityReference': ...
    def createAttribute(self, name: typing.Optional[str]) -> 'QDomAttr': ...
    def createProcessingInstruction(self, target: typing.Optional[str], data: typing.Optional[str]) -> 'QDomProcessingInstruction': ...
    def createCDATASection(self, data: typing.Optional[str]) -> 'QDomCDATASection': ...
    def createComment(self, data: typing.Optional[str]) -> 'QDomComment': ...
    def createTextNode(self, data: typing.Optional[str]) -> 'QDomText': ...
    def createDocumentFragment(self) -> 'QDomDocumentFragment': ...
    def createElement(self, tagName: typing.Optional[str]) -> 'QDomElement': ...


class QDomNamedNodeMap(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNamedNodeMap') -> None: ...

    def contains(self, name: typing.Optional[str]) -> bool: ...
    def isEmpty(self) -> bool: ...
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def length(self) -> int: ...
    def removeNamedItemNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str]) -> QDomNode: ...
    def setNamedItemNS(self, newNode: QDomNode) -> QDomNode: ...
    def namedItemNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str]) -> QDomNode: ...
    def item(self, index: int) -> QDomNode: ...
    def removeNamedItem(self, name: typing.Optional[str]) -> QDomNode: ...
    def setNamedItem(self, newNode: QDomNode) -> QDomNode: ...
    def namedItem(self, name: typing.Optional[str]) -> QDomNode: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomDocumentFragment(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocumentFragment') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomCharacterData(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomCharacterData') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setData(self, a0: typing.Optional[str]) -> None: ...
    def data(self) -> str: ...
    def length(self) -> int: ...
    def replaceData(self, offset: int, count: int, arg: typing.Optional[str]) -> None: ...
    def deleteData(self, offset: int, count: int) -> None: ...
    def insertData(self, offset: int, arg: typing.Optional[str]) -> None: ...
    def appendData(self, arg: typing.Optional[str]) -> None: ...
    def substringData(self, offset: int, count: int) -> str: ...


class QDomAttr(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomAttr') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setValue(self, a0: typing.Optional[str]) -> None: ...
    def value(self) -> str: ...
    def ownerElement(self) -> 'QDomElement': ...
    def specified(self) -> bool: ...
    def name(self) -> str: ...


class QDomElement(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomElement') -> None: ...

    def text(self) -> str: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def attributes(self) -> QDomNamedNodeMap: ...
    def setTagName(self, name: typing.Optional[str]) -> None: ...
    def tagName(self) -> str: ...
    def hasAttributeNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str]) -> bool: ...
    def elementsByTagNameNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str]) -> QDomNodeList: ...
    def setAttributeNodeNS(self, newAttr: QDomAttr) -> QDomAttr: ...
    def attributeNodeNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str]) -> QDomAttr: ...
    def removeAttributeNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str]) -> None: ...
    @typing.overload
    def setAttributeNS(self, nsURI: typing.Optional[str], qName: typing.Optional[str], value: typing.Optional[str]) -> None: ...
    @typing.overload
    def setAttributeNS(self, nsURI: typing.Optional[str], qName: typing.Optional[str], value: float) -> None: ...
    @typing.overload
    def setAttributeNS(self, nsURI: typing.Optional[str], qName: typing.Optional[str], value: int) -> None: ...
    def attributeNS(self, nsURI: typing.Optional[str], localName: typing.Optional[str], defaultValue: typing.Optional[str] = ...) -> str: ...
    def hasAttribute(self, name: typing.Optional[str]) -> bool: ...
    def elementsByTagName(self, tagname: typing.Optional[str]) -> QDomNodeList: ...
    def removeAttributeNode(self, oldAttr: QDomAttr) -> QDomAttr: ...
    def setAttributeNode(self, newAttr: QDomAttr) -> QDomAttr: ...
    def attributeNode(self, name: typing.Optional[str]) -> QDomAttr: ...
    def removeAttribute(self, name: typing.Optional[str]) -> None: ...
    @typing.overload
    def setAttribute(self, name: typing.Optional[str], value: typing.Optional[str]) -> None: ...
    @typing.overload
    def setAttribute(self, name: typing.Optional[str], value: int) -> None: ...
    @typing.overload
    def setAttribute(self, name: typing.Optional[str], value: int) -> None: ...
    @typing.overload
    def setAttribute(self, name: typing.Optional[str], value: float) -> None: ...
    @typing.overload
    def setAttribute(self, name: typing.Optional[str], value: int) -> None: ...
    def attribute(self, name: typing.Optional[str], defaultValue: typing.Optional[str] = ...) -> str: ...


class QDomText(QDomCharacterData):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomText') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def splitText(self, offset: int) -> 'QDomText': ...


class QDomComment(QDomCharacterData):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomComment') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomCDATASection(QDomText):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomCDATASection') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomNotation(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomNotation') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...


class QDomEntity(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomEntity') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def notationName(self) -> str: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...


class QDomEntityReference(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomEntityReference') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomProcessingInstruction(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomProcessingInstruction') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setData(self, d: typing.Optional[str]) -> None: ...
    def data(self) -> str: ...
    def target(self) -> str: ...
