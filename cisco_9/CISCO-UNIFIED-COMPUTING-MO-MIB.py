# SNMP MIB module (CISCO-UNIFIED-COMPUTING-MO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-COMPUTING-MO-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 08:59:13 2025
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

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsMoAnnotationOperState,
 CucsMoAnnotationOverride,
 CucsMoAnnotationOwner,
 CucsMoAnnotationTarget,
 CucsMoAnnotationType,
 CucsMoFileTxAdminState,
 CucsMoIpV4AddrKvType,
 CucsMoIpV6AddrKvType,
 CucsMoKvType,
 CucsMoVnicKvType) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsMoAnnotationOperState",
    "CucsMoAnnotationOverride",
    "CucsMoAnnotationOwner",
    "CucsMoAnnotationTarget",
    "CucsMoAnnotationType",
    "CucsMoFileTxAdminState",
    "CucsMoIpV4AddrKvType",
    "CucsMoIpV6AddrKvType",
    "CucsMoKvType",
    "CucsMoVnicKvType")

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

cucsMoObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsMoInvKvTable_Object = MibTable
cucsMoInvKvTable = _CucsMoInvKvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1)
)
if mibBuilder.loadTexts:
    cucsMoInvKvTable.setStatus("current")
_CucsMoInvKvEntry_Object = MibTableRow
cucsMoInvKvEntry = _CucsMoInvKvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1)
)
cucsMoInvKvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MO-MIB", "cucsMoInvKvInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMoInvKvEntry.setStatus("current")
_CucsMoInvKvInstanceId_Type = CucsManagedObjectId
_CucsMoInvKvInstanceId_Object = MibTableColumn
cucsMoInvKvInstanceId = _CucsMoInvKvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1, 1),
    _CucsMoInvKvInstanceId_Type()
)
cucsMoInvKvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMoInvKvInstanceId.setStatus("current")
_CucsMoInvKvDn_Type = CucsManagedObjectDn
_CucsMoInvKvDn_Object = MibTableColumn
cucsMoInvKvDn = _CucsMoInvKvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1, 2),
    _CucsMoInvKvDn_Type()
)
cucsMoInvKvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoInvKvDn.setStatus("current")
_CucsMoInvKvRn_Type = SnmpAdminString
_CucsMoInvKvRn_Object = MibTableColumn
cucsMoInvKvRn = _CucsMoInvKvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1, 3),
    _CucsMoInvKvRn_Type()
)
cucsMoInvKvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoInvKvRn.setStatus("current")
_CucsMoInvKvKey_Type = SnmpAdminString
_CucsMoInvKvKey_Object = MibTableColumn
cucsMoInvKvKey = _CucsMoInvKvKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1, 4),
    _CucsMoInvKvKey_Type()
)
cucsMoInvKvKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoInvKvKey.setStatus("current")
_CucsMoInvKvOwner_Type = CucsMoAnnotationOwner
_CucsMoInvKvOwner_Object = MibTableColumn
cucsMoInvKvOwner = _CucsMoInvKvOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1, 5),
    _CucsMoInvKvOwner_Type()
)
cucsMoInvKvOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoInvKvOwner.setStatus("current")
_CucsMoInvKvType_Type = CucsMoAnnotationType
_CucsMoInvKvType_Object = MibTableColumn
cucsMoInvKvType = _CucsMoInvKvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1, 6),
    _CucsMoInvKvType_Type()
)
cucsMoInvKvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoInvKvType.setStatus("current")
_CucsMoInvKvValue_Type = SnmpAdminString
_CucsMoInvKvValue_Object = MibTableColumn
cucsMoInvKvValue = _CucsMoInvKvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 1, 1, 7),
    _CucsMoInvKvValue_Type()
)
cucsMoInvKvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoInvKvValue.setStatus("current")
_CucsMoIpV4AddrKvTable_Object = MibTable
cucsMoIpV4AddrKvTable = _CucsMoIpV4AddrKvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2)
)
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvTable.setStatus("current")
_CucsMoIpV4AddrKvEntry_Object = MibTableRow
cucsMoIpV4AddrKvEntry = _CucsMoIpV4AddrKvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1)
)
cucsMoIpV4AddrKvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MO-MIB", "cucsMoIpV4AddrKvInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvEntry.setStatus("current")
_CucsMoIpV4AddrKvInstanceId_Type = CucsManagedObjectId
_CucsMoIpV4AddrKvInstanceId_Object = MibTableColumn
cucsMoIpV4AddrKvInstanceId = _CucsMoIpV4AddrKvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 1),
    _CucsMoIpV4AddrKvInstanceId_Type()
)
cucsMoIpV4AddrKvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvInstanceId.setStatus("current")
_CucsMoIpV4AddrKvDn_Type = CucsManagedObjectDn
_CucsMoIpV4AddrKvDn_Object = MibTableColumn
cucsMoIpV4AddrKvDn = _CucsMoIpV4AddrKvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 2),
    _CucsMoIpV4AddrKvDn_Type()
)
cucsMoIpV4AddrKvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvDn.setStatus("current")
_CucsMoIpV4AddrKvRn_Type = SnmpAdminString
_CucsMoIpV4AddrKvRn_Object = MibTableColumn
cucsMoIpV4AddrKvRn = _CucsMoIpV4AddrKvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 3),
    _CucsMoIpV4AddrKvRn_Type()
)
cucsMoIpV4AddrKvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvRn.setStatus("current")
_CucsMoIpV4AddrKvAddr_Type = InetAddressIPv4
_CucsMoIpV4AddrKvAddr_Object = MibTableColumn
cucsMoIpV4AddrKvAddr = _CucsMoIpV4AddrKvAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 4),
    _CucsMoIpV4AddrKvAddr_Type()
)
cucsMoIpV4AddrKvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvAddr.setStatus("current")
_CucsMoIpV4AddrKvDefGw_Type = InetAddressIPv4
_CucsMoIpV4AddrKvDefGw_Object = MibTableColumn
cucsMoIpV4AddrKvDefGw = _CucsMoIpV4AddrKvDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 5),
    _CucsMoIpV4AddrKvDefGw_Type()
)
cucsMoIpV4AddrKvDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvDefGw.setStatus("current")
_CucsMoIpV4AddrKvKey_Type = SnmpAdminString
_CucsMoIpV4AddrKvKey_Object = MibTableColumn
cucsMoIpV4AddrKvKey = _CucsMoIpV4AddrKvKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 6),
    _CucsMoIpV4AddrKvKey_Type()
)
cucsMoIpV4AddrKvKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvKey.setStatus("current")
_CucsMoIpV4AddrKvOperPoolName_Type = SnmpAdminString
_CucsMoIpV4AddrKvOperPoolName_Object = MibTableColumn
cucsMoIpV4AddrKvOperPoolName = _CucsMoIpV4AddrKvOperPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 7),
    _CucsMoIpV4AddrKvOperPoolName_Type()
)
cucsMoIpV4AddrKvOperPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvOperPoolName.setStatus("current")
_CucsMoIpV4AddrKvOwner_Type = CucsMoAnnotationOwner
_CucsMoIpV4AddrKvOwner_Object = MibTableColumn
cucsMoIpV4AddrKvOwner = _CucsMoIpV4AddrKvOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 8),
    _CucsMoIpV4AddrKvOwner_Type()
)
cucsMoIpV4AddrKvOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvOwner.setStatus("current")
_CucsMoIpV4AddrKvPoolName_Type = SnmpAdminString
_CucsMoIpV4AddrKvPoolName_Object = MibTableColumn
cucsMoIpV4AddrKvPoolName = _CucsMoIpV4AddrKvPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 9),
    _CucsMoIpV4AddrKvPoolName_Type()
)
cucsMoIpV4AddrKvPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvPoolName.setStatus("current")
_CucsMoIpV4AddrKvPrimDns_Type = InetAddressIPv4
_CucsMoIpV4AddrKvPrimDns_Object = MibTableColumn
cucsMoIpV4AddrKvPrimDns = _CucsMoIpV4AddrKvPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 10),
    _CucsMoIpV4AddrKvPrimDns_Type()
)
cucsMoIpV4AddrKvPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvPrimDns.setStatus("current")
_CucsMoIpV4AddrKvSecDns_Type = InetAddressIPv4
_CucsMoIpV4AddrKvSecDns_Object = MibTableColumn
cucsMoIpV4AddrKvSecDns = _CucsMoIpV4AddrKvSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 11),
    _CucsMoIpV4AddrKvSecDns_Type()
)
cucsMoIpV4AddrKvSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvSecDns.setStatus("current")
_CucsMoIpV4AddrKvSubnet_Type = InetAddressIPv4
_CucsMoIpV4AddrKvSubnet_Object = MibTableColumn
cucsMoIpV4AddrKvSubnet = _CucsMoIpV4AddrKvSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 12),
    _CucsMoIpV4AddrKvSubnet_Type()
)
cucsMoIpV4AddrKvSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvSubnet.setStatus("current")
_CucsMoIpV4AddrKvTarget_Type = CucsMoAnnotationTarget
_CucsMoIpV4AddrKvTarget_Object = MibTableColumn
cucsMoIpV4AddrKvTarget = _CucsMoIpV4AddrKvTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 13),
    _CucsMoIpV4AddrKvTarget_Type()
)
cucsMoIpV4AddrKvTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvTarget.setStatus("current")
_CucsMoIpV4AddrKvType_Type = CucsMoIpV4AddrKvType
_CucsMoIpV4AddrKvType_Object = MibTableColumn
cucsMoIpV4AddrKvType = _CucsMoIpV4AddrKvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 14),
    _CucsMoIpV4AddrKvType_Type()
)
cucsMoIpV4AddrKvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvType.setStatus("current")
_CucsMoIpV4AddrKvValue_Type = SnmpAdminString
_CucsMoIpV4AddrKvValue_Object = MibTableColumn
cucsMoIpV4AddrKvValue = _CucsMoIpV4AddrKvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 2, 1, 15),
    _CucsMoIpV4AddrKvValue_Type()
)
cucsMoIpV4AddrKvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV4AddrKvValue.setStatus("current")
_CucsMoIpV6AddrKvTable_Object = MibTable
cucsMoIpV6AddrKvTable = _CucsMoIpV6AddrKvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3)
)
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvTable.setStatus("current")
_CucsMoIpV6AddrKvEntry_Object = MibTableRow
cucsMoIpV6AddrKvEntry = _CucsMoIpV6AddrKvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1)
)
cucsMoIpV6AddrKvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MO-MIB", "cucsMoIpV6AddrKvInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvEntry.setStatus("current")
_CucsMoIpV6AddrKvInstanceId_Type = CucsManagedObjectId
_CucsMoIpV6AddrKvInstanceId_Object = MibTableColumn
cucsMoIpV6AddrKvInstanceId = _CucsMoIpV6AddrKvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 1),
    _CucsMoIpV6AddrKvInstanceId_Type()
)
cucsMoIpV6AddrKvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvInstanceId.setStatus("current")
_CucsMoIpV6AddrKvDn_Type = CucsManagedObjectDn
_CucsMoIpV6AddrKvDn_Object = MibTableColumn
cucsMoIpV6AddrKvDn = _CucsMoIpV6AddrKvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 2),
    _CucsMoIpV6AddrKvDn_Type()
)
cucsMoIpV6AddrKvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvDn.setStatus("current")
_CucsMoIpV6AddrKvRn_Type = SnmpAdminString
_CucsMoIpV6AddrKvRn_Object = MibTableColumn
cucsMoIpV6AddrKvRn = _CucsMoIpV6AddrKvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 3),
    _CucsMoIpV6AddrKvRn_Type()
)
cucsMoIpV6AddrKvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvRn.setStatus("current")
_CucsMoIpV6AddrKvAddr_Type = InetAddressIPv6
_CucsMoIpV6AddrKvAddr_Object = MibTableColumn
cucsMoIpV6AddrKvAddr = _CucsMoIpV6AddrKvAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 4),
    _CucsMoIpV6AddrKvAddr_Type()
)
cucsMoIpV6AddrKvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvAddr.setStatus("current")
_CucsMoIpV6AddrKvDefGw_Type = InetAddressIPv6
_CucsMoIpV6AddrKvDefGw_Object = MibTableColumn
cucsMoIpV6AddrKvDefGw = _CucsMoIpV6AddrKvDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 5),
    _CucsMoIpV6AddrKvDefGw_Type()
)
cucsMoIpV6AddrKvDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvDefGw.setStatus("current")
_CucsMoIpV6AddrKvKey_Type = SnmpAdminString
_CucsMoIpV6AddrKvKey_Object = MibTableColumn
cucsMoIpV6AddrKvKey = _CucsMoIpV6AddrKvKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 6),
    _CucsMoIpV6AddrKvKey_Type()
)
cucsMoIpV6AddrKvKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvKey.setStatus("current")
_CucsMoIpV6AddrKvOperPoolName_Type = SnmpAdminString
_CucsMoIpV6AddrKvOperPoolName_Object = MibTableColumn
cucsMoIpV6AddrKvOperPoolName = _CucsMoIpV6AddrKvOperPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 7),
    _CucsMoIpV6AddrKvOperPoolName_Type()
)
cucsMoIpV6AddrKvOperPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvOperPoolName.setStatus("current")
_CucsMoIpV6AddrKvOwner_Type = CucsMoAnnotationOwner
_CucsMoIpV6AddrKvOwner_Object = MibTableColumn
cucsMoIpV6AddrKvOwner = _CucsMoIpV6AddrKvOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 8),
    _CucsMoIpV6AddrKvOwner_Type()
)
cucsMoIpV6AddrKvOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvOwner.setStatus("current")
_CucsMoIpV6AddrKvPoolName_Type = SnmpAdminString
_CucsMoIpV6AddrKvPoolName_Object = MibTableColumn
cucsMoIpV6AddrKvPoolName = _CucsMoIpV6AddrKvPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 9),
    _CucsMoIpV6AddrKvPoolName_Type()
)
cucsMoIpV6AddrKvPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvPoolName.setStatus("current")
_CucsMoIpV6AddrKvPrefix_Type = Gauge32
_CucsMoIpV6AddrKvPrefix_Object = MibTableColumn
cucsMoIpV6AddrKvPrefix = _CucsMoIpV6AddrKvPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 10),
    _CucsMoIpV6AddrKvPrefix_Type()
)
cucsMoIpV6AddrKvPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvPrefix.setStatus("current")
_CucsMoIpV6AddrKvPrimDns_Type = InetAddressIPv6
_CucsMoIpV6AddrKvPrimDns_Object = MibTableColumn
cucsMoIpV6AddrKvPrimDns = _CucsMoIpV6AddrKvPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 11),
    _CucsMoIpV6AddrKvPrimDns_Type()
)
cucsMoIpV6AddrKvPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvPrimDns.setStatus("current")
_CucsMoIpV6AddrKvSecDns_Type = InetAddressIPv6
_CucsMoIpV6AddrKvSecDns_Object = MibTableColumn
cucsMoIpV6AddrKvSecDns = _CucsMoIpV6AddrKvSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 12),
    _CucsMoIpV6AddrKvSecDns_Type()
)
cucsMoIpV6AddrKvSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvSecDns.setStatus("current")
_CucsMoIpV6AddrKvTarget_Type = CucsMoAnnotationTarget
_CucsMoIpV6AddrKvTarget_Object = MibTableColumn
cucsMoIpV6AddrKvTarget = _CucsMoIpV6AddrKvTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 13),
    _CucsMoIpV6AddrKvTarget_Type()
)
cucsMoIpV6AddrKvTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvTarget.setStatus("current")
_CucsMoIpV6AddrKvType_Type = CucsMoIpV6AddrKvType
_CucsMoIpV6AddrKvType_Object = MibTableColumn
cucsMoIpV6AddrKvType = _CucsMoIpV6AddrKvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 14),
    _CucsMoIpV6AddrKvType_Type()
)
cucsMoIpV6AddrKvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvType.setStatus("current")
_CucsMoIpV6AddrKvValue_Type = SnmpAdminString
_CucsMoIpV6AddrKvValue_Object = MibTableColumn
cucsMoIpV6AddrKvValue = _CucsMoIpV6AddrKvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 3, 1, 15),
    _CucsMoIpV6AddrKvValue_Type()
)
cucsMoIpV6AddrKvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoIpV6AddrKvValue.setStatus("current")
_CucsMoKvTable_Object = MibTable
cucsMoKvTable = _CucsMoKvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4)
)
if mibBuilder.loadTexts:
    cucsMoKvTable.setStatus("current")
