# SNMP MIB module (CISCO-FIREPOWER-ORG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-ORG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:12 2025
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

(CfprOrgLevel,
 CfprOrgSrcMask) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprOrgLevel",
    "CfprOrgSrcMask")

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

cfprOrgObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprOrgOrgTable_Object = MibTable
cfprOrgOrgTable = _CfprOrgOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1)
)
if mibBuilder.loadTexts:
    cfprOrgOrgTable.setStatus("current")
_CfprOrgOrgEntry_Object = MibTableRow
cfprOrgOrgEntry = _CfprOrgOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1)
)
cfprOrgOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ORG-MIB", "cfprOrgOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOrgOrgEntry.setStatus("current")
_CfprOrgOrgInstanceId_Type = CfprManagedObjectId
_CfprOrgOrgInstanceId_Object = MibTableColumn
cfprOrgOrgInstanceId = _CfprOrgOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 1),
    _CfprOrgOrgInstanceId_Type()
)
cfprOrgOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOrgOrgInstanceId.setStatus("current")
_CfprOrgOrgDn_Type = CfprManagedObjectDn
_CfprOrgOrgDn_Object = MibTableColumn
cfprOrgOrgDn = _CfprOrgOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 2),
    _CfprOrgOrgDn_Type()
)
cfprOrgOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgOrgDn.setStatus("current")
_CfprOrgOrgRn_Type = SnmpAdminString
_CfprOrgOrgRn_Object = MibTableColumn
cfprOrgOrgRn = _CfprOrgOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 3),
    _CfprOrgOrgRn_Type()
)
cfprOrgOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgOrgRn.setStatus("current")
_CfprOrgOrgDescr_Type = SnmpAdminString
_CfprOrgOrgDescr_Object = MibTableColumn
cfprOrgOrgDescr = _CfprOrgOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 4),
    _CfprOrgOrgDescr_Type()
)
cfprOrgOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgOrgDescr.setStatus("current")
_CfprOrgOrgFltAggr_Type = Unsigned64
_CfprOrgOrgFltAggr_Object = MibTableColumn
cfprOrgOrgFltAggr = _CfprOrgOrgFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 5),
    _CfprOrgOrgFltAggr_Type()
)
cfprOrgOrgFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgOrgFltAggr.setStatus("current")
_CfprOrgOrgLevel_Type = CfprOrgLevel
_CfprOrgOrgLevel_Object = MibTableColumn
cfprOrgOrgLevel = _CfprOrgOrgLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 6),
    _CfprOrgOrgLevel_Type()
)
cfprOrgOrgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgOrgLevel.setStatus("current")
_CfprOrgOrgName_Type = SnmpAdminString
_CfprOrgOrgName_Object = MibTableColumn
cfprOrgOrgName = _CfprOrgOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 7),
    _CfprOrgOrgName_Type()
)
cfprOrgOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgOrgName.setStatus("current")
_CfprOrgOrgPermAccess_Type = TruthValue
_CfprOrgOrgPermAccess_Object = MibTableColumn
cfprOrgOrgPermAccess = _CfprOrgOrgPermAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 1, 1, 8),
    _CfprOrgOrgPermAccess_Type()
)
cfprOrgOrgPermAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgOrgPermAccess.setStatus("current")
_CfprOrgSourceMaskTable_Object = MibTable
cfprOrgSourceMaskTable = _CfprOrgSourceMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 2)
)
if mibBuilder.loadTexts:
    cfprOrgSourceMaskTable.setStatus("current")
_CfprOrgSourceMaskEntry_Object = MibTableRow
cfprOrgSourceMaskEntry = _CfprOrgSourceMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 2, 1)
)
cfprOrgSourceMaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ORG-MIB", "cfprOrgSourceMaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOrgSourceMaskEntry.setStatus("current")
_CfprOrgSourceMaskInstanceId_Type = CfprManagedObjectId
_CfprOrgSourceMaskInstanceId_Object = MibTableColumn
cfprOrgSourceMaskInstanceId = _CfprOrgSourceMaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 2, 1, 1),
    _CfprOrgSourceMaskInstanceId_Type()
)
cfprOrgSourceMaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOrgSourceMaskInstanceId.setStatus("current")
_CfprOrgSourceMaskDn_Type = CfprManagedObjectDn
_CfprOrgSourceMaskDn_Object = MibTableColumn
cfprOrgSourceMaskDn = _CfprOrgSourceMaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 2, 1, 2),
    _CfprOrgSourceMaskDn_Type()
)
cfprOrgSourceMaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgSourceMaskDn.setStatus("current")
_CfprOrgSourceMaskRn_Type = SnmpAdminString
_CfprOrgSourceMaskRn_Object = MibTableColumn
cfprOrgSourceMaskRn = _CfprOrgSourceMaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 2, 1, 3),
    _CfprOrgSourceMaskRn_Type()
)
cfprOrgSourceMaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgSourceMaskRn.setStatus("current")
_CfprOrgSourceMaskMask_Type = CfprOrgSrcMask
_CfprOrgSourceMaskMask_Object = MibTableColumn
cfprOrgSourceMaskMask = _CfprOrgSourceMaskMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 58, 2, 1, 4),
    _CfprOrgSourceMaskMask_Type()
)
cfprOrgSourceMaskMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOrgSourceMaskMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-ORG-MIB",
    **{"cfprOrgObjects": cfprOrgObjects,
       "cfprOrgOrgTable": cfprOrgOrgTable,
       "cfprOrgOrgEntry": cfprOrgOrgEntry,
       "cfprOrgOrgInstanceId": cfprOrgOrgInstanceId,
       "cfprOrgOrgDn": cfprOrgOrgDn,
       "cfprOrgOrgRn": cfprOrgOrgRn,
       "cfprOrgOrgDescr": cfprOrgOrgDescr,
       "cfprOrgOrgFltAggr": cfprOrgOrgFltAggr,
       "cfprOrgOrgLevel": cfprOrgOrgLevel,
       "cfprOrgOrgName": cfprOrgOrgName,
       "cfprOrgOrgPermAccess": cfprOrgOrgPermAccess,
       "cfprOrgSourceMaskTable": cfprOrgSourceMaskTable,
       "cfprOrgSourceMaskEntry": cfprOrgSourceMaskEntry,
       "cfprOrgSourceMaskInstanceId": cfprOrgSourceMaskInstanceId,
       "cfprOrgSourceMaskDn": cfprOrgSourceMaskDn,
       "cfprOrgSourceMaskRn": cfprOrgSourceMaskRn,
       "cfprOrgSourceMaskMask": cfprOrgSourceMaskMask}
)
