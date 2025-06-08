# SNMP MIB module (CISCO-WPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-WPAN-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:16 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWpanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819)
)
if mibBuilder.loadTexts:
    ciscoWpanMIB.setRevisions(
        ("2013-11-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWpanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWpanMIBNotifs = _CiscoWpanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0)
)
_CiscoWpanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWpanMIBObjects = _CiscoWpanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1)
)
_CiscoWpanConfig_ObjectIdentity = ObjectIdentity
ciscoWpanConfig = _CiscoWpanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1)
)
_CwpanInterfaceTable_Object = MibTable
cwpanInterfaceTable = _CwpanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwpanInterfaceTable.setStatus("current")
_CwpanInterfaceEntry_Object = MibTableRow
cwpanInterfaceEntry = _CwpanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1)
)
cwpanInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwpanInterfaceEntry.setStatus("current")


class _CwpanIfServiceStatus_Type(Integer32):
    """Custom type cwpanIfServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_CwpanIfServiceStatus_Type.__name__ = "Integer32"
_CwpanIfServiceStatus_Object = MibTableColumn
cwpanIfServiceStatus = _CwpanIfServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 1),
    _CwpanIfServiceStatus_Type()
)
cwpanIfServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfServiceStatus.setStatus("current")


class _CwpanIfServiceStatusReason_Type(Integer32):
    """Custom type cwpanIfServiceStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("powerDown", 2),
          ("powerUp", 3),
          ("moduleRemove", 4),
          ("moduleReload", 5),
          ("driverStop", 6),
          ("driverStart", 7),
          ("firmwareUpgrade", 8),
          ("firmwareReset", 9),
          ("watchDog", 10))
    )


_CwpanIfServiceStatusReason_Type.__name__ = "Integer32"
_CwpanIfServiceStatusReason_Object = MibTableColumn
cwpanIfServiceStatusReason = _CwpanIfServiceStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 2),
    _CwpanIfServiceStatusReason_Type()
)
cwpanIfServiceStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfServiceStatusReason.setStatus("current")


class _CwpanIfRplTableResetReason_Type(Integer32):
    """Custom type cwpanIfRplTableResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("manuallyClear", 2),
          ("configChange", 3),
          ("interfaceDown", 4),
          ("timeout", 5),
          ("serviceStop", 6))
    )


_CwpanIfRplTableResetReason_Type.__name__ = "Integer32"
_CwpanIfRplTableResetReason_Object = MibTableColumn
cwpanIfRplTableResetReason = _CwpanIfRplTableResetReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 3),
    _CwpanIfRplTableResetReason_Type()
)
cwpanIfRplTableResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfRplTableResetReason.setStatus("current")
_CwpanIfRplTableNodes_Type = Unsigned32
_CwpanIfRplTableNodes_Object = MibTableColumn
cwpanIfRplTableNodes = _CwpanIfRplTableNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 4),
    _CwpanIfRplTableNodes_Type()
)
cwpanIfRplTableNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfRplTableNodes.setStatus("current")
_CwpanIfRplTableMajorThreshNodes_Type = Unsigned32
_CwpanIfRplTableMajorThreshNodes_Object = MibTableColumn
cwpanIfRplTableMajorThreshNodes = _CwpanIfRplTableMajorThreshNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 5),
    _CwpanIfRplTableMajorThreshNodes_Type()
)
cwpanIfRplTableMajorThreshNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwpanIfRplTableMajorThreshNodes.setStatus("current")
_CwpanIfRplTableMinorThreshNodes_Type = Unsigned32
_CwpanIfRplTableMinorThreshNodes_Object = MibTableColumn
cwpanIfRplTableMinorThreshNodes = _CwpanIfRplTableMinorThreshNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 6),
    _CwpanIfRplTableMinorThreshNodes_Type()
)
cwpanIfRplTableMinorThreshNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfRplTableMinorThreshNodes.setStatus("current")


class _CwpanIfHAState_Type(Integer32):
    """Custom type cwpanIfHAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("active", 2),
          ("standby", 3))
    )


_CwpanIfHAState_Type.__name__ = "Integer32"
_CwpanIfHAState_Object = MibTableColumn
cwpanIfHAState = _CwpanIfHAState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 7),
    _CwpanIfHAState_Type()
)
cwpanIfHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfHAState.setStatus("current")