_CucsMoKvEntry_Object = MibTableRow
cucsMoKvEntry = _CucsMoKvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1)
)
cucsMoKvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MO-MIB", "cucsMoKvInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMoKvEntry.setStatus("current")
_CucsMoKvInstanceId_Type = CucsManagedObjectId
_CucsMoKvInstanceId_Object = MibTableColumn
cucsMoKvInstanceId = _CucsMoKvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 1),
    _CucsMoKvInstanceId_Type()
)
cucsMoKvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMoKvInstanceId.setStatus("current")
_CucsMoKvDn_Type = CucsManagedObjectDn
_CucsMoKvDn_Object = MibTableColumn
cucsMoKvDn = _CucsMoKvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 2),
    _CucsMoKvDn_Type()
)
cucsMoKvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvDn.setStatus("current")
_CucsMoKvRn_Type = SnmpAdminString
_CucsMoKvRn_Object = MibTableColumn
cucsMoKvRn = _CucsMoKvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 3),
    _CucsMoKvRn_Type()
)
cucsMoKvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvRn.setStatus("current")
_CucsMoKvKey_Type = SnmpAdminString
_CucsMoKvKey_Object = MibTableColumn
cucsMoKvKey = _CucsMoKvKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 4),
    _CucsMoKvKey_Type()
)
cucsMoKvKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvKey.setStatus("current")
_CucsMoKvOverride_Type = CucsMoAnnotationOverride
_CucsMoKvOverride_Object = MibTableColumn
cucsMoKvOverride = _CucsMoKvOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 5),
    _CucsMoKvOverride_Type()
)
cucsMoKvOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvOverride.setStatus("current")
_CucsMoKvOwner_Type = CucsMoAnnotationOwner
_CucsMoKvOwner_Object = MibTableColumn
cucsMoKvOwner = _CucsMoKvOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 6),
    _CucsMoKvOwner_Type()
)
cucsMoKvOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvOwner.setStatus("current")
_CucsMoKvTarget_Type = CucsMoAnnotationTarget
_CucsMoKvTarget_Object = MibTableColumn
cucsMoKvTarget = _CucsMoKvTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 7),
    _CucsMoKvTarget_Type()
)
cucsMoKvTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvTarget.setStatus("current")
_CucsMoKvType_Type = CucsMoKvType
_CucsMoKvType_Object = MibTableColumn
cucsMoKvType = _CucsMoKvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 8),
    _CucsMoKvType_Type()
)
cucsMoKvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvType.setStatus("current")
_CucsMoKvValue_Type = SnmpAdminString
_CucsMoKvValue_Object = MibTableColumn
cucsMoKvValue = _CucsMoKvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 4, 1, 9),
    _CucsMoKvValue_Type()
)
cucsMoKvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvValue.setStatus("current")
_CucsMoKvCfgHolderTable_Object = MibTable
cucsMoKvCfgHolderTable = _CucsMoKvCfgHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 5)
)
if mibBuilder.loadTexts:
    cucsMoKvCfgHolderTable.setStatus("current")
