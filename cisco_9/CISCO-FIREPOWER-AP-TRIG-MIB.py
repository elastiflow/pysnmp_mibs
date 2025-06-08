# SNMP MIB module (CISCO-FIREPOWER-AP-TRIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-TRIG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:39 2025
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

(CfprApPolicyPolicyOwner,
 CfprApTrigAdminState,
 CfprApTrigDay,
 CfprApTrigOperState,
 CfprApTrigTokenOperState,
 CfprApTrigTrigOperState,
 CfprApTrigTriggeredState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApPolicyPolicyOwner",
    "CfprApTrigAdminState",
    "CfprApTrigDay",
    "CfprApTrigOperState",
    "CfprApTrigTokenOperState",
    "CfprApTrigTrigOperState",
    "CfprApTrigTriggeredState")

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

cfprApTrigObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApTrigAbsWindowTable_Object = MibTable
cfprApTrigAbsWindowTable = _CfprApTrigAbsWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1)
)
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowTable.setStatus("current")
_CfprApTrigAbsWindowEntry_Object = MibTableRow
cfprApTrigAbsWindowEntry = _CfprApTrigAbsWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1)
)
cfprApTrigAbsWindowEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigAbsWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowEntry.setStatus("current")
_CfprApTrigAbsWindowInstanceId_Type = CfprApManagedObjectId
_CfprApTrigAbsWindowInstanceId_Object = MibTableColumn
cfprApTrigAbsWindowInstanceId = _CfprApTrigAbsWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 1),
    _CfprApTrigAbsWindowInstanceId_Type()
)
cfprApTrigAbsWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowInstanceId.setStatus("current")
_CfprApTrigAbsWindowDn_Type = CfprApManagedObjectDn
_CfprApTrigAbsWindowDn_Object = MibTableColumn
cfprApTrigAbsWindowDn = _CfprApTrigAbsWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 2),
    _CfprApTrigAbsWindowDn_Type()
)
cfprApTrigAbsWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowDn.setStatus("current")
_CfprApTrigAbsWindowRn_Type = SnmpAdminString
_CfprApTrigAbsWindowRn_Object = MibTableColumn
cfprApTrigAbsWindowRn = _CfprApTrigAbsWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 3),
    _CfprApTrigAbsWindowRn_Type()
)
cfprApTrigAbsWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowRn.setStatus("current")
_CfprApTrigAbsWindowConcurCap_Type = Gauge32
_CfprApTrigAbsWindowConcurCap_Object = MibTableColumn
cfprApTrigAbsWindowConcurCap = _CfprApTrigAbsWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 4),
    _CfprApTrigAbsWindowConcurCap_Type()
)
cfprApTrigAbsWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowConcurCap.setStatus("current")
_CfprApTrigAbsWindowDate_Type = DateAndTime
_CfprApTrigAbsWindowDate_Object = MibTableColumn
cfprApTrigAbsWindowDate = _CfprApTrigAbsWindowDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 5),
    _CfprApTrigAbsWindowDate_Type()
)
cfprApTrigAbsWindowDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowDate.setStatus("current")
_CfprApTrigAbsWindowJobCount_Type = Gauge32
_CfprApTrigAbsWindowJobCount_Object = MibTableColumn
cfprApTrigAbsWindowJobCount = _CfprApTrigAbsWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 6),
    _CfprApTrigAbsWindowJobCount_Type()
)
cfprApTrigAbsWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowJobCount.setStatus("current")
_CfprApTrigAbsWindowName_Type = SnmpAdminString
_CfprApTrigAbsWindowName_Object = MibTableColumn
cfprApTrigAbsWindowName = _CfprApTrigAbsWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 7),
    _CfprApTrigAbsWindowName_Type()
)
cfprApTrigAbsWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowName.setStatus("current")
_CfprApTrigAbsWindowProcBreak_Type = SnmpAdminString
_CfprApTrigAbsWindowProcBreak_Object = MibTableColumn
cfprApTrigAbsWindowProcBreak = _CfprApTrigAbsWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 8),
    _CfprApTrigAbsWindowProcBreak_Type()
)
cfprApTrigAbsWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowProcBreak.setStatus("current")
_CfprApTrigAbsWindowProcCap_Type = Gauge32
_CfprApTrigAbsWindowProcCap_Object = MibTableColumn
cfprApTrigAbsWindowProcCap = _CfprApTrigAbsWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 9),
    _CfprApTrigAbsWindowProcCap_Type()
)
cfprApTrigAbsWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowProcCap.setStatus("current")
_CfprApTrigAbsWindowTimeCap_Type = SnmpAdminString
_CfprApTrigAbsWindowTimeCap_Object = MibTableColumn
cfprApTrigAbsWindowTimeCap = _CfprApTrigAbsWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 1, 1, 10),
    _CfprApTrigAbsWindowTimeCap_Type()
)
cfprApTrigAbsWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigAbsWindowTimeCap.setStatus("current")
_CfprApTrigClientTokenTable_Object = MibTable
cfprApTrigClientTokenTable = _CfprApTrigClientTokenTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2)
)
if mibBuilder.loadTexts:
    cfprApTrigClientTokenTable.setStatus("current")
