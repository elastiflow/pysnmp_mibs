# SNMP MIB module (TN-CLEAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-CLEAR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")

(tnEventAppIndex,) = mibBuilder.importSymbols(
    "TN-LOG-MIB",
    "tnEventAppIndex")

(TNamedItem,
 TmnxActionType) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TNamedItem",
    "TmnxActionType")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnClearMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 13)
)
if mibBuilder.loadTexts:
    tnClearMIBModule.setRevisions(
        ("1905-01-24 00:00",
         "1904-06-02 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1902-02-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnClearObjs_ObjectIdentity = ObjectIdentity
tnClearObjs = _TnClearObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13)
)
_TnClearTable_Object = MibTable
tnClearTable = _TnClearTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    tnClearTable.setStatus("current")
_TnClearEntry_Object = MibTableRow
tnClearEntry = _TnClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1)
)
tnClearEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LOG-MIB", "tnEventAppIndex"),
    (0, "TN-CLEAR-MIB", "tnClearIndex"),
)
if mibBuilder.loadTexts:
    tnClearEntry.setStatus("current")


class _TnClearIndex_Type(Integer32):
    """Custom type tnClearIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnClearIndex_Type.__name__ = "Integer32"
_TnClearIndex_Object = MibTableColumn
tnClearIndex = _TnClearIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1, 1),
    _TnClearIndex_Type()
)
tnClearIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnClearIndex.setStatus("current")
_TnClearName_Type = TNamedItem
_TnClearName_Object = MibTableColumn
tnClearName = _TnClearName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1, 2),
    _TnClearName_Type()
)
tnClearName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnClearName.setStatus("current")


class _TnClearParams_Type(OctetString):
    """Custom type tnClearParams based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnClearParams_Type.__name__ = "OctetString"
_TnClearParams_Object = MibTableColumn
tnClearParams = _TnClearParams_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1, 3),
    _TnClearParams_Type()
)
tnClearParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnClearParams.setStatus("current")


class _TnClearAction_Type(TmnxActionType):
    """Custom type tnClearAction based on TmnxActionType"""
    defaultValue = 2


_TnClearAction_Type.__name__ = "TmnxActionType"
_TnClearAction_Object = MibTableColumn
tnClearAction = _TnClearAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1, 4),
    _TnClearAction_Type()
)
tnClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnClearAction.setStatus("current")
_TnClearLastClearedTime_Type = TimeStamp
_TnClearLastClearedTime_Object = MibTableColumn
tnClearLastClearedTime = _TnClearLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1, 5),
    _TnClearLastClearedTime_Type()
)
tnClearLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnClearLastClearedTime.setStatus("current")


class _TnClearResult_Type(Integer32):
    """Custom type tnClearResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_TnClearResult_Type.__name__ = "Integer32"
_TnClearResult_Object = MibTableColumn
tnClearResult = _TnClearResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1, 6),
    _TnClearResult_Type()
)
tnClearResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnClearResult.setStatus("current")


class _TnClearErrorText_Type(OctetString):
    """Custom type tnClearErrorText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnClearErrorText_Type.__name__ = "OctetString"
_TnClearErrorText_Object = MibTableColumn
tnClearErrorText = _TnClearErrorText_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 1, 1, 7),
    _TnClearErrorText_Type()
)
tnClearErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnClearErrorText.setStatus("current")
_TnClearScalar1_Type = Unsigned32
_TnClearScalar1_Object = MibScalar
tnClearScalar1 = _TnClearScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 101),
    _TnClearScalar1_Type()
)
tnClearScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnClearScalar1.setStatus("current")
_TnClearScalar2_Type = Unsigned32
_TnClearScalar2_Object = MibScalar
tnClearScalar2 = _TnClearScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 13, 102),
    _TnClearScalar2_Type()
)
tnClearScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnClearScalar2.setStatus("current")
_TnClearNotificationsPrefix_ObjectIdentity = ObjectIdentity
tnClearNotificationsPrefix = _TnClearNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 13)
)
_TnClearNotifications_ObjectIdentity = ObjectIdentity
tnClearNotifications = _TnClearNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 13, 0)
)

# Managed Objects groups


# Notification objects

tnClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 13, 0, 1)
)
tnClear.setObjects(
      *(("TN-CLEAR-MIB", "tnClearName"),
        ("TN-CLEAR-MIB", "tnClearParams"),
        ("TN-CLEAR-MIB", "tnClearLastClearedTime"),
        ("TN-CLEAR-MIB", "tnClearResult"),
        ("TN-CLEAR-MIB", "tnClearErrorText"))
)
if mibBuilder.loadTexts:
    tnClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-CLEAR-MIB",
    **{"tnClearMIBModule": tnClearMIBModule,
       "tnClearObjs": tnClearObjs,
       "tnClearTable": tnClearTable,
       "tnClearEntry": tnClearEntry,
       "tnClearIndex": tnClearIndex,
       "tnClearName": tnClearName,
       "tnClearParams": tnClearParams,
       "tnClearAction": tnClearAction,
       "tnClearLastClearedTime": tnClearLastClearedTime,
       "tnClearResult": tnClearResult,
       "tnClearErrorText": tnClearErrorText,
       "tnClearScalar1": tnClearScalar1,
       "tnClearScalar2": tnClearScalar2,
       "tnClearNotificationsPrefix": tnClearNotificationsPrefix,
       "tnClearNotifications": tnClearNotifications,
       "tnClear": tnClear}
)