_CucsMoKvCfgHolderEntry_Object = MibTableRow
cucsMoKvCfgHolderEntry = _CucsMoKvCfgHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 5, 1)
)
cucsMoKvCfgHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MO-MIB", "cucsMoKvCfgHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMoKvCfgHolderEntry.setStatus("current")
_CucsMoKvCfgHolderInstanceId_Type = CucsManagedObjectId
_CucsMoKvCfgHolderInstanceId_Object = MibTableColumn
cucsMoKvCfgHolderInstanceId = _CucsMoKvCfgHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 5, 1, 1),
    _CucsMoKvCfgHolderInstanceId_Type()
)
cucsMoKvCfgHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMoKvCfgHolderInstanceId.setStatus("current")
_CucsMoKvCfgHolderDn_Type = CucsManagedObjectDn
_CucsMoKvCfgHolderDn_Object = MibTableColumn
cucsMoKvCfgHolderDn = _CucsMoKvCfgHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 5, 1, 2),
    _CucsMoKvCfgHolderDn_Type()
)
cucsMoKvCfgHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvCfgHolderDn.setStatus("current")
_CucsMoKvCfgHolderRn_Type = SnmpAdminString
_CucsMoKvCfgHolderRn_Object = MibTableColumn
cucsMoKvCfgHolderRn = _CucsMoKvCfgHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 5, 1, 3),
    _CucsMoKvCfgHolderRn_Type()
)
cucsMoKvCfgHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvCfgHolderRn.setStatus("current")
_CucsMoKvCfgHolderFileTxAdminState_Type = CucsMoFileTxAdminState
_CucsMoKvCfgHolderFileTxAdminState_Object = MibTableColumn
cucsMoKvCfgHolderFileTxAdminState = _CucsMoKvCfgHolderFileTxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 5, 1, 4),
    _CucsMoKvCfgHolderFileTxAdminState_Type()
)
cucsMoKvCfgHolderFileTxAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvCfgHolderFileTxAdminState.setStatus("current")
_CucsMoKvCfgHolderOperState_Type = CucsMoAnnotationOperState
_CucsMoKvCfgHolderOperState_Object = MibTableColumn
cucsMoKvCfgHolderOperState = _CucsMoKvCfgHolderOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 5, 1, 5),
    _CucsMoKvCfgHolderOperState_Type()
)
cucsMoKvCfgHolderOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvCfgHolderOperState.setStatus("current")
_CucsMoKvInvHolderTable_Object = MibTable
cucsMoKvInvHolderTable = _CucsMoKvInvHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 6)
)
if mibBuilder.loadTexts:
    cucsMoKvInvHolderTable.setStatus("current")