class _CwpanIfHAFailureCode_Type(Integer32):
    """Custom type cwpanIfHAFailureCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("registrationFailed", 1),
          ("sessionMismatch", 2),
          ("modeMismatch", 4),
          ("processEnableFail", 8),
          ("modeSetFail", 16),
          ("eui64SetFail", 32),
          ("eui64GetFail", 64),
          ("beaconVersionSetFail", 128),
          ("rplVersionSetFail", 256),
          ("neighbourSetFail", 512),
          ("sockCloseFail", 1024),
          ("peerConnectionFail", 2048),
          ("invalidEvent", 4096),
          ("prefixUpdateFail", 8192),
          ("standbyNotReady", 16384),
          ("configMismatch", 32768))
    )


_CwpanIfHAFailureCode_Type.__name__ = "Integer32"
_CwpanIfHAFailureCode_Object = MibTableColumn
cwpanIfHAFailureCode = _CwpanIfHAFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 8),
    _CwpanIfHAFailureCode_Type()
)
cwpanIfHAFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfHAFailureCode.setStatus("current")


class _CwpanIfHAStateChangeReason_Type(Integer32):
    """Custom type cwpanIfHAStateChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("automatic", 2),
          ("manual", 3))
    )


_CwpanIfHAStateChangeReason_Type.__name__ = "Integer32"
_CwpanIfHAStateChangeReason_Object = MibTableColumn
cwpanIfHAStateChangeReason = _CwpanIfHAStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 9),
    _CwpanIfHAStateChangeReason_Type()
)
cwpanIfHAStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfHAStateChangeReason.setStatus("current")


