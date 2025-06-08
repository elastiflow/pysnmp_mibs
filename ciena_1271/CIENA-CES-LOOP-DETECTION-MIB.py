# SNMP MIB module (CIENA-CES-LOOP-DETECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-CES-LOOP-DETECTION-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:46 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications,
 cienaCesStatistics) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications",
    "cienaCesStatistics")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesLoopDetectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50)
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionMIB.setRevisions(
        ("2018-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesLoopDetectionMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesLoopDetectionMIBObjects = _CienaCesLoopDetectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1)
)
_CienaCesLoopDetection_ObjectIdentity = ObjectIdentity
cienaCesLoopDetection = _CienaCesLoopDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1)
)
_CienaCesLoopDetectionAdminStatus_Type = CienaGlobalState
_CienaCesLoopDetectionAdminStatus_Object = MibScalar
cienaCesLoopDetectionAdminStatus = _CienaCesLoopDetectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 1),
    _CienaCesLoopDetectionAdminStatus_Type()
)
cienaCesLoopDetectionAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionAdminStatus.setStatus("current")
_CienaCesLoopDetectionPortTable_Object = MibTable
cienaCesLoopDetectionPortTable = _CienaCesLoopDetectionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortTable.setStatus("current")
_CienaCesLoopDetectionPortEntry_Object = MibTableRow
cienaCesLoopDetectionPortEntry = _CienaCesLoopDetectionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1)
)
cienaCesLoopDetectionPortEntry.setIndexNames(
    (0, "CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionPortId"),
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortEntry.setStatus("current")


class _CienaCesLoopDetectionPortId_Type(Integer32):
    """Custom type cienaCesLoopDetectionPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesLoopDetectionPortId_Type.__name__ = "Integer32"
_CienaCesLoopDetectionPortId_Object = MibTableColumn
cienaCesLoopDetectionPortId = _CienaCesLoopDetectionPortId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 1),
    _CienaCesLoopDetectionPortId_Type()
)
cienaCesLoopDetectionPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortId.setStatus("current")


class _CienaCesLoopDetectionPortName_Type(DisplayString):
    """Custom type cienaCesLoopDetectionPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesLoopDetectionPortName_Type.__name__ = "DisplayString"
_CienaCesLoopDetectionPortName_Object = MibTableColumn
cienaCesLoopDetectionPortName = _CienaCesLoopDetectionPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 2),
    _CienaCesLoopDetectionPortName_Type()
)
cienaCesLoopDetectionPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortName.setStatus("current")


class _CienaCesLoopDetectionPortAdminStatus_Type(Integer32):
    """Custom type cienaCesLoopDetectionPortAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesLoopDetectionPortAdminStatus_Type.__name__ = "Integer32"
_CienaCesLoopDetectionPortAdminStatus_Object = MibTableColumn
cienaCesLoopDetectionPortAdminStatus = _CienaCesLoopDetectionPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 3),
    _CienaCesLoopDetectionPortAdminStatus_Type()
)
cienaCesLoopDetectionPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortAdminStatus.setStatus("current")


class _CienaCesLoopDetectionPortAction_Type(Integer32):
    """Custom type cienaCesLoopDetectionPortAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g8032", 1),
          ("portshut", 2),
          ("notify", 3))
    )


_CienaCesLoopDetectionPortAction_Type.__name__ = "Integer32"
_CienaCesLoopDetectionPortAction_Object = MibTableColumn
cienaCesLoopDetectionPortAction = _CienaCesLoopDetectionPortAction_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 4),
    _CienaCesLoopDetectionPortAction_Type()
)
cienaCesLoopDetectionPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortAction.setStatus("current")