_CucsMoKvInvHolderEntry_Object = MibTableRow
cucsMoKvInvHolderEntry = _CucsMoKvInvHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 6, 1)
)
cucsMoKvInvHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MO-MIB", "cucsMoKvInvHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMoKvInvHolderEntry.setStatus("current")
_CucsMoKvInvHolderInstanceId_Type = CucsManagedObjectId
_CucsMoKvInvHolderInstanceId_Object = MibTableColumn
cucsMoKvInvHolderInstanceId = _CucsMoKvInvHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 6, 1, 1),
    _CucsMoKvInvHolderInstanceId_Type()
)
cucsMoKvInvHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMoKvInvHolderInstanceId.setStatus("current")
_CucsMoKvInvHolderDn_Type = CucsManagedObjectDn
_CucsMoKvInvHolderDn_Object = MibTableColumn
cucsMoKvInvHolderDn = _CucsMoKvInvHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 6, 1, 2),
    _CucsMoKvInvHolderDn_Type()
)
cucsMoKvInvHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvInvHolderDn.setStatus("current")
_CucsMoKvInvHolderRn_Type = SnmpAdminString
_CucsMoKvInvHolderRn_Object = MibTableColumn
cucsMoKvInvHolderRn = _CucsMoKvInvHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 6, 1, 3),
    _CucsMoKvInvHolderRn_Type()
)
cucsMoKvInvHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvInvHolderRn.setStatus("current")
_CucsMoKvInvHolderEndpoint_Type = SnmpAdminString
_CucsMoKvInvHolderEndpoint_Object = MibTableColumn
cucsMoKvInvHolderEndpoint = _CucsMoKvInvHolderEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 6, 1, 4),
    _CucsMoKvInvHolderEndpoint_Type()
)
cucsMoKvInvHolderEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvInvHolderEndpoint.setStatus("current")
_CucsMoKvInvHolderLastUpdate_Type = DateAndTime
_CucsMoKvInvHolderLastUpdate_Object = MibTableColumn
cucsMoKvInvHolderLastUpdate = _CucsMoKvInvHolderLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 6, 1, 5),
    _CucsMoKvInvHolderLastUpdate_Type()
)
cucsMoKvInvHolderLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoKvInvHolderLastUpdate.setStatus("current")
_CucsMoVnicKvTable_Object = MibTable
cucsMoVnicKvTable = _CucsMoVnicKvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7)
)
if mibBuilder.loadTexts:
    cucsMoVnicKvTable.setStatus("current")
