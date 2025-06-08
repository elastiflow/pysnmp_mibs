# SNMP MIB module (CISCO-FIREPOWER-AP-ORG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-ORG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:27 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApOrgLevel,
 CfprApOrgSrcMask) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApOrgLevel",
    "CfprApOrgSrcMask")

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

cfprApOrgObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApOrgOrgTable_Object = MibTable
cfprApOrgOrgTable = _CfprApOrgOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1)
)
if mibBuilder.loadTexts:
    cfprApOrgOrgTable.setStatus("current")
_CfprApOrgOrgEntry_Object = MibTableRow
cfprApOrgOrgEntry = _CfprApOrgOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1)
)
cfprApOrgOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ORG-MIB", "cfprApOrgOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApOrgOrgEntry.setStatus("current")
_CfprApOrgOrgInstanceId_Type = CfprApManagedObjectId
_CfprApOrgOrgInstanceId_Object = MibTableColumn
cfprApOrgOrgInstanceId = _CfprApOrgOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 1),
    _CfprApOrgOrgInstanceId_Type()
)
cfprApOrgOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApOrgOrgInstanceId.setStatus("current")
_CfprApOrgOrgDn_Type = CfprApManagedObjectDn
_CfprApOrgOrgDn_Object = MibTableColumn
cfprApOrgOrgDn = _CfprApOrgOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 2),
    _CfprApOrgOrgDn_Type()
)
cfprApOrgOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgOrgDn.setStatus("current")
_CfprApOrgOrgRn_Type = SnmpAdminString
_CfprApOrgOrgRn_Object = MibTableColumn
cfprApOrgOrgRn = _CfprApOrgOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 3),
    _CfprApOrgOrgRn_Type()
)
cfprApOrgOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgOrgRn.setStatus("current")
_CfprApOrgOrgDescr_Type = SnmpAdminString
_CfprApOrgOrgDescr_Object = MibTableColumn
cfprApOrgOrgDescr = _CfprApOrgOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 4),
    _CfprApOrgOrgDescr_Type()
)
cfprApOrgOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgOrgDescr.setStatus("current")
_CfprApOrgOrgFltAggr_Type = Unsigned64
_CfprApOrgOrgFltAggr_Object = MibTableColumn
cfprApOrgOrgFltAggr = _CfprApOrgOrgFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 5),
    _CfprApOrgOrgFltAggr_Type()
)
cfprApOrgOrgFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgOrgFltAggr.setStatus("current")
_CfprApOrgOrgLevel_Type = CfprApOrgLevel
_CfprApOrgOrgLevel_Object = MibTableColumn
cfprApOrgOrgLevel = _CfprApOrgOrgLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 6),
    _CfprApOrgOrgLevel_Type()
)
cfprApOrgOrgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgOrgLevel.setStatus("current")
_CfprApOrgOrgName_Type = SnmpAdminString
_CfprApOrgOrgName_Object = MibTableColumn
cfprApOrgOrgName = _CfprApOrgOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 7),
    _CfprApOrgOrgName_Type()
)
cfprApOrgOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgOrgName.setStatus("current")
_CfprApOrgOrgPermAccess_Type = TruthValue
_CfprApOrgOrgPermAccess_Object = MibTableColumn
cfprApOrgOrgPermAccess = _CfprApOrgOrgPermAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 1, 1, 8),
    _CfprApOrgOrgPermAccess_Type()
)
cfprApOrgOrgPermAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgOrgPermAccess.setStatus("current")
_CfprApOrgSourceMaskTable_Object = MibTable
cfprApOrgSourceMaskTable = _CfprApOrgSourceMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 2)
)
if mibBuilder.loadTexts:
    cfprApOrgSourceMaskTable.setStatus("current")
_CfprApOrgSourceMaskEntry_Object = MibTableRow
cfprApOrgSourceMaskEntry = _CfprApOrgSourceMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 2, 1)
)
cfprApOrgSourceMaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ORG-MIB", "cfprApOrgSourceMaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApOrgSourceMaskEntry.setStatus("current")
_CfprApOrgSourceMaskInstanceId_Type = CfprApManagedObjectId
_CfprApOrgSourceMaskInstanceId_Object = MibTableColumn
cfprApOrgSourceMaskInstanceId = _CfprApOrgSourceMaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 2, 1, 1),
    _CfprApOrgSourceMaskInstanceId_Type()
)
cfprApOrgSourceMaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApOrgSourceMaskInstanceId.setStatus("current")
_CfprApOrgSourceMaskDn_Type = CfprApManagedObjectDn
_CfprApOrgSourceMaskDn_Object = MibTableColumn
cfprApOrgSourceMaskDn = _CfprApOrgSourceMaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 2, 1, 2),
    _CfprApOrgSourceMaskDn_Type()
)
cfprApOrgSourceMaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgSourceMaskDn.setStatus("current")
_CfprApOrgSourceMaskRn_Type = SnmpAdminString
_CfprApOrgSourceMaskRn_Object = MibTableColumn
cfprApOrgSourceMaskRn = _CfprApOrgSourceMaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 2, 1, 3),
    _CfprApOrgSourceMaskRn_Type()
)
cfprApOrgSourceMaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgSourceMaskRn.setStatus("current")
_CfprApOrgSourceMaskMask_Type = CfprApOrgSrcMask
_CfprApOrgSourceMaskMask_Object = MibTableColumn
cfprApOrgSourceMaskMask = _CfprApOrgSourceMaskMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 58, 2, 1, 4),
    _CfprApOrgSourceMaskMask_Type()
)
cfprApOrgSourceMaskMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOrgSourceMaskMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-ORG-MIB",
    **{"cfprApOrgObjects": cfprApOrgObjects,
       "cfprApOrgOrgTable": cfprApOrgOrgTable,
       "cfprApOrgOrgEntry": cfprApOrgOrgEntry,
       "cfprApOrgOrgInstanceId": cfprApOrgOrgInstanceId,
       "cfprApOrgOrgDn": cfprApOrgOrgDn,
       "cfprApOrgOrgRn": cfprApOrgOrgRn,
       "cfprApOrgOrgDescr": cfprApOrgOrgDescr,
       "cfprApOrgOrgFltAggr": cfprApOrgOrgFltAggr,
       "cfprApOrgOrgLevel": cfprApOrgOrgLevel,
       "cfprApOrgOrgName": cfprApOrgOrgName,
       "cfprApOrgOrgPermAccess": cfprApOrgOrgPermAccess,
       "cfprApOrgSourceMaskTable": cfprApOrgSourceMaskTable,
       "cfprApOrgSourceMaskEntry": cfprApOrgSourceMaskEntry,
       "cfprApOrgSourceMaskInstanceId": cfprApOrgSourceMaskInstanceId,
       "cfprApOrgSourceMaskDn": cfprApOrgSourceMaskDn,
       "cfprApOrgSourceMaskRn": cfprApOrgSourceMaskRn,
       "cfprApOrgSourceMaskMask": cfprApOrgSourceMaskMask}
)