_CfprApTrigClientTokenEntry_Object = MibTableRow
cfprApTrigClientTokenEntry = _CfprApTrigClientTokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2, 1)
)
cfprApTrigClientTokenEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigClientTokenInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigClientTokenEntry.setStatus("current")
_CfprApTrigClientTokenInstanceId_Type = CfprApManagedObjectId
_CfprApTrigClientTokenInstanceId_Object = MibTableColumn
cfprApTrigClientTokenInstanceId = _CfprApTrigClientTokenInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2, 1, 1),
    _CfprApTrigClientTokenInstanceId_Type()
)
cfprApTrigClientTokenInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigClientTokenInstanceId.setStatus("current")
_CfprApTrigClientTokenDn_Type = CfprApManagedObjectDn
_CfprApTrigClientTokenDn_Object = MibTableColumn
cfprApTrigClientTokenDn = _CfprApTrigClientTokenDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2, 1, 2),
    _CfprApTrigClientTokenDn_Type()
)
cfprApTrigClientTokenDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigClientTokenDn.setStatus("current")
_CfprApTrigClientTokenRn_Type = SnmpAdminString
_CfprApTrigClientTokenRn_Object = MibTableColumn
cfprApTrigClientTokenRn = _CfprApTrigClientTokenRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2, 1, 3),
    _CfprApTrigClientTokenRn_Type()
)
cfprApTrigClientTokenRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigClientTokenRn.setStatus("current")
_CfprApTrigClientTokenActivityTs_Type = DateAndTime
_CfprApTrigClientTokenActivityTs_Object = MibTableColumn
cfprApTrigClientTokenActivityTs = _CfprApTrigClientTokenActivityTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2, 1, 4),
    _CfprApTrigClientTokenActivityTs_Type()
)
cfprApTrigClientTokenActivityTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigClientTokenActivityTs.setStatus("current")
_CfprApTrigClientTokenId_Type = Unsigned64
_CfprApTrigClientTokenId_Object = MibTableColumn
cfprApTrigClientTokenId = _CfprApTrigClientTokenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2, 1, 5),
    _CfprApTrigClientTokenId_Type()
)
cfprApTrigClientTokenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigClientTokenId.setStatus("current")
_CfprApTrigClientTokenOperState_Type = CfprApTrigTokenOperState
_CfprApTrigClientTokenOperState_Object = MibTableColumn
cfprApTrigClientTokenOperState = _CfprApTrigClientTokenOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 2, 1, 6),
    _CfprApTrigClientTokenOperState_Type()
)
cfprApTrigClientTokenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigClientTokenOperState.setStatus("current")
_CfprApTrigLocalAbsWindowTable_Object = MibTable
cfprApTrigLocalAbsWindowTable = _CfprApTrigLocalAbsWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3)
)
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowTable.setStatus("current")
_CfprApTrigLocalAbsWindowEntry_Object = MibTableRow
cfprApTrigLocalAbsWindowEntry = _CfprApTrigLocalAbsWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1)
)
cfprApTrigLocalAbsWindowEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigLocalAbsWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowEntry.setStatus("current")
_CfprApTrigLocalAbsWindowInstanceId_Type = CfprApManagedObjectId
_CfprApTrigLocalAbsWindowInstanceId_Object = MibTableColumn
cfprApTrigLocalAbsWindowInstanceId = _CfprApTrigLocalAbsWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 1),
    _CfprApTrigLocalAbsWindowInstanceId_Type()
)
cfprApTrigLocalAbsWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowInstanceId.setStatus("current")
_CfprApTrigLocalAbsWindowDn_Type = CfprApManagedObjectDn
_CfprApTrigLocalAbsWindowDn_Object = MibTableColumn
cfprApTrigLocalAbsWindowDn = _CfprApTrigLocalAbsWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 2),
    _CfprApTrigLocalAbsWindowDn_Type()
)
cfprApTrigLocalAbsWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowDn.setStatus("current")
_CfprApTrigLocalAbsWindowRn_Type = SnmpAdminString
_CfprApTrigLocalAbsWindowRn_Object = MibTableColumn
cfprApTrigLocalAbsWindowRn = _CfprApTrigLocalAbsWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 3),
    _CfprApTrigLocalAbsWindowRn_Type()
)
cfprApTrigLocalAbsWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowRn.setStatus("current")
_CfprApTrigLocalAbsWindowConcurCap_Type = Gauge32
_CfprApTrigLocalAbsWindowConcurCap_Object = MibTableColumn
cfprApTrigLocalAbsWindowConcurCap = _CfprApTrigLocalAbsWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 4),
    _CfprApTrigLocalAbsWindowConcurCap_Type()
)
cfprApTrigLocalAbsWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowConcurCap.setStatus("current")
_CfprApTrigLocalAbsWindowDate_Type = DateAndTime
_CfprApTrigLocalAbsWindowDate_Object = MibTableColumn
cfprApTrigLocalAbsWindowDate = _CfprApTrigLocalAbsWindowDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 5),
    _CfprApTrigLocalAbsWindowDate_Type()
)
cfprApTrigLocalAbsWindowDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowDate.setStatus("current")
_CfprApTrigLocalAbsWindowJobCount_Type = Gauge32
_CfprApTrigLocalAbsWindowJobCount_Object = MibTableColumn
cfprApTrigLocalAbsWindowJobCount = _CfprApTrigLocalAbsWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 6),
    _CfprApTrigLocalAbsWindowJobCount_Type()
)
cfprApTrigLocalAbsWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowJobCount.setStatus("current")
_CfprApTrigLocalAbsWindowName_Type = SnmpAdminString
_CfprApTrigLocalAbsWindowName_Object = MibTableColumn
cfprApTrigLocalAbsWindowName = _CfprApTrigLocalAbsWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 7),
    _CfprApTrigLocalAbsWindowName_Type()
)
cfprApTrigLocalAbsWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowName.setStatus("current")
_CfprApTrigLocalAbsWindowProcBreak_Type = SnmpAdminString
_CfprApTrigLocalAbsWindowProcBreak_Object = MibTableColumn
cfprApTrigLocalAbsWindowProcBreak = _CfprApTrigLocalAbsWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 8),
    _CfprApTrigLocalAbsWindowProcBreak_Type()
)
cfprApTrigLocalAbsWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowProcBreak.setStatus("current")
_CfprApTrigLocalAbsWindowProcCap_Type = Gauge32
_CfprApTrigLocalAbsWindowProcCap_Object = MibTableColumn
cfprApTrigLocalAbsWindowProcCap = _CfprApTrigLocalAbsWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 9),
    _CfprApTrigLocalAbsWindowProcCap_Type()
)
cfprApTrigLocalAbsWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowProcCap.setStatus("current")
_CfprApTrigLocalAbsWindowTimeCap_Type = SnmpAdminString
_CfprApTrigLocalAbsWindowTimeCap_Object = MibTableColumn
cfprApTrigLocalAbsWindowTimeCap = _CfprApTrigLocalAbsWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 3, 1, 10),
    _CfprApTrigLocalAbsWindowTimeCap_Type()
)
cfprApTrigLocalAbsWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalAbsWindowTimeCap.setStatus("current")
_CfprApTrigLocalSchedTable_Object = MibTable
cfprApTrigLocalSchedTable = _CfprApTrigLocalSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4)
)
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedTable.setStatus("current")
_CfprApTrigLocalSchedEntry_Object = MibTableRow
cfprApTrigLocalSchedEntry = _CfprApTrigLocalSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1)
)
cfprApTrigLocalSchedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigLocalSchedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedEntry.setStatus("current")
_CfprApTrigLocalSchedInstanceId_Type = CfprApManagedObjectId
_CfprApTrigLocalSchedInstanceId_Object = MibTableColumn
cfprApTrigLocalSchedInstanceId = _CfprApTrigLocalSchedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 1),
    _CfprApTrigLocalSchedInstanceId_Type()
)
cfprApTrigLocalSchedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedInstanceId.setStatus("current")
_CfprApTrigLocalSchedDn_Type = CfprApManagedObjectDn
_CfprApTrigLocalSchedDn_Object = MibTableColumn
cfprApTrigLocalSchedDn = _CfprApTrigLocalSchedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 2),
    _CfprApTrigLocalSchedDn_Type()
)
cfprApTrigLocalSchedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedDn.setStatus("current")
_CfprApTrigLocalSchedRn_Type = SnmpAdminString
_CfprApTrigLocalSchedRn_Object = MibTableColumn
cfprApTrigLocalSchedRn = _CfprApTrigLocalSchedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 3),
    _CfprApTrigLocalSchedRn_Type()
)
cfprApTrigLocalSchedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedRn.setStatus("current")
_CfprApTrigLocalSchedAdminState_Type = CfprApTrigAdminState
_CfprApTrigLocalSchedAdminState_Object = MibTableColumn
cfprApTrigLocalSchedAdminState = _CfprApTrigLocalSchedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 4),
    _CfprApTrigLocalSchedAdminState_Type()
)
cfprApTrigLocalSchedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedAdminState.setStatus("current")
_CfprApTrigLocalSchedDescr_Type = SnmpAdminString
_CfprApTrigLocalSchedDescr_Object = MibTableColumn
cfprApTrigLocalSchedDescr = _CfprApTrigLocalSchedDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 5),
    _CfprApTrigLocalSchedDescr_Type()
)
cfprApTrigLocalSchedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedDescr.setStatus("current")
_CfprApTrigLocalSchedFlgInitialActive_Type = TruthValue
_CfprApTrigLocalSchedFlgInitialActive_Object = MibTableColumn
cfprApTrigLocalSchedFlgInitialActive = _CfprApTrigLocalSchedFlgInitialActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 6),
    _CfprApTrigLocalSchedFlgInitialActive_Type()
)
cfprApTrigLocalSchedFlgInitialActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedFlgInitialActive.setStatus("current")
_CfprApTrigLocalSchedIntId_Type = SnmpAdminString
_CfprApTrigLocalSchedIntId_Object = MibTableColumn
cfprApTrigLocalSchedIntId = _CfprApTrigLocalSchedIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 7),
    _CfprApTrigLocalSchedIntId_Type()
)
cfprApTrigLocalSchedIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedIntId.setStatus("current")
_CfprApTrigLocalSchedName_Type = SnmpAdminString
_CfprApTrigLocalSchedName_Object = MibTableColumn
cfprApTrigLocalSchedName = _CfprApTrigLocalSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 8),
    _CfprApTrigLocalSchedName_Type()
)
cfprApTrigLocalSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedName.setStatus("current")
_CfprApTrigLocalSchedOperState_Type = CfprApTrigOperState
_CfprApTrigLocalSchedOperState_Object = MibTableColumn
cfprApTrigLocalSchedOperState = _CfprApTrigLocalSchedOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 9),
    _CfprApTrigLocalSchedOperState_Type()
)
cfprApTrigLocalSchedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedOperState.setStatus("current")
_CfprApTrigLocalSchedPolicyLevel_Type = Gauge32
_CfprApTrigLocalSchedPolicyLevel_Object = MibTableColumn
cfprApTrigLocalSchedPolicyLevel = _CfprApTrigLocalSchedPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 10),
    _CfprApTrigLocalSchedPolicyLevel_Type()
)
cfprApTrigLocalSchedPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedPolicyLevel.setStatus("current")
_CfprApTrigLocalSchedPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApTrigLocalSchedPolicyOwner_Object = MibTableColumn
cfprApTrigLocalSchedPolicyOwner = _CfprApTrigLocalSchedPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 4, 1, 11),
    _CfprApTrigLocalSchedPolicyOwner_Type()
)
cfprApTrigLocalSchedPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigLocalSchedPolicyOwner.setStatus("current")
_CfprApTrigMetaTable_Object = MibTable
cfprApTrigMetaTable = _CfprApTrigMetaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5)
)
if mibBuilder.loadTexts:
    cfprApTrigMetaTable.setStatus("current")
