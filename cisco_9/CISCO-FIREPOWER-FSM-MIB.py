# SNMP MIB module (CISCO-FIREPOWER-FSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-FSM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprFsmFsmStageStatus,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprFsmFsmStageStatus")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprFsmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprFsmStatusTable_Object = MibTable
cfprFsmStatusTable = _CfprFsmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1)
)
if mibBuilder.loadTexts:
    cfprFsmStatusTable.setStatus("current")
_CfprFsmStatusEntry_Object = MibTableRow
cfprFsmStatusEntry = _CfprFsmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1)
)
cfprFsmStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FSM-MIB", "cfprFsmStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFsmStatusEntry.setStatus("current")
_CfprFsmStatusInstanceId_Type = CfprManagedObjectId
_CfprFsmStatusInstanceId_Object = MibTableColumn
cfprFsmStatusInstanceId = _CfprFsmStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 1),
    _CfprFsmStatusInstanceId_Type()
)
cfprFsmStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFsmStatusInstanceId.setStatus("current")
_CfprFsmStatusDn_Type = CfprManagedObjectDn
_CfprFsmStatusDn_Object = MibTableColumn
cfprFsmStatusDn = _CfprFsmStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 2),
    _CfprFsmStatusDn_Type()
)
cfprFsmStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusDn.setStatus("current")
_CfprFsmStatusRn_Type = SnmpAdminString
_CfprFsmStatusRn_Object = MibTableColumn
cfprFsmStatusRn = _CfprFsmStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 3),
    _CfprFsmStatusRn_Type()
)
cfprFsmStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusRn.setStatus("current")
_CfprFsmStatusConvertedEpRef_Type = SnmpAdminString
_CfprFsmStatusConvertedEpRef_Object = MibTableColumn
cfprFsmStatusConvertedEpRef = _CfprFsmStatusConvertedEpRef_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 4),
    _CfprFsmStatusConvertedEpRef_Type()
)
cfprFsmStatusConvertedEpRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusConvertedEpRef.setStatus("current")
_CfprFsmStatusDescr_Type = SnmpAdminString
_CfprFsmStatusDescr_Object = MibTableColumn
cfprFsmStatusDescr = _CfprFsmStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 5),
    _CfprFsmStatusDescr_Type()
)
cfprFsmStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusDescr.setStatus("current")
_CfprFsmStatusName_Type = SnmpAdminString
_CfprFsmStatusName_Object = MibTableColumn
cfprFsmStatusName = _CfprFsmStatusName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 6),
    _CfprFsmStatusName_Type()
)
cfprFsmStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusName.setStatus("current")
_CfprFsmStatusObjectClassName_Type = SnmpAdminString
_CfprFsmStatusObjectClassName_Object = MibTableColumn
cfprFsmStatusObjectClassName = _CfprFsmStatusObjectClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 7),
    _CfprFsmStatusObjectClassName_Type()
)
cfprFsmStatusObjectClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusObjectClassName.setStatus("current")
_CfprFsmStatusRemoteEpRef_Type = SnmpAdminString
_CfprFsmStatusRemoteEpRef_Object = MibTableColumn
cfprFsmStatusRemoteEpRef = _CfprFsmStatusRemoteEpRef_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 8),
    _CfprFsmStatusRemoteEpRef_Type()
)
cfprFsmStatusRemoteEpRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusRemoteEpRef.setStatus("current")
_CfprFsmStatusState_Type = CfprFsmFsmStageStatus
_CfprFsmStatusState_Object = MibTableColumn
cfprFsmStatusState = _CfprFsmStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 32, 1, 1, 9),
    _CfprFsmStatusState_Type()
)
cfprFsmStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFsmStatusState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-FSM-MIB",
    **{"cfprFsmObjects": cfprFsmObjects,
       "cfprFsmStatusTable": cfprFsmStatusTable,
       "cfprFsmStatusEntry": cfprFsmStatusEntry,
       "cfprFsmStatusInstanceId": cfprFsmStatusInstanceId,
       "cfprFsmStatusDn": cfprFsmStatusDn,
       "cfprFsmStatusRn": cfprFsmStatusRn,
       "cfprFsmStatusConvertedEpRef": cfprFsmStatusConvertedEpRef,
       "cfprFsmStatusDescr": cfprFsmStatusDescr,
       "cfprFsmStatusName": cfprFsmStatusName,
       "cfprFsmStatusObjectClassName": cfprFsmStatusObjectClassName,
       "cfprFsmStatusRemoteEpRef": cfprFsmStatusRemoteEpRef,
       "cfprFsmStatusState": cfprFsmStatusState}
)