_CucsMoVnicKvEntry_Object = MibTableRow
cucsMoVnicKvEntry = _CucsMoVnicKvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1)
)
cucsMoVnicKvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MO-MIB", "cucsMoVnicKvInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMoVnicKvEntry.setStatus("current")
_CucsMoVnicKvInstanceId_Type = CucsManagedObjectId
_CucsMoVnicKvInstanceId_Object = MibTableColumn
cucsMoVnicKvInstanceId = _CucsMoVnicKvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 1),
    _CucsMoVnicKvInstanceId_Type()
)
cucsMoVnicKvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMoVnicKvInstanceId.setStatus("current")
_CucsMoVnicKvDn_Type = CucsManagedObjectDn
_CucsMoVnicKvDn_Object = MibTableColumn
cucsMoVnicKvDn = _CucsMoVnicKvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 2),
    _CucsMoVnicKvDn_Type()
)
cucsMoVnicKvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvDn.setStatus("current")
_CucsMoVnicKvRn_Type = SnmpAdminString
_CucsMoVnicKvRn_Object = MibTableColumn
cucsMoVnicKvRn = _CucsMoVnicKvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 3),
    _CucsMoVnicKvRn_Type()
)
cucsMoVnicKvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvRn.setStatus("current")
_CucsMoVnicKvKey_Type = SnmpAdminString
_CucsMoVnicKvKey_Object = MibTableColumn
cucsMoVnicKvKey = _CucsMoVnicKvKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 4),
    _CucsMoVnicKvKey_Type()
)
cucsMoVnicKvKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvKey.setStatus("current")
_CucsMoVnicKvOwner_Type = CucsMoAnnotationOwner
_CucsMoVnicKvOwner_Object = MibTableColumn
cucsMoVnicKvOwner = _CucsMoVnicKvOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 5),
    _CucsMoVnicKvOwner_Type()
)
cucsMoVnicKvOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvOwner.setStatus("current")
_CucsMoVnicKvTarget_Type = CucsMoAnnotationTarget
_CucsMoVnicKvTarget_Object = MibTableColumn
cucsMoVnicKvTarget = _CucsMoVnicKvTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 6),
    _CucsMoVnicKvTarget_Type()
)
cucsMoVnicKvTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvTarget.setStatus("current")
_CucsMoVnicKvType_Type = CucsMoVnicKvType
_CucsMoVnicKvType_Object = MibTableColumn
cucsMoVnicKvType = _CucsMoVnicKvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 7),
    _CucsMoVnicKvType_Type()
)
cucsMoVnicKvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvType.setStatus("current")
_CucsMoVnicKvValue_Type = SnmpAdminString
_CucsMoVnicKvValue_Object = MibTableColumn
cucsMoVnicKvValue = _CucsMoVnicKvValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 8),
    _CucsMoVnicKvValue_Type()
)
cucsMoVnicKvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvValue.setStatus("current")
_CucsMoVnicKvVnicEtherDn_Type = SnmpAdminString
_CucsMoVnicKvVnicEtherDn_Object = MibTableColumn
cucsMoVnicKvVnicEtherDn = _CucsMoVnicKvVnicEtherDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 9),
    _CucsMoVnicKvVnicEtherDn_Type()
)
cucsMoVnicKvVnicEtherDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvVnicEtherDn.setStatus("current")
_CucsMoVnicKvVnicName_Type = SnmpAdminString
_CucsMoVnicKvVnicName_Object = MibTableColumn
cucsMoVnicKvVnicName = _CucsMoVnicKvVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 96, 7, 1, 10),
    _CucsMoVnicKvVnicName_Type()
)
cucsMoVnicKvVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMoVnicKvVnicName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-MO-MIB",
    **{"cucsMoObjects": cucsMoObjects,
       "cucsMoInvKvTable": cucsMoInvKvTable,
       "cucsMoInvKvEntry": cucsMoInvKvEntry,
       "cucsMoInvKvInstanceId": cucsMoInvKvInstanceId,
       "cucsMoInvKvDn": cucsMoInvKvDn,
       "cucsMoInvKvRn": cucsMoInvKvRn,
       "cucsMoInvKvKey": cucsMoInvKvKey,
       "cucsMoInvKvOwner": cucsMoInvKvOwner,
       "cucsMoInvKvType": cucsMoInvKvType,
       "cucsMoInvKvValue": cucsMoInvKvValue,
       "cucsMoIpV4AddrKvTable": cucsMoIpV4AddrKvTable,
       "cucsMoIpV4AddrKvEntry": cucsMoIpV4AddrKvEntry,
       "cucsMoIpV4AddrKvInstanceId": cucsMoIpV4AddrKvInstanceId,
       "cucsMoIpV4AddrKvDn": cucsMoIpV4AddrKvDn,
       "cucsMoIpV4AddrKvRn": cucsMoIpV4AddrKvRn,
       "cucsMoIpV4AddrKvAddr": cucsMoIpV4AddrKvAddr,
       "cucsMoIpV4AddrKvDefGw": cucsMoIpV4AddrKvDefGw,
       "cucsMoIpV4AddrKvKey": cucsMoIpV4AddrKvKey,
       "cucsMoIpV4AddrKvOperPoolName": cucsMoIpV4AddrKvOperPoolName,
       "cucsMoIpV4AddrKvOwner": cucsMoIpV4AddrKvOwner,
       "cucsMoIpV4AddrKvPoolName": cucsMoIpV4AddrKvPoolName,
       "cucsMoIpV4AddrKvPrimDns": cucsMoIpV4AddrKvPrimDns,
       "cucsMoIpV4AddrKvSecDns": cucsMoIpV4AddrKvSecDns,
       "cucsMoIpV4AddrKvSubnet": cucsMoIpV4AddrKvSubnet,
       "cucsMoIpV4AddrKvTarget": cucsMoIpV4AddrKvTarget,
       "cucsMoIpV4AddrKvType": cucsMoIpV4AddrKvType,
       "cucsMoIpV4AddrKvValue": cucsMoIpV4AddrKvValue,
       "cucsMoIpV6AddrKvTable": cucsMoIpV6AddrKvTable,
       "cucsMoIpV6AddrKvEntry": cucsMoIpV6AddrKvEntry,
       "cucsMoIpV6AddrKvInstanceId": cucsMoIpV6AddrKvInstanceId,
       "cucsMoIpV6AddrKvDn": cucsMoIpV6AddrKvDn,
       "cucsMoIpV6AddrKvRn": cucsMoIpV6AddrKvRn,
       "cucsMoIpV6AddrKvAddr": cucsMoIpV6AddrKvAddr,
       "cucsMoIpV6AddrKvDefGw": cucsMoIpV6AddrKvDefGw,
       "cucsMoIpV6AddrKvKey": cucsMoIpV6AddrKvKey,
       "cucsMoIpV6AddrKvOperPoolName": cucsMoIpV6AddrKvOperPoolName,
       "cucsMoIpV6AddrKvOwner": cucsMoIpV6AddrKvOwner,
       "cucsMoIpV6AddrKvPoolName": cucsMoIpV6AddrKvPoolName,
       "cucsMoIpV6AddrKvPrefix": cucsMoIpV6AddrKvPrefix,
       "cucsMoIpV6AddrKvPrimDns": cucsMoIpV6AddrKvPrimDns,
       "cucsMoIpV6AddrKvSecDns": cucsMoIpV6AddrKvSecDns,
       "cucsMoIpV6AddrKvTarget": cucsMoIpV6AddrKvTarget,
       "cucsMoIpV6AddrKvType": cucsMoIpV6AddrKvType,
       "cucsMoIpV6AddrKvValue": cucsMoIpV6AddrKvValue,
       "cucsMoKvTable": cucsMoKvTable,
       "cucsMoKvEntry": cucsMoKvEntry,
       "cucsMoKvInstanceId": cucsMoKvInstanceId,
       "cucsMoKvDn": cucsMoKvDn,
       "cucsMoKvRn": cucsMoKvRn,
       "cucsMoKvKey": cucsMoKvKey,
       "cucsMoKvOverride": cucsMoKvOverride,
       "cucsMoKvOwner": cucsMoKvOwner,
       "cucsMoKvTarget": cucsMoKvTarget,
       "cucsMoKvType": cucsMoKvType,
       "cucsMoKvValue": cucsMoKvValue,
       "cucsMoKvCfgHolderTable": cucsMoKvCfgHolderTable,
       "cucsMoKvCfgHolderEntry": cucsMoKvCfgHolderEntry,
       "cucsMoKvCfgHolderInstanceId": cucsMoKvCfgHolderInstanceId,
       "cucsMoKvCfgHolderDn": cucsMoKvCfgHolderDn,
       "cucsMoKvCfgHolderRn": cucsMoKvCfgHolderRn,
       "cucsMoKvCfgHolderFileTxAdminState": cucsMoKvCfgHolderFileTxAdminState,
       "cucsMoKvCfgHolderOperState": cucsMoKvCfgHolderOperState,
       "cucsMoKvInvHolderTable": cucsMoKvInvHolderTable,
       "cucsMoKvInvHolderEntry": cucsMoKvInvHolderEntry,
       "cucsMoKvInvHolderInstanceId": cucsMoKvInvHolderInstanceId,
       "cucsMoKvInvHolderDn": cucsMoKvInvHolderDn,
       "cucsMoKvInvHolderRn": cucsMoKvInvHolderRn,
       "cucsMoKvInvHolderEndpoint": cucsMoKvInvHolderEndpoint,
       "cucsMoKvInvHolderLastUpdate": cucsMoKvInvHolderLastUpdate,
       "cucsMoVnicKvTable": cucsMoVnicKvTable,
       "cucsMoVnicKvEntry": cucsMoVnicKvEntry,
       "cucsMoVnicKvInstanceId": cucsMoVnicKvInstanceId,
       "cucsMoVnicKvDn": cucsMoVnicKvDn,
       "cucsMoVnicKvRn": cucsMoVnicKvRn,
       "cucsMoVnicKvKey": cucsMoVnicKvKey,
       "cucsMoVnicKvOwner": cucsMoVnicKvOwner,
       "cucsMoVnicKvTarget": cucsMoVnicKvTarget,
       "cucsMoVnicKvType": cucsMoVnicKvType,
       "cucsMoVnicKvValue": cucsMoVnicKvValue,
       "cucsMoVnicKvVnicEtherDn": cucsMoVnicKvVnicEtherDn,
       "cucsMoVnicKvVnicName": cucsMoVnicKvVnicName}
)