_CfprApTrigMetaEntry_Object = MibTableRow
cfprApTrigMetaEntry = _CfprApTrigMetaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1)
)
cfprApTrigMetaEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigMetaInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigMetaEntry.setStatus("current")
_CfprApTrigMetaInstanceId_Type = CfprApManagedObjectId
_CfprApTrigMetaInstanceId_Object = MibTableColumn
cfprApTrigMetaInstanceId = _CfprApTrigMetaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 1),
    _CfprApTrigMetaInstanceId_Type()
)
cfprApTrigMetaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigMetaInstanceId.setStatus("current")
_CfprApTrigMetaDn_Type = CfprApManagedObjectDn
_CfprApTrigMetaDn_Object = MibTableColumn
cfprApTrigMetaDn = _CfprApTrigMetaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 2),
    _CfprApTrigMetaDn_Type()
)
cfprApTrigMetaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaDn.setStatus("current")
_CfprApTrigMetaRn_Type = SnmpAdminString
_CfprApTrigMetaRn_Object = MibTableColumn
cfprApTrigMetaRn = _CfprApTrigMetaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 3),
    _CfprApTrigMetaRn_Type()
)
cfprApTrigMetaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaRn.setStatus("current")
_CfprApTrigMetaAdminState_Type = CfprApTrigAdminState
_CfprApTrigMetaAdminState_Object = MibTableColumn
cfprApTrigMetaAdminState = _CfprApTrigMetaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 4),
    _CfprApTrigMetaAdminState_Type()
)
cfprApTrigMetaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaAdminState.setStatus("current")
_CfprApTrigMetaDescr_Type = SnmpAdminString
_CfprApTrigMetaDescr_Object = MibTableColumn
cfprApTrigMetaDescr = _CfprApTrigMetaDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 5),
    _CfprApTrigMetaDescr_Type()
)
cfprApTrigMetaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaDescr.setStatus("current")
_CfprApTrigMetaIntId_Type = SnmpAdminString
_CfprApTrigMetaIntId_Object = MibTableColumn
cfprApTrigMetaIntId = _CfprApTrigMetaIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 6),
    _CfprApTrigMetaIntId_Type()
)
cfprApTrigMetaIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaIntId.setStatus("current")
_CfprApTrigMetaJobCount_Type = Gauge32
_CfprApTrigMetaJobCount_Object = MibTableColumn
cfprApTrigMetaJobCount = _CfprApTrigMetaJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 7),
    _CfprApTrigMetaJobCount_Type()
)
cfprApTrigMetaJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaJobCount.setStatus("current")
_CfprApTrigMetaName_Type = SnmpAdminString
_CfprApTrigMetaName_Object = MibTableColumn
cfprApTrigMetaName = _CfprApTrigMetaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 8),
    _CfprApTrigMetaName_Type()
)
cfprApTrigMetaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaName.setStatus("current")
_CfprApTrigMetaOperState_Type = CfprApTrigOperState
_CfprApTrigMetaOperState_Object = MibTableColumn
cfprApTrigMetaOperState = _CfprApTrigMetaOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 9),
    _CfprApTrigMetaOperState_Type()
)
cfprApTrigMetaOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaOperState.setStatus("current")
_CfprApTrigMetaPolicyLevel_Type = Gauge32
_CfprApTrigMetaPolicyLevel_Object = MibTableColumn
cfprApTrigMetaPolicyLevel = _CfprApTrigMetaPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 10),
    _CfprApTrigMetaPolicyLevel_Type()
)
cfprApTrigMetaPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaPolicyLevel.setStatus("current")
_CfprApTrigMetaPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApTrigMetaPolicyOwner_Object = MibTableColumn
cfprApTrigMetaPolicyOwner = _CfprApTrigMetaPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 11),
    _CfprApTrigMetaPolicyOwner_Type()
)
cfprApTrigMetaPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaPolicyOwner.setStatus("current")
_CfprApTrigMetaSchedName_Type = SnmpAdminString
_CfprApTrigMetaSchedName_Object = MibTableColumn
cfprApTrigMetaSchedName = _CfprApTrigMetaSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 12),
    _CfprApTrigMetaSchedName_Type()
)
cfprApTrigMetaSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaSchedName.setStatus("current")
_CfprApTrigMetaTrigTime_Type = DateAndTime
_CfprApTrigMetaTrigTime_Object = MibTableColumn
cfprApTrigMetaTrigTime = _CfprApTrigMetaTrigTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 13),
    _CfprApTrigMetaTrigTime_Type()
)
cfprApTrigMetaTrigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaTrigTime.setStatus("current")
_CfprApTrigMetaWindowDn_Type = SnmpAdminString
_CfprApTrigMetaWindowDn_Object = MibTableColumn
cfprApTrigMetaWindowDn = _CfprApTrigMetaWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 5, 1, 14),
    _CfprApTrigMetaWindowDn_Type()
)
cfprApTrigMetaWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigMetaWindowDn.setStatus("current")
_CfprApTrigRecurrWindowTable_Object = MibTable
cfprApTrigRecurrWindowTable = _CfprApTrigRecurrWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6)
)
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowTable.setStatus("current")
_CfprApTrigRecurrWindowEntry_Object = MibTableRow
cfprApTrigRecurrWindowEntry = _CfprApTrigRecurrWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1)
)
cfprApTrigRecurrWindowEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigRecurrWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowEntry.setStatus("current")
_CfprApTrigRecurrWindowInstanceId_Type = CfprApManagedObjectId
_CfprApTrigRecurrWindowInstanceId_Object = MibTableColumn
cfprApTrigRecurrWindowInstanceId = _CfprApTrigRecurrWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 1),
    _CfprApTrigRecurrWindowInstanceId_Type()
)
cfprApTrigRecurrWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowInstanceId.setStatus("current")
_CfprApTrigRecurrWindowDn_Type = CfprApManagedObjectDn
_CfprApTrigRecurrWindowDn_Object = MibTableColumn
cfprApTrigRecurrWindowDn = _CfprApTrigRecurrWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 2),
    _CfprApTrigRecurrWindowDn_Type()
)
cfprApTrigRecurrWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowDn.setStatus("current")
_CfprApTrigRecurrWindowRn_Type = SnmpAdminString
_CfprApTrigRecurrWindowRn_Object = MibTableColumn
cfprApTrigRecurrWindowRn = _CfprApTrigRecurrWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 3),
    _CfprApTrigRecurrWindowRn_Type()
)
cfprApTrigRecurrWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowRn.setStatus("current")
_CfprApTrigRecurrWindowConcurCap_Type = Gauge32
_CfprApTrigRecurrWindowConcurCap_Object = MibTableColumn
cfprApTrigRecurrWindowConcurCap = _CfprApTrigRecurrWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 4),
    _CfprApTrigRecurrWindowConcurCap_Type()
)
cfprApTrigRecurrWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowConcurCap.setStatus("current")
_CfprApTrigRecurrWindowDay_Type = CfprApTrigDay
_CfprApTrigRecurrWindowDay_Object = MibTableColumn
cfprApTrigRecurrWindowDay = _CfprApTrigRecurrWindowDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 5),
    _CfprApTrigRecurrWindowDay_Type()
)
cfprApTrigRecurrWindowDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowDay.setStatus("current")
_CfprApTrigRecurrWindowHour_Type = Gauge32
_CfprApTrigRecurrWindowHour_Object = MibTableColumn
cfprApTrigRecurrWindowHour = _CfprApTrigRecurrWindowHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 6),
    _CfprApTrigRecurrWindowHour_Type()
)
cfprApTrigRecurrWindowHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowHour.setStatus("current")
_CfprApTrigRecurrWindowJobCount_Type = Gauge32
_CfprApTrigRecurrWindowJobCount_Object = MibTableColumn
cfprApTrigRecurrWindowJobCount = _CfprApTrigRecurrWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 7),
    _CfprApTrigRecurrWindowJobCount_Type()
)
cfprApTrigRecurrWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowJobCount.setStatus("current")
_CfprApTrigRecurrWindowMinute_Type = Gauge32
_CfprApTrigRecurrWindowMinute_Object = MibTableColumn
cfprApTrigRecurrWindowMinute = _CfprApTrigRecurrWindowMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 8),
    _CfprApTrigRecurrWindowMinute_Type()
)
cfprApTrigRecurrWindowMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowMinute.setStatus("current")
_CfprApTrigRecurrWindowName_Type = SnmpAdminString
_CfprApTrigRecurrWindowName_Object = MibTableColumn
cfprApTrigRecurrWindowName = _CfprApTrigRecurrWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 9),
    _CfprApTrigRecurrWindowName_Type()
)
cfprApTrigRecurrWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowName.setStatus("current")
_CfprApTrigRecurrWindowProcBreak_Type = SnmpAdminString
_CfprApTrigRecurrWindowProcBreak_Object = MibTableColumn
cfprApTrigRecurrWindowProcBreak = _CfprApTrigRecurrWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 10),
    _CfprApTrigRecurrWindowProcBreak_Type()
)
cfprApTrigRecurrWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowProcBreak.setStatus("current")
_CfprApTrigRecurrWindowProcCap_Type = Gauge32
_CfprApTrigRecurrWindowProcCap_Object = MibTableColumn
cfprApTrigRecurrWindowProcCap = _CfprApTrigRecurrWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 11),
    _CfprApTrigRecurrWindowProcCap_Type()
)
cfprApTrigRecurrWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowProcCap.setStatus("current")
_CfprApTrigRecurrWindowTimeCap_Type = SnmpAdminString
_CfprApTrigRecurrWindowTimeCap_Object = MibTableColumn
cfprApTrigRecurrWindowTimeCap = _CfprApTrigRecurrWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 6, 1, 12),
    _CfprApTrigRecurrWindowTimeCap_Type()
)
cfprApTrigRecurrWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigRecurrWindowTimeCap.setStatus("current")
_CfprApTrigSchedTable_Object = MibTable
cfprApTrigSchedTable = _CfprApTrigSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7)
)
if mibBuilder.loadTexts:
    cfprApTrigSchedTable.setStatus("current")
