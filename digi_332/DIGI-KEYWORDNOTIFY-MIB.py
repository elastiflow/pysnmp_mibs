# SNMP MIB module (DIGI-KEYWORDNOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-KEYWORDNOTIFY-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(digiKeywordNotify,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiKeywordNotify")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NotifyTable_Object = MibTable
notifyTable = _NotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12)
)
if mibBuilder.loadTexts:
    notifyTable.setStatus("mandatory")
_NotifyEntry_Object = MibTableRow
notifyEntry = _NotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1)
)
notifyEntry.setIndexNames(
    (0, "DIGI-KEYWORDNOTIFY-MIB", "notifyIndex"),
)
if mibBuilder.loadTexts:
    notifyEntry.setStatus("mandatory")
_NotifyIndex_Type = Integer32
_NotifyIndex_Object = MibTableColumn
notifyIndex = _NotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1, 11),
    _NotifyIndex_Type()
)
notifyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyIndex.setStatus("mandatory")
_NotifyTitle_Type = DisplayString
_NotifyTitle_Object = MibTableColumn
notifyTitle = _NotifyTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1, 12),
    _NotifyTitle_Type()
)
notifyTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyTitle.setStatus("mandatory")
_NotifyPort_Type = Integer32
_NotifyPort_Object = MibTableColumn
notifyPort = _NotifyPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1, 13),
    _NotifyPort_Type()
)
notifyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyPort.setStatus("mandatory")
_NotifyMessage_Type = DisplayString
_NotifyMessage_Object = MibTableColumn
notifyMessage = _NotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1, 14),
    _NotifyMessage_Type()
)
notifyMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyMessage.setStatus("mandatory")
_NotifyPortTitle_Type = DisplayString
_NotifyPortTitle_Object = MibTableColumn
notifyPortTitle = _NotifyPortTitle_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1, 15),
    _NotifyPortTitle_Type()
)
notifyPortTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyPortTitle.setStatus("mandatory")
_NotifyPortAccessPort_Type = Integer32
_NotifyPortAccessPort_Object = MibTableColumn
notifyPortAccessPort = _NotifyPortAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1, 16),
    _NotifyPortAccessPort_Type()
)
notifyPortAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyPortAccessPort.setStatus("mandatory")
_NotifyPortProtocol_Type = DisplayString
_NotifyPortProtocol_Object = MibTableColumn
notifyPortProtocol = _NotifyPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 12, 1, 17),
    _NotifyPortProtocol_Type()
)
notifyPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyPortProtocol.setStatus("mandatory")

# Managed Objects groups


# Notification objects

keywordMatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 0, 1)
)
keywordMatched.setObjects(
      *(("DIGI-KEYWORDNOTIFY-MIB", "notifyTitle"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPort"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyMessage"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPortTitle"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPortAccessPort"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPortProtocol"))
)
if mibBuilder.loadTexts:
    keywordMatched.setStatus(
        ""
    )

keywordMatchedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12, 1)
)
keywordMatchedNotification.setObjects(
      *(("DIGI-KEYWORDNOTIFY-MIB", "notifyTitle"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPort"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyMessage"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPortTitle"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPortAccessPort"),
        ("DIGI-KEYWORDNOTIFY-MIB", "notifyPortProtocol"))
)
if mibBuilder.loadTexts:
    keywordMatchedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-KEYWORDNOTIFY-MIB",
    **{"DisplayString": DisplayString,
       "keywordMatched": keywordMatched,
       "keywordMatchedNotification": keywordMatchedNotification,
       "notifyTable": notifyTable,
       "notifyEntry": notifyEntry,
       "notifyIndex": notifyIndex,
       "notifyTitle": notifyTitle,
       "notifyPort": notifyPort,
       "notifyMessage": notifyMessage,
       "notifyPortTitle": notifyPortTitle,
       "notifyPortAccessPort": notifyPortAccessPort,
       "notifyPortProtocol": notifyPortProtocol}
)
