# SNMP MIB module (CISCO-DLR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DLR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:02:46 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDlrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 865)
)
if mibBuilder.loadTexts:
    ciscoDlrMIB.setRevisions(
        ("2019-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlrNetworkStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ringNormal", 1),
          ("ringFault", 2),
          ("ringUnexcpectedLoop", 3),
          ("ringPartialFault", 4),
          ("ringRapidFaultRestore", 5))
    )



class DlrDeviceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("supBackup", 1),
          ("supActive", 2),
          ("normalRing", 3),
          ("nonDlr", 4))
    )



class DlrGatewayDeviceStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("nonGateway", 1),
          ("activeGateway", 2),
          ("backupGateway", 3),
          ("faultGateway", 4),
          ("nonSupportedGateway", 5),
          ("partialFaultGateway", 6))
    )



class DlrGatewayDeviceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("gatewayIdle", 1),
          ("activeListen", 2),
          ("activeNormal", 3),
          ("fault", 4),
          ("backupNormal", 5),
          ("lossUplink", 6),
          ("partialNetworkfault", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDlrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDlrMIBNotifs = _CiscoDlrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 0)
)
_CiscoDlrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDlrMIBObjects = _CiscoDlrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1)
)
_CiscoDlrRingTable_Object = MibTable
ciscoDlrRingTable = _CiscoDlrRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDlrRingTable.setStatus("current")
_CiscoDlrRingEntry_Object = MibTableRow
ciscoDlrRingEntry = _CiscoDlrRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1)
)
ciscoDlrRingEntry.setIndexNames(
    (0, "CISCO-DLR-MIB", "ciscoDlrRingIndex"),
)
if mibBuilder.loadTexts:
    ciscoDlrRingEntry.setStatus("current")
_CiscoDlrRingIndex_Type = Unsigned32
_CiscoDlrRingIndex_Object = MibTableColumn
ciscoDlrRingIndex = _CiscoDlrRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 1),
    _CiscoDlrRingIndex_Type()
)
ciscoDlrRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlrRingIndex.setStatus("current")
_CiscoDlrRingID_Type = Unsigned32
_CiscoDlrRingID_Object = MibTableColumn
ciscoDlrRingID = _CiscoDlrRingID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 2),
    _CiscoDlrRingID_Type()
)
ciscoDlrRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlrRingID.setStatus("current")
_CiscoDlrRingName_Type = DisplayString
_CiscoDlrRingName_Object = MibTableColumn
ciscoDlrRingName = _CiscoDlrRingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 3),
    _CiscoDlrRingName_Type()
)
ciscoDlrRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlrRingName.setStatus("current")
_CiscoDlrRingNetworkStatus_Type = DlrNetworkStatus
_CiscoDlrRingNetworkStatus_Object = MibTableColumn
ciscoDlrRingNetworkStatus = _CiscoDlrRingNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 4),
    _CiscoDlrRingNetworkStatus_Type()
)
ciscoDlrRingNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlrRingNetworkStatus.setStatus("current")
_CiscoDlrRingDeviceState_Type = DlrDeviceState
_CiscoDlrRingDeviceState_Object = MibTableColumn
ciscoDlrRingDeviceState = _CiscoDlrRingDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 5),
    _CiscoDlrRingDeviceState_Type()
)
ciscoDlrRingDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlrRingDeviceState.setStatus("current")
_CiscoDlrRingGatewayDeviceStatus_Type = DlrGatewayDeviceStatus
_CiscoDlrRingGatewayDeviceStatus_Object = MibTableColumn
ciscoDlrRingGatewayDeviceStatus = _CiscoDlrRingGatewayDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 6),
    _CiscoDlrRingGatewayDeviceStatus_Type()
)
ciscoDlrRingGatewayDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlrRingGatewayDeviceStatus.setStatus("current")
_CiscoDlrRingGatewayDeviceState_Type = DlrGatewayDeviceState
_CiscoDlrRingGatewayDeviceState_Object = MibTableColumn
ciscoDlrRingGatewayDeviceState = _CiscoDlrRingGatewayDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 7),
    _CiscoDlrRingGatewayDeviceState_Type()
)
ciscoDlrRingGatewayDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlrRingGatewayDeviceState.setStatus("current")
_CiscoDlrMIBConform_ObjectIdentity = ObjectIdentity
ciscoDlrMIBConform = _CiscoDlrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 2)
)
_CiscoDlrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDlrMIBCompliances = _CiscoDlrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 1)
)
_CiscoDlrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDlrMIBGroups = _CiscoDlrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2)
)

# Managed Objects groups

ciscoDlrMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2, 1)
)
ciscoDlrMIBMainObjectGroup.setObjects(
      *(("CISCO-DLR-MIB", "ciscoDlrRingID"),
        ("CISCO-DLR-MIB", "ciscoDlrRingNetworkStatus"),
        ("CISCO-DLR-MIB", "ciscoDlrRingDeviceState"),
        ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceStatus"),
        ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceState"),
        ("CISCO-DLR-MIB", "ciscoDlrRingName"))
)
if mibBuilder.loadTexts:
    ciscoDlrMIBMainObjectGroup.setStatus("current")


# Notification objects

ciscoDlrRingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 1)
)
ciscoDlrRingStatus.setObjects(
      *(("CISCO-DLR-MIB", "ciscoDlrRingID"),
        ("CISCO-DLR-MIB", "ciscoDlrRingName"),
        ("CISCO-DLR-MIB", "ciscoDlrRingNetworkStatus"))
)
if mibBuilder.loadTexts:
    ciscoDlrRingStatus.setStatus(
        "current"
    )

ciscoDlrRingSupervisorStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 2)
)
ciscoDlrRingSupervisorStatus.setObjects(
      *(("CISCO-DLR-MIB", "ciscoDlrRingID"),
        ("CISCO-DLR-MIB", "ciscoDlrRingName"),
        ("CISCO-DLR-MIB", "ciscoDlrRingDeviceState"))
)
if mibBuilder.loadTexts:
    ciscoDlrRingSupervisorStatus.setStatus(
        "current"
    )

ciscoDlrRingGatewayStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 3)
)
ciscoDlrRingGatewayStatus.setObjects(
      *(("CISCO-DLR-MIB", "ciscoDlrRingID"),
        ("CISCO-DLR-MIB", "ciscoDlrRingName"),
        ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceStatus"))
)
if mibBuilder.loadTexts:
    ciscoDlrRingGatewayStatus.setStatus(
        "current"
    )


# Notifications groups

ciscoDlrMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2, 2)
)
ciscoDlrMIBNotifyGroup.setObjects(
      *(("CISCO-DLR-MIB", "ciscoDlrRingStatus"),
        ("CISCO-DLR-MIB", "ciscoDlrRingSupervisorStatus"),
        ("CISCO-DLR-MIB", "ciscoDlrRingGatewayStatus"))
)
if mibBuilder.loadTexts:
    ciscoDlrMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDlrMIBModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 1, 1)
)
ciscoDlrMIBModuleCompliance.setObjects(
      *(("CISCO-DLR-MIB", "ciscoDlrMIBMainObjectGroup"),
        ("CISCO-DLR-MIB", "ciscoDlrMIBNotifyGroup"))
)
if mibBuilder.loadTexts:
    ciscoDlrMIBModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DLR-MIB",
    **{"DlrNetworkStatus": DlrNetworkStatus,
       "DlrDeviceState": DlrDeviceState,
       "DlrGatewayDeviceStatus": DlrGatewayDeviceStatus,
       "DlrGatewayDeviceState": DlrGatewayDeviceState,
       "ciscoDlrMIB": ciscoDlrMIB,
       "ciscoDlrMIBNotifs": ciscoDlrMIBNotifs,
       "ciscoDlrRingStatus": ciscoDlrRingStatus,
       "ciscoDlrRingSupervisorStatus": ciscoDlrRingSupervisorStatus,
       "ciscoDlrRingGatewayStatus": ciscoDlrRingGatewayStatus,
       "ciscoDlrMIBObjects": ciscoDlrMIBObjects,
       "ciscoDlrRingTable": ciscoDlrRingTable,
       "ciscoDlrRingEntry": ciscoDlrRingEntry,
       "ciscoDlrRingIndex": ciscoDlrRingIndex,
       "ciscoDlrRingID": ciscoDlrRingID,
       "ciscoDlrRingName": ciscoDlrRingName,
       "ciscoDlrRingNetworkStatus": ciscoDlrRingNetworkStatus,
       "ciscoDlrRingDeviceState": ciscoDlrRingDeviceState,
       "ciscoDlrRingGatewayDeviceStatus": ciscoDlrRingGatewayDeviceStatus,
       "ciscoDlrRingGatewayDeviceState": ciscoDlrRingGatewayDeviceState,
       "ciscoDlrMIBConform": ciscoDlrMIBConform,
       "ciscoDlrMIBCompliances": ciscoDlrMIBCompliances,
       "ciscoDlrMIBModuleCompliance": ciscoDlrMIBModuleCompliance,
       "ciscoDlrMIBGroups": ciscoDlrMIBGroups,
       "ciscoDlrMIBMainObjectGroup": ciscoDlrMIBMainObjectGroup,
       "ciscoDlrMIBNotifyGroup": ciscoDlrMIBNotifyGroup}
)