_CfprApTrigSchedEntry_Object = MibTableRow
cfprApTrigSchedEntry = _CfprApTrigSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1)
)
cfprApTrigSchedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigSchedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigSchedEntry.setStatus("current")
_CfprApTrigSchedInstanceId_Type = CfprApManagedObjectId
_CfprApTrigSchedInstanceId_Object = MibTableColumn
cfprApTrigSchedInstanceId = _CfprApTrigSchedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 1),
    _CfprApTrigSchedInstanceId_Type()
)
cfprApTrigSchedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigSchedInstanceId.setStatus("current")
_CfprApTrigSchedDn_Type = CfprApManagedObjectDn
_CfprApTrigSchedDn_Object = MibTableColumn
cfprApTrigSchedDn = _CfprApTrigSchedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 2),
    _CfprApTrigSchedDn_Type()
)
cfprApTrigSchedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedDn.setStatus("current")
_CfprApTrigSchedRn_Type = SnmpAdminString
_CfprApTrigSchedRn_Object = MibTableColumn
cfprApTrigSchedRn = _CfprApTrigSchedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 3),
    _CfprApTrigSchedRn_Type()
)
cfprApTrigSchedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedRn.setStatus("current")
_CfprApTrigSchedAdminState_Type = CfprApTrigAdminState
_CfprApTrigSchedAdminState_Object = MibTableColumn
cfprApTrigSchedAdminState = _CfprApTrigSchedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 4),
    _CfprApTrigSchedAdminState_Type()
)
cfprApTrigSchedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedAdminState.setStatus("current")
_CfprApTrigSchedDescr_Type = SnmpAdminString
_CfprApTrigSchedDescr_Object = MibTableColumn
cfprApTrigSchedDescr = _CfprApTrigSchedDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 5),
    _CfprApTrigSchedDescr_Type()
)
cfprApTrigSchedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedDescr.setStatus("current")
_CfprApTrigSchedFlgInitialActive_Type = TruthValue
_CfprApTrigSchedFlgInitialActive_Object = MibTableColumn
cfprApTrigSchedFlgInitialActive = _CfprApTrigSchedFlgInitialActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 6),
    _CfprApTrigSchedFlgInitialActive_Type()
)
cfprApTrigSchedFlgInitialActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedFlgInitialActive.setStatus("current")
_CfprApTrigSchedIntId_Type = SnmpAdminString
_CfprApTrigSchedIntId_Object = MibTableColumn
cfprApTrigSchedIntId = _CfprApTrigSchedIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 7),
    _CfprApTrigSchedIntId_Type()
)
cfprApTrigSchedIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedIntId.setStatus("current")
_CfprApTrigSchedName_Type = SnmpAdminString
_CfprApTrigSchedName_Object = MibTableColumn
cfprApTrigSchedName = _CfprApTrigSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 8),
    _CfprApTrigSchedName_Type()
)
cfprApTrigSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedName.setStatus("current")
_CfprApTrigSchedOperState_Type = CfprApTrigOperState
_CfprApTrigSchedOperState_Object = MibTableColumn
cfprApTrigSchedOperState = _CfprApTrigSchedOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 9),
    _CfprApTrigSchedOperState_Type()
)
cfprApTrigSchedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedOperState.setStatus("current")
_CfprApTrigSchedPolicyLevel_Type = Gauge32
_CfprApTrigSchedPolicyLevel_Object = MibTableColumn
cfprApTrigSchedPolicyLevel = _CfprApTrigSchedPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 10),
    _CfprApTrigSchedPolicyLevel_Type()
)
cfprApTrigSchedPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedPolicyLevel.setStatus("current")
_CfprApTrigSchedPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApTrigSchedPolicyOwner_Object = MibTableColumn
cfprApTrigSchedPolicyOwner = _CfprApTrigSchedPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 7, 1, 11),
    _CfprApTrigSchedPolicyOwner_Type()
)
cfprApTrigSchedPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigSchedPolicyOwner.setStatus("current")
_CfprApTrigTestTable_Object = MibTable
cfprApTrigTestTable = _CfprApTrigTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8)
)
if mibBuilder.loadTexts:
    cfprApTrigTestTable.setStatus("current")
