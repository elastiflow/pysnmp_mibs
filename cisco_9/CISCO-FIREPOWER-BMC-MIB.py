# SNMP MIB module (CISCO-FIREPOWER-BMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-BMC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:40 2025
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

(CfprBmcSELCntEqptClassId,
 CfprBmcSELCntEqptInstIdPropId,
 CfprBmcSELCntStatsClassId) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprBmcSELCntEqptClassId",
    "CfprBmcSELCntEqptInstIdPropId",
    "CfprBmcSELCntStatsClassId")

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

cfprBmcObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprBmcSELCounterTable_Object = MibTable
cfprBmcSELCounterTable = _CfprBmcSELCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cfprBmcSELCounterTable.setStatus("current")
_CfprBmcSELCounterEntry_Object = MibTableRow
cfprBmcSELCounterEntry = _CfprBmcSELCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1)
)
cfprBmcSELCounterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-BMC-MIB", "cfprBmcSELCounterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprBmcSELCounterEntry.setStatus("current")
_CfprBmcSELCounterInstanceId_Type = CfprManagedObjectId
_CfprBmcSELCounterInstanceId_Object = MibTableColumn
cfprBmcSELCounterInstanceId = _CfprBmcSELCounterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 1),
    _CfprBmcSELCounterInstanceId_Type()
)
cfprBmcSELCounterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprBmcSELCounterInstanceId.setStatus("current")
_CfprBmcSELCounterDn_Type = CfprManagedObjectDn
_CfprBmcSELCounterDn_Object = MibTableColumn
cfprBmcSELCounterDn = _CfprBmcSELCounterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 2),
    _CfprBmcSELCounterDn_Type()
)
cfprBmcSELCounterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterDn.setStatus("current")
_CfprBmcSELCounterRn_Type = SnmpAdminString
_CfprBmcSELCounterRn_Object = MibTableColumn
cfprBmcSELCounterRn = _CfprBmcSELCounterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 3),
    _CfprBmcSELCounterRn_Type()
)
cfprBmcSELCounterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterRn.setStatus("current")
_CfprBmcSELCounterBitmask_Type = SnmpAdminString
_CfprBmcSELCounterBitmask_Object = MibTableColumn
cfprBmcSELCounterBitmask = _CfprBmcSELCounterBitmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 4),
    _CfprBmcSELCounterBitmask_Type()
)
cfprBmcSELCounterBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterBitmask.setStatus("current")
_CfprBmcSELCounterCollInterval_Type = Gauge32
_CfprBmcSELCounterCollInterval_Object = MibTableColumn
cfprBmcSELCounterCollInterval = _CfprBmcSELCounterCollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 5),
    _CfprBmcSELCounterCollInterval_Type()
)
cfprBmcSELCounterCollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterCollInterval.setStatus("current")
_CfprBmcSELCounterContClassId_Type = CfprBmcSELCntEqptClassId
_CfprBmcSELCounterContClassId_Object = MibTableColumn
cfprBmcSELCounterContClassId = _CfprBmcSELCounterContClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 6),
    _CfprBmcSELCounterContClassId_Type()
)
cfprBmcSELCounterContClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterContClassId.setStatus("current")
_CfprBmcSELCounterContInstId_Type = SnmpAdminString
_CfprBmcSELCounterContInstId_Object = MibTableColumn
cfprBmcSELCounterContInstId = _CfprBmcSELCounterContInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 7),
    _CfprBmcSELCounterContInstId_Type()
)
cfprBmcSELCounterContInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterContInstId.setStatus("current")
_CfprBmcSELCounterContInstIdPropId_Type = CfprBmcSELCntEqptInstIdPropId
_CfprBmcSELCounterContInstIdPropId_Object = MibTableColumn
cfprBmcSELCounterContInstIdPropId = _CfprBmcSELCounterContInstIdPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 8),
    _CfprBmcSELCounterContInstIdPropId_Type()
)
cfprBmcSELCounterContInstIdPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterContInstIdPropId.setStatus("current")
_CfprBmcSELCounterEqptClassId_Type = CfprBmcSELCntEqptClassId
_CfprBmcSELCounterEqptClassId_Object = MibTableColumn
cfprBmcSELCounterEqptClassId = _CfprBmcSELCounterEqptClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 9),
    _CfprBmcSELCounterEqptClassId_Type()
)
cfprBmcSELCounterEqptClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterEqptClassId.setStatus("current")
_CfprBmcSELCounterEqptInstId_Type = SnmpAdminString
_CfprBmcSELCounterEqptInstId_Object = MibTableColumn
cfprBmcSELCounterEqptInstId = _CfprBmcSELCounterEqptInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 10),
    _CfprBmcSELCounterEqptInstId_Type()
)
cfprBmcSELCounterEqptInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterEqptInstId.setStatus("current")
_CfprBmcSELCounterEqptInstIdPropId_Type = CfprBmcSELCntEqptInstIdPropId
_CfprBmcSELCounterEqptInstIdPropId_Object = MibTableColumn
cfprBmcSELCounterEqptInstIdPropId = _CfprBmcSELCounterEqptInstIdPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 11),
    _CfprBmcSELCounterEqptInstIdPropId_Type()
)
cfprBmcSELCounterEqptInstIdPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterEqptInstIdPropId.setStatus("current")
_CfprBmcSELCounterGlobalId_Type = SnmpAdminString
_CfprBmcSELCounterGlobalId_Object = MibTableColumn
cfprBmcSELCounterGlobalId = _CfprBmcSELCounterGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 12),
    _CfprBmcSELCounterGlobalId_Type()
)
cfprBmcSELCounterGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterGlobalId.setStatus("current")
_CfprBmcSELCounterLocalId_Type = SnmpAdminString
_CfprBmcSELCounterLocalId_Object = MibTableColumn
cfprBmcSELCounterLocalId = _CfprBmcSELCounterLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 13),
    _CfprBmcSELCounterLocalId_Type()
)
cfprBmcSELCounterLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterLocalId.setStatus("current")
_CfprBmcSELCounterPcGlobalId_Type = SnmpAdminString
_CfprBmcSELCounterPcGlobalId_Object = MibTableColumn
cfprBmcSELCounterPcGlobalId = _CfprBmcSELCounterPcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 14),
    _CfprBmcSELCounterPcGlobalId_Type()
)
cfprBmcSELCounterPcGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterPcGlobalId.setStatus("current")
_CfprBmcSELCounterPcLocalId_Type = SnmpAdminString
_CfprBmcSELCounterPcLocalId_Object = MibTableColumn
cfprBmcSELCounterPcLocalId = _CfprBmcSELCounterPcLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 15),
    _CfprBmcSELCounterPcLocalId_Type()
)
cfprBmcSELCounterPcLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterPcLocalId.setStatus("current")
_CfprBmcSELCounterStatsClassId_Type = CfprBmcSELCntStatsClassId
_CfprBmcSELCounterStatsClassId_Object = MibTableColumn
cfprBmcSELCounterStatsClassId = _CfprBmcSELCounterStatsClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 16),
    _CfprBmcSELCounterStatsClassId_Type()
)
cfprBmcSELCounterStatsClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterStatsClassId.setStatus("current")
_CfprBmcSELCounterStatsPropId_Type = Integer32
_CfprBmcSELCounterStatsPropId_Object = MibTableColumn
cfprBmcSELCounterStatsPropId = _CfprBmcSELCounterStatsPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 17),
    _CfprBmcSELCounterStatsPropId_Type()
)
cfprBmcSELCounterStatsPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterStatsPropId.setStatus("current")
_CfprBmcSELCounterThreshold_Type = Gauge32
_CfprBmcSELCounterThreshold_Object = MibTableColumn
cfprBmcSELCounterThreshold = _CfprBmcSELCounterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 18),
    _CfprBmcSELCounterThreshold_Type()
)
cfprBmcSELCounterThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterThreshold.setStatus("current")
_CfprBmcSELCounterValue_Type = SnmpAdminString
_CfprBmcSELCounterValue_Object = MibTableColumn
cfprBmcSELCounterValue = _CfprBmcSELCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 6, 1, 1, 19),
    _CfprBmcSELCounterValue_Type()
)
cfprBmcSELCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprBmcSELCounterValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-BMC-MIB",
    **{"cfprBmcObjects": cfprBmcObjects,
       "cfprBmcSELCounterTable": cfprBmcSELCounterTable,
       "cfprBmcSELCounterEntry": cfprBmcSELCounterEntry,
       "cfprBmcSELCounterInstanceId": cfprBmcSELCounterInstanceId,
       "cfprBmcSELCounterDn": cfprBmcSELCounterDn,
       "cfprBmcSELCounterRn": cfprBmcSELCounterRn,
       "cfprBmcSELCounterBitmask": cfprBmcSELCounterBitmask,
       "cfprBmcSELCounterCollInterval": cfprBmcSELCounterCollInterval,
       "cfprBmcSELCounterContClassId": cfprBmcSELCounterContClassId,
       "cfprBmcSELCounterContInstId": cfprBmcSELCounterContInstId,
       "cfprBmcSELCounterContInstIdPropId": cfprBmcSELCounterContInstIdPropId,
       "cfprBmcSELCounterEqptClassId": cfprBmcSELCounterEqptClassId,
       "cfprBmcSELCounterEqptInstId": cfprBmcSELCounterEqptInstId,
       "cfprBmcSELCounterEqptInstIdPropId": cfprBmcSELCounterEqptInstIdPropId,
       "cfprBmcSELCounterGlobalId": cfprBmcSELCounterGlobalId,
       "cfprBmcSELCounterLocalId": cfprBmcSELCounterLocalId,
       "cfprBmcSELCounterPcGlobalId": cfprBmcSELCounterPcGlobalId,
       "cfprBmcSELCounterPcLocalId": cfprBmcSELCounterPcLocalId,
       "cfprBmcSELCounterStatsClassId": cfprBmcSELCounterStatsClassId,
       "cfprBmcSELCounterStatsPropId": cfprBmcSELCounterStatsPropId,
       "cfprBmcSELCounterThreshold": cfprBmcSELCounterThreshold,
       "cfprBmcSELCounterValue": cfprBmcSELCounterValue}
)