class _CienaCesLoopDetectionPortRevertiveMode_Type(Integer32):
    """Custom type cienaCesLoopDetectionPortRevertiveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CienaCesLoopDetectionPortRevertiveMode_Type.__name__ = "Integer32"
_CienaCesLoopDetectionPortRevertiveMode_Object = MibTableColumn
cienaCesLoopDetectionPortRevertiveMode = _CienaCesLoopDetectionPortRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 5),
    _CienaCesLoopDetectionPortRevertiveMode_Type()
)
cienaCesLoopDetectionPortRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortRevertiveMode.setStatus("current")


class _CienaCesLoopDetectionPortOperState_Type(Integer32):
    """Custom type cienaCesLoopDetectionPortOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesLoopDetectionPortOperState_Type.__name__ = "Integer32"
_CienaCesLoopDetectionPortOperState_Object = MibTableColumn
cienaCesLoopDetectionPortOperState = _CienaCesLoopDetectionPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 6),
    _CienaCesLoopDetectionPortOperState_Type()
)
cienaCesLoopDetectionPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortOperState.setStatus("current")


class _CienaCesLoopDetectionPortLoopStatus_Type(Integer32):
    """Custom type cienaCesLoopDetectionPortLoopStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CienaCesLoopDetectionPortLoopStatus_Type.__name__ = "Integer32"
_CienaCesLoopDetectionPortLoopStatus_Object = MibTableColumn
cienaCesLoopDetectionPortLoopStatus = _CienaCesLoopDetectionPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 7),
    _CienaCesLoopDetectionPortLoopStatus_Type()
)
cienaCesLoopDetectionPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortLoopStatus.setStatus("current")
_CienaCesLoopDetectionPortLoopOccurence_Type = Counter32
_CienaCesLoopDetectionPortLoopOccurence_Object = MibTableColumn
cienaCesLoopDetectionPortLoopOccurence = _CienaCesLoopDetectionPortLoopOccurence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 8),
    _CienaCesLoopDetectionPortLoopOccurence_Type()
)
cienaCesLoopDetectionPortLoopOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortLoopOccurence.setStatus("current")


class _CienaCesLoopDetectionHoldOffTime_Type(Integer32):
    """Custom type cienaCesLoopDetectionHoldOffTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CienaCesLoopDetectionHoldOffTime_Type.__name__ = "Integer32"
_CienaCesLoopDetectionHoldOffTime_Object = MibTableColumn
cienaCesLoopDetectionHoldOffTime = _CienaCesLoopDetectionHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 2, 1, 9),
    _CienaCesLoopDetectionHoldOffTime_Type()
)
cienaCesLoopDetectionHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionHoldOffTime.setUnits("milliseconds")
_CienaCesLoopDetectionPortCfmServiceTable_Object = MibTable
cienaCesLoopDetectionPortCfmServiceTable = _CienaCesLoopDetectionPortCfmServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortCfmServiceTable.setStatus("current")
_CienaCesLoopDetectionPortCfmServiceEntry_Object = MibTableRow
cienaCesLoopDetectionPortCfmServiceEntry = _CienaCesLoopDetectionPortCfmServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 3, 1)
)
cienaCesLoopDetectionPortCfmServiceEntry.setIndexNames(
    (0, "CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionPortId"),
    (0, "CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionCfmServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortCfmServiceEntry.setStatus("current")
_CienaCesLoopDetectionCfmServiceIndex_Type = Unsigned32
_CienaCesLoopDetectionCfmServiceIndex_Object = MibTableColumn
cienaCesLoopDetectionCfmServiceIndex = _CienaCesLoopDetectionCfmServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 1, 1, 3, 1, 1),
    _CienaCesLoopDetectionCfmServiceIndex_Type()
)
cienaCesLoopDetectionCfmServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLoopDetectionCfmServiceIndex.setStatus("current")
_CienaCesLoopDetectionMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesLoopDetectionMIBNotificationPrefix = _CienaCesLoopDetectionMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 2)
)
_CienaCesLoopDetectionMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesLoopDetectionMIBNotifications = _CienaCesLoopDetectionMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 2, 0)
)
_CienaCesLoopDetectionMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesLoopDetectionMIBConformance = _CienaCesLoopDetectionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 3)
)
_CienaCesLoopDetectionMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesLoopDetectionMIBCompliances = _CienaCesLoopDetectionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 3, 1)
)
_CienaCesLoopDetectionMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesLoopDetectionMIBGroups = _CienaCesLoopDetectionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 3, 2)
)