_CfprApTrigTestEntry_Object = MibTableRow
cfprApTrigTestEntry = _CfprApTrigTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1)
)
cfprApTrigTestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigTestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigTestEntry.setStatus("current")
_CfprApTrigTestInstanceId_Type = CfprApManagedObjectId
_CfprApTrigTestInstanceId_Object = MibTableColumn
cfprApTrigTestInstanceId = _CfprApTrigTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 1),
    _CfprApTrigTestInstanceId_Type()
)
cfprApTrigTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigTestInstanceId.setStatus("current")
_CfprApTrigTestDn_Type = CfprApManagedObjectDn
_CfprApTrigTestDn_Object = MibTableColumn
cfprApTrigTestDn = _CfprApTrigTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 2),
    _CfprApTrigTestDn_Type()
)
cfprApTrigTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestDn.setStatus("current")
_CfprApTrigTestRn_Type = SnmpAdminString
_CfprApTrigTestRn_Object = MibTableColumn
cfprApTrigTestRn = _CfprApTrigTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 3),
    _CfprApTrigTestRn_Type()
)
cfprApTrigTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestRn.setStatus("current")
_CfprApTrigTestAdminState_Type = CfprApTrigAdminState
_CfprApTrigTestAdminState_Object = MibTableColumn
cfprApTrigTestAdminState = _CfprApTrigTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 4),
    _CfprApTrigTestAdminState_Type()
)
cfprApTrigTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestAdminState.setStatus("current")
_CfprApTrigTestAutoDelete_Type = TruthValue
_CfprApTrigTestAutoDelete_Object = MibTableColumn
cfprApTrigTestAutoDelete = _CfprApTrigTestAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 5),
    _CfprApTrigTestAutoDelete_Type()
)
cfprApTrigTestAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestAutoDelete.setStatus("current")
_CfprApTrigTestCreationDate_Type = DateAndTime
_CfprApTrigTestCreationDate_Object = MibTableColumn
cfprApTrigTestCreationDate = _CfprApTrigTestCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 6),
    _CfprApTrigTestCreationDate_Type()
)
cfprApTrigTestCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestCreationDate.setStatus("current")
_CfprApTrigTestDescr_Type = SnmpAdminString
_CfprApTrigTestDescr_Object = MibTableColumn
cfprApTrigTestDescr = _CfprApTrigTestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 7),
    _CfprApTrigTestDescr_Type()
)
cfprApTrigTestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestDescr.setStatus("current")
_CfprApTrigTestIgnoreCap_Type = TruthValue
_CfprApTrigTestIgnoreCap_Object = MibTableColumn
cfprApTrigTestIgnoreCap = _CfprApTrigTestIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 8),
    _CfprApTrigTestIgnoreCap_Type()
)
cfprApTrigTestIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestIgnoreCap.setStatus("current")
_CfprApTrigTestIntId_Type = SnmpAdminString
_CfprApTrigTestIntId_Object = MibTableColumn
cfprApTrigTestIntId = _CfprApTrigTestIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 9),
    _CfprApTrigTestIntId_Type()
)
cfprApTrigTestIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestIntId.setStatus("current")
_CfprApTrigTestName_Type = SnmpAdminString
_CfprApTrigTestName_Object = MibTableColumn
cfprApTrigTestName = _CfprApTrigTestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 10),
    _CfprApTrigTestName_Type()
)
cfprApTrigTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestName.setStatus("current")
_CfprApTrigTestOperScheduler_Type = SnmpAdminString
_CfprApTrigTestOperScheduler_Object = MibTableColumn
cfprApTrigTestOperScheduler = _CfprApTrigTestOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 11),
    _CfprApTrigTestOperScheduler_Type()
)
cfprApTrigTestOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestOperScheduler.setStatus("current")
_CfprApTrigTestOperState_Type = CfprApTrigTrigOperState
_CfprApTrigTestOperState_Object = MibTableColumn
cfprApTrigTestOperState = _CfprApTrigTestOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 12),
    _CfprApTrigTestOperState_Type()
)
cfprApTrigTestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestOperState.setStatus("current")
_CfprApTrigTestPolicyLevel_Type = Gauge32
_CfprApTrigTestPolicyLevel_Object = MibTableColumn
cfprApTrigTestPolicyLevel = _CfprApTrigTestPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 13),
    _CfprApTrigTestPolicyLevel_Type()
)
cfprApTrigTestPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestPolicyLevel.setStatus("current")
_CfprApTrigTestPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApTrigTestPolicyOwner_Object = MibTableColumn
cfprApTrigTestPolicyOwner = _CfprApTrigTestPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 14),
    _CfprApTrigTestPolicyOwner_Type()
)
cfprApTrigTestPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestPolicyOwner.setStatus("current")
_CfprApTrigTestScheduler_Type = SnmpAdminString
_CfprApTrigTestScheduler_Object = MibTableColumn
cfprApTrigTestScheduler = _CfprApTrigTestScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 8, 1, 15),
    _CfprApTrigTestScheduler_Type()
)
cfprApTrigTestScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTestScheduler.setStatus("current")
_CfprApTrigTriggeredTable_Object = MibTable
cfprApTrigTriggeredTable = _CfprApTrigTriggeredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9)
)
if mibBuilder.loadTexts:
    cfprApTrigTriggeredTable.setStatus("current")