class _CwpanIfHAStandbyReady_Type(Integer32):
    """Custom type cwpanIfHAStandbyReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_CwpanIfHAStandbyReady_Type.__name__ = "Integer32"
_CwpanIfHAStandbyReady_Object = MibTableColumn
cwpanIfHAStandbyReady = _CwpanIfHAStandbyReady_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 1, 1, 10),
    _CwpanIfHAStandbyReady_Type()
)
cwpanIfHAStandbyReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwpanIfHAStandbyReady.setStatus("current")
_CwpanNotificationEnable_Type = TruthValue
_CwpanNotificationEnable_Object = MibScalar
cwpanNotificationEnable = _CwpanNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 1, 1, 2),
    _CwpanNotificationEnable_Type()
)
cwpanNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwpanNotificationEnable.setStatus("current")
_CiscoWpanMIBConform_ObjectIdentity = ObjectIdentity
ciscoWpanMIBConform = _CiscoWpanMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2)
)
_CiscoWpanMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWpanMIBCompliances = _CiscoWpanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 1)
)
_CiscoWpanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWpanMIBGroups = _CiscoWpanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2)
)

# Managed Objects groups

cwpanInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2, 1)
)
cwpanInterfaceInfoGroup.setObjects(
      *(("CISCO-WPAN-MIB", "cwpanIfServiceStatus"),
        ("CISCO-WPAN-MIB", "cwpanIfServiceStatusReason"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableResetReason"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMinorThreshNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfHAState"),
        ("CISCO-WPAN-MIB", "cwpanIfHAFailureCode"),
        ("CISCO-WPAN-MIB", "cwpanNotificationEnable"),
        ("CISCO-WPAN-MIB", "cwpanIfHAStateChangeReason"),
        ("CISCO-WPAN-MIB", "cwpanIfHAStandbyReady"))
)
if mibBuilder.loadTexts:
    cwpanInterfaceInfoGroup.setStatus("current")

cwpanNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2, 2)
)
cwpanNotificationControlGroup.setObjects(
    ("CISCO-WPAN-MIB", "cwpanNotificationEnable")
)
if mibBuilder.loadTexts:
    cwpanNotificationControlGroup.setStatus("current")


# Notification objects

cwpanServiceStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 1)
)
cwpanServiceStatusChangeNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfServiceStatusReason"))
)
if mibBuilder.loadTexts:
    cwpanServiceStatusChangeNotif.setStatus(
        "current"
    )

cwpanRplTableResetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 2)
)
cwpanRplTableResetNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableResetReason"))
)
if mibBuilder.loadTexts:
    cwpanRplTableResetNotif.setStatus(
        "current"
    )

cwpanRisingIfRplTblMinorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 3)
)
cwpanRisingIfRplTblMinorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMinorThreshNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanRisingIfRplTblMinorThreshNodesNotif.setStatus(
        "current"
    )

cwpanFallingIfRplTblMinorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 4)
)
cwpanFallingIfRplTblMinorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMinorThreshNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanFallingIfRplTblMinorThreshNodesNotif.setStatus(
        "current"
    )

cwpanRisingIfRplTblMajorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 5)
)
cwpanRisingIfRplTblMajorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanRisingIfRplTblMajorThreshNodesNotif.setStatus(
        "current"
    )

cwpanFallingIfRplTblMajorThreshNodesNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 6)
)
cwpanFallingIfRplTblMajorThreshNodesNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableNodes"),
        ("CISCO-WPAN-MIB", "cwpanIfRplTableMajorThreshNodes"))
)
if mibBuilder.loadTexts:
    cwpanFallingIfRplTblMajorThreshNodesNotif.setStatus(
        "current"
    )

cwpanHAStateChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 7)
)
cwpanHAStateChangeNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfHAStandbyReady"),
        ("CISCO-WPAN-MIB", "cwpanIfHAStateChangeReason"),
        ("CISCO-WPAN-MIB", "cwpanIfHAState"))
)
if mibBuilder.loadTexts:
    cwpanHAStateChangeNotif.setStatus(
        "current"
    )

cwpanHAFailureNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 0, 8)
)
cwpanHAFailureNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-WPAN-MIB", "cwpanIfHAFailureCode"))
)
if mibBuilder.loadTexts:
    cwpanHAFailureNotif.setStatus(
        "current"
    )


# Notifications groups

cwpanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 2, 3)
)
cwpanNotificationGroup.setObjects(
      *(("CISCO-WPAN-MIB", "cwpanServiceStatusChangeNotif"),
        ("CISCO-WPAN-MIB", "cwpanRplTableResetNotif"),
        ("CISCO-WPAN-MIB", "cwpanRisingIfRplTblMinorThreshNodesNotif"),
        ("CISCO-WPAN-MIB", "cwpanFallingIfRplTblMinorThreshNodesNotif"),
        ("CISCO-WPAN-MIB", "cwpanRisingIfRplTblMajorThreshNodesNotif"),
        ("CISCO-WPAN-MIB", "cwpanFallingIfRplTblMajorThreshNodesNotif"),
        ("CISCO-WPAN-MIB", "cwpanHAStateChangeNotif"),
        ("CISCO-WPAN-MIB", "cwpanHAFailureNotif"))
)
if mibBuilder.loadTexts:
    cwpanNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWpanMIBModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 819, 2, 1, 1)
)
ciscoWpanMIBModuleCompliance.setObjects(
      *(("CISCO-WPAN-MIB", "cwpanInterfaceInfoGroup"),
        ("CISCO-WPAN-MIB", "cwpanNotificationControlGroup"),
        ("CISCO-WPAN-MIB", "cwpanNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoWpanMIBModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WPAN-MIB",
    **{"ciscoWpanMIB": ciscoWpanMIB,
       "ciscoWpanMIBNotifs": ciscoWpanMIBNotifs,
       "cwpanServiceStatusChangeNotif": cwpanServiceStatusChangeNotif,
       "cwpanRplTableResetNotif": cwpanRplTableResetNotif,
       "cwpanRisingIfRplTblMinorThreshNodesNotif": cwpanRisingIfRplTblMinorThreshNodesNotif,
       "cwpanFallingIfRplTblMinorThreshNodesNotif": cwpanFallingIfRplTblMinorThreshNodesNotif,
       "cwpanRisingIfRplTblMajorThreshNodesNotif": cwpanRisingIfRplTblMajorThreshNodesNotif,
       "cwpanFallingIfRplTblMajorThreshNodesNotif": cwpanFallingIfRplTblMajorThreshNodesNotif,
       "cwpanHAStateChangeNotif": cwpanHAStateChangeNotif,
       "cwpanHAFailureNotif": cwpanHAFailureNotif,
       "ciscoWpanMIBObjects": ciscoWpanMIBObjects,
       "ciscoWpanConfig": ciscoWpanConfig,
       "cwpanInterfaceTable": cwpanInterfaceTable,
       "cwpanInterfaceEntry": cwpanInterfaceEntry,
       "cwpanIfServiceStatus": cwpanIfServiceStatus,
       "cwpanIfServiceStatusReason": cwpanIfServiceStatusReason,
       "cwpanIfRplTableResetReason": cwpanIfRplTableResetReason,
       "cwpanIfRplTableNodes": cwpanIfRplTableNodes,
       "cwpanIfRplTableMajorThreshNodes": cwpanIfRplTableMajorThreshNodes,
       "cwpanIfRplTableMinorThreshNodes": cwpanIfRplTableMinorThreshNodes,
       "cwpanIfHAState": cwpanIfHAState,
       "cwpanIfHAFailureCode": cwpanIfHAFailureCode,
       "cwpanIfHAStateChangeReason": cwpanIfHAStateChangeReason,
       "cwpanIfHAStandbyReady": cwpanIfHAStandbyReady,
       "cwpanNotificationEnable": cwpanNotificationEnable,
       "ciscoWpanMIBConform": ciscoWpanMIBConform,
       "ciscoWpanMIBCompliances": ciscoWpanMIBCompliances,
       "ciscoWpanMIBModuleCompliance": ciscoWpanMIBModuleCompliance,
       "ciscoWpanMIBGroups": ciscoWpanMIBGroups,
       "cwpanInterfaceInfoGroup": cwpanInterfaceInfoGroup,
       "cwpanNotificationControlGroup": cwpanNotificationControlGroup,
       "cwpanNotificationGroup": cwpanNotificationGroup}
)