# Managed Objects groups


# Notification objects

cienaCesLoopDetectionLoopFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 2, 0, 1)
)
cienaCesLoopDetectionLoopFound.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionCfmServiceIndex"),
        ("CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionPortName"))
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionLoopFound.setStatus(
        "current"
    )

cienaCesLoopDetectionLoopClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 2, 0, 2)
)
cienaCesLoopDetectionLoopClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionCfmServiceIndex"),
        ("CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionPortName"))
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionLoopClear.setStatus(
        "current"
    )

cienaCesLoopDetectionPortOperActionSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 2, 0, 3)
)
cienaCesLoopDetectionPortOperActionSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionPortName"))
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortOperActionSet.setStatus(
        "current"
    )

cienaCesLoopDetectionPortOperActionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 50, 2, 0, 4)
)
cienaCesLoopDetectionPortOperActionClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-LOOP-DETECTION-MIB", "cienaCesLoopDetectionPortName"))
)
if mibBuilder.loadTexts:
    cienaCesLoopDetectionPortOperActionClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-LOOP-DETECTION-MIB",
    **{"cienaCesLoopDetectionMIB": cienaCesLoopDetectionMIB,
       "cienaCesLoopDetectionMIBObjects": cienaCesLoopDetectionMIBObjects,
       "cienaCesLoopDetection": cienaCesLoopDetection,
       "cienaCesLoopDetectionAdminStatus": cienaCesLoopDetectionAdminStatus,
       "cienaCesLoopDetectionPortTable": cienaCesLoopDetectionPortTable,
       "cienaCesLoopDetectionPortEntry": cienaCesLoopDetectionPortEntry,
       "cienaCesLoopDetectionPortId": cienaCesLoopDetectionPortId,
       "cienaCesLoopDetectionPortName": cienaCesLoopDetectionPortName,
       "cienaCesLoopDetectionPortAdminStatus": cienaCesLoopDetectionPortAdminStatus,
       "cienaCesLoopDetectionPortAction": cienaCesLoopDetectionPortAction,
       "cienaCesLoopDetectionPortRevertiveMode": cienaCesLoopDetectionPortRevertiveMode,
       "cienaCesLoopDetectionPortOperState": cienaCesLoopDetectionPortOperState,
       "cienaCesLoopDetectionPortLoopStatus": cienaCesLoopDetectionPortLoopStatus,
       "cienaCesLoopDetectionPortLoopOccurence": cienaCesLoopDetectionPortLoopOccurence,
       "cienaCesLoopDetectionHoldOffTime": cienaCesLoopDetectionHoldOffTime,
       "cienaCesLoopDetectionPortCfmServiceTable": cienaCesLoopDetectionPortCfmServiceTable,
       "cienaCesLoopDetectionPortCfmServiceEntry": cienaCesLoopDetectionPortCfmServiceEntry,
       "cienaCesLoopDetectionCfmServiceIndex": cienaCesLoopDetectionCfmServiceIndex,
       "cienaCesLoopDetectionMIBNotificationPrefix": cienaCesLoopDetectionMIBNotificationPrefix,
       "cienaCesLoopDetectionMIBNotifications": cienaCesLoopDetectionMIBNotifications,
       "cienaCesLoopDetectionLoopFound": cienaCesLoopDetectionLoopFound,
       "cienaCesLoopDetectionLoopClear": cienaCesLoopDetectionLoopClear,
       "cienaCesLoopDetectionPortOperActionSet": cienaCesLoopDetectionPortOperActionSet,
       "cienaCesLoopDetectionPortOperActionClear": cienaCesLoopDetectionPortOperActionClear,
       "cienaCesLoopDetectionMIBConformance": cienaCesLoopDetectionMIBConformance,
       "cienaCesLoopDetectionMIBCompliances": cienaCesLoopDetectionMIBCompliances,
       "cienaCesLoopDetectionMIBGroups": cienaCesLoopDetectionMIBGroups}
)