_CfprApTrigTriggeredEntry_Object = MibTableRow
cfprApTrigTriggeredEntry = _CfprApTrigTriggeredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1)
)
cfprApTrigTriggeredEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TRIG-MIB", "cfprApTrigTriggeredInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTrigTriggeredEntry.setStatus("current")
_CfprApTrigTriggeredInstanceId_Type = CfprApManagedObjectId
_CfprApTrigTriggeredInstanceId_Object = MibTableColumn
cfprApTrigTriggeredInstanceId = _CfprApTrigTriggeredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 1),
    _CfprApTrigTriggeredInstanceId_Type()
)
cfprApTrigTriggeredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredInstanceId.setStatus("current")
_CfprApTrigTriggeredDn_Type = CfprApManagedObjectDn
_CfprApTrigTriggeredDn_Object = MibTableColumn
cfprApTrigTriggeredDn = _CfprApTrigTriggeredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 2),
    _CfprApTrigTriggeredDn_Type()
)
cfprApTrigTriggeredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredDn.setStatus("current")
_CfprApTrigTriggeredRn_Type = SnmpAdminString
_CfprApTrigTriggeredRn_Object = MibTableColumn
cfprApTrigTriggeredRn = _CfprApTrigTriggeredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 3),
    _CfprApTrigTriggeredRn_Type()
)
cfprApTrigTriggeredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredRn.setStatus("current")
_CfprApTrigTriggeredJobCount_Type = Gauge32
_CfprApTrigTriggeredJobCount_Object = MibTableColumn
cfprApTrigTriggeredJobCount = _CfprApTrigTriggeredJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 4),
    _CfprApTrigTriggeredJobCount_Type()
)
cfprApTrigTriggeredJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredJobCount.setStatus("current")
_CfprApTrigTriggeredOperState_Type = CfprApTrigTriggeredState
_CfprApTrigTriggeredOperState_Object = MibTableColumn
cfprApTrigTriggeredOperState = _CfprApTrigTriggeredOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 5),
    _CfprApTrigTriggeredOperState_Type()
)
cfprApTrigTriggeredOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredOperState.setStatus("current")
_CfprApTrigTriggeredOrder_Type = Gauge32
_CfprApTrigTriggeredOrder_Object = MibTableColumn
cfprApTrigTriggeredOrder = _CfprApTrigTriggeredOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 6),
    _CfprApTrigTriggeredOrder_Type()
)
cfprApTrigTriggeredOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredOrder.setStatus("current")
_CfprApTrigTriggeredTrDn_Type = SnmpAdminString
_CfprApTrigTriggeredTrDn_Object = MibTableColumn
cfprApTrigTriggeredTrDn = _CfprApTrigTriggeredTrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 7),
    _CfprApTrigTriggeredTrDn_Type()
)
cfprApTrigTriggeredTrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredTrDn.setStatus("current")
_CfprApTrigTriggeredTrId_Type = Gauge32
_CfprApTrigTriggeredTrId_Object = MibTableColumn
cfprApTrigTriggeredTrId = _CfprApTrigTriggeredTrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 79, 9, 1, 8),
    _CfprApTrigTriggeredTrId_Type()
)
cfprApTrigTriggeredTrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTrigTriggeredTrId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-TRIG-MIB",
    **{"cfprApTrigObjects": cfprApTrigObjects,
       "cfprApTrigAbsWindowTable": cfprApTrigAbsWindowTable,
       "cfprApTrigAbsWindowEntry": cfprApTrigAbsWindowEntry,
       "cfprApTrigAbsWindowInstanceId": cfprApTrigAbsWindowInstanceId,
       "cfprApTrigAbsWindowDn": cfprApTrigAbsWindowDn,
       "cfprApTrigAbsWindowRn": cfprApTrigAbsWindowRn,
       "cfprApTrigAbsWindowConcurCap": cfprApTrigAbsWindowConcurCap,
       "cfprApTrigAbsWindowDate": cfprApTrigAbsWindowDate,
       "cfprApTrigAbsWindowJobCount": cfprApTrigAbsWindowJobCount,
       "cfprApTrigAbsWindowName": cfprApTrigAbsWindowName,
       "cfprApTrigAbsWindowProcBreak": cfprApTrigAbsWindowProcBreak,
       "cfprApTrigAbsWindowProcCap": cfprApTrigAbsWindowProcCap,
       "cfprApTrigAbsWindowTimeCap": cfprApTrigAbsWindowTimeCap,
       "cfprApTrigClientTokenTable": cfprApTrigClientTokenTable,
       "cfprApTrigClientTokenEntry": cfprApTrigClientTokenEntry,
       "cfprApTrigClientTokenInstanceId": cfprApTrigClientTokenInstanceId,
       "cfprApTrigClientTokenDn": cfprApTrigClientTokenDn,
       "cfprApTrigClientTokenRn": cfprApTrigClientTokenRn,
       "cfprApTrigClientTokenActivityTs": cfprApTrigClientTokenActivityTs,
       "cfprApTrigClientTokenId": cfprApTrigClientTokenId,
       "cfprApTrigClientTokenOperState": cfprApTrigClientTokenOperState,
       "cfprApTrigLocalAbsWindowTable": cfprApTrigLocalAbsWindowTable,
       "cfprApTrigLocalAbsWindowEntry": cfprApTrigLocalAbsWindowEntry,
       "cfprApTrigLocalAbsWindowInstanceId": cfprApTrigLocalAbsWindowInstanceId,
       "cfprApTrigLocalAbsWindowDn": cfprApTrigLocalAbsWindowDn,
       "cfprApTrigLocalAbsWindowRn": cfprApTrigLocalAbsWindowRn,
       "cfprApTrigLocalAbsWindowConcurCap": cfprApTrigLocalAbsWindowConcurCap,
       "cfprApTrigLocalAbsWindowDate": cfprApTrigLocalAbsWindowDate,
       "cfprApTrigLocalAbsWindowJobCount": cfprApTrigLocalAbsWindowJobCount,
       "cfprApTrigLocalAbsWindowName": cfprApTrigLocalAbsWindowName,
       "cfprApTrigLocalAbsWindowProcBreak": cfprApTrigLocalAbsWindowProcBreak,
       "cfprApTrigLocalAbsWindowProcCap": cfprApTrigLocalAbsWindowProcCap,
       "cfprApTrigLocalAbsWindowTimeCap": cfprApTrigLocalAbsWindowTimeCap,
       "cfprApTrigLocalSchedTable": cfprApTrigLocalSchedTable,
       "cfprApTrigLocalSchedEntry": cfprApTrigLocalSchedEntry,
       "cfprApTrigLocalSchedInstanceId": cfprApTrigLocalSchedInstanceId,
       "cfprApTrigLocalSchedDn": cfprApTrigLocalSchedDn,
       "cfprApTrigLocalSchedRn": cfprApTrigLocalSchedRn,
       "cfprApTrigLocalSchedAdminState": cfprApTrigLocalSchedAdminState,
       "cfprApTrigLocalSchedDescr": cfprApTrigLocalSchedDescr,
       "cfprApTrigLocalSchedFlgInitialActive": cfprApTrigLocalSchedFlgInitialActive,
       "cfprApTrigLocalSchedIntId": cfprApTrigLocalSchedIntId,
       "cfprApTrigLocalSchedName": cfprApTrigLocalSchedName,
       "cfprApTrigLocalSchedOperState": cfprApTrigLocalSchedOperState,
       "cfprApTrigLocalSchedPolicyLevel": cfprApTrigLocalSchedPolicyLevel,
       "cfprApTrigLocalSchedPolicyOwner": cfprApTrigLocalSchedPolicyOwner,
       "cfprApTrigMetaTable": cfprApTrigMetaTable,
       "cfprApTrigMetaEntry": cfprApTrigMetaEntry,
       "cfprApTrigMetaInstanceId": cfprApTrigMetaInstanceId,
       "cfprApTrigMetaDn": cfprApTrigMetaDn,
       "cfprApTrigMetaRn": cfprApTrigMetaRn,
       "cfprApTrigMetaAdminState": cfprApTrigMetaAdminState,
       "cfprApTrigMetaDescr": cfprApTrigMetaDescr,
       "cfprApTrigMetaIntId": cfprApTrigMetaIntId,
       "cfprApTrigMetaJobCount": cfprApTrigMetaJobCount,
       "cfprApTrigMetaName": cfprApTrigMetaName,
       "cfprApTrigMetaOperState": cfprApTrigMetaOperState,
       "cfprApTrigMetaPolicyLevel": cfprApTrigMetaPolicyLevel,
       "cfprApTrigMetaPolicyOwner": cfprApTrigMetaPolicyOwner,
       "cfprApTrigMetaSchedName": cfprApTrigMetaSchedName,
       "cfprApTrigMetaTrigTime": cfprApTrigMetaTrigTime,
       "cfprApTrigMetaWindowDn": cfprApTrigMetaWindowDn,
       "cfprApTrigRecurrWindowTable": cfprApTrigRecurrWindowTable,
       "cfprApTrigRecurrWindowEntry": cfprApTrigRecurrWindowEntry,
       "cfprApTrigRecurrWindowInstanceId": cfprApTrigRecurrWindowInstanceId,
       "cfprApTrigRecurrWindowDn": cfprApTrigRecurrWindowDn,
       "cfprApTrigRecurrWindowRn": cfprApTrigRecurrWindowRn,
       "cfprApTrigRecurrWindowConcurCap": cfprApTrigRecurrWindowConcurCap,
       "cfprApTrigRecurrWindowDay": cfprApTrigRecurrWindowDay,
       "cfprApTrigRecurrWindowHour": cfprApTrigRecurrWindowHour,
       "cfprApTrigRecurrWindowJobCount": cfprApTrigRecurrWindowJobCount,
       "cfprApTrigRecurrWindowMinute": cfprApTrigRecurrWindowMinute,
       "cfprApTrigRecurrWindowName": cfprApTrigRecurrWindowName,
       "cfprApTrigRecurrWindowProcBreak": cfprApTrigRecurrWindowProcBreak,
       "cfprApTrigRecurrWindowProcCap": cfprApTrigRecurrWindowProcCap,
       "cfprApTrigRecurrWindowTimeCap": cfprApTrigRecurrWindowTimeCap,
       "cfprApTrigSchedTable": cfprApTrigSchedTable,
       "cfprApTrigSchedEntry": cfprApTrigSchedEntry,
       "cfprApTrigSchedInstanceId": cfprApTrigSchedInstanceId,
       "cfprApTrigSchedDn": cfprApTrigSchedDn,
       "cfprApTrigSchedRn": cfprApTrigSchedRn,
       "cfprApTrigSchedAdminState": cfprApTrigSchedAdminState,
       "cfprApTrigSchedDescr": cfprApTrigSchedDescr,
       "cfprApTrigSchedFlgInitialActive": cfprApTrigSchedFlgInitialActive,
       "cfprApTrigSchedIntId": cfprApTrigSchedIntId,
       "cfprApTrigSchedName": cfprApTrigSchedName,
       "cfprApTrigSchedOperState": cfprApTrigSchedOperState,
       "cfprApTrigSchedPolicyLevel": cfprApTrigSchedPolicyLevel,
       "cfprApTrigSchedPolicyOwner": cfprApTrigSchedPolicyOwner,
       "cfprApTrigTestTable": cfprApTrigTestTable,
       "cfprApTrigTestEntry": cfprApTrigTestEntry,
       "cfprApTrigTestInstanceId": cfprApTrigTestInstanceId,
       "cfprApTrigTestDn": cfprApTrigTestDn,
       "cfprApTrigTestRn": cfprApTrigTestRn,
       "cfprApTrigTestAdminState": cfprApTrigTestAdminState,
       "cfprApTrigTestAutoDelete": cfprApTrigTestAutoDelete,
       "cfprApTrigTestCreationDate": cfprApTrigTestCreationDate,
       "cfprApTrigTestDescr": cfprApTrigTestDescr,
       "cfprApTrigTestIgnoreCap": cfprApTrigTestIgnoreCap,
       "cfprApTrigTestIntId": cfprApTrigTestIntId,
       "cfprApTrigTestName": cfprApTrigTestName,
       "cfprApTrigTestOperScheduler": cfprApTrigTestOperScheduler,
       "cfprApTrigTestOperState": cfprApTrigTestOperState,
       "cfprApTrigTestPolicyLevel": cfprApTrigTestPolicyLevel,
       "cfprApTrigTestPolicyOwner": cfprApTrigTestPolicyOwner,
       "cfprApTrigTestScheduler": cfprApTrigTestScheduler,
       "cfprApTrigTriggeredTable": cfprApTrigTriggeredTable,
       "cfprApTrigTriggeredEntry": cfprApTrigTriggeredEntry,
       "cfprApTrigTriggeredInstanceId": cfprApTrigTriggeredInstanceId,
       "cfprApTrigTriggeredDn": cfprApTrigTriggeredDn,
       "cfprApTrigTriggeredRn": cfprApTrigTriggeredRn,
       "cfprApTrigTriggeredJobCount": cfprApTrigTriggeredJobCount,
       "cfprApTrigTriggeredOperState": cfprApTrigTriggeredOperState,
       "cfprApTrigTriggeredOrder": cfprApTrigTriggeredOrder,
       "cfprApTrigTriggeredTrDn": cfprApTrigTriggeredTrDn,
       "cfprApTrigTriggeredTrId": cfprApTrigTriggeredTrId}
)
